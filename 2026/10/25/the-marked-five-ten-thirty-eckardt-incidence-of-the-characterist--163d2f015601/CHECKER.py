#!/usr/bin/env python3
"""Exact, exhaustive finite-field incidence checks for a marked cubic surface.

Uses only Python's standard library.  Field elements 0,1,w,w+1 are 0,1,2,3
with w^2+w+1=0.  Coordinates are projectively normalized.
"""
from collections import Counter
from itertools import combinations, permutations, product

F4 = range(4)

def mul(a, b):
    c = 0
    for i in (0, 1):
        if (b >> i) & 1:
            c ^= a << i
    if c & 4:
        c ^= 7  # w^2 = w+1
    return c

def inv(a):
    assert a in (1, 2, 3)
    for b in (1, 2, 3):
        if mul(a, b) == 1:
            return b
    raise AssertionError('inverse')

def scale(a, v):
    return tuple(mul(a, x) for x in v)

def add(u, v):
    return tuple(x ^ y for x, y in zip(u, v))

def norm(v):
    return scale(inv(next(x for x in v if x)), v)

def original(v):
    return (v[0] ^ v[1] ^ v[2] ^ v[3],) + v

def cube(a):
    return mul(mul(a, a), a)

def on_cubic(v):
    z = 0
    for a in original(v):
        z ^= cube(a)
    return z == 0

def span_line(p, q):
    return frozenset({q} | {norm(add(p, scale(t, q))) for t in F4})

all_points = {norm(v) for v in product(F4, repeat=4) if any(v)}
assert len(all_points) == 85
points = frozenset(p for p in all_points if on_cubic(p))
assert len(points) == 45
lines = frozenset(span_line(p, q) for p, q in combinations(sorted(points), 2)
                  if span_line(p, q) <= points)
assert len(lines) == 27
assert all(len(line) == 5 for line in lines)
assert Counter(sum(p in line for line in lines) for p in points) == {3: 45}

def point_type(p):
    x = original(p)
    support = [a for a in x if a != 0]
    if len(support) == 2:
        assert len(set(support)) == 1
        return 'P10'
    assert len(support) == 4
    return 'P5' if len(set(support)) == 1 else 'P30'

def over_f2(p):
    return all(a in (0, 1) for a in p)

def line_type(line):
    n = sum(over_f2(p) for p in line)
    assert n in (0, 3)
    return 'L15' if n == 3 else 'L12'

assert Counter(point_type(p) for p in points) == {'P5': 5, 'P10': 10, 'P30': 30}
assert Counter(line_type(line) for line in lines) == {'L15': 15, 'L12': 12}
assert Counter(point_type(p) for p in points if over_f2(p)) == {'P5': 5, 'P10': 10}

S5 = list(permutations(range(5)))
assert len(S5) == 120

def permute_point(p, sigma):
    x = original(p)
    y = tuple(x[i] for i in sigma)
    assert y[0] ^ y[1] ^ y[2] ^ y[3] ^ y[4] == 0
    return norm(y[1:])

def permute_line(line, sigma):
    return frozenset(permute_point(p, sigma) for p in line)

for kind, count in [('P5', 5), ('P10', 10), ('P30', 30)]:
    representative = next(p for p in points if point_type(p) == kind)
    orbit = {permute_point(representative, g) for g in S5}
    assert len(orbit) == count
    assert orbit == {p for p in points if point_type(p) == kind}

for kind, count in [('L15', 15), ('L12', 12)]:
    representative = next(line for line in lines if line_type(line) == kind)
    orbit = {permute_line(representative, g) for g in S5}
    assert len(orbit) == count
    assert orbit == {line for line in lines if line_type(line) == kind}

incidence = Counter((line_type(line), point_type(p)) for line in lines for p in line)
assert incidence == {
    ('L15', 'P5'): 15, ('L15', 'P10'): 30, ('L15', 'P30'): 30,
    ('L12', 'P30'): 60,
}
# Every L15 is incident with (1 P5, 2 P10, 2 P30), and every L12
# with (0 P5, 0 P10, 5 P30).

outer = [line for line in lines if line_type(line) == 'L12']
adjacency = {i: set() for i in range(12)}
for i, j in combinations(range(12), 2):
    if outer[i] & outer[j]:
        assert len(outer[i] & outer[j]) == 1
        adjacency[i].add(j)
        adjacency[j].add(i)
assert all(len(adjacency[i]) == 5 for i in range(12))
assert sum(map(len, adjacency.values())) // 2 == 30
# Check the crown graph: a connected bipartite graph of two six-sets,
# with each vertex joined to five of six vertices across the partition.
color = {0: 0}
pending = [0]
while pending:
    i = pending.pop()
    for j in adjacency[i]:
        if j not in color:
            color[j] = color[i] ^ 1
            pending.append(j)
        else:
            assert color[j] != color[i]
assert len(color) == 12
assert Counter(color.values()) == {0: 6, 1: 6}
assert all(len(adjacency[i]) == 5 for i in range(12))

# Each P30 is the triple intersection of one L15 and two L12 lines.
for p in points:
    line_profile = Counter(line_type(line) for line in lines if p in line)
    expected = {'P5': {'L15': 3}, 'P10': {'L15': 3},
                'P30': {'L15': 1, 'L12': 2}}[point_type(p)]
    assert line_profile == expected

print('PASS: 45 Eckardt points (5+10+30), 27 lines (15+12)')
print('PASS: incidence L15=(1,2,2), L12=(0,0,5)')
print('PASS: 12 outer lines form a 6+6 crown intersection graph')
print('PASS: complete S5 orbits and incidence profiles')
