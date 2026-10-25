#!/usr/bin/env python3
"""Numerical consistency checks for the opposite-corner reflected-square distance.
Only the Python standard library is needed; finite checks do not constitute a proof.
"""
import math


def one_dim(t, z, K=70):
    return 1.0 + 2.0 * sum(math.exp(-math.pi**2*k*k*t)*math.cos(k*math.pi*z) for k in range(1,K+1))


def series(t, K=70):
    a = lambda k: math.exp(-math.pi**2*k*k*t)
    odd = list(range(1,K+1,2))
    even = list(range(2,K+1,2))
    return (16/math.pi**2)*(sum(a(k)/k**2 for k in odd)
                -2*sum(a(k)*a(l)/(l*l-k*k) for k in odd for l in even))


def integral(t, N=10000):
    # Composite trapezoid for F(x)=int_0^x p(z) dz and p(x)F(1-x).
    p = [one_dim(t,j/N) for j in range(N+1)]
    F = [0.0]*(N+1)
    for j in range(1,N+1):
        F[j] = F[j-1]+(p[j-1]+p[j])/(2*N)
    h = [p[j]*F[N-j] for j in range(N+1)]
    return 2*(sum(h)-0.5*(h[0]+h[-1]))/N-1


def check():
    for t in (0.025,0.05,0.1,0.25,0.5):
        a, b = series(t), integral(t)
        assert abs(a-b) < 7e-8,(t,a,b)
        assert 0<a<1
        for x,y in ((.1,.2),(.2,.6),(.4,.5),(.65,.75),(.2,.8)):
            d=one_dim(t,x)*one_dim(t,y)-one_dim(t,1-x)*one_dim(t,1-y)
            if abs(x+y-1)>1e-12: assert d*(1-x-y)>-1e-10,(t,x,y,d)
        print('t=',t,'spectral=',format(a,'.12f'),'triangular quadrature=',format(b,'.12f'))
    for t in (.1,.2,.3):
        first = 16/math.pi**2*math.exp(-math.pi**2*t)
        second = -32/(3*math.pi**2)*math.exp(-5*math.pi**2*t)
        print('large t',t,'distance',series(t),'two terms',first+second)
    for t in (.01,.015,.02):
        tiny = 8*math.sqrt(2/math.pi)*math.sqrt(t)*math.exp(-1/(8*t))
        print('small t',t,'deficit=',1-series(t),'leading asymptotic=',tiny)

if __name__=='__main__': check()
