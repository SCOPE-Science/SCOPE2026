"""Standalone finite checks for an analytic theorem on centered graph maximal averages.
Finite tests illustrate the proof; they do not certify its universal quantifiers.
"""
from fractions import Fraction
from itertools import product
from math import sqrt
import numpy as np


def mat(a,b,mask):
    n=a+b
    A=np.zeros((n,n),float)
    for i,k in enumerate(mask):
        if k==0: A[i,i]=1
        elif k==2: A[i,:]=1/n
        elif i<a:
            A[i,i]=1/(b+1); A[i,a:]=1/(b+1)
        else:
            A[i,i]=1/(a+1); A[i,:a]=1/(a+1)
    return A

def candidate_sq(a,b):
    tau=1+(a*b+1)/(a+1)**2
    return (tau+sqrt(tau*tau-4/(a+1)**2))/2

checks=0
for a,b in ((1,2),(2,2),(2,3),(2,4),(3,3),(1,5)):
    n=a+b
    vals=[]
    for mask in product(range(3),repeat=n):
        A=mat(a,b,mask)
        val=np.linalg.eigvalsh(A.T@A)[-1]
        vals.append((val,mask))
        checks+=1
    mx=max(t[0] for t in vals)
    assert abs(mx-candidate_sq(a,b))<2e-11,(a,b,mx,candidate_sq(a,b))
    checks+=1
    T=mat(a,b,(0,)*a+(1,)*b)
    evals,V=np.linalg.eigh(T.T@T)
    v=np.abs(V[:,-1])
    c=np.sum(v[:a]); d=np.sum(v[a:])
    N=a+b; mu=(c+d)/N
    m=np.r_[np.maximum.reduce([v[:a],(v[:a]+d)/(b+1),np.full(a,mu)]),np.maximum.reduce([v[a:],(v[a:]+c)/(a+1),np.full(b,mu)])]
    assert np.max(np.abs(m-T@v))<1e-10
    checks+=1

for a in range(2,11):
    for b in (a,a+2,3*a,30*a):
        tau=Fraction(1)+Fraction(a*b+1,(a+1)**2)
        det=Fraction(1,(a+1)**2)
        # Exact trace and determinant of the two-dimensional singular block.
        assert tau*tau-4*det>0
        assert tau>1
        checks+=2
        lam=candidate_sq(a,b)
        ratio=a/((a+1)**2*lam-1)
        assert 0<ratio<1
        checks+=1

print('PASS:',checks,'finite assertions; mathematical large-b proof is analytical')
