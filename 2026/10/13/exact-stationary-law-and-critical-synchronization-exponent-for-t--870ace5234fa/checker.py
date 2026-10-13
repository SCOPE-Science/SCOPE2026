"""Exact finite-state checks for stationary coupon thinning identities.

Model: one uniform coupon draw, followed by independent post-draw losses.
The universal proof is analytical; this verifies exact finite kernels independently.
"""
from fractions import Fraction
from math import comb, factorial


def count_kernel(n, q):
    P = [[Fraction(0) for _ in range(n + 1)] for _ in range(n + 1)]
    for k in range(n + 1):
        for pre, weight in ((k, Fraction(k, n)), (k + 1, Fraction(n - k, n))):
            if not weight:
                continue
            for j in range(pre + 1):
                P[k][j] += weight * comb(pre, j) * q**j * (1 - q)**(pre-j)
        assert sum(P[k]) == 1
    return P


def stationary(P):
    size = len(P)
    A = [[Fraction(int(i == j)) - P[j][i] for j in range(size)] + [Fraction(0)] for i in range(size)]
    A[-1] = [Fraction(1)] * size + [Fraction(1)]
    for k in range(size):
        pivot = next(j for j in range(k, size) if A[j][k] != 0)
        A[k], A[pivot] = A[pivot], A[k]
        value = A[k][k]
        A[k] = [z / value for z in A[k]]
        for j in range(size):
            if j == k:
                continue
            value = A[j][k]
            if value:
                A[j] = [u - value * v for u, v in zip(A[j], A[k])]
    return [row[-1] for row in A]


def inclusion(n, q, r):
    out = Fraction(1)
    for j in range(1, r + 1):
        out *= Fraction(j, n) * q**j / (1 - (1 - Fraction(j, n)) * q**j)
    return out


def check():
    assertions = 0
    for n in range(2, 9):
        for q in (Fraction(1, 4), Fraction(1, 2), Fraction(2, 3), Fraction(4, 5)):
            pi = stationary(count_kernel(n, q))
            assert all(x > 0 for x in pi)
            assertions += 1
            for r in range(n + 1):
                empirical = sum(pi[k] * comb(k, r) for k in range(r, n + 1)) / comb(n, r)
                assert empirical == inclusion(n, q, r)
                assertions += 1
            assert pi[n] == inclusion(n, q, n)
            assertions += 1
            u = q / (q + n * (1 - q))
            v2 = inclusion(n, q, 2) - u*u
            assert v2 == -u*u*(1-q)**2/(1-q*q+Fraction(2, n)*q*q)
            assertions += 1
            assert pi[n]*(1-q**n) == pi[n-1]*q**n/n
            assertions += 1
    print('PASS exact finite stationary identities:', assertions, 'assertions')


if __name__ == '__main__':
    check()
