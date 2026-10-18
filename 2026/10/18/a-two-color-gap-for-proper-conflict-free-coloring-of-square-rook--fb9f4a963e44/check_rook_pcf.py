#!/usr/bin/env python3
"""Verify proper open-neighborhood conflict-free colorings of rook graphs.

No dependencies beyond the Python standard library. Finite tests are not a proof
of the statements for all parameter values.
"""
from collections import Counter
from itertools import product
from math import gcd

FOUR = (
    (0, 1, 2, 3),
    (2, 3, 5, 4),
    (5, 4, 3, 2),
    (4, 5, 1, 0),
)

def valid(matrix):
    m, n = len(matrix), len(matrix[0])
    assert m > 0 and n > 0
    for row in matrix:
        if len(set(row)) < n:
            return False
    for j in range(n):
        if len({matrix[i][j] for i in range(m)}) < m:
            return False
    for i in range(m):
        for j in range(n):
            neighbors = [matrix[i][k] for k in range(n) if k != j]
            neighbors += [matrix[k][j] for k in range(m) if k != i]
            if not any(v == 1 for v in Counter(neighbors).values()):
                return False
    return True

def construction(m, n):
    if m > n:
        return tuple(zip(*construction(n, m)))
    if m < n:
        return tuple(tuple((i+j) % n for j in range(n)) for i in range(m))
    if n == 4:
        return FOUR
    k = n + 2
    if n % 2 == 1:
        q = 2
    elif k % 4 == 0:
        q = k // 2 - 1
    else:
        q = k // 2 - 2
    if n == 2:
        return ((0, 1), (2, 3))
    assert gcd(q,k) == 1 and q % k not in (1, k-1)
    return tuple(tuple((i + q*j) % k for j in range(n)) for i in range(n))

def brute_no_small_square(n, palette):
    # Enumerate all functions (not just proper ones) as an independent check.
    for flat in product(range(palette), repeat=n*n):
        a = tuple(flat[i*n:(i+1)*n] for i in range(n))
        if valid(a):
            return False
    return True

def main():
    tested = 0
    for m in range(2, 21):
        for n in range(2, 21):
            a = construction(m,n)
            assert valid(a), (m,n,a)
            expected = max(m,n) + (2 if m==n else 0)
            assert len(set(v for row in a for v in row)) <= expected
            tested += 1
    for n in range(21, 121):
        a = construction(n,n)
        assert valid(a), n
        tested += 1
    assert brute_no_small_square(2, 3)
    assert brute_no_small_square(3, 4)
    print('VERIFICATION_OK constructed_graphs=%d square_orders=2..120 rectangular=2..20 exhaustive_nonexistence=(2,3_colors),(3,4_colors)' % tested)

if __name__ == '__main__':
    main()
