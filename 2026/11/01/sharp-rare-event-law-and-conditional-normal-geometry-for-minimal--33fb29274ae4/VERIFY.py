#!/usr/bin/env python3
"""Reproducible tests for rare minimal-vertex central cube sections.
Uses only Python's standard library. Numerical tests corroborate, not prove,
the all-dimensional asymptotic statements.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial, gamma, pi, exp, sqrt
from random import Random


def exact_qpower(m, k):
    # Dirichlet(1,...,1): E[(sum Q_i^2)^k].
    poly = [F(0)] * (k + 1)
    poly[0] = F(1)
    coeff = [F(factorial(2 * j), factorial(j)) for j in range(k + 1)]
    for _ in range(m):
        nxt = [F(0)] * (k + 1)
        for i in range(k + 1):
            for j in range(k + 1 - i):
                nxt[i + j] += poly[i] * coeff[j]
        poly = nxt
    rising = 1
    for j in range(2*k):
        rising *= m+j
    return poly[k] * factorial(k) / rising


def exact_tmoment(m, k):
    # S^2 = chi-square(m+1) * Uniform^(2/m); T = S^2 sum(Q_i^2)/2.
    factor = F(m, m + 2*k)
    for j in range(k):
        factor *= F(m + 1 + 2*j, 2)
    return factor * exact_qpower(m, k)


def verify_moments():
    for m in range(2, 45):
        expected = {
            1: F(m, m+2),
            2: F(m*(m+5), (m+2)*(m+4)),
            3: F(m*(m*m+15*m+74), (m+2)*(m+4)*(m+6)),
            4: F(m*(m**3+30*m*m+371*m+2118), (m+2)*(m+4)*(m+6)*(m+8))
        }
        for k, value in expected.items():
            assert exact_tmoment(m, k) == value, (m, k)
        raw = [F(1)] + [expected[k] for k in range(1, 5)]
        central = [sum(F(factorial(k), factorial(j)*factorial(k-j)) * (-1)**(k-j) * raw[j]
                       for j in range(k+1)) for k in range(1, 5)]
        center_expected = [
            F(-2, m+2),
            F(3*m+8, (m+2)*(m+4)),
            F(12*(m-4), (m+2)*(m+4)*(m+6)),
            F(3*(9*m*m+274*m+128), (m+2)*(m+4)*(m+6)*(m+8))]
        assert central == center_expected


def vertex_count(normal):
    d = len(normal)
    count = 0
    for s in product((-1, 1), repeat=d):
        v = sum(a*x for a,x in zip(normal, s))
        for j in range(d):
            if s[j] != -1:
                continue
            w = v + 2 * normal[j]
            if v*w < 0:
                count += 1
    return count


def verify_combinatorics():
    rng = Random(20261031)
    for d in range(3, 8):
        for _ in range(350):
            normal = [rng.gauss(0, 1) for _ in range(d)]
            dominance = max(map(abs, normal)) > sum(map(abs, normal)) - max(map(abs, normal))
            count = vertex_count(normal)
            assert count >= 2**(d-1)
            assert (count == 2**(d-1)) == dominance, (d, normal, count)


def base_weight_sample(rng, m):
    qs = [rng.expovariate(1) for _ in range(m)]
    total = sum(qs)
    q2 = sum((x/total)**2 for x in qs)
    # chi-square(m+1) = gamma((m+1)/2, 2)
    z2 = rng.gammavariate((m + 1)/2, 2)
    uniform = rng.random()
    s2 = z2 * uniform**(2/m)
    t = s2*q2/2
    return exp(-t), m*qs[0]/total, m*q2


def verify_probability_and_profile():
    rng = Random(5122026)
    for d, n in [(4, 60000), (5, 36000), (20, 18000), (100, 9000)]:
        m = d-1
        ws, wx, wq2 = 0., 0., 0.
        for _ in range(n):
            w, x, q2 = base_weight_sample(rng, m)
            ws += w
            wx += w*x
            wq2 += w*q2
        mean = ws/n
        if d == 4:
            B = d * (2**m) * gamma(d/2) / (pi**(d/2)*gamma(d))
            assert abs(B*mean-F(1,3)) < 0.012
        if d == 100:
            estimate = exp(-1)*(1+3.5/m)
            assert abs(mean-estimate) < 0.013, (mean, estimate)
            assert abs(wx/ws-1) < 0.10, wx/ws
            assert abs(wq2/ws-2) < 0.20, wq2/ws


if __name__ == '__main__':
    verify_moments()
    verify_combinatorics()
    verify_probability_and_profile()
    print('ALL_RARE_MINIMAL_CUBE_SECTION_CHECKS_PASSED')
