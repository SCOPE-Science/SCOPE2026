"""Exhaustive exact verification for six-agent triadic IR allocations.

Run with Python 3 stdlib: python3 verify.py
Each 15-bit mask denotes the friendship edges of a labeled simple graph.
"""
from collections import Counter
from itertools import combinations, permutations
from math import comb

N = 6
EDGES = tuple(combinations(range(N), 2))
EDGE_INDEX = {e: i for i, e in enumerate(EDGES)}
assert len(EDGES) == 15
TRIPLES = tuple(combinations(range(N), 3))
PARTITIONS = tuple(
    (tuple(sorted((0, a, b))), tuple(i for i in range(N) if i not in (0, a, b)))
    for a, b in combinations(range(1, N), 2)
)
assert len(PARTITIONS) == 10


def triple_mask(t):
    return sum(1 << EDGE_INDEX[pair] for pair in combinations(t, 2))


TRIPLE_BITS = {t: triple_mask(t) for t in TRIPLES}
PARTITION_BITS = tuple((TRIPLE_BITS[a], TRIPLE_BITS[b]) for a, b in PARTITIONS)


def ir_triple(mask, bits):
    return (mask & bits).bit_count() >= 2


def independently_connected(mask, triple):
    # Independent adjacency/reachability test; not an edge-count test.
    reached = {triple[0]}
    remaining = set(triple) - reached
    while remaining:
        progress = False
        for x in tuple(remaining):
            if any((mask & (1 << EDGE_INDEX[tuple(sorted((x, y)))])) for y in reached):
                reached.add(x)
                remaining.remove(x)
                progress = True
        if not progress:
            return False
    return True


def relabel_mask(template_edges, perm):
    out = 0
    for a, b in template_edges:
        u, v = sorted((perm[a], perm[b]))
        out |= 1 << EDGE_INDEX[(u, v)]
    return out


K4_K2 = tuple(combinations(range(4), 2)) + ((4, 5),)
STAR_TWO_PAIRS = tuple((0, i) for i in range(1, 6)) + ((1, 2), (3, 4))
ORBIT_K4_K2 = {relabel_mask(K4_K2, p) for p in permutations(range(N))}
ORBIT_STAR = {relabel_mask(STAR_TWO_PAIRS, p) for p in permutations(range(N))}
assert len(ORBIT_K4_K2) == 15 and len(ORBIT_STAR) == 90
assert not (ORBIT_K4_K2 & ORBIT_STAR)

H = Counter()
DENSE_FAILURES = set()
SIX_MASKS = 1 << len(EDGES)
for mask in range(SIX_MASKS):
    connected = {t: ir_triple(mask, TRIPLE_BITS[t]) for t in TRIPLES}
    # All connected triples are independently recomputed using reachability.
    assert all(connected[t] == independently_connected(mask, t) for t in TRIPLES)
    z = sum(connected[a] and connected[b] for a, b in PARTITIONS)
    k = mask.bit_count()
    H[(k, z)] += 1
    degrees = [sum(bool(mask & (1 << EDGE_INDEX[e])) for e in EDGES if v in e) for v in range(N)]
    if z == 0 and min(degrees) > 0:
        assert k <= 7
        if k == 7:
            DENSE_FAILURES.add(mask)

SUCCESS_COUNTS = [0, 0, 0, 0, 90, 870, 3130, 5610, 6165, 4945, 2997, 1365, 455, 105, 15, 1]
MULTIPLICITY_COUNTS = [7020, 6520, 5400, 4860, 2460, 2592, 1740, 1260, 360, 480, 76]
assert sum(H.values()) == SIX_MASKS
assert [sum(H[(k, z)] for z in range(1, 11)) for k in range(16)] == SUCCESS_COUNTS
assert [sum(H[(k, z)] for k in range(16)) for z in range(11)] == MULTIPLICITY_COUNTS
assert all(sum(H[(k, z)] for z in range(11)) == comb(15, k) for k in range(16))
assert sum(SUCCESS_COUNTS) == 25748
assert 25748 * 8192 == 6437 * 32768
assert sum(z * n for z, n in enumerate(MULTIPLICITY_COUNTS)) == 10 * (SIX_MASKS // 4)
assert DENSE_FAILURES == ORBIT_K4_K2 | ORBIT_STAR
assert [H[(k, 10)] for k in range(16)] == [0] * 12 + [15, 45, 15, 1]

print('PASS: all 32,768 labeled friendship graphs, ten partitions, and independent reachability')
print('PASS: all 16 edge-count layers, 11 multiplicity layers, 15 binomial totals')
print('PASS: 25,748 feasible profiles and probability 6,437/8,192 at p=1/2')
print('PASS: 8-edge isolation-only obstruction boundary')
print('PASS: 7-edge dense obstructions form two orbits, of sizes 15 and 90')
print('PASS: all-ten-feasible coefficient vector for matching enmity graphs')

# Check the independently stored full coefficient table at the same time.
import csv
from pathlib import Path
table_path = Path(__file__).resolve().parent / 'multiplicity_coefficients.csv'
with table_path.open(newline='', encoding='utf-8') as fp:
    rows = list(csv.DictReader(fp))
assert len(rows) == 16
for j, row in enumerate(rows):
    assert int(row['friendly_edges']) == j
    assert int(row['total']) == comb(15, j)
    assert all(int(row['Z_' + str(z)]) == H[(j, z)] for z in range(11))
print('PASS: separately embedded 16-by-11 exact table matches direct enumeration')
