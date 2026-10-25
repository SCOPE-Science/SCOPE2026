#!/usr/bin/env python3
"""Exact certificate for unit-segment joins of four-dimensional lattice boxes.

Run: python3 verify.py. Uses only Python 3 standard library.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, factorial, prod

LIMIT = 4928

def es(a):
    return [1] + [sum(prod(v) for v in combinations(a, j)) for j in range(1, 5)]

def defect(a):
    _, e1, e2, e3, e4 = es(a)
    return e4 - e3 - 5*e2 - 10*e1 - 45

def count_join(a, n):
    # Independent exact lattice-slice count at integer n.
    return sum((n-k+1)*prod(k*x+1 for x in a) for k in range(n+1))

def first_coefficient_newton(values):
    # L(t)=sum_{j=0}^6 Delta^j L(0) binom(t,j).
    # [t] binom(t,j)=(-1)^(j-1)/j, j>=1.
    return sum((Fraction((-1)**(j-1), j) *
                sum((-1)**(j-k)*comb(j,k)*values[k]
                    for k in range(j+1))) for j in range(1,7))

def classify(limit):
    # For a<=b<=c<=d with product <=limit and all entries >=2:
    # a^4<=limit, a*b^3<=limit, a*b*c^2<=limit,
    # d<=floor(limit/(a*b*c)). These bounds exhaust the full domain.
    examined = 0
    successes = []
    a = 2
    while a**4 <= limit:
        b = a
        while a*b**3 <= limit:
            c = b
            while a*b*c*c <= limit:
                for d in range(c, limit//(a*b*c)+1):
                    examined += 1
                    if defect((a,b,c,d)) > 0:
                        successes.append((a,b,c,d))
                c += 1
            b += 1
        a += 1
    return examined, successes


def verify():
    examined, winners = classify(LIMIT)
    assert examined == 10618, examined
    assert winners == [(7,8,8,11)], winners
    assert defect((7,8,8,11)) == 14
    assert 24*prod((7,8,8,11)) == 118272
    # Any side equal to 1 gives defect -6(xy+xz+yz)-15(x+y+z)-55<0;
    # this exact identity is independently checked at many sample triples.
    for x in (1, 2, 5, 17):
        for y in (1, 3, 10):
            for z in (1, 4, 23):
                assert defect((1,x,y,z)) == -6*(x*y+x*z+y*z)-15*(x+y+z)-55
    # Exact independent finite-difference recovery of the linear coefficient
    # from lattice-point counts, for the sharp witness and sample neighbors.
    for side in ((7,8,8,11), (7,8,8,10), (9,9,9,9),
                 (8,8,8,8), (1,100,200,300), (3,11,11,11),
                 (7,8,9,10), (2,50,50,50)):
        vals = [count_join(side, n) for n in range(7)]
        assert first_coefficient_newton(vals) == Fraction(-defect(side), 30), side
        # General polynomial degree 6: its 7th forward difference is zero.
        vals.append(count_join(side, 7))
        assert sum((-1)**(7-j)*comb(7,j)*vals[j] for j in range(8)) == 0
    # The balancing identity holds for any b>=a+2 at fixed c,d.
    checked_balancing = 0
    for a in range(1,8):
        for b in range(a+2,12):
            for c in range(1,10):
                for d in range(1,10):
                    assert defect((a+1,b-1,c,d))-defect((a,b,c,d)) == \
                           (b-a-1)*(c*d-c-d-5)
                    checked_balancing += 1
    # In the uniform family the quartic has one positive root by Descartes,
    # and its value changes sign strictly between r=8 and r=9.
    assert defect((8,8,8,8)) < 0 < defect((9,9,9,9))
    print('EXACT_OK examined=', examined, 'unique_minimizer=',winners[0],
          'defect=', defect(winners[0]), 'balancing_cases=',checked_balancing,
          'newton_checks=8')

if __name__ == '__main__':
    verify()
