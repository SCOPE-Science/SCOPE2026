#!/usr/bin/env python3
"""Exact finite checks for matching-fugacity random spanning trees."""
from fractions import Fraction as Q
from itertools import combinations
from math import comb

checks = 0

def verify(ok, context):
    global checks
    assert ok, context
    checks += 1

def determinant(a):
    a = [[Q(x) for x in row] for row in a]
    n = len(a)
    out = Q(1)
    for k in range(n):
        q = next((i for i in range(k,n) if a[i][k]), None)
        if q is None: return Q(0)
        if q != k:
            a[k],a[q] = a[q],a[k]
            out = -out
        pivot = a[k][k]
        out *= pivot
        for i in range(k+1,n):
            f = a[i][k]/pivot
            for j in range(k+1,n): a[i][j] -= f*a[k][j]
            a[i][k]=Q(0)
    return out

def edges(n,t):
    return [(i,n+j,t if i==j else Q(1)) for i in range(n) for j in range(n)]

def laplacian_minor(n,t,z,root=0):
    N=2*n
    kept=[i for i in range(N) if i!=root]
    index={v:i for i,v in enumerate(kept)}
    L=[[Q(0) for _ in kept] for _ in kept]
    for a,b,w in edges(n,t):
        if root in (a,b):w *= z
        if a!=root: L[index[a]][index[a]] += w
        if b!=root: L[index[b]][index[b]] += w
        if a!=root and b!=root:
            L[index[a]][index[b]]-=w
            L[index[b]][index[a]]-=w
    return L

def eval_poly(n,t,z):
    d=n*n-3*n+1+(2*n-1)*t
    return z*(n-1+t)*(d+(n-1+t)*z)**(n-2)*(n-2+t+t*z)

def law(n,t):
    p=(n-1+t)/(n*(n-2+2*t))
    q=t/(n-2+2*t)
    coeff=[Q(0)]*(n+1)
    for k in range(n-1):
        a=Q(comb(n-2,k))*p**k*(1-p)**(n-2-k)
        coeff[k+1]+=a*(1-q)
        coeff[k+2]+=a*q
    return coeff

def exhaustive(n,t):
    ee=edges(n,t)
    N=2*n
    total=Q(0); root=[Q(0)]*(n+1); leaves=Q(0)
    for chosen in combinations(range(n*n),N-1):
        parents=list(range(N))
        def find(v):
            while parents[v]!=v:v=parents[v]
            return v
        weight=Q(1);deg=[0]*N; good=True
        for i in chosen:
            a,b,w=ee[i]
            aa,bb=find(a),find(b)
            if aa==bb: good=False;break
            parents[aa]=bb
            deg[a]+=1;deg[b]+=1;weight*=w
        if not good:continue
        total+=weight;root[deg[0]]+=weight
        leaves+=weight*sum(d==1 for d in deg)
    return total,[x/total for x in root],leaves/total

for n in range(2,8):
    for t in [Q(1,3),Q(1),Q(5,2),Q(7)]:
        for z in [Q(0),Q(1),Q(2),Q(3,2)]:
            actual=determinant(laplacian_minor(n,t,z))
            verify(actual==eval_poly(n,t,z),('cofactor',n,t,z,actual,eval_poly(n,t,z)))
        prob=law(n,t)
        verify(sum(prob)==1,('mass',n,t))
        mean=sum(d*prob[d] for d in range(len(prob)))
        verify(mean==Q(2)-Q(1,n),('degree-mean',n,t))
        leaf=prob[1]*2*n
        q=t/(n-2+2*t)
        p=(n-1+t)/(n*(n-2+2*t))
        verify(leaf==2*n*(1-q)*(1-p)**(n-2),('leaves',n,t))
        if n>=3:
            var=sum((d-mean)**2*prob[d] for d in range(len(prob)))
            deficit=Q(n-2)*Q(n-1)*(t-1)**2/(n*n*(n-2+2*t)**2)
            verify(var+deficit==Q(n-1)**2/n**2,('variance',n,t))

for n, weights in [(2,[Q(1,2),Q(1),Q(3)]),(3,[Q(1,3),Q(1),Q(3)]),(4,[Q(1,2),Q(2)])]:
    for t in weights:
        total,dist,leaves=exhaustive(n,t)
        verify(total==eval_poly(n,t,1),('exhaustive-Z',n,t))
        verify(dist==law(n,t),('exhaustive-degree',n,t))
        verify(leaves==2*n*law(n,t)[1],('exhaustive-leaves',n,t))

print('VERIFY_OK',checks,'exact rational assertions')
