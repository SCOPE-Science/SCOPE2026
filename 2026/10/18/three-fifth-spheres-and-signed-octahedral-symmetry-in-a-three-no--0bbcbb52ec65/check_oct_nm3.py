#!/usr/bin/env python3
"""Exhaustive, dependency-free certificate for the 3-nonmatching complex of K_{2,2,2}."""
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations

PARTS = ((0, 1), (2, 3), (4, 5))
EDGES = tuple((v, w) for v in range(6) for w in range(v + 1, 6)
              if not any(v in block and w in block for block in PARTS))
EDGE_INDEX = {frozenset(e): j for j, e in enumerate(EDGES)}
assert len(EDGES) == 12

# Exactly the forbidden three-edge perfect matchings, found without a lookup table.
FORBIDDEN = tuple(sum(1 << i for i in matching)
    for matching in combinations(range(12), 3)
    if len(set().union(*(EDGES[i] for i in matching))) == 6)
assert len(FORBIDDEN) == 8

# Explicit cube/forbidden-matching incidence for the Alexander-dual nerve proof.
def matching_of_cube_vertex(a, b, c):
    triples = ((a, 2 + b), (3 - b, 4 + c), (5 - c, 1 - a))
    return frozenset(EDGE_INDEX[frozenset(t)] for t in triples)
CUBE_MATCHINGS = tuple(matching_of_cube_vertex(a, b, c)
                       for a in range(2) for b in range(2) for c in range(2))
assert {sum(1 << j for j in m) for m in CUBE_MATCHINGS} == set(FORBIDDEN)
EDGE_TO_CUBE = {i: tuple(v for v, m in enumerate(CUBE_MATCHINGS) if i in m)
                for i in range(12)}
assert all(len(pair) == 2 and (pair[0] ^ pair[1]) in (1, 2, 4)
           for pair in EDGE_TO_CUBE.values())
assert len(set(EDGE_TO_CUBE.values())) == 12
for subset in range(1 << 8):
    common_facet = any(all(i not in CUBE_MATCHINGS[v]
                           for v in range(8) if (subset >> v) & 1)
                       for i in range(12))
    cube_edge_outside = any(not (subset >> v & 1) and not (subset >> w & 1)
                            for v, w in EDGE_TO_CUBE.values())
    assert common_facet == cube_edge_outside
# Cube independence complex: parity tetrahedra plus four antipodal bridges.
INDEPENDENT = [tuple(i for i in range(8) if subset >> i & 1)
               for subset in range(1 << 8)
               if all(not (subset >> v & 1 and subset >> w & 1)
                      for v, w in EDGE_TO_CUBE.values())]
assert len(INDEPENDENT) == 35  # two 4-vertex simplices, four isolated bridges
assert sum(len(face) == 4 for face in INDEPENDENT) == 2
assert sum(len(face) == 2 for face in INDEPENDENT) == 16
FACES = frozenset(mask for mask in range(1 << 12)
                  if all(mask & t != t for t in FORBIDDEN))
assert 0 in FACES and len(FACES) == 1699
assert all((f & (f - 1)) in FACES for f in FACES if f)  # One deletion; closure also follows directly.
f_vector = Counter(mask.bit_count() - 1 for mask in FACES if mask)
assert tuple(f_vector[d] for d in range(8)) == (12, 66, 212, 423, 516, 352, 108, 9)

# Lexicographic vertex-toggle matching on the actual face set, excluding the empty face.
TOGGLE_ORDER = (1, 9, 8, 5, 10, 2, 3, 7, 4, 0, 11, 6)
unmatched = set(FACES - {0})
matching = set()
for i in TOGGLE_ORDER:
    bit = 1 << i
    lowers = sorted(s for s in unmatched if not s & bit and (s | bit) in unmatched)
    for low in lowers:
        high = low | bit
        assert low in unmatched and high in unmatched and high.bit_count() == low.bit_count() + 1
        matching.add((low, high))
        unmatched.remove(low)
        unmatched.remove(high)
assert len(matching) == 847
crit = Counter(mask.bit_count() - 1 for mask in unmatched)
assert crit == Counter({0: 1, 5: 3}), crit

# Independently check the entire Forman orientation of the Hasse diagram, not just a log.
vertices = FACES - {0}
in_degree = {v: 0 for v in vertices}
outgoing = defaultdict(list)
cover_count = 0
for high in vertices:
    sub = high
    while sub:
        bit = sub & -sub
        low = high ^ bit
        if low:
            if (low, high) in matching:
                start, end = low, high
            else:
                start, end = high, low
            outgoing[start].append(end)
            in_degree[end] += 1
            cover_count += 1
        sub ^= bit
queue = deque(sorted(v for v in vertices if in_degree[v] == 0))
visited = 0
while queue:
    v = queue.popleft()
    visited += 1
    for w in outgoing[v]:
        in_degree[w] -= 1
        if in_degree[w] == 0:
            queue.append(w)
assert visited == len(vertices), (visited, len(vertices))

# Independent sparse GF(2) homology calculation on unreduced chains.
by_dim = {d: tuple(sorted(f for f in FACES if f.bit_count() == d + 1)) for d in range(8)}
bdry_rank = {}
for d in range(8):
    if d == 0:
        bdry_rank[d] = 0
        continue
    row_idx = {face: k for k, face in enumerate(by_dim[d - 1])}
    pivots = {}
    for high in by_dim[d]:
        column = 0
        rest = high
        while rest:
            bit = rest & -rest
            column ^= 1 << row_idx[high ^ bit]
            rest ^= bit
        while column:
            pivot = column.bit_length() - 1
            if pivot in pivots:
                column ^= pivots[pivot]
            else:
                pivots[pivot] = column
                break
    bdry_rank[d] = len(pivots)
assert tuple(bdry_rank[d] for d in range(8)) == (0, 11, 55, 157, 266, 250, 99, 9)
betti = tuple(len(by_dim[d]) - bdry_rank[d] - bdry_rank.get(d+1, 0) for d in range(8))
assert betti == (1, 0, 0, 0, 0, 3, 0, 0)

def signed_cycles(perm):
    visited = set()
    result = []
    for j in range(12):
        if j in visited:
            continue
        cyc = 0
        z = j
        while z not in visited:
            visited.add(z)
            cyc |= 1 << z
            z = perm[z]
        result.append(cyc)
    return tuple(result)

def alternating_cycle_union_sum(cycles):
    # Each invariant face is a union of whole vertex cycles of the edge permutation.
    ans = 0
    for subset in range(1 << len(cycles)):
        face = 0
        for j, cyc in enumerate(cycles):
            if subset & (1 << j):
                face |= cyc
        if face in FACES:
            ans += (-1) ** subset.bit_count()
    return ans

characters = Counter()
seen_vertex_permutations = set()
for p in permutations(range(3)):
    for flip_mask in range(8):
        g = tuple(2 * p[j] + ((flip_mask >> j & 1) ^ b)
                  for j in range(3) for b in range(2))
        assert g not in seen_vertex_permutations
        seen_vertex_permutations.add(g)
        induced = tuple(EDGE_INDEX[frozenset((g[a], g[b]))] for a, b in EDGES)
        assert len(set(induced)) == 12
        observed = alternating_cycle_union_sum(signed_cycles(induced))
        expected = sum(1 if not (flip_mask >> j & 1) else -1
                       for j in range(3) if p[j] == j)
        assert observed == expected, (p, flip_mask, observed, expected)
        characters[observed] += 1
assert len(seen_vertex_permutations) == 48
assert dict(characters) == {3: 1, 1: 15, -1: 15, -3: 1, 0: 16}, characters
assert sum(value * count for value, count in characters.items()) == 0

print('graph=K_{2,2,2}; vertices=6; edges=12; perfect_matchings=8')
print('augmented_faces=1699; ordinary_faces=1698; f_vector=' + repr(tuple(f_vector[d] for d in range(8))))
print('toggle_order=' + repr(TOGGLE_ORDER))
print('gradient_pairs=847; critical_cells=' + repr(dict(sorted(crit.items()))))
print('critical_masks=' + repr(sorted(unmatched)))
print('directed_hasse_nodes=1698; directed_hasse_edges=' + str(cover_count) + '; acyclic=yes')
print('GF2_boundary_ranks=' + repr(tuple(bdry_rank[d] for d in range(8))))
print('GF2_unreduced_betti=' + repr(betti))
print('hyperoctahedral_elements=48; character_histogram=' + repr(dict(sorted(characters.items()))))
print('signed_permutation_character_agreement=48/48; invariant_dimension=0')
print('ALL CHECKS PASSED')
