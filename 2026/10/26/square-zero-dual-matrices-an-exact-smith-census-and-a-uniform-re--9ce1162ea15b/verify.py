#!/usr/bin/env python3
"""Independent finite tests of the square-zero dual-matrix Smith census.

Uses direct matrix equations and ranks of the induced 2n-by-2n map;
no normal-form decomposition of the matrix being tested is assumed.
"""
from collections import Counter
from itertools import product
from math import prod


def rank(A, p):
    a = [list(map(lambda x: x % p, row)) for row in A]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    h = 0
    for j in range(n):
        pivot = next((i for i in range(h, m) if a[i][j]), None)
        if pivot is None:
            continue
        a[h], a[pivot] = a[pivot], a[h]
        inv = pow(a[h][j], -1, p)
        a[h] = [(x * inv) % p for x in a[h]]
        for i in range(m):
            if i != h and a[i][j]:
                c = a[i][j]
                a[i] = [(u - c*v) % p for u, v in zip(a[i], a[h])]
        h += 1
        if h == m:
            break
    return h


def matmul(A, B, p):
    n = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) % p
             for j in range(n)] for i in range(n)]


def mat(a, n):
    return tuple(tuple(a[n*i:n*(i+1)]) for i in range(n))


def gauss(n, k, q):
    if k < 0 or k > n:
        return 0
    num = prod(q**(n-i)-1 for i in range(k))
    den = prod(q**(k-i)-1 for i in range(k))
    return num // den


def gl(t, q):
    return prod(q**t - q**i for i in range(t))


def formula(n, q):
    out = Counter()
    for r in range(n//2+1):
        s = n-2*r
        a = gauss(n,r,q)*gauss(n-r,r,q)*gl(r,q)
        for t in range(s+1):
            matrices = gauss(s,t,q)**2 * gl(t,q)
            out[(r,t)] = a * q**(n*n-2*r*(n-r)-s*s) * matrices
    return out


def brute(n, p):
    candidates = [mat(a,n) for a in product(range(p), repeat=n*n)]
    zeros = tuple(tuple(0 for _ in range(n)) for _ in range(n))
    ans=Counter()
    for A in candidates:
        if matmul(A,A,p) != [list(row) for row in zeros]:
            continue
        r = rank(A,p)
        for B in candidates:
            AB=matmul(A,B,p)
            BA=matmul(B,A,p)
            if any((AB[i][j]+BA[i][j])%p for i in range(n) for j in range(n)):
                continue
            # F_p-linearization of A+epsilon B on R^n.
            L = [[A[i][j] for j in range(n)] + [0]*n
                 for i in range(n)] + [list(B[i])+list(A[i]) for i in range(n)]
            epsilon_rank = rank(L,p)-2*r
            assert 0 <= epsilon_rank <= n-2*r
            ans[(r, epsilon_rank)]+=1
    return ans


def main():
    for q,n in [(2,1),(2,2),(2,3),(3,1),(3,2),(5,1),(5,2)]:
        predicted=formula(n,q)
        actual=brute(n,q)
        assert actual==predicted, (q,n,actual,predicted)
        print(f'q={q} n={n} checked_all={q**(2*n*n)} square_zero={sum(actual.values())} strata={dict(sorted(actual.items()))}')
    for q in (2,3,4,5,7,8):
        for n in range(1,35):
            f=formula(n,q)
            # Each rank-stratum's Smith rank distribution sums to its linear-lift count.
            for r in range(n//2+1):
                s=n-2*r
                a=gauss(n,r,q)*gauss(n-r,r,q)*gl(r,q)
                d=n*n-2*r*(n-r)
                assert sum(f[(r,t)] for t in range(s+1))==a*q**d
        print(f'q={q} exact_stratum_sums_check_n=1..34 OK')
    print('CHECK_OK')

if __name__=='__main__':
    main()
