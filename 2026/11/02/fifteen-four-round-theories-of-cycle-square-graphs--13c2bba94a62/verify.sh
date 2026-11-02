#!/bin/sh
set -eu
here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT HUP INT TERM
c++ -O2 -std=c++17 "$here/cycle2_orbit.cpp" -o "$work/orbit"
c++ -O2 -std=c++17 "$here/cycle2_direct.cpp" -o "$work/direct"
"$work/orbit" 72 > "$work/orbit.csv" 2> "$work/orbit.log"
"$work/direct" 32 > "$work/direct.csv" 2> "$work/direct.log"
python3 - "$work/orbit.csv" "$work/direct.csv" "$here/class_table.csv" <<'PY'
import itertools,sys,csv

def load(p):
    t=[]
    for l in open(p,encoding='ascii'):
        a,b=l.strip().split(',')
        t.append((int(a),int(b)))
    return dict(t)
a,b=load(sys.argv[1]),load(sys.argv[2])
assert sorted(a)==list(range(5,73)), 'orbit range'
assert sorted(b)==list(range(5,33)), 'direct range'
assert len({a[n] for n in range(5,19)})==14, '14 exceptional types'
assert len({a[n] for n in range(5,73)})==15, '15 total types'
assert all(a[n]==a[19] for n in range(19,73)), 'stabilization through 72'
assert all(a[n]!=a[19] for n in range(5,19)), 'sharp threshold'
with open(sys.argv[3],newline='',encoding='utf-8') as fh:
    rows=list(csv.DictReader(fh))
assert len(rows)==28
for row in rows:
    n=int(row['n'])
    assert int(row['orbit_type_id'])==a[n]
    assert int(row['direct_type_id'])==b[n]
    assert row['rank4_class']==(f'n{n}' if n<19 else 'tail')
for i in range(5,33):
    for j in range(5,33):
        assert (a[i]==a[j]) == (b[i]==b[j]), ('independent comparison',i,j)
print('ORBIT_AND_DIRECT_RANK4_CLASSIFICATION_OK')
print('fifteen_classes_on_n_ge_5; singleton_n_5_to_18; common_tail_from_19')
print('orbit_checked_n_5_to_72; direct_checked_n_5_to_32')
# A secondary observation: four distinct selected vertices exhibit the same
# ordered adjacency patterns for all n>=12 in the finite interval below.
def patterns(n):
    out=set()
    for x in itertools.combinations(range(n),4):
        out.add(tuple(int(min(abs(x[i]-x[j]),n-abs(x[i]-x[j])) <= 2)
                      for i in range(4) for j in range(i+1,4)))
    return out
p=patterns(12)
assert len(p)==31
assert all(patterns(n)==p for n in range(12,41))
print('FOUR_VERTEX_PATTERN_STABILITY_CHECK_OK: 31 ordered-increasing patterns at n=12..40')
PY
