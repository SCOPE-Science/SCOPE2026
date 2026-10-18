#!/usr/bin/env python3
"""Exact standalone cellular verifier for the Petersen pentagon-torus presentation.

Run: python3 verify.py
Uses the standard library only. All ranks, determinants and signs are exact.
"""
from itertools import combinations, permutations
from collections import defaultdict


def det_bareiss(M):
    n = len(M)
    A = [list(row) for row in M]
    sign, previous = 1, 1
    for k in range(n - 1):
        if A[k][k] == 0:
            p = next((j for j in range(k + 1, n) if A[j][k]), None)
            if p is None:
                return 0
            A[k], A[p] = A[p], A[k]
            sign = -sign
        pivot = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = pivot * A[i][j] - A[i][k] * A[k][j]
                assert numerator % previous == 0
                A[i][j] = numerator // previous
            A[i][k] = 0
        previous = pivot
    return sign * A[-1][-1]


def rank_modp(columns, row_count, p):
    """Columns are sparse dictionaries row->integer coefficient."""
    pivots = {}
    for col in columns:
        v = {i: x % p for i, x in col.items() if x % p}
        while v:
            j = min(v)
            if j not in pivots:
                q = pow(v[j], -1, p)
                pivots[j] = {i: (x * q) % p for i, x in v.items() if (x * q) % p}
                break
            q = v[j]
            for i, x in pivots[j].items():
                t = (v.get(i, 0) - q * x) % p
                if t:
                    v[i] = t
                else:
                    v.pop(i, None)
    return len(pivots)


V = tuple(combinations(range(5), 2))
VI = {v: i for i, v in enumerate(V)}
E = tuple((i, j) for i, j in combinations(range(10), 2)
          if set(V[i]).isdisjoint(V[j]))
EI = {e: i for i, e in enumerate(E)}
assert len(E) == 15
adj = {i: {v for u, v in E if u == i} | {u for u, v in E if v == i}
       for i in range(10)}
C0 = tuple(combinations(range(10), 2))
C1 = tuple((ei, v) for ei, (a, b) in enumerate(E)
           for v in range(10) if v not in (a, b))
C2 = tuple((ei, ej) for ei, ej in combinations(range(15), 2)
           if set(E[ei]).isdisjoint(E[ej]))
I0 = {c: i for i, c in enumerate(C0)}
I1 = {c: i for i, c in enumerate(C1)}
I2 = {c: i for i, c in enumerate(C2)}
assert (len(C0), len(C1), len(C2)) == (45, 120, 75)

def add(x, i, a):
    x[i] = x.get(i, 0) + a
    if not x[i]:
        del x[i]

B1 = []
for ei, v in C1:
    a, b = E[ei]
    d = {}
    add(d, I0[tuple(sorted((b, v)))], 1)
    add(d, I0[tuple(sorted((a, v)))], -1)
    B1.append(d)
B2 = []
for ei, ej in C2:
    a, b = E[ei]
    c, d = E[ej]
    boundary = {}
    add(boundary, I1[(ej, b)], 1)
    add(boundary, I1[(ej, a)], -1)
    add(boundary, I1[(ei, d)], -1)
    add(boundary, I1[(ei, c)], 1)
    B2.append(boundary)
    twice = {}
    for i, coefficient in boundary.items():
        for k, v in B1[i].items():
            add(twice, k, coefficient * v)
    assert not twice

cycles = set()
for c in permutations(range(10), 5):
    if c[0] != min(c) or c[1] > c[-1]:
        continue
    if all(c[(k + 1) % 5] in adj[c[k]] for k in range(5)):
        cycles.add(c)
cycles = tuple(sorted(cycles))
assert len(cycles) == 12
pairs = tuple((c, d) for j, c in enumerate(cycles)
              for d in cycles[j + 1:] if set(c).isdisjoint(d))
assert len(pairs) == 6
relation_signs = (1, 1, -1, -1, -1, 1)

def coefficients(c):
    result = {}
    for j in range(5):
        a, b = c[j], c[(j + 1) % 5]
        ei = EI[tuple(sorted((a, b)))]
        result[ei] = 1 if a < b else -1
    return result

Z = []
for (cycle_a, cycle_b), sign in zip(pairs, relation_signs):
    v = {}
    for ei, x in coefficients(cycle_a).items():
        for ej, y in coefficients(cycle_b).items():
            pair = tuple(sorted((ei, ej)))
            assert pair in I2
            add(v, I2[pair], sign * x * y * (1 if ei < ej else -1))
    assert len(v) == 25 and set(map(abs, v.values())) == {1}
    bd = {}
    for j, x in v.items():
        for i, y in B2[j].items():
            add(bd, i, x * y)
    assert not bd
    Z.append(v)
assert all(sum(z.get(i, 0) for z in Z) == 0 for i in range(75))
R = (0, 1, 3, 10, 13)
selected_matrix = [[z.get(r, 0) for z in Z] for r in R]
assert selected_matrix == [
    [1, 0, 0, -1, 0, 0],
    [-1, 1, 0, 0, 0, 0],
    [0, 1, -1, 0, 0, 0],
    [0, 0, 0, 1, -1, 0],
    [0, -1, 0, 0, 0, 1],
]
minors = []
for omit in range(6):
    five = [[row[j] for j in range(6) if j != omit] for row in selected_matrix]
    determinant = det_bareiss(five)
    assert abs(determinant) == 1
    minors.append(determinant)
assert rank_modp(B2, len(C1), 3) == 70
assert rank_modp(B2, len(C1), 2) == 69
# Five torus columns are independent, so rank(d2)<=75-5=70.
# The 70 mod-3 pivots prove rank(d2)>=70 in characteristic zero.
# Each unimodular five-by-five projection proves integral saturation.

def vertex_map(sigma):
    return tuple(VI[tuple(sorted(sigma[x] for x in v))] for v in V)

six_partitions = {frozenset((frozenset(c), frozenset(d))): k
                  for k, (c, d) in enumerate(pairs)}

def orbit(v, p):
    seq = []
    while v not in seq:
        seq.append(v)
        v = p[v]
    assert v == seq[0]
    return frozenset(seq)

five_subgroups = set()
for sigma in permutations(range(5)):
    unseen = set(range(5))
    if orbit(0, sigma) != frozenset(range(5)):
        continue
    powers = []
    t = tuple(range(5))
    for k in range(4):
        t = tuple(sigma[i] for i in t)
        powers.append(t)
    five_subgroups.add(frozenset(powers))
assert len(five_subgroups) == 6
mapped_pairs = set()
for subgroup in five_subgroups:
    sigma = next(iter(subgroup))
    p = vertex_map(sigma)
    first = orbit(0, p)
    second = frozenset(range(10)) - first
    assert orbit(next(iter(second)), p) == second
    partition = frozenset((first, second))
    assert partition in six_partitions
    mapped_pairs.add(partition)
assert len(mapped_pairs) == 6

seen_targets = set()
for sigma in permutations(range(5)):
    p = vertex_map(sigma)
    e_perm, e_sign = [], []
    for a, b in E:
        x, y = p[a], p[b]
        e_perm.append(EI[tuple(sorted((x, y)))])
        e_sign.append(1 if x < y else -1)
    image_cells = []
    for a, b in C2:
        x, y = e_perm[a], e_perm[b]
        image_cells.append((I2[tuple(sorted((x, y)))],
                            e_sign[a] * e_sign[b] * (1 if x < y else -1)))
    # The action must permute the six reoriented torus cycles without signs.
    for j, torus in enumerate(Z):
        image = {}
        for i, x in torus.items():
            k, sign = image_cells[i]
            add(image, k, x * sign)
        matches = [k for k, other in enumerate(Z) if image == other]
        assert len(matches) == 1, (sigma, j, matches)
        if j == 0:
            seen_targets.add(matches[0])
assert len(seen_targets) == 6
print("VERIFY_OK PETERSEN_10_15 CELLS_45_120_75")
print("PENTAGONS_12 DISJOINT_PAIRS_6 TWO_TORUS_SQUARES_25_EACH")
print("SIGNED_BOUNDARY_SQUARE_ZERO TORUS_BOUNDARIES_ZERO INVARIANT_SUM_ZERO")
print("RANK_B2_MOD3_70 MOD2_69 KERNEL_INTEGRAL_RANK5")
print("FIVE_BY_FIVE_UNIMODULAR_MINORS", minors)
print("ALL_120_S5_ACTIONS_PERMUTE_SIX_REORIENTED_TORI")
print("SIX_SYLOW5_SUBGROUPS_BIJECT_TO_PENTAGON_PAIRS")
print("H2_EQUAL_Z6_MOD_DIAGONAL ANY_FIVE_TORI_INTEGRAL_BASIS")
