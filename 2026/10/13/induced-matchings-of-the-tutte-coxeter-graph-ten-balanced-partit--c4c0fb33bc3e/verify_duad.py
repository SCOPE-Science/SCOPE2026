#!/usr/bin/env python3
"""Exact point-subset proof-checker for induced matchings of the duad-syntheme graph."""
from itertools import combinations, product
from collections import Counter
from math import prod
from pathlib import Path
import csv

U = tuple(range(6))
P = tuple(combinations(U, 2))
def rec(V):
    if not V:
        yield ()
    else:
        x = V[0]
        for y in V[1:]:
            for T in rec(tuple(z for z in V[1:] if z != y)):
                yield ((x,y),) + T
L = tuple(sorted(tuple(sorted(M)) for M in rec(U)))
assert len(P) == len(L) == 15 and len(set(L)) == 15
pb = {p: i for i,p in enumerate(P)}
line_masks = tuple(sum(1 << pb[e] for e in line) for line in L)
incident = tuple(tuple(j for j, lm in enumerate(line_masks) if lm & (1 << i)) for i in range(15))
coefs, maximal, ext = Counter(), Counter(), Counter()
max_sets = set()
for S in range(1 << 15):
    ps = tuple(p for p in range(15) if S & (1 << p))
    free = [tuple(j for j in incident[p] if line_masks[j] & S == 1 << p) for p in ps]
    c = prod(map(len, free))
    coefs[len(ps)] += c
    if not c:
        continue
    available = sum(1 << p for p in range(15) if not (S >> p & 1)
                    and any(line_masks[j] & S == 0 for j in incident[p]))
    for chosen in product(*free):
        occupied = 0
        for j in chosen:
            occupied |= line_masks[j]
        ext_count = sum(sum(line_masks[j] & S == 0 for j in incident[p])
                        for p in range(15)
                        if not (S >> p & 1) and not (occupied >> p & 1))
        ext[(len(ps), ext_count)] += 1
        if ext_count == 0:
            maximal[len(ps)] += 1
        if len(ps) == 9:
            max_sets.add(frozenset(zip(ps, chosen)))
# Distinguish geometric optimum family from any other 9-matchings.
canonical = set()
for A0 in combinations(U, 3):
    A = set(A0)
    B = set(U)-A
    # Use a canonical unordered 3+3 partition.
    if 0 not in A:
        continue
    pattern = frozenset((pb[(a,b) if a < b else (b,a)],
        L.index(tuple(sorted((((a,b) if a < b else (b,a)), tuple(sorted(A-{a})), tuple(sorted(B-{b})))))))
        for a in A for b in B)
    canonical.add(pattern)
assert len(canonical) == 10 and canonical == max_sets
assert dict(sorted(coefs.items())) == {0:1,1:45,2:720,3:5160,4:16920,5:22680,6:8520,7:720,8:90,9:10,10:0,11:0,12:0,13:0,14:0,15:0}
assert dict(maximal) == {5:3060,6:5520,7:360,9:10}
assert ext[(8, 1)] == 90 and sum(v for (k,c), v in ext.items() if k==8 and c!=1)==0
assert ext[(9, 0)] == 10
root=Path(__file__).resolve().parent
with (root/'spectrum.csv').open(newline='',encoding='utf8') as f:
    rows=list(csv.DictReader(f))
assert len(rows)==10
for row in rows:
    k=int(row['edges'])
    assert int(row['induced_matchings'])==coefs[k]
    assert int(row['inclusion_maximal_induced_matchings'])==maximal[k]
with (root/'maxima.csv').open(newline='',encoding='utf8') as f:
    rows=list(csv.DictReader(f))
recorded=set(frozenset(tuple(map(int,flag.split(':'))) for flag in row['nine_flags_duad_idx:syntheme_idx'].split(';')) for row in rows)
assert len(rows)==10 and recorded==max_sets
print('VERIFY_POINT_OK duads=15 synthemes=15 flags=45 subsets=32768')
print('VERIFY_POINT_OK polynomial=1,45,720,5160,16920,22680,8520,720,90,10 total=54866')
print('VERIFY_POINT_OK inclusion_maximal=5:3060,6:5520,7:360,9:10')
print('VERIFY_POINT_OK size8=90 all_uniquely_extend_to_size9=true')
print('VERIFY_POINT_OK all_10_maxima_are_3plus3_partitions_of_six=true')
