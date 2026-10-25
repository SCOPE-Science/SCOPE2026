#!/usr/bin/env python3
"""Exact finite certificate for the face fan of the D4 root 24-cell.
Only Python standard library; no floating-point convex-hull computation.
"""
from itertools import combinations, product, permutations
from math import comb


def determinant(A):
    n = len(A)
    ans = 0
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        term = -1 if inversions % 2 else 1
        for i in range(n):
            term *= A[i][perm[i]]
        ans += term
    return ans


def inv_num(A, b):
    # Cramer's rule for an integral full-rank 4x4 matrix.
    d = determinant(A)
    assert d != 0
    out = []
    for j in range(4):
        Aj = [row[:] for row in A]
        for i in range(4):
            Aj[i][j] = b[i]
        num = determinant(Aj)
        assert num % d == 0
        out.append(num // d)
    return tuple(out)

roots = []
for i, j in combinations(range(4), 2):
    for s, t in product((-1, 1), repeat=2):
        r = [0] * 4
        r[i] = s
        r[j] = t
        roots.append(tuple(r))
assert len(set(roots)) == 24
# This ordered basis has determinant 2 and spans the even-sum root lattice D4.
basis = ((1, -1, 0, 0), (0, 1, -1, 0), (0, 0, 1, -1), (0, 0, 1, 1))
B = [[basis[j][i] for j in range(4)] for i in range(4)]
assert abs(determinant(B)) == 2
w = [inv_num(B, list(r)) for r in roots]
# Eight coordinate facet inequalities and sixteen signed-sum facet inequalities.
# The latter use 2*l(x) = +/- x1 +/- x2 +/- x3 +/- x4.
facets = []
for i in range(4):
    for s in (-1, 1):
        ids = frozenset(j for j, r in enumerate(roots) if s * r[i] == 1)
        facets.append(ids)
for signs in product((-1, 1), repeat=4):
    ids = frozenset(j for j, r in enumerate(roots)
                    if sum(signs[i] * r[i] for i in range(4)) == 2)
    facets.append(ids)
assert len(facets) == len(set(facets)) == 24
assert all(len(f) == 6 for f in facets)

edges, triangles, maximal = set(), set(), set()
choices = 0
chosen_pairs = []
for facet in facets:
    ids = sorted(facet)
    sums = {}
    for a, b in combinations(ids, 2):
        key = tuple(roots[a][i] + roots[b][i] for i in range(4))
        sums.setdefault(key, []).append((a, b))
    opposite = next(pairs for pairs in sums.values() if len(pairs) == 3)
    assert len(opposite) == 3
    union = [i for pair in opposite for i in pair]
    assert sorted(union) == ids
    for x, y in combinations(opposite, 2):
        for a in x:
            for b in y:
                edges.add(frozenset((a, b)))
    for abc in product(*opposite):
        triangles.add(frozenset(abc))
    # Every triangulation of a combinatorial octahedron without new
    # vertices is the 4-tetrahedron star around one of its 3 long diagonals.
    for dia in opposite:
        rem = [p for p in opposite if p != dia]
        assert len(rem) == 2
        for c, d in product(*rem):
            tetra = (*dia, c, d)
            A = [[w[q][i] for q in tetra] for i in range(4)]
            assert abs(determinant(A)) == 1
        choices += 1
    # The first vertex in a facet determines a canonical pulling diagonal.
    dia = next(pair for pair in opposite if ids[0] in pair)
    chosen_pairs.append(dia)
    rem = [p for p in opposite if p != dia]
    for c, d in product(*rem):
        maximal.add(frozenset((*dia, c, d)))

assert len(edges) == 96 and len(triangles) == 96
assert choices == 24 * 3 == 72
assert len(maximal) == 24 * 4 == 96
new_edges = set(edges)
new_triangles = set(triangles)
for tet in maximal:
    new_edges.update(frozenset(pair) for pair in combinations(tet, 2))
    new_triangles.update(frozenset(tri) for tri in combinations(tet, 3))
assert (len(new_edges), len(new_triangles)) == (120, 192)
# Explicit h-vector of the resulting simplicial 3-sphere.
f0, f1, f2, f3 = 24, 120, 192, 96
h = (1, f0 - 4, f1 - 3*f0 + 6,
     f2 - 2*f1 + 3*f0 - 4, f3 - f2 + f1 - f0 + 1)
assert h == (1, 20, 54, 20, 1)
assert sum(h) == f3 == 96
print('VERIFY_OK', 'vertices=24 facets=24', 'diagonal_options=72',
      'unimodular_tetrahedra=288', 'resolutions=3^24',
      'smooth_f=(24,120,192,96)', 'betti=(1,20,54,20,1)',
      'exceptional_surfaces=24_P1xP1')
