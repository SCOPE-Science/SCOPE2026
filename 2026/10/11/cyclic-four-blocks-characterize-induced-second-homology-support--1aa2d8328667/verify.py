#!/usr/bin/env python3
from itertools import combinations
from collections import Counter

N=10
cycles=[(1,1,2,6),(1,1,6,2),(1,2,1,6)]

def facets_from_cycle(c):
    base=(0,c[0],c[0]+c[1],c[0]+c[1]+c[2])
    return {tuple(sorted(((x+t)%N for x in base))) for t in range(N)}

facets=set().union(*(facets_from_cycle(c) for c in cycles))
assert len(facets)==30
faces={d:set() for d in range(4)}
for F in facets:
    for r in range(1,5):
        faces[r-1].update(combinations(F,r))
assert tuple(len(faces[d]) for d in range(4))==(10,40,60,30)

vertices=sorted(faces[0])
edges=sorted(faces[1]); triangles=sorted(faces[2]); tets=sorted(faces[3])
vid={x:i for i,x in enumerate(vertices)}
eid={x:i for i,x in enumerate(edges)}
tid={x:i for i,x in enumerate(triangles)}

# GF(2) rank for integer bit-vectors.
def rank_bits(rows):
    piv={}
    for x in rows:
        y=x
        while y:
            p=y.bit_length()-1
            if p in piv:
                y ^= piv[p]
            else:
                piv[p]=y
                break
    return len(piv)

# Boundary columns, represented as bitsets in the target basis.
d2=[]
for T in triangles:
    b=0
    for e in combinations(T,2): b ^= 1<<eid[e]
    d2.append(b)
d3=[]
for Q in tets:
    b=0
    for T in combinations(Q,3): b ^= 1<<tid[T]
    d3.append(b)
rank_d2=rank_bits(d2)
rank_d3=rank_bits(d3)
h2dim=len(triangles)-rank_d2-rank_d3
assert h2dim==1

# A basis for ker(d2), with each cycle represented as a bitset on global triangles.
def nullspace_from_columns(cols):
    # Gaussian elimination on column images while tracking domain combination.
    piv={} # target pivot -> (image, domain-vector)
    basis=[]
    for j,col in enumerate(cols):
        im=col; dom=1<<j
        while im:
            p=im.bit_length()-1
            if p in piv:
                im ^= piv[p][0]; dom ^= piv[p][1]
            else:
                piv[p]=(im,dom)
                break
        if not im:
            basis.append(dom)
    return basis

# Global B2 basis vectors in C2 are boundaries of tetrahedra.
B2=d3
rank_B2=rank_bits(B2)
assert rank_B2==29

def image_h2_rank(S):
    S=set(S)
    local_tri=[T for T in triangles if set(T)<=S]
    loc_to_global=[tid[T] for T in local_tri]
    local_d2=[]
    # use global edge basis; restriction is harmless
    for T in local_tri:
        b=0
        for e in combinations(T,2): b ^= 1<<eid[e]
        local_d2.append(b)
    local_cycles=nullspace_from_columns(local_d2)
    lifted=[]
    for z in local_cycles:
        g=0
        for j,gidx in enumerate(loc_to_global):
            if (z>>j)&1: g ^= 1<<gidx
        lifted.append(g)
    return rank_bits(B2+lifted)-rank_B2

def cyclic_block(i):
    return frozenset((i%N,(i+1)%N,(i+2)%N,(i+3)%N))
blocks={cyclic_block(i) for i in range(N)}
assert len(blocks)==10

# Missing tetrahedra: all four triangles are faces but the tetrahedron is absent.
missing4=[]
for Q in combinations(range(N),4):
    if Q in facets: continue
    if all(tuple(sorted(T)) in faces[2] for T in combinations(Q,3)):
        missing4.append(frozenset(Q))
assert set(missing4)==blocks

positive=[]
for mask in range(1<<N):
    S=tuple(i for i in range(N) if (mask>>i)&1)
    r=image_h2_rank(S)
    criterion=any(B<=set(S) for B in blocks)
    assert r in (0,1)
    assert bool(r)==criterion
    if r: positive.append(S)

layers=Counter(map(len,positive))
expected={4:10,5:50,6:100,7:100,8:45,9:10,10:1}
assert dict(sorted(layers.items()))==expected
min_support=min(layers)
assert min_support==4
for B in blocks:
    assert image_h2_rank(B)==1
# Every subset of size 8 supports H2; not every subset of size 7 does.
assert all(image_h2_rank(S)==1 for S in combinations(range(N),8))
assert any(image_h2_rank(S)==0 for S in combinations(range(N),7))

layer_text=','.join(f'{k}:{expected[k]}' for k in sorted(expected))
print('VERIFY_OK f=10,40,60,30 H2_F2=1 missing4=10 support_generators=10 support_layers='+layer_text+' threshold=8 criterion=cyclic4block')
