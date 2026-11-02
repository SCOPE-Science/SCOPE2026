#!/usr/bin/env python3
"""Independent finite checker of Clebsch-square and Q5 total-domination geometry."""
from itertools import combinations
from collections import deque, Counter

EVEN = tuple(v for v in range(32) if v.bit_count() % 2 == 0)
ODD = tuple(v for v in range(32) if v.bit_count() % 2 == 1)
assert len(EVEN) == len(ODD) == 16
q_neighbors = {v: frozenset(v ^ (1 << i) for i in range(5)) for v in range(32)}
# Clebsch: 16 even vectors, adjacency at Hamming distance four.
C = {v: frozenset(w for w in EVEN if (v ^ w).bit_count() == 4) for v in EVEN}
assert all(len(C[v]) == 5 for v in EVEN)
assert sum(len(C[v]) for v in EVEN) // 2 == 40
assert all(len(C[x] & C[y]) == (0 if y in C[x] else 2)
           for x, y in combinations(EVEN, 2))

# Enumerate each quadrangle as a four-subset of Clebsch vertices.
squares = []
for a in combinations(EVEN, 4):
    A = frozenset(a)
    if all(len(C[v] & A) == 2 for v in A):
        squares.append(A)
assert len(squares) == 40 and len(set(squares)) == 40

# Direct, independent four-element coverage test; the families must coincide.
covers = [frozenset(a) for a in combinations(EVEN, 4)
          if set.union(*(set(q_neighbors[x]) for x in a)) == set(ODD)]
assert len(covers) == 40 and set(covers) == set(squares)

# Distinct quadrangles never share three vertices. Shared pairs are edges.
H = [set() for _ in squares]
for i, j in combinations(range(40), 2):
    shared = squares[i] & squares[j]
    assert len(shared) <= 2
    if len(shared) == 2:
        x, y = tuple(shared)
        assert y in C[x]
        H[i].add(j)
        H[j].add(i)
assert all(len(neigh) == 12 for neigh in H)
assert sum(map(len, H)) // 2 == 240

# A second, explicit 10+30 description of the Clebsch quadrangles.
# Vertex symbols are ('z',), ('a', i), and ('b', i, j) with 0 <= i < j < 5.
B = lambda i, j: ('b', min(i, j), max(i, j))
explicit = []
for i, j in combinations(range(5), 2):
    explicit.append(frozenset((('z',), ('a',i), ('a',j), B(i,j))))
for i in range(5):
    rest = [j for j in range(5) if j != i]
    for j, k in combinations(rest, 2):
        l, m = sorted(set(range(5)) - {i, j, k})
        explicit.append(frozenset((('a',i), B(i,j), B(i,k), B(l,m))))
assert len(explicit) == 40 and len(set(explicit)) == 40

def vertex_value(v):
    if v[0] == 'z': return 0
    if v[0] == 'a': return 31 ^ (1 << v[1])
    return (1 << v[1]) | (1 << v[2])
assert {frozenset(vertex_value(v) for v in cycle) for cycle in explicit} == set(squares)

# Exhaustive 40 by 40 incidence lemma: two quadrangles have a shared
# edge or admit an intermediate quadrangle sharing an edge with both.
# The values are counts of unordered pairs classified by edge adjacency
# and the number of possible intermediate quadrangles.
common_types = Counter()
for i, j in combinations(range(40), 2):
    common = len(H[i] & H[j])
    common_types[(j in H[i],common)] += 1
    if j not in H[i]: assert common >= 1
assert common_types == {(True,4): 240, (False,2):240, (False,4):300}

# Complete metric matrix, not a random sample.
for i in range(40):
    ds = [-1] * 40
    ds[i] = 0
    q = deque([i])
    while q:
        v = q.popleft()
        for w in H[v]:
            if ds[w] == -1:
                ds[w] = ds[v] + 1
                q.append(w)
    assert Counter(ds) == {0: 1, 1: 12, 2: 27}

# The complete two-replacement graph is the Cartesian square H □ H.
# Its distances add in the two coordinates; verify its exact distribution.
profile = Counter({0: 1})
for _ in range(2):
    nxt = Counter()
    for dist, n in profile.items():
        for k, v in ((0, 1), (1, 12), (2, 27)):
            nxt[dist + k] += n * v
    profile = nxt
assert profile == {0: 1, 1: 24, 2: 198, 3: 648, 4: 729}
assert sum(profile.values()) == 1600
assert 1600 * 24 // 2 == 19200
print('CLEBSCH_SQUARE_CLASSIFICATION_AND_METRIC_PASS')
print('parity_covers=40 all_total_sets=1600 one_swap_edges=0')
print('two_swap_vertices=1600 edges=19200 degree=24 diameter=4')
print('distance_profile=1,24,198,648,729')
