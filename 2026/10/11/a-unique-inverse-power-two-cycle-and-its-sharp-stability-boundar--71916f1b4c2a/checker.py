"""Finite diagnostics of exact identities for inverse-power maps.

Only tests sampled parameters; continuum statements require the accompanying proof.
Run: python3 checker.py
"""
from fractions import Fraction as F
from math import sqrt, isclose, sinh

cases = 0
ratios = [F(i, j) for i in range(2, 24) for j in range(1, i)]
for p in range(2, 9):
    for r in ratios:
        a = (r**p - r) / (r**(p+1) - 1)
        assert F(0) < a < F(p - 1, p + 1)
        x = F(1)
        y = r
        b = r - a
        f = lambda z: a*z + b / z**p
        assert f(x) == y and f(y) == x
        assert b > 0
        if p == 2:
            assert a * (r*r + r + 1) == r
            multiplier = (a - 2*b/x**3)*(a - 2*b/y**3)
            assert multiplier == 9*a*a + 6*a - 2
        cases += 1

for a in [0.02, 0.07, 0.137, 0.14, 0.2, 0.25, 0.32]:
    for b in [0.01, 0.5, 1.0, 37.0]:
        s = (b*(1+a)/(a*a)) ** (1/3)
        eta = sqrt((1-3*a)/(1+a))
        x = s*(1-eta)/2
        y = s*(1+eta)/2
        f = lambda z: a*z + b/z**2
        assert 0 < x < y
        assert isclose(f(x), y, rel_tol=1e-11, abs_tol=1e-11)
        assert isclose(f(y), x, rel_tol=1e-11, abs_tol=1e-11)
        assert isclose((a - 2*b/x**3)*(a - 2*b/y**3),
                       9*a*a + 6*a - 2, rel_tol=1e-11, abs_tol=1e-11)
        cases += 1

# Diagnostic of the ratio monotonicity used in the general-power proof.
for p in [1.1, 1.5, 2.0, 2.7, 5.0]:
    ts = [j/200 for j in range(1, 161)]
    values = [sinh((p-1)*t)/sinh((p+1)*t) for t in ts]
    assert all(values[j] > values[j+1] for j in range(len(values)-1))
    cases += 1

print('PASS:', cases, 'exact-rational/float finite diagnostics.')
