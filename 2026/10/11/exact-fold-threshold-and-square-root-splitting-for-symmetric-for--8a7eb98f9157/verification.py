#!/usr/bin/env python3
"""Standard-library numerical checks for an exact periodic fold theorem.

These checks do not replace the global analytic proof.
"""
from math import exp, pi, cos, sin, tanh, sqrt

B = 1.0
L = pi
T = 2.0*pi
A1, A3 = 1.0, 0.125
PEAK = A1+A3
N = 32768


def forcing(t):
    return A1*cos(t)+A3*cos(3.0*t)


def rhs(t, x, c):
    return B*abs(x)+forcing(t)-c


def period_map(x, c):
    dt=T/N
    t=0.0
    for _ in range(N):
        k1=rhs(t,x,c)
        k2=rhs(t+dt/2.0,x+dt*k1/2.0,c)
        k3=rhs(t+dt/2.0,x+dt*k2/2.0,c)
        k4=rhs(t+dt,x+dt*k3,c)
        x+=dt*(k1+2*k2+2*k3+k4)/6.0
        t+=dt
    return x


def displacement(u,c):
    return period_map(u,c)-u


def positive_root(c):
    lo,hi=0.0,0.1
    assert displacement(lo,c)<0
    assert displacement(hi,c)>0
    for _ in range(38):
        mid=(lo+hi)/2.0
        if displacement(mid,c)>0:
            hi=mid
        else:
            lo=mid
    return (lo+hi)/2.0


def run():
    cs=B*B/tanh(B*L/2.0)*(A1/(B*B+1.0)+A3/(B*B+9.0))
    assert 0<cs<PEAK
    assert abs(displacement(0.0,cs))<1e-8
    assert displacement(0.0,cs-0.01)>0
    assert displacement(0.0,cs+0.01)<0
    q=1.0/(PEAK-cs)+exp(B*L)/(PEAK+cs)
    hxx=2*B*q
    hc=-2*(1-exp(-B*L))/B
    k=sqrt(-2*hc/hxx)
    eps=1e-4
    u=positive_root(cs+eps)
    assert abs(u/k/sqrt(eps)-1.0)<0.007
    assert abs(displacement(-u,cs+eps))<2e-8
    d=0.0005
    curv=(displacement(d,cs)-2*displacement(0,cs)+displacement(-d,cs))/(d*d)
    assert abs(curv/hxx-1.0)<0.004
    print('CHECK_OK')
    print('threshold',format(cs,'.13g'),'local-coefficient',format(k,'.13g'))
    print('positive-root',format(u,'.13g'),'curvature',format(curv,'.13g'))


if __name__=='__main__':
    run()
