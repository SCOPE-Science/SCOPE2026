"""Numerical and exact-rational checks for cross-scale number variance."""
from fractions import Fraction as F
from math import sin, pi, sqrt, exp

def kernel(u,s):
    return max(F(0),s-u)+max(F(0),s-(1-u))-s*s

def product_integral(s,t):
    # Piecewise quadratic polynomial integration over all exact breakpoints.
    knots=sorted({F(0),s,1-s,t,1-t,F(1)})
    out=F(0)
    for a,b in zip(knots,knots[1:]):
        if a==b: continue
        m=(a+b)/2
        # linear interpolants on each segment, product a quadratic polynomial
        ka,kb=kernel(a,s),kernel(b,s)
        la,lb=kernel(a,t),kernel(b,t)
        da,db=kb-ka,lb-la
        out+=(b-a)*(ka*la+(ka*db+la*da)/2+da*db/3)
    return out

def poly(s,t):
    a,b=sorted((min(s,1-s),min(t,1-t)))
    return a*a*(b*(1-b)-a/F(3))

cases=0
for a in range(1,12):
 for b in range(1,12):
    s,t=F(a,12),F(b,12)
    assert product_integral(s,t)==poly(s,t), (s,t)
    cases+=1
assert poly(F(1,3),F(1,3))==F(2,3)*F(1,3)**3-F(1,3)**4

def lam(k,s):
    return 2*sin(pi*k*s)**2/(pi*k)**2
for s,t in [(0.07,0.17),(0.19,0.31),(0.09,0.09),(0.11,0.47)]:
    val=sum(lam(k,s)*lam(k,t) for k in range(1,30000))
    expect=2*float(poly(F(str(s)),F(str(t))))
    assert abs(val-expect)<3e-11,(s,t,val,expect)
    cases+=1
for r in [0.05,0.2,0.6,0.95,1.0]:
    c=1.5*sqrt(r)-.5*r**1.5
    assert 0<c<=1.000000001
    cases+=1
for u in [0.0,0.25,1.0,4.0]:
    r=exp(-u)
    assert abs((1.5*exp(-u/2)-.5*exp(-3*u/2))-(1.5*sqrt(r)-.5*r**1.5))<1e-12
    cases+=1
print('PASS',cases,'rational kernel and numerical Fourier checks')
