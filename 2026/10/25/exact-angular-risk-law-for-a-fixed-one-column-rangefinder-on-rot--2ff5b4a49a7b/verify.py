#!/usr/bin/env python3
"""Standalone exact-rational and finite numerical checks for a rotating SPD rangefinder theorem.

Finite tests supplement, and do not replace, its analytic proof.
"""
from fractions import Fraction as F
from math import sin, cos, pi, sqrt, asin


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(z) for z in zip(*a)]


def power(a, k):
    ans = [[F(int(i == j)) for j in range(len(a))] for i in range(len(a))]
    for _ in range(k):
        ans = mul(ans, a)
    return ans


def check_exact(a, b, c, s, omega, m):
    d = [[a, F(0)], [F(0), b]]
    r = [[c, -s], [s, c]]
    assert c * c + s * s == 1
    mat = mul(mul(r, d), transpose(r))
    y = mul(power(mat, m), [[omega[0]], [omega[1]]])
    yy = sum(y[i][0] ** 2 for i in range(2))
    pa = [[sum(y[i][0] * y[k][0] * mat[k][j] for k in range(2)) / yy
           for j in range(2)] for i in range(2)]
    err_sq = sum((mat[i][j] - pa[i][j]) ** 2
                 for i in range(2) for j in range(2))
    v = mul(transpose(r), [[omega[0]], [omega[1]]])
    v0, v1 = v[0][0], v[1][0]
    explicit = ((b*b)*(a**(2*m))*v0*v0 + (a*a)*(b**(2*m))*v1*v1) / (a**(2*m)*v0*v0 + b**(2*m)*v1*v1)
    assert err_sq == explicit, (err_sq, explicit)


def sqerr(a, b, theta, m):
    cs, sn = cos(theta), sin(theta)
    return (b*b*a**(2*m)*cs*cs + a*a*b**(2*m)*sn*sn) / (a**(2*m)*cs*cs + b**(2*m)*sn*sn)


def minimax_sq(a, b, length, m):
    c2 = cos(length / 2)**2
    s2 = sin(length / 2)**2
    return (b*b*a**(2*m)*c2 + a*a*b**(2*m)*s2) / (a**(2*m)*c2 + b**(2*m)*s2)


def run():
    a, b, c, s = F(4), F(1), F(3, 5), F(4, 5)
    for omega in ((F(2), F(5)), (F(7), F(-3))):
        for m in (1, 3, 5):
            check_exact(a, b, c, s, omega, m)
    # The minimax formula is checked against a numerical search, not used as proof.
    for m in (1, 3, 5):
        length = pi / 3
        opt = minimax_sq(4, 1, length, m)
        center = max(sqerr(4, 1, length / 2 - t, m)
                     for t in (0.0, length / 2, length))
        assert abs(center - opt) < 1e-12
        for j in range(221):
            phi = pi * j / 220
            trial = max(sqerr(4, 1, phi - length * k / 160, m)
                        for k in range(161))
            assert trial >= opt - 1e-12
    # A full half-turn yields pathwise mean squared error exactly a*b for m=1.
    for a, b in ((4.0, 1.0), (7.0, 2.0), (1.3, 0.9)):
        for phi in (0.0, 0.27, 1.39, 2.91):
            n = 8192
            midpoint = sum(sqerr(a, b, phi - pi*(j+0.5)/n, 1)
                           for j in range(n)) / n
            assert abs(midpoint - a*b) < 3e-10, (a, b, phi, midpoint)
    # The exact critical-direction geometry gives a uniform-probability atom.
    length = pi / 3
    n = 12000
    count = sum(1 for j in range(n)
                if ((pi / 2 + length / 2 - (j+0.5)*pi/n) % pi) <= length)
    assert abs(count / n - length / pi) < 3/n
    # Finite grid sanity for the exact CDF of the parameterwise maximum.
    for m in (1, 3, 5):
        wmin2 = minimax_sq(4, 1, length, m)
        for fraction in (0.1, 0.4, 0.9):
            z = wmin2 + fraction*(16-wmin2)
            sm, rm = 1**(2*m), 4**(2*m)
            delta = asin(sqrt(sm*(16-z) / (rm*(z-1)+sm*(16-z))))
            predicted = (pi-length-2*delta)/pi
            n = 20000
            count = 0
            for j in range(n):
                phi = pi*(j+0.5)/n
                hit = ((phi - pi/2) % pi) <= length
                worst = 16 if hit else max(sqerr(4, 1, phi, m), sqerr(4, 1, phi-length, m))
                count += worst <= z
            assert abs(count/n - predicted) < 5/n, (m, z, count/n, predicted)
    print('VERIFY_OK: exact matrix identities, sharp-angle checks, half-turn quadrature, atom geometry')


if __name__ == '__main__':
    run()
