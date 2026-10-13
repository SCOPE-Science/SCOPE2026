#!/usr/bin/env python3
from fractions import Fraction
import math

def f_frac(t,k):
    return Fraction(k)*(1+t*t)**(k-1)*(t*t-1)**2/(Fraction(2)**k*t**(k+1)+(1+t*t)**(k+1))-1

def h_frac(x,k):
    return 2*(k-1)*x**(k+1)-2*k*x**(k-1)-1

# Exact rational identity checks.
for k in range(2,9):
    for t in (Fraction(2,3),Fraction(3,2),Fraction(4,5),Fraction(5,4),Fraction(7,3)):
        x=(t+1/t)/2
        lhs=f_frac(t,k)
        rhs=h_frac(x,k)/(1+2*x**(k+1))
        assert lhs == rhs, (k,t,lhs,rhs)

def H(x,k):
    return 2*(k-1)*x**(k+1)-2*k*x**(k-1)-1

def xroot(k):
    lo,hi=1.0,2.0
    while H(hi,k)<=0: hi*=2
    for _ in range(120):
        mid=(lo+hi)/2
        if H(mid,k)<0: lo=mid
        else: hi=mid
    return (lo+hi)/2

roots=[]
for k in range(2,201):
    x=xroot(k)
    tm=x-math.sqrt(x*x-1)
    tp=x+math.sqrt(x*x-1)
    assert abs(tm*tp-1)<2e-12
    roots.append((k,x,tm,tp))
for a,b in zip(roots,roots[1:]):
    assert b[1] < a[1]
    assert b[2] > a[2]
    assert b[3] < a[3]

r3=roots[1]
r4=roots[2]
assert abs(r3[2]-0.4779773474549311)<1e-12
assert abs(r3[3]-2.092149356710447)<1e-12
assert abs(r4[2]-0.5398332572293620)<1e-12
assert abs(r4[3]-1.8524238486757854)<1e-12
print('VERIFY_OK exact_identity_cases=35 nesting_k=2..200 k3=%.12f..%.12f k4=%.12f..%.12f' % (r3[2],r3[3],r4[2],r4[3]))
