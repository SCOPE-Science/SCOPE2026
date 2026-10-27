"""Reproducible arithmetic checks for fixed-equilibrium superstable 2-cycles.

Uses standard-library exact fractions and floating arithmetic. The proof of
universal statements is in RESULT.md; finite checks are supplementary.
"""
from fractions import Fraction as F
from math import factorial, log, exp

b = F(12, 25)
d1, d2 = F(2, 5), F(23, 50)

def exact_data(d):
    x, y = b-d, b+d
    qx, qy = x*(1-x), y*(1-y)
    ratio = y*(1-x)/(x*(1-y))
    return x,y,qx,qy,ratio

assert exact_data(d1) == (F(2,25), F(22,25), F(46,625), F(66,625), F(253,3))
assert exact_data(d2) == (F(1,50), F(47,50), F(49,2500), F(141,2500), F(2303,3))

def e_lower(k,n):
    return sum((F(k**j,factorial(j)) for j in range(n+1)),F(0))

# Rational lower bounds on e^5 and e^7, plus e<3.
assert e_lower(5,5) > F(253,3)
assert e_lower(7,8) > F(2303,3)
assert F(3**4) < F(253,3)
# The elementary bound e<3 follows from k!>=2^(k-1)
# for k>=2, with strict inequality for k>=4.
# These bounds rigorously imply 4<log(253/3)<5 and
# log(2303/3)<7.
assert 1-F(23,125)*5 > 0
assert 1-F(33,125)*4 < 0
assert 1-F(141,1150)*7 > 0
assert 1-F(49,1150)*7 > 0

def lam(d):
    x,y,qx,qy,ratio=exact_data(F(d))
    a=log(float(ratio))/float(d)
    return (1-a*float(qx))*(1-a*float(qy))

def strength(d):
    return log(float(exact_data(F(d))[-1]))/float(d)

assert lam(d1)<0 and lam(d2)>0
assert lam(F(1,1000))>0 and lam(F(47999,100000))<0

def bisect(lo,hi):
    sign = lam(lo)>0
    assert sign != (lam(hi)>0)
    for _ in range(90):
        mid=(lo+hi)/2
        if (lam(mid)>0)==sign: lo=mid
        else: hi=mid
    return (lo+hi)/2

brackets=[(0.001,0.4),(0.4,0.46),(0.46,0.47999)]
roots=[bisect(lo,hi) for lo,hi in brackets]
assert all(roots[i]<roots[i+1] for i in range(2))
assert all(2/(float(b)*(1-float(b))) < strength(r) for r in roots)

# Independent map evaluation checks for cycle identity and derivative multiplier.
def forward(a,b,x):
    t=exp(a*(x-b))
    return x/(x+(1-x)*t)
for d in [d1,d2]:
    x,y,*_=exact_data(d)
    a=strength(d)
    assert abs(forward(a,float(b),float(x))-float(y))<1e-12
    assert abs(forward(a,float(b),float(y))-float(x))<1e-12

print('VERIFY_OK exact_rational_witnesses=2 numerical_root_brackets=3 forward_cycle_checks=4')
print('Approximate root strengths:',', '.join('%.9f'%strength(r) for r in roots))
