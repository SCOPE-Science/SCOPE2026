#!/usr/bin/env python3
"""Reproducible finite cross-checks for exact phase-locked winding identities."""
from fractions import Fraction as Q
import math, cmath

def matrix_eigenvalues(trace, determinant):
    return ((trace+cmath.sqrt(trace*trace-4*determinant))/2,
            (trace-cmath.sqrt(trace*trace-4*determinant))/2)

def check(m):
    delta=Q(1,100*(m+1)**2)
    t=Q(1,2*m+1)
    k=t*(1+delta)
    cent=Q(2*m*(m+1),2*m+1)
    assert Q(0)<k<Q(1,2)
    assert cent/m==1+t and cent/(m+1)==1-t
    assert (1+k)*(m-1)<cent <(1-k)*(m+2)
    assert Q(1,10000*(m+1)**2)>Q(0)
    sqfactor=k*k-t*t
    assert sqfactor==t*t*(2*delta+delta*delta)>0
    assert (math.pi**2/m**2)*(1/50+1/(10000*(m+1)**2))<1
    for winding,cosphase in [(m,-1/(1+float(delta))),(m+1,1/(1+float(delta)))]:
        U=2*math.pi*winding
        A=2*math.pi*float(cent)
        theta=math.acos(cosphase)
        assert abs(U-(A+float(k)*U*math.cos(theta)))<1e-10*(1+U)
        r=float(cent/winding)
        S=U*math.sqrt(float(sqfactor))
        assert 0<S<r
        trace=2-r
        determinant=1-r+S
        assert S>0 and (4-2*r+S)>0 and (r-S)>0
        eig=matrix_eigenvalues(trace,determinant)
        assert max(map(abs,eig))<1-1e-9,(m,winding,eig)
        bad_det=1-r-S
        bad_eig=matrix_eigenvalues(trace,bad_det)
        assert max(e.real for e in bad_eig)>1
        # Numerical local trajectory diagnostic; no infinite-time claim relies on this loop.
        u=U+1e-6
        ang=theta+1e-6
        for step in range(2500):
            u,ang=A+float(k)*u*math.cos(ang),(ang+u)%(2*math.pi)
        assert abs(u-U)<1e-6, (m,winding,u-U)
        assert min(abs(ang-theta),abs(ang-theta-2*math.pi),abs(ang-theta+2*math.pi))<1e-6, (m,winding,ang-theta,max(map(abs,eig)))
    return True

if __name__=='__main__':
    values=(1,2,3,4,5,6,10,12,25,50,100,200,1000)
    for m in values:
        check(m)
    print('PASS: exact-rational coexistence and exclusion identities, finite Schur and orbit checks at',len(values),'winding indices')
