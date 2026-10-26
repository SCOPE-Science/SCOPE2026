"""Reproduce exact algebraic identities and finite numerical illustrations for the logistic Heun map.
No external dependencies. Numerical tests supplement the proof and do not certify quantifiers.
"""
from fractions import Fraction as F
from math import sqrt, isclose

checks = 0

def check(condition, message='check failed'):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1


def poly(r, x):
    return (x + r*r*x*(1-x) - r**3*x*x*(1-x)**2)/2


def qfactor(r, x):
    u = r*x
    return 1-F(1,2)*u*(u*u-(r+1)*u+(r+1))


def disc(a,b,c,d):
    return b*b*c*c-4*a*c**3-4*b**3*d-27*a*a*d*d+18*a*b*c*d

# Rational algebra checks: map derivation and quotient identity.
for rn in [F(6,5), F(3,2), F(2), F(3), F(4), F(22,5), F(9,2)]:
    c=(rn-1)/rn
    check(poly(rn,c)==c, 'equilibrium identity')
    check(poly(rn,F(0))==0, 'zero fixed point')
    for n in range(101):
        x=c*F(n,100)
        ue=rn*x*(1-x)
        check(poly(rn,x)==(x+rn*ue*(1-ue))/2, 'Heun predictor')
        check(poly(rn,x)-c==(x-c)*qfactor(rn,x), 'upper-factor identity')
        if rn<=F(22,5):
            check(0<=poly(rn,x)<=c, 'safe rational grid')
    # Cubic discriminant calculation is exact over rational coefficients.
    check(disc(rn**3,-rn**3,rn**2,F(1))==rn**6*(rn**4-18*rn**2-27), 'discriminant')

r0=sqrt(9+6*sqrt(3))
y0=(1+sqrt(1-3/r0))/3
x0=1-y0
c0=(r0-1)/r0

def g(r,y):
    return 1+r*r*y-r**3*y*y*(1-y)

check(abs(r0**4-18*r0*r0-27)<2e-12, 'critical polynomial')
check(abs(g(r0,y0))<2e-13, 'critical double root')
check(abs(1-2*r0*y0+3*r0*y0*y0)<2e-14, 'critical stationary point')
check(0<x0<c0, 'tangency inside physical interval')
check(poly(4.5,x0)<0, 'one-step failure')

constant=2*sqrt((r0*y0+3/r0)/(r0**3*(3*y0-1)))

def bisect_root(r, left, right):
    fl=g(r,left)
    fr=g(r,right)
    check(fl*fr<0, 'root bracketing')
    for _ in range(80):
        mid=(left+right)/2
        fm=g(r,mid)
        if fm==0:
            return mid
        if fl*fm<0:
            right=mid
            fr=fm
        else:
            left=mid
            fl=fm
    return (left+right)/2

for eps in [1e-2, 1e-3, 1e-4, 1e-5, 1e-6]:
    r=r0+eps
    ymin=(1+sqrt(1-3/r))/3
    lo=bisect_root(r,1/r,ymin)
    hi=bisect_root(r,ymin,1)
    width=(hi-lo)/sqrt(eps)
    check(abs(width-constant)<0.12*sqrt(eps), 'square-root convergence')
    check(0<1-hi<1-lo<(r-1)/r, 'negative interval in physical domain')
    check(g(r,(lo+hi)/2)<0, 'interior negative')

print('VERIFY_OK', checks, 'critical_r=', format(r0,'.14f'),
      'tangency_x=', format(x0,'.14f'),
      'width_coefficient=',format(constant,'.14f'))
