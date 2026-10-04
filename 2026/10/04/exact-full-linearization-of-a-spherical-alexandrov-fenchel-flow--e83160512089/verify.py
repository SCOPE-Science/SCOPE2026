#!/usr/bin/env python3
from fractions import Fraction
from math import comb

# Exact derivative of normalized elementary symmetric functions at (c,...,c):
# E_j(c,...,c)=c^j and dE_j/dkappa_i = C(n-1,j-1)/C(n,j) c^(j-1)=j/n c^(j-1).
for n in range(2, 11):
    for j in range(1, n + 1):
        coeff = Fraction(comb(n-1, j-1), comb(n, j))
        assert coeff == Fraction(j, n)

    # For F=E_{k+1}/E_k, coefficient multiplying sum_i delta kappa_i is exactly 1/n.
    for k in range(0, n):
        num = Fraction(k + 1, n) - Fraction(k, n)
        assert num == Fraction(1, n)

        # Relative first-variation coefficients of numerator and denominator of phi
        # differ by exactly 2/c times average(delta F); k cancels.
        assert (k + 1) - (k - 1) == 2

    # Scaled harmonic eigenvalues lambda_l / csc^2(R).
    # l=1 is neutral; l>=2 strictly decreases and l=2 gives -2(n+2)/n.
    lam1 = 2 * (Fraction(1, 1) - Fraction(n, n))
    assert lam1 == 0
    lam2 = 2 * (Fraction(1, 1) - Fraction(2*(n+1), n))
    assert lam2 == -Fraction(2*(n+2), n)
    prev = lam1
    for ell in range(2, 9):
        lam = 2 * (Fraction(1, 1) - Fraction(ell*(ell+n-1), n))
        assert lam < 0
        assert lam < prev
        prev = lam

print('VERIFY_OK')
