#!/usr/bin/env python3
"""Exact finite-n cross-checks for the Ewens long-cycle covariance law.
No external packages required. Executed with Python 3.11+.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial

def cycle_counts(perm):
    n = len(perm)
    seen = [False] * n
    counts = [0] * (n + 1)
    for i in range(n):
        if seen[i]:
            continue
        j, size = i, 0
        while not seen[j]:
            seen[j] = True
            size += 1
            j = perm[j]
        counts[size] += 1
    return counts

def rising(theta, length):
    out = Fraction(1)
    for i in range(length):
        out *= theta + i
    return out

def prediction(n, theta, m):
    normal = rising(theta,n)
    expected_K = theta * sum((Fraction(1) / (theta + i) for i in range(n)), Fraction(0))
    total = Fraction(0)
    for j in range(m + 1, n + 1):
        mu = theta * Fraction(factorial(n), j * factorial(n-j)) * rising(theta,n-j) / normal
        expectation_K_remainder = theta * sum((Fraction(1) / (theta + i) for i in range(n-j)), Fraction(0))
        total += mu * (1 + expectation_K_remainder - expected_K)
    return total

def observed(n, theta, m):
    numer_K = numer_R = numer_KR = Fraction(0)
    normal = rising(theta,n)
    for perm in permutations(range(n)):
        counts = cycle_counts(perm)
        k = sum(counts)
        r = sum(counts[m+1:])
        w = theta**k / normal
        numer_K += w*k
        numer_R += w*r
        numer_KR += w*k*r
    return numer_KR - numer_K * numer_R

def main():
    tested = 0
    for theta in (Fraction(1,2),Fraction(1),Fraction(2)):
        for n in range(2,8):
            signs = []
            for m in range(n):
                got = observed(n,theta,m)
                want = prediction(n,theta,m)
                assert got == want, (n,theta,m,got,want)
                signs.append(1 if want>0 else -1 if want<0 else 0)
                tested += 1
            assert signs[0] == 1 and signs[-1] == -1
            assert not any(signs[i] == -1 and signs[i+1] == 1 for i in range(n-1))
    print(f"PASS: {tested} exact permutation-model covariances across three Ewens parameters (n=2..7).")
if __name__ == '__main__':
    main()
