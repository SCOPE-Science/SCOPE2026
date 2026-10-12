#!/usr/bin/env python3
"""Finite, independent checks for rectangular-fiber enumeration and reliability.
Public reproducibility file; standard-library Python 3.10+ only.
This verifies finite instances, not the asymptotic theorems.
"""
from collections import Counter
from fractions import Fraction
from math import comb


def rectangle_test(mask, n):
    rows = {i for i in range(n) for j in range(n) if mask >> (n*i+j) & 1}
    cols = {j for i in range(n) for j in range(n) if mask >> (n*i+j) & 1}
    return all(bool(mask >> (n*i+j) & 1) == (i in rows and j in cols)
               for i in range(n) for j in range(n))


def by_cardinality(n):
    c=Counter()
    for mask in range(1 << (n*n)):
        if rectangle_test(mask,n): c[mask.bit_count()]+=1
    return c


def formula_cardinality(n):
    c=Counter({0:1})
    for a in range(1,n+1):
        for b in range(1,n+1):
            c[a*b]+=comb(n,a)*comb(n,b)
    return c


def fiber_probability(n,p):
    h=formula_cardinality(n)
    return sum(Fraction(count)*p**edges*(1-p)**(n*n-edges)
               for edges,count in h.items())


def triple_independence(mask,n):
    # Bit index (z*n+x)*n+y. Checks the actual pairwise recombination definition.
    pairs=[(z,x,y) for z in range(n) for x in range(n) for y in range(n)
           if mask >> ((z*n+x)*n+y) & 1]
    ps=set(pairs)
    for z,x,y in pairs:
        for z2,x2,y2 in pairs:
            if z==z2 and (z,x,y2) not in ps: return False
    return True


def main():
    total=0
    for n in (2,3,4):
        actual=by_cardinality(n)
        expected=formula_cardinality(n)
        assert actual==expected, (n,actual,expected)
        assert sum(actual.values()) == 1 + (2**n-1)**2
        total+=1 << (n*n)
        print('RECTANGLE',n,'histogram',dict(sorted(actual.items())))
    assert by_cardinality(2)==Counter({2:4,1:4,0:1,4:1})
    q=2
    for p in (Fraction(1,3),Fraction(1,2),Fraction(2,3)):
        num=sum(p**m.bit_count() * (1-p)**(q**3-m.bit_count())
                for m in range(1 << (q**3)) if triple_independence(m,q))
        target=fiber_probability(q,p)**q
        assert num==target, (p,num,target)
        print('DIRECT_PROB',str(p),str(num))
    assert sum(triple_independence(m,2) for m in range(256))==100
    print('VERIFY_OK','rectangle_matrices',total,
          'ternary_teams',256,'rational_probability_tests',3)

if __name__=='__main__':main()
