#!/usr/bin/env python3
from itertools import combinations, permutations, product
from collections import Counter

FACETS = {
tuple(x) for x in [
(1,2,3,5),(1,2,3,11),(1,2,5,10),(1,2,10,11),(1,3,4,5),(1,3,4,12),(1,3,11,12),
(1,4,5,8),(1,4,6,8),(1,4,6,9),(1,4,9,12),(1,5,8,10),(1,6,8,10),(1,6,9,10),
(1,9,10,11),(1,9,11,12),(2,3,5,6),(2,3,6,11),(2,4,6,9),(2,4,6,11),(2,4,7,11),
(2,4,7,12),(2,4,9,12),(2,5,6,9),(2,5,9,12),(2,5,10,12),(2,7,10,11),(2,7,10,12),
(3,4,5,7),(3,4,7,12),(3,5,6,7),(3,6,7,10),(3,6,8,10),(3,6,8,11),(3,7,10,12),
(3,8,10,12),(3,8,11,12),(4,5,7,8),(4,6,8,11),(4,7,8,11),(5,6,7,9),(5,7,8,9),
(5,8,9,12),(5,8,10,12),(6,7,9,10),(7,8,9,11),(7,9,10,11),(8,9,11,12)
]}
V=tuple(range(1,13))

def faces(k):
    return {tuple(sorted(c)) for f in FACETS for c in combinations(f,k)}

E=sorted(faces(2))
T=sorted(faces(3))
assert (len(V),len(E),len(T),len(FACETS)) == (12,60,96,48)

missing_edges=sorted(set(combinations(V,2))-set(E))
PAIRS=[(1,7),(2,8),(3,9),(4,10),(5,11),(6,12)]
assert missing_edges == PAIRS

Ei={e:i for i,e in enumerate(E)}

def edge_vector(edges):
    x=0
    for e in edges:
        x ^= 1 << Ei[tuple(sorted(e))]
    return x

def triangle_boundary(q):
    a,b,c=q
    return edge_vector(((a,b),(a,c),(b,c)))

def rref_basis(rows):
    B={}
    for x in rows:
        y=x
        for p in sorted(B,reverse=True):
            if (y>>p)&1:
                y ^= B[p]
        if not y:
            continue
        p=y.bit_length()-1
        for q in list(B):
            if (B[q]>>p)&1:
                B[q] ^= y
        B[p]=y
    return dict(sorted(B.items(),reverse=True))

def reduce_mod(x,B):
    y=x
    for p,row in B.items():
        if (y>>p)&1:
            y ^= row
    return y

B=rref_basis([triangle_boundary(t) for t in T])
assert len(B)==48
assert len(E)-len(V)+1-len(B)==1

Es=set(E); Ts=set(T)
cliques=[q for q in combinations(V,3) if set(combinations(q,2)) <= Es]
empty=sorted(set(cliques)-Ts)
assert len(cliques)==160
assert len(empty)==64
assert all(reduce_mod(triangle_boundary(q),B)!=0 for q in empty)
assert all(reduce_mod(triangle_boundary(q),B)==0 for q in T)

# The complement graph is six disjoint edges, so every graph and hence simplicial
# automorphism permutes the six antipodal pairs, possibly swapping within pairs.
auts=[]
for pair_perm in permutations(range(6)):
    for flips in product((0,1),repeat=6):
        m={}
        for i,(a,b) in enumerate(PAIRS):
            x,y=PAIRS[pair_perm[i]]
            if flips[i]:
                x,y=y,x
            m[a]=x
            m[b]=y
        if {tuple(sorted(m[v] for v in f)) for f in FACETS} == FACETS:
            auts.append(m)
assert len(auts)==24

# Full carrier-orbit classification.
unseen=set(empty)
orbits=[]
while unseen:
    q=min(unseen)
    orb={tuple(sorted(m[v] for v in q)) for m in auts}
    assert orb <= set(empty)
    orbits.append((len(orb),q,orb))
    unseen -= orb
orbits=sorted(orbits,key=lambda z:(z[0],z[1]))
assert [(n,q) for n,q,_ in orbits] == [
    (4,(1,5,9)),
    (12,(1,2,12)),
    (24,(1,2,4)),
    (24,(1,2,6)),
]

# The exceptional size-four orbit is a parallel class.
small=next(orb for n,q,orb in orbits if n==4)
assert len(set().union(*(set(q) for q in small)))==12
assert all(set(a).isdisjoint(b) for a,b in combinations(small,2))

# Transitivity and orbit-wise incidence.
assert {m[1] for m in auts}==set(V)
degrees=[]
for n,q,orb in orbits:
    ds={v:sum(v in s for s in orb) for v in V}
    assert len(set(ds.values()))==1
    degrees.append(next(iter(ds.values())))
assert degrees==[1,3,6,6]
total_degree={v:sum(v in s for s in empty) for v in V}
assert set(total_degree.values())=={16}

print(
    "VERIFY_OK f=12,60,96,48 missing_edges=6 "
    "H1_F2_dim=1 cliques3=160 facial3=96 essential3=64 "
    "aut=24 carrier_orbits=4,12,24,24 reps=159|1212|124|126 "
    "orbit_vertex_degrees=1,3,6,6 small_orbit_parallel=yes total_vertex_degree=16"
)
