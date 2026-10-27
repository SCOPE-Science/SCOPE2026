#!/usr/bin/env python3
"""Exact F_7 certificate for a tangent-filling smooth cubic.

Requires Python 3 only. Geometric smoothness is proved algebraically in RESULT.md;
this script verifies the finite incidence calculation and its Fermat arrangement.
"""
from collections import Counter

Q = 7

def projective_points():
    # Exactly one representative of each of 7^2+7+1 projective points.
    return [(x, y, 1) for x in range(Q) for y in range(Q)] + [
        (x, 1, 0) for x in range(Q)
    ] + [(1, 0, 0)]

def F(x, y, z):
    return (x*x*y + x*z*z + 2*y*y*z) % Q

def gradient(x, y, z):
    return ((2*x*y + z*z) % Q,
            (x*x + 4*y*z) % Q,
            (2*x*z + 2*y*y) % Q)

def normalize(t):
    for a in t:
        if a % Q:
            iv = pow(a, Q-2, Q)
            return tuple((b*iv) % Q for b in t)
    raise AssertionError('zero tangent vector')

def incident(point, line):
    return sum(a*b for a,b in zip(point,line)) % Q == 0

pts = projective_points()
assert len(pts) == 57 and len(set(pts)) == 57
curve = [p for p in pts if F(*p) == 0]
assert len(curve) == 12
assert all(any(gradient(*p)) for p in curve)
tangents = [normalize(gradient(*p)) for p in curve]
assert len(set(tangents)) == 12
assert all(incident(p,l) for p,l in zip(curve,tangents))

H = {1,2,4}
assert H == {h for h in range(1,Q) if h**3 % Q == 1}
expected = {normalize(v) for v in [
    (1,0,0), (0,1,0), (0,0,1),
    *[(1,-h,0) for h in H],
    *[(1,0,-h) for h in H],
    *[(0,1,-h) for h in H],
]}
assert len(expected) == 12
assert set(tangents) == expected

multiplicities = Counter(sum(incident(p,l) for l in tangents) for p in pts)
assert dict(multiplicities) == {1:36, 2:9, 3:9, 5:3}
assert sum(multiplicities.values()) == 57
assert 0 not in multiplicities
for p in pts:
    x,y,z=p
    assert (x*y*z*(x**3-y**3)*(x**3-z**3)*(y**3-z**3)) % Q == 0
    if x*y*z % Q:
        assert len({x**3 % Q,y**3 % Q,z**3 % Q}) <= 2

assert curve == [
    (0,0,1), (1,5,1), (2,6,1), (3,1,1), (3,5,1),
    (4,3,1), (5,2,1), (5,3,1), (6,4,1), (6,6,1),
    (0,1,0), (1,0,0)]
print('RATIONAL_CURVE_POINTS',len(curve))
print('DISTINCT_TANGENTS',len(tangents))
print('INCIDENCE_MULTIPLICITIES',dict(sorted(multiplicities.items())))
print('COVERED',len(pts))
print('VERIFY_OK')
