#!/usr/bin/env python3
"""Exact arithmetic checks for Euclidean embeddings of three-subset Kneser graphs.

Uses only Python's standard library.  This script checks bounded finite instances;
the unrestricted assertion is proved in RESULT.md.
"""
from fractions import Fraction
from itertools import combinations
from math import comb

COUNT=0

def eq(a,b):
    global COUNT
    COUNT+=1
    assert a == b, (a,b)

def choose(a,b):
    return comb(a,b) if isinstance(a,int) and isinstance(b,int) and 0<=b<=a else 0

def inc_eigen(n,j,i):
    # Coefficient of u_T after applying intersection-i adjacency to u_T, modulo U_{j-1}.
    val=0
    for l in range(j+1):
        count=choose(3-l,3-i-l)*choose(n-3-j+l,i-j+l)
        val += (-1)**(j-l)*comb(j,l)*count
    return val

def spec(n):
    L=comb(n-4,2)
    return [(-L,(n-4)*(n-9)//2,2*n-9),
            (n-5,11-2*n,n-7),
            (-1,3,-3)]

def proposal(n):
    if n==8:
        return (Fraction(3),Fraction(5),Fraction(4),Fraction(3))
    L=comb(n-4,2)
    t=Fraction(4*(L-1),L)
    return (t,Fraction(4),Fraction(4),t)

def psd_rational(matrix):
    # Symmetric congruence elimination by positive Schur-complement pivots.
    # All arithmetic exact; if all remaining diagonals vanish, PSD requires zero matrix.
    m=len(matrix)
    M=[list(row) for row in matrix]
    rank=0
    for k in range(m):
        pivot=next((p for p in range(k,m) if M[p][p]>0),None)
        if pivot is None:
            for a in range(k,m):
                for b in range(a,m):
                    eq(M[a][b],0)
            return rank
        if pivot!=k:
            M[k],M[pivot]=M[pivot],M[k]
            for row in M:
                row[k],row[pivot]=row[pivot],row[k]
        pk=M[k][k]
        assert pk>0
        for a in range(k+1,m):
            for b in range(a,m):
                M[a][b]-=M[a][k]*M[k][b]/pk
                M[b][a]=M[a][b]
        for a in range(k+1,m):
            M[a][k]=M[k][a]=Fraction(0)
        rank+=1
    return rank

def finite_case(n):
    vs=list(combinations(range(n),3))
    N=len(vs)
    x0,x1,x2,t=proposal(n)
    x=(x0,x1,x2)
    for a,b in combinations(vs,2):
        s=len(set(a).intersection(b))
        expected=1 if s==0 else 2
        # An intersecting pair has a common Kneser neighbor iff >=3 unused labels.
        if s:
            eq(n-(6-s)>=3,True)
        d2=x[s]
        eq(d2>=expected**2,True)
        eq(d2<=t*expected**2,True)
    row_sum=sum(comb(3,s)*comb(n-3,3-s)*x[s] for s in range(3))
    D=[[Fraction(0) if i==j else x[len(set(vs[i]).intersection(vs[j]))] for j in range(N)] for i in range(N)]
    for row in D:
        eq(sum(row),row_sum)
    gram=[[(Fraction(row_sum,N)-D[i][j])/2 for j in range(N)] for i in range(N)]
    for i in range(N):
        eq(sum(gram[i]),0)
    rank=psd_rational(gram)
    predicted=(comb(n,2)-n) if n==8 else (N-n)
    eq(rank,predicted)
    return N,rank

for n in range(8,61):
    rows=spec(n)
    for j in (1,2,3):
        for i in (3,2,1):
            eq(inc_eigen(n,j,i),rows[j-1][3-i])
        eq(sum(rows[j-1]),-1)
    x0,x1,x2,t=proposal(n)
    for row in rows:
        eq(sum(a*b for a,b in zip(row,(x0,x1,x2)))<=0,True)
    eq(t>=1,True)
    eq(x0<=t,True)
    eq(x1>=4 and x1<=4*t,True)
    eq(x2>=4 and x2<=4*t,True)
    if n==9:
        # A nonfaithful optimum has distances squared 18/5,5,4;
        # the faithful optimum has squared distances 18/5,4,4.
        for pattern in ((Fraction(18,5),Fraction(4),Fraction(4)),
                        (Fraction(18,5),Fraction(5),Fraction(4))):
            for row in rows:
                eq(sum(a*b for a,b in zip(row,pattern))<=0,True)
            eq(pattern[0],t)
            eq(pattern[1]>=4 and pattern[1]<=4*t,True)
            eq(pattern[2]>=4 and pattern[2]<=4*t,True)
    if n>=9:
        L=comb(n-4,2)
        eq(x0,Fraction(4*(L-1),L))
        eq(rows[0][1]>=0,True)
        eq(rows[0][2]>0,True)
    else:
        eq(rows[0],(-6,-2,7))
        eq(rows[2],(-1,3,-3))

# Exhaustive PSD/metric checks; n<=10 keeps the independent rational Schur test small.
finite=[]
for n in (8,9,10):
    finite.append((n,)+finite_case(n))
print('CHECK_OK',COUNT,'exact assertions; checked (n,vertices,Gram-rank)=',finite)
