#!/usr/bin/env python3
"""Finite diagnostic checks for the signed Huygens-tree Melnikov coefficient.

Requires only the Python standard library. Numerical checks supplement the proof;
finite truncation alone does not certify infinite-series claims.
"""
import math

K=((2,1,1,1,1),(1,2,1,0,0),(1,1,2,0,0),
   (1,0,0,2,1),(1,0,0,1,2))
assert all(K[i][j]==K[j][i] for i in range(5) for j in range(5))
for alpha in (0.7,1.,1.3):
    for u,v in ((0.34,1.37),(-2.3,0.71),(2.22,-0.87)):
        z=[u,v,v,v,v]
        A=[alpha,1,1,1,1]
        changes=[sum(K[i][j]*A[j]*math.sin(z[j]) for j in range(5)) for i in range(5)]
        assert max(abs(changes[i]-changes[1]) for i in range(2,5))<1e-13
        assert abs(changes[0]-(2*alpha*math.sin(u)+4*math.sin(v)))<1e-13
        assert abs(changes[1]-(alpha*math.sin(u)+3*math.sin(v)))<1e-13

def inverse(v,h):
    low,high=0.,v
    for _ in range(62):
        mid=(low+high)*0.5
        if mid+2*h*math.sin(mid)>v:high=mid
        else:low=mid
    return (low+high)*0.5

def coefficient(h,v0):
    v=v0; past=[]
    for _ in range(1200):
        v=inverse(v,h); past.append(v)
        if v<1e-13: break
    else: raise AssertionError('negative tail did not converge')
    v=v0; future=[]
    for _ in range(1200):
        future.append(v)
        v=v+2*h*math.sin(v)
        if math.pi-v<1e-13:break
    else: raise AssertionError('positive tail did not converge')
    unstable=0.
    for v in reversed(past):
        unstable=(1-h*math.cos(v))*unstable-h*math.sin(v)
    stable=0.
    for v in reversed(future):
        stable=(stable+h*math.sin(v))/(1-h*math.cos(v))
    assert unstable<0<stable
    assert 0 < inverse(v0,h) < v0 < v0+2*h*math.sin(v0) < math.pi
    return stable-unstable

for h,expected in ((0.05,1.1987022757871495),
                   (0.1,1.200387898150952),
                   (0.2,1.2071211539424944)):
    assert 0<h<2/(5+math.sqrt(17))
    assert 0<1-h<1<1+2*h
    assert 0<1-2*h<1<1+h
    value=coefficient(h,math.pi/2)
    assert abs(value-expected)<3e-9,(h,value,expected)
    print('h=',h,'Melnikov=',format(value,'.12f'),'PASS')
print('Finite algebra and convergence diagnostics passed.')
