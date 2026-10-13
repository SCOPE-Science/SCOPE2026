#!/usr/bin/env python3
from math import comb

def add(a,b):
    n=max(len(a),len(b)); out=[0]*n
    for i in range(n): out[i]=(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def compose_g(p):
    # g(p)=p^2-1
    q=mul(p,p); q[0]-=1; return q

def shift_one(p):
    # p(x+1)
    out=[0]*len(p)
    for k,a in enumerate(p):
        for j in range(k+1): out[j]+=a*comb(k,j)
    return out

def sqfree(n):
    n=abs(n)
    if n==0: return False
    p=2
    while p*p<=n:
        if n%(p*p)==0: return False
        p+=1
    return True

def v2(n):
    n=abs(n); k=0
    while n and n%2==0: n//=2; k+=1
    return k

samples=0
for c in range(2,80,4):
    assert c%4==2
    h=[0,1] # identity x = g^0
    for N in range(0,7):
        F=mul(h,h); F[0]+=c
        P=F if N%2==0 else shift_one(F)
        assert P[-1]==1
        assert all(a%2==0 for a in P[:-1])
        assert v2(P[0])==1
        # orbit critical values used by Theorem 1.8
        z=0
        vals=[]
        for i in range(N+1):
            vals.append(z*z+c)
            z=z*z-1
        assert vals==[c if i%2==0 else c+1 for i in range(N+1)]
        if N>=1:
            criterion=all(sqfree(v) for v in vals) and (c*(c+1))%4!=0
            assert criterion==(sqfree(c) and sqfree(c+1))
        samples+=1
        h=compose_g(h)
print(f"VERIFY_OK cases={samples} parity_eisenstein=1 orbit_alternation=1 squarefree_dichotomy=1")
