#!/usr/bin/env python3
"""Exact and numerical checks for event-index memory in a reset two-bead diffusion."""
from fractions import Fraction as F
from math import sqrt, exp, e, isclose
import random


def moments(r, g):
    den = r*(g+r+2)
    return (2*(g+r+1)/den,
            (2*g+r+2)/den,
            (r+2)*(g+r+1)/den)


def rho(r, g, m):
    return ((r+2*g+2)/(2*(r+g+1)**2))*((r+1)/(r+g+1))**(m-1)


def poly_z(r,g,m):
    return (-r*r+(g*(m-4)-4)*r+(g+1)*(2*g*(m-1)-3))


def peak_rate(g,m):
    return (g*(m-4)-4+sqrt(g*g*m*m+4*(g+1)*(2*g+1)))/2


def exact_checks():
    checks=0
    rational_g=(F(1,9),F(1,2),F(1),F(3,2),F(2),F(5),F(10))
    rational_r=(F(1,23),F(1,3),F(1),F(9,4),F(7),F(31))
    for g in rational_g:
        for r in rational_r:
            x,y,z=moments(r,g)
            assert -(2+r)*x+2*y+2==0;checks+=1
            assert g*x-(1+g+r)*y+z==0;checks+=1
            assert y-z+1==0;checks+=1
            assert x>0 and y>0 and z>0;checks+=1
            # Independent embedded-chain mean via the exponential-clock resolvent.
            ell=1+g
            a=(r+1)/(r+ell); b=1/(r+ell)
            assert 0<a<1 and b>0;checks+=1
            assert (r+ell)*a==r+1 and (r+ell)*b==1;checks+=1
            for m in range(1,26):
                cov=b*a**(m-1)*y
                assert cov/x==rho(r,g,m);checks+=1
                lhs=1/(r+2*g+2)+F(m-1)/(r+1)-F(m+1)/(r+g+1)
                rhs=poly_z(r,g,m)/((r+2*g+2)*(r+1)*(r+g+1))
                assert lhs==rhs;checks+=1
                if m==1:
                    assert poly_z(r,g,m)<0;checks+=1
    for m in range(2,50):
        for g in rational_g:
            z0=poly_z(F(0),g,m)
            assert z0==(g+1)*(2*g*(m-1)-3);checks+=1
            if 2*g*(m-1)<=3:
                assert g*(m-4)-4<0;checks+=1
    return checks


def asymptotic_checks():
    checks=0
    for g in (0.3,1.,10.):
        for m in (400,1200,4000):
            r=peak_rate(g,m)
            assert r>0;checks+=1
            assert abs(r/m-g)<8*(g+1)/m;checks+=1
            assert abs(m*rho(r,g,m)-1/(2*e*g))<11*(g+1)/(g*g*m);checks+=1
            assert abs(poly_z(r,g,m))<3e-7*max(1.,r*r);checks+=1
    for g,m in ((1.,4),(10.,2),(2.,2),(1.,10)):
        r=peak_rate(g,m)
        assert 2*g*(m-1)>3 and r>0;checks+=1
        assert rho(r,g,m)>rho(r*0.1,g,m);checks+=1
        assert rho(r,g,m)>rho(3*r,g,m);checks+=1
    return checks


def sample_series(r,g,n,seed):
    rng=random.Random(seed)
    lam=1+g
    q=0.
    xseries=[]
    for k in range(n+6000):
        t=rng.expovariate(r)
        h=exp(-lam*t)
        common=sqrt(2*g*t/lam)*rng.gauss(0.,1.)
        rel=sqrt(-__import__('math').expm1(-2*lam*t))/lam*rng.gauss(0.,1.)
        x=(1-h)*q/lam+common+rel
        q=(1+g*h)*q/lam+common-g*rel
        if k>=6000:
            xseries.append(x)
    return xseries


def simulation_checks():
    checks=0
    for j,(r,g,m) in enumerate(((0.1,1.,4),(1.1622776601683795,1.,4),
                               (5.,1.,4),(0.1,10.,2),(6.19340539866,10.,2),
                               (25.,10.,2))):
        xs=sample_series(r,g,200000,777007+j)
        mu=sum(xs)/len(xs)
        var=sum((v-mu)**2 for v in xs)/len(xs)
        cov=sum((xs[i]-mu)*(xs[i+m]-mu) for i in range(len(xs)-m))/(len(xs)-m)
        assert abs(var/float(moments(F(str(r)),F(str(g)))[0])-1)<0.06;checks+=1
        assert abs(cov/var-rho(r,g,m))<0.015;checks+=1
    return checks


def main():
    a=exact_checks();b=asymptotic_checks();c=simulation_checks()
    print('PASS: exact rational checks',a,'asymptotic/critical checks',b,
          'independent exact-transition simulation checks',c,'total',a+b+c)

if __name__=='__main__':
    main()
