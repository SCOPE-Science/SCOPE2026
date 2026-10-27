#!/usr/bin/env python3
"""Exact standard-library verification of Hasse polynomial data and finite-field counts."""
from collections import Counter

P = 5

def add(x,y): return tuple((a+b)%P for a,b in zip(x,y))
def neg(x): return tuple(-a%P for a in x)
def sub(x,y): return add(x,neg(y))

def field(n):
    if n==1: modulus=(0,1)
    elif n==2: modulus=(3,0,1)  # t^2 -2
    elif n==3: modulus=(1,1,0,1)  # t^3+t+1, no F5 root
    else: raise ValueError(n)
    from itertools import product
    elements=list(product(range(P),repeat=n))
    zero=(0,)*n; one=(1,)+(0,)*(n-1)
    def mul(x,y):
        coeff=[0]*(2*n-1)
        for i,a in enumerate(x):
            for j,b in enumerate(y): coeff[i+j]=(coeff[i+j]+a*b)%P
        for k in range(2*n-2,n-1,-1):
            lead=coeff[k]
            for j in range(n): coeff[k-n+j]=(coeff[k-n+j]-lead*modulus[j])%P
        return tuple(coeff[:n])
    def scalar(a): return (a%P,)+(0,)*(n-1)
    return elements,zero,one,mul,scalar

def count(n):
    elems,zero,one,mul,const=field(n)
    two=const(2);three=const(3)
    counts=Counter()
    compcounts=Counter(); pairs=Counter()
    for a in elems:
        aa=mul(a,a)
        for b in elems:
            bb=mul(b,b);ab=mul(a,b)
            smooth0=add(add(aa,b),three)
            smooth1=add(add(b,mul(two,a)),two)
            smooth2=add(sub(b,mul(two,a)),two)
            if zero in (smooth0,smooth1,smooth2): continue
            B=add(aa,mul(two,b))
            A=mul(two,a)
            C=add(add(bb,mul(two,aa)),two)
            factors=(add(B,A),sub(B,A),C)
            k=sum(t==zero for t in factors)
            counts[3-k]+=1
            for i,t in enumerate(factors):
                if t==zero: compcounts[i]+=1
            for i in range(3):
                for j in range(i+1,3):
                    if factors[i]==factors[j]==zero:pairs[(i,j)]+=1
    q=5**n; delta=int(n%2==0)
    predicted={1:3,2:3*q-9-6*delta,3:(q-3)**2+6*delta}
    assert dict(counts)==predicted,(n,counts,predicted)
    assert all(compcounts[i]==q-1-2*delta for i in range(3)),(n,compcounts)
    assert all(pairs[(i,j)]==1 for i in range(3) for j in range(i+1,3)),(n,pairs)
    print('GF(%s) counts=%s Hasse-components=%s intersections=%s OK'%(q,dict(counts),dict(compcounts),dict(pairs)))


def symbolic_cert():
    # f(x)=sum F_i*x^i, g=f(x)^2 mod 5; assert exact coefficient-index matrix
    import itertools
    for a,b in itertools.product(range(P),repeat=2):
        f={0:1,2:a,4:b,6:a,8:1}
        g={i+j:0 for i in f for j in f}
        for i,u in f.items():
            for j,v in f.items(): g[i+j]=(g[i+j]+u*v)%P
        A=2*a%P; B=(a*a+2*b)%P; C=(b*b+2*a*a+2)%P
        H=[[g.get(5*i-j,0)%P for j in range(1,4)] for i in range(1,4)]
        assert H==[[B,0,A],[0,C,0],[A,0,B]],(a,b,H)
    print('Hasse-Witt symbolic coefficient family: 25/25 GF(5) coefficient specializations OK')

if __name__=='__main__':
    symbolic_cert()
    for n in (1,2,3): count(n)
