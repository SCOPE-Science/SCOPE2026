from fractions import Fraction as F
from math import isfinite

def q2(t):
    return 15*t**4 + 12*t**3 - 78*t**2 + 60*t + 7

def q3(t):
    return 45*t**7 + 169*t**6 - 507*t**5 + 681*t**4 - 1153*t**3 + 1155*t**2 - 561*t - 85

a2,b2=F(-103,1000),F(-102,1000)
a3,b3=F(-119,1000),F(-118,1000)
assert q2(a2) < 0 < q2(b2)
assert q3(a3) > 0 > q3(b3)
assert b3 < a2  # disjoint isolating intervals

# Exact support/edge data for K=conv{(-1,-1),(1,-1),(1/2,1),(-1/2,1)}.
# Area is 3.  With x=(0,t), the four edge contributions to
# 2*Area*mu_p^p are bottom, top, right slant, left slant.
def B(t,p):
    return (2*(1+t)**(1-p)*(1-t)**p
            +(1-t)**(1-p)*(1+t)**p
            +(3-t)**(1-p)*(5+t)**p)

# Direct finite-difference sanity check around the isolated roots.
def bisect_p2(lo,hi,steps=100):
    lo=float(lo); hi=float(hi)
    for _ in range(steps):
        m=(lo+hi)/2
        if q2(F.from_float(m)) < 0: lo=m
        else: hi=m
    return (lo+hi)/2

def bisect_p3(lo,hi,steps=100):
    lo=float(lo); hi=float(hi)
    for _ in range(steps):
        m=(lo+hi)/2
        if q3(F.from_float(m)) > 0: lo=m
        else: hi=m
    return (lo+hi)/2

t2=bisect_p2(a2,b2)
t3=bisect_p3(a3,b3)
assert -0.103 < t2 < -0.102
assert -0.119 < t3 < -0.118
assert abs(t2-t3) > 0.015

for p,t0 in [(2,t2),(3,t3)]:
    eps=1e-6
    assert B(t0,p) < B(t0-eps,p)
    assert B(t0,p) < B(t0+eps,p)

# General strict-convexity identity used in the proof:
# if f(t)=a(t)^(1-p)b(t)^p for positive affine a,b, then
# f''=p(p-1)f*(a'/a-b'/b)^2 >= 0.
# The bottom term is strictly convex throughout (-1,1), so their sum is strict.
for p in (2,3,5):
    for t in (-0.8,-0.2,0.4):
        a=1+t; ap=1.0; b=1-t; bp=-1.0
        f=(a**(1-p))*(b**p)
        second=p*(p-1)*f*(ap/a-bp/b)**2
        assert second > 0

print("VERIFY_OK p-critical trapezoid counterexample")
