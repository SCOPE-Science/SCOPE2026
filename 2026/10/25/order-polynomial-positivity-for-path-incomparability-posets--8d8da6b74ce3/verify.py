#!/usr/bin/env python3
"""Exact arithmetic checks for order polytopes of path-incomparability posets.
No external packages required; finite checks supplement the universal proof.
"""
from fractions import Fraction
from math import factorial, comb
from itertools import product


def mul_linear(p, c):
    q = [0] * (len(p) + 1)
    for i, v in enumerate(p):
        q[i] += c * v
        q[i + 1] += v
    return q


def matchings(n, edges):
    # Matching generating polynomial for a subgraph of the path on n vertices.
    prev2 = [1]  # zero vertices
    prev1 = [1]  # one vertex
    for j in range(2, n + 1):
        p = prev1[:]
        if j - 2 in edges:
            if len(p) < len(prev2) + 1:
                p += [0] * (len(prev2) + 1 - len(p))
            for k, v in enumerate(prev2):
                p[k + 1] += v
        prev2, prev1 = prev1, p
    return prev1


def factorial_scaled_coeffs(n, edges):
    out = [0] * (n + 1)
    for k, m in enumerate(matchings(n, edges)):
        p = [1]
        for r in range(-k, n-k):
            p = mul_linear(p, r)
        for j, val in enumerate(p):
            out[j] += m * val
    return out


def independent_count(n, edges, t):
    # Brute force all functions to [t]; no P-partition generating function used.
    ans = 0
    for v in product(range(1, t + 1), repeat=n):
        if all(v[i] <= v[j] for i in range(n) for j in range(i + 1, n)
               if j > i + 1 or i not in edges):
            ans += 1
    return ans


def main():
    cases = 0
    values = 0
    zeros = []
    for n in range(1, 11):
        for mask in range(1 << (n - 1)):
            edges = {j for j in range(n - 1) if mask >> j & 1}
            m = matchings(n, edges)
            coeff = factorial_scaled_coeffs(n, edges)
            assert coeff[0] == 0
            assert all(c >= 0 for c in coeff), (n, mask, coeff)
            assert coeff[-1] == sum(m)
            a = [m[k] * factorial(k) * factorial(n - 1 - k)
                 for k in range(len(m))]
            assert all(a[k + 1] <= a[k] for k in range(len(a) - 1))
            assert coeff[1] == sum((-1)**k*a[k] for k in range(len(a)))
            if coeff[1] == 0:
                zeros.append((n, mask))
            for t in (1, 2, 3):
                actual = sum(coeff[j] * (t ** j) for j in range(n + 1)) // factorial(n)
                if n <= 7:
                    assert actual == independent_count(n, edges, t), (n, mask, t)
                    values += 1
            cases += 1
    assert set(zeros) == {(2,1), (3,3)}
    print(f'EXACT_OK path_cases={cases} independent_counts={values} zero_linear={zeros}')


if __name__ == '__main__':
    main()
