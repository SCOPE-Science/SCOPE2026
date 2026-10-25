#!/usr/bin/env python3
"""Exact verification for shortest geometric cycles in the Petersen matching complex.

Requires Python 3.10+ and SymPy 1.12+. All objects are generated directly from
Petersen = KG(5,2); no data file, cached matrix, or external service is needed.
"""
from itertools import combinations, permutations, product
from collections import defaultdict
from sympy import Matrix, SparseMatrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

V = list(combinations(range(5), 2))
E = sorted((u, v) for u, v in combinations(V, 2) if set(u).isdisjoint(v))
assert len(V) == 10 and len(E) == 15
edge_id = {edge: i for i, edge in enumerate(E)}
F = {d: [c for c in combinations(range(15), d + 1)
          if len({v for j in c for v in E[j]}) == 2 * (d + 1)]
     for d in range(5)}
assert tuple(len(F[d]) for d in range(5)) == (15, 75, 145, 90, 6)

def boundary(d):
    prev = {f: i for i, f in enumerate(F[d - 1])}
    return SparseMatrix(len(F[d - 1]), len(F[d]), {
        (prev[face[:j] + face[j + 1:]], col): (-1) ** j
        for col, face in enumerate(F[d]) for j in range(d + 1)})

D = {d: boundary(d) for d in range(1, 5)}
for d in range(2, 5):
    assert D[d - 1] * D[d] == SparseMatrix(D[d - 1].rows, D[d].cols, {})

def invariant_factors(M):
    diag = smith_normal_form(M, domain=ZZ)
    return tuple(abs(int(diag[i, i])) for i in range(min(diag.shape)) if diag[i, i])

boundary_factors = {d: invariant_factors(D[d]) for d in D}
assert [len(boundary_factors[d]) for d in range(1, 5)] == [14, 61, 79, 6]
assert all(set(factors) == {1} for factors in boundary_factors.values())
assert 145 - 61 - 79 == 5 and 90 - 79 - 6 == 5

# An induced six-vertex octahedral two-sphere is exactly three disjoint
# conflicting pairs of Petersen edges, with no other conflicts between them.
spheres = []
for W in combinations(range(15), 6):
    conflict = [(a, b) for a, b in combinations(W, 2) if set(E[a]) & set(E[b])]
    if len(conflict) == 3 and len({x for pair in conflict for x in pair}) == 6:
        spheres.append(tuple(sorted(conflict)))
assert len(spheres) == 110 and len(set(spheres)) == len(spheres)
sphere_id = {x: i for i, x in enumerate(spheres)}
face2_id = {f: i for i, f in enumerate(F[2])}

def orientation_sign(seq):
    return (-1) ** sum(seq[i] > seq[j]
                       for i in range(len(seq)) for j in range(i + 1, len(seq)))

def sphere_column(sphere):
    out = {}
    for choices in product((0, 1), repeat=3):
        tri = tuple(sphere[k][choices[k]] for k in range(3))
        coeff = (-1) ** sum(choices) * orientation_sign(tri)
        out[face2_id[tuple(sorted(tri))]] = coeff
    assert len(out) == 8
    v = SparseMatrix(145, 1, {(i, 0): c for i, c in out.items()})
    assert D[2] * v == SparseMatrix(75, 1, {})
    return v

Z = [sphere_column(sphere) for sphere in spheres]

def edge_map(perm):
    return tuple(edge_id[tuple(sorted((tuple(sorted(perm[t] for t in u)),
                                       tuple(sorted(perm[t] for t in v))))) ]
                 for u, v in E)

def sphere_action(sphere, emap):
    return tuple(sorted(tuple(sorted(emap[i] for i in pair)) for pair in sphere))

orbit_reps = []
unseen = set(range(len(spheres)))
all_permutations = list(permutations(range(5)))
edge_maps = [edge_map(p) for p in all_permutations]
while unseen:
    i = min(unseen)
    orbit = {sphere_id[sphere_action(spheres[i], m)] for m in edge_maps}
    assert orbit <= unseen
    unseen -= orbit
    orbit_reps.append((i, sorted(orbit)))
assert [len(x[1]) for x in orbit_reps] == [10, 60, 40]
assert [spheres[i] for i, _ in orbit_reps] == [
    ((0, 1), (3, 4), (6, 9)),
    ((0, 1), (3, 4), (6, 12)),
    ((0, 1), (3, 5), (6, 7))]

# The kernel of D[2] is saturated in the integral two-chain group.
# Hence the torsion in coker([D[3]|octahedral sphere columns]) is exactly
# the finite quotient H_2/shortest-sphere span, provided the rank is 84.
orbit_quotients = []
for i, orb in orbit_reps:
    A = D[3].row_join(Matrix.hstack(*(Z[j] for j in orb)))
    factors = invariant_factors(A)
    assert len(factors) == 84
    orbit_quotients.append(tuple(x for x in factors if x != 1))
assert orbit_quotients == [(2,), (), ()]
for i, _ in orbit_reps:
    A = D[3].row_join(Z[i])
    factors = invariant_factors(A)
    assert len(factors) == 80 and set(factors) == {1}

# Full S_5 homology characters over Q, independently using rational kernels,
# signed cellular actions, and the equivariant Euler-Poincare identity.
K = Matrix.hstack(*D[3].nullspace())
B = Matrix(D[4])
assert K.shape == (90, 11) and B.shape == (90, 6)
rowsK = list((K.T).rref()[1]); rowsB = list((B.T).rref()[1])
invK = K.extract(rowsK, list(range(11))).inv()
invB = B.extract(rowsB, list(range(6))).inv()

def action_on_three_chains(emap):
    idx = {f: i for i, f in enumerate(F[3])}
    return SparseMatrix(90, 90, {
        (idx[tuple(sorted(emap[t] for t in f))], j):
        orientation_sign(tuple(emap[t] for t in f))
        for j, f in enumerate(F[3])})

def chain_trace(d, emap):
    return sum(orientation_sign(tuple(emap[t] for t in f))
               for f in F[d] if tuple(sorted(emap[t] for t in f)) == f)

def cycle_type(p):
    seen, lengths = set(), []
    for i in range(5):
        if i not in seen:
            j, n = i, 0
            while j not in seen:
                seen.add(j); n += 1; j = p[j]
            lengths.append(n)
    return tuple(sorted(lengths, reverse=True))

reps = {}
for p in all_permutations:
    reps.setdefault(cycle_type(p), p)
character_rows = []
for typ, p in sorted(reps.items()):
    emap = edge_map(p)
    P3 = action_on_three_chains(emap)
    tr_K = (invK * (P3 * K).extract(rowsK, list(range(11)))).trace()
    tr_B = (invB * (P3 * B).extract(rowsB, list(range(6)))).trace()
    h3 = int(tr_K - tr_B)
    lefschetz = -1 + sum((-1) ** d * chain_trace(d, emap) for d in range(5))
    h2 = h3 + lefschetz
    fixed = typ.count(1)
    sign = (-1) ** (5 - len(typ))
    assert h2 == sign * fixed
    assert h3 == fixed * (fixed - 1) // 2 + typ.count(2) - fixed
    character_rows.append((typ, h2, h3))
assert [x[1:] for x in character_rows] == [
    (5, 5), (-3, 1), (1, 1), (2, -1), (0, 1), (-1, -1), (0, 0)]
print('VERIFY_OK_PETERSEN_MATCHING_MINIMUM_OCTAHEDRAL_SPHERES')
print('PETERSEN_VERTICES_EDGES', len(V), len(E))
print('MATCHING_COMPLEX_FACE_VECTOR', tuple(len(F[d]) for d in range(5)))
print('INTEGRAL_BOUNDARY_RANKS', tuple(len(boundary_factors[d]) for d in range(1, 5)))
print('ALL_BOUNDARY_SMITH_FACTORS_UNIT', True)
print('INTEGRAL_H2_H3_RANKS', 5, 5)
print('MINIMUM_SIX_VERTEX_OCTAHEDRAL_SPHERES', len(spheres))
print('S5_OCTAHEDRAL_ORBIT_SIZES', tuple(len(x[1]) for x in orbit_reps))
print('ORBIT_QUOTIENT_NONUNIT_SMITH', tuple(orbit_quotients))
print('ONE_SPHERE_FROM_EACH_ORBIT_PRIMITIVE', True)
print('S5_CHARACTER_ROWS', character_rows)
print('H2_SIGN_TWIST_FIVE_POINT_PERMUTATION_H3_SPECHT_3_2', True)
