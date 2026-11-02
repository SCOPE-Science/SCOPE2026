#!/usr/bin/env python3
"""Exact independent Kalman-rank checks for weighted friendship networks.

No third-party dependencies. All matrices and operations are integer; rank is
computed over the rationals by exact fractions. These finite checks complement,
but do not replace, the all-parameter eigenspace proof.
"""
from fractions import Fraction
from itertools import combinations, product


def laplacian(m, a, c, b):
    n = 2*m+1
    L = [[0]*n for _ in range(n)]
    def edge(i,j,w):
        L[i][i] += w; L[j][j] += w
        L[i][j] -= w; L[j][i] -= w
    for j in range(m):
        x,y=2*j+1,2*j+2
        edge(0,x,a); edge(0,y,c); edge(x,y,b)
    return L


def rank_q(rows):
    if not rows: return 0
    a=[[Fraction(x) for x in row] for row in rows]
    n=len(a); p=len(a[0]); r=0
    for j in range(p):
        piv=next((i for i in range(r,n) if a[i][j]),None)
        if piv is None: continue
        a[r],a[piv]=a[piv],a[r]
        for i in range(r+1,n):
            if a[i][j]:
                q=a[i][j]/a[r][j]
                for k in range(j+1,p): a[i][k]-=q*a[r][k]
                a[i][j]=0
        r+=1
        if r==n: return r
    return r


def controllability_rank(L, S):
    n=len(L)
    if not S: return 0
    cols=[[int(i==k) for i in range(n)] for k in S]
    allcols=list(cols)
    for _ in range(1,n):
        cols=[[sum(L[i][j]*v[j] for j in range(n)) for i in range(n)] for v in cols]
        allcols.extend(cols)
    return rank_q([[col[i] for col in allcols] for i in range(n)])


def predicted(m,a,c,b,S):
    S=set(S)
    covered={j for j in range(m) if 2*j+1 in S or 2*j+2 in S}
    if a==c:
        if len(covered)<m: return False
        if b==m*a:
            return 0 in S or any((2*j+1 in S and 2*j+2 in S) for j in range(m))
        return True
    if len(covered)<m-1: return False
    if 0 in S: return True
    X=any(2*j+1 in S for j in range(m))
    Y=any(2*j+2 in S for j in range(m))
    if X and not Y and b==m*a: return False
    if Y and not X and b==m*c: return False
    return True


def test():
    count=0
    cases=[]
    for m in (2,3):
        for a,c,b in product((1,2,3),(1,2,3),(1,2,3,4,6)):
            cases.append((m,a,c,b))
    for m,a,c,b in cases:
        L=laplacian(m,a,c,b)
        n=len(L)
        for mask in range(1,1<<n):
            S=[i for i in range(n) if mask>>i&1]
            actual=controllability_rank(L,S)==n
            expected=predicted(m,a,c,b,S)
            assert actual==expected,(m,a,c,b,S,actual,expected)
            count+=1
    # Stress at larger m and both exact nodal conductances.
    for m,a,c,b in [(4,1,2,4),(4,1,2,8),(4,1,2,3),(4,2,2,8),(4,2,2,3),(4,3,1,12)]:
        L=laplacian(m,a,c,b)
        n=len(L)
        allS=[]
        for size in (m-1,m,m+1):
            allS.extend(combinations(range(n),size))
        for S in allS:
            assert (controllability_rank(L,S)==n)==predicted(m,a,c,b,S),(m,a,c,b,S)
            count+=1
    print('PASS: '+str(count)+' exact rational controllability comparisons')


if __name__=='__main__': test()
