#!/usr/bin/env python3
"""Standalone exact arithmetic checks of finite-difference witnesses.

The checks cover finite parameter ranges only; the attached proof handles all
integer orders and all real exponents in its stated domain.
"""
from math import comb
import sympy as sp

z, w, Z, W = sp.symbols('z w Z W')

def binomial_weights(k):
    return [(-1)**i * comb(2*k, i) for i in range(2*k+1)]

for k in range(1, 7):
    weights = binomial_weights(k)
    assert sum(weights) == 0
    for j in range(1,k+1):
        expr = sum(weights[i] * (z+i*w)**(j-1) * (Z+i*W)**j
                   for i in range(2*k+1))
        assert sp.expand(expr) == 0, (k,j)
    for j in range(k+1,k+4):
        witness = sum(weights[i] * (i+1)**(2*j-1)
                      for i in range(2*k+1))
        assert witness > 0, (k,j,witness)

# One sample of the genuinely non-polynomial obstruction: for k=2,
# exponent p=3, and z=1,w=i, the real/imaginary weighted sum is nonzero.
for k in range(1,5):
    x = [1+1j*i for i in range(2*k+1)]
    for p in (1.5, 3.0, 5.0, 7.0):
        val = sum(binomial_weights(k)[i] * abs(t)**(p-2) * t.conjugate()
                  for i,t in enumerate(x))
        # Some accidental zeros may occur for special sample points,
        # so this is only a finite numerical diagnostic, not a proof.
        if abs(val) < 1e-8:
            x = [1.17+(.31+.71j)*i for i in range(2*k+1)]
            val = sum(binomial_weights(k)[i] * abs(t)**(p-2) * t.conjugate()
                      for i,t in enumerate(x))
        assert abs(val) > 1e-9, (k,p,val)

print('FINITE_DIFFERENCE_RELATION_EXACT_TESTS_OK')
