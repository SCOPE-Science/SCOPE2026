#!/usr/bin/env python3
"""Finite checks for the clique-fiber Boolean-cube Ising model."""
from collections import Counter
from itertools import combinations
from math import sqrt

def graph(d):
    L=1<<d
    edges=set()
    for s in range(L):
        for i,j in combinations(range(d),2):
            edges.add(tuple(sorted((i*L+s,j*L+s))))
    for i in range(d):
        for s in range(L):
            for j in range(d):
                if j != i:
                    edges.add(tuple(sorted((i*L+s, i*L+(s^(1<<j))))))
    return edges

def B(d,r):
    L=1<<d;q=r//L
    return 2*(d-1-q)*r+L*q*(q+1)

for d in range(3,9):
    L=1<<d;N=d*L
    chosen={i*L+s for i in range(d) for s in range(L) if (s.bit_count()%2)==(i%2)}
    assert len(chosen)==N//2
    edges=graph(d)
    assert len(edges)==N*(d-1)
    assert len({v for e in edges for v in e})==N
    deg=Counter(v for e in edges for v in e)
    assert set(deg.values())=={2*(d-1)}
    for r in range(N//2,-1,-1):
        q=Counter(v%L for v in chosen)
        if len(q)<L:q.update({s:0 for s in range(L) if s not in q})
        assert max(q.values())-min(q.values())<=1
        internal=sum(c*(c-1)//2 for c in q.values())
        assert 2*(d-1)*r-2*internal==B(d,r)
        # Count every edge directly for the geometrically important d=3,4.
        if d <= 4:
            cut=sum((a in chosen)!=(b in chosen) for a,b in edges)
            assert cut==B(d,r),(d,r,cut,B(d,r))
        if r:
            top=max(q,key=q.get)
            chosen.remove(next(v for v in chosen if v%L==top))
    print(f'd={d} vertices={N} edges={len(edges)} all {N//2+1} sector witnesses verified')
# Concrete 3D realization of the rhombicuboctahedron.
d=3; L=8
v=[]
for i in range(d):
    for s in range(L):
        v.append(tuple((-1 if (s>>j)&1 else 1)*(1+sqrt(2) if i==j else 1) for j in range(d)))
geo={(a,b) for a in range(24) for b in range(a+1,24) if abs(sum((v[a][j]-v[b][j])**2 for j in range(3))-4)<1e-8}
assert geo==graph(3)
print('d=3 coordinate embedding: every unit-edge graph relation verified')
