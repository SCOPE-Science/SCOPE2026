"""Standalone numerical checks for concentric staggered polygon microscopic weights.
Requires numpy, scipy and mpmath. All dimensions are finite; proof is analytic.
"""
import math
import numpy as np
from scipy.optimize import brentq
from scipy.spatial import ConvexHull
import mpmath as mp

def data(n,r):
    s=2/math.tan(math.pi/(2*n))
    ang=(2*np.arange(n)+1)*math.pi/n
    c=float(np.sqrt(1+r*r-2*r*np.cos(ang)).sum())
    a=r*s
    denom=n*(a+s-2*c)
    return a,s,c,(s-c)/denom,(a-c)/denom

def dist_matrix(n,r):
    k=np.arange(n); z=np.concatenate([r*np.exp(2j*np.pi*k/n),np.exp(2j*np.pi*(k+0.5)/n)])
    return np.abs(z[:,None]-z[None,:])

def run():
    ncheck=0
    for n in (4,5,6,8,12,20):
        threshold=brentq(lambda r:data(n,r)[2]-data(n,r)[1],0,1,xtol=1e-14)
        assert 0<threshold<1
        for r in (threshold*.5,threshold*.9,threshold*1.1, (1+threshold)/2, 1.):
            if r>=1.0: r=1.0
            a,b,c,x,y=data(n,r)
            D=dist_matrix(n,r)
            assert abs(n*(x+y)-1)<1e-12
            assert np.max(np.abs(D@np.r_[np.full(n,x),np.full(n,y)]-(a*x+c*y)))<2e-12
            assert y>0
            assert (x<0)==(r<threshold)
            assert a+b-2*c<0
            # Independent full linear solve, without assuming orbit constancy.
            v=np.linalg.solve(D,np.ones(2*n));v=v/v.sum()
            assert np.max(abs(v[:n]-x))<1e-10
            assert np.max(abs(v[n:]-y))<1e-10
            ncheck+=7
    for n in (4,5,6,8,12):
        threshold=brentq(lambda r:data(n,r)[2]-data(n,r)[1],0,1)
        t0=math.cos(math.pi/n)
        assert data(n,t0)[2] < data(n,t0)[1]
        t=(t0+threshold)/2
        vertices=np.r_[t*np.exp(2j*np.pi*np.arange(n)/n),np.exp(2j*np.pi*(np.arange(n)+.5)/n)]
        hull=ConvexHull(np.c_[vertices.real,vertices.imag])
        assert len(hull.vertices)==2*n
        x,y=data(n,t)[3:5]
        assert x<0<y
        ncheck+=5
    for n in (4,6):
        t=(math.cos(math.pi/n)+brentq(lambda r:data(n,r)[2]-data(n,r)[1],0,1))/2
        D=dist_matrix(n,t)
        zeta=np.exp(-1e-4*D)
        v=np.linalg.solve(zeta,np.ones(2*n))
        v=v/v.sum()
        x,y=data(n,t)[3:5]
        assert np.max(abs(v[:n]-x)) < 1e-3
        assert np.max(abs(v[n:]-y)) < 1e-3
        ncheck+=2
    mp.mp.dps=35
    for n in (3,4,5,10,20,40,80,160,320):
        angles=[(2*k+1)*mp.pi/n for k in range(n)]
        cc=lambda r:mp.fsum(mp.sqrt(1+r*r-2*r*mp.cos(t)) for t in angles)
        s=2*mp.cot(mp.pi/(2*n))
        lo,hi=mp.mpf(0),mp.mpf(1)
        for _ in range(90):
            mid=(lo+hi)/2
            if cc(mid)<s:lo=mid
            else:hi=mid
        root=(lo+hi)/2
        assert abs(cc(root)-s)<mp.mpf('1e-20')
        if n==3:assert abs(root-(3-4*mp.sqrt(3)/3))<mp.mpf('1e-20')
        eps=mp.pi/(2*n)
        assert abs(cc(1)-2/mp.sin(eps))<mp.mpf('1e-20')
        assert (1-root)*n*n > mp.pi**2/4
        if n>=40:assert abs((1-root)*n*n-mp.pi**2/4)<mp.mpf('0.01')
        ncheck+=4
    print('PASS:',ncheck,'independent row, direct linear solve, sign, threshold, and asymptotic checks.')
    print('n=4 critical radius:',format(brentq(lambda r:data(4,r)[2]-data(4,r)[1],0,1),'.12f'))
    print('n=3 closed form:',float(3-4*mp.sqrt(3)/3))
    print('limit n^2(1-r_n):',math.pi**2/4)
if __name__=='__main__':run()
