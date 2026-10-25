#!/usr/bin/env python3
"""Reproduce the finite combinatorial checks for the Shrikhande three-cut theorem.

Only Python's standard library is required. This is a consistency checker;
proof of the integral homotopy statement is in RESULT.md.
"""
from collections import Counter
from itertools import combinations, product

V = tuple(product(range(4), repeat=2))
idx = {v: i for i, v in enumerate(V)}
steps = ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1))
A = [[False]*16 for _ in V]
for i, (a,b) in enumerate(V):
    for dx,dy in steps:
        A[i][idx[((a+dx)%4,(b+dy)%4)]] = True
assert all(sum(row)==6 for row in A)
assert all(sum(A[u][w] and A[v][w] for w in range(16))==2
           for u,v in combinations(range(16),2))
for u in range(16):
    nei = [v for v in range(16) if A[u][v]]
    assert len(nei)==6
    assert all(sum(A[v][w] for w in nei)==2 for v in nei)

E = {p for p in combinations(range(16),2) if A[p[0]][p[1]]}
T = {t for t in combinations(range(16),3) if all(A[i][j] for i,j in combinations(t,2))}
assert (len(E),len(T))==(48,32)
assert all(sum(set(e).issubset(t) for t in T)==2 for e in E)

# An Alexander-dual face is a set containing no disconnected triple.
def connected3(t):
    return sum(A[u][v] for u,v in combinations(t,2))>=2

def qualifies(c):
    return all(connected3(t) for t in combinations(c,3))

faces = [list(combinations(range(16),k)) for k in (1,2)]
faces += [[c for c in combinations(range(16),k) if qualifies(c)] for k in (3,4,5)]
assert [len(x) for x in faces] == [16,120,176,60,0]
assert len([q for q in faces[3] if sum(A[u][v] for u,v in combinations(q,2))==5]) == 48
assert len([q for q in faces[3] if sum(A[u][v] for u,v in combinations(q,2))==4]) == 12

# Every tetrahedron contains at least two globally free triangular faces.
incidence = Counter(t for q in faces[3] for t in combinations(q,3))
assert Counter(incidence.values()) == Counter({1:144,3:32})
assert Counter(sum(incidence[t]==1 for t in combinations(q,3))
               for q in faces[3]) == Counter({2:48,4:12})

# The two four-step coordinate loops bound tetrahedra in the dual.
for fixed in range(4):
    for coord in (0,1):
        c = tuple(sorted(idx[(k,fixed) if coord==0 else (fixed,k)] for k in range(4)))
        assert c in faces[3]

# Independently recompute signed simplicial boundary ranks over finite fields.
def rank_mod_p(nrows, ncols, col_faces, row_faces, p):
    rows = [[0]*ncols for _ in range(nrows)]
    rindex = {c:i for i,c in enumerate(row_faces)}
    for j,f in enumerate(col_faces):
        for i in range(len(f)):
            sub = f[:i]+f[i+1:]
            rows[rindex[sub]][j] = (1 if i%2==0 else p-1)
    basis = {}
    for row in rows:
        while True:
            pivot = next((i for i,x in enumerate(row) if x%p),None)
            if pivot is None:break
            if pivot not in basis:
                k = pow(row[pivot],-1,p)
                basis[pivot] = [(x*k)%p for x in row]
                break
            f=row[pivot]
            br=basis[pivot]
            row=[(a-f*b)%p for a,b in zip(row,br)]
    return len(basis)

for p in (2,3,5):
    ranks=[rank_mod_p(len(faces[k-1]),len(faces[k]),faces[k],faces[k-1],p)
           for k in (1,2,3)]
    assert ranks == [15,105,60],(p,ranks)
    bettis = [len(faces[0])-ranks[0],
              len(faces[1])-ranks[0]-ranks[1],
              len(faces[2])-ranks[1]-ranks[2],
              len(faces[3])-ranks[2]]
    assert bettis == [1,0,11,0],(p,bettis)

assert sum((-1)**k*len(faces[k]) for k in range(4))==12
print('VERIFY_OK: 16 vertices, 48 graph edges, 32 graph triangles;')
print('dual f-vector (16,120,176,60), 60 collapsible tetrahedra,')
print('boundary ranks (15,105,60) mod 2,3,5, Betti vector (1,0,11,0).')
