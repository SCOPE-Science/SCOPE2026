#!/usr/bin/env python3
"""Exact rational checks of finite instances for the even-stage Gauss end-step."""
from fractions import Fraction as F
from math import factorial


def coeffs(s):
    return [F(factorial(s)*factorial(2*s-j),factorial(2*s)*factorial(s-j)*factorial(j)) for j in range(s+1)]

def eye(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def zero(n): return [[F(0) for _ in range(n)] for _ in range(n)]
def add(a,b): return [[x+y for x,y in zip(u,v)] for u,v in zip(a,b)]
def mul(a,b):
    n=len(a)
    return [[sum((a[i][k]*b[k][j] for k in range(n)),F(0)) for j in range(n)] for i in range(n)]
def scale(a,c):return [[c*x for x in row] for row in a]
def inv(a):
    n=len(a)
    z=[row[:] + u for row,u in zip(a,eye(n))]
    for k in range(n):
        p=next(j for j in range(k,n) if z[j][k])
        z[k],z[p]=z[p],z[k]
        d=z[k][k];z[k]=[x/d for x in z[k]]
        for j in range(n):
            if j!=k:
                d=z[j][k]
                z[j]=[x-d*y for x,y in zip(z[j],z[k])]
    return [row[n:] for row in z]
def lap(parts):
    n=sum(parts)
    a=zero(n)
    labels=sum(([i]*r for i,r in enumerate(parts)),[])
    for i in range(n):
        for j in range(i):
            if labels[i]!=labels[j]:
                a[i][j]=a[j][i]=-1
                a[i][i]+=1;a[j][j]+=1
    return a

def polynomial(coeff,a):
    n=len(a)
    out=zero(n)
    for c in reversed(coeff):out=add(mul(a,out),scale(eye(n),c))
    return out

def stability(s,x):
    cs=coeffs(s)
    q=lambda y:sum((c*y**j for j,c in enumerate(cs)),F(0))
    return q(-x)/q(x)

def step(s,a,h):
    ah=scale(a,F(h));c=coeffs(s)
    return mul(polynomial([v*(-1)**j for j,v in enumerate(c)],ah),inv(polynomial(c,ah)))


def run():
    checked_coef=0
    for s in range(1,36):
        c=coeffs(s)
        e=c[::2];o=c[1::2]
        for i in range(len(e)):
            for j in range(i):
                lhs=e[i]* (o[j] if j<len(o) else 0)-e[j]*(o[i] if i<len(o) else 0)
                assert lhs>=0,(s,i,j)
                if i<len(o):assert lhs>0,(s,i,j)
                checked_coef+=1
        for x in (F(1,20),F(1),F(17),F(1000)):
            r=stability(s,x)
            assert -1<r<1
            if s%2==0:assert r>0
    comparisons=0;positive_entries=0
    families=((1,1),(1,2),(2,3),(1,1,1),(1,2,1),(2,2,3),(1,2,3,1),(3,3,3),(2,1,2,2))
    for s in (2,4,6,8):
        for parts in families:
            n=sum(parts);l=lap(parts)
            for h in (F(1,4), F(1),F(4),F(100)):
                t=step(s,l,h)
                labels=sum(([i]*r for i,r in enumerate(parts)),[])
                for i in range(n):
                    assert sum(t[i])==1,(s,parts,h,i)
                    for j in range(n):
                        assert t[i][j]>0,(s,parts,h,i,j,t[i][j])
                        positive_entries+=1
                        if i!=j:
                            r=parts[labels[i]]
                            delta=(1-stability(s,F(n*h)))/n if labels[i]!=labels[j] else ((1-stability(s,F((n-r)*h)))-F(n-r,n)*(1-stability(s,F(n*h))))/r
                            assert t[i][j]==delta,(s,parts,h,i,j)
                            comparisons+=1
    neg_odd=0;neg_path=0
    for s in (1,3,5,7):
        t=step(s,lap((1,1,1)),F(10000))
        for i in range(3):
            assert t[i][i]<0,(s,i,t[i][i])
            neg_odd+=1
    path=zero(4)
    for i in range(3):
        path[i][i]+=1;path[i+1][i+1]+=1;path[i][i+1]=path[i+1][i]=-1
    for s in (2,4,6,8):
        t=step(s,path,F(10000))
        assert t[0][1]<0,(s,t[0][1]);neg_path+=1
    print('VERIFY_OK coefficient_pairs=%d positive_entries=%d projector_comparisons=%d odd_diagonal_witnesses=%d path_witnesses=%d' % (checked_coef,positive_entries,comparisons,neg_odd,neg_path))

if __name__=='__main__':run()
