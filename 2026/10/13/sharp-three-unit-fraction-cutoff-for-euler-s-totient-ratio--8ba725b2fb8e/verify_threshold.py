#!/usr/bin/env python3
"""Finite independent arithmetic checks for a sharp totient-ratio threshold.

This program checks bounded instances only. The accompanying proof establishes
all unbounded statements using a denominator obstruction.
"""
from fractions import Fraction
from math import gcd

LOW = Fraction(6, 7)
classes = []
for x in range(2, 4):
    for y in range(x, 7):
        for z in range(y, 100):
            q = Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
            if LOW < q < 1:
                classes.append((x, y, z, q))
                assert q.denominator % 2 == 0 or q.denominator % 3 == 0, (x, y, z, q)

assert classes
assert set((x,y) for x,y,z,q in classes) == {(2,3), (2,4), (2,5), (3,3)}
assert all(z <= 41 for _,_,z,_ in classes)
assert LOW == Fraction(1,2) + Fraction(1,3) + Fraction(1,42)
assert Fraction(1,2)+Fraction(1,3)+Fraction(1,6) == 1

N = 300000
phi = list(range(N+1))
for p in range(2,N+1):
    if phi[p] == p:
        for k in range(p,N+1,p):
            phi[k] -= phi[k]//p

equality_count = 0
prime_support_gap_count = 0
gap_count = 0
for n in range(2,N+1):
    r = Fraction(phi[n], n)
    if r > LOW:
        gap_count += 1
        assert r.denominator % 2 != 0 and r.denominator % 3 != 0
    if r == LOW:
        equality_count += 1
        m = n
        while m % 7 == 0:
            m //= 7
        assert m == 1, n
for k in range(1,9):
    if 7**k <= N:
        assert Fraction(phi[7**k],7**k) == LOW
assert gap_count > 0 and equality_count > 0, 'verify non-vacuous checks'

# Direct coprimality proof invariant: for all x,y,z whose sum lies in the gap,
# the reduced denominator never has gcd 1 with 6. This is a finite check only;
# mathematical coverage uses x,y,z bounds and valuations.
assert all(gcd(q.denominator,6)>1 for _,_,_,q in classes)
print('VERIFY_OK upper_fraction_triples=%d distinct_rationals=%d phi_sieve_N=%d ratio_gap_n=%d totient_equality_cases=%d witness_7=2,3,42 infinite_proof=separate' % (
    len(classes),len(set(q for *_,q in classes)),N,gap_count,equality_count))
