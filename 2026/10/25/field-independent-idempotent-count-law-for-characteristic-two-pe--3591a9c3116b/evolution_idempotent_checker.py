#!/usr/bin/env python3
"""Independent finite-field tests for the characteristic-two evolution-idempotent distribution.

Run with Python 3: python evolution_idempotent_checker.py
No external packages are required. Field elements are binary polynomial residues.
"""
from collections import Counter
from functools import reduce
from itertools import product
from math import prod

IRREDUCIBLE = {1: 0b11, 2: 0b111, 3: 0b1011}

def field_mul(a, b, e):
    mod = IRREDUCIBLE[e]
    ans = 0
    while b:
        if b & 1:
            ans ^= a
        b >>= 1
        a <<= 1
        if a & (1 << e):
            a ^= mod
    return ans

def mat_rank(rows, n, q):
    # Characteristic-two Gaussian elimination, with multiplicative inverses.
    e = (q - 1).bit_length()
    a = [list(r) for r in rows]
    rank = 0
    for j in range(n):
        piv = next((i for i in range(rank, n) if a[i][j]), None)
        if piv is None:
            continue
        a[piv], a[rank] = a[rank], a[piv]
        v = a[rank][j]
        iv = next(t for t in range(1, q) if field_mul(v, t, e) == 1)
        a[rank] = [field_mul(iv, x, e) for x in a[rank]]
        for i in range(n):
            if i != rank and a[i][j]:
                b = a[i][j]
                a[i] = [a[i][h] ^ field_mul(b, a[rank][h], e) for h in range(n)]
        rank += 1
    return rank

def fixed_count(a, q):
    n = len(a)
    e = (q - 1).bit_length()
    sq = [field_mul(t,t,e) for t in range(q)]
    count = 0
    for v in product(range(q), repeat=n):
        w = tuple(sq[t] for t in v)
        if all((reduce(lambda z,p: z^field_mul(p[0],p[1],e),zip(a[i],w),0))==v[i] for i in range(n)):
            count += 1
    return count

def gl_order(n, q):
    return prod(q**n-q**i for i in range(n))

def binom_gaussian(n, k):
    if k < 0 or k > n:
        return 0
    numerator = prod(2**n - 2**i for i in range(k))
    denominator = prod(2**k - 2**i for i in range(k))
    return numerator // denominator

def predicted_counts(n):
    result = {}
    for k in range(n+1):
        s = 0
        for j in range(n-k+1):
            term = (-1)**j * (2**(j*(j-1)//2)) * binom_gaussian(n-k, j)
            term *= 2**((k+j)*(n-k-j)) * gl_order(n-k-j,2)
            s += term
        result[2**k] = binom_gaussian(n,k)*s
    assert sum(result.values()) == gl_order(n,2)
    return result

def enumerate_gl_and_idempotents(e, n):
    q=2**e
    observed = Counter()
    tested=0
    for entries in product(range(q), repeat=n*n):
        rows = [entries[i*n:(i+1)*n] for i in range(n)]
        if mat_rank(rows,n,q) < n:
            continue
        tested += 1
        observed[fixed_count(rows,q)] += 1
    assert tested == gl_order(n,q), (e,n,tested)
    canonical = predicted_counts(n)
    expected = {cnt: gl_order(n,q)*freq//gl_order(n,2) for cnt, freq in canonical.items()}
    assert all(gl_order(n,q)*freq % gl_order(n,2)==0 for freq in canonical.values())
    assert dict(observed) == {c:v for c,v in expected.items() if v},(e,n,observed,expected)
    print('PASS', 'field_order',q,'dimension',n,'matrices',tested,'idempotent_count_frequencies',dict(sorted(observed.items())))
    return tested

if __name__=='__main__':
    total=0
    for e,n in [(1,1),(2,1),(3,1),(1,2),(2,2),(3,2),(1,3),(1,4)]:
        total += enumerate_gl_and_idempotents(e,n)
    print('ALL_CHARACTERISTIC_TWO_EVOLUTION_CHECKS_PASSED',total)
