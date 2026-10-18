#!/usr/bin/env python3
"""Exact certificates for adjacent part-frequency inequalities in strict partitions."""
from itertools import product

POS = (3,5,6,7,10)
NEG = (3,5,6,10,14)

def cert(T):
    v=[1]
    for a in T:
        w=v+[0]*a
        for i,b in enumerate(v):w[i+a]+=b
        v=w
    w=[(v[i] if i<len(v) else 0)
       -(v[i-8] if 0<=i-8<len(v) else 0)
       +(v[i-16] if 0<=i-16<len(v) else 0)
       for i in range(len(v)+16)]
    assert min(w)>=0, (T,[(i,c) for i,c in enumerate(w) if c<0])
    return w

for T in (POS,NEG):
    v=cert(T)
    print('POLYNOMIAL_OK',','.join(map(str,T)),len(v),sum(v),min(v))

N=500
q=[0]*(N+1);q[0]=1
for j in range(1,N+1):
    for n in range(N,j-1,-1):q[n]+=q[n-j]
A=[[0]*(N+1) for _ in range(N+1)]
for k in range(1,N+1):
    for n in range(k,N+1):
        A[k][n]=q[n-k]-(A[k][n-k] if n-k>=k else 0) if False else 0
    # coefficient of q^k Q(q)/(1+q^k): independent shift recurrence
    for n in range(k,N+1):
        A[k][n]=q[n-k]-(A[k][n-k] if n-k>=k else 0)
checks=0
for k in range(5,N):
    for n in range(k,N+1):
        assert A[k][n]>=A[k+1][n],(k,n)
        checks+=1
print('FREQUENCY_CHECKS_OK',checks)
# Verify exact non-power-of-two partition formula for generic adjacent k, n<=200.
M=200
for k in range(5,51):
    if (k&(k-1))==0 or ((k+1)&k)==0:continue
    v=[0]*(M+1);v[0]=1
    for j in range(1,M+1):
        if j not in(k,k+1) and (j&(j-1))!=0:
            for n in range(M,j-1,-1):v[n]+=v[n-j]
    for n in range(k,M+1):
        assert A[k][n]-A[k+1][n]==v[n-k],(k,n)
print('GENERIC_IDENTITY_OK')
