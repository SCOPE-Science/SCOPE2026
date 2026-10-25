#!/usr/bin/env python3
"""Independent finite checks for exact-lag moment and discount phase formulas.

The analytic inequalities and all-parameter claims are proved in RESULT.md;
these tests are diagnostic and are not substituted for that proof.
"""
from math import exp, log, isfinite
from fractions import Fraction


def coeff(a, sig, h):
    q = exp(-a*h)
    r = 1-q
    v = sig**2 * (1-q*q)/(2*a)
    lam2 = -(2*r-r*r)/h
    lam4 = (-4*r+6*r*r)/h
    return q, r, v, lam2, lam4


def growth_shape(s):
    q = exp(-s)
    return 2*(1-4*q+3*q*q)/s


def bisect(fn, lo, hi, count=100):
    yl = fn(lo)
    assert yl*fn(hi) < 0
    for _ in range(count):
        mid = (lo+hi)/2
        if fn(mid)*yl > 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def derivative_numerator(s):
    q = exp(-s)
    N = 1 - 4*q + 3*q*q
    Np = 4*q-6*q*q
    return s*Np-N


def discounted_closed(a, sig, beta, h):
    _q,_r,v,lam2,lam4 = coeff(a,sig,h)
    if beta <= lam4:
        return float('inf')
    return 6*(v/h)**2/(beta*(beta-lam2)*(beta-lam4))


def numeric_laplace_via_rk4(a,sig,beta,h,T,step):
    _,_,v,lam2,lam4 = coeff(a,sig,h)
    c = v/h
    def rhs(t,y):
        m2,m4,J = y
        return (lam2*m2+c, lam4*m4+6*c*m2,exp(-beta*t)*m4)
    m2=m4=J=0.0
    t=0.0
    count=round(T/step)
    step=T/count
    for k in range(count):
        y=(m2,m4,J)
        k1=rhs(t,y)
        k2=rhs(t+step/2,tuple(y[i]+step*k1[i]/2 for i in range(3)))
        k3=rhs(t+step/2,tuple(y[i]+step*k2[i]/2 for i in range(3)))
        k4=rhs(t+step,tuple(y[i]+step*k3[i] for i in range(3)))
        m2,m4,J = tuple(y[i]+step*(k1[i]+2*k2[i]+2*k3[i]+k4[i])/6 for i in range(3))
        t += step
    return J


# Check finite-lag variance cancellation exactly for rational transition factors.
for numerator in range(1,39):
    for denominator in range(numerator+1,48):
        q=Fraction(numerator,denominator)
        r=1-q
        v=Fraction(1,2)*(1-q*q)   # a=sigma=1
        assert v/(2*r-r*r) == Fraction(1,2)
print('exact rational stationary variance identity: 1045 rational pairs PASS')

s0=log(3)
star=bisect(derivative_numerator,s0,10.0)
Fstar=growth_shape(star)
assert 2.54 < star < 2.55
assert .5536<Fstar<.5538
assert all(growth_shape(s)<Fstar for s in (s0,1.2,1.8,2.0,2.2,2.4,2.7,2.9,3.3,5,20))
for beta in (.10,.25,.40,.50,.553):
    left=bisect(lambda s:growth_shape(s)-beta,s0,star)
    right=bisect(lambda s:growth_shape(s)-beta,star,4/beta+20)
    for s in (s0,(s0+left)/2):
        assert growth_shape(s)<beta
    for s in ((left+star)/2,star,(star+right)/2):
        assert growth_shape(s)>beta
    assert growth_shape(right+3)<beta
    print(f'discount={beta:.3f}, divergent lag interval=[{left:.12f}, {right:.12f}]')

for a,sig,beta,h in [(1.,1.,.4,.5),(1.,1.,.4,1.2),(1.,1.,.4,7.),
                     (2.,1.5,1.2,1.0),(0.5,1.1,0.3,1.0)]:
    closed=discounted_closed(a,sig,beta,h)
    assert isfinite(closed)
    numeric=numeric_laplace_via_rk4(a,sig,beta,h,180.,.03)
    rel=abs(numeric-closed)/closed
    print('RK4-Laplace',a,sig,beta,h,'closed',f'{closed:.12g}',
          'quadrature',f'{numeric:.12g}','relerr',f'{rel:.3g}')
    assert rel<1e-4

# Exponential moment growth in the nominally divergence-producing regime.
assert coeff(1,1,2)[4] > .4
assert coeff(1,1,7)[4] < .4
assert coeff(1,1,.5)[4] < 0
print('PEAK s=',format(star,'.15f'),'discount critical beta/a=',format(Fstar,'.15f'))
print('ALL CHECKS PASSED')
