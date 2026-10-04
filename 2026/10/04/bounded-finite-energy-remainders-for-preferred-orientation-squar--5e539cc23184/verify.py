#!/usr/bin/env python3
import math


def bisect(fun, a, b, target=0.0, steps=100):
    fa = fun(a) - target
    fb = fun(b) - target
    assert fa * fb <= 0.0
    for _ in range(steps):
        c = 0.5 * (a + b)
        fc = fun(c) - target
        if fa * fc <= 0.0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    return 0.5 * (a + b)


def square_gap_width(m, ell):
    t = m * math.pi
    def f(y):
        k = (t + y) / ell
        return math.cos(y) - (k * k - 1.0) / (k * k + 1.0)
    scale = ell / t
    ym = bisect(f, -5.0 * scale, -1.0e-15)
    yp = bisect(f, 1.0e-15, 5.0 * scale)
    return ((t + yp) ** 2 - (t + ym) ** 2) / (ell ** 2)


def hex_d(y, m, ell):
    t = m * math.pi
    k = (t + y) / ell
    return (k**4 - 6.0*k*k - 3.0 - (k*k + 3.0)**2 * math.cos(2.0*y)) / (4.0 * (k*k - 1.0))


def hex_root(m, ell, d, sign):
    t = m * math.pi
    lead = math.sqrt(2.0 * (d + 3.0)) * ell / t
    if sign < 0:
        return bisect(lambda y: hex_d(y, m, ell), -2.0*lead, -0.3*lead, d)
    return bisect(lambda y: hex_d(y, m, ell), 0.3*lead, 2.0*lead, d)


def hex_pair_width(m, ell):
    y3m = hex_root(m, ell, 3.0, -1)
    y1m = hex_root(m, ell, -1.0, -1)
    y1p = hex_root(m, ell, -1.0, 1)
    y3p = hex_root(m, ell, 3.0, 1)
    t = m * math.pi
    def energy(y):
        return ((t + y) / ell) ** 2
    return (energy(y1m) - energy(y3m)) + (energy(y3p) - energy(y1p))


def square_asym(m, ell):
    return 8.0/ell - 8.0*ell/(3.0*(m*math.pi)**2)


def hex_asym(m, ell):
    return 8.0*(math.sqrt(3.0)-1.0)/ell + 8.0*ell*(4.0-3.0*math.sqrt(3.0))/(3.0*(m*math.pi)**2)


for ell in (0.5, 1.0, 2.3):
    for m in (50, 100):
        gs = square_gap_width(m, ell)
        gh = hex_pair_width(m, ell)
        # Second-order formula is already very accurate.
        assert abs(gs - square_asym(m, ell)) < 2.0e-6
        assert abs(gh - hex_asym(m, ell)) < 6.0e-6
        # Multiplying the residual by m^4 should remain bounded at these scales.
        assert abs(gs - square_asym(m, ell)) * m**4 < 2.0
        assert abs(gh - hex_asym(m, ell)) * m**4 < 8.0

print('VERIFY_OK')
