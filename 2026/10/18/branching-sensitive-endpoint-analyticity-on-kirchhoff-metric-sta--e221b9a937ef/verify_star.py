#!/usr/bin/env python3
"""Numerical checks for the Kirchhoff star heat-derivative endpoint theorem.

All proofs of infinite statements are analytic; this checks finite quadratures,
Gaussian scaling, inequalities, and the reciprocal-degree pattern.
Uses the Python standard library only.
"""
from math import exp, sqrt, pi, isfinite

def g(z):
    return exp(-z*z/4)/(2*sqrt(pi))

def q(z):
    return (z*z/4-0.5)*g(z)

def simpson(fun, a, b, n=6000):
    if n % 2:
        n += 1
    h=(b-a)/n
    total=fun(a)+fun(b)
    for k in range(1,n):
        total+=(4 if k%2 else 2)*fun(a+h*k)
    return total*h/3

def F(m,x,n=6000):
    alpha=1.0 if m is None else 1.0-2.0/m
    return simpson(lambda y: abs(q(x-y)-alpha*q(x+y))+(1+alpha)*abs(q(x+y)),0,max(22,x+15),n)

def direct_row(m,t,x,n=6000):
    # Integral of t|time-derivative kernel| across all outgoing rays.
    alpha=1-2/m
    h=lambda z: (z*z/(4*t)-0.5)*exp(-z*z/(4*t))/(2*sqrt(pi*t))
    return simpson(lambda y: abs(h(x-y)-alpha*h(x+y))+(1+alpha)*abs(h(x+y)),0,max(22*sqrt(t),x+15*sqrt(t)),n)

def maxgrid(m):
    # Golden section search is exploratory only, not a uniqueness proof.
    a,b=1.2,1.8
    ratio=(sqrt(5)-1)/2
    c=b-ratio*(b-a);d=a+ratio*(b-a)
    fc=F(m,c,6000);fd=F(m,d,6000)
    for _ in range(34):
        if fc>=fd:
            b,d,fd=d,c,fc
            c=b-ratio*(b-a);fc=F(m,c,6000)
        else:
            a,c,fc=c,d,fd
            d=a+ratio*(b-a);fd=F(m,d,6000)
    x=(a+b)/2
    return F(m,x,8000),x

def D_at(x,n=16000):
    return 4*simpson(lambda y: abs(q(x+y)) if q(x+y)*(q(x-y)-q(x+y))<0 else 0.,0,max(22,x+15),n)

def main():
    checks=0
    c2=sqrt(2/pi)*exp(-0.5)
    for x in [0.,.17,.75,sqrt(2),1.49,2.6,5.]:
        assert abs(F(2,x)-c2)<1.5e-6,(x,F(2,x),c2)
        checks+=1
        vals=[F(m,x) for m in [2,3,4,10,100,None]]
        assert all(a<=b+2.e-7 for a,b in zip(vals,vals[1:])),(x,vals)
        checks+=1
        assert vals[-1]-vals[2] <=2*c2/4+2e-6,(x,vals)
        checks+=1
        for m in [3,4,10]:
            assert abs(direct_row(m,.31,x*sqrt(.31))-F(m,x))<3.e-7,(m,x)
            checks+=1
            assert abs(direct_row(m,1.73,x*sqrt(1.73))-F(m,x))<3.e-7,(m,x)
            checks+=1
    j=sqrt(2)/(4*sqrt(pi))*(exp(-.5)-3*exp(-4.5))
    for m in [3,4,10,100]:
        assert F(m,sqrt(2))>c2+2*(1-2/m)*j-1e-7
        checks+=1
    maxima=[maxgrid(m) for m in [3,4,10,100,1000,None]]
    assert all(maxima[i][0]<maxima[i+1][0] for i in range(5)),maxima
    checks+=1
    cinf,xinf=maxima[-1]
    k=D_at(xinf)
    assert .713<cinf<.717 and .46<k<.47,(cinf,xinf,k)
    checks+=1
    for m in [100,1000]:
        cm=maxgrid(m)[0]
        assert 0<(cinf-cm)<2*c2/m+0.0001,(m,cinf-cm)
        checks+=1
    print('PASS: %d deterministic finite checks' % checks)
    print('C2=%.12f; C3~=%.12f; C_infinity~=%.12f;' % (c2,maxima[0][0],cinf))
    print('maximizer x_infinity~=%.6f; kappa~=%.9f (exploratory quadrature)' %(xinf,k))

if __name__=='__main__':
    main()
