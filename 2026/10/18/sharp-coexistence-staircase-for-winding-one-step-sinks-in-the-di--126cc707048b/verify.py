#!/usr/bin/env python3
"""Finite exact-arithmetic and analytical-consistency checks for the stated map.

Run: python3 verify.py
No external packages required. Finite tests are not the quantified proof.
"""
from fractions import Fraction as Q
from math import isqrt, pi, sqrt


def census(width, kick2):
    assert width > 0 and kick2 > 0
    lim = isqrt(kick2.numerator // kick2.denominator) + 3
    return sum(Q(m * m) < kick2 < Q(m * m) + width
               for m in range(-lim, lim + 1))


def capacity_formula(width):
    assert width > 0
    p = 1
    while Q((p+1)**2 - 1) < width:
        p += 1
    z = 0
    while Q((z+1)**2) < width:
        z += 1
    return max(2*p, 2*z+1)


def capacity_by_all_cells(width):
    # The boundaries of all counted integer-square windows cover every
    # possible maximizer cell. A generous finite cutoff is exact because
    # after m^2 > m0^2 + width, further windows cannot overlap more.
    maxmode = isqrt(width.numerator // width.denominator) + 8
    endpoints = {Q(0)}
    for m in range(maxmode + 1):
        endpoints.add(Q(m*m)); endpoints.add(Q(m*m)+width)
    ordered = sorted(endpoints)
    vals = [census(width, (a+b)/2) for a,b in zip(ordered, ordered[1:])]
    return max(vals)


widths = [Q(1, 100), Q(1), Q(11, 10), Q(3), Q(31,10), Q(4),
          Q(41,10), Q(8), Q(81,10), Q(9), Q(91,10), Q(15),
          Q(151,10), Q(100)]
for w in widths:
    assert capacity_by_all_cells(w) == capacity_formula(w), w
    for q in range(1, 10):
        assert (capacity_formula(w) >= 2*q) == (w > q*q-1)
        assert (capacity_formula(w) >= 2*q+1) == (w > q*q)

# Symbolic Jacobian determinant = b and trace = 1+b+c,
# with entries [[1+c,b],[c,b]]. Check identities on exact rationals.
for b in [Q(1,10), Q(1,2), Q(9,10)]:
    for c in [Q(-7,2), Q(-1), Q(0), Q(1), Q(3)]:
        a11, a12, a21, a22 = 1+c, b, c, b
        assert a11*a22-a12*a21 == b
        tr = a11+a22
        assert tr == 1+b+c
        assert 1-tr+b == -c
        assert 1+tr+b == 2*(1+b)+c

# Independent parameter-space spot checks: each mode is tested directly
# against the squared sine-amplitude and strict Schur conditions.
for b in [0.1, 0.5, 0.9]:
    for k in [0.2, 1.7, 2.9, 6.6, 10.4, 37.0, 79.0]:
        t = (k/(2*pi*(1-b)))**2
        w = ((1+b)/(pi*(1-b)))**2
        positive = int(sqrt(t))+3
        from_windows = sum(m*m < t < m*m+w for m in range(-positive,positive+1))
        direct = 0
        for m in range(-positive,positive+1):
            d=2*pi*(1-b)*m
            if k*k > d*d:
                c = -sqrt(k*k-d*d)
                if -2*(1+b)<c<0:
                    direct += 1
        assert direct == from_windows, (b,k,from_windows,direct)
print('VERIFY_OK')
