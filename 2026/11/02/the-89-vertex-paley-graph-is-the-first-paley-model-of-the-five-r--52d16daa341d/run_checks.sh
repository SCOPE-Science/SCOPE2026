#!/bin/sh
set -eu
cd "$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
python3 verify_paley89.py
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT HUP INT TERM
g++ -std=c++17 -O3 verify_paley89_direct.cpp -o "$tmp/paley_four_ec"
"$tmp/paley_four_ec"
