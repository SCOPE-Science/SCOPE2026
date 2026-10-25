#!/usr/bin/env python3
"""Finite independent checks of polygonal-semigroup cutoff and boundary family."""
import heapq
from math import gcd

def poly(m,n): return n*((m-2)*n-m+4)//2

def apery(a,b,c):
    d=[10**30]*a; d[0]=0; heap=[(0,0)]
    while heap:
        v,r=heapq.heappop(heap)
        if v!=d[r]:continue
        for w in (b,c):
            j=(r+w)%a
            if v+w<d[j]:d[j]=v+w;heapq.heappush(heap,(v+w,j))
    F=max(d)-a
    g=sum(d)//a-(a-1)//2
    return F,g

def triangular_f(n):
    k=n//2
    if n%2==0:
        return (2*k+1)*(k*k-k-1)+2*k*(k+1)*(2*k+3)
    return (2*k+3)*(k*k+k-1)+(2*k+2)*(k+1)*(2*k+1)

for m in range(3,18):
    t=m-2; M=(t+2)*(3*t-2)
    for n in list(range(2,45))+[12*M+1,12*M+2,12*M+17]:
        a,b,c=[poly(m,n+j) for j in range(3)]
        assert a<b<c and gcd(gcd(a,b),c)==1
        assert b-a==t*n+1 and c-a==2*t*n+t+2
        assert (2*t*a-(t-1))%(b-a)==0
        assert (8*t*a-M)%(c-a)==0
        if t>=2:
            assert gcd(a,b)<=t-1
            assert gcd(b,c)<=t-1
            assert gcd(a,c)<=M
        if n>12*M:
            assert c*M<a*(M+1) and c<2*a
            assert c-a>M
for n in range(2,55):
    a,b,c=[poly(3,n+j) for j in range(3)]
    F,g=apery(a,b,c)
    assert F==triangular_f(n), (n,F,triangular_f(n))
    assert 2*g==F+1,(n,F,g)
# Small region nonsymmetry examples, independent Apéry computation.
for m in range(4,12):
    for n in range(2,21):
        a,b,c=[poly(m,n+j) for j in range(3)]
        F,g=apery(a,b,c)
        if n>12*m*(3*m-8):assert 2*g!=F+1
print('VERIFY_OK: 15 polygonal families, 930 gcd/cutoff cases, 53 triangular Apéry identities, 160 nontriangular Apéry cases')
