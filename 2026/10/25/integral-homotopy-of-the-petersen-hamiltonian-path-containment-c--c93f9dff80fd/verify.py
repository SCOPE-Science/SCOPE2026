#!/usr/bin/env python3
"""Exact integer and finite-poset verification for the Petersen path-containment complex.

All graph and face data are reconstructed from the Kneser KG(5,2) definition.
Requires Python 3.10+ and the standard library only.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations, permutations

vertices = list(combinations(range(5), 2))
vertex_id = {v: i for i, v in enumerate(vertices)}
edges = [(i, j) for i in range(10) for j in range(i + 1, 10)
         if set(vertices[i]).isdisjoint(vertices[j])]
assert len(edges) == 15
edge_id = {e: i for i, e in enumerate(edges)}
adj = [[] for _ in vertices]
for a, b in edges:
    adj[a].append(b)
    adj[b].append(a)

# Every ordered spanning vertex path is generated, then reversal and
# other duplicates are removed by its edge-set bit mask.
facets = set()
def extend(last, used, mask):
    if used == (1 << 10) - 1:
        facets.add(mask)
        return
    for other in adj[last]:
        if not (used >> other) & 1:
            index = edge_id[tuple(sorted((last, other)))]
            extend(other, used | (1 << other), mask | (1 << index))
for start in range(10):
    extend(start, 1 << start, 0)
assert len(facets) == 120 and all(f.bit_count() == 9 for f in facets)

faces = {0}
for facet in facets:
    face = facet
    while face:
        faces.add(face)
        face = (face - 1) & facet
assert len(faces) == 10212
f_vector = [sum(f.bit_count() == k for f in faces) for k in range(1, 10)]
assert f_vector == [15, 105, 445, 1245, 2346, 2905, 2190, 840, 120]

# Toggle each edge-vertex, always using only as-yet-unmatched simplices.
# The order is fixed so the finite calculation is deterministic.
order = [12, 1, 7, 9, 10, 14, 11, 5, 3, 4, 8, 0, 13, 2, 6]
unmatched = set(faces)
lower_to_upper, upper_to_lower = {}, {}
for v in order:
    bit = 1 << v
    for low in sorted(unmatched):
        up = low | bit
        if low & bit == 0 and up in unmatched:
            unmatched.remove(low)
            unmatched.remove(up)
            lower_to_upper[low] = up
            upper_to_lower[up] = low
assert len(lower_to_upper) == 5092
assert Counter(f.bit_count() - 1 for f in unmatched) == Counter({5: 4, 6: 24})
assert 0 in lower_to_upper and lower_to_upper[0].bit_count() == 1

# Acyclicity test: orient matched cover relations upward, all others down.
indegree = {f: 0 for f in faces}
successors = {f: [] for f in faces}
incidences = 0
for high in faces:
    bits = high
    while bits:
        bit = bits & -bits
        bits -= bit
        low = high ^ bit
        source, target = ((low, high) if lower_to_upper.get(low) == high
                          else (high, low))
        successors[source].append(target)
        indegree[target] += 1
        incidences += 1
ready = deque(f for f, degree in indegree.items() if degree == 0)
removed = 0
while ready:
    vertex = ready.popleft()
    removed += 1
    for neighbor in successors[vertex]:
        indegree[neighbor] -= 1
        if indegree[neighbor] == 0:
            ready.append(neighbor)
assert removed == len(faces) and incidences == 58830

# Signed gradient-path boundary, with the edge ordering given above.
critical_five = sorted(f for f in unmatched if f.bit_count() == 6)
critical_six = sorted(f for f in unmatched if f.bit_count() == 7)
five_id = {face: i for i, face in enumerate(critical_five)}
def incidence(high, low):
    extra = high ^ low
    assert extra.bit_count() == 1 and high & low == low
    return -1 if ((high & (extra - 1)).bit_count() & 1) else 1

@lru_cache(maxsize=None)
def project_five(face):
    if face in five_id:
        return {five_id[face]: 1}
    if face in upper_to_lower:
        # The cell is removed with its lower-dimensional mate.
        return {}
    up = lower_to_upper[face]
    assert up.bit_count() == 7
    coefficient = incidence(up, face)
    result = {}
    bits = up
    while bits:
        bit = bits & -bits
        bits -= bit
        other = up ^ bit
        if other == face:
            continue
        weight = -coefficient * incidence(up, other)
        for index, value in project_five(other).items():
            result[index] = result.get(index, 0) + weight * value
    return {i: v for i, v in result.items() if v}

matrix = [[0] * len(critical_six) for _ in critical_five]
for column, high in enumerate(critical_six):
    bits = high
    while bits:
        bit = bits & -bits
        bits -= bit
        low = high ^ bit
        sign = incidence(high, low)
        for row, value in project_five(low).items():
            matrix[row][column] += sign * value
assert len(matrix) == 4 and all(len(row) == 24 for row in matrix)
assert all(entry == 0 for row in matrix for entry in row)

# Independent simplicial chain rank check over F_2, without Morse matching.
by_size = {k: sorted(f for f in faces if f.bit_count() == k)
           for k in range(10)}
ranks = {}
for size in range(1, 10):
    index = {face: j for j, face in enumerate(by_size[size - 1])}
    pivots = {}
    for high in by_size[size]:
        vector = 0
        bits = high
        while bits:
            bit = bits & -bits
            bits -= bit
            vector ^= 1 << index[high ^ bit]
        while vector:
            pivot = vector.bit_length() - 1
            if pivot in pivots:
                vector ^= pivots[pivot]
            else:
                pivots[pivot] = vector
                break
    ranks[size] = len(pivots)
assert [ranks[s] for s in range(1, 10)] == [1, 14, 91, 354, 891, 1455, 1446, 720, 120]

# Independently compare all 2^15 edge sets with the definition of linear forest.
linear_forests = set()
for mask in range(1 << len(edges)):
    degrees = [0] * 10
    parent = list(range(10))
    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x
    valid = True
    for i, (a, b) in enumerate(edges):
        if mask & (1 << i):
            degrees[a] += 1
            degrees[b] += 1
            if max(degrees[a], degrees[b]) > 2:
                valid = False
                break
            a_root, b_root = root(a), root(b)
            if a_root == b_root:
                valid = False
                break
            parent[a_root] = b_root
    if valid:
        linear_forests.add(mask)
assert faces <= linear_forests
missing = linear_forests - faces
minimal = {m for m in missing if all((m ^ (1 << j)) not in missing
           for j in range(15) if m & (1 << j))}
assert len(linear_forests) == 10372 and len(missing) == 160
assert Counter(m.bit_count() for m in minimal) == Counter({6: 10, 8: 30})
# Both classes of minimal obstructions are single S_5-orbits.
edge_permutations = []
for pi in permutations(range(5)):
    perm_v = [vertex_id[tuple(sorted(pi[k] for k in v))] for v in vertices]
    edge_permutations.append([edge_id[tuple(sorted((perm_v[a], perm_v[b])))]
                              for a, b in edges])
for size in (6, 8):
    representative = min(m for m in minimal if m.bit_count() == size)
    orbit = {sum(1 << pi[j] for j in range(15) if rep & (1 << j))
             for pi in edge_permutations for rep in (representative,)}
    assert orbit == {m for m in minimal if m.bit_count() == size}

print('GRAPH vertices=10 edges=15 spanning_paths=120')
print('COMPLEX nonempty_faces=10211 f_vector=' + repr(f_vector))
print('MATCHING pairs=5092 critical_0=1 critical_5=4 critical_6=24')
print('ACYCLIC directed_cover_relations=58830 visited=10212')
print('MORSE_BOUNDARY_6_TO_5 4x24 integer_zero_matrix')
print('SIMPLICIAL_F2_BOUNDARY_RANKS ' + repr([ranks[s] for s in range(1, 10)]))
print('LINEAR_FORESTS total=10372 not_extendible=160')
print('MINIMAL_OBSTRUCTIONS six_edges=10 eight_edges=30 two_S5_orbits')
print('HOMOTOPY wedge(4,S5) wedge(24,S6)')
print('VERIFY_OK')
