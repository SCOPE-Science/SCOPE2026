#!/usr/bin/env python3
"""Exact-arithmetic checks for the dyadic triangular-product local density.
All calculations use integers or rational numbers; finite tests do not replace the proof.
"""
from collections import Counter
from fractions import Fraction


def coefficient(j):
    return Fraction(j + 1, 1 << (j + 2))


def density(n):
    if n == 0:
        return Fraction(5, 36)
    v = (abs(n) & -abs(n)).bit_length() - 1
    if v & 1:
        return Fraction(5, 36) * (1 - Fraction(1, 1 << (v+1)))
    unit = (n >> v) % 8
    c = {1: Fraction(7, 36), 3: Fraction(1, 144),
         5: Fraction(5, 72), 7: Fraction(1, 144)}[unit]
    return Fraction(5, 36) + c / (1 << v)


def valuation_disintegration(n):
    if n == 0:
        return sum((coefficient(k) / 4 for k in range(0, 200, 2)), Fraction(0))
    v = (abs(n) & -abs(n)).bit_length() - 1
    unit = (n >> v) % 8
    lower = sum((coefficient(k)/4 for k in range(0, v, 2)), Fraction(0))
    if v & 1:
        return lower + coefficient(v)/6
    return (lower + coefficient(v)/12
            + (coefficient(v+1)/2 if unit%4==3 else 0)
            + (coefficient(v+2) if unit==5 else 0)
            + (Fraction(v+5, 1 << (v+4)) if unit==1 else 0))


def square_residues(mod):
    return {a*a % mod for a in range(mod)}


def product_residue_counts(k):
    mod = 1 << k
    count = [0]*mod
    for u in range(mod):
        for v in range(mod):
            count[(u*v)%mod] += 1
    return count


def verify():
    for k in range(1, 13):
        mod=1 << k
        hist=Counter((a*(a+1)//2)%mod for a in range(2*mod))
        assert len(hist)==mod and set(hist.values())=={2}
    print('TRIANGULAR_FIBERS_OK levels=1..12')

    for v in range(26):
        for odd_unit in (1,3,5,7):
            n=odd_unit << v
            assert density(n)==valuation_disintegration(n)
            assert density(-n)==valuation_disintegration(-n)
    print('VALUATION_DISINTEGRATION_OK valuations=0..25 signs=+- unit_classes=4')

    tests=(-32,-16,-9,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,16,32)
    for k in range(3,10):
        mod=1 << k
        counts=product_residue_counts(k)
        sq=square_residues(mod)
        for n in tests:
            hits=sum(cnt for res,cnt in enumerate(counts) if ((res+n)%mod) in sq)
            finite=Fraction(hits,mod*mod)
            true=density(n)
            # Squares modulo 2^k can differ from 2-adic squares only for
            # residues with valuation at least k-2.
            assert finite>=true
            assert finite-true <= Fraction(k+1,1<<(k-2))
        print('CONGRUENCE_OK modulus=',mod,'parameters=',len(tests))

    for k in range(1,8):
        mod=1<<k
        sq=square_residues(mod)
        hist=Counter((a*(a+1)//2)%mod for a in range(2*mod))
        expected=sum(hist[u]*hist[v] for u in range(mod) for v in range(mod) if ((u*v+5)%mod) in sq)
        direct=sum(1 for a in range(2*mod) for b in range(2*mod)
                   if ((a*(a+1)//2)*(b*(b+1)//2)+5)%mod in sq)
        assert direct == expected
    print('TRIANGULAR_VS_HAAR_COUNTS_OK levels=1..7')

    assert density(0)==Fraction(5,36)
    assert density(1)==Fraction(1,3)
    assert density(2)==Fraction(5,48)
    assert density(3)==Fraction(7,48)
    assert density(5)==Fraction(5,24)
    assert density(7)==Fraction(7,48)
    assert density(9)==Fraction(1,3)
    for n in range(-2000,2001):
        assert Fraction(5,48)<=density(n)<=Fraction(1,3)
    print('SHARP_BOUNDS_AND_SPECIAL_CASES_OK parameters=-2000..2000')
    print('VERIFY_OK')

if __name__=='__main__':
    verify()
