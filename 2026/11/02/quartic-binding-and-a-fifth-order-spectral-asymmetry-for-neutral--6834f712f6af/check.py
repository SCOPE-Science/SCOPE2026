#!/usr/bin/env python3
"""Reproduce threshold expansions and spectrum checks for compact neutral defects."""
from fractions import Fraction
import math
import numpy as np
import mpmath as mp
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh

mp.mp.dps = 65
cases = [
    ((0,4),(1,-1)),
    ((0,2,4),(1,-2,1)),
    ((0,1,5),(1,-2,1)),
    ((0,2,5,9),(1,-2,2,-1)),
    ((0,1,2,4),(2,-3,2,-1)),
]

def invariants(x,w):
    assert len(x)==len(w) and sorted(x)==list(x) and sum(w)==0
    d=[[abs(a-b) for b in x] for a in x]
    A=-Fraction(sum(w[i]*w[j]*d[i][j] for i in range(len(x)) for j in range(len(x))),2)
    c=0; A2=0
    for i in range(len(x)-1):
        c+=w[i]; A2+=c*c*(x[i+1]-x[i])
    assert A==A2 and A>0
    z=[sum(d[i][j]*w[j] for j in range(len(w))) for i in range(len(w))]
    B=sum(w[i]*z[i]**2 for i in range(len(w)))
    return A,B

def determinant(k,epsilon,x,w,J=1):
    M=mp.eye(len(x))
    for i in range(len(x)):
        for j in range(len(x)):
            M[i,j]-=mp.mpf(epsilon)*mp.mpf(w[j])*mp.exp(-k*abs(x[i]-x[j]))/(2*J*mp.sinh(k))
    return mp.det(M)

def root(epsilon,x,w,J=1):
    A,B=invariants(x,w)
    e=mp.mpf(str(epsilon))
    k0=(e*e*int(A))/(2*J*J)
    a,b=k0/10, k0*10
    fa=determinant(a,e,x,w,J)
    fb=determinant(b,e,x,w,J)
    for _ in range(10):
        if fa*fb<0:break
        a/=2;b*=2;fa=determinant(a,e,x,w,J);fb=determinant(b,e,x,w,J)
    assert fa*fb<0,(fa,fb)
    for _ in range(140):
        c=(a+b)/2; fc=determinant(c,e,x,w,J)
        if fa*fc<0:b=c
        else:a=c;fa=fc
    k=(a+b)/2
    E=2*J*mp.cosh(k)
    return k,E

def direct_eigen(x,w,epsilon,J=1):
    L=max(550,max(x)+540)
    idx=np.arange(-L,L+1)
    diagonal=np.zeros(len(idx))
    for z,v in zip(x,w):diagonal[z+L]=epsilon*v
    mat=diags([J*np.ones(len(idx)-1), diagonal, J*np.ones(len(idx)-1)],[-1,0,1],format='csr')
    hi=eigsh(mat,k=1,which='LA',return_eigenvectors=False,tol=1e-12,maxiter=40000)[0]
    lo=eigsh(mat,k=1,which='SA',return_eigenvectors=False,tol=1e-12,maxiter=40000)[0]
    return hi,lo

if __name__=='__main__':
    print('NEUTRAL DEFECT SPECTRAL VERIFICATION')
    for x,w in cases:
        A,B=invariants(x,w)
        c4=mp.mpf(int(A)**2)/4
        c5=mp.mpf(int(A)*int(B))/8
        print('sites=%s weights=%s A=%s B=%s c4=%s c5=%s'%(x,w,A,B,c4,c5))
        for e in ['0.08','0.04','0.02','0.01']:
            kp,Ep=root(e,x,w); km,Em=root('-'+e,x,w)
            ee=mp.mpf(e)
            gp=Ep-2;gm=Em-2
            # The two-sided fifth-order prediction and small-parameter residuals.
            rp=abs(gp-c4*ee**4-c5*ee**5)/ee**6
            rm=abs(gm-c4*ee**4+c5*ee**5)/ee**6
            assert kp>0 and km>0 and mp.isfinite(rp) and mp.isfinite(rm)
            if e=='0.01':
                assert abs(gp/ee**4-c4)<mp.mpf('1.2'), (x,w,gp/ee**4,c4)
                assert abs(gm/ee**4-c4)<mp.mpf('1.2'), (x,w,gm/ee**4,c4)
                assert abs((gp-gm)/ee**5-2*c5)<mp.mpf('1.0'), (x,w,(gp-gm)/ee**5,2*c5)
            print(' eps=%s plus/eps4=%s minus/eps4=%s residual-over-eps6=(%s,%s)'% (e,mp.nstr(gp/ee**4,11),mp.nstr(gm/ee**4,11),mp.nstr(rp,11),mp.nstr(rm,11)))
        eps='0.2'
        kplus,Eplus=root(eps,x,w);kminus,Eminus=root('-'+eps,x,w)
        hi,lo=direct_eigen(x,w,float(eps))
        errp=abs(hi-float(Eplus));errm=abs(lo+float(Eminus))
        assert errp<2e-7 and errm<2e-7,(x,errp,errm)
        print(' finite-chain Eplus=%0.12f Eminus=%0.12f errors=(%.3g,%.3g)'%(hi,lo,errp,errm))
    print('ALL CHECKS PASSED')
