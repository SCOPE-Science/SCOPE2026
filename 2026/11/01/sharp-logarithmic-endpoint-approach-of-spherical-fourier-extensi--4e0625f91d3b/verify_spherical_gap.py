#!/usr/bin/env python3
"""Reproducible numerical checks for the sharp spherical mixed-norm stability gap.

This script is diagnostic only: the infinite-dimensional theorem and asymptotic
remainders rely on the written analytical proof, not finite computation.
"""
import math

PI = math.pi

def sinc(r):
    return math.sin(r)/r if abs(r) > 1e-6 else 1 - r*r/6 + r**4/120 - r**6/5040

def v(r):
    if abs(r) <= 1e-5:
        return r/3 - r**3/30 + r**5/840
    return (math.sin(r)-r*math.cos(r))/(r*r)

def N(r):
    return (r*r-2)*math.sin(r)+2*r*math.cos(r)

def root():
    left, right = PI/2, PI
    assert N(left)>0 and N(right)<0
    for _ in range(90):
        mid=(left+right)/2
        if N(mid)>0: left=mid
        else: right=mid
    return (left+right)/2

r = root()
star=v(r)
kappa=1 - 2/r**2
C0=6**1.5*math.sqrt(PI)/4
C1=r*r*math.sqrt(2*PI/kappa)
gamma_inf=16*PI*PI*(1-star*star)
coefficient=16*PI*PI*(3-star*star)
assert 2 < r < 2.2
assert abs(N(r)) < 1e-13
assert .4 < star < .5 and .5 < kappa < .6
assert abs(v(PI)-1/PI)<1e-14
assert 5/16<1/PI
# Identities for the derivative, its critical-point equation and the Bessel ODE.
for x in [.15,.5,1.2,2,3.3,4,6.4]:
    h=1e-4
    deriv=(v(x+h)-v(x-h))/(2*h)
    expected=N(x)/x**3
    assert abs(deriv-expected)<2e-6, (x,deriv,expected)
    second=(v(x+h)-2*v(x)+v(x-h))/(h*h)
    assert abs(second+2*expected/x+(1-2/x**2)*v(x))<2e-5

try:
    from scipy.integrate import quad
except ImportError:
    print('CHECK_OK: elementary identities; optional SciPy quadrature unavailable')
else:
    for q in (16, 32, 64, 128):
        x0,err0=quad(lambda x: abs(sinc(x))**q*x*x,0,150,epsabs=1e-10,epsrel=1e-10,limit=300)
        x1,err1=quad(lambda x: abs(v(x))**q*x*x,0,150,epsabs=1e-10,epsrel=1e-10,limit=300,points=[r])
        t0=x0**(2/q)
        t1=x1**(2/q)
        gap=16*PI*PI*(t0-t1)
        approx=16*PI*PI*(1-star*star+((-3+star*star)*math.log(q)+2*math.log(C0)-2*star*star*math.log(C1))/q)
        assert 0<gap<gamma_inf
        assert abs(gap-approx)<7 and abs(gap-approx)<110/q, (q,gap,approx)
        print('q',q,'gap',round(gap,8),'two_term',round(approx,8))
    print('CHECK_OK: derivative identity, Bessel ODE, global-tail bound, Laplace asymptotic profile')
print('r*',r,'v*',star,'kappa',kappa,'C0',C0,'C1',C1,'limit',gamma_inf,'log_coefficient',coefficient)
