"""Exact-rational algebra checks for the radial clock of a polynomial-tail diffusion.

The mathematical proof is in RESULT.md; finite arithmetic does not verify
probabilistic limits or establish historical novelty.
"""
from fractions import Fraction as F

checks = 0
for d in (1, 2, 3, 5, 8):
    for r in (F(1, 3), F(1, 1), F(3, 2), F(5, 1)):
        q = F(d) + r
        for u in (F(0), F(1, 10), F(1, 3), F(2, 3), F(9, 10)):
            ell = u / q
            a = 1 - ell * q
            assert a > 0
            # The exact power of radius in quadratic variation is zero.
            assert 2 * ell * q + 2 * (a - 1) == 0
            checks += 1
            # The exact power of radius in the transformed generator is -a.
            assert 2 * ell * q + a - 2 == -a
            checks += 1
            # This is the radial bracket after inserting the power-law gradient.
            assert (d + a - 2) - (1 - 2 * ell) * q == -(r + a)
            checks += 1
            # Unit normalization c_pi=1: radial-clock variance = 1 and
            # the exponent in P(|X_t|>R) is 1/(4*a*a*t).
            for t in (F(1, 4), F(1), F(7, 3)):
                kappa = 1 / (4 * a * a * t)
                assert 2 * t * (2 * a * a * kappa) == 1
                checks += 1
# Brownian normalization at ell=0: dX=sqrt(2)dB gives exp(-R^2/(4t)).
for t in (F(1, 3), F(1), F(5, 2)):
    assert 1 / (4 * t) == F(1, 2) / (2 * t)
    checks += 1
print(f"radial_clock_algebra: {checks} exact rational assertions passed")
