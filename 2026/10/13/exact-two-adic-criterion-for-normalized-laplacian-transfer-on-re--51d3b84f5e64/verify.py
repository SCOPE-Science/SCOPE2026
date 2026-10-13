"""Exact rational checks for normalized-Laplacian apex transfer on regular double cones.

Run with Python 3 standard library: python3 verify.py
This verifies reduction formulas and test cases. The all-parameter theorem
is proved analytically, not inferred from these finite checks.
"""
from fractions import Fraction as Q
from math import gcd


def coeffs(m,k,eps):
    assert m>=1 and 0<=k<m and eps in (0,1)
    d=m+eps
    r=k+2
    # Normalized adjacency on the symmetric apex/core block:
    # diagonal values e/d and k/r, off-diagonal square 2m/(dr).
    tr=Q(eps,d)+Q(k,r)
    de=Q(eps*k-2*m,d*r)
    lam=Q(eps,d)-Q(2,r)
    assert tr==1+lam and de==lam
    # Eigenvalues of normalized Laplacian in the apex support:
    antisym=Q(d+eps,d)
    sym=1-lam
    assert sym==Q(m*(k+4)+2*eps,(m+eps)*(k+2))
    assert antisym==Q(m+2*eps,m+eps)
    assert sym/antisym==Q(m*(k+4)+2*eps,(k+2)*(m+2*eps))
    # Stationary eigenprojection from degree-weighted vector:
    w=Q(2*d,2*d+m*r)
    assert 0<w<1
    return antisym, sym, w


def criterion(m,k,eps):
    a=m*(k+4)+2*eps
    b=(k+2)*(m+2*eps)
    g=gcd(a,b)
    p,q=a//g,b//g
    assert gcd(p,q)==1
    yes=(p%2==0 and q%2==1)
    # Divisibility by the next higher power of two is equivalent.
    def nu2(n):
        c=0
        while n%2==0:
            c+=1;n//=2
        return c
    assert yes == (nu2(a)>nu2(b))
    ant,sym,w=coeffs(m,k,eps)
    if yes:
        min_t_over_pi=Q(q,1)/ant
        assert (min_t_over_pi*ant).denominator==1
        assert (min_t_over_pi*ant).numerator%2==1
        assert (min_t_over_pi*sym).denominator==1
        assert (min_t_over_pi*sym).numerator%2==0
    else:
        min_t_over_pi=None
    return yes,min_t_over_pi


n=0
for m in range(1,100):
    for k in range(m):
        if m*k%2: continue
        for eps in (0,1):
            yes,time=criterion(m,k,eps)
            if eps==0:
                assert yes==(k%4==0)
                if yes: assert time==Q(k+2,2)
            if eps==1 and k%4==0: assert not yes
            n+=1
assert criterion(5,4,0)==(True,Q(3))
assert criterion(5,4,1)==(False,None)
assert criterion(5,2,1)==(True,Q(6))
assert criterion(6,1,1)==(True,Q(21,8))
assert criterion(1,0,0)==(True,Q(1))
assert criterion(1,0,1)==(False,None)
print('VERIFY_OK exact_reduced_eigenvalues_and_valuation_tests=%d examples=6'%n)
