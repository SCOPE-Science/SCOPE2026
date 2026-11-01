#!/usr/bin/env python3
"""Independent finite-chain and fixed-orbit check of Franklin matching data."""
from itertools import combinations
from collections import Counter

# Edge list is generated without a graph library or importing the other checker.
E = set()
for v in range(12):
    E.add(tuple(sorted((v,(v+1)%12))))
    E.add(tuple(sorted((v,(v+(5 if v%2==0 else -5))%12))))
E = sorted(E)
assert len(E)==18
F={0:[()]}
for k in range(1,7):
    selected=[]
    for s in combinations(range(18),k):
        vs=tuple(x for i in s for x in E[i])
        if len(set(vs))==len(vs):selected.append(s)
    F[k]=selected
assert [len(F[k]) for k in range(1,7)]==[18,117,336,417,186,17]

ranks={}
for k in range(1,7):
    index={face:j for j,face in enumerate(F[k-1])}
    basis={}
    for simplex in F[k]:
        v=0
        for j in range(k):
            v ^= 1 << index[simplex[:j]+simplex[j+1:]]
        while v:
            pivot=v.bit_length()-1
            if pivot in basis:v^=basis[pivot]
            else:
                basis[pivot]=v
                break
    ranks[k]=len(basis)
assert tuple(ranks[k] for k in range(1,7))==(1,17,100,236,169,17)
# Reduced mod-two homology ranks in simplicial dimensions zero through five.
betti={k-1:len(F[k])-ranks[k]-ranks.get(k+1,0) for k in range(1,7)}
assert betti=={0:0,1:0,2:0,3:12,4:0,5:0}
print('FRANKLIN_INDEPENDENT_CHAIN_VERIFIED')
print('rank array',tuple(ranks[k] for k in range(1,7)))
print('Betti array',tuple(betti[k] for k in range(6)))
