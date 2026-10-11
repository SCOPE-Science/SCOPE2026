#!/usr/bin/env python3
"""Exact rational checks and independent DFT checks for valuation-shell Fourier concentration."""
from fractions import Fraction
from collections import Counter
from math import isclose
import numpy as np

def spec(p,n,s,t):
    m=(p-1)*p**(n-t-1)
    v=s+t
    if v<=n-2:
        one=(p-1)**2*p**(n-s-t-2)
        return {Fraction(1):one,Fraction(0):m-one}
    if v==n-1:
        return {Fraction(1):p-2,Fraction(1,p):1,Fraction(0):m-p+1}
    return {Fraction((p-1)**2, p**(s+t-n+2)):1,Fraction(0):m-1}

def frequency_shell(p,n,t):
    N=p**n
    return [a for a in range(N) if a%p**t==0 and a%p**(t+1)!=0]

def space_shell(p,n,s):
    N=p**n
    return [x for x in range(N) if x%p**s==0 and x%p**(s+1)!=0]

def entries(p,n,s,t):
    F=frequency_shell(p,n,t)
    fine=p**(n-s)
    coarse=p**(n-s-1)
    return F,[[ (Fraction(1,p**s) if (a-b)%fine==0 else 0)
            -(Fraction(1,p**(s+1)) if (a-b)%coarse==0 else 0)
            for b in F] for a in F]

def verify_exact(p,n,s,t):
    F,B=entries(p,n,s,t)
    m=len(F)
    predicted={v:k for v,k in spec(p,n,s,t).items() if k}
    assert sum(predicted.values())==m
    diag=Fraction((p-1)*p**(n-s-1),p**n)
    assert all(B[i][i]==diag for i in range(m))
    tr=sum(B[i][i] for i in range(m))
    tr2=sum(z*z for row in B for z in row)
    assert tr==sum(v*k for v,k in predicted.items()),(p,n,s,t,'trace')
    assert tr2==sum(v*v*k for v,k in predicted.items()),(p,n,s,t,'trace2')
    # A spectral polynomial annihilates the proposed symmetric rational matrix.
    if m<=36:
        import sympy as sp
        A=sp.Matrix([[sp.Rational(x.numerator,x.denominator) for x in row] for row in B])
        def polyeval(vals):
            C=sp.eye(m)
            for v in vals:
                C=C*(A-sp.Rational(v.numerator,v.denominator)*sp.eye(m))
            return C
        assert polyeval(predicted)==sp.zeros(m,m),(p,n,s,t,'poly')
    return m

def verify_dft(p,n,s,t):
    N=p**n
    F=frequency_shell(p,n,t)
    X=space_shell(p,n,s)
    a=np.asarray(F,dtype=float)[:,None]
    x=np.asarray(X,dtype=float)[None,:]
    B=np.exp(2j*np.pi*a*x/N)/np.sqrt(N)
    eig=np.linalg.eigvalsh(B@B.conj().T)
    predicted=sorted(float(v) for v,k in spec(p,n,s,t).items() for _ in range(max(0,k)))
    assert len(predicted)==len(eig)
    assert np.max(np.abs(eig-predicted))<3e-11,(p,n,s,t,eig,predicted)

if __name__=='__main__':
    cases=0; dfts=0; dims=0
    for p in (2,3,5):
      for n in range(2,5):
       for s in range(n):
        for t in range(n):
         dims+=verify_exact(p,n,s,t)
         cases+=1
         if p**n<=125:
           verify_dft(p,n,s,t);dfts+=1
    for p in (2,3):
      n=5
      for s in range(n):
       for t in range(n):
        dims+=verify_exact(p,n,s,t);cases+=1
        if p==2:verify_dft(p,n,s,t);dfts+=1
    print(f'VERIFY_OK exact_case_count={cases} exact_matrix_dimensions_sum={dims} dft_cases={dfts} polynomial_identity_for_m_le_36=PASS trace_trace2=PASS')
