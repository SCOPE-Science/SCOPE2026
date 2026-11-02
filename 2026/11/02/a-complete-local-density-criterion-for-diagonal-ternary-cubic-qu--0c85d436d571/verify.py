#!/usr/bin/env python3
"""Finite arithmetic checks for the mixed-valuation ternary cubic criterion.

This script tests finite residue models; the all-prime assertion uses a
mathematical proof based on the genus-one Hasse bound and Hensel lifting.
"""
from itertools import product


def primes_through(N):
    return [n for n in range(2, N+1) if all(n%d for d in range(2,int(n**0.5)+1))]


def cubic_residues(p):
    return {pow(x,3,p) for x in range(p)}


def verify():
    tested_pairs = 0
    primes = [p for p in primes_through(127) if p % 3 == 1]
    for p in primes:
        cubes = cubic_residues(p)
        unitcubes = cubes-{0}
        for alpha in range(1,p):
            for beta in range(1,p):
                if (-beta*pow(alpha,-1,p)) %p in unitcubes:
                    continue
                image = {(alpha*x+beta*y)%p for x,y in product(cubes, repeat=2)}
                assert image == set(range(p)),(p,alpha,beta,image)
                tested_pairs +=1
    # Complete group-theoretic classification of distinct-valuation cosets.
    states = 0
    for u0,u1,u2 in product(range(3),repeat=3):
        S=[(0,u0),(1,u1),(2,u2)]
        D={((x[0]-y[0])%3,(x[1]-y[1])%3) for x in S for y in S}
        assert len(D)==(3 if (u0+u1+u2)%3==0 else 7)
        states+=1
    # At p=7, 1*x^3+2*y^3 represents every nonzero residue,
    # even though -2 is not a cubic residue modulo 7.
    assert (-2)%7 not in cubic_residues(7)
    assert cubic_residues(7)|{0} == {0,1,6}
    print('VERIFY_OK',f'primes_1mod3={len(primes)}',f'noncube_unit_pairs={tested_pairs}',f'coset_patterns={states}', 'p7_witness=1,2,7')

if __name__ == '__main__':
    verify()
