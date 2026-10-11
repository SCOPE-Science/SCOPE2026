#!/usr/bin/env python3
"""Independent coordinate and F2 homology census for neighborhood complex of nonincidence graph PG(2,3)."""
from itertools import product,combinations
from collections import Counter
Q=3
# Distinct projective points via first nonzero coordinate fixed as 1.
points=sorted((1,y,z) for y in range(Q) for z in range(Q)) + sorted((0,1,z) for z in range(Q)) + [(0,0,1)]
assert len(points)==13 and len(set(points))==13
# Symmetric incidence matrix point vs line coefficient vector.
inc=lambda p,l: sum(a*b for a,b in zip(p,l))%Q==0
rows=[sum(1<<i for i,p in enumerate(points) if not inc(p,l)) for l in points]
assert len(set(rows))==13 and all(r.bit_count()==9 for r in rows)

# Construct cliques of common point-neighborhood by independent k-subset tests.
faces=[[] for _ in range(9)]
for size in range(1,10):
    for verts in combinations(range(13),size):
        m=sum(1<<v for v in verts)
        if any(m&r==m for r in rows):faces[size-1].append(m)
assert tuple(map(len,faces))==(13,78,286,702,1170,1014,468,117,13)

# Exact F2 ranks of simplicial boundary maps, with reduced boundary d0 to F2.
def rank_columns(columns):
    basis={}
    for x in columns:
        while x:
            k=x.bit_length()-1
            if k in basis:x^=basis[k]
            else:basis[k]=x;break
    return len(basis)
rank=[]
for dim in range(9):
    if dim==0: rank.append(1);continue
    prev={m:i for i,m in enumerate(faces[dim-1])}
    cols=[]
    for mask in faces[dim]:
        col=0
        for b in range(13):
            if mask>>b&1:col^=1<<prev[mask^(1<<b)]
        cols.append(col)
    rank.append(rank_columns(cols))
assert rank==[1,12,66,220,482,649,364,104,13],rank
bettis=[len(faces[d])-rank[d]- (rank[d+1] if d+1<9 else 0) for d in range(9)]
assert bettis==[0,0,0,0,39,1,0,0,0],bettis
print('PASS: independent projective coordinates, 13 neighborhoods of size9.')
print('PASS: direct complete f-vector:',tuple(map(len,faces)))
print('PASS: ranks (d0 reduced, d1..d8):',rank)
print('PASS: reduced F2 Betti numbers dimensions 0..8:',bettis)
