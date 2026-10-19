#!/usr/bin/env python3
"""Independent finite-length numerical diagnostics of homogeneous nonlinear transport."""
import math

def trajectory(j,r,n):
    x=0.0
    arr=[0.0]
    for i in range(n+1):
        if x >= 1 or 1-x**r <= 0: return float('inf'),arr
        x=j/(1-x**r)
        arr.append(x)
    return x,arr

def flux(n,r):
    s=(r+1)**(-1/r); jstar=r*s/(r+1)
    lo,hi=jstar,1.0
    for _ in range(65):
        mid=(lo+hi)/2
        val,_=trajectory(mid,r,n)
        if val>1:hi=mid
        else:lo=mid
    val,seq=trajectory((lo+hi)/2,r,n)
    return (lo+hi)/2,seq

def run():
    for r in (2,3,5):
        s=(r+1)**(-1/r); js=r*s/(r+1); C=2*math.pi**2*r*s/(r+1)**2
        for n in (200,500,1000):
            j,seq=flux(n,r)
            assert j>js and j<1
            scaled=n*n*(j-js)
            assert abs(scaled/C-1)<0.09,(r,n,scaled,C)
            for t in (0.2,0.5,0.8):
                k=int(t*(n+1))
                observed=n*(seq[k]-s)
                expected=-2*math.pi*s/(r+1)/math.tan(math.pi*t)
                assert abs(observed-expected)<0.09,(r,n,t,observed,expected)
            print('r=',r,'n=',n,'normalised-current=',format(scaled,'.8f'),'limit=',format(C,'.8f'))
    print('DIAGNOSTICS_PASS')
if __name__=='__main__':run()
