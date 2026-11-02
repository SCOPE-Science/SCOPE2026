#!/usr/bin/env python3
"""Exact rational spot-checks for graph heat-flow Lipschitz amplification.

For integer k >= 1, sampling t = k log(2) makes all heat spectral
multipliers rational. The small graph optimizations below enumerate the
integer vertices of a network-constraint Lipschitz polytope; the general
identity is established by the separate analytic proof.
"""
from fractions import Fraction as F
from itertools import product
from math import exp, log


def mm(A, B):
    n = len(A)
    return [[sum(A[i][r] * B[r][j] for r in range(n))
             for j in range(n)] for i in range(n)]


def diag_identity(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def rational_heat(p, q, k):
    n = p + q
    L = [[F(0) for j in range(n)] for i in range(n)]
    for a in range(p):
        for b in range(p, n):
            L[a][a] += 1
            L[b][b] += 1
            L[a][b] -= 1
            L[b][a] -= 1
    spectrum = sorted(set([0, p, q, p + q]))
    H = [[F(0) for j in range(n)] for i in range(n)]
    for eig in spectrum:
        P = diag_identity(n)
        for other in spectrum:
            if other == eig:
                continue
            T = [[L[i][j] - F(other) * (i == j)
                  for j in range(n)] for i in range(n)]
            P = mm(P, T)
            div = F(eig - other)
            P = [[z / div for z in row] for row in P]
        coef = F(1, 2 ** (eig * k))
        H = [[H[i][j] + coef * P[i][j] for j in range(n)]
             for i in range(n)]
    assert all(sum(row) == 1 for row in H)
    assert all(z > 0 for row in H for z in row)
    return H


def exact_vertex_optimum(coeff, p, q):
    # Fix the first B-vertex to 0; every admissible potential has
    # A-values in [-1,1] and remaining B-values in [-2,2].
    # The inequalities are network-incidence constraints with integral
    # right sides, hence the bounded polytope has integer vertices.
    best = None
    for avals in product((-1, 0, 1), repeat=p):
        low = max(avals) - 1
        high = min(avals) + 1
        for b_rest in product(range(low, high + 1), repeat=q - 1):
            f = list(avals) + [0] + list(b_rest)
            value = sum(c * x for c, x in zip(coeff, f))
            best = value if best is None or value > best else best
    return best


def check():
    cases = 0
    for p in range(1, 6):
        for q in range(1, 6):
            for k in (1, 2):
                H = rational_heat(p, q, k)
                coeff = [H[0][j] - H[p][j] for j in range(p + q)]
                got = exact_vertex_optimum(coeff, p, q)
                x = F(1, 2 ** (q * k))
                y = F(1, 2 ** (p * k))
                z = x * y
                u = F(p - 1, p) * (x - z)
                v = F(q - 1, q) * (y - z)
                target = z + 2 * max(u, v)
                assert got == target, (p, q, k, got, target)
                cases += 1
    # A separate independent numerical matrix/LP check can be run with
    # scipy, but is not necessary for the rational certificate above.
    for m in range(1, 6):
        for n in range(m, 13):
            A = 2 * (n - 1) / n
            B = (n - 2) / n
            fun = lambda t: A * exp(-m*t) - B * exp(-(m+n)*t)
            assert abs(fun(0) - 1) < 1e-13
            if n <= m + 2:
                assert all(fun(j / 20) <= 1 + 1e-12 for j in range(1, 30))
            else:
                peak_t = log((n-2)*(m+n)/(2*m*(n-1))) / n
                assert peak_t > 0 and fun(peak_t) > 1
                assert fun(peak_t) > fun(peak_t + .01)
                assert fun(peak_t) > fun(max(0, peak_t - .01))
    print('CHECK_OK exact_integer_potentials_and_spectral_matrices=', cases)


if __name__ == '__main__':
    check()
