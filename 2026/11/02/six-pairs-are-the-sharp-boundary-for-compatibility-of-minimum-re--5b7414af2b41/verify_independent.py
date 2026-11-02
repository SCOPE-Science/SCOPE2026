#!/usr/bin/env python3
"""Independent bitmask-based exhaustive stability and score certificate."""
from itertools import permutations
from verify_witness import MEN, WOMEN
N = len(MEN)


def better_mask(order, choice):
    mask = 0
    for v in order:
        if v == choice:
            return mask
        mask |= 1 << v
    raise AssertionError('invalid preference list')


rows=[]
for assignment in permutations(range(N)):
    inv=[0]*N
    for i,j in enumerate(assignment): inv[j]=i
    # Any unmatched man-woman pair that has a bit in both masks blocks.
    bm=[better_mask(MEN[i],assignment[i]) for i in range(N)]
    bw=[better_mask(WOMEN[j],inv[j]) for j in range(N)]
    all_good=all(not ((bm[i] >> j) & 1 and (bw[j] >> i) & 1)
                 for i in range(N) for j in range(N) if j != assignment[i])
    if not all_good:continue
    # Distinct scoring routine based on inverse-position arrays
    rm=[{w:r for r,w in enumerate(pref,1)} for pref in MEN]
    rw=[{i:r for r,i in enumerate(pref,1)} for pref in WOMEN]
    values=[rm[i][assignment[i]] for i in range(N)]+[rw[j][inv[j]] for j in range(N)]
    rows.append((assignment,min(values),max(values)))
assert len(rows)==7
assert min(top-bottom for _,bottom,top in rows)==2
assert min(top for _,_,top in rows)==4
assert [x[0] for x in rows if x[2]-x[1]==2]==[(0,1,2,3,4,5)]
assert [x[0] for x in rows if x[2]==4]==[(1,0,2,3,4,5)]
print('PASS: independent mask enumeration',len(rows),'stable of',720)
