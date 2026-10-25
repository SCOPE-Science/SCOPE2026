#!/usr/bin/env python3
"""Exact standard-library certificate for the 3-by-4 rook open-neighborhood complex."""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations

ROWS, COLS = 3, 4
ORDER = (1, 7, 10, 0, 6, 11, 4, 5, 2, 8, 9, 3)
V = tuple((a, b) for a in range(ROWS) for b in range(COLS))


def vertices(mask):
    return tuple(j for j in range(len(V)) if mask & (1 << j))


def boundary(mask):
    return [(mask ^ (1 << j), (-1) ** p)
            for p, j in enumerate(vertices(mask))]


neighborhoods = [
    tuple(j for j, (a, b) in enumerate(V)
          if j != i and (a == x or b == y))
    for i, (x, y) in enumerate(V)
]
assert len(neighborhoods) == 12 and all(len(n) == 5 for n in neighborhoods)
faces = {
    sum(1 << j for j in s)
    for n in neighborhoods
    for k in range(1, len(n) + 1)
    for s in combinations(n, k)
}
vector = Counter(f.bit_count() - 1 for f in faces)
assert vector == Counter({0: 12, 1: 66, 2: 120, 3: 60, 4: 12})
assert len(faces) == 270

# Sequential element matching on nonempty simplices only.
paired = set()
low_to_up, up_to_low = {}, {}
for j in ORDER:
    for sigma in sorted(faces):
        tau = sigma | (1 << j)
        if sigma != tau and sigma not in paired and tau in faces and tau not in paired:
            paired.add(sigma)
            paired.add(tau)
            low_to_up[sigma] = tau
            up_to_low[tau] = sigma
assert len(low_to_up) == 125
critical = faces - paired
assert Counter(f.bit_count() - 1 for f in critical) == Counter({0: 1, 1: 1, 2: 18})

# Direct, independent Forman orientation of all incidence edges.
# A matched incidence points from lower to upper; every other one points down.
arcs = defaultdict(list)
indegree = {f: 0 for f in faces}
covers = 0
for tau in faces:
    if tau.bit_count() < 2:
        continue
    for sigma, sign in boundary(tau):
        assert sigma in faces and sign in (-1, 1)
        a, b = (sigma, tau) if low_to_up.get(sigma) == tau else (tau, sigma)
        arcs[a].append(b)
        indegree[b] += 1
        covers += 1
assert covers == 792
queue = deque(f for f in faces if indegree[f] == 0)
seen = 0
while queue:
    f = queue.popleft()
    seen += 1
    for g in arcs[f]:
        indegree[g] -= 1
        if indegree[g] == 0:
            queue.append(g)
assert seen == 270, "The proposed matching contains a directed cycle"

# Integral Morse boundary in degree 2: recursively eliminate matched 1/2 pairs.
# Lower 1-faces that match upward are eliminated using the oriented triangle
# relation. Edges matched downward to vertices vanish in the reduced basis.
critical_edge, = [f for f in critical if f.bit_count() == 2]

@lru_cache(None)
def projection(edge):
    if edge == critical_edge:
        return 1
    if edge in up_to_low:
        assert edge.bit_count() == 2 and up_to_low[edge].bit_count() == 1
        return 0
    if edge in low_to_up:
        triangle = low_to_up[edge]
        assert triangle.bit_count() == 3
        signs = dict(boundary(triangle))
        pivot = signs[edge]
        assert abs(pivot) == 1
        rest = sum(sign * projection(other)
                   for other, sign in boundary(triangle) if other != edge)
        return -rest * pivot
    raise AssertionError('Unclassified edge')

morse_degrees = [sum(sign * projection(edge) for edge, sign in boundary(t))
                 for t in sorted(critical) if t.bit_count() == 3]
assert len(morse_degrees) == 18
assert morse_degrees == [0] * 18

# Independent binary chain ranks of the original simplicial boundary matrices.
def rank_mod2(columns):
    pivots = {}
    for x in columns:
        while x:
            k = x.bit_length() - 1
            if k in pivots:
                x ^= pivots[k]
            else:
                pivots[k] = x
                break
    return len(pivots)

rank_by_degree = {}
for d in range(1, 5):
    source = sorted(f for f in faces if f.bit_count() == d + 1)
    target = sorted(f for f in faces if f.bit_count() == d)
    target_index = {f: i for i, f in enumerate(target)}
    boundary_columns = [sum(1 << target_index[g] for g, _ in boundary(f))
                        for f in source]
    rank_by_degree[d] = rank_mod2(boundary_columns)
assert rank_by_degree == {1: 11, 2: 54, 3: 48, 4: 12}
assert 12 - 66 + 120 - 60 + 12 == 18

print('FACE_VECTOR',tuple(vector[k] for k in range(5)))
print('NONEMPTY_FACES',len(faces),'HASSE_COVERS',covers)
print('MORSE_PAIRS',len(low_to_up),'CRITICAL_VECTOR',(1,1,18))
print('MORSE_INTEGER_BOUNDARY_D2',tuple(morse_degrees))
print('BINARY_BOUNDARY_RANKS',tuple(rank_by_degree[k] for k in range(1,5)))
print('CRITICAL_EDGE',vertices(critical_edge))
print('ROOK34_HOMOTOPY_CERTIFICATE_OK')
