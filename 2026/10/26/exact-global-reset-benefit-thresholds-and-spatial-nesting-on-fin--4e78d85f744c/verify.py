#!/usr/bin/env python3
"""Exact reproducibility checks for the finite-cycle reset threshold theorem.

Uses only the Python standard library; finite checks are not the global proof.
"""
from fractions import Fraction
from math import floor


def convolve(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def polynomial(m, a):
    b = m - a
    h = convolve(convolve([1, 0, 1], [1]*a), [1]*b)
    h[a] -= a*b
    h[b] -= a*b
    # Division by (1-r)^2: cumulative sums twice.
    p = []
    for k in range(m-1):
        p.append(sum((k-j+1)*h[j] for j in range(k+1)))
    assert convolve(p, [1, -2, 1]) == h
    return p


def solve_linear(A, y):
    A = [list(map(Fraction, row)) + [Fraction(rhs)] for row, rhs in zip(A, y)]
    n=len(A)
    for j in range(n):
        pivot=next(i for i in range(j,n) if A[i][j])
        A[j],A[pivot]=A[pivot],A[j]
        den=A[j][j]
        A[j]=[v/den for v in A[j]]
        for i in range(n):
            if i!=j:
                fac=A[i][j]
                A[i]=[u-fac*v for u,v in zip(A[i],A[j])]
    return [row[-1] for row in A]


def direct_mean(m,d,q):
    states=[i for i in range(m) if i!=d]
    indices={s:j for j,s in enumerate(states)}
    A=[]
    for x in states:
        row=[Fraction(int(x==s)) for s in states]
        row[indices[0]]-=q
        for y in ((x+1)%m,(x-1)%m):
            if y!=d:
                row[indices[y]]-= (1-q)/2
        A.append(row)
    return solve_linear(A,[1]*len(states))[indices[0]]


def sum_poly(r,n):
    return sum((r**k for k in range(n)),Fraction(0))


def rational_mean(m,d,r):
    q=(1-r)**2/(1+r*r)
    exact=(1+r*r)*sum_poly(r,d)*sum_poly(r,m-d)/(r**d+r**(m-d))
    return q,exact


if __name__=='__main__':
    checked=0
    for m in range(3,36):
        for a in range(1,m//2+1):
            b=m-a
            p=polynomial(m,a)
            assert len(p)==m-1 and p[0]==p[-1]==1 and p==p[::-1]
            h=(m-2)//2
            for k in range(h+1):
                if k<a:
                    want=Fraction((k+1)**3+2*(k+1),3)
                else:
                    t=k-a+1
                    want=a*(t*t+(a-b)*t+Fraction(a*a+2,3))
                assert p[k]==want,(m,a,k,p[k],want)
            assert sum(p)==Fraction(-a*b*(m*m-5*a*b-5),6)
            signs=[1 if u>0 else -1 for u in p if u]
            assert sum(signs[i]!=signs[i-1] for i in range(1,len(signs)))<=2
            checked+=1
    matrices=0
    for m in range(3,10):
        for d in range(1,m//2+1):
            for r in [Fraction(1,3),Fraction(2,3)]:
                q,pred=rational_mean(m,d,r)
                assert direct_mean(m,d,q)==pred,(m,d,q)
                matrices+=1
    print('PASS',checked,'exact polynomial certificates and',matrices,'exact matrix mean identities')
