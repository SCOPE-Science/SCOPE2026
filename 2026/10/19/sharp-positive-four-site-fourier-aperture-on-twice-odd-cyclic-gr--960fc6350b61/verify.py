#!/usr/bin/env python3
"""Reproduce supplementary finite moment checks for the stated cyclic quadrature."""
from math import ceil,cos,pi
from cmath import exp

def weights(N):
    assert N>=6 and N%4==2
    D=(3*N+3)//4
    u=cos(pi*(N-D)/N)
    v=cos(pi*(N-D+2)/N)
    alpha=(0.5-v*v)/(u*u-v*v)
    assert 0<alpha<1
    w={}
    for j in (0,D,N//2,D-N//2):
        w[j]=w.get(j,0.0)+alpha/4
    for j in (1,D-1,N//2+1,D-N//2-1):
        w[j]=w.get(j,0.0)+(1-alpha)/4
    return D,w

def main():
    checked=0
    for N in range(6,1000,4):
        D,w=weights(N)
        assert D==ceil(3*N/4)
        assert min(w.values())>0 and 0 in w and D in w
        assert all(0<=j<=D for j in w)
        assert len(w)<=8
        assert abs(sum(w.values())-1)<1e-12
        for k in (1,2,3):
            moment=sum(t*exp(2j*pi*k*j/N) for j,t in w.items())
            assert abs(moment)<3e-12,(N,k,moment)
            checked+=1
    print('VERIFY_OK', checked, 'first-three-moment comparisons; all N=4q+2 from 6 through 998')
if __name__=='__main__':main()
