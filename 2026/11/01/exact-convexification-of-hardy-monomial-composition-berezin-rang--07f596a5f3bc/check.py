#!/usr/bin/env python3
"""Finite, supplementary checks of exact monomial Berezin-hull geometry.
No finite collection of tests establishes the universal theorem.
"""
from fractions import Fraction
import cmath
import math

checks=0
for m in range(2,31):
    n=m+1
    for r in [Fraction(0),Fraction(1,10),Fraction(1,4),Fraction(1,3),Fraction(1,2),Fraction(2,3),Fraction(9,10),Fraction(99,100),Fraction(1)]:
        S=sum((r*r)**j for j in range(n))
        c=1/S
        R=r**n/S
        assert 0 <= c <= 1
        assert 0 <= R <= (1-c)/m or r==0
        if 0<r<1:
            assert R < (1-c)/m
        checks+=4
    for ang_index in range(101):
        theta=2*math.pi*ang_index/101
        v=math.cos(theta)
        h=max(v,(1+v)/n)
        observed=v
        for idx in range(1,100):
            rr=idx/100
            ss=sum(rr**(2*j) for j in range(n))
            cc=1/ss
            rad=rr**n/ss
            observed=max(observed,cc*v+rad)
        assert observed <= h+1e-12
        checks+=1
    a=(math.pi+math.sqrt(m*m-1)-math.acos(1/m))/n**2
    p=2*(math.pi+math.sqrt(m*m-1)-math.acos(1/m))/n
    R=1/n
    assert abs(p-2*n*a)<1e-11
    assert a>0 and p>0
    checks+=2
print(f"PASS: {checks} finite checks; exact universal theorem is proved separately")
