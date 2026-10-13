#!/usr/bin/env python3
import math

PI=math.pi

def phi(lam,t):
    return math.cosh(lam*(t-PI))/math.cosh(lam*PI)

def beta3(lam):
    c=math.cosh(PI*lam/3.0)
    return 1.0/(4.0*c*c-3.0)

def v3_closed(lam):
    c=math.cosh(PI*lam/3.0)
    return (9.0/(32.0*PI*PI))*((4*c*c-3)**2)*(4*c*c-1)/(c*c)

def v3_delta(lam):
    c=math.cosh(PI*lam/3.0)
    s=math.sinh(PI*lam/3.0)
    d=4*c*c-3
    b=1/d
    varc=(1+b)/2-b*b
    bp=-(8*PI/3)*c*s/(d*d)
    return varc/(bp*bp)

def v2(lam):
    return math.cosh(PI*lam)**2/(PI*PI)

def ratio(lam):
    c=math.cosh(PI*lam/3.0)
    return 9*(4*c*c-1)/(32*c**4)

def fisher(lam):
    x=PI*lam
    w=x/(math.cosh(x)**2)-1/math.sinh(2*x)
    return 1/(2*lam*lam)+(PI/lam)*w

maxerr=0.0
for lam in (0.02,0.05,0.1,0.3,0.5,1.0,2.0,4.0):
    c=math.cosh(PI*lam/3)
    b=beta3(lam)
    maxerr=max(maxerr,abs(phi(lam,2*PI/3)-b))
    inv=(3/PI)*math.acosh(0.5*math.sqrt(3+1/b))
    maxerr=max(maxerr,abs(inv-lam))
    maxerr=max(maxerr,abs(v3_closed(lam)-v3_delta(lam))/max(1,v3_closed(lam)))
    maxerr=max(maxerr,abs(v3_closed(lam)/v2(lam)-ratio(lam)))
    assert 0 < ratio(lam) < 27/32

# Strict decrease of the exact ratio on the grid.
rs=[ratio(x) for x in (0.02,0.05,0.1,0.3,0.5,1.0,2.0,4.0)]
assert all(a>b for a,b in zip(rs,rs[1:]))

# Small-scale MLE-relative efficiency limits, checked away from cancellation.
lam=0.005
eff3=1/(fisher(lam)*v3_closed(lam))
eff2=1/(fisher(lam)*v2(lam))
assert abs(eff3-8/9)<2e-5
assert abs(eff2-3/4)<3e-5
assert maxerr < 1e-12

print("VERIFY_OK max_identity_error<1e-12 ratio_sup<0.84375 efficiency_limits=(0.8888888889,0.75)")
