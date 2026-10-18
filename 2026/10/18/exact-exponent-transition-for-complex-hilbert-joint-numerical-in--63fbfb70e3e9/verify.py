#!/usr/bin/env python3
"""Finite exact and numerical consistency checks for Hilbert joint numerical indices.

The universal assertion is proved analytically in RESULT.md; these checks do not
certify infinitely many dimensions, tuple lengths or real exponents.
"""
from fractions import Fraction as F
from itertools import product
import cmath
import math
import random

checks = 0

def check(ok, detail=""):
    global checks
    if not ok:
        raise AssertionError(detail)
    checks += 1

# Exact Gaussian-integer sign second moments, the key nonstandard step.
rng = random.Random(27182818)
for k in range(1, 7):
    for dimension in range(1, 5):
        for trial in range(30):
            vectors = [tuple(complex(rng.randrange(-4, 5), rng.randrange(-4, 5))
                             for _ in range(dimension)) for _ in range(k)]
            target = sum(sum(int(z.real*z.real + z.imag*z.imag) for z in v) for v in vectors)
            signed = 0
            maximum = 0
            for signs in product((-1, 1), repeat=k):
                value = sum(int(z.real*z.real + z.imag*z.imag)
                            for t in range(dimension)
                            for z in [sum(signs[j] * vectors[j][t] for j in range(k))])
                signed += value
                maximum = max(maximum, value)
            check(signed == (2**k) * target, 'sign orthogonality')
            check(maximum >= target, 'signed norm domination')

# Polarization of non-Hermitian complex bilinear forms; all data integral.
for dimension in range(2, 7):
    for trial in range(80):
        mat = [[complex(rng.randrange(-3,4),rng.randrange(-3,4)) for _ in range(dimension)]
               for _ in range(dimension)]
        x = [complex(rng.randrange(-2,3),rng.randrange(-2,3)) for _ in range(dimension)]
        y = [complex(rng.randrange(-2,3),rng.randrange(-2,3)) for _ in range(dimension)]
        def form(u,v):
            return sum(sum(mat[a][b] * u[b] for b in range(dimension)) * v[a].conjugate()
                       for a in range(dimension))
        lhs = sum((1j**r) * form([x[t] + (1j**r)*y[t] for t in range(dimension)],
                                  [x[t] + (1j**r)*y[t] for t in range(dimension)])
                  for r in range(4))
        check(abs(lhs - 4*form(x,y)) < 1e-8, 'polarization')

# Every finite trial checks the explicit witness at random unit vectors as well
# as the exact extremizer; tests include exponent 1 and both sides of 2.
for k in range(1, 19):
    for p in (1.0, 1.2, 1.5, 1.999, 2.0, 2.001, 2.5, 4.0, 9.0, 100.0):
        norm_p = k**(1/p)
        max_radius = 0.5*k**max(1/p-0.5, 0)
        exact_ratio = max_radius/norm_p
        promised = 0.5*k**(-1/max(p, 2.0))
        check(math.isclose(exact_ratio, promised, rel_tol=1e-12), 'phase identity')
        if p < 2:
            b = [1/math.sqrt(2*k)] * k
        else:
            b = [1/math.sqrt(2)] + [0]*(k-1)
        value = 2**-0.5 * sum(abs(t)**p for t in b)**(1/p)
        check(math.isclose(value, max_radius, rel_tol=1e-12), 'sharp witness')
        for trial in range(6):
            a = complex(rng.gauss(0,1), rng.gauss(0,1))
            vec = [complex(rng.gauss(0,1), rng.gauss(0,1)) for _ in range(k)]
            scale = (abs(a)**2 + sum(abs(z)**2 for z in vec))**-0.5
            actual = abs(a)*scale*(sum((abs(z)*scale)**p for z in vec))**(1/p)
            check(actual <= max_radius*(1+1e-12), 'witness upper bound')

# Algebraic exponent cancellation as rational identities.
for p in (F(1), F(3,2), F(2)):
    reciprocal_p = F(1)/p
    reciprocal_q = F(1)-reciprocal_p
    check(-reciprocal_q - (reciprocal_p-F(1,2)) == -F(1,2), 'low-p exponent')

print(f'VERIFY_OK assertions={checks} exact_sign_and_polarization=True universal_proof_in_RESULT_required=True')
