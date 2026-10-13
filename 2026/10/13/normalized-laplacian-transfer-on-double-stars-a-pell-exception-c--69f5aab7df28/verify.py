#!/usr/bin/env python3
"""Independent finite checks for normalized-Laplacian double-star transfer identities.
The unrestricted PGST theorem is proved analytically, not inferred from this test.
"""
from fractions import Fraction
from math import gcd, isqrt, sqrt, pi, cos, sin

def rational_c(q):
    n=6*q*(q+1); k=isqrt(n)
    return k*k==n

def recurrence_polynomial(p,q):
    # recurrence for determinant of xI-B, with exact squared Jacobi weights
    alpha=Fraction(p,p+1); beta=Fraction(1,(p+1)*(q+1)); gamma=Fraction(q,q+1)
    # coefficients constant-first
    def xmul(A):return [Fraction(0)]+A
    def sub(A,B,c=1):
        out=[Fraction(0)]*max(len(A),len(B))
        for i,v in enumerate(A):out[i]+=v
        for i,v in enumerate(B):out[i]-=c*v
        return out
    P0=[Fraction(1)];P1=[Fraction(0),Fraction(1)]
    P2=sub(xmul(P1),P0,alpha)
    P3=sub(xmul(P2),P1,beta)
    P4=sub(xmul(P3),P2,gamma)
    c2=Fraction(p*q,(p+1)*(q+1))
    target=[c2,Fraction(0),-1-c2,Fraction(0),Fraction(1)]
    assert P4==target,(p,q,P4,target)

N=0
for p in range(1,21):
 for q in range(1,21):
  recurrence_polynomial(p,q);N+=1
pell=[0,2];
for _ in range(8):pell.append(10*pell[-1]-pell[-2]+4)
assert pell[:7]==[0,2,24,242,2400,23762,235224]
found=[q for q in range(1,100001) if rational_c(q)]
assert found==[q for q in pell if 1<=q<=100001],(found,pell)
for q in found:
 k=isqrt(6*q*(q+1))
 assert k%6==0 and q%2==0
 h=k//6
 assert Fraction(2*h,q+1) == Fraction(k,3*(q+1))
 a=Fraction(2*h,q+1).numerator;b=Fraction(2*h,q+1).denominator
 assert a%2==0 and b%2==1

try:
 import numpy as np
except ImportError:
 print('VERIFY_OK rational_Jacobi_tests=%d pell_scan=100000 numerical_skipped_missing_numpy'%N)
 raise SystemExit(0)

def L_and_pairs(p,q):
 n=p+q+2; u=p;v=p+1
 A=np.zeros((n,n),dtype=float)
 for i in range(p): A[i,u]=A[u,i]=1
 A[u,v]=A[v,u]=1
 for i in range(p+2,n): A[i,v]=A[v,i]=1
 d=A.sum(axis=1)
 L=np.eye(n)-A/np.sqrt(d[:,None]*d[None,:])
 return L

def amplitude(p,q,i,j,t):
 L=L_and_pairs(p,q); lam,V=np.linalg.eigh(L)
 return sum(V[i,k]*V[j,k]*np.exp(-1j*t*lam[k]) for k in range(len(lam)))

count=0
for p in range(1,11):
 for q in range(1,11):
  L=L_and_pairs(p,q); evals=np.linalg.eigvalsh(L)
  c=sqrt(p*q/((p+1)*(q+1)))
  nonone=[float(x) for x in evals if abs(x-1)>1e-8]
  assert np.allclose(nonone,[0,1-c,1+c,2],atol=1e-11),(p,q,nonone,c)
  assert sum(abs(evals-1)<1e-8)==p+q-2
  count+=1

witness=[]
for q in (1,3,4,5,6):
 c=sqrt(2*q/(3*(q+1)))
 bestk=min(range(0,20000),key=lambda k:abs(np.exp(1j*pi*(2*k+1)*c)+1))
 t=pi*(2*bestk+1)
 fid=abs(amplitude(2,q,0,1,t))**2
 assert fid>0.999,(q,bestk,fid)
 witness.append((q,bestk,round(float(fid),10)))
# For the first Pell exceptions, odd-phase pairs have exact separation from -1.
for q in (2,24,242):
 c=sqrt(2*q/(3*(q+1)))
 k=isqrt(6*q*(q+1))
 f=Fraction(k,3*(q+1))
 assert f.numerator%2==0 and f.denominator%2==1
 for m in range(0,2*f.denominator):
  assert ((2*m+1)*f.numerator - f.denominator)% (2*f.denominator)!=0
print('VERIFY_OK rational_Jacobi_tests=%d numerical_eigenspectra=%d pell_scan=100000 pell_terms=%d high_fidelity_witnesses=%s'%(N,count,len(found),witness))
