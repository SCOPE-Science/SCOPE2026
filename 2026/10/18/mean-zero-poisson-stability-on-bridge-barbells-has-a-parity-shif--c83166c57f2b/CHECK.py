#!/usr/bin/env python3
"""Exact rational checks for the barbell graph Poisson-norm theorem.

No non-standard Python modules are required. Finite tests support, but do not
replace, the general algebraic and order-statistic proof in RESULT.md.
"""
from fractions import Fraction as Q


def inverse(A):
    n=len(A)
    B=[[Q(A[i][j]) for j in range(n)]+[Q(int(i==j)) for j in range(n)] for i in range(n)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if B[i][j])
        B[j],B[pivot]=B[pivot],B[j]
        scale=B[j][j]
        B[j]=[x/scale for x in B[j]]
        for i in range(n):
            if i!=j and B[i][j]:
                c=B[i][j]
                B[i]=[x-c*y for x,y in zip(B[i],B[j])]
    return [row[n:] for row in B]


def matrix(a,b):
    n=a+b
    L=[[Q(0) for j in range(n)] for i in range(n)]
    for group in (range(a),range(a,n)):
        for i in group:
            for j in group:
                if i != j:
                    L[i][j]-=1; L[i][i]+=1
    L[0][a]-=1; L[a][0]-=1
    L[0][0]+=1;L[a][a]+=1
    return L


def green_from_inverse(a,b):
    n=a+b; L=matrix(a,b)
    G0=inverse([[L[i][j]+Q(1,n) for j in range(n)] for i in range(n)])
    return [[G0[i][j]-Q(1,n) for j in range(n)] for i in range(n)]


def resistance(i,j,a,b):
    if i==j:return Q(0)
    if i<a and j<a:return Q(2,a)
    if i>=a and j>=a:return Q(2,b)
    return Q(1) + (Q(2,a) if ((i<a and i!=0) or (j<a and j!=0)) else 0) + (Q(2,b) if ((i>=a and i!=a) or (j>=a and j!=a)) else 0)


def green_from_resistance(a,b):
    n=a+b
    R=[[resistance(i,j,a,b) for j in range(n)] for i in range(n)]
    r=[sum(row)/n for row in R]
    mean=sum(r)/n
    return [[(r[i]+r[j]-mean-R[i][j])/2 for j in range(n)] for i in range(n)]


def median_norm(row):
    s=sorted(row)
    c=s[len(s)//2]
    return sum(abs(v-c) for v in row)


def restriction_extremizer(row):
    n=len(row); indices=sorted(range(n),key=lambda j:row[j])
    h=n//2; f=[Q(0)]*n
    for j in indices[:h]:f[j]=-1
    for j in indices[-h:]:f[j]=1
    assert sum(f)==0
    return f


def predictions(a,b):
    assert 2<=a<=b
    n=a+b
    U=Q(2*((a+1)*b*(b+1)-a),n*n)
    if b==a: W=Q(a+2,2)
    elif b==a+1: W=Q((a+1)*(a+2),n)
    else: W=Q(a*b+n+2,n)
    return U,W


def check_pair(a,b):
    n=a+b
    L=matrix(a,b)
    G=green_from_resistance(a,b)
    for i in range(n):
        assert sum(G[i])==0
        for j in range(n):
            assert G[i][j]==G[j][i]
            assert sum(L[i][k]*G[k][j] for k in range(n))==Q(int(i==j))-Q(1,n)
    H=green_from_inverse(a,b)
    assert G==H
    U,W=predictions(a,b)
    rowU=[sum(abs(v) for v in row) for row in G]
    rowW=[median_norm(row) for row in G]
    assert max(rowU)==U and max(rowW)==W
    unrestricted_argmax={i for i,z in enumerate(rowU) if z==U}
    restricted_argmax={i for i,z in enumerate(rowW) if z==W}
    expected={i for i in range(1,a)} if a<b else {i for i in list(range(1,a))+list(range(a+1,n))}
    assert unrestricted_argmax==expected,(a,b,unrestricted_argmax,expected)
    assert restricted_argmax==expected,(a,b,restricted_argmax,expected)
    assert rowW[0]==W-1
    assert rowW[a]==Q(a*a,n)
    assert rowW[a+1]==Q(a,b)*W
    for i in (0,1,a,a+1):
        f=restriction_extremizer(G[i])
        assert sum(G[i][j]*f[j] for j in range(n))==rowW[i]
    return 1


def main():
    checks=0
    for a in range(2,10):
        for b in range(a,17):
            checks+=check_pair(a,b)
    # Exact global maximizers for fixed total order n.
    for n in range(4,101):
        choices=[(a,predictions(a,n-a)[1]) for a in range(2,n//2+1)]
        best=max(v for _,v in choices)
        best_positions=[a for a,v in choices if v==best]
        expected=n//2 if n%2 else (n//2-1 if n>=6 else 2)
        assert best_positions==[expected], (n,best_positions,expected)
        checks+=1
    # Asymptotic ratios are checked exactly at sampled large N.
    for n in (100,1000):
        for a in (2,n//3,n//2):
            U,W=predictions(a,n-a)
            assert abs(Q(U,n)-Q(2*a*(n-a)**2,n**3))<Q(100,n)
            assert abs(Q(W,n)-Q(a*(n-a),n**2))<Q(100,n)
            checks+=1
    print(f'PASS: {checks} parameter families, exact inverse identities, dual-median and extremizer checks')

if __name__=='__main__':main()
