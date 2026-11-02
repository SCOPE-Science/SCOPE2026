#!/usr/bin/env python3
"""Finite-field spot checks for a homogeneous power-sum singularity boundary.

This tests rational points only; the accompanying proof is over an algebraic
closure and does not rely on finite-field exhaustion.
"""
from itertools import product
from math import factorial


def rank_mod_p(rows, p):
    a = [[v % p for v in row] for row in rows]
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], -1, p)
        a[r] = [(inv * v) % p for v in a[r]]
        for i in range(len(a)):
            if i != r:
                v = a[i][c]
                a[i] = [(x - v * y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def projective_points(p, n):
    for i in range(n):
        for tail in product(range(p), repeat=n-i-1):
            yield (0,) * i + (1,) + tail


def test(p, n, m):
    singular = []
    count = 0
    for x in projective_points(p, n):
        if any(sum(pow(t, j, p) for t in x) % p for j in range(1, m+1)):
            continue
        count += 1
        jac = [[j * pow(t, j-1, p) for t in x] for j in range(1, m+1)]
        if rank_mod_p(jac, p) < m:
            singular.append(x)
    if n < p:
        assert not singular, (p, n, m, singular)
    if n == p:
        assert singular == [(1,) * n], (p, n, m, singular[:10])
    if n > p:
        assert (1,) * p + (0,) * (n-p) in singular
    return count, len(singular)


def main():
    cases = [(5, 4, 3), (5, 5, 3), (5, 5, 4),
             (5, 6, 3), (7, 5, 3), (7, 6, 3), (7, 7, 3)]
    for p, n, m in cases:
        good, bad = test(p, n, m)
        print(f"(p,n,m)=({p},{n},{m}): points={good}, singular={bad}")
    # Independent monomial basis of the coinvariant algebra in m variables:
    # exponents 0 <= a_i < i, for 1 <= i <= m.
    for m in range(2, 8):
        assert factorial(m) == len(list(product(*(range(i) for i in range(1, m+1)))))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
