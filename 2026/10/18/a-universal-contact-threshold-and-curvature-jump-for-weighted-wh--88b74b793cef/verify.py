#!/usr/bin/env python3
"""Reproduce the weighted-wheel John ellipsoid contact and determinant formulas.

Uses only the Python standard library. The independent SPD optimization comparison
is in verify_unrestricted.py (which uses numpy/scipy).
"""
import math

TOL=3e-9

def root_q(m,t):
    if t <= 1/math.sqrt(2):
        return 0.0
    lo,hi=0.0,1.0
    for _ in range(110):
        q=(lo+hi)/2
        f=(1+q**m)/(2*(1-q)*(1-q**(m-1)))
        if f<t*t:lo=q
        else:hi=q
    return (lo+hi)/2

def construct(m,t):
    q=root_q(m,t)
    if q == 0:
        alpha=1/(t*t); beta=0.0
    else:
        beta=2*q*(1-q**(m-1))/((1+q)*(1-q**m))
        alpha=beta*(1-q)**2/q
    eig=[alpha+beta*(2-2*math.cos(2*math.pi*k/m)) for k in range(m)]
    diag=sum(1/u for u in eig)/m
    rim=sum((2-2*math.cos(2*math.pi*k/m))/u for k,u in enumerate(eig))/m
    detlog=-sum(math.log(u) for u in eig)
    if q:
        detlog_closed=m*math.log((1+q)/2)+m*math.log((1-q**m)/(1-q**(m-1)))-2*math.log(1-q**m)
    else:
        detlog_closed=2*m*math.log(t)
    return q,alpha,beta,diag,rim,detlog,detlog_closed

def check():
    count=0
    for m in range(3,26):
        for t in [0.5,0.6,1/math.sqrt(2),0.72,0.8,0.95,1.,1.25,1.5,2.,4.,10.]:
            q,a,b,d,r,z,w=construct(m,t)
            assert 0<=q<1 and a>0 and b>=0
            assert abs(a*t*t+b-1)<TOL
            assert abs(d-t*t)<TOL
            assert abs(z-w)<TOL
            if t<=1/math.sqrt(2):
                assert b==0. and r<=1+TOL
            else:
                assert b>0 and abs(r-1)<TOL
            count+=1
    # Exact boundary curvatures in the variable y=t^2 from cycle adjacency moments:
    for m in range(3,50):
        lam=[2-2*math.cos(2*math.pi*k/m) for k in range(m)]
        assert abs(sum(lam)/m-2)<TOL
        assert abs(sum((z-2)**2 for z in lam)/m-2)<TOL
    print('VERIFY_OK',count,'parameter configurations and 47 boundary-moment identities')

if __name__=='__main__':check()
