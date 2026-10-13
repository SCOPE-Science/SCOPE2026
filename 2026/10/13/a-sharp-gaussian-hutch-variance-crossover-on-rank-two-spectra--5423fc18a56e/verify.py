"""Standalone arithmetic and numerical checks for rank-two Gaussian trace-estimation risk.
Run: python3 verify.py (Python standard library only).
The infinite-population results are established by the proof, not by this program.
"""
from fractions import Fraction as F
import math
import random


def vh(a, b):
    return F(2, 3) * (a*a + b*b)


def vp(a, b):
    return a*b*(a*a+6*a*b+b*b)/(a+b)**2


def r(a, b, theta):
    c, s = math.cos(theta), math.sin(theta)
    d = float(a*a)*c*c+float(b*b)*s*s
    return float(a*b)*(float(b)*s*s+float(a)*c*c)/d

checks = 0
# Exact fraction checks of the variance comparison polynomial and the
# alternative scale-free expression of the residual second moment.
for ai in range(1, 19):
    for bi in range(1, ai + 1):
        a, b = F(ai), F(bi)
        s = a*b/(a+b)**2
        assert vp(a,b) == (a+b)**2*(s+4*s*s)
        assert vh(a,b) == F(2,3)*(a+b)**2*(1-2*s)
        t = a/b
        quartic = 2*t**4+t**3-14*t*t+t+2
        assert vh(a,b)-vp(a,b) == b*b*quartic/(3*(t+1)**2)
        checks += 3

# Deterministic midpoint quadrature tests of the two analytical angular
# integrals, of E[r^2], and of the conditional-error variance law.
for a,b in [(1.,1.),(2.,1.),(3.,1.),(10.,1.),(1.2,1.),(5.,2.)]:
    n=8192
    edinv=edinv2=er2=0.0
    for j in range(n):
        th=2*math.pi*(j+0.5)/n
        c=math.cos(th); s=math.sin(th)
        d=a*a*c*c+b*b*s*s
        edinv+=1/d
        edinv2+=1/(d*d)
        er2+=r(a,b,th)**2
    edinv/=n; edinv2/=n; er2/=n
    assert math.isclose(edinv, 1/(a*b), rel_tol=2e-10,abs_tol=1e-11)
    assert math.isclose(edinv2, (a*a+b*b)/(2*a**3*b**3),rel_tol=2e-10,abs_tol=1e-11)
    assert math.isclose(2*er2, float(vp(F(str(a)),F(str(b)))), rel_tol=2e-10,abs_tol=1e-11)
    checks+=3

# Algebraic threshold and sign checks.  It is also elementary that
# u=t+1/t increases strictly for t>1 and 2u^2+u-18 increases for u>2.
u=(math.sqrt(145)-1)/4
threshold=(u+math.sqrt(u*u-4))/2
assert 2.33148 < threshold < 2.33150
for t,expected in [(1.,-1),(2.,-1),(threshold,0),(3.,+1),(10.,+1)]:
    expr=2*t**4+t**3-14*t*t+t+2
    assert abs(expr)<1e-9 if expected==0 else (expr*expected>0)
    checks+=1

# Direct independent Gaussian simulations, not evidence of infinitely-many
# samples. Reconstruct the three-query estimator from two matrix products
# for the sketched subspace and one for the residual quadratic form.
rng=random.Random(126701)
for a,b in [(1.,1.),(2.,1.),(3.,1.)]:
    n=60000
    sums=sums2=0.0
    pos=0
    for _ in range(n):
        g0,g1,z0,z1=[rng.gauss(0,1) for _ in range(4)]
        d=(a*g0)**2+(b*g1)**2
        q0,q1=a*g0/math.sqrt(d),b*g1/math.sqrt(d)
        p0,p1=-q1,q0
        residual=a*p0*p0+b*p1*p1
        est=q0*q0*a+q1*q1*b+residual*(p0*z0+p1*z1)**2
        e=est-(a+b)
        sums+=e; sums2+=e*e
        pos+=(e>0)
    assert abs(sums/n) < 0.07*math.sqrt(float(vp(F(str(a)),F(str(b)))))
    assert abs(sums2/n-float(vp(F(str(a)),F(str(b)))))<0.09*float(vp(F(str(a)),F(str(b))))
    assert abs(pos/n-2*(1-0.5*(1+math.erf(1/math.sqrt(2)))))<0.016
    checks+=3

print('VERIFY_OK', 'checks=',checks,'threshold=',format(threshold,'.12f'))
