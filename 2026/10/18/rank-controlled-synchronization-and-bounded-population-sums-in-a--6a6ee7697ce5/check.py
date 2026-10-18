#!/usr/bin/env python3
"""Finite exact-rational checks for a contracted-rotation network; analytical infinite claims require proofs."""
from fractions import Fraction
from math import isqrt

def fib_word(n):
    # alpha=(3-sqrt(5))/2, Sturmian digit formula with certified integer-square-root intervals.
    # For k<=n use floors computed as floor(((k+1)*(1+sqrt(5))/2)).
    # Since sqrt(5) irrational, floor ((m + m sqrt5)/2) = (m+isqrt(5*m*m))//2.
    return [2 + ((k+1)+isqrt(5*(k+1)**2))//2 - ((k+2)+isqrt(5*(k+2)**2))//2 for k in range(n)]

def delta_interval(n):
    w=fib_word(n)
    # delta=1/2 + (1/4)sum omega_k/2^k, remaining sum <=2^(1-n).
    low=Fraction(1,2)+sum((Fraction(a,2**(k+2)) for k,a in enumerate(w)),Fraction())
    hi=low+Fraction(1,2**(n+1))
    return low,hi

def certified_branches(x,n,terms=160):
    dlo,dhi=delta_interval(terms)
    xl=xh=Fraction(x)
    history=[]
    for k in range(n):
        dmin=2*(1-dhi); dmax=2*(1-dlo)
        if xh<dmin:j=0
        elif xl>=dmax:j=1
        else:raise AssertionError(f'undetermined branch at {k}')
        history.append(j)
        xl=xl/2+dlo-j
        xh=xh/2+dhi-j
        assert 0<=xl<=xh<=1
    return history

if __name__=='__main__':
    w=fib_word(200)
    assert w[:18]==[0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1]
    l,h=delta_interval(200)
    assert Fraction(5,8)<l<h<Fraction(3,4)
    for x in [Fraction(1,11),Fraction(1,7),Fraction(1,3),Fraction(2,3),Fraction(9,10)]:
        word=certified_branches(x,55,200)
        # The source's exact semiconjugacy implies bounded-imbalance |N_n-n*alpha|<=1.
        # Rational two-sided bounds on alpha via sqrt5 approximants at 200-bit precision:
        scale=10**70
        sqrt5lo=isqrt(5*scale*scale)
        alo=Fraction(3,2)-Fraction(sqrt5lo+1,2*scale)
        ahi=Fraction(3,2)-Fraction(sqrt5lo,2*scale)
        count=0
        for k,a in enumerate(word,1):
            count+=a
            assert count-k*ahi>=-1 and count-k*alo<=1
    print('PASS: 275 exact-rational certified branch steps and Sturmian count checks; exact interval for delta.')
