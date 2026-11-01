"""Reproducible checks for the negative-type threshold of bridged clique metrics.
Run: python verify_bridge_barbells.py. Requires Python, NumPy, SciPy.
Finite tests corroborate, but do not replace, the analytic proof.
"""
from fractions import Fraction as F
from itertools import product
from math import log, sqrt
from scipy.optimize import brentq
import numpy as np

def metric(q, r):
    # 0 = left bridge endpoint, 1..q = left ordinary clique vertices,
    # q+1 = right bridge endpoint, q+2..q+r+1 = right ordinary clique vertices.
    n=q+r+2; h=q+1
    d=[[0]*n for _ in range(n)]
    for i in range(n):
      for j in range(i+1,n):
        if i<=q<j:
          v=1+int(i!=0)+int(j!=h)
        else:
          v=1
        d[i][j]=d[j][i]=v
    return d

def powered_quadratic(d,coeff,p):
    return sum(coeff[i]*coeff[j]*F(d[i][j]**p) for i in range(len(d)) for j in range(len(d)))

def reduction(q,r,a,p):
    n=q+r+2; h=q+1
    X=sum(a[1:q+1]);Y=sum(a[q+2:]);S=a[0]+X
    assert S==-a[h]-Y
    dx=sum((a[i]-F(X,q))**2 for i in range(1,q+1))
    dy=sum((a[j]-F(Y,r))**2 for j in range(q+2,n))
    H=F(2**p);J=F(3**p);t=H-2
    C=[[F(2),t,-t],
       [t,F(1)+F(1,q),2*H-J-1],
       [-t,2*H-J-1,F(1)+F(1,r)]]
    v=[S,X,Y]
    return -dx-dy-sum(v[i]*C[i][j]*v[j] for i in range(3) for j in range(3))

def critical(q,r):
    if q==r==1:return 2.0
    delta=(1/q-1/r)/2
    gamma=1+(1/q+1/r)/2
    def fun(p):
      H=2**p;J=3**p
      beta=(H-2)**2/2
      z=(H*H+2)/2-J
      return beta+sqrt(delta*delta+z*z)-gamma
    return brentq(fun,1,2,xtol=1e-13)

def gram_eigen(q,r,p):
    d=np.array(metric(q,r),dtype=float)
    n=d.shape[0];J=np.eye(n)-np.ones((n,n))/n
    B=-0.5*J@(d**p)@J
    e=np.linalg.eigvalsh(B)
    idx=int(np.argmin(abs(e)))
    return np.delete(e,idx),B

cnt=0
for q,r,p in product(range(1,6),range(1,6),(1,2,3)):
    d=metric(q,r)
    n=q+r+2
    for seed in range(7):
      coeff=[F(((i+seed*3+2*i*seed)%13)-6) for i in range(n-1)]
      coeff.append(-sum(coeff))
      direct=powered_quadratic(d,coeff,p)
      rhs=reduction(q,r,coeff,p)
      assert direct==rhs,(q,r,p,seed,direct,rhs)
      cnt+=1
print('EXACT_QUADRATIC_FORM_OK',cnt)
for q,r in product(range(1,11),range(1,11)):
    pstar=critical(q,r)
    # min positive-side spectral gap; Gram has one trivial zero eigenvalue
    for gap in (0.02,0.08):
        if pstar-gap>0:
           ev,_=gram_eigen(q,r,pstar-gap)
           assert ev[0]>1e-7,(q,r,pstar-gap,ev[:4])
    ev,_=gram_eigen(q,r,pstar)
    if q==r==1:
       assert abs(ev[0])<1e-8 and abs(ev[1])<1e-8 and ev[2]>1e-6,(q,r,ev)
    else:
       assert abs(ev[0])<1e-8 and ev[1]>1e-5,(q,r,ev[:3])
       ev2,_=gram_eigen(q,r,pstar+0.012)
       assert ev2[0]<-1e-5,(q,r,ev2)
    assert (q==r==1 and abs(pstar-2)<1e-12) or 1<pstar<2
print('CRITICAL_INERTIA_OK',100)
for q,r in product(range(1,10),range(1,10)):
    p=critical(q,r)
    assert critical(q+1,r)<p-1e-10
    assert critical(q,r+1)<p-1e-10
print('STRICT_MONOTONICITY_CHECK_OK',81)
pinf=log(2)/log(1.5)
derivative=3**pinf*log(1.5)
for q,r in [(40,50),(100,100),(100,200),(500,700),(2000,3000)]:
    actual=critical(q,r)
    pred=pinf+(1/q+1/r)/(2*derivative)
    assert abs(actual-pred)<2*(1/q+1/r)**2,(q,r,actual,pred)
print('ASYMPTOTIC_CHECK_OK limit=',f'{pinf:.12f}','coefficient=',f'{1/(2*derivative):.12f}')
print('ALL_BRIDGE_BARBELL_CHECKS_OK')
