#!/usr/bin/env python3
"""Independent simplicial boundary-rank check over F2, no Morse-pair reuse."""
from itertools import combinations
from collections import defaultdict

edges=[(r,c) for c in range(5) for r in range(3)]  # column-major, unlike Morse proof
simp=defaultdict(list)
for size in range(1,7):
    for face in combinations(range(15),size):
        rcounts=[0,0,0];ccounts=[0]*5
        for e in face:
            r,c=edges[e]
            rcounts[r]+=1;ccounts[c]+=1
        if max(rcounts)<=2 and max(ccounts)<=2:
            simp[size-1].append(face)
assert [len(simp[d]) for d in range(6)]==[15,105,420,990,1260,690]

def rank_f2(columns):
    pivots={}
    for v in columns:
        while v:
            k=v.bit_length()-1
            if k in pivots:v^=pivots[k]
            else:
                pivots[k]=v
                break
    return len(pivots)

ranks=[0]
for k in range(1,6):
    ix={face:i for i,face in enumerate(simp[k-1])}
    columns=[]
    for face in simp[k]:
        v=0
        for j in range(len(face)):
            boundary=face[:j]+face[j+1:]
            v^=1<<ix[boundary]
        columns.append(v)
    ranks.append(rank_f2(columns))
betti=[len(simp[d])-ranks[d]- (ranks[d+1] if d+1<6 else 0) for d in range(6)]
assert ranks==[0,14,91,329,661,599],ranks
assert betti==[1,0,0,0,0,91],betti
print({'faces':[len(simp[d]) for d in range(6)],'boundary_ranks_mod2':ranks[1:],'betti_mod2':betti})
