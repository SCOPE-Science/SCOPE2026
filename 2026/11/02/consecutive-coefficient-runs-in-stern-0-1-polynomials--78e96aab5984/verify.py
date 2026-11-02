#!/usr/bin/env python3
"""Exact finite checks for consecutive support blocks of Stern (0,1)-polynomials.

All coefficients and congruences are integral, with no floating-point operations.
"""
from functools import lru_cache
from collections import Counter

@lru_cache(maxsize=None)
def support(n):
    if n == 0:
        return frozenset()
    if n == 1:
        return frozenset((0,))
    if n % 2 == 0:
        return frozenset(2*j for j in support(n//2))
    return frozenset([2*j+1 for j in support(n//2)] +
                     [2*j for j in support(n//2+1)])

def lucas_support(n):
    return frozenset(k for k in range((n-1)//2+1)
                     if not (k & (n-1-2*k)))

def runs(exponents):
    if not exponents:
        return Counter()
    positions = sorted(exponents)
    result = Counter()
    streak = 1
    for a,b in zip(positions, positions[1:]):
        if b == a + 1:
            streak += 1
        else:
            result[streak] += 1
            streak = 1
    result[streak] += 1
    return result

def main():
    limit = 4096
    assert support(0) == frozenset()
    full = Counter()
    report=[]
    for n in range(1, limit+1):
        e = support(n)
        assert e == lucas_support(n), (n,e,lucas_support(n))
        z = runs(e)
        assert max(z) <= 3, (n,z)
        full.update(z)
        if n >= 4 and n & (n-1) == 0:
            r = n.bit_length()-1
            a = 3**(r-2)
            expected={1: 2*a+1, 2:(a+1)//2, 3:(a-1)//2}
            got={j:full[j] for j in (1,2,3)}
            assert got == expected, (r,got,expected)
            report.append((r,got))
    assert support(5) == frozenset((0,1,2))
    print('VERIFY_OK: {} complete polynomial supports versus independent Lucas formula'.format(limit))
    print('MAX_RUN=3; attained at index 5')
    print('DYADIC_CHECKS='+repr(report))

if __name__ == '__main__':
    main()
