#!/usr/bin/env python3
"""Exhaustive equality-case census for binary cyclic pair-distance codes."""
from itertools import product

N = 7
MASK = (1 << N) - 1

def pair_weight(x):
    return (x | ((x << 1) & MASK) | (x >> (N - 1))).bit_count()

def double_zero_positions(x):
    return [i for i in range(N)
            if not (x & (1 << i)) and not (x & (1 << ((i + 1) % N)))]

families = [[] for _ in range(N)]
for x in range(1, 1 << N):
    positions = double_zero_positions(x)
    if len(positions) == 1:
        families[positions[0]].append(x)
assert all(len(group) == 5 for group in families)

solutions = []
for words in product(*families):
    if all(pair_weight(x ^ y) == 6
           for i, x in enumerate(words) for y in words[i+1:]):
        solutions.append(frozenset((0, *words)))
assert len(solutions) == 2
assert solutions[0] != solutions[1]
assert all(len(code) == 8 for code in solutions)
assert all({x ^ y for x in code for y in code} == code for code in solutions)

all_codes = set()
for code in solutions:
    for t in range(1 << N):
        all_codes.add(frozenset(x ^ t for x in code))
assert len(all_codes) == 32
assert sum(0 in code for code in all_codes) == 2
for code in all_codes:
    assert min(pair_weight(x ^ y) for x in code for y in code if x != y) == 6

print('VERIFY_OK: two through-zero codes, 32 translated codes; all linear or affine.')
