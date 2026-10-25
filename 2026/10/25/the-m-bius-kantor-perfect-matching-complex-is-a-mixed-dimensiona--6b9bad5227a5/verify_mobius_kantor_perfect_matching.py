#!/usr/bin/env python3
"""Standalone exact finite certificate for the Möbius--Kantor perfect-matching complex.

Only the Python standard library is required. Run with Python >=3.9.
"""
from collections import Counter, deque
from functools import lru_cache

N = 8
EDGES = sorted(
    {tuple(sorted((i, (i + 1) % N))) for i in range(N)}
    | {(i, i + N) for i in range(N)}
    | {tuple(sorted((i + N, (i + 3) % N + N))) for i in range(N)}
)
ORDER = [23, 22, 21, 6, 19, 11, 17, 4, 20, 14, 13, 12,
         7, 8, 9, 15, 18, 10, 5, 16, 3, 2, 1, 0]
assert len(EDGES) == 24 and sorted(ORDER) == list(range(24))
incidence = [[] for _ in range(16)]
for j, (a, b) in enumerate(EDGES):
    incidence[a].append(j)
    incidence[b].append(j)

perfect = []
def enumerate_perfect(remaining, chosen):
    if not remaining:
        perfect.append(tuple(sorted(chosen)))
        return
    a = min(remaining)
    for e in incidence[a]:
        x, y = EDGES[e]
        b = x ^ y ^ a
        if b in remaining:
            enumerate_perfect(remaining - {a, b}, chosen + [e])

enumerate_perfect(set(range(16)), [])
assert len(perfect) == 33 and len(set(perfect)) == 33
faces = set()
for match in perfect:
    for q in range(1, 1 << 8):
        faces.add(sum(1 << match[i] for i in range(8) if (q >> i) & 1))
assert len(faces) == 6051
bydim = {}
for m in faces:
    bydim.setdefault(m.bit_count() - 1, []).append(m)
for v in bydim.values():
    v.sort()
face_vector = tuple(len(bydim[d]) for d in range(8))
assert face_vector == (24, 228, 984, 1842, 1752, 924, 264, 33)

@lru_cache(None)
def boundary(m):
    bits = [i for i in range(24) if m & (1 << i)]
    return tuple((m ^ (1 << i), (-1) ** j) for j, i in enumerate(bits))

remaining = set(faces)
matched_pairs = []
for edge_idx in ORDER:
    bit = 1 << edge_idx
    stage = [(m, m | bit) for m in sorted(remaining)
             if not m & bit and m | bit in remaining]
    for lower, upper in stage:
        assert lower in remaining and upper in remaining
        remaining.remove(lower)
        remaining.remove(upper)
    matched_pairs.extend(stage)
critical = remaining
critical_by_dim = {d: sorted(m for m in critical if m.bit_count() - 1 == d)
                   for d in range(8)}
assert len(matched_pairs) == 3019 and len(critical) == 13
assert tuple(len(critical_by_dim[d]) for d in range(8)) == (1, 0, 4, 8, 0, 0, 0, 0)
assert critical_by_dim[2] == [32848, 2752512, 4333568, 5244928]
assert critical_by_dim[3] == [278720, 527364, 527392, 1097729,
                            1163264, 1327112, 2113666, 2162736]
matched_lower = dict(matched_pairs)
matched_upper = {b: a for a, b in matched_pairs}
assert len(matched_lower) == len(matched_upper) == len(matched_pairs)

# Complete Hasse graph orientation: matched lower->upper, all other upper->lower.
indegree = {f: 0 for f in faces}
outgoing = {f: [] for f in faces}
incidence_count = 0
for upper in faces:
    for lower, _ in boundary(upper):
        if not lower:   # omit the empty simplex from nonaugmented face poset
            continue
        assert lower in faces
        if matched_lower.get(lower) == upper:
            outgoing[lower].append(upper)
            indegree[upper] += 1
        else:
            outgoing[upper].append(lower)
            indegree[lower] += 1
        incidence_count += 1
assert incidence_count == 27192
queue = deque(f for f, degree in indegree.items() if degree == 0)
visited = 0
while queue:
    u = queue.popleft()
    visited += 1
    for v in outgoing[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            queue.append(v)
assert visited == len(faces), 'discrete-Morse vector field has a cycle'

# Integral Morse boundary via explicit signed gradient-path recursion.
@lru_cache(None)
def project(cell):
    if cell in matched_upper:
        return {}
    if cell in critical:
        return {cell: 1}
    upper = matched_lower[cell]
    coefficient = next(sign for lower, sign in boundary(upper) if lower == cell)
    terms = Counter()
    for other, sign in boundary(upper):
        if other == cell:
            continue
        for critical_cell, value in project(other).items():
            terms[critical_cell] -= coefficient * sign * value
    return {k: v for k, v in terms.items() if v}

morse_matrix = []
for upper in critical_by_dim[3]:
    terms = Counter()
    for lower, sign in boundary(upper):
        for critical_cell, value in project(lower).items():
            terms[critical_cell] += sign * value
    morse_matrix.append([terms[cell] for cell in critical_by_dim[2]])
assert morse_matrix == [[0] * 4 for _ in range(8)]

# Independent simplicial mod-2 boundary ranks.
def rank_mod2(columns):
    pivots = {}
    for column in columns:
        x = column
        while x:
            bit = x.bit_length() - 1
            if bit not in pivots:
                pivots[bit] = x
                break
            x ^= pivots[bit]
    return len(pivots)

ranks = {}
for d in range(1, 8):
    lower_index = {f: i for i, f in enumerate(bydim[d - 1])}
    columns = []
    for f in bydim[d]:
        bitcol = 0
        for face, _ in boundary(f):
            bitcol ^= 1 << lower_index[face]
        columns.append(bitcol)
    ranks[d] = rank_mod2(columns)
assert ranks == {1: 23, 2: 205, 3: 775, 4: 1059, 5: 693, 6: 231, 7: 33}
assert tuple(len(bydim[d]) - ranks.get(d, 0) - ranks.get(d + 1, 0)
             for d in range(1, 7)) == (0, 4, 8, 0, 0, 0)

# Independently enumerate every graph matching, not merely its extendible members.
vertex_bits = [(1 << a) | (1 << b) for a, b in EDGES]
all_matchings = {0}
for edge_idx in range(24):
    for mask in tuple(all_matchings):
        if all(not (mask & (1 << other)) or not
               (vertex_bits[edge_idx] & vertex_bits[other])
               for other in range(edge_idx)):
            all_matchings.add(mask | (1 << edge_idx))
bad = all_matchings - faces - {0}
assert len(all_matchings) - 1 == 11067 and len(bad) == 5016
minimal = [m for m in bad if all(
    m ^ (1 << i) not in bad for i in range(24) if m & (1 << i))]
assert Counter(m.bit_count() for m in minimal) == {3: 112, 4: 120}

print('graph: GP(8,3), vertices=16, edges=24')
print('perfect matchings:', len(perfect))
print('complex nonempty simplices:', len(faces), 'face vector:', face_vector)
print('discrete-Morse pairs:', len(matched_pairs), 'critical vector:',
      tuple(len(critical_by_dim[d]) for d in range(8)))
print('Hasse incidences:', incidence_count, 'acyclic topological sort:', visited)
print('exact integral Morse boundary degree 3->2: 4 by 8 zero matrix')
print('independent mod-2 boundary ranks:', ranks)
print('nonextendible matchings:', len(bad), 'minimal obstruction sizes:',
      sorted(Counter(m.bit_count() for m in minimal).items()))
print('HOMOTOPY: wedge of 4 S^2 and 8 S^3')
print('VERIFY_OK')
