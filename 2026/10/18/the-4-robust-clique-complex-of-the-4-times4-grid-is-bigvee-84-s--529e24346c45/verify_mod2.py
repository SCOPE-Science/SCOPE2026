#!/usr/bin/env python3
"""Independent mod-2 homology cross-check for the 4x4 grid's 4-robust complex."""
from collections import defaultdict
from itertools import combinations

N=16
edges=set()
for r in range(4):
    for c in range(4):
        i=4*r+c
        if r<3:edges.add(frozenset((i,i+4)))
        if c<3:edges.add(frozenset((i,i+1)))

forbidden=[]
for q in combinations(range(N),4):
    if all(frozenset((u,v)) not in edges for u,v in combinations(q,2)):
        forbidden.append(sum(1<<v for v in q))

faces=defaultdict(list)
for s in range(1,1<<N):
    if any((s & f)==f for f in forbidden):
        continue
    faces[s.bit_count()-1].append(s)


def boundary_rank(d):
    if d<=0:return 0
    source=faces[d]
    index={s:i for i,s in enumerate(faces[d-1])}
    pivots={}
    for s in source:
        bitset=0
        for v in range(N):
            if s>>v & 1:
                bitset^=1<<index[s-(1<<v)]
        while bitset:
            high=bitset.bit_length()-1
            if high in pivots:
                bitset^=pivots[high]
            else:
                pivots[high]=bitset
                break
    return len(pivots)

ranks=[boundary_rank(d) for d in range(7)]
betti=[len(faces[d])-ranks[d]-ranks[d+1] for d in range(6)]
betti[0]-=1
assert betti == [0,0,0,0,0,84], betti
assert ranks == [0,15,105,455,960,828,0], ranks
assert sum((-1)**i*len(faces[i]) for i in range(6)) == -83
print('HOMOLOGY_OK', 'ranks='+repr(ranks),'reduced_F2_betti='+repr(betti),'Euler=-83')
