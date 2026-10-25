#!/usr/bin/env python3
"""Finite, deterministic sanity checks for ellipsoid scale-defect formulas.

The mathematical proof is independent of this program. All distances are
Euclidean; this program uses standard-library arithmetic only.
"""
from math import sqrt, sin, cos, pi


def parameters(a, b):
    assert 0 < b <= a
    t0 = b * sqrt(1.0 - (1.0 - (b / a) ** 2) ** 2)
    return t0, b*b/a


def circular_affine_bound(a, b, t):
    assert 0 <= t <= b
    return a * (1.0 - sqrt(max(0.0, 1.0 - (t / b) ** 2)))


def axis_distance(a, b, x):
    """Exact distance from x times a major-axis unit vector to ellipsoid boundary."""
    assert 0 <= x <= a
    if a == b or x >= a - b*b/a:
        return a - x
    return b * sqrt(1.0 - (x*x)/(a*a-b*b))


def chord_witness(a, b, t):
    rho = sqrt(max(0.0, 1.0 - (t/b)**2))
    x = a * rho
    return axis_distance(a, b, x)


checks = 0
for a, b in ((1.0, 1.0), (2.0, 1.0), (5.0, 3.0), (10.0, 1.0)):
    t0, R = parameters(a, b)
    assert 0 < t0 <= b
    assert abs(circular_affine_bound(a, b, t0) - R) < 1e-11
    checks += 2
    for j in range(1, 601):
        t = b * j / 601.0
        upper = circular_affine_bound(a, b, t)
        lower = chord_witness(a, b, t)
        assert lower <= upper + 2e-12
        if t <= t0:
            assert abs(lower - upper) < 2e-12
        elif a > b:
            assert lower < upper - 1e-14
        checks += 1
    if a > b:
        # The axis point is nearest the major endpoint precisely above the cusp.
        x0 = a - b*b/a
        assert abs(axis_distance(a, b, x0) - R) < 1e-12
        checks += 1
        for f in (0.23, 0.71):
            t = t0 + f*(b-t0)
            assert chord_witness(a, b, t) < circular_affine_bound(a, b, t)
            checks += 1

# The exact nearest-point minimization over a 2D ellipse is reproduced on
# a fine deterministic mesh. Grid distance is an upper estimate of the true
# nearest-point distance, and is used only as a numerical sanity check.
for a, b in ((2.0, 1.0), (5.0, 3.0)):
    for j in range(1, 20):
        x = a*j/20.0
        exact = axis_distance(a, b, x)
        mesh = min(sqrt((x-a*cos(2*pi*k/12000))**2+(b*sin(2*pi*k/12000))**2) for k in range(12000))
        assert 0 <= mesh-exact < 2e-4
        checks += 1

print(f"PASS: {checks} finite arithmetic and projection checks")
print("These checks do not establish the quantified all-dimensions proof.")
