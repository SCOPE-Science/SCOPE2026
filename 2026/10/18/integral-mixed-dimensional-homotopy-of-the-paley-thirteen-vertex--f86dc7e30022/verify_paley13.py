#!/usr/bin/env python3
"""Self-contained exact certificate for the ordinary 3-cut complex of Paley(13).

No nonstandard Python packages are needed. A face is a 13-bit integer; bit i
corresponds to vertex i of the quadratic-residue Paley graph over F_13.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations
from math import gcd

N = 13
UNIVERSE = (1 << N) - 1
MATCH_ORDER = [8, 12, 9, 1, 2, 11, 0, 3, 5, 7, 6, 10, 4]
RESIDUES = {x * x % N for x in range(1, N)}
assert RESIDUES == {1, 3, 4, 9, 10, 12}
ADJ = [sum(1 << j for j in range(N) if (j - i) % N in RESIDUES)
       for i in range(N)]
assert all(a.bit_count() == 6 for a in ADJ)
for i in range(N):
    for j in range(i + 1, N):
        common = (ADJ[i] & ADJ[j]).bit_count()
        assert common == (2 if (ADJ[i] >> j) & 1 else 3)

# For three vertices, connectedness is equivalent to having >=2 edges.
def edge_count_on_three(vertices):
    return sum((ADJ[i] >> j) & 1 for i, j in combinations(vertices, 2))

DISCONNECTED = {
    sum(1 << v for v in triple)
    for triple in combinations(range(N), 3)
    if edge_count_on_three(triple) <= 1
}
assert len(DISCONNECTED) == 143
assert 286 - len(DISCONNECTED) == 143

# Ordinary 3-cut complex, not the total 3-cut complex. Include only
# NONEMPTY simplices: the empty face is excluded from Forman's face poset.
FACES = {
    s for s in range(1, 1 << N)
    if any((t & (UNIVERSE ^ s)) == t for t in DISCONNECTED)
}
F_VECTOR_BY_SIZE = {1: 13, 2: 78, 3: 286, 4: 715, 5: 1287,
                    6: 1716, 7: 1716, 8: 1287, 9: 637, 10: 143}
assert dict(Counter(s.bit_count() for s in FACES)) == F_VECTOR_BY_SIZE
assert len(FACES) == 7878

# Acyclic element matching: in each ordered vertex stage, pair each
# remaining cell s not containing the pivot with remaining s union pivot.
# All pairs are disjoint and are face/coface incidences of codimension one.
remaining = set(FACES)
pairs = []
for vertex in MATCH_ORDER:
    pivot = 1 << vertex
    stage = [(s, s | pivot) for s in sorted(remaining)
             if not (s & pivot) and (s | pivot) in remaining]
    for lower, upper in stage:
        assert lower in remaining and upper in remaining
        remaining.remove(lower)
        remaining.remove(upper)
    pairs.extend(stage)
LOW_TO_HIGH = dict(pairs)
HIGH_TO_LOW = {high: low for low, high in pairs}
assert len(pairs) == len(LOW_TO_HIGH) == len(HIGH_TO_LOW) == 3936
assert sorted(remaining) == [256, 4671, 6711, 7389, 7695, 7739]
assert dict(Counter(s.bit_count()-1 for s in remaining)) == {0:1,7:3,8:2}

# A matching is acyclic iff the oriented whole Hasse graph is acyclic:
# reverse precisely the matched arrows (lower -> higher), while all other
# covering incidences point downwards. Verify by complete topological sort.
indeg = {s: 0 for s in FACES}
steps_from = {s: [] for s in FACES}
incidences = 0
for upper in FACES:
    for vertex in range(N):
        if not ((upper >> vertex) & 1):
            continue
        lower = upper ^ (1 << vertex)
        if not lower:
            continue
        assert lower in FACES
        a, b = ((lower, upper) if LOW_TO_HIGH.get(lower) == upper
                else (upper, lower))
        steps_from[a].append(b)
        indeg[b] += 1
        incidences += 1
assert incidences == 50076
queue = deque(s for s in FACES if indeg[s] == 0)
processed = 0
while queue:
    s = queue.popleft()
    processed += 1
    for t in steps_from[s]:
        indeg[t] -= 1
        if indeg[t] == 0:
            queue.append(t)
assert processed == len(FACES)

# Integral Morse differential in degrees 8 -> 7. Facet orientations are
# the vertex order 0,...,12. Eliminate matched (7,8) pairs by exact
# signed unimodular substitution. Upper cells in (6,7) matches vanish
# in the degree-7 Morse chain group, while critical 7-cells survive.
def signed_facets(s):
    sign = 1
    for vertex in range(N):
        if (s >> vertex) & 1:
            yield s ^ (1 << vertex), sign
            sign = -sign

critical_7 = sorted(s for s in remaining if s.bit_count() == 8)
critical_8 = sorted(s for s in remaining if s.bit_count() == 9)
indices = {s: k for k, s in enumerate(critical_7)}
visiting = set()

@lru_cache(None)
def reduced_degree_7(s):
    assert s.bit_count() == 8
    if s in remaining:
        assert s in indices
        return {indices[s]: 1}
    if s in HIGH_TO_LOW:
        assert HIGH_TO_LOW[s].bit_count() == 7
        return {}
    assert s in LOW_TO_HIGH
    assert s not in visiting
    visiting.add(s)
    t = LOW_TO_HIGH[s]
    assert t.bit_count() == 9
    facets = list(signed_facets(t))
    incidence = next(sign for face, sign in facets if face == s)
    result = {}
    for face, sign in facets:
        if face == s:
            continue
        for row, coefficient in reduced_degree_7(face).items():
            result[row] = result.get(row, 0) - incidence * sign * coefficient
    visiting.remove(s)
    return {row: value for row, value in result.items() if value}

boundary_columns = []
for eight_cell in critical_8:
    coefficients = {}
    for face, incidence in signed_facets(eight_cell):
        for row, amount in reduced_degree_7(face).items():
            coefficients[row] = coefficients.get(row, 0) + incidence * amount
    boundary_columns.append([coefficients.get(i, 0) for i in range(3)])
assert boundary_columns == [[-1, -1, 1], [-1, -1, 1]]
assert gcd(*(coefficient for col in boundary_columns for coefficient in col)) == 1
assert boundary_columns[0] == boundary_columns[1]

# A CW complex with one vertex, three 7-cells and two 8-cells has
# 7-skeleton a wedge of three 7-spheres. Since pi_7 of this wedge is Z^3,
# the two attaching maps are classified by the computed integral degrees.
# The primitive vector (-1,-1,1) can be made (1,0,0) by an integral
# change of basis; one 8-cell cancels that sphere and the other becomes
# a freely attached 8-sphere. The resulting type is 2*S^7 wedge S^8.
print('VERIFY_OK')
print('graph_vertices=13 degree=6 strongly_regular=(13,6,2,3)')
print('disconnected_triples=143 connected_triples=143')
print('nonempty_simplices=7878 facet_count=143 hasse_incidences=50076')
print('morse_pairs=3936 critical={0:1,7:3,8:2}')
print('critical_7=' + repr(critical_7))
print('critical_8=' + repr(critical_8))
print('integral_boundary_columns=' + repr(boundary_columns))
print('homotopy=two_7_spheres_wedge_one_8_sphere')
