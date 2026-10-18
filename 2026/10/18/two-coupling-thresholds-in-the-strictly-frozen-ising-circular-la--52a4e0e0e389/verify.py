#!/usr/bin/env python3
"""Direct finite-spin and transfer-matrix checks for a circular ladder."""
from collections import Counter
from math import comb

def brute(n, J, K):
    hist=Counter()
    for mask in range(1 << (2*n)):
        a=[1 if mask>>i&1 else -1 for i in range(n)]
        b=[1 if mask>>(n+i)&1 else -1 for i in range(n)]
        ok=True
        for i in range(n):
            for row,other in ((a,b),(b,a)):
                if row[i]*(J*(row[(i-1)%n]+row[(i+1)%n])+K*other[i]) <= 0:
                    ok=False
                    break
            if not ok:break
        if ok:
            k=sum(a[i]!=a[(i+1)%n] for i in range(n))
            unsat=sum(a[i]*b[i] != (1 if K >=0 else -1) for i in range(n))
            hist[k,unsat]+=1
    return hist

def predicted(n, J, K):
    out=Counter()
    if K==0:
        out[(0,0)]=2
        out[(0,n)]=2
        return out
    q=abs(K)
    if q>2*J:
        for k in range(0,n+1,2):out[(k,0)]=2*comb(n,k)
    else:
        out[(0,0)]=2
        for k in range(2,n//2+1,2):out[(k,0)]=(2*n*comb(n-k-1,k-1))//k
        if q<2*J:out[(0,n)]=2
    return out

cases=0
for n in range(3,9):
    for K in (-7,-4,-3,-1,0,1,3,4,7):
        b=brute(n,2,K);p=predicted(n,2,K)
        assert b == p,(n,K,b,p)
        cases+=1
print('PASS',cases,'complete spin-space / coupling comparisons')

# Coefficient-wise transfer matrix multiplication (stdlib only).
def plus(a,b):
    c=Counter(a)
    for k,v in b.items():c[k]+=v
    return c

def times(a,b):
    c=Counter()
    for i,v in a.items():
        for j,w in b.items():c[i+j]+=v*w
    return c

def mul(A,B):
    n=len(A)
    return [[sum_poly([times(A[i][k],B[k][j]) for k in range(n)])
             for j in range(n)] for i in range(n)]

def sum_poly(polys):
    c=Counter()
    for p in polys:
        for k,v in p.items():c[k]+=v
    return c

pairs=('00','01','10','11')
M=[[Counter() for _ in pairs] for _ in pairs]
for i,p in enumerate(pairs):
    for j,q in enumerate(pairs):
        if p[1]==q[0] and not (p[0]==q[1]!=p[1]):
            M[i][j][int(p[1]!=q[1])]=1
P=[[Counter({0:int(i==j)}) if i==j else Counter() for j in range(4)] for i in range(4)]
for n in range(1,31):
    P=mul(P,M)
    if n<3:continue
    coeff=sum_poly(P[i][i] for i in range(4))
    actual=Counter({k:v for k,v in coeff.items() if v})
    expected=Counter({k:p for (k,w),p in predicted(n,2,4).items() if p})
    assert actual==expected,(n,actual,expected)
print('PASS',28,'complete transfer-matrix polynomial comparisons')
