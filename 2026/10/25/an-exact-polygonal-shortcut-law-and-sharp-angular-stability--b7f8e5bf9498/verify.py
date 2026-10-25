#!/usr/bin/env python3
"""Independent numerical checks for the polygon-boundary shortcut law.

Run: python3 verify.py. No third-party dependencies. Finite checks do not
replace the proof for all polygons or the sharpness limit.
"""
from math import pi, sin, cos, sqrt, isclose


def adjacent_pair_area(theta):
    """Directly integrate 1(|s e1-t e2| <= 1) over the positive quadrant."""
    smax = (1.0 / sin(theta)) if theta < pi / 2 else 1.0
    n = 60000  # even, composite Simpson
    step = smax / n
    c, si = cos(theta), sin(theta)
    total = 0.0
    for k in range(n + 1):
        s = k * step
        root = sqrt(max(0.0, 1.0 - (s * si) ** 2))
        hi, lo = s * c + root, s * c - root
        length = max(0.0, hi - max(0.0, lo))
        total += (1 if k == 0 or k == n else (4 if k & 1 else 2)) * length
    return total * step / 3


def f(beta):
    return beta / sin(beta)


def test():
    for theta in (0.4, 0.7, 1.1, pi/2, 2.2, 2.75):
        direct = adjacent_pair_area(theta)
        exact = (pi - theta) / (2 * sin(theta))
        assert abs(direct - exact) < 0.00002, (theta, direct, exact)
    for n in (4, 8, 12, 40, 400):
        b = 2 * pi / n
        eps = 1 / n**2
        betas = [b + (eps if i % 2 else -eps) for i in range(n)]
        excess = sum(f(x) for x in betas) - n * f(b)
        variance = sum((x - b) ** 2 for x in betas)
        assert excess + 1e-12 >= variance / 6
        if n >= 40:
            assert 0.16 < excess / variance < 0.18, (n, excess / variance)
    print("VERIFY_OK: exact adjacent-sector integrals and sharp angular-energy bound")


if __name__ == '__main__':
    test()
