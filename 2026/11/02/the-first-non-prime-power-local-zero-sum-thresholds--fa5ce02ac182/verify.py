"""Exact exhaustive check for the local zero-sum constants at n = 6.
Requires only Python 3 standard library. Executes without external data.
"""
from math import gcd
from collections import Counter

N = 36
UNITS = tuple(x for x in range(N) if gcd(x, 6) == 1)
TARGETS = {x for x in range(N) if gcd(x, N) == 6}
assert UNITS == (1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35)
assert TARGETS == {6, 30}
assert all({(u * v) % N for v in TARGETS} == TARGETS for u in UNITS)

# Every partial multiset is represented by a nondecreasing list of units,
# starting with 1 after a unit normalization. Unrestricted subtree traversal.
histogram = Counter()
max_depth = 0
max_witness = None
nodes = 0

def descend(last_index, chosen, sums):
    global nodes, max_depth, max_witness
    nodes += 1
    depth = len(chosen)
    histogram[depth] += 1
    if depth > max_depth:
        max_depth, max_witness = depth, tuple(chosen)
    for index in range(last_index, len(UNITS)):
        x = UNITS[index]
        next_sums = [set(S) for S in sums]
        for k in range(6, 0, -1):
            next_sums[k].update((r + x) % N for r in sums[k - 1])
        if any(next_sums[k] & TARGETS for k in range(1, 7)):
            continue
        descend(index, chosen + [x], next_sums)

start_sums = [set() for _ in range(7)]
start_sums[0] = {0}
start_sums[1] = {1}
descend(0, [1], start_sums)
assert nodes == sum(histogram.values())
assert max_depth == 12, (max_depth, histogram)
assert nodes == 3944, (nodes, histogram)

# Explicit 12-term counterexample to both upper bounds at length 12.
witness = [1] * 5 + [35] * 5 + [13, 23]
reach = [set() for _ in range(13)]
reach[0] = {0}
for i, a in enumerate(witness):
    for k in range(i + 1, 0, -1):
        reach[k].update((v + a) % N for v in reach[k - 1])
assert all(not (reach[k] & TARGETS) for k in range(1, 13))
assert all(gcd(a, 6) == 1 for a in witness)
print('VERIFY_OK')
print('unit residues:', UNITS)
print('target residues:', sorted(TARGETS))
print('bad-prefix nodes:', nodes)
print('maximal bad length:', max_depth)
print('per-length counts:', sorted(histogram.items()))
print('maximal bad witness:', max_witness)
print('12-term no-target witness:', witness)
