#!/bin/sh
set -eu
cd "$(dirname "$0")"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT HUP INT TERM
cc -O3 -std=c11 count.c -o "$TMP/count"
cc -O3 -std=c11 direct16.c -o "$TMP/direct16"
cc -O3 -std=c11 orbits.c -o "$TMP/orbits"
"$TMP/count" --pairs > "$TMP/a"
"$TMP/direct16" --pairs > "$TMP/b"
grep '^PAIR ' "$TMP/a" > "$TMP/ap"
grep '^PAIR ' "$TMP/b" > "$TMP/bp"
cmp "$TMP/ap" "$TMP/bp"
[ "$(wc -l < "$TMP/ap")" -eq 40320 ]
"$TMP/orbits" > "$TMP/orbitdata"
grep '^orbits 8$' "$TMP/orbitdata"
tail -n 6 "$TMP/a"
tail -n 6 "$TMP/b"
cat "$TMP/orbitdata"
echo VERIFIED_MATCHED_40320
