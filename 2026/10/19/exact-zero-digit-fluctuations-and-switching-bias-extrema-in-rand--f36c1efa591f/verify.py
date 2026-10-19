#!/usr/bin/env python3
"""Exact finite-cylinder checks for the alpha=1 random symmetric doubling maps.

Uses only Python's standard library. Each branch is propagated independently
as a true affine image of an interval, not inferred from a precomputed sign
transition matrix. This checks the branch coding and finite-N generating laws;
long-time conclusions are proved analytically in RESULT.md.
"""
from collections import defaultdict
from fractions import Fraction as Q

ZERO = Q(0)
ONE = Q(1)
HALF = Q(1, 2)

# (map selection, source lower, source upper, affine offset, zero digit)
# On each branch, T(x)=2*x+offset. Intervals are understood up to null endpoints.
BRANCHES = [
    (0, Q(-1), -HALF, Q(1), 0),
    (0, -HALF, ZERO, Q(1), 0),
    (0, ZERO, HALF, ZERO, 1),
    (0, HALF, ONE, Q(-1), 0),
    (1, Q(-1), -HALF, Q(1), 0),
    (1, -HALF, ZERO, ZERO, 1),
    (1, ZERO, HALF, Q(-1), 0),
    (1, HALF, ONE, Q(-1), 0),
]


def poly_mul(a, b):
    z = defaultdict(Q)
    for i, x in a.items():
        for j, y in b.items():
            z[i+j] += x*y
    return {k:v for k,v in z.items() if v}


def row_mat_product(v, matrix):
    out = [defaultdict(Q), defaultdict(Q)]
    for source in range(2):
        for target in range(2):
            p = poly_mul(v[source], matrix[source][target])
            for deg, coef in p.items():
                out[target][deg] += coef
    return [{k:v for k,v in a.items() if v} for a in out]


def matrix_pgf(p, n):
    q = ONE-p
    m = [[{0:HALF, 1:q*HALF}, {0:p*HALF}],
         [{0:q*HALF}, {0:HALF, 1:p*HALF}]]
    v = [{0:q}, {0:p}]
    for _ in range(n):
        v = row_mat_product(v, m)
    z = defaultdict(Q)
    for comp in v:
        for k, val in comp.items():
            z[k] += val
    return dict(z)


def direct_affine_pgf(p, n):
    q=ONE-p
    # The initial stationary density equals q on [-1,0] and p on [0,1].
    # The state holds (interval lower, interval upper, digit count): density.
    state = {(Q(-1), ZERO, 0):q, (ZERO, ONE, 0):p}
    for _ in range(n):
        new = defaultdict(Q)
        for (a,b,k), den in state.items():
            for sel,lo,hi,offset,digit in BRANCHES:
                left=max(a,lo)
                right=min(b,hi)
                if not (left < right):
                    continue
                w=p if sel==0 else q
                nl=2*left+offset
                nr=2*right+offset
                assert nr-nl==2*(right-left)
                assert (nl,nr) in ((Q(-1),ZERO),(ZERO,ONE))
                new[(nl,nr,k+digit)] += den*w*HALF
        state=dict(new)
    totals=defaultdict(Q)
    for (a,b,k),den in state.items():
        totals[k]+=den*(b-a)
    return dict(totals)


def exact_moments(p,n):
    vals=direct_affine_pgf(p,n)
    mean=sum(Q(k)*v for k,v in vals.items())
    variance=sum((Q(k)-mean)**2*v for k,v in vals.items())
    return mean,variance


def check():
    total=0
    for p in (Q(1,11),Q(1,5),Q(1,3),Q(1,2),Q(3,5),Q(5,6),Q(10,11)):
        h=p*(ONE-p)
        mu=HALF-h
        gamma=Q(1,4)+h-5*h*h
        for n in range(0,11):
            direct=direct_affine_pgf(p,n)
            matrix=matrix_pgf(p,n)
            assert direct==matrix, ('PGF disagreement',p,n,direct,matrix)
            assert sum(direct.values())==ONE
            assert all(v>=0 for v in direct.values())
            total+=3
            if n>=1:
                mean,var=exact_moments(p,n)
                target=n*gamma-2*h*(ONE-4*h)*(ONE-Q(1,2)**n)
                assert mean==n*mu,(p,n,mean,n*mu)
                assert var==target,(p,n,var,target)
                total+=2
        if p==HALF:
            for n in range(11):
                from math import comb
                vals=matrix_pgf(p,n)
                assert vals=={k:Q(comb(n,k)*3**(n-k),4**n) for k in range(n+1) if comb(n,k)},n
                total+=1
    # Direct exact check of geometric finite lag covariance, via PGF of two marks.
    for p in (Q(1,7),Q(1,4),Q(1,2),Q(2,3),Q(6,7)):
        q=ONE-p;h=p*q
        T=((ONE-p/2,p/2),(q/2,(ONE+p)/2))
        R=((q/2,ZERO),(ZERO,p/2))
        v=[q,p]
        mu=HALF-h
        for k in range(1,11):
            # v R T^(k-1) R 1, no stationary projectors assumed.
            x=[v[0]*R[0][0],v[1]*R[1][1]]
            for _ in range(k-1):
                x=[x[0]*T[0][0]+x[1]*T[1][0],x[0]*T[0][1]+x[1]*T[1][1]]
            actual=x[0]*R[0][0]+x[1]*R[1][1]-mu*mu
            expected=h*(ONE-4*h)*Q(1,4)*Q(1,2)**(k-1)
            assert actual==expected,(p,k,actual,expected)
            total+=1
    assert Q(1,4)+Q(1,10)-5*Q(1,10)**2==Q(3,10)
    assert Q(1,4)+Q(1,4)-5*Q(1,4)**2==Q(3,16)
    total+=2
    print('PASS: %d exact checks (direct interval-affine cylinders, matrix PGF, finite variances, covariances, extrema).'%total)

if __name__=='__main__': check()
