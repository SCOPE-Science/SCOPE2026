#!/usr/bin/env python3
"""Independent checks for bipartite resistance negative-type thresholds.
Only standard scientific libraries are needed: sympy, numpy, scipy.
Computes resistance from the reduced graph Laplacian, not from the theorem's formula.
Finite tests are corroborations, not the proof of the all-size statement.
"""
from fractions import Fraction
import math
import numpy as np
import sympy as sp
from scipy.optimize import brentq


def graph_laplacian(m,n):
    N=m+n
    L=sp.zeros(N)
    for i in range(m):
        for j in range(m,N):
            L[i,i]+=1;L[j,j]+=1;L[i,j]-=1;L[j,i]-=1
    return L


def independent_resistances(m,n):
    N=m+n
    inverse=graph_laplacian(m,n)[:N-1,:N-1].inv()
    R=sp.zeros(N)
    for i in range(N):
        for j in range(i+1,N):
            z=sp.zeros(N-1,1)
            if i!=N-1:z[i]=1
            if j!=N-1:z[j]=-1
            R[i,j]=R[j,i]=(z.T*inverse*z)[0]
    return R


def predicted_resistance(m,n):
    N=m+n
    a=sp.Rational(m+n-1,m*n)
    b=sp.Rational(2,n)
    c=sp.Rational(2,m)
    R=sp.zeros(N)
    for i in range(N):
        for j in range(i+1,N):
            R[i,j]=R[j,i]=b if j<m else (c if i>=m else a)
    return R


def critical(m,n):
    assert m>=2 and n>=2
    A=(m-1)/m;B=(n-1)/n
    X=2*m/(m+n-1);Y=2*n/(m+n-1)
    def fun(p):return A*X**p+B*Y**p-2
    return brentq(fun,0.0,20.0,xtol=1e-13)


pairs=[(2,2),(2,3),(2,4),(2,5),(2,9),(3,3),(3,4),(3,6),(4,4),(4,5),(4,7),(5,5),(5,8)]
for m,n in pairs:
    R=independent_resistances(m,n)
    assert R==predicted_resistance(m,n),(m,n)
    # Evaluate independently from the full centered powered-resistance matrix.
    J=np.eye(m+n)-np.ones((m+n,m+n))/(m+n)
    D=np.array(R.tolist(),float)
    p=critical(m,n)
    for exponent, expected in [(p*.7,'pos'),(p,'zero'),(p*1.3,'negative')]:
        G=-.5*J @ (D**exponent) @J
        eig=np.linalg.eigvalsh(G)
        ev=np.delete(eig,np.argmin(abs(eig))) # remove the constant-vector zero
        if expected=='pos':assert min(ev)>1e-10,(m,n,exponent,ev)
        if expected=='zero':assert abs(min(ev))<5e-9 and ev[1]>1e-8,(m,n,ev)
        if expected=='negative':assert min(ev)<-1e-10,(m,n,exponent,ev)
    # Exact sign identity at the key Euclidean exponent.
    a=sp.Rational(m+n-1,m*n)
    b=sp.Rational(2,n);c=sp.Rational(2,m)
    F=sp.Rational(m-1,m)*b**2+sp.Rational(n-1,n)*c**2-2*a**2
    assert F==sp.Rational(2*((m-n)**2-1),m*m*n*n)
    if abs(m-n)==1:assert abs(p-2)<1e-9
    elif m==n:assert p>2
    else:assert 1<p<2
print('EXACT_RESISTANCE_AND_GRAM_OK cases=',len(pairs),'roots=',len(pairs)*3)

for q in [150,800,2000]:
    for k in [0,1,2,3]:
        p=critical(q,q+k)
        target=(1-k*k)/2
        assert abs(q*(p-2)-target)<0.25
print('FIXED_IMBALANCE_ASYMPTOTICS_OK')

for m in [2,4,9]:
    for n in [500,4000]:
        p=critical(m,n)
        assert abs(n*(p-1)-1/math.log(2))<0.2
print('FIXED_SIDE_ASYMPTOTICS_OK')
print('ALL_RESISTANCE_NEGATIVE_TYPE_CHECKS_OK')
