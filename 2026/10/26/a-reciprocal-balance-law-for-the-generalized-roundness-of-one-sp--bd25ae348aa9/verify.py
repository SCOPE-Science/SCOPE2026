#!/usr/bin/env python3
"""Numerical checks of one-exceptional-arm star negative-type formulas.

Requires Python 3, numpy, scipy, mpmath. This is a finite diagnostic,
not a proof of the universal metric statement.
"""
import math
import numpy as np
from scipy.optimize import brentq
from scipy.linalg import eigvalsh
from mpmath import mp

def threshold(m, t):
    p0 = math.log2(2*m/(m-1))
    def criterion(p):
        h = ((1+t)**p - t**p - 1)/t**(p/2)
        return 2*(2-(2**p)*(m-1)/m)-h*h
    return brentq(criterion,1,p0,xtol=1e-13)

def largest_cnd_eigenvalue(m,t,p):
    weights=[t]+[1.0]*m
    dist=np.zeros((m+2,m+2))
    for k,v in enumerate(weights,1):
        dist[0,k]=dist[k,0]=v
    for i in range(1,m+2):
        for j in range(i+1,m+2):
            dist[i,j]=dist[j,i]=weights[i-1]+weights[j-1]
    D=dist**p
    # Difference coordinates: exceptional coefficient b, each ordinary coefficient a_i;
    # hub coefficient is minus their sum.
    Z=np.vstack((-np.ones(m+1),np.eye(m+1)))
    Q=Z.T@D@Z
    return eigvalsh(Q)[-1]

def run():
    cnt=0
    for m in (2,3,4,6,8,12):
        pmin=math.log2(2*(m+1)/m)
        p0=math.log2(2*m/(m-1))
        for t in (.02,.1,.25,.5,1,2,4,10,50):
            p=threshold(m,t)
            assert pmin-1e-11 <= p < p0
            assert abs(p-threshold(m,1/t))<1e-10
            if t!=1: assert p>pmin+1e-5
            else: assert abs(p-pmin)<1e-12
            for x in (.97,1,1.03):
                pp=p*x
                e=largest_cnd_eigenvalue(m,t,pp)
                if x<1: assert e < 1e-8,(m,t,pp,e)
                if x>1: assert e > 1e-7,(m,t,pp,e)
                if x==1: assert abs(e)<1e-8,(m,t,pp,e)
                cnt+=1
    for p in np.linspace(1.01,1.99,73):
        upper=2**p-2
        for t in np.geomspace(.0001,10000,101):
            h=((1+t)**p-t**p-1)/t**(p/2)
            assert h<=upper+1e-9,(p,t,h,upper)
            cnt+=1
    # Critical asymptotic: high precision needed when t is tiny.
    mp.dps=260
    for m in (2,3,5):
        p0=mp.log(2*m/mp.mpf(m-1),2)
        for l in (30,80,160,320):
            t=mp.e**(-l)
            def cr(p):
                h=((1+t)**p -t**p -1)/t**(p/2)
                return 2*(2-(2**p)*(m-1)/mp.mpf(m))-h*h
            lo=mp.mpf('1'); hi=p0
            for _ in range(1100):
                md=(lo+hi)/2
                if cr(md)>0:lo=md
                else:hi=md
            eps=p0-(lo+hi)/2
            if m>2:
                pred=p0**2/(4*mp.log(2))*t**(2-p0)
                ratio=float(eps/pred)
                if l>=160: assert abs(ratio-1)<0.08,(m,l,ratio)
            else:
                pred=mp.lambertw(l/mp.log(2))/l
                ratio=float(eps/pred)
                if l>=160:assert abs(ratio-1)<0.04,(m,l,ratio)
            cnt+=1
    print('PASS',cnt,'finite checks including spectral, inversion, balanced minimum and asymptotic tests')
if __name__=='__main__':run()
