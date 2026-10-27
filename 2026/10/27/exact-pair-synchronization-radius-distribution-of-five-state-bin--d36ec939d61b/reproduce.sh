#!/bin/sh
# Reproduce the exhaustive pair-synchronization-radius census.
set -eu
cd "$(dirname "$0")"
TMPDIR_REPLAY=$(mktemp -d)
trap 'rm -rf "$TMPDIR_REPLAY"' EXIT HUP INT TERM
c++ -O3 -std=c++17 forward_levels.cpp -o "$TMPDIR_REPLAY/forward"
c++ -O3 -std=c++17 reverse_bfs.cpp -o "$TMPDIR_REPLAY/reverse"
"$TMPDIR_REPLAY/forward" > "$TMPDIR_REPLAY/forward.txt"
"$TMPDIR_REPLAY/reverse" > "$TMPDIR_REPLAY/reverse.txt"
python3 check_witness.py
python3 - "$TMPDIR_REPLAY/forward.txt" "$TMPDIR_REPLAY/reverse.txt" <<'PY'
import pathlib,sys,csv
f=pathlib.Path(sys.argv[1]).read_text()
r=pathlib.Path(sys.argv[2]).read_text()
with open('pair_radius_counts.csv',newline='') as inp:
    expected={int(t['pair_radius']):int(t['labeled_automata']) for t in csv.DictReader(inp)}
for d,n in expected.items():
    assert f'\n{d} {n}\n' in '\n'+f, (d,n,'forward')
    assert f'\n{d} {n}\n' in '\n'+r, (d,n,'reverse')
assert 'SYNC 8063385 NON 1702240 MAX 10' in f
assert 'non 1702240' in r
assert 'extreme_count 240' in r
assert 'orbit_size 240 equal 1' in r
assert 'VERIFY_OK' in r
print('VERIFY_OK: two complete enumerations agree with the exact distribution and orbit check')
PY
