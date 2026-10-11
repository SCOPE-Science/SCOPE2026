#!/usr/bin/env python3
import json

# Heawood graph as the point-line incidence graph of the Fano plane.
V=list(range(14))
edges=[]
for j in range(7):
    for off in (0,1,3):
        p=(j+off)%7
        edges.append(tuple(sorted((p,7+j))))
edges=sorted(set(edges))
assert len(edges)==21
assert all(sum(v in e for e in edges)==3 for v in V)

# Ordered Abrams discrete configuration space D_2(H): open cells are ordered
# products of vertices/open edges with pairwise disjoint closures.
C0=[(x,y) for x in V for y in V if x!=y]
i0={c:i for i,c in enumerate(C0)}
C1=[]
for ei,(a,b) in enumerate(edges):
    for y in V:
        if y not in (a,b): C1.append((0,ei,y)) # first coordinate moves
for ej,(a,b) in enumerate(edges):
    for x in V:
        if x not in (a,b): C1.append((1,x,ej)) # second coordinate moves
i1={c:i for i,c in enumerate(C1)}
C2=[]
for ei,e in enumerate(edges):
    for ej,f in enumerate(edges):
        if set(e).isdisjoint(f): C2.append((ei,ej))
assert (len(C0),len(C1),len(C2))==(182,504,336)

# Boundary matrices over F_2 represented by column bitsets.
d1=[]
for c in C1:
    bits=0
    if c[0]==0:
        _,ei,y=c; a,b=edges[ei]
        bits ^= 1<<i0[(a,y)]; bits ^= 1<<i0[(b,y)]
    else:
        _,x,ej=c; a,b=edges[ej]
        bits ^= 1<<i0[(x,a)]; bits ^= 1<<i0[(x,b)]
    d1.append(bits)
d2=[]
for ei,ej in C2:
    a,b=edges[ei]; c,d=edges[ej]
    bits=0
    bits ^= 1<<i1[(1,a,ej)]; bits ^= 1<<i1[(1,b,ej)]
    bits ^= 1<<i1[(0,ei,c)]; bits ^= 1<<i1[(0,ei,d)]
    d2.append(bits)

# Check d1*d2=0 exactly over F_2.
for col in d2:
    acc=0
    x=col
    while x:
        lb=x & -x; j=lb.bit_length()-1
        acc ^= d1[j]; x-=lb
    assert acc==0

def rank_columns(cols):
    basis={}
    for x in cols:
        y=x
        while y:
            p=y.bit_length()-1
            if p in basis: y ^= basis[p]
            else:
                basis[p]=y; break
    return len(basis)

r1=rank_columns(d1); r2=rank_columns(d2)
assert (r1,r2)==(181,307)
b0=len(C0)-r1
b1=len(C1)-r1-r2
b2=len(C2)-r2
assert (b0,b1,b2)==(1,16,29)
assert len(C0)-len(C1)+len(C2)==14

cert={
 "graph":"Heawood graph as the Fano-plane incidence graph",
 "ordered_particles":2,
 "cell_counts":[182,504,336],
 "boundary_ranks_mod2":[181,307],
 "betti_mod2":[1,16,29],
 "reduced_betti_mod2":{"1":16,"2":29},
 "euler_characteristic":14
}
with open('certificate.json','w',encoding='utf-8') as f:
    json.dump(cert,f,sort_keys=True,indent=2); f.write('\n')
print('VERIFY_OK')
print(json.dumps(cert,sort_keys=True))
