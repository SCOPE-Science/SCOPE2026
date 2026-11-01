#!/usr/bin/env python3
"""Exact rational supporting checks for sharp radius scaling.

All experiments have finite range; the all-radius, all-cardinality theorem is
proved analytically in RESULT.md. This file uses Python's standard library only.
"""
from fractions import Fraction as Q
from math import gcd
from itertools import combinations

assertions = 0

def check(test, description):
    global assertions
    if not test:
        raise AssertionError(description)
    assertions += 1


def interval_arcs(a, r, negative=False):
    centers = [Q(j, a) + (Q(1, 2*a) if negative else Q(0))
               for j in range(a+1)]
    width = r/a
    return [(max(Q(0), c-width), min(Q(1), c+width))
            for c in centers if min(Q(1), c+width) > max(Q(0), c-width)]


def intersect(x, y):
    i = j = 0
    z = []
    while i < len(x) and j < len(y):
        lo = max(x[i][0], y[j][0])
        hi = min(x[i][1], y[j][1])
        if hi > lo:
            z.append((lo, hi))
        if x[i][1] < y[j][1]:
            i += 1
        else:
            j += 1
    return z


def P(A, r):
    total = Q(0)
    for neg in (False, True):
        common = [(Q(0), Q(1))]
        for a in A:
            common = intersect(common, interval_arcs(a, r, neg))
        total += sum((hi-lo for lo, hi in common), Q(0))
    return total


def B(k):
    x = k % 1
    return x*x - x + Q(1, 6)


def P_5_fourier(a, b):
    g = gcd(a,b)
    a,b = a//g,b//g
    if (a+b) % 2 == 0:
        return Q(8,25) + Q(2,a*b)*(B(Q(b-a,5))-B(Q(b+a,5)))
    return Q(8,25)+Q(1,2*a*b)*(B(Q(2*(b-a),5))-B(Q(2*(b+a),5)))

# Independent methods for each finite pair: rational interval geometry, and
# the Bernoulli/Fourier formula.
for b in range(2,40):
    for a in range(1,b):
        check(P((a,b), Q(1,5)) == P_5_fourier(a,b), ('Fourier vs intervals',a,b))

# Exhaust the exact finite exceptions left by the two tail bounds in the proof.
odd_cases = {5:Q(8,25),7:Q(32,105),9:Q(4,15),11:Q(52,165),13:Q(4,13)}
for b,ans in odd_cases.items():
    cases = [P_5_fourier(a,b) for a in range(1,b,2) if gcd(a,b)==1]
    check(min(cases)==ans, ('odd exceptional minimum',b))
mixed_cases = [P_5_fourier(a,b) for b in range(2,8)
               for a in range(1,b) if gcd(a,b)==1 and (a+b)%2==1]
check(min(mixed_cases)==Q(3,10), 'mixed exceptional minimum')
check(P((1,3), Q(1,5)) == Q(4,15), 'reciprocal sharp witness')

# All-cardinality sample: choose many 1-, 2-, 3-, and 4-frequency sets, and
# compare their rational normalized overlaps at successively larger radii.
radii = [Q(1,30),Q(1,20),Q(1,12),Q(1,8),Q(1,6),
         Q(1,5),Q(11,50),Q(6,25),Q(1,4)]
for n in (1,2,3,4):
    for A in combinations(range(1,11), n):
        values = [P(A,r)/r for r in radii]
        for i in range(len(values)-1):
            check(values[i] <= values[i+1], ('scale monotonicity',A,i))

# Exact extremal plateau for all frequencies in the powers-of-three chain.
for n in range(1,7):
    freq = tuple(3**j for j in range(n))
    for r in radii:
        check(P(freq,r) == Q(4,3**(n-1))*r,
              ('sharp powers-of-three identity',n,r))

# The exact optimal two-frequency interval, using its proven global lower
# bound, and explicit sharp witness at a rational mesh of positive thresholds.
for j in range(11):
    r = Q(1,5)+Q(j,200)
    check(P((1,3),r) == Q(4,3)*r, ('continuous sharp witness',r))

print('CHECK_OK exact_assertions=' + str(assertions))
