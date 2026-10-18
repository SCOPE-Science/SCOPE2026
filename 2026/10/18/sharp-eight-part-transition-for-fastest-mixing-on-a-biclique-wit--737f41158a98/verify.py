#!/usr/bin/env python3
"""Independent finite reconstructions for a one-edge-deleted biclique FMMC theorem.
This program checks exact algebra, matrices and sample feasibility; general optimality is proved analytically in RESULT.md.
Requires Python 3, numpy>=2.0, sympy>=1.12. Execute: python verify.py
"""
import math
from fractions import Fraction
import numpy as np
import sympy as sp

def analytic(m):
    if not isinstance(m, int) or m < 2:
        raise ValueError('m must be an integer >=2')
    r=m-1
    if m <=7:
        return 1/(2*r),1/m,1/math.sqrt(m)
    d=math.sqrt(m*m-8*m+8)
    return (m-2+d)/(r*(2*r+d)),2/(2*r+d),(m-2)/(2*r+d)

def build(m,x,y):
    """Row/col indices: left 0..m-1, right m..2m-1; absent edge (0,m)."""
    P=np.zeros((2*m,2*m),dtype=float)
    for i in range(m):
        for j in range(m):
            if i==0 and j==0:continue
            v=y if (i==0 or j==0) else x
            P[i,m+j]=P[m+j,i]=v
    np.fill_diagonal(P,1-P.sum(axis=1))
    return P

def small_blocks(m,x,y):
    r=m-1
    E=np.array([[1-r*y, -math.sqrt(r)*y],[-math.sqrt(r)*y,1-2*r*x-y]])
    spec=[1,1-m*y]+list(np.linalg.eigvalsh(E))
    spec += [1-r*x-y]*(2*(r-1))
    return np.sort(np.array(spec))

def test():
    count=0
    z=sp.symbols('z',real=True)
    for m in range(2,8):
        r=m-1
        # Low branch admits rational optimal weights. Check the exact 2x2 square identity.
        x=sp.Rational(1,2*r); y=sp.Rational(1,m)
        E=sp.Matrix([[1-r*y,-sp.sqrt(r)*y],[-sp.sqrt(r)*y,1-2*r*x-y]])
        assert E**2==sp.eye(2)/m
        assert sp.Rational(m-2,2*m)<=1/sp.sqrt(m)
        count+=3
    for m in range(8,22):
        r=m-1;s=sp.sqrt(m*m-8*m+8);D=2*r+s
        x=(m-2+s)/(r*D);y=2/D;t=(m-2)/D
        a=1-r*y
        E=sp.Matrix([[a,-sp.sqrt(r)*y],[-sp.sqrt(r)*y,1-2*r*x-y]])
        assert all(sp.simplify(v)==0 for v in list(E**2-t*t*sp.eye(2)))
        assert sp.simplify(1-r*x-y-t)==0
        assert sp.simplify((1-m*y)-(s-2)/D)==0
        A=2*r*(s-2)/(s*D);B=m*(m-s)/(2*s*D);C=(m+s)/(2*D)
        assert sp.simplify(A+B+C-1)==0
        q=a/t;K=(r*y-(r-1)*a/2)/t
        assert sp.simplify(-r*A-r*(1-q)*B+r*(1+q)*C)==0
        assert sp.simplify(-A+(-m/2+K)*B+(m/2+K)*C)==0
        assert float(A)>0 and float(B)>0 and float(C)>0
        count+=8
    for m in list(range(2,24))+[25,28,32,40,60]:
        x,y,t=analytic(m)
        P=build(m,x,y)
        assert np.min(P)>-3e-13
        assert np.max(abs(P.sum(axis=1)-1))<5e-13
        assert np.max(abs(P-P.T))<1e-14
        lam=np.linalg.eigvalsh(P)
        assert np.max(np.abs(lam-small_blocks(m,x,y)))<1e-11
        mu=np.max(abs(lam[:-1])); assert abs(mu-t)<1e-11
        assert abs(lam[-1]-1)<1e-11
        count+=6
    rng=np.random.default_rng(4621)
    for m in [2,3,4,7,8,9,10,15,20,40]:
        r=m-1;t=analytic(m)[2]
        for _ in range(300):
            y=rng.uniform(0,1/r)
            x=rng.uniform(0,(1-y)/r)
            P=build(m,x,y)
            v=small_blocks(m,x,y)
            mu=max(abs(v[:-1]))
            assert mu>=t-1e-12
            count+=1
    print(f'VERIFY_OK {count} exact/spectral/feasibility assertion groups; m=2..60')

if __name__=='__main__':test()
