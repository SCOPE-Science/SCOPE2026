#!/usr/bin/env python3
"""Exact coefficient tests for the one-point linear Hodge polynomial.
All arithmetic uses only Python's standard library. Finite checks are not a proof.
"""
from fractions import Fraction
from math import comb, factorial


def valuation(n, p):
    value = 0
    while n and n % p == 0:
        value += 1
        n //= p
    return value


def residue(frac, p):
    assert frac.denominator % p != 0, (frac, p)
    return (frac.numerator % p) * pow(frac.denominator % p, -1, p) % p


def mul(a, b, size):
    out = [Fraction(0) for _ in range(size)]
    for i, c in enumerate(a):
        if not c:
            continue
        for j, d in enumerate(b[:size-i]):
            if d:
                out[i+j] += c*d
    return out


def polynomials(max_g):
    # R_{2g}(x)=[z^g](sin(sqrt(z))/sqrt(z))^{-x}.
    z = [Fraction(0)] * (max_g+1)
    for k in range(1, max_g+1):
        z[k] = Fraction((-1)**(k+1), factorial(2*k+1))
    zpower = [Fraction(1)] + [Fraction(0)]*max_g
    rising = [Fraction(1)]
    rows = [[Fraction(0) for _ in range(g+1)] for g in range(max_g+1)]
    for m in range(max_g+1):
        if m:
            zpower = mul(zpower, z, max_g+1)
            new = [Fraction(0)]*(len(rising)+1)
            for j, c in enumerate(rising):
                new[j] += (m-1)*c
                new[j+1] += c
            rising = new
        for g in range(m, max_g+1):
            A = zpower[g] / factorial(m)
            if A:
                for j, c in enumerate(rising):
                    rows[g][j] += A*c
    return rows


def check(max_g=30):
    R = polynomials(max_g)
    cases = 0
    for p in (5, 7, 11, 13, 17, 19, 23, 29, 31):
        for g in range(1, max_g+1):
            s = (p-1)//2
            q, r = divmod(g, s)
            if q == 0:
                continue
            E = q + valuation(factorial(q), p)
            m = q+r
            H = [sum(R[g][j]*comb(j, i) for j in range(i, g+1)) / 4**g
                 for i in range(g+1)]
            scaled = [p**E*h for h in H]
            assert all(x.denominator % p for x in scaled)
            assert all(residue(scaled[i], p) == 0 for i in range(m+1, g+1))
            uq = factorial(q) // p**valuation(factorial(q), p)
            expected = ((-1)**(g+m+q) * pow(4**g, -1, p) *
                        pow(factorial(r)*6**r*uq, -1, p)) % p
            assert residue(scaled[m], p) == expected != 0, (p, g, m)
            cases += 1
    return cases


if __name__ == '__main__':
    print('VERIFY_OK', check())
