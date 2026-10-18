#!/usr/bin/env python3
"""Reproduce algebraic and numerical diagnostics for the Jordan-shear return threshold.
Only Python's standard library is required. Numerical checks complement, not replace, proof.
"""
import math
from fractions import Fraction as F

checks=0

def check(cond, description):
    global checks
    if not cond:
        raise AssertionError(description)
    checks+=1

def slope(t,e):
    return 1.0/(-math.expm1(-t)) + e/(1-e*t) - 2/t

def curvature(t,e):
    z=-math.expm1(-t)
    return -math.exp(-t)/z**2 + e**2/(1-e*t)**2 + 2/t**2

def bisect_increasing(f,a,b):
    assert f(a)<0<f(b)
    for _ in range(115):
        c=(a+b)*.5
        if f(c)>0:b=c
        else:a=c
    return (a+b)*.5

def crit(e):
    left=1.e-7
    right=(1/e)*(1-1e-9)
    t=bisect_increasing(lambda x:slope(x,e),left,right)
    k=3*math.sqrt(math.expm1(t)/((1-e*t)*t*t))
    return t,k

def log_expm1(t):
    if t<50: return math.log(math.expm1(t))
    return t+math.log1p(-math.exp(-t))

def level(t,e,k):
    return log_expm1(t)-math.log1p(-e*t)-2*math.log(t)+2*math.log(3/k)

def bisect_sign(f,a,b, increasing):
    for _ in range(100):
        c=.5*(a+b)
        if (f(c)>0)==increasing: b=c
        else:a=c
    return .5*(a+b)

# Exact rational identities for the conjugated fast dynamics, for many samples.
for ei in (F(1,100), F(1,7), F(2,3), F(5,2)):
    for ki in (F(0), F(1,5), F(3), F(7,2)):
        for yi in (F(-1), F(-2,3), F(0), F(1,4), F(1,2), F(1)):
            B=ki*(yi**3-yi)/(3*ei)
            Bprime=ki*(3*yi*yi-1)/(3*ei)
            S_prime=yi/ei
            check(ei*(S_prime*B+Bprime) == yi*B+ki*(yi*yi-F(1,3)),
                  'fast u differential equation')
            check(ei*S_prime==yi,'fast v differential equation')
            check(B==ki*yi*(yi*yi-1)/(3*ei),'shear primitive identity')
            if yi in (F(-1),F(0),F(1)):
                check(B==0,'exact shear cancellation nodes')

for ei in (0.001,0.005,0.01,0.05,0.1,0.2,0.5,1.,2.):
    t,k=crit(ei)
    check(0<t<1/ei,'minimizer interior')
    check(abs(slope(t,ei))<1e-9,'critical derivative vanishes')
    check(curvature(t,ei)>0,'strict logarithmic convexity at minimum')
    check(level(t,ei,k)==0 or abs(level(t,ei,k))<2e-12,'threshold value')
    for factor in (0.8,1.0,1.2):
        kk=k*factor
        check((level(t,ei,kk)>0) == (factor<1.0) if factor !=1.0 else abs(level(t,ei,kk))<2e-12,
              'trichotomy sign at minimizing point')
        if factor>1.0:
            tleft=bisect_sign(lambda x:level(x,ei,kk),1e-10,t,False)
            tright=bisect_sign(lambda x:level(x,ei,kk),t,(1/ei)*(1-1e-11),True)
            yleft=math.sqrt(1-ei*tleft)
            yright=math.sqrt(1-ei*tright)
            check(0<yright<yleft<1,'two positive nontrivial returns')
            for tt in (tleft,tright):
                R2=math.exp(-tt)*(1+(kk*kk/9)*(1-ei*tt)*tt*tt)
                check(abs(R2-1)<3e-11,'return equation replay')

# Concrete, moderate-precision example with three distinct positive returns.
e=.01;k=4.;tcrit,kcrit=crit(e)
assert k>kcrit
t1=bisect_sign(lambda t:level(t,e,k),1e-10,tcrit,False)
t2=bisect_sign(lambda t:level(t,e,k),tcrit,(1/e)*(1-1e-11),True)
y1=math.sqrt(1-e*t2);y2=math.sqrt(1-e*t1)
check(abs(y1-0.9879802462900596)<2e-11,'example first return')
check(abs(y2-0.9952623157555187)<2e-11,'example second return')

# Small-epsilon critical law and exact limiting scalar stationarity equation.
tzero=bisect_increasing(lambda t:1/(-math.expm1(-t))-2/t,1.0,2.0)
kzero=3*math.sqrt(math.expm1(tzero))/tzero
check(abs(tzero-1.5936242600400401)<2e-12,'limiting minimizer')
check(abs(kzero-3.727901268990078)<2e-12,'limiting critical shear')
e=1e-5;_,ke=crit(e)
check(abs((ke/kzero-1)/e-tzero/2)<1e-4,'first-order critical shear expansion')
print('PASS',checks,'checks')
print('limiting critical t = %.15f, k = %.15f'%(tzero,kzero))
print('epsilon=0.01 k=4 three positive returns y=%.15f, %.15f, 1'%(y1,y2))
