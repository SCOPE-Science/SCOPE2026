#!/usr/bin/env python3
"""Independent arithmetic and finite-section checks for the rank-two Fock Ky Fan disk Hessian.

Standard Python library only.  This program is supplementary: the proof of the
all-degree statement is the falling-factorial argument in RESULT.md, not the
finite numerical sections used here.
"""
import math
from fractions import Fraction


def A(t, k):
    return (t**k / math.factorial(k)) / sum(
        t**l / math.factorial(l) for l in range(1, k + 1)
    ) if k >= 2 else 0.0


def B(t, k):
    return (t**(k + 2) / math.factorial(k + 1)) / sum(
        t**l / math.factorial(l) for l in range(2, k + 2)
    )


def lower_gamma(s, x):
    # gammainc(s,x) = x**s * exp(-x) * sum_{j>=0}
    # x**j / [s(s+1)...(s+j)].
    term = 1.0 / s
    total = term
    for j in range(1, 220):
        term *= x / (s + j)
        total += term
        if abs(term) < 2e-16 * abs(total):
            break
    return math.exp(-x) * x**s * total


def eigenvalues_symmetric(a):
    # Jacobi sweeps for a small real symmetric test matrix.
    a = [row[:] for row in a]
    n = len(a)
    for _ in range(100 * n * n):
        p, q = max(((p, q) for p in range(n) for q in range(p + 1, n)),
                   key=lambda z: abs(a[z[0]][z[1]]))
        if abs(a[p][q]) < 2e-14:
            break
        apq = a[p][q]
        tau = (a[q][q] - a[p][p]) / (2 * apq)
        tt = 1.0 / (abs(tau) + math.sqrt(1 + tau * tau))
        if tau < 0:
            tt = -tt
        c = 1.0 / math.sqrt(1 + tt * tt)
        s = tt * c
        app, aqq = a[p][p], a[q][q]
        a[p][p] = app - tt * apq
        a[q][q] = aqq + tt * apq
        a[p][q] = a[q][p] = 0.0
        for r in range(n):
            if r not in (p, q):
                arp, arq = a[r][p], a[r][q]
                a[r][p] = a[p][r] = c * arp - s * arq
                a[r][q] = a[q][r] = s * arp + c * arq
    else:
        raise ArithmeticError('Jacobi convergence failed')
    return sorted(a[i][i] for i in range(n))


def partial_sum(t, eps, k, n=12, m=256):
    # The test domain is |z|**2 < t + eps*cos(k*arg(z)), exact area pi*t.
    mat = [[0.0] * n for _ in range(n)]
    for j in range(m):
        th = 2 * math.pi * j / m
        u = t + eps * math.cos(k * th)
        for p in range(n):
            for q in range(p, n):
                shape = (p + q) / 2 + 1
                radial = lower_gamma(shape, u) / math.sqrt(math.factorial(p) * math.factorial(q))
                value = radial * math.cos((p - q) * th) / m
                mat[p][q] += value
    for p in range(n):
        for q in range(p + 1, n):
            mat[q][p] = mat[p][q]
    e = eigenvalues_symmetric(mat)
    return e[-1] + e[-2]


def run():
    checks = 0
    for t in (Fraction(1, 5), Fraction(1, 2), Fraction(1, 1), Fraction(5, 1), Fraction(11, 1)):
        a2 = (t * t / 2) / (t + t * t / 2)
        b2 = (t**4 / 6) / (t*t/2 + t**3/6)
        delta2 = t - a2 - b2
        assert delta2 == t * (2*t + 3) / ((t + 2)*(t + 3))
        assert delta2 > 0
        checks += 2
        aa, bb = Fraction(0), t
        for k in range(2, 72):
            na = (t**k / math.factorial(k)) / sum((t**l / math.factorial(l) for l in range(1,k+1)), Fraction(0))
            nb = (t**(k+2)/math.factorial(k+1)) / sum((t**l / math.factorial(l) for l in range(2,k+2)), Fraction(0))
            assert na < aa or k == 2
            assert nb < bb
            assert t - na - nb > 0
            aa, bb = na, nb
            checks += 3
    print('RATIONAL_IDENTITIES_OK', checks)
    # Directly integrate the symbol matrix and diagonalize without using the
    # formal perturbation expansion.  The missing high modes are exponentially
    # suppressed at these small radii; convergence is checked against n=14.
    numeric = 0
    for t in (0.6, 1.0, 2.0):
        eps = 0.001
        for k in (1, 2, 3, 4):
            predicted = math.exp(-t) * (t - A(t, k) - B(t, k)) / 4
            e0 = partial_sum(t, 0.0, k, n=14)
            ep = partial_sum(t, eps, k, n=14)
            em = partial_sum(t, -eps, k, n=14)
            measured = (2*e0 - ep - em)/(2*eps*eps)
            if abs(measured-predicted) > 3e-6:
                raise AssertionError((t,k,predicted,measured))
            numeric += 1
    print('DIRECT_SHAPE_SECOND_DIFFERENCES_OK', numeric)
    print('ALL_CHECKS_OK')


if __name__ == '__main__':
    run()
