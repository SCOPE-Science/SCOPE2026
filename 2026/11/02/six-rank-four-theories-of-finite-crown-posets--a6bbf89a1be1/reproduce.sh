#!/bin/sh
set -eu
cd "$(dirname "$0")"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT HUP INT TERM
c++ -O3 -std=c++17 verify_types.cpp -o "$tmp/crown_types"
"$tmp/crown_types" 15 > "$tmp/cpp.out" 2> "$tmp/cpp.timings"
python3 verify_types.py 15 > "$tmp/python.out"
awk '{print $1, $2}' "$tmp/cpp.out" > "$tmp/cpp.classes"
awk '{print $1, $2}' "$tmp/python.out" > "$tmp/python.classes"
diff -u "$tmp/cpp.classes" "$tmp/python.classes"
cat "$tmp/cpp.classes"
if test "$(awk '$1>=7 {print $2}' "$tmp/cpp.classes" | sort -u | wc -l)" -ne 1; then exit 1; fi
if test "$(awk '$1>=2 && $1<=7 {print $2}' "$tmp/cpp.classes" | sort -u | wc -l)" -ne 6; then exit 1; fi
python3 verify_gap.py
echo 'TWO_IMPLEMENTATIONS_AGREE; SIX_CLASSES_IN_TESTED_RANGE; TAIL_7_TO_15_AGREES'
