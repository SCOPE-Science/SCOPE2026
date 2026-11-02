#!/usr/bin/env python3
"""Exact, standard-library-only certificate for majority C-colourings of H(3,3).

Vertices are lexicographically ordered ternary triples, with edges exactly
between triples differing in one coordinate. All searches are exhaustive.
"""
from itertools import combinations, permutations, product
from math import comb

V = list(product(range(3), repeat=3))
INDEX = {v: i for i, v in enumerate(V)}
N = 27
FULL = (1 << N) - 1
ADJ = [sum(1 << j for j, y in enumerate(V)
           if sum(a != b for a, b in zip(x, y)) == 1) for x in V]
assert all(mask.bit_count() == 6 for mask in ADJ)

def minimum_degree_at_least(mask, d):
    return all((ADJ[i] & mask).bit_count() >= d
               for i in range(N) if (mask >> i) & 1)

def move_mask(mask, relabel):
    answer = 0
    while mask:
        bit = mask & -mask
        answer |= 1 << relabel[bit.bit_length()-1]
        mask -= bit
    return answer

# Enumerate every nonempty subset with at most seven vertices, rather than
# inferring from representative examples or partial graph enumeration.
valid_by_size = {}
seen = 0
six = set()
for k in range(1, 8):
    number = 0
    for subset in combinations(range(N), k):
        seen += 1
        mask = sum(1 << j for j in subset)
        if minimum_degree_at_least(mask, 3):
            number += 1
            if k == 6:
                six.add(mask)
    valid_by_size[k] = number
assert seen == sum(comb(N, k) for k in range(1, 8))
assert [valid_by_size[k] for k in range(1, 8)] == [0, 0, 0, 0, 0, 54, 0]
print('ALL_SMALL_CLASS_SUBSETS_OK', seen, valid_by_size)

# Every six-element class is a 3 by 2 by 1 coordinate box, and conversely.
BOXES = {}  # mask -> the unique unconstrained/full coordinate
for full_axis in range(3):
    for half_axis in range(3):
        if half_axis == full_axis:
            continue
        fixed_axis = 3 - full_axis - half_axis
        for fixed_value in range(3):
            for half_values in combinations(range(3), 2):
                mask = sum(1 << INDEX[v] for v in V
                           if v[fixed_axis] == fixed_value
                           and v[half_axis] in half_values)
                assert mask.bit_count() == 6
                assert mask not in BOXES
                BOXES[mask] = full_axis
assert len(BOXES) == 54 and set(BOXES) == six
print('SIX_VERTEX_CORE_BOX_CLASSIFICATION_OK', len(BOXES))

# A four-colour partition must have sizes 6,6,6,9, since there are no
# smaller or seven-vertex majority classes and 4*6 <= 27 < 5*6.
# Enumerate ALL triples of small classes and test the exact condition
# on the nine remaining vertices; no colouring is omitted.
partitions = set()
disjoint_types = [0, 0, 0, 0]
valid_types = [0, 0, 0, 0]
boxes = sorted(BOXES)
for a, b, c in combinations(boxes, 3):
    if a & b or (a | b) & c:
        continue
    distinct_axes = len({BOXES[a], BOXES[b], BOXES[c]})
    disjoint_types[distinct_axes] += 1
    remainder = FULL ^ (a | b | c)
    if minimum_degree_at_least(remainder, 3):
        partitions.add((a, b, c))
        valid_types[distinct_axes] += 1
assert disjoint_types[1:] == [540, 972, 54]
assert valid_types[1:] == [288, 0, 0]
assert len(partitions) == 288
print('ALL_OPTIMAL_UNLABELLED_PARTITIONS_OK', len(partitions),
      'disjoint_axis_types', disjoint_types[1:])

# Independent reduction to a 3x3 rook graph, one coordinate constant
# along every colour class. Every legal 2D partition consists of three
# edges (pairs of adjacent cells) and a three-cell remainder with no
# isolated vertex. Count these without referring to the 3D box census.
W = list(product(range(3), repeat=2))
E = [frozenset((i, j)) for i, j in combinations(range(9), 2)
     if sum(a != b for a, b in zip(W[i], W[j])) == 1]
E = sorted(E, key=lambda e: tuple(sorted(e)))
rook_partitions = set()
remain_types = {'straight_line': 0, 'corner': 0}
for e1, e2, e3 in combinations(E, 3):
    used = e1 | e2 | e3
    if len(used) != 6:
        continue
    rem = frozenset(range(9)) - used
    if all(any(j != i and frozenset((i,j)) in E for j in rem)
           for i in rem):
        key = frozenset((e1,e2,e3,rem))
        rook_partitions.add(key)
for part in rook_partitions:
    remainder = next(x for x in part if len(x)==3)
    on_line = any(len({W[j][axis] for j in remainder}) == 1
                  for axis in range(2))
    remain_types['straight_line' if on_line else 'corner'] += 1
assert len(rook_partitions) == 96
assert remain_types == {'straight_line':24, 'corner':72}
assert len(partitions) == 3 * len(rook_partitions)
print('INDEPENDENT_ROOK_PARTITION_COUNT_OK', 96, remain_types)

# Generate 3!*(3!)^3 = 1296 concrete graph automorphisms.
AUT = []
for coordinate_perm in permutations(range(3)):
    for p0, p1, p2 in product(permutations(range(3)), repeat=3):
        symbol_perms = (p0, p1, p2)
        relabel = tuple(INDEX[tuple(symbol_perms[i][v[coordinate_perm[i]]]
                                      for i in range(3))] for v in V)
        AUT.append(relabel)
assert len(AUT) == len(set(AUT)) == 1296
assert all(all((ADJ[i] >> j) & 1 == (ADJ[p[i]] >> p[j]) & 1
                   for i in range(N) for j in range(N)) for p in AUT)

# Orbits of unordered class partitions under the full Hamming graph group.
remaining = set(partitions)
orbit_sizes = []
orbit_remainder_types = {}
for representative in sorted(partitions):
    if representative not in remaining:
        continue
    orbit = {tuple(sorted(move_mask(mask, p) for mask in representative))
             for p in AUT}
    assert orbit <= partitions
    orbit_sizes.append(len(orbit))
    full_axis = BOXES[representative[0]]
    assert all(BOXES[part] == full_axis for part in representative)
    axes = [j for j in range(3) if j != full_axis]
    rest = FULL ^ (representative[0] | representative[1] | representative[2])
    quotient_remainder = {tuple(V[j][k] for k in axes)
                          for j in range(N) if rest >> j & 1}
    assert len(quotient_remainder) == 3
    is_line = any(len({u[k] for u in quotient_remainder}) == 1
                  for k in range(2))
    orbit_remainder_types[len(orbit)] = 'straight_line' if is_line else 'corner'
    remaining -= orbit
assert not remaining
assert sorted(orbit_sizes) == [18,54,216]
assert orbit_remainder_types == {18:'straight_line',54:'straight_line',
                                216:'corner'}

# Check one explicit coloring directly in the ORIGINAL graph (not quotient):
# each row below specifies the color of (x,y,z) for all three values of z.
TABLE = ((0, 1, 0), (3, 1, 3), (0, 2, 2))
classes = [sum(1 << INDEX[(x,y,z)] for x,y,z in V
               if TABLE[x][y] == color) for color in range(4)]
assert sorted(x.bit_count() for x in classes) == [6,6,6,9]
assert sum(x.bit_count() for x in classes) == 27
assert all(minimum_degree_at_least(x,3) for x in classes)
print('FOUR_COLOUR_DIRECT_WITNESS_OK', [x.bit_count() for x in classes])
print('FULL_AUTOMORPHISM_ORBIT_CENSUS_OK', sorted(orbit_sizes), orbit_remainder_types)
print('NAMED_FOUR_COLOURINGS_OK', len(partitions)*24)
print('VERIFY_OK')
