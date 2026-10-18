#!/usr/bin/env python3
"""Independent chain-rank check from connected-component enumeration.
Uses only the Python 3 standard library, separate graph and face algorithms.
"""
from collections import defaultdict
from itertools import combinations

points=tuple(range(7));lines=tuple(range(7,14))
incidence=[(p,7+s) for s in points for p in ((s)%7,(s+1)%7,(s+3)%7)]
assert len(incidence)==21
nb={v:set() for v in range(14)}
for a,b in incidence:
    nb[a].add(b);nb[b].add(a)

# Independent connected-component test (not forbidden-triple lookup).
def admissible(m):
    unseen={v for v in range(14) if m>>v&1}
    while unseen:
        seed=unseen.pop();visited={seed};front=[seed]
        while front:
            v=front.pop()
            for w in nb[v]&unseen:
                unseen.remove(w);visited.add(w);front.append(w)
                if len(visited)>2:return False
    return True

layers=defaultdict(list)
for m in range(1,1<<14):
    if admissible(m):layers[m.bit_count()-1].append(m)
assert [len(layers[d]) for d in range(7)]==[14,91,322,651,728,392,58]

def rank_two(col_dim):
    rows={m:i for i,m in enumerate(layers[col_dim-1])}
    pivots={}
    for co in layers[col_dim]:
        vec=0
        for v in range(14):
            if co>>v&1:vec^=1<<rows[co^(1<<v)]
        while vec:
            j=vec.bit_length()-1
            if j not in pivots:
                pivots[j]=vec;break
            vec^=pivots[j]
    return len(pivots)

def rank_prime(col_dim,p):
    rows={m:i for i,m in enumerate(layers[col_dim-1])}
    pivots={}
    for co in layers[col_dim]:
        vec={}
        vertices=[v for v in range(14) if co>>v&1]
        for i,v in enumerate(vertices):vec[rows[co^(1<<v)]]=(-1 if i%2 else 1)%p
        while vec:
            j=max(vec)
            if j not in pivots:
                inv=pow(vec[j],-1,p)
                pivots[j]={i:(c*inv)%p for i,c in vec.items()}
                break
            mul=vec[j]
            for i,c in pivots[j].items():
                new=(vec.get(i,0)-mul*c)%p
                if new:vec[i]=new
                else:vec.pop(i,None)
    return len(pivots)

expected=[13,78,244,407,321,58]
for p in [2,3,5]:
    ranks=[rank_two(d) if p==2 else rank_prime(d,p) for d in range(1,7)]
    assert ranks==expected,(p,ranks)
    betas={d:len(layers[d])-(ranks[d-1] if d>=1 else 0)-(ranks[d] if d<6 else 0) for d in range(7)}
    # d0: connected component correction requires reduced H0, and rank1 is 13.
    assert betas=={0:1,1:0,2:0,3:0,4:0,5:13,6:0},(p,betas)
    print('PASS: characteristic',p,'ranks',ranks,'ordinary_Betti',betas)
print('PASS: independent graph construction, connected-component enumeration, boundary ranks')
