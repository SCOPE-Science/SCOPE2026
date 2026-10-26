#!/usr/bin/env python3
"""Self-contained arithmetic checks for a scalar SAV recurrence and explicit trap."""
from fractions import Fraction as F
import math

CHECKS = 0
def require(condition, description):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(description)

def step(x, r, h, c):
    den = 1.0 + h*x*x/(x*x+2.0*c)
    rr = r/den
    return x-h*rr*x/math.sqrt(x*x/2.0+c), rr

def rationalized(x, r, h, c):
    t=1.0/h
    A=x*x+2.0*c
    den=x*x+t*A
    return x-2.0*r*math.sqrt(A/2.0)*x/den, r*t*A/den

# Exact arithmetic for the h=20, a=C=1 witness.
x1 = F(-37,23)
r1sq = F(3,23)**2*F(3,2)
A1=x1*x1+2
D=A1+20*x1*x1
require(A1==F(2427,529), 'first-step squared numerator')
require(D==F(29807,529), 'second-step rational denominator')
r2sq=r1sq*(A1/D)**2
require(r2sq==(F(7281,685561)**2)*F(3,2),'second-step auxiliary square')
require(r2sq<F(1,75)**2,'sharp rational auxiliary upper bound')
require(F(28)**2<809<F(29)**2,'root bracket')

# With 28 < sqrt(809) < 29, x2 lies between these exact bounds.
x2_lower=x1*(1-F(145620,29807*29))
x2_upper=x1*(1-F(145620,29807*28))
require(x2_lower<F(-132,100) and x2_upper>F(-134,100),'bound orientation test')
require(F(-134,100)<x2_lower<x2_upper<F(-132,100),'x2 enclosure')
# 3 sqrt(2) r2 < .06: square both positive sides.
require(18*r2sq < F(6,100)**2,'infinite-tail bound')
# On [-1.6,-1], q(x)=(x*x+2)/(21*x*x+2) <= 3/23.
for k in range(101):
    xx=-1.6+0.6*k/100
    q=(xx*xx+2)/(21*xx*xx+2)
    require(q<=3/23+1e-14,'finite sampled q sanity')

for a in [1.0,-1.0,2.0,-2.0,3.0,-3.0]:
    for c in [0.5,1.0,2.0]:
        for h in [8.0,20.0,100.0,1000.0]:
            x,r=a,math.sqrt(a*a/2+c)
            for k in range(45):
                xa,ra=step(x,r,h,c)
                xb,rb=rationalized(x,r,h,c)
                require(abs(xa-xb)<1e-10*max(1,abs(xa)),'source recurrence equivalence')
                require(abs(ra-rb)<1e-10*max(1,abs(ra)),'auxiliary recurrence equivalence')
                require(0<ra<=r,'positive energy descent')
                x,r=xa,ra
            if h>=1000:
                b=-2*c/a
                K=(a*a+2*c)**2/a**3*(1+abs(a)/math.sqrt(2*c))
                require(abs(h*(x-b)-K)<max(0.08,0.03*abs(K)), 'large-step asymptotic coefficient')

# Numerically check the certified witness without using numerics to prove its limit.
x,r=1.0,math.sqrt(1.5)
for k in range(60):
    x,r=step(x,r,20.0,1.0)
require(-1.40<x<-1.26,'witness numerical enclosure')
require(r<1e-20,'witness auxiliary decay')
print('PASS',CHECKS,'standard-library assertions; infinite claims rely on the analytic invariant-tail proof')
