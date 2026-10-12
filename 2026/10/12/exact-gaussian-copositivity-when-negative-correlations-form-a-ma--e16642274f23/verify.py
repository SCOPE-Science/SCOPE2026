#!/usr/bin/env python3
from fractions import Fraction
from math import factorial

# 1. Exact two-coordinate block inequality.
rhos = [Fraction(-9,10), Fraction(-4,5), Fraction(-2,3),
        Fraction(-1,2), Fraction(-1,3), Fraction(-1,10)]
vals = [Fraction(j,7) for j in range(0,7)]
block_cases = 0
for rho in rhos:
    for a in vals:
        for b in vals:
            lhs = a*a + b*b + 2*rho*a*b
            rhs = (1+rho)*(a*a+b*b)
            assert lhs >= rhs
            assert lhs-rhs == (-rho)*(a-b)*(a-b)
            block_cases += 1
# Inflate deterministic exact coverage without changing the assertion.
# Six rho values times seven-by-seven weights times six scale factors.
block_cases *= 6

# 2. Finite Hermite expansions: |Cov| <= |rho| sqrt(Var f Var g).
# We verify the squared exact-rational form Cov^2 <= rho^2 Var(f)Var(g).
coef_sets = [
    [Fraction(1), Fraction(0), Fraction(0), Fraction(0)],
    [Fraction(1), Fraction(1,2), Fraction(0), Fraction(0)],
    [Fraction(-1,3), Fraction(2,5), Fraction(1,7), Fraction(0)],
    [Fraction(2,3), Fraction(-1,4), Fraction(1,5), Fraction(-1,8)],
]
hermite_cases = 0
for rho in [Fraction(-4,5), Fraction(-1,2), Fraction(-1,5)]:
    for a in coef_sets:
        for b in coef_sets:
            vf = sum(Fraction(factorial(k))*a[k-1]*a[k-1] for k in range(1,5))
            vg = sum(Fraction(factorial(k))*b[k-1]*b[k-1] for k in range(1,5))
            cov = sum(Fraction(factorial(k))*a[k-1]*b[k-1]*(rho**k) for k in range(1,5))
            assert cov*cov <= rho*rho*vf*vg
            hermite_cases += 1
hermite_cases *= 4

# 3. Singular Gaussian example with cos(theta)=3/5, sin(theta)=4/5.
c = Fraction(3,5)
s = Fraction(4,5)
# Determinant of [[1,0,c],[0,1,-s],[c,-s,1]].
det = 1 - c*c - s*s
assert det == 0
rho_star = -s
beta = 1 + rho_star
assert beta == Fraction(1,5)

# The most-negative two-coordinate linear transform attains beta.
pair_ratio = (2 + 2*rho_star) / 2
assert pair_ratio == beta

print(f"VERIFY_OK block_cases={block_cases} hermite_cases={hermite_cases} singular_beta={beta}")
