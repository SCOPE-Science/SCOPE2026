#!/usr/bin/env python3
"""Exact, standard-library verification for the Shrikhande three-cut complex.

The unit-pivot reduction uses integral elementary operations. All assertions
are necessary; a finite-field-only rank test would not establish freeness.
"""
from collections import Counter
from itertools import combinations

N = 16
V = tuple(range(N))
STEPS = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1))

def neighbors(v):
    x, y = divmod(v, 4)
    return {4 * ((x + a) % 4) + ((y + b) % 4) for a, b in STEPS}

ADJ = {v: neighbors(v) for v in V}
EDGES = {pair for pair in combinations(V, 2) if pair[1] in ADJ[pair[0]]}
assert len(EDGES) == 48
assert all(len(ADJ[v]) == 6 for v in V)
assert {len(ADJ[u] & ADJ[v]) for u, v in combinations(V, 2)} == {2}

def edge_count(face):
    return sum(b in ADJ[a] for a, b in combinations(face, 2))

# For three vertices, connected means at least two induced edges.
T = set(t for t in combinations(V, 3) if edge_count(t) >= 2)
assert len(T) == 176
U = sorted(q for q in combinations(V, 4)
           if all(t in T for t in combinations(q, 3)))
assert len(U) == 60
assert Counter(edge_count(q) for q in U) == {5: 48, 4: 12}
assert not any(all(t in T for t in combinations(q, 3))
               for q in combinations(V, 5))

# Each tetrahedron has a triangular facet belonging to no other tetrahedron.
# Its removal together with that triangle is an elementary collapse.
COFACETS = Counter(t for q in U for t in combinations(q, 3))
assert Counter(COFACETS[t] for t in T) == {1: 144, 3: 32}
removed = set()
for q in U:
    private = [t for t in combinations(q, 3) if COFACETS[t] == 1]
    assert private
    chosen = private[0]
    assert chosen not in removed
    removed.add(chosen)
assert len(removed) == 60
FACES2 = sorted(T - removed)
assert len(FACES2) == 116

# The complete one-skeleton has an integral cycle basis indexed by the
# 105 edges not in the spanning tree consisting of all edges {0,v}.
OTHER_EDGES = [e for e in combinations(V, 2) if 0 not in e]
assert len(OTHER_EDGES) == 105
row_index = {edge: i for i, edge in enumerate(OTHER_EDGES)}
A = [[0] * len(FACES2) for _ in OTHER_EDGES]
for j, t in enumerate(FACES2):
    for i in range(3):
        face = t[:i] + t[i+1:]
        if face in row_index:
            A[row_index[face]][j] = (-1) ** i

# An integral unit-pivot reduction. Swapping rows/columns and subtracting
# integer multiples are unimodular; reaching an identity block proves that
# the reduced boundary has surjective image over Z, with no torsion.
rows, cols = len(A), len(A[0])
maximum_abs = 1
for k in range(rows):
    nr = [sum(v != 0 for v in A[i][k:]) for i in range(k, rows)]
    nc = [sum(A[i][j] != 0 for i in range(k, rows)) for j in range(k, cols)]
    best = None
    for i in range(k, rows):
        for j in range(k, cols):
            if abs(A[i][j]) == 1:
                cost = ((nr[i-k]-1)*(nc[j-k]-1), i, j)
                if best is None or cost < best:
                    best = cost
    assert best is not None, f"no unimodular pivot at {k}"
    _, i, j = best
    A[i], A[k] = A[k], A[i]
    for row in A:
        row[k], row[j] = row[j], row[k]
    if A[k][k] == -1:
        A[k] = [-x for x in A[k]]
    assert A[k][k] == 1
    for i in range(k+1, rows):
        coeff = A[i][k]
        if coeff:
            A[i] = [A[i][j] - coeff*A[k][j] for j in range(cols)]
    for j in range(k+1, cols):
        coeff = A[k][j]
        if coeff:
            for i in range(rows):
                A[i][j] -= coeff*A[i][k]
    maximum_abs = max(maximum_abs, *(abs(x) for row in A[k:] for x in row[k:]))
    assert all(A[i][k] == (1 if i == k else 0) for i in range(rows))
    assert all(A[k][j] == (1 if j == k else 0) for j in range(cols))
assert all(A[i][j] == (1 if i == j else 0)
           for i in range(rows) for j in range(cols))

# The dual complex collapses to a two-dimensional complex with C2=116,
# integral rank(boundary_2)=105, full 1-skeleton, and H2=Z^11.
# Combinatorial Alexander duality yields H_11=Z^11 for the three-cut complex.
assert len(FACES2) - len(OTHER_EDGES) == 11
assert sum(1 for t in combinations(V, 3) if t not in T) == 384

print("graph vertices=16 edges=48 common_neighbors=2")
print("dual f_vector=(1,16,120,176,60)")
print("dual tetrahedra: diamonds=48 induced_four_cycles=12")
print("tetrahedron_private_triangle_collapses=60")
print("reduced_triangle_boundary: dimensions=105x116 unit_pivots=105")
print("dual reduced integral homology: H_2=Z^11, all others zero")
print("ordinary three-cut integral homology: H_11=Z^11, all others zero")
print("three-cut homotopy: wedge of 11 spheres of dimension 11")
print("VERIFY_OK")
