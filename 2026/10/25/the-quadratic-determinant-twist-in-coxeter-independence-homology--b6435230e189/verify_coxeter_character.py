#!/usr/bin/env python3
"""Exact finite verification of the Coxeter independence-homology character.

Only the Python standard library is required. Enumerations are exhaustive.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, product

MOD = 7
P = tuple(range(MOD)) + (MOD,)  # label 7 denotes infinity
DUADS = tuple(combinations(P, 2))
INDEX = {d: i for i, d in enumerate(DUADS)}


def det_point(a, b):
    x, y = (1, 0) if a == 7 else (a, 1)
    z, w = (1, 0) if b == 7 else (b, 1)
    return (x * w - y * z) % MOD


def harmonic(u, v):
    if set(u) & set(v):
        return False
    a, b = u
    c, d = v
    return (det_point(a, c) * det_point(b, d)
            + det_point(a, d) * det_point(b, c)) % MOD == 0


def neighbors_from_edges(n, edges):
    result = [0] * n
    for u, v in edges:
        result[u] |= 1 << v
        result[v] |= 1 << u
    return tuple(result)


EDGE_H = tuple((i, j) for i, j in combinations(range(28), 2)
               if harmonic(DUADS[i], DUADS[j]))
NEIGH_H = neighbors_from_edges(28, EDGE_H)
assert len(EDGE_H) == 42 and all(s.bit_count() == 3 for s in NEIGH_H)

# An independently defined model: the 28 noncollinear triples of the Fano plane.
FANO_TRIPLES = tuple(t for t in combinations(range(1, 8), 3)
                     if t[0] ^ t[1] ^ t[2])
EDGE_F = tuple((i, j) for i, j in combinations(range(28), 2)
               if not (set(FANO_TRIPLES[i]) & set(FANO_TRIPLES[j])))
NEIGH_F = neighbors_from_edges(28, EDGE_F)
# Explicit isomorphism, indexed by the lexicographic harmonic duads.
ISO = (0, 13, 25, 19, 7, 21, 10, 11, 18, 6, 20, 15, 26, 23,
       24, 17, 2, 4, 12, 8, 5, 3, 1, 9, 22, 27, 14, 16)
assert sorted(ISO) == list(range(28))
assert len(EDGE_F) == 42
for i, j in combinations(range(28), 2):
    assert bool(NEIGH_H[i] & (1 << j)) == bool(NEIGH_F[ISO[i]] & (1 << ISO[j]))
print('COXETER_MODELS_ISOMORPHIC_VERTICES_EDGES', len(DUADS), len(EDGE_H))


def independent_sets(neigh):
    faces = []
    def search(face, available):
        faces.append(face)
        while available:
            bit = available & -available
            available -= bit
            vertex = bit.bit_length() - 1
            search(face | bit, available & ~neigh[vertex])
    search(0, (1 << len(neigh)) - 1)
    return faces


FACES_F = independent_sets(NEIGH_F)
FACES_H = independent_sets(NEIGH_H)
assert len(FACES_F) == len(FACES_H) == 196009
assert Counter(x.bit_count() for x in FACES_F) == Counter(x.bit_count() for x in FACES_H)
assert sum((-1) ** x.bit_count() for x in FACES_F) == -7
print('ALL_INDEPENDENT_FACES_INCLUDING_EMPTY', len(FACES_F))
print('FACE_SIZE_COUNTS', sorted(Counter(x.bit_count() for x in FACES_F).items()))

# An explicit acyclic matching in the augmented face poset.
PIVOTS = (12, 0, 20, 1, 6, 14, 22, 2, 26, 23, 27, 16, 9, 21,
          5, 3, 10, 19, 24, 13, 18, 17, 15, 7, 11, 8, 25, 4)
active = set(FACES_F)
low_to_up = {}
up_to_low = {}
for vertex in PIVOTS:
    bit = 1 << vertex
    stage = [(s, s | bit) for s in active
             if not (s & bit) and (s | bit) in active]
    for lo, hi in stage:
        low_to_up[lo] = hi
        up_to_low[hi] = lo
        active.remove(lo)
        active.remove(hi)
assert len(low_to_up) == len(up_to_low) == 98001
assert len(active) == 7 and all(s.bit_count() == 7 for s in active)
print('MATCHED_PAIRS_AND_CRITICAL_SIX_CELLS', len(low_to_up), len(active))
print('CRITICAL_FACE_MASKS', sorted(active))

# Check Forman acyclicity by topologically sorting the complete oriented Hasse graph.
indegree = {s: 0 for s in FACES_F}
for upper in FACES_F:
    bits = upper
    while bits:
        bit = bits & -bits
        bits -= bit
        lower = upper ^ bit
        if low_to_up.get(lower) == upper:
            indegree[upper] += 1
        else:
            indegree[lower] += 1
queue = deque(s for s, deg in indegree.items() if deg == 0)
count = 0
while queue:
    face = queue.popleft()
    count += 1
    if face in low_to_up:
        hi = low_to_up[face]
        indegree[hi] -= 1
        if indegree[hi] == 0:
            queue.append(hi)
    bits = face
    while bits:
        bit = bits & -bits
        bits -= bit
        lo = face ^ bit
        if low_to_up.get(lo) == face:
            continue
        indegree[lo] -= 1
        if indegree[lo] == 0:
            queue.append(lo)
assert count == len(FACES_F)
print('ORIENTED_HASSE_DAG_NODES', count)
print('REDUCED_HOMOLOGY_ONLY_H6_Z7')


def normalize_matrix(a, b, c, d):
    vec = (a, b, c, d)
    z = next((v for v in vec if v), None)
    if z is None:
        return None
    inv = pow(z, -1, MOD)
    return tuple((v * inv) % MOD for v in vec)


def image_point(m, x):
    a, b, c, d = m
    v, w = ((a, c) if x == 7
            else ((a * x + b) % MOD, (c * x + d) % MOD))
    return (v * pow(w, -1, MOD)) % MOD if w else 7


def cycles(perm):
    seen = set()
    result = []
    for i in range(len(perm)):
        if i in seen:
            continue
        orbit = []
        j = i
        while j not in seen:
            seen.add(j)
            orbit.append(j)
            j = perm[j]
        result.append(orbit)
    return result


def signed_orbit_independence(neigh, perm):
    # A g-invariant independent set is a union of entire g-orbits.
    # Discard orbits containing edges. For the remainder, independence
    # is independence in their quotient conflict graph.
    good = []
    for orbit in cycles(perm):
        mask = sum(1 << i for i in orbit)
        if all((neigh[i] & mask) == 0 for i in orbit):
            good.append(mask)
    conflict = []
    for mask in good:
        row = 0
        for i, other in enumerate(good):
            if any((neigh[j] & other) for j in range(28) if mask & (1 << j)):
                row |= 1 << i
        conflict.append(row)

    @lru_cache(None)
    def signed_sum(available):
        if available == 0:
            return 1
        bit = available & -available
        i = bit.bit_length() - 1
        # Exclude orbit i, or include it with negative sign.
        return (signed_sum(available ^ bit)
                - signed_sum((available ^ bit) & ~conflict[i]))

    # Augmented simplicial Lefschetz equals minus the signed orbit sum.
    return -signed_sum((1 << len(good)) - 1)


def direct_lefschetz(faces, perm):
    # Independent cross-check: enumerate every face, not the quotient graph.
    total = 0
    for mask in faces:
        bits = mask
        image = 0
        images = []
        while bits:
            bit = bits & -bits
            bits -= bit
            j = perm[bit.bit_length() - 1]
            image |= 1 << j
            images.append(j)
        if image != mask:
            continue
        inversions = sum(images[i] > images[j]
                         for i in range(len(images))
                         for j in range(i + 1, len(images)))
        total += (-1) ** (len(images) + inversions)
    return -total


MATRICES = sorted({normalize_matrix(a, b, c, d)
                   for a, b, c, d in product(range(7), repeat=4)
                   if (a * d - b * c) % MOD})
assert len(MATRICES) == 336
CLASS_TABLE = Counter()
REPS = {}
SUM_TRACE = 0
for mat in MATRICES:
    a, b, c, d = mat
    point_perm = tuple(image_point(mat, x) for x in P)
    vertex_perm = tuple(INDEX[tuple(sorted((point_perm[x], point_perm[y])))]
                        for x, y in DUADS)
    assert len(set(vertex_perm)) == 28
    assert all((NEIGH_H[i] & (1 << j) != 0) ==
               (NEIGH_H[vertex_perm[i]] & (1 << vertex_perm[j]) != 0)
               for i, j in combinations(range(28), 2))
    trace = signed_orbit_independence(NEIGH_H, vertex_perm)
    determinant = (a * d - b * c) % MOD
    eta = 1 if pow(determinant, 3, MOD) == 1 else -1
    fixed_points = sum(point_perm[i] == P[i] for i in range(8))
    predicted = eta * (fixed_points - 1)
    assert trace == predicted, (mat, trace, predicted)
    point_type = tuple(sorted(Counter(len(c) for c in cycles(point_perm)).items()))
    class_key = (point_type, eta, trace)
    CLASS_TABLE[class_key] += 1
    REPS.setdefault(class_key, vertex_perm)
    SUM_TRACE += trace
assert len(CLASS_TABLE) == 8
assert sorted(CLASS_TABLE.values()) == [1, 21, 28, 42, 48, 56, 56, 84]
for class_key, permutation in sorted(REPS.items()):
    direct = direct_lefschetz(FACES_H, permutation)
    assert direct == class_key[2], (class_key, direct)
print('CHARACTER_CLASS_TABLE_BEGIN')
for key, amount in sorted(CLASS_TABLE.items()):
    print('CLASS', key, 'NUMBER', amount)
print('CHARACTER_CLASS_TABLE_END')
assert SUM_TRACE == 0
print('FULL_PGL_ORDER_AND_TRACE_SUM', len(MATRICES), SUM_TRACE)
print('RATIONAL_INVARIANTS', SUM_TRACE // len(MATRICES))
print('VERIFY_OK_COXETER_PGL_CHARACTER')
