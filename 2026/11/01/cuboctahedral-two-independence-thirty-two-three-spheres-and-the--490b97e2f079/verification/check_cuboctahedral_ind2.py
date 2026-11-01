#!/usr/bin/env python3
"""Exact finite verification of the cuboctahedral two-independence calculation.

Pure Python 3, no external dependencies. Vertices 0..7 label the cube by bits;
the 12 vertices of its line graph are the lexicographically sorted cube edges.
"""
from collections import Counter, defaultdict, deque
from itertools import permutations

CUBE_EDGES = sorted((x, x ^ (1 << i))
                    for x in range(8) for i in range(3)
                    if x < (x ^ (1 << i)))
assert len(CUBE_EDGES) == 12
EDGE_INDEX = {e: i for i, e in enumerate(CUBE_EDGES)}
N = 12
ADJ = [sum(1 << j for j, f in enumerate(CUBE_EDGES)
           if i != j and len(set(e + f)) < 4)
       for i, e in enumerate(CUBE_EDGES)]
assert sum(x.bit_count() for x in ADJ) == 48

# Components of an induced simple graph have size at most two iff its
# maximum induced degree is at most one.
def valid(m):
    return all((ADJ[i] & m).bit_count() <= 1
               for i in range(N) if m & (1 << i))

FACES = [m for m in range(1 << N) if valid(m)]
FSET = set(FACES)
FVECTOR = Counter(m.bit_count() - 1 for m in FACES)
assert dict(FVECTOR) == {-1: 1, 0: 12, 1: 66, 2: 164, 3: 177, 4: 36}
FACETS = [m for m in FACES if not any((m | (1 << v)) in FSET
                                       for v in range(N) if not m & (1 << v))]
assert Counter(m.bit_count() - 1 for m in FACETS) == {3: 45, 4: 36}

# Sequential element matching on the augmented face poset.
PIVOT_ORDER = (8, 4, 9, 0, 10, 7, 11, 3, 5, 6, 2, 1)
remaining = set(FACES)
matched = []
for v in PIVOT_ORDER:
    bit = 1 << v
    for m in FACES:
        high = m | bit
        if not m & bit and m in remaining and high in remaining:
            remaining.remove(m)
            remaining.remove(high)
            matched.append((m, high))
assert len(matched) == 212
assert len(remaining) == 32
assert {m.bit_count() - 1 for m in remaining} == {3}
assert sum(1 for low, high in matched if low == 0) == 1
assert len(set(x for pair in matched for x in pair)) == 424

# Orient every cover relation from upper to lower, reversing matched edges.
reversed_pairs = set(matched)
indegree = {m: 0 for m in FACES}
out = {m: [] for m in FACES}
hasse = 0
for high in FACES:
    rest = high
    while rest:
        bit = rest & -rest
        low = high ^ bit
        assert low in FSET
        if (low, high) in reversed_pairs:
            a, b = low, high
        else:
            a, b = high, low
        out[a].append(b)
        indegree[b] += 1
        hasse += 1
        rest ^= bit
assert hasse == 1524
queue = deque(m for m in FACES if indegree[m] == 0)
seen = 0
while queue:
    m = queue.popleft()
    seen += 1
    for v in out[m]:
        indegree[v] -= 1
        if indegree[v] == 0:
            queue.append(v)
assert seen == len(FACES), 'The complete matched face-poset graph has a cycle'

# Independent mod-2 boundary ranks (not used in the integral Morse proof).
def rank2(columns):
    pivots = {}
    for col in columns:
        while col:
            r = col.bit_length() - 1
            if r not in pivots:
                pivots[r] = col
                break
            col ^= pivots[r]
    return len(pivots)

by_dimension = {d: sorted(m for m in FACES if m.bit_count()-1 == d)
                for d in range(5)}
RANKS = {}
for d in range(1, 5):
    lowindex = {m: j for j, m in enumerate(by_dimension[d-1])}
    cols = []
    for high in by_dimension[d]:
        col = 0
        rem = high
        while rem:
            bit = rem & -rem
            col ^= 1 << lowindex[high ^ bit]
            rem ^= bit
        cols.append(col)
    RANKS[d] = rank2(cols)
assert RANKS == {1: 11, 2: 55, 3: 109, 4: 36}, RANKS
betti = {0: len(by_dimension[0])-RANKS[1]-1,
         1: len(by_dimension[1])-RANKS[1]-RANKS[2],
         2: len(by_dimension[2])-RANKS[2]-RANKS[3],
         3: len(by_dimension[3])-RANKS[3]-RANKS[4],
         4: len(by_dimension[4])-RANKS[4]}
assert betti == {0: 0, 1: 0, 2: 0, 3: 32, 4: 0}

# Signed coordinate cycles identify the 10 conjugacy classes of B_3.
def signed_type(p, b):
    visited = set()
    typ = []
    for i in range(3):
        if i in visited:
            continue
        cyc = []
        j = i
        while j not in visited:
            visited.add(j)
            cyc.append(j)
            j = p[j]
        typ.append((len(cyc), sum((b >> c) & 1 for c in cyc) % 2))
    return tuple(sorted(typ))

def sign_sequence(a):
    return -1 if sum(a[i] > a[j] for i in range(len(a))
                     for j in range(i + 1, len(a))) % 2 else 1

EXPECTED = {
    ((1, 0), (1, 0), (1, 0)): (1, 32),
    ((1, 0), (1, 0), (1, 1)): (3, 2),
    ((1, 0), (1, 1), (1, 1)): (3, 8),
    ((1, 1), (1, 1), (1, 1)): (1, 10),
    ((1, 0), (2, 0)): (6, 2),
    ((1, 0), (2, 1)): (6, 0),
    ((1, 1), (2, 0)): (6, 4),
    ((1, 1), (2, 1)): (6, -2),
    ((3, 0),): (8, -1),
    ((3, 1),): (8, 1),
}
observed = defaultdict(list)
permutations_of_edges = set()
for p in permutations(range(3)):
    for b in range(8):
        def act_cube(x):
            return b ^ sum(((x >> i) & 1) << p[i] for i in range(3))
        image = tuple(EDGE_INDEX[tuple(sorted((act_cube(u), act_cube(v))))]
                      for u, v in CUBE_EDGES)
        permutations_of_edges.add(image)
        assert all(bool(ADJ[i] & (1 << j)) ==
                   bool(ADJ[image[i]] & (1 << image[j]))
                   for i in range(N) for j in range(N))
        trace = 0
        for f in FACES:
            members = [i for i in range(N) if f & (1 << i)]
            mapped = [image[i] for i in members]
            if sum(1 << j for j in mapped) == f:
                trace += (-1) ** len(members) * sign_sequence(mapped)
        observed[signed_type(p, b)].append(trace)
assert len(permutations_of_edges) == 48
assert set(observed) == set(EXPECTED)
for typ, (size, trace) in EXPECTED.items():
    assert len(observed[typ]) == size
    assert set(observed[typ]) == {trace}, (typ, observed[typ])
assert sum(sum(v) for v in observed.values()) == 96  # invariant dimension two
assert EXPECTED[((1, 1), (1, 1), (1, 1))][1] == 10

# Four edges around one square face of Q3 induce a C_4 in the line graph.
square = [EDGE_INDEX[(0,1)], EDGE_INDEX[(1,3)],
          EDGE_INDEX[(2,3)], EDGE_INDEX[(0,2)]]
assert all(bool(ADJ[square[i]] & (1 << square[j])) ==
           (j in {(i+1) % 4, (i-1) % 4})
           for i in range(4) for j in range(4) if i != j)

print('CUBOCTAHEDRAL_IND2_EXACT_MORSE_CHARACTER_OK')
print('cube_edges=', CUBE_EDGES)
print('f_vector=', [FVECTOR[d] for d in range(-1, 5)])
print('facet_dimensions=', dict(sorted(Counter(m.bit_count()-1 for m in FACETS).items())))
print('face_count=', len(FACES), 'matching_pairs=', len(matched),
      'critical_three_cells=', len(remaining), 'Hasse_cover_relations=', hasse)
print('boundary_ranks_mod_two=', RANKS, 'reduced_Betti_mod_two=', betti)
print('signed_cycle_type: class_size character_H3')
for typ in sorted(EXPECTED):
    print(typ, *EXPECTED[typ])
print('full_cube_symmetry_invariant_dimension=', 2)
print('central_antipodal_trace=', 10,
      'central_even_odd_dimensions=', (21, 11))
