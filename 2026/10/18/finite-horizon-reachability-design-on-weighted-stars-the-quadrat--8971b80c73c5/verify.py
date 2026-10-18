#!/usr/bin/env python3
"""Exact finite checks for short-horizon star reachability calculations.

No dependencies beyond the Python standard library. The mathematical proof
of the general results is given separately; these checks are finite examples.
"""
from fractions import Fraction as F
from itertools import permutations
from math import factorial

def det(a):
    n = len(a)
    z = F(0)
    for p in permutations(range(n)):
        inv = sum(p[i] > p[j] for i in range(n) for j in range(i+1,n))
        q = F(-1 if inv%2 else 1)
        for i in range(n): q *= a[i][p[i]]
        z += q
    return z

def matmul(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0))
             for j in range(len(b[0]))] for i in range(len(a))]

def convolve(p,q,M):
    r = [F(0)]*(M+1)
    for i,a in enumerate(p):
        if not a: continue
        for j,b in enumerate(q[:M+1-i]):
            if b: r[i+j] += a*b
    return r

def exact_gram_expansion(lam):
    n = len(lam)
    M = n*n+2
    g = []
    for a in lam:
        row=[]
        for b in lam:
            s=[F(0)]*(M+1)
            for k in range(M): s[k+1]=F((a+b)**k, factorial(k+1))
            row.append(s)
        g.append(row)
    coefficients=[F(0)]*(M+1)
    for p in permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        term=[F(1)]+[F(0)]*M
        for i in range(n): term=convolve(term,g[i][p[i]],M)
        sign=-1 if inv%2 else 1
        for k in range(M+1): coefficients[k]+=sign*term[k]
    hilbert=[[F(1,(i+j+1)*factorial(i)*factorial(j)) for j in range(n)] for i in range(n)]
    vand=F(1)
    for i in range(n):
        for j in range(i+1,n): vand*=lam[j]-lam[i]
    lead=det(hilbert)*vand*vand
    s=sum(lam)
    u=sum(t*t for t in lam)
    expected=(lead,lead*s,lead*(F(s*s,2)+F(n,2*(4*n*n-1))*u))
    actual=tuple(coefficients[n*n:n*n+3])
    assert actual==expected, (lam,actual,expected)
    return 3

def star_krylov(weights):
    m=len(weights);n=m+1
    L=[[F(0)]*n for _ in range(n)]
    for i,w in enumerate(weights,1):
        L[0][0]+=w;L[i][i]+=w;L[0][i]-=w;L[i][0]-=w
    A=[[-t for t in row] for row in L]
    cols=[[F(int(i==0)) for i in range(n)]]
    for _ in range(m):
        cols.append([sum((A[i][j]*cols[-1][j] for j in range(n)),F(0)) for i in range(n)])
    K=[[cols[j][i] for j in range(n)] for i in range(n)]
    target=F(1)
    for w in weights: target*=w
    for i in range(m):
        for j in range(i+1,m):target*=weights[j]-weights[i]
    assert abs(det(K))==abs(target), (weights,det(K),target)
    return 1

def main():
    checks=0
    for lam in ((0,2),(1,5),(-3,2),(-2,0,3), (0,1,4),(1,3,7),(-4,-1,0,3),(-2,0,1,5)):
        checks+=exact_gram_expansion(tuple(F(x) for x in lam))
    for m in range(1,6):
        for variant in range(3):
            weights=[F((i+1)**2 + variant*(i+1)) for i in range(m)]
            checks+=star_krylov(weights)
    print('VERIFY_OK',checks,'exact coefficient/determinant identities across',8+15,'finite test instances')
if __name__=='__main__':main()
