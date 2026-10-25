#!/usr/bin/env python3
"""Independent numerical sanity checks of the disk-intersection formulae.

No external packages or external resources required. The analytic proof is separate.
"""
import math

PI = math.pi

def rho(c, t):
    return math.sqrt(1.0 - c*c*math.sin(t)**2) - c*math.cos(t)

def roots(r, p, q, n):
    h = PI/n
    s = q/(p+q)
    lo = 1.0-r
    hi = math.sqrt(1.0-r*r*math.sin(h)**2)-r*math.cos(h)
    def angle(c):
        return math.acos(max(-1.0,min(1.0,(1.0-r*r-c*c)/(2.0*r*c))))
    def equation(c):
        return r*math.sin(angle(c))-s*rho(c,h)*math.sin(h)
    a,b=lo,hi
    for _ in range(90):
        m=(a+b)/2
        if equation(m)<0:
            a=m
        else:
            b=m
    c=(a+b)/2
    return c,lo,hi,angle(c)

def integrate(f,a,b,subdivisions=512):
    n=subdivisions
    step=(b-a)/n
    total=f(a)+f(b)
    for j in range(1,n):
        total+=(4 if j%2 else 2)*f(a+step*j)
    return step*total/3.0

def error(c,r,p,q,n):
    h=PI/n
    if c<=0:
        alpha=0.0
    else:
        z=(1-r*r-c*c)/(2*r*c)
        alpha=math.acos(max(-1,min(1,z))) if -1<z<1 else (0 if z>=1 else h)
    alpha=max(0.0,min(h,alpha))
    f=lambda t:rho(c,t)**2-r*r
    return n*(p*integrate(lambda t:max(-f(t),0),0,alpha) + q*integrate(lambda t:max(f(t),0),alpha,h))

for r,p,q in [(0.5,1.0,1.0),(0.27,2.0,5.0),(0.8,4.0,1.0)]:
    s=q/(p+q)
    previous=None
    for n in [8,16,32,64,128]:
        c,lo,hi,a=roots(r,p,q,n)
        assert lo<c<hi and 0<a<PI/n
        h=PI/n
        assert abs(r*math.sin(a)-s*rho(c,h)*math.sin(h))<1e-12
        val=error(c,r,p,q,n)
        span=hi-lo
        for offset in [-0.2,-0.05,0.05,0.2]:
            ctest=c+span*offset
            if lo<ctest<hi:
                assert val<=error(ctest,r,p,q,n)+1e-10
        pred=PI**3*r*r*(1-r)*(p+q)*s*(1-s*s)/(3*n*n)
        if n>=32:
            assert abs(val/pred-1.0)<0.025
        if n>=64:
            base=r*(1-r)*PI*PI*s*s/(2*n*n)
            assert abs((c-(1-r))/base-1)<0.025
        if previous is not None:
            assert val<previous
        previous=val
print('All deterministic numerical sanity checks passed (not a proof).')
