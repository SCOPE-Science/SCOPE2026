"""Exact-arithmetic checks for a randomized SDIRK two-state positivity law.

The symbolic theorem is proved in RESULT.md. These finite checks are supplementary.
Python 3 standard library only. Run: python verify.py
"""
from fractions import Fraction as F
from math import sqrt, isclose


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]


def scale(t, A):
    return [[t * A[i][j] for j in range(2)] for i in range(2)]


def inv(A):
    d = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    assert d != 0
    return [[A[1][1] / d, -A[0][1] / d], [-A[1][0] / d, A[0][0] / d]]


I = [[F(1), F(0)], [F(0), F(1)]]


def direct_update(a, b, h, x):
    Q = [[-a, a], [b, -b]]
    S = inv(add(I, scale(-h*x, Q)))
    Y1 = S
    Y2 = mul(add(I, scale(h*(1-2*x), mul(Y1,Q))), S)
    return add(I, scale(h/2, mul(add(Y1,Y2),Q)))


def rho(z,x):
    return (1+(2*x-1)*z+(x*x-2*x+F(1,2))*z*z)/(1+x*z)**2


def projector_update(a,b,h,x):
    lam=a+b
    pi=[[b/lam,a/lam],[b/lam,a/lam]]
    J=add(I,scale(-1,pi))
    return add(pi,scale(rho(h*lam,x),J))


def success_probability(z, m):
    z=float(z); m=float(m)
    if m == .5: return 1.
    z0=2/(1-2*m)
    if z<=z0: return 1.
    if m<1/3:
        z1=(1+m+sqrt((1-m)*(3-m)))/(1-3*m)
        if z>=z1: return 0.
    return 2*m+2/z-sqrt(2*(1-m)*((1-2*m)*z-2)/z)


def critical_x(z,m):
    z=float(z);m=float(m)
    return 1-m-1/z+sqrt((1-m)*((1-2*m)*z-2)/(2*z))

checks=0
for ai in range(1,11):
    for bi in range(1,11):
        a=F(ai,7);b=F(bi,9)
        m=min(a,b)/(a+b)
        for hn in (F(1,10),F(1),F(5),F(100)):
            for xi in range(1,11):
                x=F(1,2)+F(xi,20)
                D=direct_update(a,b,hn,x)
                P=projector_update(a,b,hn,x)
                assert D==P
                assert all(sum(D[i])==1 for i in range(2))
                crit=rho(hn*(a+b),x)>=-m/(1-m)
                assert crit==all(D[i][j]>=0 for i in range(2) for j in range(2))
                checks+=1

# Test exact phase boundaries at rational stationary masses and rational z.
for m in (F(1,10),F(1,5),F(1,4),F(1,3),F(2,5),F(9,20),F(1,2)):
    for zi in range(1,301,3):
        z=F(zi,23)
        p=success_probability(z,m)
        assert -1e-11<=p<=1+1e-11,(z,m,p)
        if m<F(1,2):
            z0=2/(1-2*m)
            if z<z0:assert p==1
        # High-resolution midpoint rule estimates the exact probability by direct RK signs.
        count=0
        for j in range(400):
            x=F(1,2)+F(2*j+1,1600)
            count+=(rho(z,x)>=-m/(1-m))
        assert abs(count/400-p)<.00251,(z,m,p,count)
        checks+=1

# Exact boundary examples (the math is established analytically in RESULT.md).
for m in (F(1,10),F(1,4),F(2,5)):
    z0=2/(1-2*m)
    assert rho(z0,F(1,2))==-m/(1-m)
    checks+=1

print('PASS: ',checks, 'checks: rational stage matrices, projectors, row sums, positivity; probability grid; thresholds')
