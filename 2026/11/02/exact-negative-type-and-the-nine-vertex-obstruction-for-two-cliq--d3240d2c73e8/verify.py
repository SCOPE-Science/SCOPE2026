#!/usr/bin/env python3
"""Exact-rational checks for the p-negative-type clique-overlap formula.

Checks individual powered-distance quadratic forms by an independent
full-vertex Gram-matrix Schur-complement algorithm. Here q=2**p is
represented directly as a rational number; off-diagonal distances
have powered values 1 or q.
"""
from fractions import Fraction
from itertools import product


def distance_matrix(h, a, b, q):
    n=h+a+b
    labels=[0]*h+[1]*a+[2]*b
    return [[Fraction(0) if i==j else (q if {labels[i],labels[j]}=={1,2} else Fraction(1))
             for j in range(n)] for i in range(n)]


def is_psd_gram(h, a, b, q):
    d=distance_matrix(h,a,b,q)
    n=len(d)
    k=n-1
    # Gram for vectors x_i-x_last, with squared distances d^p.
    M=[[ (d[i][n-1]+d[j][n-1]-d[i][j])/2 for j in range(k)] for i in range(k)]
    while M:
        j=next((i for i in range(len(M)) if M[i][i]>0),None)
        if j is None:
            return all(M[i][j]==0 for i in range(len(M)) for j in range(len(M)))
        p=M[j][j]
        v=[M[i][j] for i in range(len(M)) if i!=j]
        idx=[i for i in range(len(M)) if i!=j]
        M=[[M[i][k]-M[i][j]*M[j][k]/p for k in idx] for i in idx]
    return True


def predicted(h,a,b,q):
    x=Fraction(1,h)+Fraction(1,a)
    y=Fraction(1,h)+Fraction(1,b)
    off=q-Fraction(1)-Fraction(1,h)
    return off*off<=x*y


def check():
    tests=0
    # All split pairs of order at most 11, h at least 2, and
    # a nonuniform grid of rational distance powers.
    qs=[Fraction(1),Fraction(6,5),Fraction(3,2),Fraction(17,10),
        Fraction(9,5),Fraction(19,10),Fraction(2),Fraction(21,10),
        Fraction(5,2),Fraction(3),Fraction(4)]
    for h in range(2,10):
        for a in range(1,11-h):
            for b in range(1,11-h-a+1):
                for q in qs:
                    full=is_psd_gram(h,a,b,q)
                    reduced=predicted(h,a,b,q)
                    assert full==reduced,(h,a,b,q,full,reduced)
                    tests+=1
    # At exponent p=1, compare two independent integer criteria.
    p1tests=0
    for h in range(1,30):
        for a in range(1,20):
            for b in range(1,20):
                assert predicted(h,a,b,Fraction(2)) == ((h-2)*a*b<=h+a+b)
                p1tests+=1
    # Minimal-order classification: check all complete clique overlaps,
    # without identifying graphs under A/B exchange.
    low=[]; nine=[]
    for n in range(3,10):
        for h in range(2,n-1):
            for a in range(1,n-h):
                b=n-h-a
                if b<a: continue
                if (h-2)*a*b>n:
                    (nine if n==9 else low).append((h,a,b))
    assert low==[], low
    assert nine==[(4,2,3),(5,2,2)], nine
    print('Exact full-Gram/Schur tests:',tests)
    print('Exact one-negative-type integer-criterion tests:',p1tests)
    print('Minimal counterexample order 9:',nine)
    print('All verification assertions passed.')

if __name__=='__main__':
    check()
