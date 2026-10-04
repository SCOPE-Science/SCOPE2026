#!/usr/bin/env python3
import math


def G(k, d, ell):
    u = k * ell
    x = k * d
    return (2.0*u*u/(math.cos(x/2.0)**2) + (3.0*u**4 + 10.0*u*u + 3.0)*math.cos(x))/((u*u-1.0)**2)


def bisect(f, a, b, steps=100):
    fa, fb = f(a), f(b)
    if not (math.isfinite(fa) and math.isfinite(fb) and fa*fb <= 0.0):
        raise AssertionError((a, b, fa, fb))
    for _ in range(steps):
        c = (a+b)/2.0
        fc = f(c)
        if fa*fc <= 0.0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    return (a+b)/2.0


def period_measure(n, d, ell):
    # One phase period k in [2*pi*n/d, 2*pi*(n+1)/d].
    def gx(x):
        return G((2.0*math.pi*n+x)/d, d, ell)
    eps = 1e-10
    a = 2.0*math.pi/3.0
    b = 4.0*math.pi/3.0
    r0 = bisect(lambda x: gx(x)-3.0, eps, 0.5)
    lo_l = bisect(lambda x: gx(x)+1.5, a+1e-6, math.pi-1e-5)
    hi_l = bisect(lambda x: gx(x)-3.0, lo_l+1e-8, math.pi-1e-8)
    hi_r = bisect(lambda x: gx(x)-3.0, math.pi+1e-8, b-1e-6)
    lo_r = bisect(lambda x: gx(x)+1.5, hi_r+1e-8, b-1e-8)
    rend = bisect(lambda x: gx(x)-3.0, 2.0*math.pi-0.5, 2.0*math.pi-eps)
    return ((a-r0) + (hi_l-lo_l) + (lo_r-hi_r) + (rend-b))/d


def check_factorizations():
    for u in (5.0, 11.0, 37.0):
        for c in (-0.8, -0.2, 0.4, 0.9):
            if abs(1.0+c) < 1e-12:
                continue
            g = (4.0*u*u/(1.0+c) + (3.0*u**4+10.0*u*u+3.0)*c)/((u*u-1.0)**2)
            lhs3 = (1.0+c)*(u*u-1.0)**2*(g-3.0)
            rhs3 = ((u*u+3.0)*c-u*u+3.0)*((3.0*u*u+1.0)*c+3.0*u*u-1.0)
            if abs(lhs3-rhs3) > 1e-8*max(1.0, abs(rhs3)):
                raise AssertionError((u,c,lhs3,rhs3))
            lhslo = 2.0*(1.0+c)*(u*u-1.0)**2*(g+1.5)
            rhslo = (2.0*c+1.0)*(3.0*c*u**4+10.0*c*u*u+3.0*c+3.0*u**4+2.0*u*u+3.0)
            if abs(lhslo-rhslo) > 1e-8*max(1.0, abs(rhslo)):
                raise AssertionError((u,c,lhslo,rhslo))


def check_asymptotics():
    for d, ell in ((1.0,1.0),(5.0,1.0),(2.3,0.7)):
        target = 4.0/(math.sqrt(3.0)*math.pi*ell)
        vals=[]
        for n in (40,80,160,320):
            w=period_measure(n,d,ell)
            vals.append(n*(4.0*math.pi/(3.0*d)-w))
        if abs(vals[-1]-target) > 0.02/ell:
            raise AssertionError((d,ell,target,vals))
        if abs(vals[-1]-target) >= abs(vals[0]-target):
            raise AssertionError((d,ell,target,vals))


def check_cumulative():
    d=1.7; ell=0.9
    coeff=4.0/(math.sqrt(3.0)*math.pi*ell)
    # On exact full-period endpoints, the corrected residual should remain bounded.
    for N in (80,160,320):
        total=sum(period_measure(n,d,ell) for n in range(20,N+1))
        leading=(N-19)*4.0*math.pi/(3.0*d)
        corr=coeff*sum(1.0/n for n in range(20,N+1))
        residual=total-leading+corr
        if abs(residual) > 0.25:
            raise AssertionError((N,residual))


if __name__ == '__main__':
    check_factorizations()
    check_asymptotics()
    check_cumulative()
    print('VERIFY_OK')
