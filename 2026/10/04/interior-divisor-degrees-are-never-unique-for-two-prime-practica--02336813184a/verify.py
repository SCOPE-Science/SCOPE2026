#!/usr/bin/env python3
from math import prod

def is_prime(n):
    if n < 2: return False
    d=2
    while d*d<=n:
        if n%d==0: return False
        d += 1 if d==2 else 2
    return True

def phi_prime_power(q,e):
    if e==0: return 1
    return (q-1)*(q**(e-1))

def check(a,p=None,b=0):
    A=2**a
    n=A if b==0 else A*(p**b)
    weights=[]
    for j in range(b+1):
        for i in range(a+1):
            ph2=1 if i<=1 else 2**(i-1)
            php=1 if j==0 else phi_prime_power(p,j)
            weights.append(ph2*php)
    c=[0]*(n+1); c[0]=1
    for w in weights:
        for d in range(n,w-1,-1):
            c[d]+=c[d-w]
    assert c[0]==c[n]==1
    assert c[1]==c[n-1]==2
    assert min(c[1:n])>=2
    return n

tests=0
for a in range(1,6):
    check(a); tests+=1
    A=2**a
    for p in range(3,A+2,2):
        if is_prime(p):
            for b in (1,2):
                check(a,p,b); tests+=1
print('VERIFY_OK', tests)
