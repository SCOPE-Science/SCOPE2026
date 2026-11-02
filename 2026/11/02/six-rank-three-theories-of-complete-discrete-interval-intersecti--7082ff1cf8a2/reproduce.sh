#!/bin/sh
set -eu
D="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT HUP INT TERM
${CXX:-c++} -O2 -std=c++17 "$D/interval_types.cpp" -o "$TMP/interval_types"
"$TMP/interval_types" 26 > "$TMP/interval_types_output.txt"
diff -u "$D/interval_types_output.txt" "$TMP/interval_types_output.txt"
python3 "$D/independent_types.py" 12 > "$TMP/independent_types_output.txt"
diff -u "$D/independent_types_output.txt" "$TMP/independent_types_output.txt"
python3 "$D/witness.py" > "$TMP/witness_output.txt"
diff -u "$D/witness_output.txt" "$TMP/witness_output.txt"
printf 'ALL_REPRODUCTION_CHECKS_PASSED\n'
