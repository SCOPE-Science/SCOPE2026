#!/usr/bin/env python3
"""Exact exhaustive certificate for four- and five-draw occupancy mixtures.

No stochastic sampling, floating point, or external packages are used.
Every homogeneous degree-n monomial in the ordered probability gaps is checked.
"""
from fractions import Fraction
from math import comb, factorial
from itertools import product


def weak_compositions(total, parts):
    if parts == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for tail in weak_compositions(total - first, parts - 1):
                yield (first,) + tail


def stirling(n):
    a = [[0] * (n + 1) for _ in range(n + 1)]
    a[0][0] = 1
    for t in range(1, n + 1):
        for j in range(1, t + 1):
            a[t][j] = a[t - 1][j - 1] + j * a[t - 1][j]
    return a[n]


def uniform_matrix(n):
    S = stirling(n)
    return [[Fraction(S[k] * factorial(j) // factorial(j-k), j**n) if j >= k else Fraction(0)
             for j in range(1, n + 1)] for k in range(1, n + 1)]


def inverse(M):
    n = len(M)
    A = [[*M[i], *(Fraction(int(i == j)) for j in range(n))] for i in range(n)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if A[i][k])
        A[k], A[pivot] = A[pivot], A[k]
        c = A[k][k]
        A[k] = [x / c for x in A[k]]
        for i in range(n):
            if i == k:
                continue
            c = A[i][k]
            A[i] = [A[i][j] - c * A[k][j] for j in range(2*n)]
    return [row[n:] for row in A]


def q_coefficient(n, k, alpha):
    """Coefficient of ordered-gap monomial alpha in Pr(K_n=k).

    Inclusion-exclusion over nonempty subsets T of the n possible labels:
    sum_T (-1)^(k-|T|) C(n-|T|, k-|T|) (sum_{i in T}p_i)^n.
    With p_i=sum_{r>=i} gap_r, sum_{i in T} p_i
    =sum_r |T intersection {1,...,r}| gap_r.
    """
    total = 0
    for mask in range(1, 1 << n):
        s = mask.bit_count()
        if s > k:
            continue
        weight = (-1)**(k-s) * comb(n-s, k-s)
        mon = 1
        for r, exponent in enumerate(alpha, start=1):
            if exponent:
                mon *= (mask & ((1 << r)-1)).bit_count() ** exponent
        total += weight * mon
    denominator = 1
    for power in alpha:
        denominator *= factorial(power)
    return Fraction(factorial(n) * total, denominator)


def exact_occupancy(probs, n):
    """Independent reference by enumerating labeled n-tuples."""
    q = [Fraction(0)] * n
    for choices in product(range(len(probs)), repeat=n):
        pr = Fraction(1)
        for i in choices:
            pr *= probs[i]
        q[len(set(choices))-1] += pr
    return q


def matvec(M, v):
    return [sum((a*b for a, b in zip(row, v)), Fraction(0)) for row in M]


def check(n):
    M = uniform_matrix(n)
    inv = inverse(M)
    assert all(sum(M[i][k] * inv[k][j] for k in range(n)) == int(i == j)
               for i in range(n) for j in range(n))
    counts = [0] * n
    zero_counts = [0] * n
    minima = [None] * n
    degree_count = 0
    for alpha in weak_compositions(n, n):
        degree_count += 1
        c = [q_coefficient(n, k, alpha) for k in range(1,n+1)]
        for j in range(n):
            value = sum((inv[j][k] * c[k] for k in range(n)), Fraction(0))
            assert value >= 0, (n, j+1, alpha, value)
            if value == 0:
                zero_counts[j] += 1
            else:
                counts[j] += 1
                minima[j] = value if minima[j] is None else min(minima[j],value)
    assert degree_count == comb(2*n-1, n)
    for j in range(n):
        assert counts[j] + zero_counts[j] == degree_count
    # Independently enumerate labeled sample paths and verify that the
    # computed weights reconstruct the full distinct-count distribution.
    for t in range(1, n+3):
        raw = [Fraction((i+1)**t,1) for i in range(n)]
        probs = [v/sum(raw) for v in raw]
        q = exact_occupancy(probs,n)
        w = matvec(inv,q)
        assert all(v >= 0 for v in w)
        assert sum(w) == 1
        assert matvec(M,w) == q
    print(f'PASS n={n} monomials={degree_count} nonzero_coefficients={counts} '
          f'zero_coefficients={zero_counts} minimum_positive_coefficients={list(map(str,minima))} '
          f'pathwise_profiles={n+2}')

if __name__ == '__main__':
    check(4)
    check(5)
