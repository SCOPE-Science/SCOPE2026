#!/usr/bin/env python3
"""Independent face/enumeration and finite-field chain-rank check (stdlib)."""
from itertools import combinations

# Independently construct the D4 roots using ordered signed supports.
V = []
for i in range(4):
    for j in range(i+1,4):
        for signs in ((1,1),(1,-1),(-1,1),(-1,-1)):
            x=[0,0,0,0]; x[i]=signs[0];x[j]=signs[1]
            V.append(tuple(x))
assert len(set(V)) == 24
E=set()
for u in range(24):
    for v in range(u+1,24):
        if sum((a-b)**2 for a,b in zip(V[u],V[v]))==2:
            E.add((u,v))
assert len(E)==96

# Enumeration by recursive adding vertices in strictly increasing order.
face_lists = [[] for _ in range(8)]
def explore(prefix, last):
    if prefix:
        face_lists[len(prefix)-1].append(sum(1<<v for v in prefix))
    for nxt in range(last+1,24):
        if all((min(v,nxt),max(v,nxt)) not in E for v in prefix):
            explore(prefix+(nxt,),nxt)
explore((),-1)
assert [len(x) for x in face_lists] == [24,180,488,474,216,84,24,3]

# Standard simplicial boundary ranks over GF(p), no Morse matching used.
def rank_mod_p(columns,nrows,p):
    pivots={}
    for col in columns:
        current={k:v%p for k,v in col.items() if v%p}
        while current:
            lead=max(current)
            if lead not in pivots:
                coeff=current[lead]
                inv=pow(coeff,-1,p)
                pivots[lead]={i:(v*inv)%p for i,v in current.items()}
                break
            basis=pivots[lead]
            k=current[lead]
            for i,v in basis.items():
                x=(current.get(i,0)-k*v)%p
                if x:current[i]=x
                else:current.pop(i,None)
    return len(pivots)

for p in (2,3,5):
    ranks=[]
    for degree in range(1,8):
        index={f:i for i,f in enumerate(face_lists[degree-1])}
        columns=[]
        for upper in face_lists[degree]:
            vs=[i for i in range(24) if upper&(1<<i)]
            columns.append({index[upper^(1<<i)]:(-1)**j for j,i in enumerate(vs)})
        ranks.append(rank_mod_p(columns,len(face_lists[degree-1]),p))
    assert ranks == [23,157,300,153,63,21,3], (p,ranks)
    betti=[len(fs)-(ranks[d-1] if d else 1)-(ranks[d] if d<7 else 0)
           for d,fs in enumerate(face_lists)]
    assert betti == [0,0,31,21,0,0,0,0], (p,betti)
    print(f'GF({p}) boundary ranks={ranks}; reduced Betti={betti}')
print('all independent finite-field homology checks passed')
