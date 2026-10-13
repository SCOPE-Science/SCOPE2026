#!/usr/bin/env python3
"""Exact finite-field consistency checks for modular polar maps of bitangent pencils.
Scientific proof of the universal theorem is in RESULT.md; samples are not an infinite certificate.
"""
from math import gcd as igcd

def clean(f,p):
    f=list(f)
    if p:f=[a%p for a in f]
    while len(f)>1 and not f[-1]:f.pop()
    return tuple(f)

def add(f,g,p):
    return clean([(f[i] if i<len(f) else 0)+(g[i] if i<len(g) else 0) for i in range(max(len(f),len(g)))],p)

def neg(f,p):return clean([-a for a in f],p)
def sub(f,g,p):return add(f,neg(g,p),p)
def scale(f,c,p):return clean([c*a for a in f],p)

def mul(f,g,p):
    ans=[0]*(len(f)+len(g)-1)
    for i,a in enumerate(f):
        for j,b in enumerate(g):ans[i+j]+=a*b
    return clean(ans,p)

def der(f,p):return clean([i*a for i,a in enumerate(f)][1:] or [0],p)

def divrem(a,b,p):
    a=list(clean(a,p));b=clean(b,p)
    assert b!=(0,)
    q=[0]*max(1,len(a)-len(b)+1)
    inv=pow(b[-1],-1,p)
    while len(a)>=len(b) and any(a):
        k=len(a)-len(b); c=a[-1]*inv%p;q[k]=c
        for i,t in enumerate(b):a[i+k]=(a[i+k]-c*t)%p
        while len(a)>1 and a[-1]==0:a.pop()
    return clean(q,p),clean(a,p)

def pgcd(a,b,p):
    while b!=(0,):a,b=b,divrem(a,b,p)[1]
    return scale(a,pow(a[-1],-1,p),p)

def quotient_pair(h,m,p):
    hp=der(h,p);rh=mul((0,1),hp,p)
    D=add(h,rh,p);M=sub(scale(h,m,p),rh,p)
    # Ratio  (B/C)^2/(4(A/C)) = M^2/(h' D).
    N=mul(M,M,p);den=mul(hp,D,p)
    gg=pgcd(N,den,p)
    N=divrem(N,gg,p)[0];den=divrem(den,gg,p)[0]
    return N,den,hp,D,M

def degree(h,m,p):
    N,D,_,_,_=quotient_pair(h,m,p)
    return max(len(N),len(D))-1

def is_inseparable(N,D,p):
    return sub(mul(der(N,p),D,p),mul(N,der(D,p),p),p)==(0,)

cases=[
    (7,2,(2,3,1),3,False,'ordinary'),
    (7,3,(6,11,6,1),5,False,'ordinary'),
    (3,2,(2,0,1),1,False,'m+1 divisible'),
    (5,4,(4,0,0,0,1),3,False,'m+1 divisible'),
    (3,3,(1,2,0,1),3,False,'m divisible separable'),
    (3,3,(1,0,1,1),3,True,'m divisible inseparable'),
    (5,5,(1,4,0,0,0,1),5,False,'m divisible separable'),
    (5,5,(1,0,0,0,1,1),5,True,'m divisible inseparable'),
    (7,7,(1,6,0,0,0,0,0,1),7,False,'m divisible larger'),
]
for p,m,raw,expected,inseparable,label in cases:
    h=clean(raw,p)
    assert len(h)==m+1 and h[0]!=0 and pgcd(h,der(h,p),p)==(1,), (label,h)
    N,D,_,_,_=quotient_pair(h,m,p)
    assert degree(h,m,p)==expected,(label,degree(h,m,p),expected)
    assert is_inseparable(N,D,p)==inseparable,(label,N,D)
    if m%p==0:
        second=add(scale(der(h,p),2,p),mul((0,1),der(der(h,p),p),p),p)
        assert (second==(0,))==inseparable,label
    print(f'p={p};m={m};{label};degree={expected};inseparable={inseparable};numerator={N};denominator={D}')
# The above establishes nontrivial instances of each degree regime, including both
# separable and inseparable degrees p at m=p. The theorem for ALL coefficients and
# all m is proved from polynomial gcd and leading terms in RESULT.md.
print('VERIFY_OK: polar-degree phase tests and m=p separability examples')
