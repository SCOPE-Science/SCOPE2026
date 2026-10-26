#!/usr/bin/env python3
"""Exact rational moments and numerical eigenvalue tests for odd-band spherical concentration."""
from fractions import Fraction as F
from math import comb
import numpy as np
from scipy.linalg import eigh

checks=0

def verify(condition,description):
    global checks
    if not condition:
        raise AssertionError(description)
    checks += 1

def moment(d,m,n,c):
    # Squared latitude s; integer beta for odd spatial dimensions d.
    beta=(d-3)//2+m
    halfpower=F(3,2) if m%2==0 else F(1,2)
    a=F(c)**2
    ans=F(0)
    for j in range(beta+1):
        power=F(n+j)+halfpower
        # power is half-integer and a is square of a rational number.
        val=F(c)**(2*power.numerator//power.denominator)
        ans+=F((-1)**j*comb(beta,j),1)*(1-val)/power
    return ans

def beta_full(d,m,n):
    beta=(d-3)//2+m
    halfpower=F(3,2) if m%2==0 else F(1,2)
    return sum((F((-1)**j*comb(beta,j),1)/(F(n+j)+halfpower) for j in range(beta+1)),F(0))

def spectra(d,K,c,weight=(1,)):
    out=[]
    for m in range(2*K+2):
        z=K-m//2+1
        G=np.array([[float(sum((F(v)*beta_full(d,m,i+j+t) for t,v in enumerate(weight)),F(0))) for j in range(z)] for i in range(z)])
        H=np.array([[float(sum((F(v)*moment(d,m,i+j+t,c) for t,v in enumerate(weight)),F(0))) for j in range(z)] for i in range(z)])
        verify(np.linalg.eigvalsh(G)[0]>1e-8,(d,K,c,m,'G positive'))
        verify(np.allclose(G,G.T),(d,K,c,m,'symmetry'))
        eig=eigh(H,G,eigvals_only=True)[::-1]
        for x in eig:
            verify(-1e-9<x<1+1e-9,(d,K,c,m,'range',x))
        out.append(eig)
    return out

for d in (3,5,7):
 for K in (0,1,2,3):
  for c in (F(1,3),F(1,2),F(2,3)):
   for weight in ((1,), (1,2), (1,0,1)):
    ls=spectra(d,K,c,weight)
    for m in range(len(ls)-1):
     a,b=ls[m],ls[m+1]
     for j in range(len(b)):
         verify(a[j]>b[j]+1e-11, (d,K,c,m,j,'forward',a[j],b[j]))
     for j in range(len(a)-1):
         verify(b[j]>a[j+1]+1e-11,(d,K,c,m,j,'interlace',b[j],a[j+1]))
    tops=sorted([(x,m,j) for m,a in enumerate(ls) for j,x in enumerate(a)],reverse=True)
    verify(tops[0][1:]==(0,0),(d,K,c,'top'))
    verify(tops[1][1:]==(1,0),(d,K,c,'second'))
print('PASS:',checks,'independent exact-rational moment/numeric spectral assertions')
