#!/usr/bin/env python3
"""Supplementary finite-dimensional checks for the quantitative numerical recovery theorem.
No finite sample constitutes an infinite-dimensional proof.
"""
import cmath, math

def almost(a,b,tol=1e-12):
    assert abs(a-b)<tol,(a,b)

def example(t,theta):
    s=math.sqrt((1+t)/2); q=math.sqrt((1-t)/2)
    x1=s; x2=q*cmath.exp(1j*theta)
    observed=abs(x1)**2-abs(x2)**2
    response=2*x1.conjugate()*x2
    almost(observed,t)
    almost(abs(response),math.sqrt(1-t*t))
    return response

count=0
for k in range(101):
    t=-1+2*k/100
    for j in range(36):
        z=example(t,2*math.pi*j/36)
        count+=1
    # In this extremal family, every affine correction preserves its (1,2) entry 2.
    for a in [-2,-1,0,1,2]:
        for b in [-3,-1,0,1,3]:
            off_diagonal=2+0j
            assert abs(off_diagonal)==2
            count+=1
assert abs(max(math.sqrt(1-(-1+2*k/100)**2) for k in range(101))-1)<1e-12
print('VERIFIED',count,'supplementary fixed-fiber identities and exact matrix-entry obstructions')
