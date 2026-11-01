#!/usr/bin/env python3
"""Exact small-instance checks for the cyclic Fourier frame on primitive words.

Run with Python 3 and sympy: python checker.py. The theorem for all sizes is
proved analytically; this program independently enumerates modest samples.
"""
from itertools import product
from math import gcd
from fractions import Fraction
from collections import Counter
from sympy import Matrix, Symbol, Poly, Rational, mobius, divisors, factorint


def primitive(x):
    n = len(x)
    return not any(all(x[i] == x[(i + d) % n] for i in range(n))
                   for d in divisors(n) if 1 <= d < n)


def period_count(q, n):
    return sum(int(mobius(d)) * q ** (n // d) for d in divisors(n))


def predicted_moment(q, n, delta):
    P = period_count(q, n)
    return Fraction(sum(int(mobius(d))*q**(n//d)
                        for d in divisors(n) if delta % (n//d) == 0), P)


def predicted_eigen(q, n, k):
    P = period_count(q, n)
    return Fraction(sum(int(mobius(d))*d*q**(n//d)
                        for d in divisors(gcd(n,k))), P)


def check_one(q,n):
    words = [x for x in product(range(q), repeat=n) if primitive(x)]
    P=len(words)
    assert P==period_count(q,n), ('count',q,n,P)
    # Independently count equal symbol pairs, then use character orthogonality
    # under simultaneous permutation of the q alphabet symbols.
    for delta in range(n):
        equality_count = sum(x[0]==x[delta] for x in words)
        if delta == 0:
            direct = Fraction(1)
        else:
            direct = Fraction(q*equality_count-P,(q-1)*P)
        assert direct==predicted_moment(q,n,delta), ('moment',q,n,delta,direct)
    moment=[predicted_moment(q,n,abs(i-j)) for i in range(n) for j in range(n)]
    C=Matrix(n,n,lambda i,j: Rational(predicted_moment(q,n,(j-i)%n)))
    z=Symbol('z')
    computed=C.charpoly(z).as_poly()
    expected=Poly(1,z)
    levels=Counter(predicted_eigen(q,n,k) for k in range(n))
    for eigen,multiplicity in levels.items():
        expected*=Poly((z-Rational(eigen))**multiplicity,z)
    assert computed==expected, ('spectrum',q,n)
    expected_nullity=1 if (q,n)==(2,2) else 0
    assert C.nullspace().__len__()==expected_nullity, ('rank',q,n)
    B=min(levels)
    A=max(levels)
    if B>0:
        assert Fraction(A,B)<=4
        assert (Fraction(A,B)==4) == ((q,n)==(2,3))
    return len(words),n*n,len(levels)


def main():
    run=[(q,n) for q,high in [(2,10),(3,7),(4,6),(5,5)] for n in range(2,high+1)]
    count=0; comparisons=0; spectra=0
    for q,n in run:
        m,e,l=check_one(q,n)
        count+=1; comparisons+=n; spectra+=1
    # Further exact arithmetic on larger n,q (no word enumeration).
    arithmetic=0
    for q in range(2,11):
        for n in range(2,121):
            ev=[predicted_eigen(q,n,k) for k in range(n)]
            P=period_count(q,n)
            assert P>0
            assert max(ev)==Fraction(q**n,P)
            assert min(ev)==predicted_eigen(q,n,0)
            if (q,n)==(2,2):
                assert min(ev)==0
            else:
                assert 0<min(ev) and max(ev)/min(ev)<=4
                assert (max(ev)/min(ev)==4)==((q,n)==(2,3))
            arithmetic+=1
    print('PASS,',count,'complete enumerated (alphabet,length) instances;',comparisons,
          'exact pair-moment comparisons;',spectra,
          'exact spectral polynomial comparisons;',arithmetic,
          'larger parameter checks. All are finite corroboration only.')

if __name__=='__main__': main()
