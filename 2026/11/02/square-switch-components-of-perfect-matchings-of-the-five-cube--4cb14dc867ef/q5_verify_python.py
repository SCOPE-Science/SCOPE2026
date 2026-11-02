"""Independent exhaustive perfect-matching flip verification for the five-cube.

No external dependencies. Matching states are bitsets of the 80 graph edges;
the implementation does not use bipartite permutation encodings.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations

DIM = 5
VERTICES = 1 << DIM
EDGES = tuple((u, v) for u in range(VERTICES) for v in range(u + 1, VERTICES) if (u ^ v).bit_count() == 1)
assert len(EDGES) == 80
EDGE_NO = {e: i for i, e in enumerate(EDGES)}
INC = [[] for _ in range(VERTICES)]
for i, (u, v) in enumerate(EDGES):
    INC[u].append((v, i))
    INC[v].append((u, i))

STATES = []
def visit(unmatched, edgeset):
    if not unmatched:
        STATES.append(edgeset)
        return
    low = unmatched & -unmatched
    u = low.bit_length() - 1
    rest = unmatched ^ low
    for v, edgeid in INC[u]:
        vflag = 1 << v
        if rest & vflag:
            visit(rest ^ vflag, edgeset | (1 << edgeid))
visit((1 << VERTICES) - 1, 0)
assert len(STATES) == 589185
INDEX = {m: i for i, m in enumerate(STATES)}
assert len(INDEX) == len(STATES)

SQUARES = set()
for u in range(VERTICES):
    for a, b in combinations(range(DIM), 2):
        x = u ^ (1 << a)
        y = u ^ (1 << b)
        z = x ^ (1 << b)
        edges = ((min(u, x), max(u, x)), (min(u, y), max(u, y)),
                 (min(x, z), max(x, z)), (min(y, z), max(y, z)))
        mask = sum(1 << EDGE_NO[e] for e in edges)
        SQUARES.add(mask)
SQUARES = tuple(sorted(SQUARES))
assert len(SQUARES) == 80

N = len(STATES)
PARENT = list(range(N))
SIZE = [1] * N

def root(a):
    while PARENT[a] != a:
        PARENT[a] = PARENT[PARENT[a]]
        a = PARENT[a]
    return a

def merge(a, b):
    a = root(a)
    b = root(b)
    if a != b:
        if SIZE[a] < SIZE[b]:
            a, b = b, a
        PARENT[b] = a
        SIZE[a] += SIZE[b]

DEGREES = Counter()
EDGE_COUNT = 0
for i, m in enumerate(STATES):
    degree = 0
    for square in SQUARES:
        if (m & square).bit_count() == 2:
            m2 = m ^ square
            j = INDEX.get(m2)
            assert j is not None
            degree += 1
            if i < j:
                EDGE_COUNT += 1
                merge(i, j)
    DEGREES[degree] += 1
COMPONENTS = Counter()
for i in range(N):
    if root(i) == i:
        COMPONENTS[SIZE[i]] += 1

assert COMPONENTS == Counter({1: 120, 4: 80, 99280: 1, 489465: 1}), COMPONENTS
assert EDGE_COUNT == 3219360, EDGE_COUNT
assert DEGREES[0] == 120, DEGREES
assert sum(DEGREES.values()) == N
assert sum(d * multiplicity for d, multiplicity in DEGREES.items()) == 2 * EDGE_COUNT
# Four-vertex components have degree exactly two within their component,
# hence each such component is a four-cycle.
for i in range(N):
    if SIZE[root(i)] == 4:
        assert sum((STATES[i] & s).bit_count() == 2 for s in SQUARES) == 2
# Check geometry: all isolated states are one orbit of cube automorphisms,
# and all eighty four-cycle components belong to one component orbit.
FROZEN = {i for i in range(N) if SIZE[root(i)] == 1}
FOUR = {root(i) for i in range(N) if SIZE[root(i)] == 4}
frozen_rep = STATES[next(iter(FROZEN))]
small_rep = STATES[next(i for i in range(N) if SIZE[root(i)] == 4)]

def transform(m, f):
    out = 0
    while m:
        low = m & -m
        idx = low.bit_length() - 1
        u, v = EDGES[idx]
        u, v = f[u], f[v]
        if u > v:
            u, v = v, u
        out |= 1 << EDGE_NO[(u, v)]
        m ^= low
    return out

frozen_orbit = set()
small_component_orbit = set()
for perm in permutations(range(DIM)):
    permute = [sum(((v >> j) & 1) << perm[j] for j in range(DIM))
               for v in range(VERTICES)]
    for translate in range(VERTICES):
        f = [x ^ translate for x in permute]
        frozen_orbit.add(INDEX[transform(frozen_rep, f)])
        small_component_orbit.add(root(INDEX[transform(small_rep, f)]))
assert frozen_orbit == FROZEN, (len(frozen_orbit), len(FROZEN))
assert small_component_orbit == FOUR, (len(small_component_orbit), len(FOUR))

print('Q5_INDEPENDENT_80_EDGE_BITSET_EXHAUSTIVE_PASS')
print('Q5_SYMMETRY_ORBITS_FROZEN_AND_FOUR_CYCLE_COMPONENTS_PASS')
print('states', N, 'edges', EDGE_COUNT, 'components', sorted(COMPONENTS.items()))
print('degree_histogram', sorted(DEGREES.items()))
