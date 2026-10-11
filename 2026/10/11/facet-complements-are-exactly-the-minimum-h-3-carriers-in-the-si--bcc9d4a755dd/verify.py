#!/usr/bin/env python3
from itertools import combinations

V=tuple(range(1,17))

def perm_from_cycles(cycles):
    p={i:i for i in V}
    for cyc in cycles:
        cyc=tuple(cyc)
        for a,b in zip(cyc,cyc[1:]+cyc[:1]):
            p[a]=b
    return tuple(p[i] for i in V)

P=perm_from_cycles(((2,7),(4,10),(5,6),(11,12)))
Q=perm_from_cycles(((1,2,3,4,5,10),(6,8,9),(11,12,13,14,15,16)))

def compose(a,b):
    return tuple(a[b[i]-1] for i in range(16))

ID=tuple(V)
G={ID}
todo=[ID]
while todo:
    g=todo.pop()
    for h in (P,Q):
        for z in (compose(g,h),compose(h,g)):
            if z not in G:
                G.add(z); todo.append(z)
assert len(G)==720

def image_face(face,g):
    return tuple(sorted(g[x-1] for x in face))

BASE=((1,2,4,5,11),(1,2,4,11,13))
FACETS=set()
for b in BASE:
    FACETS |= {image_face(b,g) for g in G}
assert len(FACETS)==150

def faces(k):
    return {tuple(sorted(c)) for f in FACETS for c in combinations(f,k)}

E=sorted(faces(2))
T=sorted(faces(3))
Q4=sorted(faces(4))
assert (len(V),len(E),len(T),len(Q4),len(FACETS))==(16,120,330,375,150)

Ti={t:i for i,t in enumerate(T)}
Qi={q:i for i,q in enumerate(Q4)}

def gf2_basis(rows):
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

def gf2_reduce(x,B):
    y=x
    while y:
        p=y.bit_length()-1
        if p in B:
            y ^= B[p]
        else:
            break
    return y

# Boundary of a tetrahedron as a triangle-chain bit vector.
D3={}
for q4 in Q4:
    x=0
    for t in combinations(q4,3):
        x ^= 1<<Ti[t]
    D3[q4]=x

# Boundary of a 4-simplex as a tetrahedron-chain bit vector.
D4={}
for f in FACETS:
    x=0
    for q4 in combinations(f,4):
        x ^= 1<<Qi[tuple(sorted(q4))]
    D4[f]=x

B3=gf2_basis(D3.values())
B4=gf2_basis(D4.values())
assert (len(B3),len(B4),len(Q4)-len(B3)-len(B4))==(225,149,1)

# Kernel of the local d3 map, returned as global tetrahedron-chain bit vectors.
def local_kernel_chains(S):
    S=set(S)
    qs=[q for q in Q4 if set(q)<=S]
    piv={}  # boundary pivot -> (boundary vector, tetrahedron-chain vector)
    kernels=[]
    for q in qs:
        y=D3[q]
        chain=1<<Qi[q]
        while y:
            p=y.bit_length()-1
            if p in piv:
                y ^= piv[p][0]
                chain ^= piv[p][1]
            else:
                piv[p]=(y,chain)
                break
        if not y:
            kernels.append(chain)
    return qs, kernels, len(piv)

def local_h3_dim(S):
    S=set(S)
    qs,kernels,r3=local_kernel_chains(S)
    fs=[f for f in FACETS if set(f)<=S]
    r4=len(gf2_basis(D4[f] for f in fs))
    return len(qs)-r3-r4

def supports_global_nonzero(S):
    _, kernels, _ = local_kernel_chains(S)
    return any(gf2_reduce(z,B4)!=0 for z in kernels)

# Exhaust all 10-sets. Any smaller support is contained in a 10-set,
# so this also excludes all supports of size <=10.
assert all(not supports_global_nonzero(S) for S in combinations(V,10))

all11=list(combinations(V,11))
special=[S for S in all11 if supports_global_nonzero(S)]
assert len(special)==150

facet_complements={tuple(sorted(set(V)-set(f))) for f in FACETS}
assert set(special)==facet_complements

# Each facet complement has exactly one local H3 class, and all other
# eleven-vertex induced subcomplexes have none.
for S in all11:
    h=local_h3_dim(S)
    if S in facet_complements:
        assert h==1
    else:
        assert h==0

# Published S6 action: orbit decomposition on the 150 supports.
unseen=set(special)
orbits=[]
while unseen:
    S=min(unseen)
    orb={tuple(sorted(g[x-1] for x in S)) for g in G}
    assert orb <= set(special)
    orbits.append((len(orb), min(orb)))
    unseen-=orb
orbits=sorted(orbits)
assert orbits==[
    (30,(1,2,3,4,6,8,11,12,14,15,16)),
    (120,(1,2,3,4,5,6,7,12,13,14,16)),
]

def induced_f(S):
    S=set(S)
    return (
        len(S),
        sum(set(e)<=S for e in E),
        sum(set(t)<=S for t in T),
        sum(set(q)<=S for q in Q4),
        sum(set(f)<=S for f in FACETS),
    )

assert induced_f(orbits[0][1])==(11,55,92,52,4)
assert induced_f(orbits[1][1])==(11,55,95,58,7)

print(
    "VERIFY_OK f=16,120,330,375,150 H3_F2_dim=1 "
    "min_vertex_support=11 supports11=150 facet_complements=yes "
    "other11_local_H3=0 S6_order=720 support_orbits=30,120 "
    "rep30_f=11,55,92,52,4 rep120_f=11,55,95,58,7"
)
