#!/usr/bin/env python3
"""Independent finite checks for the first-coordinate Fourier spectrum on rank-one matrices.
The unrestricted result is proved algebraically; this checker samples small finite fields.
"""
import itertools
import math
from fractions import Fraction
import numpy as np

def mul(x,y,q):
    if q == 4:
        z=0
        for i in range(2):
            if (y>>i)&1:z ^= x<<i
        for i in (2,):
            if (z>>i)&1:z ^= 0b111 << (i-2)
        return z
    return (x*y)%q

def add(x,y,q): return x^y if q == 4 else (x+y)%q

def psi(x,q):
    if q==4:
        t=add(x,mul(x,x,q),q)
        assert t in (0,1)
        return complex(1 if t==0 else -1)
    return np.exp(2j*np.pi*(x%q)/q)

def do(q,m,n):
    z=q-1
    vecm=list(itertools.product(range(q),repeat=m))
    vecn=list(itertools.product(range(q),repeat=n))
    matrices=set()
    for u in vecm[1:]:
      for v in vecn[1:]:
        matrices.add(tuple(mul(ui,vj,q) for ui in u for vj in v))
    X=list(matrices)
    assert len(X)==(q**m-1)*(q**n-1)//z
    frequencies=[(-1,-1,0)]+[(i,j,a) for i in range(m) for j in range(n) for a in range(1,q)]
    F=np.empty((len(X),len(frequencies)),dtype=complex)
    for h,M in enumerate(X):
      for k,(i,j,a) in enumerate(frequencies):
        F[h,k]=1 if k==0 else psi(mul(a,M[i*n+j],q),q)
    G=F.conj().T@F/len(X)
    D=(q**m-1)*(q**n-1)
    c1=Fraction(q**(m+n-1)-q**m-q**n+1,D)
    c2=Fraction(q**(m+n-2)-q**m-q**n+1,D)
    t=c1-c2
    assert 1-c1==q*t
    lam0=q*t
    lamr=(1+z*n)*t
    lamc=(1+z*m)*t
    lamrc=t
    T=z*m*n
    B=(1-c1)+z*(c1-c2)*(m+n-1)+c2*T
    root=math.sqrt(float((1-B)**2+4*c1*c1*T))
    lplus=(float(1+B)+root)/2
    lminus=(float(1+B)-root)/2
    expected=sorted([float(lam0)]*(m*n*(q-2))+
                    [float(lamr)]*(m-1)+[float(lamc)]*(n-1)+
                    [float(lamrc)]*((m-1)*(n-1))+
                    [lplus,lminus])
    actual=sorted(np.linalg.eigvalsh(G).real)
    assert len(expected)==len(actual)
    assert np.max(np.abs(np.array(expected)-actual))<1e-10, (q,m,n,actual,expected)
    # Independent rank-Fourier kernel check of each pair.
    G_formula=np.empty_like(G)
    for a,A in enumerate(frequencies):
      for b,Bb in enumerate(frequencies):
        if a==b:r=0
        elif a==0 or b==0:r=1
        else:
          i,j,aa=A; k,l,bb=Bb
          r=1 if i==k or j==l else 2
        G_formula[a,b]=[1.,float(c1),float(c2)][r]
    assert np.max(np.abs(G-G_formula))<1e-10
    return len(X),len(frequencies),float(t),lplus,lminus

cases=[(2,2,2),(2,2,3),(2,3,3),(2,3,4),(3,2,2),(3,2,3),(3,3,3),(4,2,2),(4,2,3),(5,2,2),(5,2,3),(7,2,2)]
count=0
for q,m,n in cases:
  size,N,t,hi,lo=do(q,m,n)
  count+=1
  print(f'field={q} shape={m}x{n} rank_one={size} band={N} t={t:.8f} lambda_plus={hi:.8f} lambda_minus={lo:.8f}')
print(f'VERIFY_OK {count} exact-rank-kernel_and_complete-eigenvalue_cases=PASS GF4_trace=PASS')
