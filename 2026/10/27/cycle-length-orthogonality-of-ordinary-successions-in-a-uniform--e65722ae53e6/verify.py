#!/usr/bin/env python3
"""Exact independent enumeration of succession/cycle-length covariances.

Usage: python verify.py
Requires only the Python standard library.
"""
from fractions import Fraction as F
from itertools import permutations
from math import factorial


def expected_covariance(n, j):
    return (F(2, n * (n - 1)) * (j == 1)
            - F(1, n * (n - 1)) * ((j == 2) + (j == n - 1))
            + F(1, n * n) * (j == n))


def expected_position(n, i, j):
    assert n >= 5 and 1 <= i < n and 1 <= j <= n
    p = int(i >= 2) + int(i <= n - 2)
    if j == 1:
        return F(p, n * (n - 1) * (n - 2))
    if j == 2:
        return F(1-p, n * (n - 1) * (n - 3))
    if 3 <= j <= n - 2:
        return F(0)
    if j == n - 1:
        return F(p - n + 2, n * (n - 1) * (n - 2) * (n - 3))
    return F(1, n * n * (n - 1))


def cycles_by_length(perm):
    n = len(perm)
    seen = [False] * n
    counts = [0] * (n + 1)
    for k in range(n):
        if not seen[k]:
            t = k
            length = 0
            while not seen[t]:
                seen[t] = True
                length += 1
                t = perm[t]
            counts[length] += 1
    return counts


def exhaust(n):
    denom = factorial(n)
    marginal = [0] * (n + 1)
    mixed = [[0] * (n + 1) for _ in range(n - 1)]
    count_succ = [0] * (n - 1)
    count = 0
    for perm in permutations(range(n)):
        count += 1
        c = cycles_by_length(perm)
        for j in range(1, n + 1):
            marginal[j] += c[j]
        for i in range(n - 1):
            if perm[i + 1] == perm[i] + 1:
                count_succ[i] += 1
                for j in range(1, n + 1):
                    mixed[i][j] += c[j]
    assert count == denom
    checks = 0
    for j in range(1, n + 1):
        total_cov = F(sum(row[j] for row in mixed), denom) - F(sum(count_succ) * marginal[j], denom * denom)
        assert total_cov == expected_covariance(n, j), (n, j, total_cov, expected_covariance(n, j))
        checks += 1
        for i in range(n - 1):
            cov = F(mixed[i][j], denom) - F(count_succ[i] * marginal[j], denom * denom)
            assert count_succ[i] * n == denom, (n, i)
            if n >= 5:
                assert cov == expected_position(n, i + 1, j), (n, i+1, j, cov, expected_position(n, i+1, j))
                checks += 1
    return count, checks


def analytic_checks():
    checks = 0
    for n in range(5, 151):
        m = n - 2
        # All expectations below are in a uniformly random n-point permutation
        # conditioned on two prescribed arrows, after contracting to m symbols.
        labels = [1, 2] + list(range(3, n - 1)) + [n-1, n]
        for j in labels:
            loop = F(1,j) if j <= m else F(0)
            if j == 1:
                loop += 2
            if j == 1:
                path = F(1) - F(1,m)
                double = F(1) - F(2,m)
            elif j == 2:
                path = F(1,2) - F(1,m)
                double = F(1,2) + F(1,m*(m-1))
            elif j <= m:
                path = F(1,j)
                double = F(1,j)
            elif j == n-1:
                path = F(1,m)
                double = F(m-2,m*(m-1))
            else:
                path = F(1,m)
                double = F(1,m)
            for i in range(1,n):
                p = (i>=2) + (i<=n-2)
                joint = (loop + p*path + (m-p)*double)/F(n*(n-1))
                covariance = joint - F(1,n*j)
                assert covariance == expected_position(n,i,j), (n,i,j,covariance,expected_position(n,i,j))
                checks += 1
        for j in range(1,n+1):
            assert sum(expected_position(n,i,j) for i in range(1,n)) == expected_covariance(n,j)
            checks += 1
    return checks


def main():
    perm_count = 0
    checks = 0
    for n in range(2,9):
        p,c = exhaust(n)
        perm_count += p
        checks += c
    algebra_checks = analytic_checks()
    print('PASS: exact exhaustive permutation enumeration for n=2,...,8.')
    print('Permutations enumerated:', perm_count)
    print('Exact marginal/positionwise covariance comparisons:', checks)
    print('Algebraic category-table and summation comparisons:', algebra_checks)
    print('Scope of finite checks: these verify instances, not the infinite proof.')


if __name__ == '__main__':
    main()
