#!/usr/bin/env python3
"""Exact and floating-point checks of cubic-harmonic sampling on Johnson embeddings.
Requires Python 3.10+, sympy, numpy.
"""
from math import comb
from fractions import Fraction as F
from itertools import combinations
import numpy as np
import sympy as s

def scalar(n,k,t):
    z=F(n*t-k*k,k*(n-k))
    return (F(n+1)*z**3-3*z)/F(n-2)

def observed(n,k):
    sets=[set(x) for x in combinations(range(n),k)]
    G=np.array([[float(scalar(n,k,len(x&y))) for y in sets] for x in sets])
    return np.linalg.eigvalsh(G)

def spectral(n,k):
    N=comb(n,k)
    den=(n-1)*(n-2)**2*k**2*(n-k)**2
    ans={}
    ans[0]=F(N*(n+1)*(n-2*k)**2,k*(n-k)*(n-1)*(n-2)**2)
    ans[1]=F(N*n*(n*n+n-6*k*(n-k))**2,den*(n-3))
    ans[2]=F(N*6*n*(k-1)*(n-k-1)*(n-2*k)**2*(n+1),den*(n-4)*(n-3))
    if k>=3:
        ans[3]=F(N*6*n*n*(k-2)*(k-1)*(n+1)*(n-k-1)*(n-k-2),den*(n-5)*(n-4)*(n-3))
    return ans

def multiplicity(n,j):
    return comb(n,j)-(comb(n,j-1) if j else 0)

def compare_matrix(n,k):
    observed_eigs=observed(n,k)
    eigs=spectral(n,k)
    theory=[]
    for j in range(k+1):
        theory += [float(eigs.get(j,F(0)))]*multiplicity(n,j)
    theory.sort()
    err=max(abs(a-b) for a,b in zip(theory,observed_eigs))
    assert len(theory)==len(observed_eigs)
    assert err<1e-10, (n,k,err)
    print('direct-matrix',n,k,'size',len(theory),'max-abs-error',f'{err:.2e}', 'rank',sum(v>1e-9 for v in observed_eigs))

for n,k in [(5,2),(6,2),(6,3),(7,3),(8,2),(8,3),(8,4),(9,3),(10,3)]:
    compare_matrix(n,k)

# Independent symbolic check using a binomial incidence decomposition.
n,k,t=s.symbols('n k t',positive=True,integer=True)
z=(n*t-k*k)/(k*(n-k))
P=s.factor(((n+1)*z**3-3*z)/(n-2))
cs=[s.factor(sum(s.Integer(-1)**(r-i)*s.binomial(r,i)*P.subs(t,i) for i in range(r+1))) for r in range(4)]
for j in range(4):
    factor=s.Integer(0)
    for r in range(j,4):
        ratio=s.prod(k-a for a in range(r))*s.prod(n-k-a for a in range(j))/s.prod(n-a for a in range(r+j))
        factor += cs[r]*s.prod(k-j-a for a in range(r-j))/s.factorial(r-j)*ratio
    k2=k*(n-k)
    D=k2**2*(n-1)*(n-2)**2
    formulas=[(n+1)*(n-2*k)**2/(k2*(n-1)*(n-2)**2),
              n*(n*n+n-6*k2)**2/(D*(n-3)),
              6*n*(k-1)*(n-k-1)*(n-2*k)**2*(n+1)/(D*(n-4)*(n-3)),
              6*n*n*(k-2)*(k-1)*(n+1)*(n-k-1)*(n-k-2)/(D*(n-5)*(n-4)*(n-3))]
    assert s.cancel(factor-formulas[j])==0, j
print('exact symbolic four-sector identities passed')

# First four Pell solutions using exact integer equations.
a,b=2,1
for r in range(2,6):
    a,b=2*a+3*b,a+2*b
    N,K=a+1,(a+1-b)//2
    assert (N-1)**2-3*(N-2*K)**2==1
    assert N*N+N==6*K*(N-K)
    eig=spectral(N,K)
    assert eig[1]==0
    assert eig[0]>0 and eig[2]>0 and (K<3 or eig[3]>0)
    print('Pell branch',r,'n',N,'k',K,'missing-dimension',N-1)
print('ALL CHECKS PASSED')
