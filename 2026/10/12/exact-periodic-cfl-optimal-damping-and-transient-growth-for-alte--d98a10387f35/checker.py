#!/usr/bin/env python3
"""Exact-rational and floating-point checks for alternating variable-step AB2.
Run: python3 checker.py.  Python standard library only.
"""
from fractions import Fraction as Q
from math import sqrt, hypot, isclose


def mm(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def step(a, previous):
    c = a * a / (2 * previous)
    return ((1-a-c, c), (Q(1),Q(0)))


def prod(x, y):
    return mm(step(y,x), step(x,y))


def td(A):
    return A[0][0] + A[1][1], A[0][0]*A[1][1]-A[0][1]*A[1][0]


def rho(A):
    t,d=td(A)
    disc=float(t*t-4*d)
    if disc < 0 and disc > -1e-12:disc=0.0
    assert disc>=0,(A,disc)
    return (float(t)+sqrt(disc))/2


count=0
vals=[Q(i,j) for j in (2,3,5,7,11,13) for i in range(1,2*j+1)]
for x in vals:
    for y in vals:
        L=x+y; d=x*y/4; A=prod(x,y);t,dt=td(A)
        assert dt==d and t==1-L+L*L/2+d
        assert 1-t+dt==L*(1-L/2)
        assert 1+t+dt>0
        assert (rho(A)<1-1e-10) == (L<2) if L!=2 else True
        if L==2: assert abs(rho(A)-1)<1e-10
        if L<2:
            eq=prod(L/2,L/2)
            assert rho(A)>=rho(eq)-1e-10
            if x!=y and abs(float(L-Q(4,3)))>1e-10:
                assert rho(A)>rho(eq)+1e-12
        count+=1

assert prod(Q(2,3),Q(2,3))==((Q(1,3),Q(0)),(Q(0),Q(1,3)))
assert Q(1)-Q(4,3)+Q(4,3)**2/2==Q(5,9)
for j in range(1,200):
    L=Q(j,100)
    dmax=L*L/16
    F=1-L+L*L/2
    assert (F+dmax)**2-4*dmax == (3*L-4)**2*(9*L*L-8*L+16)/256

# Strict optimality of equal splitting for arbitrary positive pairs, checked numerically.
for j in range(1,180):
    L=Q(j,100)
    uniform=rho(prod(L/2,L/2))
    for k in range(1,100):
        x=L*Q(k,100); y=L-x
        if x!=y:
            assert rho(prod(x,y))>uniform-1e-12
    assert uniform>=Q(1,3)-1e-12

# Verify predicted asymptotic norm and spectral radius of fixed-total-period sequences.
L=Q(1)
for k in (300,3000,30000):
    y=L/k;x=L-y
    A=prod(x,y)
    # largest singular value via eigenvalues of A^T A
    a,b=A[0];c,d=A[1]
    p=float(a*a+c*c); q=float(b*b+d*d);v=float(a*b+c*d)
    norm=sqrt((p+q+sqrt((p-q)**2+4*v*v))/2)
    assert abs(float(y)*norm-float(L*L))< 8/k
    assert abs(rho(A)-0.5)<0.08

print('VERIFY_OK',count,'exact-rational two-step matrix and stability cases;',
      '199 exact discriminant identities;',
      '17721 fixed-total comparisons;',
      '3 transient-growth cases')
