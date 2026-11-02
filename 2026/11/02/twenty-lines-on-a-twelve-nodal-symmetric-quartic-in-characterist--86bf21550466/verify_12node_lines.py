#!/usr/bin/env python3
"""Exact independent GF(4) check for the line configuration of a symmetric quartic.

All field operations use the polynomial z^2+z+1 over F_2. The
mathematical argument classifying lines over an algebraic closure is in
RESULT.md; this program verifies the complete resulting finite configuration.
"""
from itertools import combinations, product
from collections import Counter

F = range(4)

def add(a, b):
    return a ^ b

def mul(a, b):
    out = 0
    for i in (0, 1):
        if (b >> i) & 1:
            out ^= (a << i)
    if out & 8:
        out ^= 0b1011  # z^3 = z^2+z; unused for degree <= 2 multiplication
    if out & 4:
        out ^= 0b111   # z^2 = z+1
    return out

def inv(a):
    assert a != 0
    return next(b for b in (1, 2, 3) if mul(a, b) == 1)

def normalize(v):
    m = next(x for x in v if x)
    return tuple(mul(x, inv(m)) for x in v)

def vadd(a, b):
    return tuple(add(x, y) for x, y in zip(a, b))

def smul(a, v):
    return tuple(mul(a, x) for x in v)

def span(a, b):
    assert normalize(a) != normalize(b)
    return frozenset(normalize(vadd(smul(s, a), smul(t, b)))
                     for s, t in product(F, repeat=2) if s or t)

def quartic(p):
    q = 0
    for x in p:
        q ^= mul(x, x)
    for i, j in combinations(range(4), 2):
        q ^= mul(p[i], p[j])
    prod = 1
    for x in p:
        prod = mul(prod, x)
    return prod ^ mul(q, q)

def gradient(p):
    return tuple(mul(mul(p[(i+1)%4], p[(i+2)%4]), p[(i+3)%4])
                 for i in range(4))

# Exhaust every projective F_4 point and every F_4 projective line.
points = sorted({normalize(p) for p in product(F, repeat=4) if any(p)})
assert len(points) == 85
all_lines = {span(a, b) for a, b in combinations(points, 2)}
assert len(all_lines) == 357  # Gaussian binomial [4 choose 2]_4
contained = {line for line in all_lines if all(quartic(p) == 0 for p in line)}
assert len(contained) == 20

# Completely separate structural construction of 8 + 12 listed lines.
coordinate = set()
for z in range(4):
    other = [i for i in range(4) if i != z]
    for coeff in ((1, 2, 3), (1, 3, 2)):
        roots = [p for p in points if p[z] == 0 and
                 (mul(coeff[0], p[other[0]]) ^
                  mul(coeff[1], p[other[1]]) ^
                  mul(coeff[2], p[other[2]])) == 0]
        assert len(roots) == 5
        coordinate.add(frozenset(roots))
assert len(coordinate) == 8
paired = set()
for (i,j),(k,l) in [((0,1),(2,3)), ((0,2),(1,3)), ((0,3),(1,2))]:
    for a, b in product((2,3), repeat=2):
        x=[0]*4; y=[0]*4
        x[i]=a; x[j]=1; y[k]=b; y[l]=1
        paired.add(span(tuple(x), tuple(y)))
assert len(paired) == 12
assert not (coordinate & paired)
assert contained == coordinate | paired

# The twelve isolated geometric nodes are all in F_4.
singular = {p for p in points if quartic(p) == 0 and not any(gradient(p))}
assert len(singular) == 12
assert all(sum(p in line for line in contained) == 4 for p in singular)
assert Counter(len(line & singular) for line in coordinate) == {3:8}
assert Counter(len(line & singular) for line in paired) == {2:12}

# Every pair of distinct projective lines meets in <= 1 point.
intersections = Counter()
smooth_crossings = set()
for L, M in combinations(contained, 2):
    meet = L & M
    assert len(meet) <= 1
    if meet:
        p = next(iter(meet))
        typ = tuple(sorted((('C' if L in coordinate else 'P'),
                            ('C' if M in coordinate else 'P'))))
        intersections[(typ, 'node' if p in singular else 'smooth')] += 1
        if p not in singular:
            smooth_crossings.add(p)
assert intersections == {
    (('C','C'),'node'): 12,
    (('C','P'),'node'): 48,
    (('P','P'),'node'): 12,
    (('C','C'),'smooth'): 4,
    (('P','P'),'smooth'): 18,
}
assert len(smooth_crossings) == 22
assert all(sum(p in line for line in contained) == 2 for p in smooth_crossings)

# Frobenius p -> p^2 has no fixed line or node: each has degree 2.
def frob_point(p):
    return normalize(tuple(mul(x, x) for x in p))
def frob_line(line):
    return frozenset(frob_point(p) for p in line)
assert all(frob_line(line) != line and frob_line(line) in contained for line in contained)
assert all(frob_point(p) != p for p in singular)
assert sum(frob_point(p) == p for p in smooth_crossings) == 4
print('SYMMETRIC_12_NODE_QUARTIC_20_LINES_ALL_CHECKS_PASS')
print('projective_points=85 projective_lines=357 contained_lines=20')
print('singular_nodes=12 coordinate_lines=8 paired_lines=12')
print('nodal_pairs=72 smooth_crossings=22 smooth_F2_crossings=4')
print('line_closed_points_of_degree_2=10 node_closed_points_of_degree_2=6')
