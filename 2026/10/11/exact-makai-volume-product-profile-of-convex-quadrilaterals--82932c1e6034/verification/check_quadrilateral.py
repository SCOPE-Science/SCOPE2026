"""Supplementary exact-rational checks for the quadrilateral polar-area formula.

Run: python verification/check_quadrilateral.py
Finite checks support, but do not replace, the analytic proof.
"""
from fractions import Fraction as F
from functools import cmp_to_key


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def polar_area_direct(t, s):
    """Intersect all half-planes coming from ordered vertex differences."""
    vs = [(t, F(0)), (F(0), s), (t - 1, F(0)), (F(0), s - 1)]
    normals = [(a[0] - b[0], a[1] - b[1])
               for a in vs for b in vs if a != b]
    corners = set()
    for ax, ay in normals:
        for bx, by in normals:
            det = ax * by - ay * bx
            if det == 0:
                continue
            candidate = ((by - ay) / det, (ax - bx) / det)
            if all(nx * candidate[0] + ny * candidate[1] <= 1
                   for nx, ny in normals):
                corners.add(candidate)
    assert len(corners) >= 4
    centre = (sum(x for x, _ in corners) / len(corners),
              sum(y for _, y in corners) / len(corners))

    def polar_half(v):
        return (v[0] - centre[0], v[1] - centre[1])

    def compare(a, b):
        x, y = polar_half(a), polar_half(b)
        ua = 0 if (x[1] > 0 or (x[1] == 0 and x[0] >= 0)) else 1
        ub = 0 if (y[1] > 0 or (y[1] == 0 and y[0] >= 0)) else 1
        if ua != ub:
            return -1 if ua < ub else 1
        c = cross(x, y)
        return -1 if c > 0 else (1 if c < 0 else 0)

    ordered = sorted(corners, key=cmp_to_key(compare))
    area = abs(sum(cross(ordered[i], ordered[(i + 1) % len(ordered)])
                   for i in range(len(ordered))) / 2)
    return area


def formula(t, s):
    a = (t + s - 1) ** 2 / (2 * max(t * s, (1-t)*(1-s)))
    b = (t - s) ** 2 / (2 * max(t*(1-s), (1-t)*s))
    return 2 - a - b


def main():
    tests = [(F(i, 13), F(j, 13)) for i in range(1, 13)
             for j in range(1, 13)]
    tests += [(F(3, 19), F(17, 29)), (F(7, 10), F(1, 2)),
              (F(1, 100), F(99, 100)), (F(99, 100), F(99, 100))]
    for t, s in tests:
        direct = polar_area_direct(t, s) / 2
        expected = formula(t, s)
        assert direct == expected, (t, s, direct, expected)
        assert F(3, 2) < expected <= 2, (t, s, expected)
        assert (expected == 2) == (t == s == F(1, 2))
    print('EXACT_POLAR_INTERSECTIONS_OK', len(tests))
    print('square', formula(F(1,2), F(1,2)))
    print('trapezoid', formula(F(3,4), F(3,4)))


if __name__ == '__main__':
    main()
