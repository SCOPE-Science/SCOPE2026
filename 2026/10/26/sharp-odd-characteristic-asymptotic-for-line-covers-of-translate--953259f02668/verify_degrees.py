#!/usr/bin/env python3
"""Finite consistency checks for translated-conic full-secant degrees.

These are finite checks of the polynomial character formulation, NOT a proof
of the asymptotic assertion (which uses Weil and Pippenger--Spencer).
"""
from itertools import combinations
from math import comb, sqrt

def char(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p-1)//2, p) == 1 else -1

def all_two_roots(p, c, slope, intercept):
    return all(sum(1 for x in range(p) if (x*x + z-slope*x-intercept) % p == 0)==2 for z in c)

def check(p, c):
    ell = len(c)
    assert len(set(c)) == ell and p % 2 and ell >= 2
    m = ell - 1
    allowed_by_geom = 0
    allowed_by_char = 0
    for i, ci in enumerate(c):
        for a in range(p):
            geom = sum(all_two_roots(p,c,s,(a*a+ci-s*a)%p) for s in range(p))
            by_char = 0
            for t in range(p):
                if t == 0:
                    continue
                if all(char(t*t+4*(ci-cj),p) == 1 for j,cj in enumerate(c) if i != j):
                    by_char += 1
            assert geom == by_char, (p,c,i,a,geom,by_char)
            bound = (m-1+2**(-m))*sqrt(p)+2*m+1
            assert abs(geom-p/(2**m)) <= bound, (p,c,i,a,geom,bound)
            allowed_by_geom += geom
            allowed_by_char += by_char
    assert allowed_by_geom == allowed_by_char
    return p,tuple(c),allowed_by_geom,p*ell

if __name__ == '__main__':
    for p, c in ((7,[0,1]),(11,[0,1,3]),(19,[0,1,3,7]),(31,[0,2,4,9]),(43,[1,4,11])):
        print('case', check(p,c))
    print('FULL_SECANT_DEGREES_OK')
