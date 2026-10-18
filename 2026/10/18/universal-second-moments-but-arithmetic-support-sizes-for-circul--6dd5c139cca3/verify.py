#!/usr/bin/env python3
"""Exact finite permutation checks for a circular correlogram covariance theorem."""
from fractions import Fraction as F
from itertools import permutations, combinations_with_replacement
from math import factorial, gcd

checks = 0

def require(x, y, label):
    global checks
    checks += 1
    if x != y:
        raise AssertionError((label, x, y))

def lam_value(a):
    n=len(a); mean=F(sum(a),n)
    x=[F(t)-mean for t in a]
    q=sum(z*z for z in x); r=sum(z**4 for z in x)
    return F((n*n-3*n+3)*q*q - n*(n-1)*r, (n-1)*(n-2)*(n-3))

def predicted(a):
    n=len(a); h=n//2; m=h if n%2==0 else h
    lam=lam_value(a)
    v=[[F(0) for _ in range(m)] for _ in range(m)]
    for i in range(m):
        for j in range(m):
            if n%2==0 and i==h-1 and j==h-1:
                v[i][j]=lam*F(n-2,2*(n-1))
            elif n%2==0 and (i==h-1 or j==h-1):
                v[i][j]=-lam*F(1,n-1)
            else:
                v[i][j]=lam*F(n-3,n-1) if i==j else -lam*F(2,n-1)
    return v

def empirical(a):
    n=len(a); m=n//2; counts=[0]*m; cross=[[0]*m for _ in range(m)]; N=0
    for perm in permutations(a):
        N += 1
        c=[]
        for d in range(1,m+1):
            if n%2==0 and d==m:
                t=sum(perm[i]*perm[i+d] for i in range(m))
            else:
                t=sum(perm[i]*perm[(i+d)%n] for i in range(n))
            c.append(t)
        for i in range(m):
            counts[i]+=c[i]
            for j in range(m):
                cross[i][j]+=c[i]*c[j]
    assert N==factorial(n)
    return [[F(cross[i][j],N)-F(counts[i],N)*F(counts[j],N) for j in range(m)] for i in range(m)]

for n in range(4,9):
    data=[list(range(n)), [0]*(n-1)+[3], [0]*(n-2)+[1,2], [-3,1,1,2]+[0]*(n-4)]
    for k,a in enumerate(data):
        e=empirical(a); p=predicted(a)
        for i in range(n//2):
            for j in range(n//2):
                require(e[i][j],p[i][j],('cov',n,k,i,j))
            require(sum(e[i]),0,('row_zero',n,k,i))
        l=lam_value(a)
        require(l>=0,True,('nonneg',n,k))
        single=len(set(a))==1 or max(a.count(t) for t in set(a))>=n-1
        require(l==0,single,('degenerate',n,k))

for n in range(4,13):
    for tup in combinations_with_replacement(range(3),n):
        l=lam_value(tup)
        isdegenerate=len(set(tup))==1 or max(tup.count(t) for t in set(tup))>=n-1
        require(l==0,isdegenerate,('classification',n,tup))


# Exact support and equal multiplicities using binary-digit separated data.
# Product 2**(2**i) * 2**(2**j) occupies a unique binary digit,
# so a sum of pair products represents the graph's edge set injectively.
for n in range(4,9):
    a = [2**(2**i) for i in range(n)]
    m=n//2
    supports=[{} for _ in range(m)]
    joint={}
    for perm in permutations(a):
        scores=[]
        for d in range(1,m+1):
            if n%2==0 and d==m:
                val=sum(perm[i]*perm[i+d] for i in range(m))
            else:
                val=sum(perm[i]*perm[(i+d)%n] for i in range(n))
            supports[d-1][val]=supports[d-1].get(val,0)+1
            scores.append(val)
        key=tuple(scores)
        joint[key]=joint.get(key,0)+1
    require(len(joint),factorial(n)//(2*n),('joint_support',n))
    require(set(joint.values()),{2*n},('joint_atoms',n))
    for d in range(1,m+1):
        g=gcd(n,d); ell=n//g
        aut=(2*ell)**g*factorial(g) if ell>=3 else 2**g*factorial(g)
        require(len(supports[d-1]),factorial(n)//aut,('lag_support',n,d))
        require(set(supports[d-1].values()),{aut},('lag_atoms',n,d))

print('VERIFY_OK',checks,'exact assertions')
