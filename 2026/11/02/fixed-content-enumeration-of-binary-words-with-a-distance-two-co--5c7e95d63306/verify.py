#!/usr/bin/env python3
"""Exact fixed-content near-commuting necklace enumerator and checks.

Input: n >= 2.  Output: counts of indexed binary words by Hamming weight.
Only Python's standard library is required.
"""
from collections import defaultdict
from math import comb, gcd
import sys


def mobius(d):
    if d == 1:
        return 1
    sign = 1
    p = 2
    while p * p <= d:
        if d % p == 0:
            d //= p
            sign = -sign
            if d % p == 0:
                return 0
            while d % p == 0:
                d //= p
        p += 1
    return -sign if d > 1 else sign


def proper_divisors(n):
    return (d for d in range(1, n) if n % d == 0)


def polynomial_nonprimitive(i):
    """Coefficients of sum over nonprimitive binary i-words x^weight."""
    c = [0] * (i + 1)
    for d in range(2, i + 1):
        if i % d:
            continue
        mu = mobius(d)
        if mu == 0:
            continue
        for k in range(i // d + 1):
            c[d*k] -= mu * comb(i//d, k)
    return c


def first_shift_terms(n, i):
    """Exact weight coefficients for words whose earliest successful shift is i."""
    assert 1 <= i <= n//2
    g=gcd(n,i)
    L=n//g
    out=[0]*(n+1)
    for b in range(g):
        for a in range(1,L):
            out[b*L+a]+=n*comb(g-1,b)
    if n%i:
        for b in range(g):
            out[b*L+1]-=n*comb(g-1,b)
            out[b*L+L-1]-=n*comb(g-1,b)
    else:
        for r, number in enumerate(polynomial_nonprimitive(i)):
            if r:
                out[r*L-1]-=L*r*number
            if r<i:
                out[r*L+1]-=L*(i-r)*number
    return out


def direct_first_shift(n):
    """Independent enumeration of the earliest successful nonredundant shift."""
    out=[[0]*(n+1) for _ in range(n//2)]
    mask=(1<<n)-1
    for w in range(1<<n):
        for i in range(1,n//2+1):
            rot=((w<<i)&mask)|(w>>(n-i))
            if (w^rot).bit_count()==2:
                out[i-1][w.bit_count()]+=1
                break
    return out


def enumerator(n):
    """Exact coefficients for all binary n-words with a distance-two rotation."""
    if n < 2:
        raise ValueError('n must be at least 2')
    out = [0] * (n + 1)
    for i in range(1, n//2+1):
        g = gcd(n, i)
        L = n//g
        # All words at distance 2 from the i-th rotation.
        for b in range(g):
            multiplicity = n*comb(g-1, b)
            for a in range(1, L):
                out[b*L+a] += multiplicity
        # Remove words already attained at a strictly smaller shift.
        if n % i:
            for b in range(g):
                multiplicity = n*comb(g-1, b)
                out[b*L+1] -= multiplicity
                out[b*L+L-1] -= multiplicity
        else:
            c = polynomial_nonprimitive(i)
            for r, number in enumerate(c):
                if number == 0:
                    continue
                if r:
                    out[r*L-1] -= L*r*number
                if r < i:
                    out[r*L+1] -= L*(i-r)*number
    return out


def direct(n):
    """Independent bitwise enumeration; no periodicity or divisor calculations."""
    out = [0] * (n+1)
    mask = (1 << n)-1
    for w in range(1 << n):
        for shift in range(1, n):
            rotated = ((w << shift) & mask) | (w >> (n-shift))
            if (w ^ rotated).bit_count() == 2:
                out[w.bit_count()] += 1
                break
    return out


def verify():
    reference = [0, 2, 6, 12, 30, 54, 98, 160, 234, 400, 462, 864,
                 806, 1722, 1530, 3328, 1938, 7290, 2774, 13360,
                 6090, 26422, 5106, 60096, 7900, 113256, 21600,
                 240240, 10614, 535980, 13082, 1065984, 82962,
                 2244340, 34650, 4894560, 22718, 9984462, 345930,
                 21050240, 31242, 44773848, 36206]
    # Indexed totals A179674, n=1,...,43; read-only published numerical anchor.
    for n in range(2, 44):
        p = enumerator(n)
        assert len(p) == n+1 and p[0] == p[n] == 0
        assert p == p[::-1]
        assert all(x >= 0 and x % n == 0 for x in p)
        assert sum(p) == reference[n-1], (n, sum(p), reference[n-1])
    for n in range(2, 18):
        assert enumerator(n) == direct(n), (n, enumerator(n), direct(n))
    for n in range(2, 15):
        observed=direct_first_shift(n)
        for i, row in enumerate(observed, 1):
            assert row == first_shift_terms(n, i), (n,i,row,first_shift_terms(n,i))
    for prime in [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]:
        assert all(prime % d for d in range(2, int(prime**.5)+1))
        row = enumerator(prime)
        assert row[1] == row[prime-1] == prime
        assert all(row[t] == prime*(prime-1)//2 for t in range(2, prime-1))
    print('VERIFY_OK 42 OEIS totals; 16 exact exhaustive lengths (2..17); 13 first-shift bucket lengths; 16 primes; positivity, complement, necklace divisibility')
    for n in (7, 8, 9, 12, 14, 15):
        print('n=%s fixed-weight indexed counts=%s'%(n, enumerator(n)))


if __name__ == '__main__':
    if len(sys.argv)==2:
        print(enumerator(int(sys.argv[1])))
    else:
        verify()
