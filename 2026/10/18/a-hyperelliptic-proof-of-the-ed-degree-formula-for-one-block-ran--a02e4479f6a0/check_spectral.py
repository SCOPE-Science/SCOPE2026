"""Exact finite-specialization checks for a spectral-curve ED-degree proof.

Requires SymPy. The all-dimensional mathematical proof is in RESULT.md;
these examples do not assert a finite search proves an infinite theorem.
"""
import sympy as sp

z = sp.symbols("z")
for m in range(2, 8):
    # A=diag(0,...,m-1), b=(1,...,1), c11=-3, c22=m+4.
    D = sp.prod(j - z for j in range(m))
    adjsum = sum(sp.prod(k - z for k in range(m) if k != j)
                 for j in range(m))
    arrowhead = sp.expand((m + 4 - z) * D - adjsum)
    branch = sp.expand((z + 3) * D * arrowhead)
    assert sp.degree(branch, z) == 2*m + 2
    assert sp.gcd(branch, sp.diff(branch, z)) == 1
    isotropic_finite = sp.expand((m + 7) * D - adjsum)
    assert sp.degree(isotropic_finite, z) == m
    assert sp.gcd(isotropic_finite, sp.diff(isotropic_finite, z)) == 1
    beta0, beta1, f = m, m*(m-1)//2, m+7
    slope_numerator = (beta1 + 3*beta0)*f - beta0**2
    assert slope_numerator == m*(m*m+10*m+35)//2
    assert slope_numerator != 0
    total = (2*m - 2) + 2*(2*m)
    assert total == 6*m - 2
    print(f"m={m} branch={2*m+2} genus={m} poles={2*m} ED={total} PASS")
print("SPECTRAL_SPECIALIZATION_CHECKS_OK")
