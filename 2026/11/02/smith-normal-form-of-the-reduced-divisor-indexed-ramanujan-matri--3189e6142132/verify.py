#!/usr/bin/env python3
"""Exact small-modulus checks for reduced Ramanujan divisor matrices.

Only Python's standard library is required. The independent determinantal-divisor
checks enumerate all minors rather than relying on the module proof.
"""
from itertools import combinations
from functools import reduce
from math import gcd, isqrt, prod


def factors(n):
    out = {}
    p = 2
    while p * p <= n:
        if n % p == 0:
            a = 0
            while n % p == 0:
                n //= p
                a += 1
            out[p] = a
        p += 1
    if n > 1:
        out[n] = 1
    return out


def phi(n):
    for p in factors(n):
        n = n // p * (p - 1)
    return n


def mobius(n):
    f = factors(n)
    return 0 if any(a > 1 for a in f.values()) else (-1) ** len(f)


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def ramanujan(d, e):
    g = gcd(d, e)
    t = d // g
    return mobius(t) * phi(d) // phi(t)


def determinant(a):
    """Exact Bareiss determinant, with integer pivoting."""
    b = [row[:] for row in a]
    n = len(b)
    if not n:
        return 1
    sign = 1
    prev = 1
    for k in range(n - 1):
        if b[k][k] == 0:
            pivot = next((j for j in range(k + 1, n) if b[j][k]), None)
            if pivot is None:
                return 0
            b[k], b[pivot] = b[pivot], b[k]
            sign *= -1
        v = b[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                q, r = divmod(b[i][j] * v - b[i][k] * b[k][j], prev)
                assert r == 0
                b[i][j] = q
            b[i][k] = 0
        prev = v
    return sign * b[n-1][n-1]


def predicted(n):
    ds = divisors(n)[1:]
    size = len(ds)
    exponent = {}
    facn = factors(n)
    for ell in set(facn) | set(factors(phi(n))):
        if ell not in facn:
            v = factors(phi(n)).get(ell, 0)
            exponent[ell] = [v] if v else []
            continue
        a = facn[ell]
        m = n // ell ** a
        T = len(divisors(m))
        h = factors(phi(m)).get(ell, 0)
        exps = [j for j in range(1, a+1) for _ in range(T)]
        exps.remove(1)
        if h:
            exps[-1] += h
        exponent[ell] = sorted(exps)
    out = [1] * size
    for ell, exps in exponent.items():
        for i, e in enumerate([0]*(size-len(exps))+exps):
            out[i] *= ell**e
    assert all(out[i+1] % out[i] == 0 for i in range(size-1))
    return out


def actual_invariants_by_all_minors(a):
    size = len(a)
    prev = 1
    inv = []
    for k in range(1, size+1):
        g = 0
        for rr in combinations(range(size), k):
            for cc in combinations(range(size), k):
                minor = [[a[i][j] for j in cc] for i in rr]
                g = gcd(g, determinant(minor))
        g = abs(g)
        assert g > 0 and g % prev == 0
        inv.append(g//prev)
        prev = g
    return inv


def matrix(n):
    ds = divisors(n)[1:]
    return [[ramanujan(d,e) for e in ds] for d in ds]


def rank_mod(a, ell):
    a = [[v % ell for v in row] for row in a]
    size = len(a)
    r = 0
    for j in range(size):
        i = next((k for k in range(r, size) if a[k][j] % ell), None)
        if i is None:
            continue
        a[r], a[i] = a[i], a[r]
        inv = pow(a[r][j], -1, ell)
        a[r] = [(inv*v)%ell for v in a[r]]
        for k in range(r+1,size):
            s = a[k][j]
            if s:
                a[k] = [(v-s*w)%ell for v,w in zip(a[k], a[r])]
        r+=1
    return r


def primes_under(k):
    return [i for i in range(2,k) if len(factors(i)) == 1 and list(factors(i).values()) == [1]]


def main():
    minor_cases = 0
    det_cases = 0
    ranks = 0
    for n in range(2, 31):
        a = matrix(n)
        s = predicted(n)
        actual = actual_invariants_by_all_minors(a)
        assert actual == s, (n,actual,s)
        minor_cases += 1
    for n in range(2, 151):
        a = matrix(n)
        s = predicted(n)
        det = determinant(a)
        assert det == prod(s), (n,det,s)
        assert det* n == phi(n) * prod(divisors(n)[1:]), n
        det_cases += 1
        for ell in primes_under(23):
            actual = rank_mod(a,ell)
            expected = sum(t % ell != 0 for t in s)
            assert actual == expected, (n,ell,actual,expected)
            ranks += 1
    print(f'VERIFY_OK: {minor_cases} complete determinantal-divisor Smith checks; '
          f'{det_cases} exact determinants; {ranks} modular ranks.')

if __name__ == '__main__':
    main()
