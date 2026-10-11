#!/usr/bin/env python3
"""Numerical and exact-algebra checks for the sharp harmonic L2 Landau radius.
Only supplementary finite checks; the general theorem follows from the proof.
"""
from fractions import Fraction
from math import isclose


def S(r):
    t = r*r
    return t*(4-3*t+t*t)/(1-t)**3


def root(M):
    if M == 1:
        return 1.0
    a,b = 0.,1.
    for _ in range(180):
        x=(a+b)/2
        if 2*(M*M-1)*S(x) > 1:
            b=x
        else:
            a=x
    return (a+b)/2


def exact_sum(r):
    # Check partial sums at four rational arguments; this is not a proof
    # of the infinite-series identity.
    q = r*r
    total = sum(Fraction(n*n)*q**(n-1) for n in range(2,82))
    exact = q*(4-3*q+q*q)/(1-q)**3
    assert total <= exact
    assert (exact-total) < Fraction(1,10**18)

for rational in [Fraction(1,4), Fraction(1,3),Fraction(1,2),Fraction(2,3)]:
    exact_sum(rational)

for M in [1.00001,1.01,1.2,2.,5.,10.,100.]:
    R=root(M)
    c2=M*M-1
    assert isclose(2*c2*S(R),1.,rel_tol=1e-12)
    for t in [.4,.7,.9]:
        assert 2*c2*S(R*t)<1
    weights=[n*(R**(n-1))/(2*S(R)) for n in range(2,1502)]
    energy=2*sum(a*a for a in weights)
    derivative=sum(n*a*(R**(n-1)) for n,a in enumerate(weights,2))
    assert isclose(energy,c2,rel_tol=1e-9,abs_tol=1e-9),(M,energy,c2)
    assert isclose(derivative,.5,rel_tol=1e-10,abs_tol=1e-10)
    print(f'M={M:.5g}: sharp radius={R:.13f}; extremal energy={energy:.12g}; critical derivative={derivative:.12g}')
# Supplementary sharpness checks for the co-Lipschitz profile on smaller disks.
for M in [1.2, 2., 5.]:
    r=.75*root(M)
    c=(M*M-1)**.5
    gamma=[c*n*r**(n-1)/(2*S(r))**.5 for n in range(2,502)]
    norm2=2*sum(t*t for t in gamma)
    vertical=1-2*sum(n*t*r**(n-1) for n,t in enumerate(gamma,2))
    assert isclose(norm2,c*c,rel_tol=1e-10)
    assert isclose(vertical,1-(2*c*c*S(r))**.5,rel_tol=1e-10)
    assert vertical>0
assert S(Fraction(1,5)) == Fraction(1,25)*(4-Fraction(3,25)+Fraction(1,625))/(1-Fraction(1,25))**3
print('PASS: rational series checks, radius brackets and extremal Parseval/derivative identities')
