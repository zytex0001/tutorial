import discord
from discord.ext import commands

bot=commands.Bot(command_prefix="?")

@bot.event
async def on_ready():
    print("Ich bin jetzt online")

@bot.command()
async def test(ctx):
  await ctx.send("Bestanden")

bot.run("TOKEN")
