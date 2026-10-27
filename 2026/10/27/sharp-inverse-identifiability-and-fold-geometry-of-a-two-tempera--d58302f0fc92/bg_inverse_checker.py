#!/usr/bin/env python3
"""Numerical cross-checks for inverse torque/rotation tomography of a harmonic Brownian gyrator.

This script compares forward formulas with direct Lyapunov solvers, numerical
angular integration, and the algebraic inverse. Requires numpy and scipy.
"""
import numpy as np
from math import sqrt, pi
from scipy.linalg import solve_continuous_lyapunov
from scipy.integrate import quad


def observables(a, b, c, t1, t2):
    K=np.array([[a,c],[c,b]],dtype=float)
    D=np.diag([t1,t2]); S=solve_continuous_lyapunov(K,2*D)
    M = c*(S[0,0]-S[1,1])+(b-a)*S[0,1]
    V = S[0,0]-S[1,1]
    B = D @ np.linalg.inv(S)-K
    # Parameterize the normal current by a unit radial direction;
    # integrate radial density exactly to obtain an angle-only integral.
    Sinv=np.linalg.inv(S)
    def angular(theta):
        x=np.array([np.cos(theta),np.sin(theta)])
        return (x[0]*(B@x)[1]-x[1]*(B@x)[0])/(2*pi*sqrt(np.linalg.det(S))*(x@Sinv@x))
    W=quad(angular,0,2*pi,epsabs=3e-12,epsrel=3e-12,limit=300)[0]
    return M,W,V,S


def predicted(a,b,c,t1,t2):
    L=a+b; P=a*b-c*c; dt=t1-t2
    M=2*c*dt/L
    W=-c*dt*sqrt(P)/sqrt(t1*t2*L*L+c*c*dt*dt)
    V= dt*(L*L-4*c*c)/(2*L*P)-(t1+t2)*(a-b)/(2*P)
    return M,W,V


def inverse(L,t1,t2,M,W,V=None):
    dt=t1-t2
    if M==0:
        assert W==0
        if V is None:return None
        # solve V=t1/a-t2/(L-a) by monotone bisection
        from scipy.optimize import brentq
        a=brentq(lambda a:t1/a-t2/(L-a)-V,1e-13*L,L*(1-1e-13),xtol=2e-14*L)
        return [(a,L-a,0.)]
    if not (M*W < 0): return []
    c=L*M/(2*dt)
    P=W*W*(1+4*t1*t2/(M*M))
    discr=L*L-4*(P+c*c)
    if not P>0 or discr< -1e-10:return []
    discr=max(discr,0)
    d=sqrt(discr)
    return [((L+u*d)/2,(L-u*d)/2,c) for u in (+1,-1) if not (u==-1 and d<1e-12)]


def main():
    rng=np.random.default_rng(20261023)
    count=0
    for _ in range(1200):
        L=float(rng.uniform(0.5,4)); s=float(rng.uniform(0.08,0.92));
        ab=L*L*s*(1-s)
        c=float(rng.uniform(-0.9,0.9)*sqrt(ab))
        if abs(c)<1e-4: c=0.13*sqrt(ab)
        a,b=L*s,L*(1-s)
        t1,t2=np.exp(rng.uniform(-1.5,1.5,size=2))
        if abs(t1-t2)<1e-4:t2+=0.2
        M,W,V,S=observables(a,b,c,t1,t2)
        MF,WF,VF=predicted(a,b,c,t1,t2)
        for val,ref in ((M,MF),(W,WF),(V,VF)):
            assert abs(val-ref)<4e-9*max(1,abs(ref)),(val,ref,a,b,c,t1,t2)
        inv=inverse(L,t1,t2,M,W)
        assert len(inv)==(1 if abs(a-b)<1e-7 else 2)
        assert any(max(abs(x-a),abs(y-b),abs(z-c))<1e-8 for x,y,z in inv)
        if len(inv)==2:
            vvals=[observables(x,y,z,t1,t2)[2] for x,y,z in inv]
            assert abs(vvals[0]-vvals[1])>1e-7
            assert min(abs(V-vv) for vv in vvals)<1e-8
        count+=1
    # Test strictly interior, saturated boundary and infeasible data
    for tt in [0.1,0.5,0.93]:
      L=2.6;t1=2.0;t2=0.5;dt=t1-t2
      M=dt*tt
      c=L*M/(2*dt)
      pmax=L*L/4-c*c
      Wmax=abs(M)*sqrt(pmax)/sqrt(M*M+4*t1*t2)
      for fac in [0.05,0.4,0.9999,1.]:
        inv=inverse(L,t1,t2,M,-fac*Wmax)
        assert len(inv)>0
        if fac==1: assert len(inv)==1
        else:assert len(inv)==2
      assert not inverse(L,t1,t2,M,-1.1*Wmax)
    for a in [0.13,0.77,1.45]:
      L=2.2;t1=2.0;t2=0.8;b=L-a
      V=t1/a-t2/b
      rec=inverse(L,t1,t2,0,0,V)
      assert len(rec)==1 and abs(rec[0][0]-a)<1e-9
    print('PASS: 1200 direct Lyapunov and independent angular-quadrature comparisons;')
    print('PASS: 1200 inverse fibre reconstructions and strict variance splitting;')
    print('PASS: 12 exact boundary/interior test cases, 3 infeasibility tests, 3 zero-torque reconstructions.')

if __name__=='__main__': main()
