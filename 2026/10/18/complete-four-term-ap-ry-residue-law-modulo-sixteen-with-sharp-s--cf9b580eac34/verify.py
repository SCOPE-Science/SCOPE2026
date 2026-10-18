#!/usr/bin/env python3
"""Exact, standalone arithmetic verification of the stated four-term residue law."""
from math import comb
from collections import Counter

def r(n):
    assert n >= 0
    return sum(((n >> (j+1)) & 1) * (1-((n >> j) & 1)) for j in range(n.bit_length())) % 2

def a(n):
    return (1+4*(n&1)+8*r(n)) % 16

def apery(n):
    return sum(comb(n,k)**2*comb(n+k,k)**2 for k in range(n+1))

def E(p,u,v):
    return (1+8*(u^p),5+8*u,1+8*(v^(1-p)),5+8*v)

def O(p,u,v,w):
    return (5+8*u,1+8*(v^(1-p)),5+8*v,1+8*(w^p))

states=[(p,u,v) for p in (0,1) for u in (0,1) for v in (0,1)]
ix={s:i for i,s in enumerate(states)}
M=[[0]*8 for _ in range(8)]
for col,(p,u,v) in enumerate(states):
    for dest in ((0,u^p,u),(1,u,v^(1-p))):
        M[ix[dest]][col]+=1

def mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def add(A,B,c=1):
    return [[A[i][j]+c*B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def scale(A,c):
    return [[c*x for x in row] for row in A]
def eye(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]
def power(A,n):
    B=eye(len(A))
    while n:
        if n&1:B=mul(B,A)
        A=mul(A,A);n//=2
    return B
I=eye(8)
assert all(sum(row[j] for row in M)==2 for j in range(8))
assert mul(mul(mul(power(M,2),add(M,I,-2)),add(M,I,-1)), add(add(power(M,2),M,-2),scale(I,2))) == [[0]*8 for _ in range(8)]
for n in range(240):
    assert apery(n)%16==a(n)
for t in range(8192):
    s=states[ix[(t&1,r(t),r(t+1))]]
    assert (0,s[1]^s[0],s[1])==(0,r(2*t),r(2*t+1))
    assert (1,s[1],s[2]^(1-s[0]))==(1,r(2*t+1),r(2*t+2))
    assert tuple(a(2*t+j) for j in range(4))==E(*s)
    assert tuple(a(2*t+1+j) for j in range(4))==O(t&1,r(t),r(t+1),r(t+2))
allowed={E(p,u,v) for p in (0,1) for u in (0,1) for v in (0,1)}
odd={O(p,u,v,w) for p in (0,1) for u in (0,1) for v in (0,1) for w in (0,1)}
assert len(allowed)==8 and len(odd)==16 and not (allowed&odd)
allowed |= odd
cnt=Counter(tuple(a(n+j) for j in range(4)) for n in range(2**16))
assert set(cnt)==allowed
for m in range(1,6):
    L=4*m; Mpow=power(M,L)
    exact=Mpow[ix[(0,0,0)]][ix[(0,0,0)]]
    assert exact==2**(L-3)-(-4)**(m-1)
print('VERIFY_OK')
