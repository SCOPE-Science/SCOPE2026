"""Exact finite census and symmetry verification for binary radius-one covering cycles.

Only Python's standard library is needed. Positions are indexed modulo the
cycle length, and the least significant integer bit denotes position zero.
This is an exhaustive computation, not a random search.
"""
from collections import Counter
from pathlib import Path

WINDOW = 7
MAX_LENGTH = 22
balls = []
for a in range(1 << WINDOW):
    coverage = 0
    for b in range(1 << WINDOW):
        if (a ^ b).bit_count() <= 1:
            coverage |= 1 << b
    balls.append(coverage)
all_covered = (1 << (1 << WINDOW)) - 1

def windows(x, length):
    if length >= WINDOW:
        zz = x | (x << length)
        for j in range(length):
            yield (zz >> j) & ((1 << WINDOW) - 1)
    else:
        for j in range(length):
            yield sum(((x >> ((j + k) % length)) & 1) << k
                      for k in range(WINDOW))

def is_cover(x, length):
    union = 0
    for w in windows(x, length):
        union |= balls[w]
    return union == all_covered

counts = {}
solutions = set()
for m in range(1, MAX_LENGTH + 1):
    count = 0
    for x in range(1 << m):
        if is_cover(x, m):
            count += 1
            if m == MAX_LENGTH:
                solutions.add(x)
    counts[m] = count
assert all(counts[m] == 0 for m in range(1, MAX_LENGTH)), counts
assert counts[MAX_LENGTH] == 132 and len(solutions) == 132, counts
assert all(x.bit_count() == 11 for x in solutions)

MASK = (1 << MAX_LENGTH) - 1

def rotate(x):
    return (x >> 1) | ((x & 1) << (MAX_LENGTH - 1))

def mirror(x):
    return int(f'{x:0{MAX_LENGTH}b}'[::-1], 2)

def orbit(x):
    out = set()
    for y in (x, x ^ MASK, mirror(x), mirror(x) ^ MASK):
        for _ in range(MAX_LENGTH):
            out.add(y)
            y = rotate(y)
    return out

remaining = set(solutions)
orbits = []
while remaining:
    rep = min(remaining)
    klass = orbit(rep)
    assert klass <= solutions
    orbits.append((rep, len(klass)))
    remaining -= klass
assert orbits == [(141243, 44), (158331, 88)], orbits

for x in solutions:
    ws = list(windows(x, MAX_LENGTH))
    assert len(set(ws)) == MAX_LENGTH
    multiplicities = Counter(sum((a ^ w).bit_count() <= 1 for w in ws)
                             for a in range(1 << WINDOW))
    assert multiplicities == Counter({1: 80, 2: 48}), multiplicities

# Exact witness list is a convenience copy; the census itself does not use it.
path = Path(__file__).with_name('optimal_cycles.txt')
if path.exists():
    recorded = [int(s.strip()[::-1], 2) for s in path.read_text().splitlines()]
    assert len(recorded) == 132 and set(recorded) == solutions

print('VERIFY_OK: optimum 22; 132 indexed optimal cycles; two orbits of 44, 88; all balanced')
