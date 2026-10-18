#!/usr/bin/env python3
"""Exact rational checks for round John ellipsoids of edge-transitive matching polytopes.
No external dependencies. Run: python check_john.py
"""
from fractions import Fraction as F

def inverse(a):
    n=len(a)
    a=[[F(z) for z in row]+[F(int(i==j)) for j in range(n)] for i,row in enumerate(a)]
    for k in range(n):
        j=next(j for j in range(k,n) if a[j][k])
        a[k],a[j]=a[j],a[k]
        v=a[k][k];a[k]=[x/v for x in a[k]]
        for j in range(n):
            if j!=k:
                v=a[j][k]
                a[j]=[x-v*y for x,y in zip(a[j],a[k])]
    return [row[n:] for row in a]

def matmul(A,B):
    return [[sum((a*b for a,b in zip(row,col)),F(0)) for col in zip(*B)] for row in A]

def trans(A):return [list(row) for row in zip(*A)]

def verify(name,n,d,edges):
    m=len(edges); D=m-2*n+1
    assert d>=2 and m==n*d and D>=1
    assert len(set(edges))==m
    assert all(0<=i<n and 0<=j<n for i,j in edges)
    assert all(sum(i==x for i,j in edges)==d for x in range(n))
    assert all(sum(j==x for i,j in edges)==d for x in range(n))
    # Signed incidence, omit the last row (the sole linear dependence).
    A=[[F(int(i==v)) for i,j in edges] for v in range(n)]+[[-F(int(j==v)) for i,j in edges] for v in range(n-1)]
    Gram=matmul(A,trans(A)); invG=inverse(Gram)
    P0=matmul(matmul(trans(A),invG),A)
    P=[[F(int(i==j))-P0[i][j] for j in range(m)] for i in range(m)]
    assert P==matmul(P,P)
    assert sum(P[i][i] for i in range(m))==D
    assert all(sum(row)==0 for row in P)
    p2=F(D,m)
    assert all(P[i][i]==p2 for i in range(m)), (name,[P[i][i] for i in range(m)])
    # contact covariance: sum_e (P e)(P e)^T = P
    assert matmul(P,P)==P
    # coordinate projection leads to radius squared (1/d)^2 / p2
    radius_squared=F(1,d*d)/p2
    assert radius_squared == F(n,d*D)
    # From each coordinate inequality, the candidate tangent point is feasible:
    # x*=1/d, contact x_e = x* - (1/d)/p2 * P[:,e].
    for e in range(m):
        x=[F(1,d)-F(1,d)/p2*P[f][e] for f in range(m)]
        assert x[e]==0
        assert min(x)>=0,(name,e,min(x))
        assert all(sum(x[t] for t,(i,j) in enumerate(edges) if i==a)==1 for a in range(n))
        assert all(sum(x[t] for t,(i,j) in enumerate(edges) if j==b)==1 for b in range(n))
    print('%s: n=%d d=%d edges=%d dim=%d projected_norm_sq=%s radius_sq=%s contacts=%d' % (name,n,d,m,D,p2,radius_squared,m))


def crown(n):return [(i,j) for i in range(n) for j in range(n) if i!=j]
def complete(n):return [(i,j) for i in range(n) for j in range(n)]
def cube(k):
    L=[v for v in range(1<<k) if v.bit_count()%2==0]
    R=[v for v in range(1<<k) if v.bit_count()%2==1]
    ri={v:i for i,v in enumerate(R)}
    return [(i,ri[v^(1<<a)]) for i,v in enumerate(L) for a in range(k)]

def cycle(n):return [(i,i) for i in range(n)]+[(i,(i+1)%n) for i in range(n)]

if __name__=='__main__':
    verify('C6',3,2,cycle(3))
    verify('K33',3,3,complete(3))
    verify('C8',4,2,cycle(4))
    verify('crown4=Q3',4,3,crown(4))
    verify('crown5',5,4,crown(5))
    verify('Q4',8,4,cube(4))
    print('EXACT_RATIONAL_CHECKS_PASS')
