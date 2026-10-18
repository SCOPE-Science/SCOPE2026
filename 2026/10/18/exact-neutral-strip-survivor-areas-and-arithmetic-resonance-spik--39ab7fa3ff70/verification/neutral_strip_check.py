#!/usr/bin/env python3
"""Independent geometric checks for the neutral-strip survivor area theorem.

No external packages required. Uses exact rational polygon clipping for
rational parameters and floating clipping for irrational-angle examples.
"""
from fractions import Fraction
from math import acos, cos, pi, sqrt, tan


def clip(poly, a, b, bound):
    if not poly:
        return []
    ans = []
    before = poly[-1]
    vb = a * before[0] + b * before[1] - bound
    for point in poly:
        vp = a * point[0] + b * point[1] - bound
        if (vb <= 0) != (vp <= 0):
            ratio = vb / (vb - vp)
            ans.append((before[0] + ratio * (point[0] - before[0]),
                        before[1] + ratio * (point[1] - before[1])))
        if vp <= 0:
            ans.append(point)
        before, vb = point, vp
    return ans


def polygon_area(poly):
    if not poly:
        return 0
    twice = sum(p[0] * q[1] - p[1] * q[0]
                 for p, q in zip(poly, poly[1:] + poly[:1]))
    return abs(twice) / 2


def polygon_survivor_area(c, h, m, exact=False):
    unit = Fraction(1) if exact else 1.0
    zero = unit * 0
    edge = 1000 * unit
    poly = [(-edge, -edge), (edge, -edge), (edge, edge), (-edge, edge)]
    a, b = unit, -unit
    for _ in range(m):
        poly = clip(poly, a, b, h)
        poly = clip(poly, -a, -b, h)
        a, b = (2 - c) * a + b, -a
    return polygon_area(poly)


def tangent_area_formula(c, h, m):
    theta = acos(1 - c / 2)
    directions = sorted((j * theta) % pi for j in range(m))
    unique = []
    for x in directions:
        if not unique or x - unique[-1] > 1e-9:
            unique.append(x)
    if unique[-1] > pi - 1e-9:
        unique.pop()
    # Numeric floating angle duplicates at the zero angle must coalesce.
    angles = unique
    gaps = [angles[i+1]-angles[i] for i in range(len(angles)-1)]
    gaps.append(pi + angles[0] - angles[-1])
    return h * h / tan(theta / 2) * sum(tan(g / 2) for g in gaps)


def check():
    for c, period, expected in [(1, 3, 3), (2, 2, 2), (3, 3, 1)]:
        c = Fraction(c)
        h = Fraction(1)
        got = polygon_survivor_area(c, h, period, exact=True)
        assert got == expected, (c, got, expected)
        repeat = polygon_survivor_area(c, h, period + 7, exact=True)
        assert repeat == expected, (c, repeat)
    assert polygon_survivor_area(Fraction(1), Fraction(1), 2, True) == 4
    assert polygon_survivor_area(Fraction(3), Fraction(1), 2, True) == Fraction(4, 3)
    # A nonresonant irrational rotation and a high-denominator rational rotation.
    for angle, horizons in [(pi * sqrt(2) / 4, (2, 3, 7, 15, 36)),
                            (pi * 3 / 11, (2, 3, 9, 12, 25))]:
        c = 2 * (1 - cos(angle))
        for n in horizons:
            lhs = polygon_survivor_area(c, 1.0, n)
            rhs = tangent_area_formula(c, 1.0, n)
            assert abs(lhs-rhs) < 4e-8 * max(1, abs(rhs)), (c,n,lhs,rhs)
    # The finite-horizon areas are nonincreasing, reaching the infinite-area
    # formula for rational angles once the full period of unoriented normals appears.
    for c, v in [(1.0, 3), (2.0, 2), (3.0, 3)]:
        a = polygon_survivor_area(c, 1., v)
        th = acos(1-c/2)
        limit = v * tan(pi/(2*v))/tan(th/2)
        assert abs(a-limit) < 1e-9
    print('NEUTRAL_STRIP_POLYGON_AREA_CHECKS_OK')


if __name__ == '__main__':
    check()
