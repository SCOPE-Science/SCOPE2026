"""Exhaustive independent-block partition certificate for proper symmetry-breaking colourings of KG(5,2)."""
from itertools import combinations, permutations
from collections import Counter
from math import factorial

symbols = range(5)
vertices = tuple(combinations(symbols, 2))
index = {pair: i for i, pair in enumerate(vertices)}
assert len(vertices) == 10
edges = tuple((i, j) for i in range(10) for j in range(i + 1, 10)
              if set(vertices[i]).isdisjoint(vertices[j]))
assert len(edges) == 15
independent = tuple(m for m in range(1, 1 << 10)
                    if all(not ((m >> i) & (m >> j) & 1) for i, j in edges))
by_bit = [[] for _ in range(10)]
for block in independent:
    for bit in range(10):
        if (block >> bit) & 1:
            by_bit[bit].append(block)

group = []
for perm in permutations(symbols):
    group.append(tuple(index[tuple(sorted((perm[a], perm[b])))] for a, b in vertices))
assert len(group) == len(set(group)) == 120

def image(block, perm):
    return sum(1 << perm[i] for i in range(10) if (block >> i) & 1)

hist = Counter()
proper_partitions = []

def visit(unused, blocks):
    if not unused:
        blocks = tuple(sorted(blocks))
        stabilizer = sum(all(image(b, perm) == b for b in blocks) for perm in group)
        hist[len(blocks), stabilizer] += 1
        if len(blocks) == 4:
            proper_partitions.append((blocks, stabilizer))
        return
    first = (unused & -unused).bit_length() - 1
    for block in by_bit[first]:
        if block & unused == block:
            visit(unused ^ block, blocks + (block,))

visit((1 << 10) - 1, ())
expected = {
    3: {6: 20},
    4: {1: 160, 2: 350, 6: 10},
    5: {1: 1844, 2: 400},
    6: {1: 2745, 2: 120},
    7: {1: 1425, 2: 10},
    8: {1: 315},
    9: {1: 30},
    10: {1: 1},
}
assert dict(hist) == {(k, s): n for k, row in expected.items() for s, n in row.items()}
assert sum(hist.values()) == 7430

partmap = {p: stabilizer for p, stabilizer in proper_partitions}
remaining = set(partmap)
orbit_hist = Counter()
distinguished_orbits = Counter()
while remaining:
    rep = min(remaining)
    orbit = {
        tuple(sorted(image(b, g) for b in rep))
        for g in group
    }
    assert orbit <= remaining
    remaining -= orbit
    stab = partmap[rep]
    shape = tuple(sorted((b.bit_count() for b in rep), reverse=True))
    orbit_hist[(shape, len(orbit), stab)] += 1
    if stab == 1:
        distinguished_orbits[(shape, len(orbit))] += 1

expected_orbits = {
 ((3,3,2,2),30,2):1,
 ((3,3,2,2),60,2):2,
 ((3,3,2,2),120,1):1,
 ((3,3,3,1),10,6):1,
 ((3,3,3,1),20,2):1,
 ((3,3,3,1),60,2):1,
 ((4,2,2,2),40,1):1,
 ((4,3,2,1),60,2):2,
}
assert dict(orbit_hist) == expected_orbits
assert dict(distinguished_orbits) == {((3,3,2,2),120):1,((4,2,2,2),40):1}

numbers = [0] * 11
for k in range(11):
    numbers[k] = hist[k, 1]
assert numbers[4:] == [160,1844,2745,1425,315,30,1]

def eval_poly(q, counts):
    result = 0
    falling = 1
    for k in range(11):
        if k:
            falling *= q - k + 1
        result += counts[k] * falling
    return result

assert eval_poly(3, numbers) == 0
assert eval_poly(4, numbers) == 3840
assert eval_poly(5, numbers) == 240480
print('PARTITION_VERIFIER_PASS: 7430 proper partitions; all stabilizers and 10 four-class orbits')
print('DISTINGUISHING_FALLING_COEFFICIENTS', numbers)
print('ORBIT_TABLE', sorted(orbit_hist.items()))
