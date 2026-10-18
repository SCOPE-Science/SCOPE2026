#!/usr/bin/env python3
"""Independent exact mod-2 check of fixed-point complexes for short binary cubes."""
from collections import defaultdict
from itertools import combinations
from math import comb


def rank_mod2(boundary_columns):
    pivots={}
    for col in boundary_columns:
        x=col
        while x:
            p=x.bit_length()-1
            if p in pivots: x^=pivots[p]
            else:
                pivots[p]=x
                break
    return len(pivots)


def build(n):
    t=7
    reps=[v for v in range(1<<n) if (v&4)==0]
    neighbors={i:set() for i in range(len(reps))}
    for i,j in combinations(range(len(reps)),2):
        u=reps[i]^reps[j]
        if max(u.bit_count(),(u^t).bit_count())<=3:
            neighbors[i].add(j);neighbors[j].add(i)
    # Enumerate all cliques directly, independent of the quotient-graph decomposition.
    faces=[(i,) for i in range(len(reps))]
    idx=0
    while idx<len(faces):
        face=faces[idx]
        for j in range(face[-1]+1,len(reps)):
            if all(j in neighbors[i] for i in face):
                faces.append(face+(j,))
        idx+=1
    assert max(map(len,faces))==4
    bydim=defaultdict(list)
    for f in faces:bydim[len(f)-1].append(f)
    ranks={}
    for k in range(1,4):
        rowindex={f:i for i,f in enumerate(bydim[k-1])}
        boundary=[]
        for f in bydim[k]:
            column=0
            for j in range(k+1):column ^=1<<rowindex[f[:j]+f[j+1:]]
            boundary.append(column)
        ranks[k]=rank_mod2(boundary)
    betti={k:len(bydim[k])-ranks.get(k,0)-ranks.get(k+1,0) for k in range(4)}
    d=n-3;E=d*(1<<(d-1));V=1<<d
    assert betti=={0:1,1:E-V+1,2:0,3:E},(n,betti,E,V)
    # Check the explicit orbit-adjacency equivalence derived in the proof.
    for i,j in combinations(range(len(reps)),2):
        x,y=reps[i],reps[j]
        outer=(x^y)>>3
        inner=(x^y)&3
        predicted=(outer.bit_count()<=1 and inner!=0)
        assert predicted==(j in neighbors[i])
    print(f'n={n}: |orbits|={len(reps)}, simplices={[len(bydim[k]) for k in range(4)]}, Betti(F2)={betti}')

for n in (4,5,6,7):build(n)
print('PASS')
