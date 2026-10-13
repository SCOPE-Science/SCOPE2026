#!/usr/bin/env python3
"""Exact exhaustive enumeration of short comma-free error-detecting codes."""
from collections import Counter
from itertools import combinations
from pathlib import Path

WIDTH = 6
MASK = (1 << WIDTH) - 1

def rotate(word, step):
    return ((word << step) & MASK) | (word >> (WIDTH - step))

def primitive(word):
    return len({rotate(word, t) for t in range(WIDTH)}) == WIDTH

def splice(left, right, amount):
    return (((left << WIDTH) | right) >> (WIDTH - amount)) & MASK

candidates = tuple(word for word in range(1 << WIDTH) if primitive(word))
assert len(candidates) == 54
levels = Counter()
solutions = []

def compatible(code, new):
    if any((new ^ old).bit_count() < 3 for old in code):
        return False
    expanded = code + (new,)
    hits = set(expanded)
    return all(splice(left, right, t) not in hits
               for left in expanded for right in expanded
               for t in range(1, WIDTH))

def dfs(code, next_position):
    levels[len(code)] += 1
    if len(code) == 6:
        solutions.append(code)
    for position in range(next_position, len(candidates)):
        word = candidates[position]
        if compatible(code, word):
            dfs(code + (word,), position + 1)

dfs((), 0)
assert dict(levels) == {0: 1, 1: 54, 2: 814, 3: 3042, 4: 2480, 5: 324, 6: 16}
assert len(solutions) == 16

def reverse(word):
    return int(f'{word:06b}'[::-1], 2)

def transform(code, fn):
    return tuple(sorted(fn(word) for word in code))

all_codes = set(solutions)
seen = set()
orbits = []
for code in solutions:
    if code in seen:
        continue
    orbit = {transform(code, lambda w:w),
             transform(code, reverse),
             transform(code, lambda w:w ^ MASK),
             transform(code, lambda w:reverse(w ^ MASK))}
    assert orbit <= all_codes
    seen.update(orbit)
    orbits.append(orbit)
assert sorted(map(len, orbits)) == [4, 4, 4, 4]
assert seen == all_codes

for code in solutions:
    distances = Counter((left ^ right).bit_count() for left, right in combinations(code, 2))
    assert distances == Counter({3: 8, 4: 7})

expected = {tuple(int(w, 2) for w in line.split())
            for line in Path(__file__).with_name('optimal_codes.txt').read_text(encoding='utf-8').splitlines() if line.strip()}
assert expected == all_codes
print('VERIFY_OK: primitive=54, subtree_counts=1/54/814/3042/2480/324/16,')
print('maximum=6, optimizers=16, reversal-complement_orbits=4, distance_spectrum=8*3+7*4')
