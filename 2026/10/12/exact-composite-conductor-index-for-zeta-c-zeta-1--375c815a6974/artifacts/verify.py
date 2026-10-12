#!/usr/bin/env python3
from math import gcd, comb, prod


def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

def phi(n):
    return sum(1 for a in range(1,n+1) if gcd(a,n)==1)

def factorint(n):
    f={}; p=2
    while p*p<=n:
        while n%p==0: f[p]=f.get(p,0)+1; n//=p
        p+=1
    if n>1: f[n]=f.get(n,0)+1
    return f

def poly_div_exact(a,b):
    # ascending coefficients; b monic
    a=a[:]
    q=[0]*max(1,(len(a)-len(b)+1))
    while len(a)>=len(b):
        k=len(a)-len(b); c=a[-1]
        q[k]=c
        for j,x in enumerate(b): a[k+j]-=c*x
        while a and a[-1]==0: a.pop()
    assert not a
    while len(q)>1 and q[-1]==0: q.pop()
    return q

def cyclo_poly(n, memo={1:[-1,1]}):
    if n in memo: return memo[n][:]
    # x^n-1 divided by Phi_d for proper d|n
    a=[-1]+[0]*(n-1)+[1]
    for d in divisors(n):
        if d<n: a=poly_div_exact(a, cyclo_poly(d))
    memo[n]=a
    return a[:]

def peval(a,x):
    y=0
    for c in reversed(a): y=y*x+c
    return y

def E_formula(n,m):
    fac=factorint(n); R=1
    mf=factorint(m)
    for p,e in fac.items():
        if mf.get(p,0)==e:
            R*=p**(e-1)*(p-2)
        else:
            R*=p**(e-1)*(p-1)
    return (R-(1 if m==n else 0))//2

def index_formula(n,c):
    z=1
    for m in divisors(n):
        E=E_formula(n,m)
        if m==1: v=1-c
        else: v=peval(cyclo_poly(m),c)
        z*=abs(v)**E
    return z

def is_composite(n):
    return n>1 and any(n%d==0 for d in range(2,int(n**0.5)+1))

cases=0; pairchecks=0
for n in range(3,316,2):
    if not is_composite(n): continue
    U=[a for a in range(n) if gcd(a,n)==1]
    cnt=[0]*n
    for i,a in enumerate(U):
        for b in U[i+1:]: cnt[(a+b)%n]+=1
    for t,N in enumerate(cnt):
        m=n//gcd(t,n)
        E=E_formula(n,m)
        assert N==E,(n,t,m,N,E)
        pairchecks+=1
    assert sum(cnt)==comb(phi(n),2)
    assert E_formula(n,n)>=1
    assert index_formula(n,0)==1
    assert index_formula(n,2)>1
    for c in (-5,-2,-1,0,2,3,5):
        assert index_formula(n,c)>=1
    cases+=1
print(f'VERIFY_OK odd_composite_conductors={cases} n_max=315 residue_pair_checks={pairchecks} classification_c0_c2=OK')
