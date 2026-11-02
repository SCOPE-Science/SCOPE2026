#!/usr/bin/env python3
"""Finite checks of the exact finite-ring non-Hermitian cage amplification law.

Uses only the Python standard library. Finite checks supplement the analytic proof.
"""
import cmath
import math


def mm(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def dagger(a):
    return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a))]


def norm_f2(a):
    return sum(abs(z) ** 2 for row in a for z in row)


def difference(a, b):
    return max(abs(a[i][j] - b[i][j]) for i in range(len(a)) for j in range(len(a)))


def identity(n):
    return [[complex(i == j) for j in range(n)] for i in range(n)]


def block(j, h, k):
    e = cmath.exp(1j * k)
    em = math.exp(-h)
    ep = math.exp(h)
    return [
        [0j, 0j, -j * (em + e)],
        [0j, 0j, -j * (-1 + ep * e)],
        [-j * (ep + e.conjugate()), -j * (-1 + em * e.conjugate()), 0j],
    ]


def propagate(b, j, t):
    b2 = mm(b, b)
    linear = -1j * math.sin(2 * j * t) / (2 * j)
    quadratic = (math.cos(2 * j * t) - 1) / (4 * j * j)
    return [[complex(i == p) + linear * b[i][p] + quadratic * b2[i][p]
             for p in range(3)] for i in range(3)]


def gain_from_trace(f):
    q = math.sqrt((f + 1) / 4)
    return q + math.sqrt(max(q * q - 1, 0))


def c_closed(n):
    if n % 4 == 0:
        return 0.0
    if n % 2:
        return math.sin(math.pi / (2 * n)) ** 2
    return math.sin(math.pi / n) ** 2


def gain_closed(n, h):
    u = math.sinh(h) ** 2
    q2 = 1 + u * (2 + u - c_closed(n))
    return math.sqrt(q2) + math.sqrt(max(q2 - 1, 0))


def approximate_gain(e):
    # Direct power method on E*E; independent from reciprocal-pair trace formula.
    m = mm(dagger(e), e)
    v = [1 + .3j, .17 - .4j, -.43 + .2j]
    for _ in range(450):
        w = [sum(m[i][k] * v[k] for k in range(3)) for i in range(3)]
        length = math.sqrt(sum(abs(z) ** 2 for z in w))
        v = [z / length for z in w]
    w = [sum(m[i][k] * v[k] for k in range(3)) for i in range(3)]
    return math.sqrt(max(0, sum((v[i].conjugate() * w[i]).real for i in range(3))))


def run():
    checks = 0
    for n in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 23, 24, 25, 28]:
        cs = [math.cos(2 * math.pi * m / n) ** 2 for m in range(n)]
        assert abs(min(cs) - c_closed(n)) < 3e-14
        checks += 1
        for h in [-1.4, -.8, -.35, .35, .8, 1.4]:
            u = math.sinh(h) ** 2
            predicted_global = gain_closed(n, h)
            observed_global = 0.0
            for m in range(n):
                k = 2 * math.pi * m / n
                b = block(1.0, h, k)
                b2 = mm(b, b)
                b3 = mm(b2, b)
                assert difference(b3, [[4 * z for z in row] for row in b]) < 4e-12
                checks += 1
                assert abs(norm_f2(b) - 8 * math.cosh(h) ** 2) < 3e-12
                assert abs(norm_f2(b2) - 16 * (math.cosh(h) ** 4 - u * cs[m] + 1)) < 5e-11
                checks += 2
                for t in [0.07, 0.35, .7, 1.09, math.pi / 2, 1.8, 2.5, math.pi]:
                    e = propagate(b, 1.0, t)
                    ss = math.sin(t) ** 2
                    f = 3 + 8 * u * ss + 4 * u * (u - cs[m]) * ss * ss
                    assert abs(norm_f2(e) - f) < 2e-10
                    checks += 1
                    g = gain_from_trace(f)
                    assert g <= predicted_global + 4e-12
                    checks += 1
                    if t == math.pi / 2:
                        observed_global = max(observed_global, approximate_gain(e))
                        assert abs(approximate_gain(e) - g) < 2e-8
                        checks += 1
            assert abs(observed_global - predicted_global) < 2e-8
            checks += 1
    for n in [2, 3, 4, 5, 8]:
        for m in range(n):
            b = block(1.0, 0.0, 2 * math.pi * m / n)
            for t in [.2, .7, 1.5]:
                e = propagate(b, 1, t)
                assert difference(mm(dagger(e), e), identity(3)) < 1e-12
                checks += 1
    print('PASS:', checks, 'finite numerical checks; analytic arguments establish the all-parameter theorem.')


if __name__ == '__main__':
    run()
