#!/usr/bin/env python3
"""Reproduce exact algebra and representative scalar-root checks for the stated delay model.
These finite checks do not replace the universal comparison proof in RESULT.md.
"""
from fractions import Fraction as F
from math import exp, isclose


def kernel(n, p, alpha, h):
    return (1 + alpha*p)*n / (1 + h*(1 + alpha*p)*n)


def rate(a, tau):
    assert 0 < a < 1 and tau >= 0
    lo, hi = 0.0, 1.0
    for _ in range(180):
        m=(lo+hi)/2
        if m+a*exp(m*tau)<1:
            lo=m
        else:
            hi=m
    r=(lo+hi)/2
    assert abs(r+a*exp(r*tau)-1)<1e-12
    return r


def check():
    # Exact rational algebra: saturation gap equals q / [h(1+h*z)].
    for h,q in [(F(1,2),F(1,2)),(F(4,5),F(3,5)),(F(2),F(1))]:
        for n in [F(1,4),F(7,3)]:
            for p in [F(0),F(7,5)]:
                alpha=F(13,7)
                z=(1+alpha*p)*n
                H=kernel(n,p,alpha,h)
                assert q/h-q*H == q/(h*(1+h*z))
                assert q*H<1
                U=n+F(1)
                P=p+F(1)
                A=q*kernel(U,P,alpha,h)
                assert 0<A<1

    # Equilibrium algebra across h<q, checked with exact rationals.
    for q,h,kappa,alpha,p in [
        (F(3,4),F(1,2),F(8),F(2),F(3,2)),
        (F(1),F(1,4),F(4),F(1,3),F(7,5)),
        (F(2,3),F(1,6),F(5),F(3),F(1,2)),
    ]:
        assert h<q and kappa>1/(q-h)
        n=1/((q-h)*(1+alpha*p))
        H=kernel(n,p,alpha,h)
        assert q*H==1
        sigma=p/(q*n*(1-n/kappa))
        assert sigma>0
        assert sigma*n*(1-n/kappa)==H*p

    # Finite examples (not proof): exact characteristic exponent limits.
    for beta,tau,kappa,h,alpha in [
        (0.7,0.,4.,1.,100.),
        (0.7,0.5,3.,exp(-0.7*.5),100.), # equality h=q
        (0.3,2.,17.,0.8,13.),
        (0.5,1.,2.,exp(-0.5),1e5),
        (3.,0.3,10.,0.5,0.7),
    ]:
        q=exp(-beta*tau)
        assert h>=q-1e-13
        a=q*kappa/(1+h*kappa)
        r=rate(a,tau)
        assert 0<r<1
        for eps in (min(a/3,(1-a)/3), min(a/50,(1-a)/50)):
            rlo=rate(a-eps,tau)
            rhi=rate(a+eps,tau)
            assert rlo>r>rhi
            assert abs(rlo-rhi)<1
    print('CHECK_OK')

if __name__=='__main__':
    check()
