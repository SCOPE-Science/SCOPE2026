#!/usr/bin/env python3
"""Exact and exhaustive pentagon stable-set toric singular-locus certificate.
Run: python3 CHECK.py. Standard library only; no external data."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import gcd

N = 5
V = sorted({tuple(int(i in S) for i in range(N))
            for r in range(3) for S in combinations(range(N), r)
            if all((i-j) % N not in (1, N-1) for i, j in combinations(S, 2))})
assert len(V) == 11

# Every facet is stored as (primitive outward normal, right side).
H = [(tuple(-int(j == i) for j in range(N)), 0) for i in range(N)]
H += [(tuple(int(j in (i, (i+1) % N)) for j in range(N)), 1)
      for i in range(N)]
H.append(((1,)*N, 2))
assert len(H) == 11

def dot(a, b):
    return sum(x*y for x,y in zip(a,b))

def rank(rows):
    if not rows: return 0
    A = [[Fraction(x) for x in row] for row in rows]
    m, n, r = len(A), len(A[0]), 0
    for c in range(n):
        k = next((k for k in range(r, m) if A[k][c]), None)
        if k is None: continue
        A[r],A[k] = A[k],A[r]
        t = A[r][c]
        A[r] = [z/t for z in A[r]]
        for k in range(m):
            if k != r and A[k][c]:
                t = A[k][c]
                A[k] = [x-t*y for x,y in zip(A[k],A[r])]
        r += 1
        if r == m: break
    return r

def det(A):
    n = len(A)
    if n == 0: return 1
    if n == 1: return A[0][0]
    return sum(((-1)**j)*A[0][j]*det([row[:j]+row[j+1:] for row in A[1:]])
               for j in range(n))

def lattice_index(rows):
    k = rank(rows)
    if k == 0: return 1
    d = 0
    for rr in combinations(range(len(rows)), k):
        for cc in combinations(range(len(rows[0])), k):
            d = gcd(d, abs(det([[rows[i][j] for j in cc] for i in rr])))
    assert d > 0
    return d

def intersection_solution(rows, rhs):
    A = [[Fraction(x) for x in row] + [Fraction(b)] for row,b in zip(rows,rhs)]
    for c in range(N):
        k = next((k for k in range(c,N) if A[k][c]), None)
        if k is None: return None
        A[k], A[c] = A[c], A[k]
        z = A[c][c]
        A[c] = [x/z for x in A[c]]
        for i in range(N):
            if i != c:
                z = A[i][c]
                A[i] = [x-z*y for x,y in zip(A[i],A[c])]
    return tuple(row[-1] for row in A)

# The listed inequalities describe exactly the stable-set polytope:
# boundedness follows from x_i>=0 and x_i+x_{i+1}<=1;
# enumerating all 5-facet intersections finds all vertices.
assert all(dot(a,v) <= b for v in V for a,b in H)
polyvertices = set()
for ids in combinations(range(len(H)), N):
    p = intersection_solution([H[i][0] for i in ids], [H[i][1] for i in ids])
    if p is not None and all(dot(a,p) <= b for a,b in H):
        polyvertices.add(p)
assert polyvertices == set(V), (polyvertices,set(V))

incident = [sum(1 << i for i,v in enumerate(V) if dot(a,v)==b)
            for a,b in H]
# Irredundancy: each stated inequality is a true facet of dimension four.
for M in incident:
    vv = [v for i,v in enumerate(V) if M>>i&1]
    assert rank([tuple(x-y for x,y in zip(v,vv[0])) for v in vv[1:]]) == N-1

# Every nonempty face equals an intersection of a subset of facet hyperplanes.
faces = {}
for chosen in range(1<<len(H)):
    mask = (1<<len(V))-1
    for j in range(len(H)):
        if chosen>>j&1: mask &= incident[j]
    if not mask: continue
    if mask in faces: continue
    tight = [j for j,M in enumerate(incident) if mask&M == mask]
    vv = [v for i,v in enumerate(V) if mask>>i&1]
    d = rank([tuple(x-y for x,y in zip(v,vv[0])) for v in vv[1:]])
    normals = [H[j][0] for j in tight]
    codim = rank(normals)
    assert codim == N-d
    simplicial = len(tight) == codim
    smooth = simplicial and lattice_index(normals) == 1
    faces[mask] = (d,tuple(tight),smooth)

assert len(faces) == 143
assert Counter(d for d,_,_ in faces.values()) == {0:11,1:35,2:50,3:35,4:11,5:1}
singular = {mask for mask,(_,_,sm) in faces.items() if not sm}
assert Counter(faces[mask][0] for mask in singular) == {0:10,1:20,2:10}
# Every simplicial normal cone is unimodular (hence smooth).
assert all(lattice_index([H[j][0] for j in fid]) == 1
           for d,fid,sm in faces.values() if len(fid)==N-d)

max_singular = {mask for mask in singular
                if not any(mask != other and mask&other == mask for other in singular)}
assert len(max_singular)==10
assert {faces[mask][0] for mask in max_singular} == {2}

def e(i):
    return tuple(int(j==i%N) for j in range(N))

def add(a,b):
    return tuple(x+y for x,y in zip(a,b))

def mask_of(vv):
    return sum(1 << V.index(v) for v in vv)

A=[];B=[]
for i in range(N):
    A.append(mask_of([e(i), add(e(i),e(i+2)), add(e(i),e(i+3))]))
    B.append(mask_of([add(e(i),e(i+2)), add(e(i),e(i+3)), add(e(i+1),e(i+3))]))
assert len(set(A+B)) == 10
assert set(A+B) == max_singular

for mask in max_singular:
    vv = [v for i,v in enumerate(V) if mask>>i&1]
    assert len(vv)==3
    assert lattice_index([tuple(x-y for x,y in zip(v,vv[0])) for v in vv[1:]])==1
    fid=faces[mask][1]
    assert len(fid)==4
    rays=[H[j][0] for j in fid]
    assert rank(rays)==3 and lattice_index(rays)==1
    # The unique four-ray dependence is balanced with coefficients ±1.
    cc = next(c for c in combinations(range(N),3)
              if rank([[r[j] for j in c] for r in rays])==3)
    R=[[r[j] for j in cc] for r in rays]
    dep=[(-1)**i*det([r for j,r in enumerate(R) if j!=i]) for i in range(4)]
    g=gcd(*dep)
    dep=[x//g for x in dep]
    assert sorted(dep)==[-1,-1,1,1], dep
    # Each independent triple is a basis for the cone's saturated lattice.
    for ids in combinations(range(4),3):
        assert lattice_index([rays[i] for i in ids])==1

inter=Counter()
for x,y in combinations(A+B,2):
    shared = x&y
    inter[faces[shared][0] if shared else -1]+=1
assert inter=={-1:10,0:20,1:15},inter
edge_counts = Counter(sum(bool(M&F==F) for M in A+B)
                      for F,(d,_,_) in faces.items() if d==1 and F in singular)
assert edge_counts=={1:15,3:5},edge_counts
assert Counter(sum(bool(M>>i&1) for M in A+B) for i in range(len(V))) == {0:1,1:5,5:5}
print('VERIFY_OK')
print('VERTICES=11 FACETS=11 F_VECTOR=(11,35,50,35,11,1)')
print('SINGULAR_ORBITS=(10,20,10) COMPONENTS=10=5+5')
print('ALL_COMPONENTS=P2 GENERIC_TRANSVERSE=CONIFOLD')
print('INTERSECTION_PAIRS=(DISJOINT:10,POINT:20,LINE:15)')
print('SINGULAR_EDGES=(ONE_COMPONENT:15,THREE_COMPONENTS:5)')
