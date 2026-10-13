"""Exact arithmetic checks for a heterogeneous SIS extinction construction.

This program checks the algebraic inequalities; the infinite-dimensional
Rayleigh estimate and parabolic comparison are proven in RESULT.md.
Run: python verify_cosine_sis.py
"""
from fractions import Fraction as Q


def prod(a, b):
    z = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            z[i + j] += x * y
    return z


def cosmean(p):
    # Only degrees <= 3 occur; E cos(pi x)=E cos(pi x)^3=0,
    # E cos(pi x)^2=1/2 on x in (0,1).
    assert len(p) <= 4
    return sum(v * ([Q(1), Q(0), Q(1, 2), Q(0)][i])
               for i, v in enumerate(p))

beta = [Q(1), -Q(3, 4)]
f = [Q(1, 4), Q(1)]
V = prod(beta, f)
assert V == [Q(1, 4), Q(13, 16), -Q(3, 4)], V
assert cosmean(V) == -Q(1, 8)
assert cosmean(f) == Q(1, 4)
assert beta[0] - abs(beta[1]) == Q(1, 4)
assert beta[0] + abs(beta[1]) == Q(7, 4)
assert sum(map(abs, V)) <= Q(2)  # Uniform |V| <= 2.

# Neumann Poincare: pi^2>9. For u=m+v, mean(v)=0,
# Rayleigh numerator <= -m^2/8 + 4|m|w - 88 w^2,
# Young 4|m|w<=m^2/16+64w^2, giving <= -||u||^2/16.
initial_eigen_bound = -Q(1, 16)
perturbation = Q(7, 4) * Q(1, 100)
comparison_eigen_bound = initial_eigen_bound + perturbation
assert comparison_eigen_bound == -Q(9, 200)
assert comparison_eigen_bound < -Q(1, 25)

ell = [Q(199, 200), Q(1, 200)]  # ell(x)=1-(1-cos(pi*x))/200
assert ell[0] - ell[1] == Q(99, 100)
assert ell[0] + ell[1] == Q(1)
Nstar_trial = Q(2) + cosmean(prod(ell, f))
assert Nstar_trial == Q(9, 4) + Q(1, 800)
assert initial_eigen_bound + Q(1, 50) == -Q(17, 400) < 0

seed = Q(1, 10000)
bootstrap_width = Q(1, 100)
bootstrap_error = Q(5, 4) * Q(7, 4) * Q(25) * seed
assert bootstrap_error == Q(7, 1280)
assert bootstrap_error < bootstrap_width
assert Q(2) < Q(9, 4) < Q(9, 4) + seed < Nstar_trial

# The existence, positivity and normalization of the Neumann principal
# eigenfunction follow from Sturm-Liouville/Rayleigh theory, not numerics.
print('VERIFY_OK: V coefficients, cosine moments, spectral bounds,')
print('           positive admissible witness, bootstrap, and population window')
