#!/bin/sh
set -eu
cd "$(dirname "$0")"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT HUP INT TERM
c++ -std=c++17 -O3 tri_types.cpp -o "$tmp/tri_types"
"$tmp/tri_types" 26 > "$tmp/tri_results26.txt"
python3 tri_independent.py 12 > "$tmp/tri_py12.txt"
diff -u tri_results26.txt "$tmp/tri_results26.txt"
diff -u tri_py12.txt "$tmp/tri_py12.txt"
printf 'All exact finite comparisons passed.\n'
