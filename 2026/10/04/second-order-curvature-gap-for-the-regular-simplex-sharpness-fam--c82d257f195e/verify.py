#!/usr/bin/env python3
from fractions import Fraction

for n in range(3, 81):
    m = n - 1
    lam = Fraction(m, m + 1)
    full_m2 = Fraction(m*m, m + 2)
    cap_m2 = Fraction(m*m, (m+1)*(m+1)) + lam*lam*full_m2
    diff = cap_m2 - full_m2
    expected_diff = -Fraction(m*m*(m-1), (m+1)*(m+1)*(m+2))
    assert diff == expected_diff
    eps_coeff = Fraction(n, 2) * (-diff)
    expected_eps = Fraction(m*m*(m-1), 2*(m+1)*(m+2))
    assert eps_coeff == expected_eps
    tan_coeff = eps_coeff / (m*m)
    expected_tan = Fraction(n-2, 2*n*(n+1))
    assert tan_coeff == expected_tan
    cap_fraction = lam ** m
    sharp_constant = Fraction(n-1, n) ** (n-1)
    assert cap_fraction == sharp_constant

print('VERIFY_OK')
