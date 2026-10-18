"""Numerical cross-check of the exact random-direction width law for convex kites.

Requires only Python's standard library. Finite tests supplement, not replace,
the proof for all positive geometric parameters.
"""
from math import acos, asin, atan, cos, hypot, pi, sin, sqrt
from random import Random


def clip(t, lo, hi):
    return max(lo, min(hi, t))


def exact_cdf(a, b, t):
    if a > b:
        a, b = b, a
    if t < 0:
        return 0.0
    p, q = atan(1 / b), atan(1 / a)
    L, s = hypot(1, b), a + b
    first = clip(p - acos(clip(t / 2, 0, 1)), 0, p)
    if t >= L:
        middle = q - p
    else:
        phi = asin(clip(t / L, 0, 1))
        lo, hi = 2 * p, p + q
        middle = max(0, min(hi, phi) - lo)
        middle += max(0, hi - max(lo, pi - phi))
    last = clip(asin(clip(t / s, 0, 1)) - q, 0, pi / 2 - q)
    return (2 / pi) * (first + middle + last)


def vertex_width(a, b, theta):
    c, s = cos(theta), sin(theta)
    dots = [-a*s, c, b*s, -c]
    return max(dots) - min(dots)


def check():
    r = Random(2022)
    cases = [
        (0.24213332485, 1.67502597318), # asymmetric kite in Akiyama--Kamae
        (1, 1), (0.5, 2), (1, 2), (2, 3),
        (1 / 3, 3), (2 - sqrt(3), sqrt(3)),
        (0.5, 0.5), (0.01, 100), (2, 0.6),
    ]
    cases += [(r.uniform(.03, 5), r.uniform(.03, 5)) for _ in range(60)]
    n = 12000
    max_err = 0.0
    for a, b in cases:
        widths = [vertex_width(a, b, (j + .5)*pi/(2*n)) for j in range(n)]
        for k in range(51):
            t = k*(max(2, a+b, hypot(1, a), hypot(1, b)) + 0.2)/50
            empirical = sum(w <= t for w in widths)/n
            analytic = exact_cdf(a, b, t)
            max_err = max(max_err, abs(empirical - analytic))
            assert abs(empirical - analytic) < 2/n + 1e-12, (a, b, t, empirical, analytic)
        assert exact_cdf(a, b, 0) == 0
        assert abs(exact_cdf(a, b, 10000)-1) < 1e-12
        # Numerical Cauchy perimeter identity for mean width.
        avg = sum(widths)/n
        target = (2/pi)*(hypot(1, a)+hypot(1, b))
        assert abs(avg-target) < 1e-7, (a, b, avg, target)
        # Sharp geometric criterion for an additional smooth interior maximum.
        aa, bb = sorted((a, b))
        p, q = atan(1/bb), atan(1/aa)
        theta_max = atan(bb)
        assert (p < theta_max < q) == (bb > 1 and aa*bb < 1)
    print('PASS: %d kite shapes, 51 thresholds each, 12000 angles per shape.' % len(cases))
    print('Worst empirical-CDF discrepancy:', max_err)
    print('All independent projection, mean-width and phase tests passed.')


if __name__ == '__main__':
    check()
