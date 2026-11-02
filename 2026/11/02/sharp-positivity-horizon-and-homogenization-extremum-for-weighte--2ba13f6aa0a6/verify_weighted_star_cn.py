"""Exact and numeric verification of star Crank-Nicolson positivity frontier."""
import numpy as np
import sympy as sp
from scipy.optimize import brentq

def threshold(w):
    def f(t):return sum(t*x/(1+t*x) for x in w)-1
    hi=1.
    while f(hi)<0:hi*=2
    return brentq(f,0.,hi,rtol=8e-15)

def fullmatrix(w,t):
    m=len(w);L=np.zeros((m+1,m+1))
    for i,x in enumerate(w,1):
        L[0,0]+=x;L[i,i]+=x;L[0,i]-=x;L[i,0]-=x
    return 2*np.linalg.inv(np.eye(m+1)+t*L)-np.eye(m+1)

numeric=0
for m in range(2,17):
    for trial in range(35):
        rng=np.random.default_rng(19+100*m+trial)
        w=np.exp(rng.uniform(-5,5,size=m))
        t=threshold(w)
        # exact characterization on both sides of the threshold
        for c in [0,0.15,0.8,1.,1.2,3.]:
            C=fullmatrix(w,c*t)
            assert np.min(C[1:,1:].diagonal())>=-1e-10 if c<=1 else True
            assert min(np.diag(C)[1:]-C[0,0])>0 if c>0 else True
            assert np.min(C-np.diag(np.diag(C)))>=-1e-12
            assert (C.min()>=-3e-10) if c<=1 else (C[0,0]<-1e-11)
            assert np.max(np.abs(C.sum(axis=1)-1))<1e-10
        # balanced equal rate is unique worst horizon for fixed W
        W=sum(w)
        assert t+1e-11 >= m/(W*(m-1))
        numeric+=1

exact=0
for w in [[sp.Rational(1),sp.Rational(4)], [sp.Rational(1,2),sp.Rational(3,2),sp.Rational(5,4)], [sp.Rational(1,2),sp.Rational(3,4),sp.Rational(2),sp.Rational(5,4)]]:
    m=len(w);t=sp.symbols('t',real=True)
    L=sp.zeros(m+1)
    for i,x in enumerate(w,1):
        L[0,0]+=x;L[i,i]+=x;L[0,i]-=x;L[i,0]-=x
    R=(sp.eye(m+1)+t*L).inv()
    S=1+sum(t*x/(1+t*x) for x in w)
    assert sp.factor(R[0,0]-1/S)==0
    for i,x in enumerate(w,1):
        other=sum(t*y/(1+t*y) for j,y in enumerate(w,1) if j!=i)
        assert sp.factor(R[i,i]-R[0,0]-other/(S*(1+t*x)))==0
    exact+=1
print(f'PASS {numeric} randomly weighted stars, {numeric*6} whole-matrix comparisons, {exact} exact-rational symbolic resolvent identities')
