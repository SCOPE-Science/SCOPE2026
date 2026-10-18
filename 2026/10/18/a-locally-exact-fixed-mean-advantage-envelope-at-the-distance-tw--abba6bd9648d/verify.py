#!/usr/bin/env python3
"""Finite sanity checks of a local fixed-mean binomial envelope.
No finite test certifies the infinite-index uniform-gap argument.
"""
import math
from math import comb

def parameters(k):
    d=max(2,(9+math.isqrt(8*k+33))//8)
    a=math.sqrt((k+1)*(k+2)); h=math.sqrt(d*(d-1))
    mu=k+(d*a-k*h)/(a+h)
    return d, mu

def point(r,j,q):
    if j<0 or j>r:return 0.0
    return comb(r,j)*q**j*(1-q)**(r-j)

def diff(k,ell,r,mu):
    q=(mu-ell)/r
    if q<0 or q>1:return None
    return point(r,k+2-ell,q)-point(r,k-ell,q)

def test():
    count=0
    for k in [1,2,3,10,24,60,100]:
        d,mu=parameters(k); m=k+d; q=mu/m
        assert k<mu<k+1
        main=diff(k,0,m,mu)
        assert abs(main)<2.e-12
        count+=2
        rival=-1e6
        for ell in range(k+1):
            for r in range(max(1,k+1-ell),max(120,3*k+80)):
                if (ell,r)==(0,m):continue
                z=diff(k,ell,r,mu)
                if z is not None:rival=max(rival,z)
        assert rival<-1e-9,(k,rival)
        count+=1
        c=point(m,k,q)
        slope=2*c/(m*q*(1-q))
        h=1e-5
        numeric=(diff(k,0,m,mu+h)-diff(k,0,m,mu-h))/(2*h)
        assert abs(numeric-slope)<1e-7,(k,numeric,slope)
        count+=1
    print('passed',count,'finite checks; analytic proof is separate')

if __name__=='__main__':test()
