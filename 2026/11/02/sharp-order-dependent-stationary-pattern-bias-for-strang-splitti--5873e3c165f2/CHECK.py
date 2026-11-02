#!/usr/bin/env python3
"""Symbolic and numerical checks for odd-power Strang stationary patterns.

Run: python CHECK.py
Requires Python 3 and SymPy. Numerical checks supplement, but do not
replace, the proof in RESULT.md.
"""
import math
import random
import sympy as sp


def reaction(x, h, p):
    return math.exp(h)*x/(1+math.expm1(2*p*h)*abs(x)**(2*p))**(1/(2*p))


def heat_checkerboard(x, h, lam):
    return x*math.exp(-lam*h)


def drd(x,h,lam,p):
    return heat_checkerboard(reaction(heat_checkerboard(x,h/2,lam),h,p),h/2,lam)


def rdr(x,h,lam,p):
    return reaction(heat_checkerboard(reaction(x,h/2,p),h,lam),h/2,p)


def values(h,lam,p):
    a=p*h
    yd=math.sinh((1-lam)*a)/math.sinh(a)
    yr=math.sinh((1-lam)*a)/(math.sinh((1-lam)*a)+math.sinh(lam*a))
    return yd,yr


def heat_cycle4(x,h,lam):
    # Laplacian C4 has eigenvalues 0,2,2,4; kappa=lam/4.
    kappa=lam/4
    s=[1.,-1.,1.,-1.]
    alpha=sum(x)/4
    beta=sum(a*b for a,b in zip(x,s))/4
    return [alpha+math.exp(-4*kappa*h)*beta*s[i]
            +math.exp(-2*kappa*h)*(x[i]-alpha-beta*s[i]) for i in range(4)]


def run():
    L,T=sp.symbols('L T',real=True)
    m=1-L
    for p in range(1,5):
        B=sp.exp(2*p*T)
        bd=(B-1)*sp.exp(-p*L*T)
        br=(sp.exp(p*T)-1)*(1+sp.exp(p*(1-2*L)*T))
        yd=sp.sinh(p*m*T)/sp.sinh(p*T)
        yr=sp.sinh(p*m*T)/(sp.sinh(p*m*T)+sp.sinh(p*L*T))
        tests=[(sp.exp(2*p*m*T)-1)/bd-yd,
               (sp.exp(2*p*m*T)-1)/br-yr,
               yr/yd-sp.cosh(p*T/2)/sp.cosh(p*(1-2*L)*T/2),
               yr.subs(L,sp.Rational(1,2))-sp.Rational(1,2),
               sp.limit((yd-m)/T**2,T,0)+p*p*m*L*(2-L)/6,
               sp.limit((yr-m)/T**2,T,0)-p*p*m*L*(1-2*L)/6]
        for eq in tests:
            assert sp.simplify(sp.together(eq).rewrite(sp.exp))==0
    count=24
    rng=random.Random(261014867)
    for p in range(1,5):
        for k in range(160):
            lam=rng.uniform(.03,.97)
            h=rng.uniform(.02,1.5)
            x=rng.uniform(-1.3,1.3)
            yd,yr=values(h,lam,p)
            mu=1-lam
            assert 0<yd<mu and yd<yr<1
            assert (yr>mu)==(lam<.5)
            xd=yd**(1/(2*p))
            xr=yr**(1/(2*p))
            assert math.isclose(drd(xd,h,lam,p),xd,rel_tol=2e-11)
            assert math.isclose(rdr(xr,h,lam,p),xr,rel_tol=2e-11)
            assert math.isclose(drd(-xd,h,lam,p),-xd,rel_tol=2e-11)
            assert math.isclose(rdr(-xr,h,lam,p),-xr,rel_tol=2e-11)
            for f,z in [(drd,xd),(rdr,xr)]:
                eps=1e-5
                derivative=(f(z+eps,h,lam,p)-f(z-eps,h,lam,p))/(2*eps)
                assert math.isclose(derivative,math.exp(-2*p*mu*h),rel_tol=1e-6)
            bd=math.expm1(2*p*h)*math.exp(-p*lam*h)
            br=math.expm1(p*h)*(1+math.exp(p*(1-2*lam)*h))
            for f,b in [(drd,bd),(rdr,br)]:
                direct=f(x,h,lam,p)
                rational=math.exp(mu*h)*x/(1+b*abs(x)**(2*p))**(1/(2*p))
                assert math.isclose(direct,rational,abs_tol=2e-11,rel_tol=2e-11)
            s=[1.,-1.,1.,-1.]
            state=[x*t for t in s]
            for order in ['DRD','RDR']:
                if order=='DRD':
                    state2=heat_cycle4(state,h/2,lam)
                    state2=[reaction(z,h,p) for z in state2]
                    state2=heat_cycle4(state2,h/2,lam)
                    scalar=drd(x,h,lam,p)
                else:
                    state2=[reaction(z,h/2,p) for z in state]
                    state2=heat_cycle4(state2,h,lam)
                    state2=[reaction(z,h/2,p) for z in state2]
                    scalar=rdr(x,h,lam,p)
                assert max(abs(a-b*scalar) for a,b in zip(state2,s))<2e-11
            count+=12
    print('PASS:',count,'symbolic and numerical probes; odd-power p=1..4 and 4-cycle exact subflows')

if __name__=='__main__':
    run()
