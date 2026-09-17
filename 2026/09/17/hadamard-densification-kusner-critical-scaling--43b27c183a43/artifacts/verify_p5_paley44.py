#!/usr/bin/env python3
"""Numerical consistency check for the non-dyadic p=5, m=44 instance.
Requires NumPy. This is not the proof; RESULT.md contains the exact argument.
"""
import math
import numpy as np

p=5.0
q=43
m=q+1

def legendre(x):
    x%=q
    if x==0: return 0
    return 1 if pow(x,(q-1)//2,q)==1 else -1

Q=np.array([[legendre(j-i) for j in range(q)] for i in range(q)],dtype=int)
H=np.empty((m,m),dtype=int)
H[0,0]=1; H[0,1:]=1; H[1:,0]=-1; H[1:,1:]=np.eye(q,dtype=int)+Q
H[1:,:]*=-1
assert np.max(np.abs(H@H.T-m*np.eye(m,dtype=int)))==0

def data(a):
    R=a**p+2
    A=(a+1)**p+(a-1)**p+2
    B=2*a**p+2**p
    return R,A,B,(2*A-B)/(2**(p-1)*R)

lo,hi=1.0,4**(1/p)
target=1+1/m
assert data(lo)[-1] < target < data(hi)[-1]
for _ in range(100):
    mid=(lo+hi)/2
    if data(mid)[-1] < target: lo=mid
    else: hi=mid
a=(lo+hi)/2
R,A,B,phi=data(a)
alpha=(R/4)**(1/p)
beta=(m*(A-B)/(2**p))**(1/p)
qv=np.array([[a,1,1,0],[-1,a,0,1],[-1,0,a,-1],[0,-1,1,a]],float)
H4=np.array([[1,1,1,1],[1,-1,1,-1],[1,1,-1,-1],[1,-1,-1,1]],int)
K=np.kron(H4,H)
keep=[]; weights=[]
for j in range(4):
    for t in range(m):
        if t==0 and j in (0,3):
            continue
        keep.append(j*m+t)
        weights.append(beta if t==0 and j in (1,2) else alpha)
weights=np.array(weights)
U=[]; V=[]
for i in range(4):
    for s in range(m):
        U.append(np.concatenate([H[s,r]*qv[i] for r in range(m)]))
        V.append(K[i*m+s,keep]*weights)
X=np.array([np.concatenate([sig*U[k],V[k]]) for k in range(4*m) for sig in (1,-1)])
expected=2**p*m*R
err=0.0
for i in range(len(X)-1):
    d=np.sum(np.abs(X[i+1:]-X[i])**p,axis=1)
    err=max(err,float(np.max(np.abs(d-expected))))
print('a =',repr(a))
print('shape =',X.shape)
print('relative max pairwise error =',err/expected)
c=math.sqrt(2)*math.log(1+math.sqrt(2))-7*math.log(2)/4
print('c =',repr(c),'8/c =',repr(8/c))
