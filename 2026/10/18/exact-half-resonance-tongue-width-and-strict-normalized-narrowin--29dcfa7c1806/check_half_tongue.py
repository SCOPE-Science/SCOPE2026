#!/usr/bin/env python3
"""Numerical and asymptotic checks of an analytic width identity."""
import math
from scipy.optimize import brentq, minimize_scalar

def dk(m,k):
    return brentq(lambda d: 2*d-k*math.cos(m)*math.cos(d),0.0,k/2+1e-8) if m<math.pi/2 else 0.0

def width_from_midpoint(k):
    f=lambda m: math.sin(2*m)*(math.sin(2*dk(m,k))/(2*dk(m,k)) if m<math.pi/2 else 1.)
    sol=minimize_scalar(lambda m:-f(m),bounds=(0,math.pi/2),method='bounded',options={'xatol':1e-14})
    return k*k/(4*math.pi)*f(sol.x),sol.x

def width_from_separation(k):
    rhs=lambda d: 4*d/(math.cos(d)**2)*(d/(math.cos(d)**2)+math.tan(d))
    d=brentq(lambda d:rhs(d)-k*k,1e-15,.7)
    W=math.sin(d)*math.sqrt(k*k-4*d*d/(math.cos(d)**2))/math.pi
    return W,d

for k in (0.05,0.1,0.2,0.5,0.8,0.95,0.999):
    w,m=width_from_midpoint(k); v,d=width_from_separation(k)
    assert abs(w-v)<2e-12,(k,w,v)
    ratio=w*4*math.pi/(k*k)
    pred=1-k*k/12+23*k**4/1440
    print('K=%.3f W=%.14g R=%.14g delta*=%.12g m*=%.12g approxR=%.14g'%(k,w,ratio,d,m,pred))
    assert 0<ratio<1
assert all(width_from_separation(k)[0]/k**2 > width_from_separation(k+.01)[0]/(k+.01)**2 for k in (.1,.25,.5,.8,.98))
print('CHECK_OK')

def lift(x,k,o):
    return x+2*math.pi*o-k*math.sin(x)

def residual(x,k,o):
    return lift(lift(x,k,o),k,o)-x-2*math.pi

def count_simple_roots(k,o,N=4000):
    xs=[2*math.pi*i/N for i in range(N+1)]
    vals=[residual(x,k,o) for x in xs]
    roots=[]
    for i in range(N):
        if vals[i]*vals[i+1]<0:
            roots.append(brentq(lambda x:residual(x,k,o),xs[i],xs[i+1]))
    return roots
k=.8; w,_=width_from_separation(k)
for off in (w/10,w/4,0.51*w):
    rr=count_simple_roots(k,.5+off)
    print('omega=%.12f period2 points=%d roots=%s'%(.5+off,len(rr),[round(z,6) for z in rr]))
    assert len(rr)==(4 if off < w/2 else 0)
print('DIRECT_ITERATE_OK')
