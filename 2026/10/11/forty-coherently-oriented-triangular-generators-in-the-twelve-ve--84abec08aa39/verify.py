#!/usr/bin/env python3
from itertools import combinations, permutations
from collections import Counter
from fractions import Fraction

F={tuple(sorted(x)) for x in [
(1,2,3,4,6),(1,2,3,4,11),(1,2,3,5,6),(1,2,3,5,12),(1,2,3,10,11),(1,2,3,10,12),
(1,2,4,5,6),(1,2,4,5,12),(1,2,4,11,12),(1,2,9,10,11),(1,2,9,10,12),(1,2,9,11,12),
(1,3,4,5,6),(1,3,4,5,12),(1,3,4,11,12),(1,3,10,11,12),(1,8,9,10,11),(1,8,9,10,12),
(1,8,9,11,12),(1,8,10,11,12),(2,3,4,5,7),(2,3,4,5,12),(2,3,4,6,7),(2,3,4,11,12),
(2,3,5,6,7),(2,3,10,11,12),(2,4,5,6,7),(2,9,10,11,12),(3,4,5,6,8),(3,4,5,7,8),
(3,4,6,7,8),(3,5,6,7,8),(4,5,6,7,9),(4,5,6,8,9),(4,5,7,8,9),(4,6,7,8,9),
(5,6,7,8,10),(5,6,7,9,10),(5,6,8,9,10),(5,7,8,9,10),(6,7,8,9,11),(6,7,8,10,11),
(6,7,9,10,11),(6,8,9,10,11),(7,8,9,10,12),(7,8,9,11,12),(7,8,10,11,12),(7,9,10,11,12)
]}
V=tuple(range(1,13))
def faces(k): return sorted({tuple(sorted(c)) for f in F for c in combinations(f,k)})
E=faces(2); T=faces(3); Q=faces(4)
assert (len(V),len(E),len(T),len(Q),len(F))==(12,60,120,120,48)
Es=set(E); Ts=set(T)
missing_edges=sorted(set(combinations(V,2))-Es)
assert missing_edges==[(1,7),(2,8),(3,9),(4,10),(5,11),(6,12)]

Ei={e:i for i,e in enumerate(E)}
def evec(edges):
    x=0
    for e in edges: x ^= 1<<Ei[tuple(sorted(e))]
    return x

def rref_basis(rows):
    B={}
    for x in rows:
        y=x
        for p in sorted(B,reverse=True):
            if (y>>p)&1: y ^= B[p]
        if not y: continue
        p=y.bit_length()-1
        for q in list(B):
            if (B[q]>>p)&1: B[q] ^= y
        B[p]=y
    return dict(sorted(B.items(),reverse=True))
def reduce_mod(x,B):
    for p,row in B.items():
        if (x>>p)&1: x ^= row
    return x

B=rref_basis([evec(combinations(t,2)) for t in T])
assert len(B)==48
# connected graph: cycle dimension 60-12+1=49, so H1(F2) dimension is one.
assert len(E)-len(V)+1-len(B)==1

cliques=[c for c in combinations(V,3) if set(combinations(c,2))<=Es]
empty=sorted(set(cliques)-Ts)
assert len(cliques)==160 and len(empty)==40
assert all(reduce_mod(evec(combinations(c,2)),B)!=0 for c in empty)

# Integral cocycle: coefficient 1 on these increasingly oriented edges, 0 elsewhere.
WPOS={(3,8),(4,8),(4,9),(5,8),(5,9),(5,10),(6,8),(6,9),(6,10),(6,11),
      (7,8),(7,9),(7,10),(7,11),(7,12)}
def w(e): return 1 if tuple(sorted(e)) in WPOS else 0
# orientation convention: all edges and triangles increasingly oriented.
def tri_eval(t):
    a,b,c=t
    return w((b,c))-w((a,c))+w((a,b))
assert all(tri_eval(t)==0 for t in T)
assert Counter(tri_eval(t) for t in empty)==Counter({1:40})

# Full automorphism group: any automorphism must preserve the six missing edges,
# so exhaust all 2^6 * 6! permutations of the antipodal pairs.
pairs=missing_edges
Fset=set(F)
auts=[]
for pp in permutations(range(6)):
    for mask in range(64):
        m={}
        for i,(a,b) in enumerate(pairs):
            c,d=pairs[pp[i]]
            if (mask>>i)&1: c,d=d,c
            m[a]=c; m[b]=d
        if {tuple(sorted(m[x] for x in f)) for f in Fset}==Fset:
            auts.append(m)
assert len(auts)==24

unseen=set(empty); orbits=[]
while unseen:
    q=min(unseen)
    O={tuple(sorted(m[x] for x in q)) for m in auts}
    orbits.append((len(O),q))
    unseen-=O
assert sorted(orbits)==[(4,(1,5,9)),(12,(1,3,8)),(24,(1,4,8))]

# Each vertex occurs equally often in the complete carrier family.
vinc={v:sum(v in q for q in empty) for v in V}
assert set(vinc.values())=={10}

print('VERIFY_OK f=12,60,120,120,48 H1_F2_dim=1 empty3=40 '
      'all_empty3_nonzero=yes integral_pairings=+1:40 aut=24 '
      'carrier_orbits=4,12,24 reps=159|138|148 carrier_vertex_degree=10')
