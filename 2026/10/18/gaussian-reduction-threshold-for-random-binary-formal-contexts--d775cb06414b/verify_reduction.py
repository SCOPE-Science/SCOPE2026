#!/usr/bin/env python3
"""Standalone exact checks for Bernoulli formal-context object reduction.

Uses a brute-force subset-intersection predicate, a conditional-binomial
law, and an independent inclusion-exclusion formula.
"""
from fractions import Fraction
from itertools import product
from math import comb


def is_redundant(rows, m):
    """Test removal of labelled row zero, allowing the empty intersection."""
    target = rows[0]
    for subset in range(1 << (len(rows)-1)):
        common=(1 << m)-1
        for i in range(1,len(rows)):
            if subset & (1 << (i-1)):
                common &= rows[i]
        if common == target:
            return True
    return False


def exhaustive(r, m, p):
    total = Fraction(0)
    for values in product((0,1), repeat=r*m):
        rows=[]
        for i in range(r):
            rows.append(sum(values[i*m+j] << j for j in range(m)))
        if is_redundant(rows,m):
            k=sum(values)
            total+=p**k * (1-p)**(r*m-k)
    return total


def conditional_binomial(r,m,p):
    total=Fraction(0)
    for s in range(m+1):
        h=p**s
        inner=Fraction(0)
        for k in range(r):
            inner += comb(r-1,k)*h**k*(1-h)**(r-1-k) * (1-p**k)**(m-s)
        total += comb(m,s)*p**s*(1-p)**(m-s)*inner
    return total


def inclusion_exclusion(r,m,p):
    total=Fraction(0)
    for s in range(m+1):
        inner=sum((-1)**j*comb(m-s,j)*(1-p**s*(1-p**j))**(r-1)
                  for j in range(m-s+1))
        total+=comb(m,s)*p**s*(1-p)**(m-s)*inner
    return total


def run():
    count=0
    for p in (Fraction(1,3),Fraction(1,2),Fraction(2,3)):
        for r in range(2,5):
            for m in range(1,5):
                if r*m>12:continue
                a=exhaustive(r,m,p)
                b=conditional_binomial(r,m,p)
                c=inclusion_exclusion(r,m,p)
                assert a==b==c,(p,r,m,a,b,c)
                count+=1
    for r in (2,3,4):
        assert conditional_binomial(r,1,Fraction(1,2)) == 1-Fraction(1,2)**r
    print('exact cases checked:',count)
    print('uniform binary r=3,m=4:',conditional_binomial(3,4,Fraction(1,2)))
    print('VERIFY_OK')

if __name__=='__main__':run()
