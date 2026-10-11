#!/usr/bin/env python3
from itertools import combinations

REPS = [
    ((1,2,3,4,5,8),39),
    ((1,2,3,4,5,9),39),
    ((1,2,3,4,7,9),39),
    ((1,2,3,5,6,9),13),
    ((1,2,3,5,8,10),13),
    ((1,2,3,7,9,12),13),
]

G=[]
for a in range(13):
    for m in (1,3,9):
        G.append({x:((m*(x-1)+a)%13)+1 for x in range(1,14)})
assert len(G)==39

FACETS=set()
orbit_sizes=[]
for rep, expected in REPS:
    O={tuple(sorted(g[x] for x in rep)) for g in G}
    assert len(O)==expected
    orbit_sizes.append(len(O))
    FACETS |= O
assert sorted(orbit_sizes)==[13,13,13,39,39,39]
assert len(FACETS)==156

def faces(k):
    return {tuple(sorted(c)) for f in FACETS for c in combinations(f,k)}

V=tuple(range(1,14))
E=sorted(faces(2))
T=sorted(faces(3))
Q=sorted(faces(4))
P=sorted(faces(5))
assert (len(V),len(E),len(T),len(Q),len(P),len(FACETS))==(13,78,286,533,468,156)
assert set(T)==set(combinations(V,3))

Ei={e:i for i,e in enumerate(E)}
Ti={t:i for i,t in enumerate(T)}

def rank_basis(rows):
    B={}
    for x in rows:
        y=x
        while y:
            p=y.bit_length()-1
            if p in B:
                y ^= B[p]
            else:
                B[p]=y
                break
    return B

def reduce_mod(x,B):
    y=x
    while y:
        p=y.bit_length()-1
        if p in B:
            y ^= B[p]
        else:
            break
    return y

d2=[]
for t in T:
    x=0
    for e in combinations(t,2):
        x ^= 1<<Ei[e]
    d2.append(x)

d3=[]
for q in Q:
    x=0
    for t in combinations(q,3):
        x ^= 1<<Ti[t]
    d3.append(x)

B2=rank_basis(d2)
B3=rank_basis(d3)
r2=len(B2); r3=len(B3)
assert (r2,r3,len(T)-r2-r3)==(66,219,1)

all4=set(combinations(V,4))
missing=sorted(all4-set(Q))
assert len(missing)==182

def tet_boundary_class(q):
    x=0
    for t in combinations(q,3):
        x ^= 1<<Ti[t]
    return reduce_mod(x,B3)

assert all(tet_boundary_class(q)==0 for q in Q)
assert all(tet_boundary_class(q)!=0 for q in missing)

unseen=set(missing)
orbits=[]
while unseen:
    q=min(unseen)
    O={tuple(sorted(g[x] for x in q)) for g in G}
    assert O <= set(missing)
    orbits.append((len(O),q))
    unseen -= O
orbits=sorted(orbits)
expected=[
    (13,(1,2,4,10)),
    (13,(1,2,9,11)),
    (39,(1,2,3,11)),
    (39,(1,2,4,6)),
    (39,(1,2,4,12)),
    (39,(1,2,7,8)),
]
assert orbits==expected

A={1,3,4,9,10,12}
def pair_signature(q):
    a=b=0
    for x,y in combinations(q,2):
        d=(y-x)%13
        if d in A:
            a+=1
        else:
            b+=1
    return (a,b)

sigs=[(n,q,pair_signature(q)) for n,q in orbits]
assert sigs==[
    (13,(1,2,4,10),(3,3)),
    (13,(1,2,9,11),(3,3)),
    (39,(1,2,3,11),(4,2)),
    (39,(1,2,4,6),(3,3)),
    (39,(1,2,4,12),(3,3)),
    (39,(1,2,7,8),(2,4)),
]

print(
    "VERIFY_OK f=13,78,286,533,468,156 H2_F2_dim=1 "
    "missing4=182 all_missing4_nonzero=yes "
    "affine_orbits=13,13,39,39,39,39 "
    "reps=12410|12911|12311|1246|12412|1278 "
    "pair_signatures=3:3|3:3|4:2|3:3|3:3|2:4"
)
