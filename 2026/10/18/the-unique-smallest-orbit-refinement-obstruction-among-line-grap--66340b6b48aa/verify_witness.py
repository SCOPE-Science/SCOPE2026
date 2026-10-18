#!/usr/bin/env python3
"""Direct graph-aut check for the exceptional 8-vertex line graph, no dependencies."""
from itertools import permutations

E=((0,1),(0,2),(0,3),(1,4),(4,5),(5,6),(6,7),(6,8))
N=len(E)
G=[[int(i!=j and bool(set(E[i])&set(E[j]))) for j in range(N)] for i in range(N)]

def colors(mark=None):
    c=[1 if x==mark else 0 for x in range(N)]
    for _ in range(N+2):
        signatures=[(c[i],tuple(sorted(c[j] for j in range(N) if G[i][j]))) for i in range(N)]
        names={s:k for k,s in enumerate(sorted(set(signatures)))}
        nc=[names[s] for s in signatures]
        if len(set(nc))==len(set(c)):return nc
        c=nc
    raise AssertionError('No stabilization')

def aut_orbits(mark=None):
    candidates=[]
    degree=[sum(row) for row in G]
    for p in permutations(range(N)):
        if mark is not None and p[mark]!=mark:continue
        if any(degree[i]!=degree[p[i]] for i in range(N)):continue
        if all(G[i][j]==G[p[i]][p[j]] for i in range(N) for j in range(i)):
            candidates.append(p)
    parts=[];unused=set(range(N))
    while unused:
        x=min(unused);o={p[x] for p in candidates}
        assert o<=unused
        parts.append(tuple(sorted(o)));unused-=o
    return parts

for mark in [None]+list(range(N)):
    c=colors(mark)
    parts=aut_orbits(mark)
    assert all(len({c[i] for i in block})==1 for block in parts)
    if mark is None:
        assert len(set(c))==2 and len(parts)==3
    else:
        assert len(set(c))==len(parts)
print('AUTOMORPHISM_ENUMERATION_OK')
