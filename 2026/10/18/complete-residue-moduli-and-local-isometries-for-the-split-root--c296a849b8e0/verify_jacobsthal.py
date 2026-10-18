#!/usr/bin/env python3
"""Exact modular checks for the stated generalized Jacobsthal theorem.
Finite checks corroborate, but do not replace, the infinite proof.
"""
from math import gcd

def prime_factors(n):
    out = set()
    d = 2
    while d*d <= n:
        if n % d == 0:
            out.add(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.add(n)
    return out

def predicted(a, m):
    return m in (1,2) or (m == 3 and a % 3 == 0) or (
        m % 2 and all((a+1) % p == 0 for p in prime_factors(m)))

def image(a,m):
    # Exact eventual cycle of state (J_n,J_{n+1}) modulo m.
    s = (0,1 % m)
    seen = set()
    values = set()
    while s not in seen:
        seen.add(s)
        values.add(s[0])
        s=(s[1],((a-1)*s[1]+a*s[0])%m)
    return values

cnt=0
for a in range(2,52,2):
    for m in range(1,121):
        assert (len(image(a,m)) == m) == predicted(a,m), (a,m)
        cnt += 1

cnt_bij=0
for a in range(2,52,2):
    for m in range(3,121,2):
        if not all((a+1)%p == 0 for p in prime_factors(m)):
            continue
        # Exact modular recurrence produces the first 2m values.
        vals=[0,1]
        for n in range(2,2*m):
            vals.append(((a-1)*vals[-1]+a*vals[-2])%m)
        assert sorted(vals[::2]) == list(range(m)), (a,m,'even')
        assert sorted(vals[1::2]) == list(range(m)), (a,m,'odd')
        for i in range(m):
            for j in range(i):
                assert gcd(vals[2*i]-vals[2*j],m)==gcd(i-j,m)
                assert gcd(vals[2*i+1]-vals[2*j+1],m)==gcd(i-j,m)
        cnt_bij+=1
print('VERIFY_OK',cnt,'full-state modular profiles;',cnt_bij,'complete-modulus double-permutation/isometry tests')
