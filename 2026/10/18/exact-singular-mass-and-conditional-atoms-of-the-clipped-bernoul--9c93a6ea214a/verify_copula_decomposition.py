"""Supplementary checks for the clipped Bernoulli-correlation copula measure.

The general theorem follows from the written proof, not these finite tests.
Run with Python 3 using only the standard library.
"""
from fractions import Fraction
from math import isclose, log, sqrt


def cuts(s, u):
    return s*u/(1-u+s*u), u/(s+(1-s)*u)


def jumps(s, u):
    return s/(2*(1-u+s*u)), s/(2*(s+(1-s)*u))


def raw_derivative(r, u, v):
    return v + r*(1-2*u)*sqrt(v*(1-v))/(2*sqrt(u*(1-u)))


def density(r, u, v):
    return 1 + r*(1-2*u)*(1-2*v)/(4*sqrt(u*(1-u)*v*(1-v)))


def mass(r):
    s=r*r
    return -s*log(s)/(1-s)


def simpson(f, a, b, n=800):
    h=(b-a)/n
    return h/3*(f(a)+f(b)+4*sum(f(a+i*h) for i in range(1,n,2))
                 +2*sum(f(a+i*h) for i in range(2,n,2)))


def run():
    nchecks=0
    for p in range(1,10):
        r=Fraction(p,10); s=r*r
        for k in range(1,100):
            u=Fraction(k,100)
            l,h=cuts(s,u)
            jl,ju=jumps(s,u)
            assert 0<l<u<h<1
            assert jl==l/(2*u)
            assert ju==(1-h)/(2*(1-u))
            assert 0<jl and 0<ju and jl+ju<1
            nchecks+=6
            for t in [l,h]:
                a=float(u); v=float(t)
                G=a*v+float(r)*sqrt(a*(1-a)*v*(1-v))
                assert abs(G-min(a,v))<2e-13
                nchecks+=1
            a=float(u); rf=float(r)
            assert abs(raw_derivative(rf,a,float(l))-float(jl))<3e-12
            assert abs(1-raw_derivative(rf,a,float(h))-float(ju))<3e-12
            nchecks+=2
        # Confirm conditional continuous density plus two atoms totals 1,
        # and check its strictly-positive exact analytic lower bound on a grid.
        for i in range(1,23):
            u=i/23
            l,h=cuts(float(s),u)
            jl,ju=jumps(float(s),u)
            cont=simpson(lambda v:density(float(r),u,v),l,h,12800)
            assert abs(cont+jl+ju-1)<3e-7
            nchecks+=1
            for j in range(1,60):
                v=l+(h-l)*j/60
                c=density(float(r),u,v)
                assert c>=1-(1-float(r))**2/4-2e-12
                nchecks+=1
        # Independently integrate each curve's atom density over U.
        a=simpson(lambda u: float(jumps(float(s),u)[0]),0,1,2000)
        b=simpson(lambda u: float(jumps(float(s),u)[1]),0,1,2000)
        assert isclose(a+b,mass(float(r)), rel_tol=0,abs_tol=1e-7)
        assert isclose(a,b,rel_tol=0,abs_tol=1e-8)
        nchecks+=2
    for r in [0.01,0.05,0.2,0.5,0.9,0.99]:
        assert 0<mass(r)<1
        nchecks+=1
    print('PASS:',nchecks,'supplementary exact-rational and numerical checks')
    print('example |rho|=1/2 singular fraction:',format(mass(0.5),'.15f'))


if __name__=='__main__':
    run()
