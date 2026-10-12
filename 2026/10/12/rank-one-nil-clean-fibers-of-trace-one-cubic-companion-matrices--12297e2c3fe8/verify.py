#!/usr/bin/env python3
from itertools import product

def add(A,B,p): return [[(A[i][j]+B[i][j])%p for j in range(3)] for i in range(3)]
def sub(A,B,p): return [[(A[i][j]-B[i][j])%p for j in range(3)] for i in range(3)]
def mul(A,B,p): return [[sum(A[i][k]*B[k][j] for k in range(3))%p for j in range(3)] for i in range(3)]
def zero(A): return all(x==0 for row in A for x in row)
def outer(u,v,p): return [[u[i]*v[j]%p for j in range(3)] for i in range(3)]
def dot(u,v,p): return sum(u[i]*v[i] for i in range(3))%p

def companion(c0,c1,p):
    return [[0,0,(-c0)%p],[1,0,(-c1)%p],[0,1,1%p]]

def rank_one_idempotents(p):
    reps=[]
    for first in range(3):
        for tail in product(range(p), repeat=2-first):
            u=[0]*3; u[first]=1
            for j,x in enumerate(tail,start=first+1): u[j]=x
            reps.append(tuple(u))
    Es=[]
    for u in reps:
        for v in product(range(p), repeat=3):
            if dot(u,v,p)==1:
                Es.append(outer(u,v,p))
    assert len(Es)==(p*p+p+1)*p*p
    return Es

def trim(a):
    while len(a)>1 and a[-1]==0: a.pop()
    return a

def inv(a,p): return pow(a,p-2,p)
def divmod_poly(a,b,p):
    a=trim([x%p for x in a]); b=trim([x%p for x in b])
    if b==[0]: raise ZeroDivisionError
    q=[0]*max(1,(len(a)-len(b)+1))
    while len(a)>=len(b) and a!=[0]:
        k=len(a)-len(b); c=a[-1]*inv(b[-1],p)%p
        q[k]=c
        for j in range(len(b)): a[j+k]=(a[j+k]-c*b[j])%p
        trim(a)
    return trim(q),trim(a)
def gcd_poly(a,b,p):
    a=trim([x%p for x in a]); b=trim([x%p for x in b])
    while b!=[0]:
        _,r=divmod_poly(a,b,p); a,b=b,r
    if a==[0]: return [0]
    s=inv(a[-1],p); return trim([(x*s)%p for x in a])
def phi_poly(f,p):
    d=len(trim(f[:]))-1
    n=0
    for coeffs in product(range(p), repeat=d):
        if gcd_poly(list(coeffs),f,p)==[1]: n+=1
    return n

def predicted(c0,c1,p):
    f=[c0%p,c1%p,(-1)%p,1]
    val=phi_poly(f,p)//(p-1)
    if c0%p==0:
        h=[c1%p,(-1)%p,1]
        val += p*phi_poly(h,p)//(p-1)
        if c1%p==0: val += p*p
    return val

def actual(c0,c1,p,Es):
    C=companion(c0,c1,p); ans=0
    for E in Es:
        N=sub(C,E,p)
        N2=mul(N,N,p); N3=mul(N2,N,p)
        if zero(N3): ans+=1
    return ans

def run(p):
    Es=rank_one_idempotents(p)
    hist={}
    for c0,c1 in product(range(p), repeat=2):
        a=actual(c0,c1,p,Es); b=predicted(c0,c1,p)
        if a!=b: raise AssertionError((p,c0,c1,a,b))
        hist[a]=hist.get(a,0)+1
    print('FIELD',p,'COEFFICIENT_PAIRS',p*p,'RANK_ONE_IDEMPOTENTS',len(Es),'HIST',sorted(hist.items()))

for p in (2,3,5,7): run(p)
print('VERIFY_OK')
