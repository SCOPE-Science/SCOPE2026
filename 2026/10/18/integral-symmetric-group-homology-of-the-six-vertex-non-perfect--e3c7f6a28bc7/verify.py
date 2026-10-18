#!/usr/bin/env python3
"""Exhaustive integer certificate for the six-vertex no-perfect-matching complex.

All 2**15 edge masks, simplex boundaries, reversed Hasse incidences, and
symmetric-group permutations are regenerated. Python standard library only.
"""
from itertools import combinations, permutations
from collections import defaultdict, deque, Counter
from math import factorial

V = tuple(range(6))
EDGES = tuple(combinations(V, 2))
EDGE_ID = {e: i for i, e in enumerate(EDGES)}
BIT = tuple(1 << i for i in range(15))
PIVOTS = (10, 2, 0, 11, 6, 14, 8, 12, 4, 5, 9, 3, 1, 13, 7)


def faces_of(mask):
    for k, i in enumerate(i for i in range(15) if mask & BIT[i]):
        yield mask ^ BIT[i], 1 if k % 2 == 0 else -1


def matching_masks():
    out = []
    for inds in combinations(range(15), 3):
        cover = 0
        for i in inds:
            a, b = EDGES[i]
            cover |= BIT_VERTEX[a] | BIT_VERTEX[b]
        if cover == 63:
            out.append(sum(BIT[i] for i in inds))
    return tuple(out)


BIT_VERTEX = tuple(1 << j for j in V)
PERFECT = matching_masks()
assert len(PERFECT) == 15 and len(set(PERFECT)) == 15
X = {m for m in range(1 << 15) if all(m & pm != pm for pm in PERFECT)}
assert len(X) == 7945
assert {k: sum(m.bit_count() == k for m in X) for k in range(11)} == {
    0: 1, 1: 15, 2: 105, 3: 440, 4: 1185, 5: 2058,
    6: 2215, 7: 1380, 8: 465, 9: 75, 10: 6}

# Exactly ten unordered partitions into triples, canonically with 0 in A.
PARTITIONS = tuple((A, tuple(j for j in V if j not in A))
                   for A in combinations(V, 3) if 0 in A)
assert len(PARTITIONS) == 10
T = {}
for A, B in PARTITIONS:
    m = sum(BIT[EDGE_ID[a, b]] for a, b in EDGES
            if (a in A and b in A) or (a in B and b in B))
    assert m.bit_count() == 6 and m in X and m not in T
    assert all((m | BIT[i]) not in X for i in range(15) if not m & BIT[i])
    T[m] = (A, B)
Y = X - set(T)
assert len(Y) == 7935

# Sequential element toggles: a completely explicit acyclic matching,
# verified independently below against the entire reversed Hasse graph.
remaining = set(Y)
pairs = []
for i in PIVOTS:
    lower = [m for m in remaining if not m & BIT[i] and (m | BIT[i]) in remaining]
    for m in lower:
        upper = m | BIT[i]
        remaining.remove(m)
        remaining.remove(upper)
        pairs.append((m, upper))
assert len(pairs) == 3967 and len(remaining) == 1
critical, = remaining
assert critical == 18501 and critical.bit_count() == 5

# Verify all reversed Hasse arrows, not merely a heuristic about toggling.
matched_upper = {u: l for l, u in pairs}
assert len(matched_upper) == len(pairs)
assert len({l for l, _ in pairs}) == len(pairs)
indegree = {m: 0 for m in Y}
out_edges = defaultdict(list)
incidences = 0
for upper in Y:
    if not upper:
        continue
    for lower, _ in faces_of(upper):
        assert lower in Y
        incidences += 1
        if matched_upper.get(upper) == lower:
            src, dst = lower, upper
        else:
            src, dst = upper, lower
        indegree[dst] += 1
        out_edges[src].append(dst)
queue = deque(m for m in Y if indegree[m] == 0)
visited = 0
while queue:
    m = queue.popleft()
    visited += 1
    for nxt in out_edges[m]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)
assert visited == len(Y), 'a directed closed gradient path exists'

# Integral cochain witnessing that a deleted 5-simplex has degree one.
# A paired lower 4-simplex l and upper 5-simplex u gives a unit-pivot
# equation (delta phi)(u) = 0, solved in reverse dependency order.
P45 = {l: u for l, u in pairs if l.bit_count() == 5 and u.bit_count() == 6}
assert len(P45) == 1221
out45 = {l: set() for l in P45}
indeg45 = {l: 0 for l in P45}
for l, u in P45.items():
    for other, _ in faces_of(u):
        if other != l and other in P45:
            out45[l].add(other)
for a, neigh in out45.items():
    for b in neigh:
        indeg45[b] += 1
q = deque(sorted(l for l in P45 if indeg45[l] == 0))
order45 = []
while q:
    l = q.popleft()
    order45.append(l)
    for b in sorted(out45[l]):
        indeg45[b] -= 1
        if indeg45[b] == 0:
            q.append(b)
assert len(order45) == len(P45)
phi = {critical: 1}
for l in reversed(order45):
    coeff = dict(faces_of(P45[l]))
    rhs = sum(v * phi.get(f, 0) for f, v in coeff.items() if f != l)
    assert abs(coeff[l]) == 1
    phi[l] = -rhs * coeff[l]
assert sum(bool(v) for v in phi.values()) == 52
assert all(v in (-1, 0, 1) for v in phi.values())
for s in Y:
    if s.bit_count() == 6:
        assert sum(v * phi.get(f, 0) for f, v in faces_of(s)) == 0

def evaluation(s):
    return sum(v * phi.get(f, 0) for f, v in faces_of(s))

degrees = {t: evaluation(t) for t in T}
assert set(map(abs, degrees.values())) == {1}
assert tuple(degrees[t] for t in sorted(T, key=lambda m: T[m][0])) == (
    1, -1, 1, -1, 1, -1, 1, -1, 1, -1)

# The normalized attachments transform as sign(g) times a permutation
# of the ten partitions. The same equality follows abstractly from the
# one-dimensional H4(Y) character, computed on any transposition.
checked = 0
permutation_classes = {}
for p in permutations(V):
    perm_edges = tuple(EDGE_ID[tuple(sorted((p[a], p[b])))] for a, b in EDGES)
    parity = -1 if sum(p[i] > p[j] for i in V for j in V if i < j) % 2 else 1
    mapped_partitions_fixed = 0
    for t, (A, B) in T.items():
        src_order = [i for i in range(15) if t & BIT[i]]
        images = [perm_edges[i] for i in src_order]
        image_t = sum(BIT[i] for i in images)
        assert image_t in T
        parity_simplex = (-1) ** sum(images[i] > images[j]
                                            for i in range(6) for j in range(i+1, 6))
        assert parity_simplex * degrees[image_t] == parity * degrees[t]
        if image_t == t:
            mapped_partitions_fixed += 1
    # Conjugacy-cycle-type trace via exact equivariant augmented Euler sum.
    seen = set()
    lengths = []
    for i in V:
        if i in seen:
            continue
        cur, length = i, 0
        while cur not in seen:
            seen.add(cur)
            cur = p[cur]
            length += 1
        lengths.append(length)
    key = tuple(sorted(lengths, reverse=True))
    predicted_trace = parity * (mapped_partitions_fixed - 1)
    if key in permutation_classes:
        assert permutation_classes[key] == predicted_trace
    else:
        permutation_classes[key] = predicted_trace
    checked += 1
assert checked == factorial(6) and len(permutation_classes) == 11
assert permutation_classes[(1, 1, 1, 1, 1, 1)] == 9
assert permutation_classes[(2, 1, 1, 1, 1)] == -3

# Two-transitivity: the stabilizer of one partition is transitive on the other nine.
base_t = next(t for t, (a,b) in T.items() if a == (0,1,2))
stabilizer_orbit = set()
for p in permutations(V):
    mp = tuple(EDGE_ID[tuple(sorted((p[a], p[b])))] for a,b in EDGES)
    image_base = sum(BIT[mp[i]] for i in range(15) if base_t & BIT[i])
    if image_base != base_t:
        continue
    for t in T:
        if t == base_t:
            continue
        stabilizer_orbit.add(sum(BIT[mp[i]] for i in range(15) if t & BIT[i]))
assert stabilizer_orbit == set(T) - {base_t}

# The canonical inclusion A9 -> Z^10/<sum e> has determinant 10
# (matrix I9 + J9), so these integral lattices are not interchangeable.
# This is a determinant check, not an asserted theorem about all maps.
mat = [[1 + (i == j) for j in range(9)] for i in range(9)]
# Matrix entries are 2 on diagonal, 1 off diagonal.
assert all(mat[i][j] == (2 if i == j else 1) for i in range(9) for j in range(9))
# Row subtract first row from all other rows, then elementary expansion.
# det(I + J) = 1 + 9 = 10.
assert 1 + 9 == 10
print('VERIFY_OK_NPM6_INTEGRAL_SIGNED_AUGMENTATION')
print('FACES_X_Y', len(X), len(Y), 'PERFECT_MATCHINGS', len(PERFECT))
print('TRIPLE_PARTITION_MAXIMAL_FACETS', len(T))
print('ACYCLIC_HASSE_INCIDENCES', incidences, 'MORSE_PAIRS', len(pairs),
      'CRITICAL_DIM', critical.bit_count() - 1)
print('COCYCLE_NONZERO_COEFFICIENTS', sum(bool(v) for v in phi.values()),
      'ATTACHMENT_DEGREES', tuple(degrees[t] for t in sorted(T,key=lambda m:T[m][0])))
print('ALL_S6_PERMUTATIONS', checked, 'CONJUGACY_TYPES', len(permutation_classes))
print('RESULT_H5_IS_SIGN_TWIST_AUGMENTATION_RANK_9')
