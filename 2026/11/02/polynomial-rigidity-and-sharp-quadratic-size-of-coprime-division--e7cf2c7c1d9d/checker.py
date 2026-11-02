#!/usr/bin/env python3
"""Finite sanity checks for the polynomial-lift criterion."""
from math import gcd
from itertools import product
# Signed-coefficient examples: functions T(a,b)=a(a+b)-2a, T=a(b-2)+a*a, T=a, and outside T=a*b+1.
valid=[lambda a,b:a,lambda a,b:a*(a+b),lambda a,b:a*(a*a+b),lambda a,b:a*(a*a+b-1)]
for t in valid:
    for a,b in product(range(2,35),range(1,35)):
        u=t(a,b)//a
        assert t(a,b)>1 and t(a,b)==a*u and u>=1
        A=a*t(a,b);B=b*t(a,b)+1;c=a*b*u-1;d=b*b*u
        assert A*d==B*c+1
        assert gcd(A,B)==1
# Universal obstruction to offset >1: choose x=y any prime dividing s.
for s in range(2,30):
    p=next(p for p in range(2,s+1) if s%p==0 and all(p%d for d in range(2,p)))
    t=p*p+5+s
    assert gcd(p*t,p*t+s)>=p
# Nonzero T(0,Y) examples must have an obstruction.
for t in [lambda a,b:a+1,lambda a,b:a*a+b,lambda a,b:a*a+b*b,lambda a,b:a*a-a+b+2]:
    assert any(gcd(a*t(a,b),b*t(a,b)+1)>1 for a,b in product(range(2,80),range(1,30)))
print('ALL_CHECKS_OK')
