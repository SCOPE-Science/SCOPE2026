#!/usr/bin/env python3
"""Exact finite checks of terminal-sibling pair moments in uniform recursive trees.

Run with Python 3.10+; requires only the standard library. Finite enumeration
checks the derivation but the all-n theorem follows from exact recurrences.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb, factorial

checks = 0

def verify(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

# Brute-force all (n-1)! rooted recursive trees for n <= 8.
for n in range(2, 9):
    totals = {key:0 for key in ('X', 'Y', 'Z', 'XX', 'XY', 'YY')}
    msum = [0] * n
    count = 0
    for parents in product(*(range(j) for j in range(1, n))):
        p = (-1, *parents)
        children = [0]*n
        for j in range(1, n):
            children[p[j]] += 1
        leaf_children = [0]*n
        for j in range(1,n):
            if children[j] == 0:
                leaf_children[p[j]] += 1
        X = sum(leaf_children)
        Y = sum(comb(v,2) for v in leaf_children)
        Z = sum(comb(v,3) for v in leaf_children)
        vals = dict(X=X,Y=Y,Z=Z,XX=X*X,XY=X*Y,YY=Y*Y)
        for key in totals:
            totals[key] += vals[key]
        for r in range(1,n):
            msum[r] += sum(comb(v,r) for v in leaf_children)
        count += 1
    verify(count == factorial(n-1), f'tree count {n}')
    E = {key: Q(val,count) for key,val in totals.items()}
    verify(E['X'] == Q(n,2), f'E[X] n={n}')
    if n>=3:
        verify(E['Y'] == Q(n,6), f'E[Y] n={n}')
        verify(E['XX'] - E['X']**2 == Q(n,12), f'Var X n={n}')
    if n>=4:
        verify(E['XY'] - E['X']*E['Y'] == Q(n,8), f'Cov X,Y n={n}')
    if n>=5:
        verify(E['YY'] - E['Y']**2 == Q(59*n,180), f'Var Y n={n}')
    for r in range(1,n):
        verify(Q(msum[r],count) == Q(n,factorial(r+1)), f'factorial binomial moment n={n},r={r}')

# Check the exact conditional increment identities on every realized tree.
for n in range(2,8):
    for parents in product(*(range(j) for j in range(1,n))):
        p = (-1,*parents)
        children = [0]*n
        for j in range(1,n):
            children[p[j]] += 1
        lc=[0]*n
        for j in range(1,n):
            if children[j]==0:lc[p[j]]+=1
        X=sum(lc);Y=sum(comb(v,2) for v in lc);Z=sum(comb(v,3) for v in lc)
        dX=[];dY=[]
        for u in range(n):
            pp = p + (u,)
            out=[0]*(n+1)
            for j in range(1,n+1):out[pp[j]]+=1
            lc2=[0]*(n+1)
            for j in range(1,n+1):
                if out[j]==0:lc2[pp[j]]+=1
            dX.append(sum(lc2)-X)
            dY.append(sum(comb(v,2) for v in lc2)-Y)
        verify(sum(dX)==n-X, f'drift X n={n}')
        verify(sum(dY)==X-2*Y, f'drift Y n={n}')
        verify(sum(a*a for a in dX)==n-X, f'square X n={n}')
        verify(sum(a*b for a,b in zip(dX,dY))==X, f'cross X,Y n={n}')
        verify(sum(v*v for v in dY)==X+4*Y+6*Z, f'square Y n={n}')

# The derived moment polynomials solve their one-step linear recurrences.
for n in range(5,201):
    x=Q(n,2);y=Q(n,6);z=Q(n,24)
    A=Q(n*n,4)+Q(n,12)
    B=Q(n*n,12)+Q(n,8)
    C=Q(n*n,36)+Q(59*n,180)
    N=n+1
    verify((1-Q(2,n))*A+2*x+1-x/n == Q(N*N,4)+Q(N,12),f'XX recurrence {n}')
    verify((1-Q(3,n))*B+A/n+y+x/n == Q(N*N,12)+Q(N,8),f'XY recurrence {n}')
    verify((1-Q(4,n))*C+2*B/n+(x+4*y+6*z)/n == Q(N*N,36)+Q(59*N,180),f'YY recurrence {n}')

# Exact covariance is positive definite (not a degeneracy).
verify(Q(1,12)*Q(59,180)-Q(1,8)**2 == Q(101,8640), 'positive definite covariance')
print(f'PASS: {checks} exact integer/rational assertions; n=2..8 exhaustive; polynomial recurrences n=5..200.')
