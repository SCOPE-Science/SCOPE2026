#!/usr/bin/env python3
"""Exact finite tests for a two-initial-weight Bergman-shift moment theorem.

Requires Python and sympy. The script checks algebraic certificates and examples;
the universal operator statements are proved analytically in RESULT.md.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, sqrt
import sympy as sp

checks=0

def verify(assertion, context=""):
    global checks
    checks+=1
    if not bool(assertion):
        raise AssertionError(context or f"assertion {checks}")

def gamma(m,c,d):
    if m==0: return sp.Integer(1)
    if m==1: return c/sp.Integer(2)+d
    return c/sp.Integer(m+1)

def moment_matrix(m,k,c,d):
    return sp.Matrix([[gamma(m+i+j,c,d) for j in range(k+1)] for i in range(k+1)])

def positive_semidefinite(M):
    n=M.rows
    for z in range(1,n+1):
        for indices in combinations(range(n),z):
            if M.extract(indices,indices).det()<0:
                return False
    return True

def k_criterion(k,c,d):
    N=sp.Integer(k+1)
    low=d+2*c/(N**2*(N+1)**2)
    det=(1-c+4*c/N**2)*12*c/(N**2*(N**2-1)**2) - (d+6*c/(N**2*(N**2-1)))**2
    return low>=0 and det>=0

def n_criterion(n,c,d):
    n=sp.Integer(n)
    return d+c/((n+1)*(n+2))>=0 and 1-n*d-n*c/(n+1)>=0

# Independent orthogonal-polynomial inverse-Gram certificates.
for N in range(2,9):
    N0=sp.Integer(N)
    H=sp.Matrix([[sp.Rational(1,i+j+1) for j in range(N)] for i in range(N)])
    top=H.inv()[:2,:2]
    expected=sp.Matrix([[N0**2,-N0**2*(N0**2-1)/2],
                        [-N0**2*(N0**2-1)/2,N0**2*(N0**2-1)**2/3]])
    verify(top==expected, f"Hilbert inverse N={N}")
    S=expected.inv()
    verify(S==sp.Matrix([[4/N0**2,6/(N0**2*(N0**2-1))],
                         [6/(N0**2*(N0**2-1)),12/(N0**2*(N0**2-1)**2)]]))
    Hp=sp.Matrix([[sp.Rational(1,i+j+2) for j in range(N)] for i in range(N)])
    verify(Hp.inv()[0,0]==N0**2*(N0+1)**2/2)
    # endpoint Legendre and Jacobi polynomial sums
    verify(sum((2*j+1) for j in range(N))==N0**2)
    verify(sum((2*j+1)*j*(j+1) for j in range(N))==N0**2*(N0**2-1)/2)
    verify(sum((2*j+1)*j*j*(j+1)*(j+1) for j in range(N))==N0**2*(N0**2-1)**2/3)
    verify(sum(2*j**3 for j in range(1,N+1))==N0**2*(N0+1)**2/2)

# Independent principal-minor tests of the two Hankel conditions.
for c in (sp.Rational(1,4),sp.Rational(1,2),sp.Integer(1),sp.Rational(6,5)):
    for d in (sp.Rational(-1,20),sp.Rational(-1,100),sp.Integer(0),sp.Rational(1,100),sp.Rational(1,10)):
        if c/2+d<=0: continue
        for k in range(1,4):
            direct=positive_semidefinite(moment_matrix(0,k,c,d)) and positive_semidefinite(moment_matrix(1,k,c,d))
            verify(direct==k_criterion(k,c,d),f"k criterion c={c},d={d},k={k}")
        for n in range(1,10):
            direct=all(sum((-1)**j*comb(n,j)*gamma(m+j,c,d) for j in range(n+1))>=0 for m in range(5))
            verify(direct==n_criterion(n,c,d),f"n criterion c={c},d={d},n={n}")

# Exact match of the published fixed-first-weight, second-order slice.
x=sp.symbols('x',real=True)
c=sp.Rational(3,2)*x
d=sp.Rational(1,2)-sp.Rational(3,4)*x
N=sp.Integer(3)
det=sp.factor((1-c+4*c/N**2)*12*c/(N**2*(N**2-1)**2)
             -(d+6*c/(N**2*(N**2-1)))**2)
verify(sp.simplify(det+(40*x**2-63*x+24)/96)==0)
verify(sp.simplify(d+2*c/(N**2*(N+1)**2)+(35*x-24)/48)==0)

# Independent large-order scale diagnostics (not substitutes for the proof).
for cval in (sp.Rational(1,5),sp.Rational(1,2),sp.Rational(4,5)):
    cv=float(cval)
    for N in (100,1000,10000):
        dlo=-2*cv/(N**2*(N+1)**2)
        dhi=sqrt(12*cv*(1-cv+4*cv/N**2))/(N*(N**2-1))-6*cv/(N**2*(N**2-1))
        verify(abs((-dlo)*N**4-2*cv)<10/N)
        verify(abs(dhi*N**3-sqrt(12*cv*(1-cv)))<50/N)
for N in (100,1000,10000):
    dlo=-2/(N**2*(N+1)**2)
    dhi=(4*sqrt(3)-6)/(N**2*(N**2-1))
    verify(abs((-dlo)*N**4-2)<15/N)
    verify(abs(dhi*N**4-(4*sqrt(3)-6))<15/N)

print(f"PASS: {checks} exact or finite consistency assertions")
