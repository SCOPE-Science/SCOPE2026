#!/usr/bin/env python3
"""Exact finite verification for the Frucht-graph matching-complex theorem.

The graph is specified by its 12-cycle and LCF chord offsets. Uses only the
Python standard library. Every nonempty matching is enumerated exhaustively.
"""
from collections import Counter, deque

N = 12
JUMPS = (-5, -2, -4, 2, 5, -2, 2, 5, -2, -5, 4, 2)
PIVOTS = (4, 6, 10, 7, 15, 1, 16, 2, 8, 14, 17, 12, 3, 13, 0, 5, 9, 11)
EXPECTED_CRITICAL = (16, 2188, 33036, 34852, 65804, 66060,
                     69665, 69668, 69889, 69892, 70145, 70148,
                     73761, 73764, 73985, 74241, 74244,
                     135297, 139393, 147969, 167968)

# The chord list agrees with the published LCF representation of the graph.
E = set()
for i in range(N):
    E.add(tuple(sorted((i, (i + 1) % N))))
    E.add(tuple(sorted((i, (i + JUMPS[i]) % N))))
E = tuple(sorted(E))
assert len(E) == 18 and len(set(E)) == 18
assert all(a != b for a, b in E)
assert Counter(v for a, b in E for v in (a, b)) == Counter({i: 3 for i in range(N)})

# Independent exhaustive enumeration, rather than relying on a f-vector log.
F = set()
for mask in range(1, 1 << len(E)):
    occupied = 0
    bits = mask
    valid = True
    while bits:
        bit = bits & -bits
        j = bit.bit_length() - 1
        a, b = E[j]
        pairmask = (1 << a) | (1 << b)
        if occupied & pairmask:
            valid = False
            break
        occupied |= pairmask
        bits -= bit
    if valid:
        F.add(mask)
face_vector = Counter(x.bit_count()-1 for x in F)
assert face_vector == {0:18, 1:117, 2:333, 3:397, 4:152, 5:8}
assert len(F) == 1025

# Explicit deterministic matching of face-coface pairs.
remaining = set(F)
pairs = []
for j in PIVOTS:
    bit = 1 << j
    for x in sorted(remaining):
        y = x | bit
        if x in remaining and not (x & bit) and y in remaining:
            assert x.bit_count() + 1 == y.bit_count()
            remaining.remove(x)
            remaining.remove(y)
            pairs.append((x, y))
assert len(pairs) == 502
assert tuple(sorted(remaining)) == EXPECTED_CRITICAL
assert Counter(x.bit_count()-1 for x in remaining) == {0:1, 3:20}

# Orient unmatched Hasse incidences downward and paired incidences upward.
# A complete Kahn topological sort is an exact acyclicity certificate.
mate = dict(pairs)
indegree = {x:0 for x in F}
adjacency = {x:[] for x in F}
incidences = 0
for coface in F:
    bits = coface
    while bits:
        bit = bits & -bits
        face = coface ^ bit
        bits -= bit
        if face == 0:
            continue
        assert face in F
        incidences += 1
        if mate.get(face) == coface:
            origin, target = face, coface
        else:
            origin, target = coface, face
        adjacency[origin].append(target)
        indegree[target] += 1
queue = deque(x for x, d in indegree.items() if d == 0)
visited = 0
while queue:
    x = queue.popleft()
    visited += 1
    for y in adjacency[x]:
        indegree[y] -= 1
        if indegree[y] == 0:
            queue.append(y)
assert visited == len(F), (visited, len(F))

# Separately compute all mod-two boundary ranks as a sanity cross-check.
levels = {d: sorted(x for x in F if x.bit_count() == d+1) for d in range(6)}
ranks = []
for d in range(1, 6):
    index = {x:i for i, x in enumerate(levels[d-1])}
    basis = {}
    for coface in levels[d]:
        col = 0
        bits = coface
        while bits:
            bit = bits & -bits
            col ^= 1 << index[coface ^ bit]
            bits -= bit
        while col:
            p = col.bit_length() - 1
            if p in basis:
                col ^= basis[p]
            else:
                basis[p] = col
                break
    ranks.append(len(basis))
assert ranks == [17, 100, 233, 144, 8]

print('EDGE_COUNT',len(E))
print('FACE_VECTOR',tuple(face_vector[d] for d in range(6)))
print('TOTAL_FACES',len(F))
print('MATCHED_PAIRS',len(pairs))
print('CRITICAL_VECTOR',tuple(Counter(x.bit_count()-1 for x in remaining)[d] for d in range(6)))
print('HASSE_INCIDENCES',incidences)
print('DIRECTED_DAG_VERTICES',visited)
print('BOUNDARY_RANKS_MOD_2',tuple(ranks))
print('VERIFY_OK')
