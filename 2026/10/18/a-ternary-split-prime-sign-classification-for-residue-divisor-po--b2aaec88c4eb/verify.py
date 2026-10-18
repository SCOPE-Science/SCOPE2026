#!/usr/bin/env python3
"""Independent finite checks for a real-exponent residue divisor-sum identity."""
from fractions import Fraction
from math import isclose

def direct(n,s):
    return sum((Fraction(d)**s if isinstance(s,int) else d**s) * (1 if d % 3 == 0 else -1 if d % 3 == 1 else 0)
               for d in range(1,n+1) if n%d==0)

def predicted(n,s):
    t=0; m=n
    while m%3==0:
        t+=1; m//=3
    ordinary=sum((Fraction(d)**s if isinstance(s,int) else d**s) for d in range(1,m+1) if m%d==0)
    character=sum((1 if d%3==1 else -1)*(Fraction(d)**s if isinstance(s,int) else d**s)
                  for d in range(1,m+1) if m%d==0)
    return (sum((Fraction(3)**(j*s) if isinstance(s,int) else 3**(j*s)) for j in range(1,t+1))-Fraction(1,2))*ordinary-character/2

for s in [-2,-1,0,1,2]:
    for n in range(1,2001):
        z=direct(n,s);v=predicted(n,s)
        assert z==v,(n,s,z,v)
        if s<=-1: assert z<0
        elif s>0: assert (z>0)==(n%3==0)
        elif s==0:
            t=0;m=n
            while m%3==0:t+=1;m//=3
            if t==0:assert z<0
            elif t>=2:assert z>0
            else:
                # At t=1, zero exactly for m supported on primes 1 mod 3.
                has_bad=any(m%d==0 and d%3==2 for d in range(2,m+1))
                assert (z>0)==has_bad and (z==0)==(not has_bad)
for s in [-0.95,-0.75,-0.5,-0.25]:
    for n in range(1,2501):
        z=direct(n,s);v=predicted(n,s)
        assert isclose(z,v,abs_tol=1e-9,rel_tol=1e-10),(n,s,z,v)
        if n%3:assert z<0
for n in (9,18,63):
    print('example s=-3/4',n,round(direct(n,-0.75),9))
assert direct(9,-0.75)<0<direct(18,-0.75)
assert direct(63,-0.75)<0
print('PASS exact integer-exponent cases, floating half-line regression, zero supports')
