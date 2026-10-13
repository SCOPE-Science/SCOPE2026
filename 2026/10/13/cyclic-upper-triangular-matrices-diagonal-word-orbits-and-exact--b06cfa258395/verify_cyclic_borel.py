#!/usr/bin/env python3
"""Independent exhaustive checks of finite-field upper-triangular cyclic-matrix counts.

Cyclicity is independently tested by linear independence of I,A,...,A^(n-1).
No orbit-stabilizer assumption is used by the enumerator.
"""
from itertools import product
from collections import Counter
from math import comb, factorial


def field_tables(q):
    if q == 4:
        add = [[i ^ j for j in range(q)] for i in range(q)]
        mul = [[0] * q for _ in range(q)]
        for x in range(q):
            for y in range(q):
                z = 0
                for i in range(2):
                    for j in range(2):
                        if (x >> i) & (y >> j) & 1:
                            z ^= 1 << (i + j)
                if z & 8:
                    z ^= 0b1100
                if z & 4:
                    z ^= 0b111
                mul[x][y] = z
    else:
        add = [[(i+j)%q for j in range(q)] for i in range(q)]
        mul = [[(i*j)%q for j in range(q)] for i in range(q)]
    inv = [0] * q
    for x in range(1,q):
        inv[x] = next(y for y in range(1,q) if mul[x][y] == 1)
    return add, mul, inv


def matrix_product(A, B, add, mul):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            t = 0
            for k in range(n):
                t = add[t][mul[A[i][k]][B[k][j]]]
            C[i][j] = t
    return C


def full_rank_rows(rows, add, mul, inv):
    rows = [r[:] for r in rows]
    h, width, pivots = len(rows), len(rows[0]), 0
    for c in range(width):
        pivot = next((i for i in range(pivots, h) if rows[i][c]), None)
        if pivot is None:
            continue
        rows[pivots], rows[pivot] = rows[pivot], rows[pivots]
        invp = inv[rows[pivots][c]]
        for j in range(c,width):
            rows[pivots][j] = mul[invp][rows[pivots][j]]
        for i in range(pivots+1,h):
            z = rows[i][c]
            if z:
                for j in range(c,width):
                    rows[i][j] = add[rows[i][j]][(-mul[z][rows[pivots][j]]) % len(add)] if len(add) != 4 else add[rows[i][j]][mul[z][rows[pivots][j]]]
        pivots += 1
        if pivots == h:
            break
    return pivots == h


def cyclic(A, add, mul, inv):
    n = len(A)
    cur = [[int(i == j) for j in range(n)] for i in range(n)]
    powers = []
    for i in range(n):
        powers.append([x for row in cur for x in row])
        cur = matrix_product(cur, A, add, mul)
    return full_rank_rows(powers, add, mul, inv)


def check(q, n):
    add, mul, inv = field_tables(q)
    pairs = [(i,j) for i in range(n) for j in range(i+1,n)]
    obs = Counter()
    for entries in product(range(q), repeat=n+len(pairs)):
        diag = entries[:n]
        A = [[0]*n for _ in range(n)]
        for i in range(n):
            A[i][i] = diag[i]
        for (i,j),x in zip(pairs,entries[n:]):
            A[i][j] = x
        if cyclic(A, add, mul, inv):
            obs[diag] += 1
    N = n*(n-1)//2
    for diag in product(range(q), repeat=n):
        k = len(set(diag))
        expected = (q-1)**(n-k)*q**(N-n+k)
        assert obs[diag] == expected, (q,n,diag,obs[diag],expected)
    print('EXHAUSTIVE_OK',q,n, 'cyclic',sum(obs.values()), 'total',q**(n+N), 'diagonals',q**n)


def stirling(n,k):
    if n == k == 0:return 1
    if n == 0 or k == 0:return 0
    a = [[0]*(k+1) for _ in range(n+1)]
    a[0][0] = 1
    for i in range(1,n+1):
        for j in range(1,min(i,k)+1):
            a[i][j] = a[i-1][j-1] + j*a[i-1][j]
    return a[n][k]


def formula(q,n):
    N=n*(n-1)//2
    return sum((factorial(q)//factorial(q-k))*stirling(n,k)*(q-1)**(n-k)*q**(N-n+k) for k in range(1,min(n,q)+1))


def power_sum(q,n):
    # Equivalent integer representation of the cyclic probability:
    # p = [sum (-1)^(q-j) C(q,j) q^j j^n] * (q-1)^(n-q) / q^(2n)
    # Evaluate at rational precision via fractions.
    from fractions import Fraction
    sig = sum((-1)**(q-j)*comb(q,j)*q**j*j**n for j in range(q+1))
    return Fraction(sig*(q-1)**n, q**(2*n)*(q-1)**q)


def tests():
    for q,n in [(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(4,2),(4,3),(5,2),(5,3)]:
        check(q,n)
        assert power_sum(q,n) == __import__('fractions').Fraction(formula(q,n),q**(n*(n+1)//2))
    for q in (2,3,4,5,7,8,9,11):
        for n in range(1,31):
            assert power_sum(q,n) == __import__('fractions').Fraction(formula(q,n),q**(n*(n+1)//2))
    print('VERIFY_OK_CYCLIC_BOREL')

if __name__ == '__main__':
    tests()
