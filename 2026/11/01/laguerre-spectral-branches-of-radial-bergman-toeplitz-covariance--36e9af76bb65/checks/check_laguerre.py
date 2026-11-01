#!/usr/bin/env python3
"""Finite reproducibility checks for radial Toeplitz covariance spectra.
Uses standard Python and (for high-precision asymptotic checks) mpmath.
Finite checks support but do not prove the infinite-dimensional theorem.
"""
from fractions import Fraction
from math import comb, factorial
from itertools import product
import mpmath as mp

CHECKS = 0

def ok(condition, msg):
    global CHECKS
    assert condition, msg
    CHECKS += 1

def rising(x, k):
    v = 1
    for i in range(k):
        v *= x+i
    return v

def moment(a, b, j):
    return Fraction(rising(b, j), rising(a+b, j))

def det(a):
    if len(a)==1:
        return a[0][0]
    return sum((-1)**j*a[0][j]*det([[a[i][k] for k in range(len(a)) if k!=j] for i in range(1,len(a))]) for j in range(len(a)))

def jacobi_h(a,b,j):
    return Fraction(factorial(j)*rising(a,j)*rising(b,j),rising(a+b,2*j)*rising(a+b+j-1,j))

def gram(a,b,m):
    return [[moment(a,b,i+j)-moment(a,b,i)*moment(a,b,j) for j in range(1,m+1)] for i in range(1,m+1)]

# Every finite principal covariance determinant equals the product of monic
# shifted-Jacobi squared norms; all coefficients are exact rationals.
for a,b,m in product([1,2,3,7,31],[1,2,4],[1,2,3,4]):
    G = gram(a,b,m)
    for k in range(1,m+1):
        expected = Fraction(1)
        for j in range(1,k+1):
            expected *= jacobi_h(a,b,j)
        ok(det([row[:k] for row in G[:k]])==expected, (a,b,m,k))
    ok(all(G[i][i]>0 for i in range(m)), (a,b,m,'variance'))

# Direct Toeplitz action on a homogeneous monomial has beta moment eigenvalue.
for d,alpha,n in product([1,2,3,5], [0,1,3], [0,1,2,9]):
    a=n+d;b=alpha+1
    for k in range(7):
        beta_ratio=Fraction(rising(b,k),rising(a+b,k))
        gamma_ratio=Fraction(factorial(alpha+k)*factorial(a+alpha),factorial(alpha)*factorial(a+alpha+k))
        ok(beta_ratio==gamma_ratio, (d,alpha,n,k))

# Numerical eigen-branch hierarchy, for several nonintegral weights.
mp.mp.dps=75
for d in [1,2,3,5]:
    for b_str in ['0.5','1','1.75','3.5']:
        b=mp.mpf(b_str)
        for n in [40,180,800]:
            a=mp.mpf(n+d)
            m=3
            mus=[mp.rf(b,j)/mp.rf(a+b,j) for j in range(2*m+1)]
            mat=mp.matrix([[mus[i+j]-mus[i]*mus[j] for i in range(1,m+1)] for j in range(1,m+1)])
            eig,_=mp.eigsy(mat)
            vals=list(reversed(list(eig)))
            ok(all(v>0 for v in vals),(d,b_str,n,'positive eigenvalues'))
            for k in range(1,m+1):
                target=mp.factorial(k)*mp.rf(b,k)
                ratio=vals[k-1]*n**(2*k)/target
                ok(0<ratio<mp.mpf('1.1'),(d,b_str,n,k,mp.nstr(ratio,7)))
                if n==800:
                    ok(abs(ratio-1)<mp.mpf('0.101'),(d,b_str,n,k,'terminal',mp.nstr(ratio,7)))
            # Characteristic polynomial invariants are algebraic trace identities.
            ok(abs(sum(vals)-sum(mat[i,i] for i in range(m)))<mp.mpf('1e-55'),(d,b_str,n,'trace'))

# Direct multiplicity sum of homogeneous polynomials.
for d in [1,2,3,4,6]:
    for n in range(0,40):
        ok(sum(comb(q+d-1,d-1) for q in range(n+1))==comb(n+d,d),(d,n))

print('PASS',CHECKS,'finite assertions; no infinite-proof inference')
