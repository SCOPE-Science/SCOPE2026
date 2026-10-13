#!/usr/bin/env python3
"""Reproduce exact-arithmetic identities and finite checks for bipartite quantum mixing.

Python 3 standard library only. Finite checks corroborate, but do not prove,
statements quantified over all graph orders and all sampling laws.
"""
from fractions import Fraction as Q
from math import acos, cos, sin, sqrt


def probability_blocks(a, b, u, v):
    """Five distinct ordered-pair probabilities under two cosine moments."""
    z = 1-2*u+v
    return (1-2*(1-u)/a+z/a**2, z/a**2,
            1-2*(1-u)/b+z/b**2, z/b**2, (1-v)/(a*b))


def loss(a, b, u, v):
    da, oa, db, ob, cross = probability_blocks(a, b, u, v)
    n = a+b
    h = Q(1, n)
    return (a*(da-h)**2 + a*(a-1)*(oa-h)**2
            + b*(db-h)**2 + b*(b-1)*(ob-h)**2
            + 2*a*b*(cross-h)**2)


def parameters(a, b):
    n, p = a+b, a*b
    return (n, p, 2*p*p-p*(3*n+4)+2*n*n,
            p*(3*n+4)-3*n*n, p*p-p*(3*n+4)+2*n*n)


def gradient(a,b,u,v):
    n,p,C,_,_ = parameters(a,b)
    return (Q(4,p*p)*(C+2*(p*(n+2)-n*n)*u),
            Q(2*n,p*p)*(p-n+n*v))


def cubic(a,b,x):
    n,_,C,K,_ = parameters(a,b)
    return n*n*x*x*x+K*x+C


def matrix_multiply(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


exact_gradients=0
exact_blocks=0
star_cases=0
two_by_many_cases=0
balanced_cases=0
for a in range(1,13):
    for b in range(1,13):
        n,p,C,K,H=parameters(a,b)
        for u,v in [(Q(-1,2),Q(1,3)),(Q(0),Q(1,2)),
                    (Q(2,5),Q(4,7))]:
            h=Q(1,7)
            du=(loss(a,b,u+h,v)-loss(a,b,u-h,v))/(2*h)
            dv=(loss(a,b,u,v+h)-loss(a,b,u,v-h))/(2*h)
            assert (du,dv)==gradient(a,b,u,v)
            exact_gradients+=1
        # Direct cubic adjacency identity, including all degenerate small cases.
        A=[[0 if i==j or (i<a)==(j<a) else 1 for j in range(n)]
           for i in range(n)]
        A2=matrix_multiply(A,A)
        A3=matrix_multiply(A2,A)
        assert A3==[[p*z for z in row] for row in A]
        for x in [Q(-1),Q(-3,5),Q(0),Q(1,3),Q(1)]:
            blocks=probability_blocks(a,b,x,x*x)
            # Independently infer the five probabilities from the exact A^2 entries:
            q=(x-1)/p
            d=Q(1)
            for i in range(n):
                for j in range(n):
                    re=d if i==j else Q(0)
                    re+=q*A2[i][j]
                    sq=re*re+Q(1-x*x,p)*A[i][j]*A[i][j]
                    expected=(blocks[0] if i==j else blocks[1]) if i<a and j<a else (
                        (blocks[2] if i==j else blocks[3]) if i>=a and j>=a else blocks[4])
                    assert sq==expected,(a,b,i,j,x,sq,expected)
                    exact_blocks+=1
for m in range(3,75):
    x=Q(1-m,m+1)
    assert cubic(1,m,x)==0
    assert loss(1,m,x,x*x)==Q(m*(m-3)**2,(m+1)**2)
    gu,gv=gradient(1,m,x,x*x)
    assert gv==Q(2*(m-3),m)
    assert gu==-2*x*gv
    star_cases+=1
for m in range(2,75):
    x=Q(2-m,m+2)
    assert cubic(2,m,x)==0
    assert loss(2,m,x,x*x)==Q((m-2)**2*(m+1),(m+2)**2)
    two_by_many_cases+=1
for r in range(2,75):
    n,p,C,K,H=parameters(r,r)
    assert H==r*r*(r*r-6*r+4)
    assert loss(r,r,Q(-1),Q(1))==Q(2*r**3-17*r**2+48*r-32,r*r)
    assert (H>=0)==(r>=6)
    balanced_cases+=1
assert loss(1,2,Q(0),Q(1,3))==0
assert loss(1,1,Q(0),Q(1,2))==0
assert loss(1,3,Q(-1,2),Q(1,4))==0
assert loss(2,2,Q(0),Q(0))==0
assert loss(1,2,Q(0),Q(0))>0
# For selected large domains independently compare calculated minima with nearby
# feasible two-atom laws (the latter are not proof of global optimization).
finite_variations=0
for a in range(1,10):
    for b in range(1,10):
        if (a,b) in [(1,1),(1,2),(2,1)]:
            continue
        n,p,C,K,H=parameters(a,b)
        if min(a,b)==1:
            mm=max(a,b)
            opt=Q(1-mm,mm+1)
        elif H>=0:
            opt=Q(-1)
        else:
            # Cubic strictly increasing: bisection is only a numerical cross-check.
            l,rr=-1.,0.
            for _ in range(75):
                mid=(l+rr)/2.
                if float(cubic(a,b,mid))<0:l=mid
                else:rr=mid
            opt=(l+rr)/2.
        fmin=float(loss(a,b,opt,opt*opt))
        for x in [-1.,-.7,-.1,.2,.8,1.]:
            for y in [-.9,-.3,.2,1.]:
                u=(x+y)/2
                v=(x*x+y*y)/2
                assert float(loss(a,b,u,v))>=fmin-1e-8
                finite_variations+=1
print('VERIFY_OK exact_gradient_tests=%d exact_matrix_entry_tests=%d '
      'star_formula_tests=%d two_by_many_tests=%d balanced_threshold_tests=%d '
      'feasible_two_atom_tests=%d' % (
      exact_gradients,exact_blocks,star_cases,two_by_many_cases,
      balanced_cases,finite_variations))
