#!/usr/bin/env python3
"""Independent exact cyclotomic check of two-digit Cantor Fourier zeros.
Requires sympy; the companion checker uses only Python's standard library.
"""
from sympy import Poly, symbols, cyclotomic_poly

z = symbols('z')
cases = ((2,2),(4,2),(4,3),(6,2),(8,2),(10,1))
count = 0
for b,n in cases:
    modulus=b**n
    phi=Poly(cyclotomic_poly(modulus,z),z,domain='ZZ')
    E=[sum((b//2)*((mask>>j)&1)*(b**j) for j in range(n)) for mask in range(2**n)]
    for k in range(modulus):
        polynomial=Poly(sum(z**((k*x)%modulus) for x in E),z,domain='ZZ')
        exact_zero=polynomial.rem(phi).is_zero
        digit_zero=any(k%(b**j)==0 and (k//(b**j))%2==1 for j in range(n))
        assert exact_zero==digit_zero,(b,n,k,exact_zero,digit_zero)
        count+=1
print(f'EXACT_CYCLOTOMIC_OK comparisons={count} fields={len(cases)}')
