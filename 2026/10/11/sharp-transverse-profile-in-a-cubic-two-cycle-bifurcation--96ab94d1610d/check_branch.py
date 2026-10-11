#!/usr/bin/env python3
"""Independent finite-precision consistency checks for the cubic-cycle formulas.
The mathematical proof is analytic; these checks are not certificates of novelty or of an infinite theorem.
"""
import math

A0 = -0.25
TWO_PI = 2.0 * math.pi


def coefficients(phi, a):
    p = a - math.sin(phi) * math.cos(phi)
    g = p - math.sin(phi) ** 2
    return p, g


def integrate(rhs, y0, n=16000):
    h = TWO_PI / n
    v = list(y0)
    for k in range(n):
        t = k * h
        k1 = rhs(t, v)
        k2 = rhs(t + h / 2, [x + h * z / 2 for x, z in zip(v, k1)])
        k3 = rhs(t + h / 2, [x + h * z / 2 for x, z in zip(v, k2)])
        k4 = rhs(t + h, [x + h * z for x, z in zip(v, k3)])
        v = [x + h * (b1 + 2 * b2 + 2 * b3 + b4) / 6
             for x, b1, b2, b3, b4 in zip(v, k1, k2, k3, k4)]
    return v


def variational_rhs(phi, y):
    p, g = coefficients(phi, A0)
    L = 2 * p / g
    B = 2 * (p / g) ** 2
    return [L * y[0], L * y[1] + B * y[0] ** 2]


def poincare(w, a):
    def rhs(phi, y):
        p, g = coefficients(phi, a)
        return [2 * p * y[0] * (1 + y[0]) / (g - y[0] * math.sin(phi) ** 2)]
    return integrate(rhs, [w], n=12000)[0]


def run():
    m, C = integrate(variational_rhs, [1, 0])
    assert abs(m - 1) < 1e-9, m
    assert 26.8029 < C < 26.8030, C
    slope = 32 * math.pi / C
    assert 3.7507 < slope < 3.7508, slope
    for a in [A0 - 0.0005, A0 + 0.0005]:
        d = a - A0
        w0 = slope * d
        p0 = poincare(w0, a)
        assert abs((p0 - w0) / w0) < 0.003, (a, p0, w0)
    print('CHECK_OK C=%.10f kappa=%.10f' % (C, slope))


if __name__ == '__main__':
    run()
