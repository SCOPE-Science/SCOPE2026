#!/usr/bin/env python3
from math import comb

X=set(range(1,7))
edges=[
    ({1,3,6},{3,4,6}),
    ({2,5,6},{3,5,6}),
    ({1,2,6},{2,4,6}),
    ({1,5,6},{4,5,6}),
    ({1,3,5},{3,4,5}),
    ({1,2,5},{2,4,5}),
    ({1,2,3},{2,3,4}),
]
blocks=[B for e in edges for B in e]
assert len(blocks)==14 and len({frozenset(B) for B in blocks})==14
assert all(B <= X and len(B)==3 for B in blocks)
cover_checks=0
for i,(A,B) in enumerate(edges):
    # G-Sperner on every matching edge.
    assert not (A <= B) and not (B <= A)
    U=A|B
    C=X-U
    # ECFF condition: every block off this edge has a point outside U.
    disjoint=[]
    for j,D in enumerate(blocks):
        if j not in (2*i,2*i+1):
            cover_checks += 1
            assert not (D <= U), (i,j,D,U)
            assert D & C
        else:
            assert D <= U
            disjoint.append(j)
    assert len(C)==2

def t1(n):
    t=1
    while comb(t,t//2)<n:
        t+=1
    return t

# Sperner lower bound t(1,14)=6 and edge-cover-free value t_e(E_14)=t(1,7)=5.
assert comb(5,2)==10 < 14 <= comb(6,3)==20
assert t1(14)==6
assert comb(4,2)==6 < 7 <= comb(5,2)==10
assert t1(7)==5
print(f'ALL CHECKS PASSED; blocks={len(blocks)}; edges={len(edges)}; cover_checks={cover_checks}; t1_14={t1(14)}; t1_7={t1(7)}')
