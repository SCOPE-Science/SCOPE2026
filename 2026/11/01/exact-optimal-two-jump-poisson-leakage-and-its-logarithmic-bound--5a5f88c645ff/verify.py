#!/usr/bin/env python3
"""Numerical cross-checks for circle Poisson boundary leakage; not a proof."""
import math

PI=math.pi

def kernel(t,r):
    return (1-r*r)/(1-2*r*math.cos(t)+r*r)

def simpson(f,a,b,n=16000):
    if n%2: raise ValueError("n must be even")
    h=(b-a)/n
    return h/3*(f(a)+f(b)+4*sum(f(a+h*j) for j in range(1,n,2))+2*sum(f(a+h*j) for j in range(2,n,2)))

def leakage(ell,r):
    return 4*ell-4/PI*simpson(lambda t:(ell-t)*kernel(t,r),0,ell)

def fourier(r,n=20000):
    return 2*PI-16/PI*sum(r**(2*j+1)/(2*j+1)**2 for j in range(n))

for r in (0.,0.3,0.7):
    q=leakage(PI,r)
    assert abs(q-fourier(r))<2.e-8,(r,q,fourier(r))
    assert q>leakage(PI/2,r) and q>leakage(3*PI/2,r)
    h=0.001
    gap=q-leakage(PI+h,r)
    c=(2/PI)*(1-r)/(1+r)
    assert abs(gap/(h*h)-c)<0.001,(r,gap/(h*h),c)
print("CHECK_OK: Fourier/arc integral, strict maximum and local coefficient (sampled parameters)")
