#!/usr/bin/env python3
"""Independent uncompressed simplicial-chain rank checks for Petersen 5-cut.
Only Python 3 standard library; does not use the Morse matching or certificate.
"""
from itertools import combinations
from collections import defaultdict
V=tuple(combinations(range(5),2));N=len(V)
E={(u,v) for u,v in combinations(range(N),2) if set(V[u]).isdisjoint(V[v])}
def is_connected(subset):
    reached={min(subset)}
    while True:
        step=reached|{v for v in subset if any(tuple(sorted((u,v))) in E for u in reached)}
        if step==reached:return len(reached)==len(subset)
        reached=step
facets=[tuple(sorted(set(range(N))-set(S)))
        for S in combinations(range(N),5) if not is_connected(set(S))]
by_size=defaultdict(set)
for facet in facets:
    for size in range(1,6):
        for simplex in combinations(facet,size): by_size[size].add(simplex)
assert [len(by_size[k]) for k in range(1,6)]==[10,45,120,200,120]

def boundary_rank_mod_p(k,p):
    target={v:i for i,v in enumerate(sorted(by_size[k]))}
    pivots={};rank=0
    for simplex in sorted(by_size[k+1]):
        col={target[simplex[:i]+simplex[i+1:]]:(-1 if i%2 else 1)%p for i in range(k+1)}
        while col:
            head=min(col)
            if head not in pivots:
                inv=pow(col[head],-1,p)
                pivots[head]={z:(a*inv)%p for z,a in col.items()}
                rank+=1
                break
            t=col[head]
            for j,a in pivots[head].items():
                b=(col.get(j,0)-t*a)%p
                if b:col[j]=b
                else:col.pop(j,None)
    return rank
for p in (2,3,5,7,11):
    ranks={k:boundary_rank_mod_p(k,p) for k in range(1,5)}
    b=[len(by_size[k+1])-ranks.get(k,0)-ranks.get(k+1,0) for k in range(5)]
    b[0]-=1
    assert ranks=={1:9,2:36,3:84,4:115} and b==[0,0,0,1,5]
    print(f'p={p}: boundary ranks (9,36,84,115), reduced Betti (0,0,0,1,5)')
