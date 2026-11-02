#!/usr/bin/env python3
"""Finite numerical consistency checks for the stated Gabor-frame formulas.
This is not a proof of the analytic continuum theorem.
"""
import math
import cmath

PI=math.pi

def sq_zak(w,x,omega):
    q=math.exp(-2*PI*w)
    a=2*PI*w
    s=math.sinh(a*(1-omega))
    t=math.sinh(a*omega)
    den=1-2*q*math.cos(2*PI*x)+q*q
    return (2*PI*q/w)**2*(s*s+t*t+2*s*t*math.cos(2*PI*x))/den**2

def lower(w,d):
    q=math.exp(-2*PI*w)
    c=abs(math.cos(PI*d))
    return 4*PI**2*q*(1-q)**2*(1-c)/(w*w*(1+q*q+2*q*c)**2)

def upper_half(w):
    tanh=math.tanh(PI*w)
    return PI**2/(w*w)*(tanh*tanh+1/(tanh*tanh))

def edge(w,x): return sq_zak(w,x,0)

def mid(w,x): return sq_zak(w,x,.5)

def near(a,b,tol=1e-8):
    return abs(a-b)<=tol*max(1,abs(a),abs(b))

for w in (.2,.7,1.,2.):
    for x,omega in ((.17,.23),(.37,.82),(.5,.5),(0.,0.)):
        N=20000
        exact=sum((cmath.exp(2j*PI*n*omega)/((x-n)**2+w*w)
                   for n in range(-N,N+1)))
        assert near(abs(exact)**2,sq_zak(w,x,omega),tol=3e-4), (w,x,omega)
    for d in (.07,.17,.36,.5,.71,.93):
        x=(1+d)/2 if d<=.5 else d/2
        attained=mid(w,x)+mid(w,x-d)
        assert near(attained,lower(w,d),tol=1e-9), (w,d,attained,lower(w,d))
        for k in range(127):
            xx=k/127
            assert mid(w,xx)+mid(w,xx-d)>=attained-1e-8*max(1,attained)
        assert lower(w,d)<=lower(w,.5)*(1+1e-12)
        if d!=.5:
            assert edge(w,0)+edge(w,d)>upper_half(w)
    actual_upper=max(edge(w,k/6000)+edge(w,k/6000-.5) for k in range(6000))
    assert near(actual_upper,upper_half(w),tol=1e-9)
    d=1e-5
    q=math.exp(-2*PI*w)
    coef=2*PI**4*q*(1-q)**2/(w*w*(1+q)**4)
    assert abs(lower(w,d)/(coef*d*d)-1)<1e-5
print('CHECK_OK: Poisson Zak identity, sharp lower fibers, balanced upper fibers, quadratic edge')
