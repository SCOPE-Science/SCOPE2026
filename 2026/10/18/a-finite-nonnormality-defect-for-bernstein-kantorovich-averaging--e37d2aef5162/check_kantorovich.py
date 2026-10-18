#!/usr/bin/env python3
"""Finite exact-rational checks and numerical asymptotic checks for the classical
Bernstein-Kantorovich integral operator. Only the Python standard library is used.
Numerics corroborate, but do not prove, the asymptotic theorem.
"""
from fractions import Fraction
from math import comb, exp, lgamma, log, sqrt, pi


def eigenvalues(n):
    N = n + 1
    v = [Fraction(1)]
    for k in range(1, N):
        v.append(v[-1] * Fraction(N - k, N))
    return v


def hs2_by_integrals(n):
    N = n + 1
    return Fraction(N, 2*n+1) * sum(
        (Fraction(comb(n,k)**2, comb(2*n,2*k)) for k in range(N)),
        Fraction(0)
    )


def hs2_closed(n):
    return Fraction(n+1, 2*n+1) * Fraction(4**n, comb(2*n,n))


def bin_average_matrix(n):
    """Matrix BA: bin integration followed by the Bernstein coefficient map.
    Its nonzero spectrum equals that of the L2 integral operator AB.
    """
    N = n + 1
    M = []
    for row in range(N):
        a = []
        for k in range(N):
            val = Fraction(0)
            for power in range(n-k+1):
                degree = k + power + 1
                term = Fraction(
                    comb(n,k)*comb(n-k,power)*
                    ((row+1)**degree - row**degree),
                    degree * N**(degree-1))
                val += term if power % 2 == 0 else -term
            a.append(val)
        M.append(a)
    return M


def matmul(A, B):
    n = len(A)
    return [[sum((A[i][k]*B[k][j] for k in range(n)), Fraction(0))
             for j in range(n)] for i in range(n)]


checks = 0
for n in range(1, 31):
    hs = hs2_by_integrals(n)
    assert hs == hs2_closed(n)
    ev = eigenvalues(n)
    assert hs > sum((v*v for v in ev), Fraction(0))
    checks += 2
    if n <= 6:
        M = bin_average_matrix(n)
        assert all(sum(row) == 1 for row in M)
        assert all(sum(M[i][k] for i in range(n+1)) == 1 for k in range(n+1))
        P = [r[:] for r in M]
        for p in range(1, min(5,n+1)):
            assert sum(P[i][i] for i in range(n+1)) == sum(v**p for v in ev)
            P = matmul(P, M)
            checks += 1
        checks += 2

for n in (100, 300, 1000, 3000, 10000):
    N = n+1
    hs = N/(2*n+1)*exp(n*log(4) + 2*lgamma(n+1) - lgamma(2*n+1))
    l = 1.0
    moment = 1.0
    for k in range(1, N):
        l *= (N-k)/N
        moment += l*l
    defect = hs - moment
    approximation = 1/6 - 5*sqrt(pi)/(96*sqrt(N))
    assert abs(defect-approximation) < .20/N, (n,defect,approximation)
    checks += 1

print('PASS:', checks, 'exact structural or asymptotic consistency checks')
