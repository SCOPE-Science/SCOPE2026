#!/usr/bin/env python3
"""Independent affine-coordinate verifier (different points, lines and blocker enumeration)."""
from itertools import combinations
from collections import Counter
from functools import lru_cache
q=3
# Point labels 0..8 are affine pairs (x,y), 9,10,11 slopes 0,1,2,
# and 12 the vertical direction. Each affine line has its point at infinity.
lines=[]
for slope in range(3):
    for intercept in range(3):
        pts=[3*x+y for x in range(3) for y in range(3)
             if (y-slope*x)%3==intercept]
        pts.append(9+slope)
        lines.append(frozenset(pts))
for x in range(3):
    lines.append(frozenset([3*x+y for y in range(3)]+[12]))
lines.append(frozenset(range(9,13)))
assert len(lines)==13 and len(set(lines))==13
assert all(len(L)==4 for L in lines)
assert all(len(A&B)==1 for A,B in combinations(lines,2))
L=[sum(1<<i for i in l) for l in lines]

# Enumerate minimal hitting sets via *deletion*: a hitting set is minimal
# precisely when deleting any of its members destroys the hitting property.
def hits(S):return all(S&l for l in L)
H=[]
for S in range(1<<13):
    if not hits(S):continue
    if any(hits(S&~(1<<i)) for i in range(13) if S>>i&1):continue
    H.append(S)
assert len(H)==247 and Counter(S.bit_count() for S in H)=={4:13,6:234}

for k,expected in [(4,{15:13,16:702}),(5,{29:117,31:468,32:702}),(6,{56:468,57:78,60:936,61:234})]:
    spectrum=Counter()
    for supp in combinations(range(13),k):
        trace=set()
        for S in H:
            p=0
            for j,i in enumerate(supp):
                if S>>i&1:p|=1<<j
            trace.add(p)
        spectrum[len(trace)]+=1
    assert spectrum==expected,(k,spectrum)
print('AFFINE_COORDINATE_INDEPENDENT_SPECTRA_PASS')

# Independent exact minimax recurrence, without certificate or primary code.
Q=[sum(1<<j for j,S in enumerate(H) if S>>i&1) for i in range(13)]
@lru_cache(None)
def rank(V):
    best=0
    for q in Q:
        a=V&q;b=V&~q
        if a and b:
            cand=1+min(rank(a),rank(b))
            if cand>best:best=cand
    return best
r=rank((1<<len(H))-1)
assert r==6
print('AFFINE_COORDINATE_INDEPENDENT_ONLINE_RANK_PASS rank=6 states='+str(rank.cache_info().currsize))
print('ALL_AFFINE_INDEPENDENT_CHECKS_PASS')
