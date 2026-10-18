#!/usr/bin/env python3
"""Exact verification of a four-hook generating identity and its boundary values.
Requires Python 3 and SymPy. No network access or external data required.
"""
import sympy as S
from functools import lru_cache
q=S.symbols('q')
A=q**4/(1-q**8)+q**4*(1+q**2)*(1/(1-q**4)-q/(1-q**6))+q**9/(1-q**6)+q**5*(1/(1-q**2)-q**3/(1-q**4))
B=q**4*(2+2*q+3*q**2+2*q**3+2*q**4+2*q**5)/((1-q)*(1+q)**2*(1+q**2)*(1-q+q**2)*(1+q+q**2))
R=1-q+q**2+q**3+2*q**4+2*q**7+2*q**8+q**9-q**10
assert S.cancel(A-B-q**7*(1-q)*R/((1-q**6)*(1-q**8)))==0
N=160
Q=[0]*(N+1);Q[0]=1
for j in range(1,N+1):
    for n in range(N,j-1,-1):Q[n]+=Q[n-j]
e=[Q[n]-(2*Q[n-1] if n>=1 else 0)+(Q[n-2] if n>=2 else 0) for n in range(N+1)]
assert [e[i] for i in [0,1,2,3,4,5,9,12]]==[1,-1,0,1,-1,1,1,1]
assert all(e[n]>=0 for n in range(5,N+1))
H=[0]*(N+1)
for n in range(N+1):
    H[n]=Q[n]+(H[n-6] if n>=6 else 0)+(H[n-8] if n>=8 else 0)-(H[n-14] if n>=14 else 0)
K=[H[n]-(H[n-1] if n else 0) for n in range(N+1)]
assert min(K)>=0
assert all(K[n]>=K[n-1] for n in range(11,N+1))
c=[1,-1,1,1,2,0,0,2,2,1,-1]
def C(n):return sum(c[i]*K[n-7-i] for i in range(11) if 0<=n-7-i<=N)
TABLE=[0,0,0,0,0,0,0,1,-1,1,2,1,2,2,4,6,7,7,11,13,17,22,27,31,40,48,57]
assert [C(n) for n in range(27)]==TABLE
@lru_cache(None)
def partitions(n,max_part):
    if n==0:return ((),)
    out=[]
    for first in range(min(n,max_part),0,-1):
        for tail in partitions(n-first,first):out.append((first,)+tail)
    return tuple(out)
def four_hooks(part):
    return sum(part[i]-j+1+sum(part[r]>=j for r in range(i+1,len(part)))==4 for i in range(len(part)) for j in range(1,part[i]+1))
for n in range(27):
    left=sum(four_hooks(part) for part in partitions(n,n) if all(v%2 for v in part))
    right=sum(four_hooks(part) for part in partitions(n,n) if len(set(part))==len(part))
    assert left-right==TABLE[n],(n,left,right,TABLE[n])
print('VERIFY_OK symbolic_identity=1 independently_enumerated_n=0..26 auxiliary_n=0..160')
