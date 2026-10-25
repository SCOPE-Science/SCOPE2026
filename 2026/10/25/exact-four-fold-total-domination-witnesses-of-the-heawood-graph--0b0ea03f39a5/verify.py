"""Exact exhaustive checks for four-fold total-domination witnesses of the Heawood graph.

Run with Python 3 standard library. No external data files are required.
"""
from collections import Counter
from itertools import combinations, permutations, product

# Points of PG(2,2) are the nonzero three-bit vectors 1,...,7.
# A line has the form {u,v,u xor v}.
POINTS = range(1, 8)
LINES = tuple(sorted({tuple(sorted((a, b, a ^ b)))
                      for a in POINTS for b in POINTS if a != b}))
assert len(LINES) == 7
assert all(len(x) == 3 for x in LINES)
assert len({tuple(sorted((a, b))) for line in LINES
            for a, b in combinations(line, 2)}) == 21

LABELS = tuple(combinations(range(4), 2))
BITLABELS = tuple(sum(1 << c for c in pair) for pair in LABELS)
BIT_TO_INDEX = {value: i for i, value in enumerate(BITLABELS)}

def valid(assignment):
    return all((BITLABELS[assignment[a - 1]] |
                BITLABELS[assignment[b - 1]] |
                BITLABELS[assignment[c - 1]]) == 15
               for a, b, c in LINES)

# First calculation: test each of the 6**7 possible seven-point assignments.
valid_assignments = [q for q in product(range(6), repeat=7) if valid(q)]
assert len(valid_assignments) == 1008
assert all(sorted(Counter(q).values()) == [1, 1, 1, 1, 1, 2]
           for q in valid_assignments)
assert all(sum(v > 1 for v in Counter(q).values()) == 1
           for q in valid_assignments)

# Independently: normalize the duplicated label at points 1,2 to {0,1};
# the line's third point 3 then has label {2,3}. Enumerate only four free
# positions. The proof establishes that every assignment normalizes this way.
pair = BIT_TO_INDEX[(1 << 0) | (1 << 1)]
complement = BIT_TO_INDEX[(1 << 2) | (1 << 3)]
local_solutions = []
for four in product(range(6), repeat=4):
    seq = (pair, pair, complement) + four
    if valid(seq):
        local_solutions.append(seq)
assert len(local_solutions) == 8
assert all(sorted(Counter(q).values()) == [1, 1, 1, 1, 1, 2]
           for q in local_solutions)
assert 21 * 6 * len(local_solutions) == len(valid_assignments)

# Verify the stated one-orbit classification under projective collineations
# (invertible 3-by-3 matrices over F_2) and permutations of four colors.
linear_maps = set()
for a, b, c in product(POINTS, repeat=3):
    sigma = tuple((a if x & 1 else 0) ^
                  (b if x & 2 else 0) ^
                  (c if x & 4 else 0)
                  for x in POINTS)
    if set(sigma) == set(POINTS):
        linear_maps.add(sigma)
assert len(linear_maps) == 168
perms = []
for p in permutations(range(4)):
    tr = tuple(BIT_TO_INDEX[sum(1 << p[c] for c in LABELS[i])]
               for i in range(6))
    perms.append(tr)
assert len(perms) == 24
base = local_solutions[0]
orbit = set()
for perm in linear_maps:
    moved = [None] * 7
    for i, point_image in enumerate(perm):
        moved[point_image - 1] = base[i]
    for relabel in perms:
        orbit.add(tuple(relabel[x] for x in moved))
assert orbit == set(valid_assignments)

# Incidence graph H is bipartite, with two independently constrained copies
# of this seven-point problem (the second is the dual Fano plane).
N_NAMED = len(valid_assignments) ** 2
assert N_NAMED == 1016064
# Every one-sided solution uses all six two-subsets, so the global action of
# S4 on the four named total dominating sets is free; all four sets differ.
assert N_NAMED % 24 == 0
N_UNNAMED = N_NAMED // 24
assert N_UNNAMED == 42336

print('FANO_POINTS=7 LINES=7 COLOR_PAIRS=6')
print('BRUTE_FORCE_ONE_SIDE=1008')
print('REPEATED_LABEL_PATTERN=2,1,1,1,1,1')
print('NORMALIZED_FOUR_VERTEX_COMPLETIONS=8')
print('COUNT_FACTOR=21*6*8=1008')
print('LINEAR_COLLINEATIONS=168 COLOR_PERMUTATIONS=24')
print('ONE_SIDE_SYMMETRY_ORBIT=1008')
print('HEAWOOD_NAMED_WITNESSES=1016064')
print('HEAWOOD_UNNAMED_FAMILIES=42336')
print('VERIFY_OK')
