#!/usr/bin/env python3
"""Exact finite certificate for the normal-fan singularities of STAB(C7).
Requires Python 3.10+ and SymPy 1.10+; no network or external datasets.
All calculations are over the integers and rational numbers.
"""
from collections import Counter
from functools import reduce
from itertools import combinations, product
from math import gcd
import sympy as sp

N = 7
VS = [tuple(x) for x in product((0, 1), repeat=N)
      if all(x[i] + x[(i + 1) % N] <= 1 for i in range(N))]
assert len(VS) == 29

NORMALS, RHS = [], []
for i in range(N):
    row = [0] * N
    row[i] = -1
    NORMALS.append(tuple(row)); RHS.append(0)
for i in range(N):
    row = [0] * N
    row[i] = row[(i + 1) % N] = 1
    NORMALS.append(tuple(row)); RHS.append(1)
NORMALS.append((1,) * N); RHS.append(3)
assert len(NORMALS) == 15


def matrix_rank(rows):
    return sp.Matrix(rows).rank() if rows else 0


def lattice_index(rows):
    """Index of the span of independent integral vectors in its saturation.
    Uses the gcd of maximal minors, not floating-point volume.
    """
    rank = matrix_rank(rows)
    if not rank:
        return 1
    assert len(rows) == rank
    A = sp.Matrix(rows).T
    return reduce(gcd, (abs(int(A.extract(I, range(rank)).det()))
                       for I in combinations(range(A.rows), rank)))


# Certify the inequality representation, rather than merely assuming it.
# A bounded 7-dimensional polyhedron has vertices at independent 7-fold
# intersections of its bounding hyperplanes.
feasible_vertices = set()
for I in combinations(range(15), N):
    A = sp.Matrix([NORMALS[i] for i in I])
    if A.det() == 0:
        continue
    sol = tuple(A.inv() * sp.Matrix([RHS[i] for i in I]))
    if all(sum(a * x for a, x in zip(normal, sol)) <= c
           for normal, c in zip(NORMALS, RHS)):
        feasible_vertices.add(sol)
assert feasible_vertices == set(VS), (len(feasible_vertices), len(VS))
# Boundedness follows from nonnegativity and adjacent edge inequalities.
# All 15 inequalities really are facets (supporting vertices span dimension 6).
FMS = []
for normal, c in zip(NORMALS, RHS):
    face_indices = [j for j, v in enumerate(VS)
                    if sum(x*y for x,y in zip(normal, v)) == c]
    FMS.append(sum(1 << j for j in face_indices))
    u = VS[face_indices[0]]
    assert matrix_rank([tuple(VS[j][t] - u[t] for t in range(N))
                        for j in face_indices[1:]]) == N-1


# Every nonempty face is an intersection of a subset of the 15 facets.
faces = {(1 << len(VS)) - 1}
for facet_mask in FMS:
    faces |= {q & facet_mask for q in tuple(faces) if q & facet_mask}
assert len(faces) == 1151

rows = []
for mask in faces:
    active = tuple(i for i, fm in enumerate(FMS) if mask & fm == mask)
    rank = matrix_rank([NORMALS[i] for i in active])
    dim = N - rank
    if len(active) != rank:
        singular = True
    else:
        singular = lattice_index([NORMALS[i] for i in active]) != 1
    rows.append((mask, active, dim, singular))
assert Counter((d, s) for _, _, d, s in rows) == {
    (0, True):28, (0, False):1,
    (1, True):105, (1, False):35,
    (2, True):126, (2, False):175,
    (3, True):56, (3, False):294,
    (4, True):7, (4, False):224,
    (5, False):84, (6, False):15, (7, False):1,
}
assert sum(r[3] for r in rows) == 322
# In particular every simplicial cone is unimodular.
assert all(len(active) > N - dim for _, active, dim, bad in rows if bad)

singular_rows = [r for r in rows if r[3]]
maximal = [r for r in singular_rows
           if not any(r[0] != s[0] and r[0] & s[0] == r[0]
                      for s in singular_rows)]
assert len(maximal) == 14
assert Counter(r[2] for r in maximal) == {3: 7, 4: 7}


def vertex_mask(predicate):
    return sum(1 << j for j, v in enumerate(VS) if predicate(v))


# Type A: one selected vertex of C7. This is STAB(the residual path P4).
A_faces = set()
for i in range(N):
    f = vertex_mask(lambda v: v[i] == 1)
    A_faces.add(f)
    r = next(z for z in maximal if z[0] == f)
    assert r[2] == 4 and len(r[1]) == 4 and f.bit_count() == 8
    assert set(r[1]) == {(i-1)%N, (i+1)%N, N+(i-1)%N, N+i}

# Type B: maximal three-element independent subsets avoiding a fixed vertex.
# Matching edges within the six remaining path vertices, plus the odd-hole facet.
B_faces = set()
for i in range(N):
    pairs = [((i+1+2*t)%N, (i+2+2*t)%N) for t in range(3)]
    f = vertex_mask(lambda v: v[i] == 0 and all(v[a] + v[b] == 1
                                                for a,b in pairs))
    B_faces.add(f)
    r = next(z for z in maximal if z[0] == f)
    assert r[2] == 3 and len(r[1]) == 5 and f.bit_count() == 4
    assert set(r[1]) == {i, N+(i+1)%N, N+(i+3)%N, N+(i+5)%N, 2*N}
    pts = [VS[t] for t in range(len(VS)) if (f >> t) & 1]
    assert lattice_index([tuple(pts[j][a] - pts[0][a] for a in range(N))
                          for j in range(1,4)]) == 1
assert A_faces.isdisjoint(B_faces)
assert A_faces | B_faces == {r[0] for r in maximal}

# Check every minimal nonregular cone, not just one representative.
# One primitive integral circuit identifies each as a Segre cone.
for r in maximal:
    rays = [NORMALS[j] for j in r[1]]
    rank = N - r[2]
    M = sp.Matrix(rays).T
    ker = M.nullspace()
    assert len(ker) == 1
    rel = list(ker[0])
    assert all(abs(x) == 1 for x in rel)
    signs = tuple(sorted((sum(bool(x > 0) for x in rel), sum(bool(x < 0) for x in rel))))
    assert signs == ((2, 2) if r[2] == 4 else (2, 3))
    assert all(lattice_index([ray for j,ray in enumerate(rays) if j != skip]) == 1
               for skip in range(len(rays)))

print('VERIFY_OK: 29 vertices; 15 facets; 1151 faces; 322 singular orbits;')
print('14 maximal singular faces (7 dim4 conifold, 7 dim3 Segre 2x3);')
print('all simplicial normal cones unimodular; local circuit lattices saturated.')
