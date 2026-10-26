#!/usr/bin/env python3
"""Independent arithmetic checks of the spectral and delay formulas.
Uses only the Python standard library. The proof of universality is in RESULT.md.
"""
from fractions import Fraction as Q
import cmath
import math

# Exact factorization at the critical step size.
s0 = Q(15, 16)
r0 = Q(2, 5)
T0 = Q(10) + 6*s0
assert T0 == Q(125, 8)
# (z-r0)(z^2-14z/25+4/25) has coefficients below.
a = Q(14, 25)
b = Q(4, 25)
assert T0 == Q(125,8)
assert T0*(-a-r0) == -15
assert T0*(b+r0*a) == 6
assert T0*(-r0*b) == -1
# Cubic discriminant is -108(9s^2-12s+5).
def disc(s):
    A, B, C, D = 10+6*s, -15, 6, -1
    return B*B*C*C-4*A*C*C*C-4*B*B*B*D-27*A*A*D*D+18*A*B*C*D
for s in (Q(0), Q(1,4), Q(15,16),Q(1),Q(5),Q(100)):
    assert disc(s) == -108*(9*s*s-12*s+5)
assert -(6*r0**3)/(3*T0*r0**2-30*r0+6) == Q(-32,125)
assert -Q(3)/T0 -Q(3,2)*(Q(-32,125)/r0) == Q(96,125)
# Rational exponential-series enclosure: 39/100 < exp(-15/16) < 2/5.
x=Q(15,16)
L=sum((x**j)/math.factorial(j) for j in range(4))
U=L+(x**4/math.factorial(4))/(1-x/Q(5))
assert L>Q(5,2) and U<Q(100,39)

def data(s):
    T=10+6*s
    def P(r):return ((T*r-15)*r+6)*r-1
    lo,hi=0.,1.
    for j in range(90):
        mid=(lo+hi)/2
        if P(mid)>0:hi=mid
        else:lo=mid
    r=(lo+hi)/2
    aa=(15/T-r)/2
    q2=1/(T*r)
    bb=math.sqrt(q2-aa*aa)
    z=complex(aa,bb)
    t=math.exp(-s)
    c=abs(t-z)**2/abs(r-z)**2
    d=(t-r)*(t-z.conjugate())/((z-r)*(z-z.conjugate()))
    return r,z,c,d,t

def normalized(n,r,z,c,d):
    return c+2*(d*(z/r)**n).real

for s in (.01,.2,.5,.8,.9375,.96,1.,2.,10.):
    r,z,c,d,t=data(s)
    assert r>0 and z.imag>0
    assert abs(((10+6*s)*z**3-15*z**2+6*z-1))<2e-12
    if s!=15/16:
        assert (abs(z)>r)==(s>15/16)
    else:
        assert abs(abs(z)-r)<2e-14
    y=[1.,t,t*t]
    for n in range(3,26):
        y.append((15*y[n-1]-6*y[n-2]+y[n-3])/(10+6*s))
        assert abs(y[n]-normalized(n,r,z,c,d)*r**n)<1e-12

# Exact-start positivity at the critical parameter follows from c>2|d|.
r,z,c,d,t=data(15/16)
assert .39<t<.4 and c>2*abs(d)
# Near-critical first-sign-loss indices and their predicted asymptotic scale.
H0=math.sqrt(17/20)*math.sqrt((math.exp(-15/16)-7/25)**2+51/625)/(.4-math.exp(-15/16))
limit=(125/96)*math.log(H0)
assert 4.57<limit<4.59
for delta in (.06,.03,.015,.0075,.003,.001):
    r,z,c,d,t=data(15/16+delta)
    assert c>2*abs(d)
    eps=math.log(abs(z)/r)
    lower=math.log(c/(2*abs(d)))/eps
    first=None
    for n in range(3, int(12/delta)+20):
        if normalized(n,r,z,c,d)<0:
            first=n
            break
    assert first is not None
    assert first+1>=lower
    assert abs(first*delta-limit)<.40
print('PASS: exact polynomial, critical root and derivative, exponential enclosure, 9 recurrences, critical positivity, 6 delayed sign-loss checks')
