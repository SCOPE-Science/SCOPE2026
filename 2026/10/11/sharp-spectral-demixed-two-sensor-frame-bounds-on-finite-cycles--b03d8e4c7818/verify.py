#!/usr/bin/env python3
"""Reproducible finite cross-checks of the cycle spectral-frame identities.

Requires only Python's standard library.  The proof is analytic and valid for
all cycle orders; these checks test representative finite ranges independently.
"""
import cmath
import math


def euler_phi(n):
    return sum(math.gcd(j, n) == 1 for j in range(1, n + 1))


def integer_gap(N, K, s):
    # Minimum undirected circular distance of twice-frequency residues.
    return min(min((2 * k * s) % N, N - ((2 * k * s) % N))
               for k in range(1, K + 1))


def eigenvalues_2x2_gram(N, k, s):
    # Compute trace and determinant from the measurement matrix, not the formula.
    a = cmath.exp(2j * math.pi * k * s / N)
    b = cmath.exp(-2j * math.pi * k * s / N)
    # Columns: (1,a)/sqrt(N), (1,b)/sqrt(N).
    m00 = (1 + abs(a) ** 2) / N
    m11 = (1 + abs(b) ** 2) / N
    m01 = (1 + a.conjugate() * b) / N
    d = math.sqrt(max(0.0, (m00 - m11) ** 2 + 4 * abs(m01) ** 2))
    return (m00 + m11 - d) / 2, (m00 + m11 + d) / 2


def run():
    comparisons = 0
    for N in range(5, 121):
        g = math.gcd(N, 2)
        M = N // g
        for K in range(1, (N - 1) // 2 + 1):
            q = M // (K + 1)
            assert q >= 1
            values = [integer_gap(N, K, s) for s in range(1, N)]
            assert max(values) == g * q, (N, K, max(values), g*q)
            if M % (K+1) == 0:
                assert sum(v == g*q for v in values) == g*euler_phi(K+1)
            # Direct two-column Gramian tests at several nontrivial modes.
            for s in sorted({1, N-1, (N-1)//2, N//3 or 1}):
                if not (1 <= s < N):
                    continue
                for k in sorted({1, K, max(1, K//2)}):
                    low, high = eigenvalues_2x2_gram(N, k, s)
                    expected = abs(math.cos(2*math.pi*k*s/N))
                    assert abs(low - 2*(1-expected)/N) < 2e-13
                    assert abs(high - 2*(1+expected)/N) < 2e-13
                    comparisons += 2
            for s in range(1, N):
                c = max(abs(math.cos(2*math.pi*k*s/N)) for k in range(1, K+1))
                expected = math.cos(math.pi * integer_gap(N,K,s) / N)
                assert abs(c - expected) < 2e-13
    print('PASS: all N=5..120, every valid K and nonzero s;'
          ' exact optimum, equality counts, and', comparisons, 'Gram tests')


if __name__ == '__main__':
    run()
