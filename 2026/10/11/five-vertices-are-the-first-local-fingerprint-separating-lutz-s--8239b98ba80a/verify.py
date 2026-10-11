#!/usr/bin/env python3
from itertools import combinations
from collections import Counter

V = tuple(range(1, 13))
F38 = [
(1,2,6,9),(1,2,6,12),(1,2,9,12),(1,3,5,8),(1,3,5,11),(1,3,8,11),(2,3,4,7),(2,3,4,10),(2,3,7,10),
(1,5,8,10),(1,5,10,11),(1,6,7,9),(1,6,7,12),(1,7,8,10),(1,7,8,11),(1,7,10,12),(1,9,10,12),
(2,4,5,7),(2,4,5,10),(2,5,8,10),(2,6,9,11),(2,7,8,10),(2,7,8,11),(2,8,9,11),(2,8,9,12),
(3,4,6,7),(3,4,6,10),(3,5,9,11),(3,6,7,12),(3,7,10,12),(3,8,9,11),(3,8,9,12),(3,9,10,12),
(4,5,6,7),(4,5,6,10),(5,6,7,9),(5,6,9,11),(5,6,10,11)]
A = [f for f in F38 if f != (2,4,5,7)]
B = [f for f in F38 if f != (3,4,6,10)]


def faces_of(facets, vertices=V):
    vertices=set(vertices)
    faces=set()
    for facet in facets:
        inter=tuple(sorted(vertices.intersection(facet)))
        for r in range(1, len(inter)+1):
            faces.update(combinations(inter, r))
    return faces


def fvector(faces):
    if not faces:
        return ()
    m=max(map(len, faces))
    return tuple(sum(len(s)==r for s in faces) for r in range(1,m+1))


def gf2_rank(rows, ncols):
    rows=[r for r in rows if r]
    rank=0
    for col in range(ncols):
        pivot=next((i for i in range(rank,len(rows)) if (rows[i]>>col)&1), None)
        if pivot is None:
            continue
        rows[rank],rows[pivot]=rows[pivot],rows[rank]
        for i in range(len(rows)):
            if i != rank and ((rows[i]>>col)&1):
                rows[i] ^= rows[rank]
        rank += 1
        if rank == len(rows):
            break
    return rank


def betti_f2(faces):
    if not faces:
        return ()
    dmax=max(map(len,faces))-1
    simplices={d:sorted(s for s in faces if len(s)==d+1) for d in range(dmax+1)}
    ranks={}
    for d in range(1,dmax+1):
        lower={s:i for i,s in enumerate(simplices[d-1])}
        rows=[0]*len(simplices[d-1])
        for j,s in enumerate(simplices[d]):
            for t in combinations(s,d):
                rows[lower[t]] ^= 1 << j
        ranks[d]=gf2_rank(rows,len(simplices[d]))
    return tuple(len(simplices[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(dmax+1))


def profile(facets,k):
    out=Counter()
    for S in combinations(V,k):
        fs=faces_of(facets,S)
        out[(fvector(fs),betti_f2(fs))]+=1
    return out


def boundary_triangles(facets):
    c=Counter()
    for f in facets:
        for t in combinations(f,3):
            c[tuple(sorted(t))]+=1
    return {t for t,n in c.items() if n==1}

assert len(F38)==38 and len(A)==37 and len(B)==37
assert fvector(faces_of(A))==(12,58,84,37)
assert fvector(faces_of(B))==(12,58,84,37)
assert betti_f2(faces_of(A))==(1,0,0,0)
assert betti_f2(faces_of(B))==(1,0,0,0)

perm={1:1,2:3,3:2,4:4,5:6,6:5,7:10,10:7,8:12,12:8,9:11,11:9}
ba,bb=boundary_triangles(A),boundary_triangles(B)
assert len(ba)==20 and len(bb)==20
assert {tuple(sorted(perm[v] for v in t)) for t in ba}==bb

sizes=[]
for k in range(1,5):
    pa,pb=profile(A,k),profile(B,k)
    assert pa==pb
    sizes.append(len(pa))
pa,pb=profile(A,5),profile(B,5)
assert pa!=pb
assert len(pa)==len(pb)==38 and sum(pa.values())==sum(pb.values())==792
expected={
 ((5,10,4),(1,2,0)): 1,
 ((5,9,4),(1,1,0)): 1,
 ((5,8,1),(1,3,0)): 1,
 ((5,8,2),(1,2,0)): -1,
 ((5,9,2),(1,3,0)): -1,
 ((5,10,5),(1,1,0)): -1,
}
got={key:pa[key]-pb[key] for key in set(pa)|set(pb) if pa[key]!=pb[key]}
assert got==expected
print('VERIFY_OK facets=37 f=12,58,84,37 boundary_triangles=20 boundary_iso=explicit profiles_equal_k=1..4 distinct=1,2,5,14 first_difference_k=5 profiles5=38 subsets5=792 shifts=+1:+1:+1,-1:-1:-1')
