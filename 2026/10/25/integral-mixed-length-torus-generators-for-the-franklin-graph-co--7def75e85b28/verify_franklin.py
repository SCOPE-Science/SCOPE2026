#!/usr/bin/env python3
"""Exact, standard-library checks for the Franklin graph torus-lattice theorem.

Run with Python 3.9 or later. No external data or dependencies are needed.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations

N = 12
shifts = (5, -5) * 6
edges = sorted({tuple(sorted((i, j))) for i in range(N)
                for j in ((i + 1) % N, (i + shifts[i]) % N)})
edge_set = set(edges)
neighbors = [set() for _ in range(N)]
for a, b in edges:
    neighbors[a].add(b)
    neighbors[b].add(a)
assert len(edges) == 18 and all(len(neighbors[v]) == 3 for v in range(N))

def enumerate_cycles():
    out = []
    for start in range(N):
        def rec(path, mask):
            for next_v in sorted(neighbors[path[-1]]):
                if next_v == start and len(path) >= 3:
                    if path[1] < path[-1]:
                        out.append(tuple(path))
                elif next_v > start and not (mask >> next_v & 1):
                    rec(path + [next_v], mask | (1 << next_v))
        rec([start], 1 << start)
    return out

cycles = enumerate_cycles()
assert len(cycles) == 107
assert Counter(map(len, cycles)) == {4: 3, 6: 20, 8: 24, 10: 48, 12: 12}

zero_cells = list(combinations(range(N), 2))
one_cells = [(v, e) for v in range(N) for e in edges if v not in e]
two_cells = [(e, f) for j, e in enumerate(edges)
             for f in edges[j + 1:] if set(e).isdisjoint(f)]
idx0 = {c: i for i, c in enumerate(zero_cells)}
idx1 = {c: i for i, c in enumerate(one_cells)}
idx2 = {c: i for i, c in enumerate(two_cells)}
assert (len(zero_cells), len(one_cells), len(two_cells)) == (66, 180, 117)

# Orient an edge a<b from a to b; orient a square (e,f) by e then f, e<f.
d1_cols = []
for v, (a, b) in one_cells:
    d1_cols.append({idx0[tuple(sorted((v, b)))]: 1,
                    idx0[tuple(sorted((v, a)))]: -1})
d2_cols = []
for (a, b), (c, d) in two_cells:
    d2_cols.append({idx1[(b, (c, d))]: 1,
                    idx1[(a, (c, d))]: -1,
                    idx1[(d, (a, b))]: -1,
                    idx1[(c, (a, b))]: 1})
for col in d2_cols:
    bd = defaultdict(int)
    for j, s in col.items():
        for k, t in d1_cols[j].items():
            bd[k] += s * t
    assert all(x == 0 for x in bd.values())

# Product tori, one per unordered pair of vertex-disjoint simple cycles.
def oriented_edge_cycle(path):
    terms = []
    for i, v in enumerate(path):
        w = path[(i + 1) % len(path)]
        terms.append((tuple(sorted((v, w))), 1 if v < w else -1))
    return terms

product_tori = defaultdict(list)
cycle_pairs = defaultdict(list)
for i, a in enumerate(cycles):
    ca = oriented_edge_cycle(a)
    for j in range(i + 1, len(cycles)):
        b = cycles[j]
        if not set(a).isdisjoint(b):
            continue
        cb = oriented_edge_cycle(b)
        vec = defaultdict(int)
        for e, ce in ca:
            for f, cf in cb:
                q = (e, f) if e < f else (f, e)
                vec[idx2[q]] += (1 if e < f else -1) * ce * cf
        vec = {t: z for t, z in vec.items() if z}
        assert len(vec) == len(a) * len(b)
        assert all(abs(z) == 1 for z in vec.values())
        # Verify the entire torus has zero signed cellular boundary.
        boundary = defaultdict(int)
        for k, s in vec.items():
            for l, t in d2_cols[k].items():
                boundary[l] += s * t
        assert all(z == 0 for z in boundary.values())
        typ = tuple(sorted((len(a), len(b))))
        product_tori[typ].append(vec)
        cycle_pairs[typ].append((i, j))
assert {k: len(v) for k, v in product_tori.items()} == {
    (4, 4): 3, (4, 6): 12, (6, 6): 4}

def mod_rank(vectors, p):
    basis = {}
    for col in vectors:
        vec = {i: z % p for i, z in col.items() if z % p}
        while vec:
            pivot = min(vec)
            if pivot not in basis:
                inv = pow(vec[pivot], -1, p)
                basis[pivot] = {i: z * inv % p for i, z in vec.items()}
                break
            t = vec[pivot]
            for i, z in basis[pivot].items():
                new = (vec.get(i, 0) - t * z) % p
                if new:
                    vec[i] = new
                else:
                    vec.pop(i, None)
    return len(basis)

assert mod_rank(d2_cols, 101) == 108
assert mod_rank(d2_cols, 2) == 107

# A nonzero 9x9 unit minor plus rank(d2)>=108 proves that these cycles
# are a Z-basis of the whole rank-nine kernel (a primitive subgroup of Z^117).
type46 = product_tori[(4, 6)]
type66 = product_tori[(6, 6)]
ordered = type46 + type66
basis_indices = (0, 1, 2, 4, 6, 8, 12, 13, 14)
square_indices = (0, 2, 4, 7, 13, 15, 17, 39, 41)
basis_vectors = [ordered[i] for i in basis_indices]

def determinant_bareiss(a):
    a = [list(row) for row in a]
    n = len(a)
    if n == 0:
        return 1
    den = 1
    sign = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            for r in range(k + 1, n):
                if a[r][k]:
                    a[k], a[r] = a[r], a[k]
                    sign *= -1
                    break
            else:
                return 0
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % den == 0
                a[i][j] = numerator // den
            a[i][k] = 0
        den = pivot
    return sign * a[n - 1][n - 1]

minor = [[vec.get(i, 0) for vec in basis_vectors] for i in square_indices]
assert determinant_bareiss(minor) == 1

def inverse_unimodular(mat):
    n = len(mat)
    aug = [[Fraction(x) for x in row] + [Fraction(int(i == j))
           for j in range(n)] for i, row in enumerate(mat)]
    for i in range(n):
        s = next(j for j in range(i, n) if aug[j][i] != 0)
        aug[i], aug[s] = aug[s], aug[i]
        q = aug[i][i]
        aug[i] = [x / q for x in aug[i]]
        for j in range(n):
            if j != i and aug[j][i]:
                q = aug[j][i]
                aug[j] = [x - q * y for x, y in zip(aug[j], aug[i])]
    inv = [row[n:] for row in aug]
    assert all(x.denominator == 1 for row in inv for x in row)
    return [[int(x) for x in row] for row in inv]

inv = inverse_unimodular(minor)

def coordinates(vec):
    values = [vec.get(i, 0) for i in square_indices]
    coeff = [sum(inv[i][j] * values[j] for j in range(9)) for i in range(9)]
    reconstructed = defaultdict(int)
    for j, a in enumerate(coeff):
        for t, x in basis_vectors[j].items():
            reconstructed[t] += a * x
    assert {t: x for t, x in reconstructed.items() if x} == vec
    return coeff

all_coeff = {typ: [coordinates(v) for v in vs] for typ, vs in product_tori.items()}
assert all(sum(abs(x) for x in c[6:]) == 0 for c in all_coeff[(4, 4)])

def rational_rank(cols):
    pivots = {}
    for col in cols:
        vec = {i: Fraction(x) for i, x in enumerate(col) if x}
        while vec:
            q = min(vec)
            if q not in pivots:
                v = vec[q]
                pivots[q] = {i: x / v for i, x in vec.items()}
                break
            t = vec[q]
            for i, x in pivots[q].items():
                val = vec.get(i, 0) - t * x
                if val:
                    vec[i] = val
                else:
                    vec.pop(i, None)
    return len(pivots)

expected = {
    ((4, 4),): 3, ((4, 6),): 6, ((6, 6),): 4,
    ((4, 4), (4, 6)): 6, ((4, 4), (6, 6)): 7,
    ((4, 6), (6, 6)): 9,
    ((4, 4), (4, 6), (6, 6)): 9,
}
for combination, expected_rank in expected.items():
    coords = [co for typ in combination for co in all_coeff[typ]]
    assert rational_rank(coords) == expected_rank

# Integral-primitivity certificates: the following explicit determinants are
# all units. Consequently each subgroup has torsion-free quotient in H2.
unit_certificates = {
    ((4, 4),): ((0, 1, 2), (13, 17, 39), 1),
    ((4, 6),): ((0, 1, 2, 4, 6, 8), (2, 13, 15, 17, 39, 41), -1),
    ((6, 6),): ((0, 1, 2, 3), (0, 2, 4, 7), -1),
    ((4, 4), (6, 6)): ((0, 1, 2, 3, 4, 5, 6),
                         (0, 2, 4, 7, 13, 17, 39), -1),
}
for comb, (is_, js, expected_det) in unit_certificates.items():
    group = [v for typ in comb for v in product_tori[typ]]
    det = determinant_bareiss([[group[i].get(j, 0) for i in is_] for j in js])
    assert det == expected_det, (comb, det)

# Exhaust the graph automorphisms by edge-preserving backtracking.
automorphisms = []
def extend(mapping, used):
    if len(mapping) == N:
        automorphisms.append(tuple(mapping[i] for i in range(N)))
        return
    v = min((i for i in range(N) if i not in mapping),
            key=lambda i: (-sum(j in mapping for j in neighbors[i]), i))
    for w in range(N):
        if w not in used and all((u in neighbors[v]) ==
                                (mapping[u] in neighbors[w]) for u in mapping):
            mapping[v] = w
            used.add(w)
            extend(mapping, used)
            used.remove(w)
            del mapping[v]
extend({}, set())
assert len(automorphisms) == 48
cyclekeys = [frozenset(tuple(sorted((c[i], c[(i + 1) % len(c)])))
                       for i in range(len(c))) for c in cycles]
key_to_index = {k: i for i, k in enumerate(cyclekeys)}
for typ, pairs in cycle_pairs.items():
    all_pairs = set(pairs)
    orbit = set()
    for perm in automorphisms:
        for ci, cj in pairs[:1]:
            images = []
            for idx in (ci, cj):
                image_key = frozenset(tuple(sorted((perm[u], perm[v])))
                                      for u, v in cyclekeys[idx])
                images.append(key_to_index[image_key])
            orbit.add(tuple(sorted(images)))
    assert orbit == all_pairs, (typ, len(orbit), len(all_pairs))

print('VERIFY_OK_FRANKLIN_MIXED_LENGTH_INTEGRAL_TORUS_BASIS')
print('GRAPH',N,len(edges),'AUTOMORPHISMS',len(automorphisms))
print('CYCLE_LENGTH_COUNTS',dict(sorted(Counter(map(len, cycles)).items())))
print('UNORDERED_CUBICAL_CELLS',len(zero_cells),len(one_cells),len(two_cells))
print('BOUNDARY2_RANK_MOD_101_2',108,107,'INTEGRAL_H2_RANK',9)
print('TORUS_COUNTS',[(k,len(v)) for k,v in sorted(product_tori.items())])
print('TORUS_SUBLATTICE_RANKS',sorted(expected.items()))
print('UNIT_BASIS_COLUMNS',basis_indices,'ROWS',square_indices,'DETERMINANT',1)
print('THREE_SQUARE_SQUARE_TORI_INCLUDED_IN_SQUARE_HEXAGON_LATTICE')
print('BASIS_SIX_SQUARE_HEXAGON_THREE_HEXAGON_HEXAGON_TORI')
print('ALL_PARTIAL_TORUS_QUOTIENTS_TORSION_FREE')
