#!/usr/bin/env python3
"""Numerical consistency checks for the explicit side-information instance."""
from itertools import combinations
from math import log2, isclose

p = {"a": 4/15, "b": 5/15, "c": 5/15, "d": 1/15}
L = log2(3)

def h(x):
    return -x*log2(x) - (1-x)*log2(1-x)

h1 = h(1/3)
def entropy(partition):
    masses = [sum(p[y] for y in block) for block in partition]
    return -sum(m*log2(m) for m in masses)

def rate(partition):
    total = 0.0
    for block in partition:
        mass = sum(p[y] for y in block)
        # A singleton a,b,c has a 1-versus-2 output partition.
        # Every other block has the discrete output partition.
        block_entropy = h1 if len(block) == 1 and block[0] in "abc" else L
        total += mass * block_entropy
    return total

def canonical(blocks):
    return tuple(sorted((tuple(sorted(b)) for b in blocks), key=lambda b: b[0]))

symbols = ("a", "b", "c", "d")
initial = canonical([(y,) for y in symbols])
H0, R0 = entropy(initial), rate(initial)
candidate_slopes = {}
for i, j in combinations(symbols, 2):
    blocks = [list(b) for b in initial if b[0] not in (i, j)]
    blocks.append([i, j])
    nxt = canonical(blocks)
    candidate_slopes[(i, j)] = (rate(nxt)-R0)/(entropy(nxt)-H0)

best = max(candidate_slopes.values())
winners = [pair for pair, slope in candidate_slopes.items()
           if isclose(slope, best, rel_tol=0, abs_tol=1e-12)]
assert winners == [("b", "c")], (candidate_slopes, winners)

P = canonical([("a",), ("b", "c"), ("d",)])
Q = canonical([("a", "b", "d"), ("c",)])
entropy_gap = entropy(P)-entropy(Q)
rate_gap = rate(P)-rate(Q)
expected_entropy_gap = (5*log2(5)-8)/15
expected_rate_gap = 2/45
assert entropy_gap > 0 and rate_gap > 0
assert isclose(entropy_gap, expected_entropy_gap, rel_tol=0, abs_tol=1e-12)
assert isclose(rate_gap, expected_rate_gap, rel_tol=0, abs_tol=1e-12)
assert isclose(best, -2/3, rel_tol=0, abs_tol=1e-12)

print("VERIFY_OK unique_first_merge=b,c")
print("slopes=" + "; ".join(f"{a}{b}:{s:.12f}" for (a,b),s in candidate_slopes.items()))
print(f"entropy_gap={entropy_gap:.12f} expected={expected_entropy_gap:.12f}")
print(f"rate_gap={rate_gap:.12f} expected={expected_rate_gap:.12f}")
