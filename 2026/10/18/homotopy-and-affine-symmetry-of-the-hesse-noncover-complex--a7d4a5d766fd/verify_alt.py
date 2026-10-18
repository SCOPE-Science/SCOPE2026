#!/usr/bin/env python3
"""Separate exact modular chain-rank cross-check for the Hesse line noncover complex."""
from itertools import product, combinations
V=list(product(range(3),repeat=2))
L={frozenset(i for i,(x,y) in enumerate(V) if (a*x+b*y-c)%3==0)
   for a,b in product(range(3),repeat=2) if a or b for c in range(3)}
F=[sorted(set(c for l in L for c in combinations(sorted(set(range(9))-l),d+1)))
   for d in range(6)]
assert [len(z) for z in F]==[9,36,84,126,72,12]
def rank_mod(p,cols,rows):
    basis={}
    for C in cols:
        v={i:(coeff%p) for i,coeff in C.items() if coeff%p}
        while v:
            pivot=min(v)
            if pivot not in basis:
                u={i:((x*pow(v[pivot],-1,p))%p) for i,x in v.items()}
                basis[pivot]=u;break
            other=basis[pivot];scale=v[pivot]
            for i,x in other.items():
                val=(v.get(i,0)-scale*x)%p
                if val:v[i]=val
                elif i in v:del v[i]
    return len(basis)
for p in (2,3,5,101):
    ranks=[]
    for d in range(1,6):
        row_index={s:i for i,s in enumerate(F[d-1])}
        cols=[]
        for s in F[d]:
            cols.append({row_index[s[:i]+s[i+1:]]:(-1)**i for i in range(d+1)})
        ranks.append(rank_mod(p,cols,len(F[d-1])))
    betti=[len(F[d])-(ranks[d-1] if d else 1)-(ranks[d] if d<5 else 0) for d in range(6)]
    assert ranks==[8,28,56,59,12]
    assert betti==[0,0,0,11,1,0]
    print(f'prime={p} boundary_ranks={ranks} reduced_betti={betti}')
