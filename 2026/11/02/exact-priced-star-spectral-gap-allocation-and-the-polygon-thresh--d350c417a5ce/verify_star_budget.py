#!/usr/bin/env python3
"""Exact checks for heterogeneous-cost spectral-gap design of a weighted star.

All matrix arithmetic is rational; no third-party packages or online services.
The analytic theorem is proved separately. Finite checks are consistency tests.
"""
from fractions import Fraction as F
from itertools import combinations, product
import random

COUNT = 0

def check(condition, message):
    global COUNT
    COUNT += 1
    if not condition:
        raise AssertionError(message)

def determinant(M):
    n = len(M)
    if not n:
        return F(1)
    A = [list(row) for row in M]
    det = F(1)
    for k in range(n):
        pivot = next((j for j in range(k,n) if A[j][k]), None)
        if pivot is None:
            return F(0)
        if pivot != k:
            A[k], A[pivot] = A[pivot], A[k]
            det = -det
        t = A[k][k]
        det *= t
        for j in range(k+1,n):
            ratio = A[j][k]/t
            for h in range(k+1,n):
                A[j][h] -= ratio*A[k][h]
            A[j][k] = F(0)
    return det

def principal_minors_psd(S):
    n = len(S)
    for r in range(1,n+1):
        for idx in combinations(range(n),r):
            M = [[S[i][j] for j in idx] for i in idx]
            check(determinant(M)>=0, ('negative principal minor', idx, M))

def optimum(roots):
    """roots are positive integers, prices are their squares."""
    m=len(roots)
    n=m+1
    s=sum(roots)
    j=max(range(m),key=lambda i:roots[i])
    delta=max(0, 2*roots[j]-s)
    w=[F(1) for _ in roots]
    if delta:
        for i,a in enumerate(roots):
            if i==j:
                w[i]-=F(delta,n*a)
            else:
                w[i]+=F(delta,n*a)
    c=[a*a for a in roots]
    C=sum(c,F(0))-F(delta*delta,n)
    return w,C,j,delta

def verify_case(roots):
    m=len(roots);n=m+1
    w,C,j,delta=optimum(roots)
    check(all(x>0 for x in w),('nonpositive edge',roots))
    check(sum(F(a*a)*x for a,x in zip(roots,w))==C,('cost',roots))
    S=[[((w[i]-1) if i==k else F(0))+F(1,n) for k in range(m)] for i in range(m)]
    principal_minors_psd(S)
    if delta:
        z=[F(a if i==j else -a) for i,a in enumerate(roots)]
        check(sum(z)==delta,('dual resultant',roots))
        check(all(sum(S[i][k]*z[k] for k in range(m))==0 for i in range(m)),('complementary slackness',roots))
        dual=sum(F(a*a) for a in roots)-F(sum(z)**2,n)
        check(dual==C,('duality gap',roots))
        # Explicit Schur identity for j: the reduction is exact, not numerical.
        other=sum(roots)-roots[j]
        check(other>0 and roots[j]-other==delta,('dominance',roots))
    else:
        check(all(x==1 for x in w),('polygon regime',roots))
        check(C==sum(a*a for a in roots),('polygon value',roots))
    # Direct quadratic form identity for x orthogonal to the all-ones vector.
    for y in [[F((i*3+2*j)%7-3) for i in range(m)] for j in range(3)]:
        x0=-sum(y,F(0))/n
        x=[x0]+[yy+x0 for yy in y]
        check(sum(x)==0,('zero sum',roots))
        energy=sum(w[i]*(x[i+1]-x[0])**2 for i in range(m))
        norm=sum(xx**2 for xx in x)
        qform=sum(y[i]*sum(S[i][k]*y[k] for k in range(m)) for i in range(m))
        check(energy-norm==qform,('spectral reduction',roots))


def main():
    # Exhaust all length patterns through four spokes with square prices 1,4,9,16.
    for m in range(2,5):
        for roots in product(range(1,5), repeat=m):
            verify_case(roots)
    # Broader deterministic exact-rational tests through seven spokes.
    rng=random.Random(271828)
    for m in range(5,8):
        for _ in range(24):
            roots=[rng.randrange(1,13) for i in range(m)]
            if _%3==0:
                roots[0]=sum(roots[1:])+rng.randrange(1,5)
            verify_case(roots)
    # Named phase witnesses, including a threshold equality.
    for roots in [(1,1,1),(2,1,1),(3,1,1),(4,1,1),(10,1,2,3),(5,4,3)]:
        verify_case(roots)
    print('VERIFY_OK',COUNT,'exact-rational assertions')

if __name__=='__main__':
    main()
