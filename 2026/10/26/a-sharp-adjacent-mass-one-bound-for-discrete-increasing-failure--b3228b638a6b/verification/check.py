"""Numerical/exact checks for the sharp discrete IFR local-ratio-one inequality.
Run: python check.py (standard Python, mpmath optional and not required).
These finite checks are not the proof of the universal inequality.
"""
from fractions import Fraction
from math import log, exp

def bisect_root():
    lo, hi = 0.5, 0.6
    for _ in range(100):
        x = (lo+hi)/2
        if x**3-(1-x)**2 >= 0: hi=x
        else: lo=x
    return (lo+hi)/2

a=bisect_root(); s=a*a; tstar=1/a; b=2-1/a
assert 0.5<a<0.6 and 0<b<a<1
assert abs(a**3-(1-a)**2)<3e-15
assert abs((1+s)*(tstar-1)-1)<3e-15
assert abs((1-a) + a*(1-a) + s-1)<1e-13
assert abs(a*(1-a)-s*(1-b))<1e-14
assert abs(s/(1-b)-(1-a))<1e-14
assert s < 1/3 and s > 0.3
assert log(1/s) <2*(1-s)

def F(v, t):
    val=v/(t-1)
    x=v*t
    count=0
    while x<1:
        val-=1-x
        x*=t
        count+=1
        assert count<100000
    return val

checks=0
for i in range(1, 3001):
    t=1+ i/3001
    assert F(s,t)<1e-10,(t,F(s,t))
    assert F(s-0.0001,t)<1e-10
    checks+=2
for d in range(2,1001):
    td=s**(-1/d)
    g=(d-1+s)*(td-1)
    assert g>1-1e-12,(d,g)
    checks+=1
# Exact 5-point witness demonstrates that an extrapolated 1/3 bound fails.
p={-1:Fraction(3,7),0:Fraction(12,49),1:Fraction(12,49),2:Fraction(3,49),3:Fraction(1,49)}
assert sum(p.values())==1
assert sum(k*v for k,v in p.items())==0
assert p[1]==p[0]
assert sum(v for k,v in p.items() if k>=1)==Fraction(16,49)<Fraction(1,3)
S={j:sum(v for k,v in p.items() if k>=j) for j in range(-2,5)}
for j in range(-1,4):
    assert S[j]*S[j]>=S[j-1]*S[j+1],j
    checks+=1
print('root a=',repr(a),'sharp constant s=',repr(s),'b=',repr(b))
print('finite numerical and exact checks passed (at least):',checks+10)
print('five-point witness tail=',Fraction(16,49))
