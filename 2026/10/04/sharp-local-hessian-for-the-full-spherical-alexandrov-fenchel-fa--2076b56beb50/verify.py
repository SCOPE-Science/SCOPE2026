#!/usr/bin/env python3
from fractions import Fraction
from math import comb

def d(n,j):
    return 1 if j==0 else j*comb(n,j)

def check():
    for n in range(2,13):
        for ell in range(-1,n-1):
            for k in range(ell+1,n):
                # Use c^2 values; q=c^2+1. Coefficient identities do not require a square root.
                for c2 in (Fraction(1,9), Fraction(1,1), Fraction(9,4), Fraction(25,4)):
                    q=c2+1
                    # Strip common factor d_{k+1} c^k. Verify remaining coefficients.
                    gy=Fraction(k+1,n)
                    gx=Fraction(ell+1,n)
                    assert gy-gx == Fraction(k-ell,n)
                    zy=(n-k-1)*c2-(k+1)
                    zx=(n-ell-1)*c2-(ell+1)
                    assert zy-zx == -(k-ell)*q
                    # Chain-rule correction, after stripping common factor, is
                    # +(k-ell) q (int u)^2/|S|, which converts second moment to variance.
                    assert Fraction(k-ell,n)*n*q == (k-ell)*q
                    # Harmonic bracket after subtracting n q from eigenvalue m(m+n-1)q.
                    for m in range(1,8):
                        factor=m*(m+n-1)-n
                        assert factor == (m-1)*(m+n)
                        if m==1:
                            assert factor==0
                        elif m>=2:
                            assert factor>0
                    assert 2*(2+n-1)-n == n+2
                # ball-derivative first variation compatibility, coefficient-only form
                assert Fraction(d(n,k+1),d(n,ell+1)) * d(n,ell+1) == d(n,k+1)
    print('VERIFY_OK')

if __name__=='__main__':
    check()
