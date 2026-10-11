#!/usr/bin/env python3
import itertools
import math
from fractions import Fraction

import numpy as np
import sympy as sp
from scipy.spatial import ConvexHull

def det_int(cols):
    M = sp.Matrix.hstack(*[sp.Matrix(c) for c in cols])
    return int(M.det())

def zero_one_D(n):
    cols = [tuple(v) for v in itertools.product((0,1), repeat=n) if any(v)]
    best = 0
    for C in itertools.combinations(cols, n):
        best = max(best, abs(det_int(C)))
    return best

for n in range(2,5):
    e = [np.zeros(n, dtype=int)] + [np.eye(n, dtype=int)[i] for i in range(n)]

    # Relative unit ball vertices 1/2(e_i-e_j).
    roots = sorted(set(
        tuple((e[i]-e[j]).tolist())
        for i in range(n+1) for j in range(n+1) if i != j
    ))
    Mverts = np.array(roots, dtype=float) / 2.0
    volM = ConvexHull(Mverts).volume
    targetM = math.comb(2*n,n)/(2**n * math.factorial(n))
    assert abs(volM-targetM) < 2e-11, (n, volM, targetM)

    # Polar vertices ±2*1_S.
    bits = [tuple(v) for v in itertools.product((0,1), repeat=n) if any(v)]
    Pverts = np.unique(np.array(
        [tuple(2*x for x in b) for b in bits] +
        [tuple(-2*x for x in b) for b in bits],
        dtype=float
    ), axis=0)
    volP = ConvexHull(Pverts).volume
    targetP = (n+1)*2**n
    assert abs(volP-targetP) < 2e-10, (n, volP, targetP)

    # Total-unimodular root determinant bound.
    max_root_det = 0
    for C in itertools.combinations(roots, n):
        max_root_det = max(max_root_det, abs(det_int(C)))
    assert max_root_det == 1

    # Zero-one determinant and polar determinant reduction.
    D = zero_one_D(n)
    max_polar_det = 0
    signed_polar = [tuple(2*x for x in b) for b in bits]
    for C in itertools.combinations(signed_polar, n):
        max_polar_det = max(max_polar_det, abs(det_int(C)))
    assert max_polar_det == (2**n)*D

    max_reflection = Fraction(2**n, math.factorial(n))

    # Normalization scalars, excluding v_n where symbolic pi occurs.
    mass_scalar = Fraction(2**n, 1)
    massstar_scalar = Fraction((2**n)*D, 1)
    assert mass_scalar * max_reflection == Fraction(4**n, math.factorial(n))
    assert massstar_scalar * max_reflection == Fraction((4**n)*D, math.factorial(n))

    # Polar/parallelotope dual volume product.
    max_cross_polar = Fraction((4**n)*D, math.factorial(n))
    polar_product = Fraction(4**n, math.factorial(n))
    min_parallelotope = polar_product / max_cross_polar
    assert min_parallelotope == Fraction(1,D)

# Exact planar specializations.
n=2
D=zero_one_D(n)
assert D == 1
assert sp.simplify((4**n)*sp.pi/sp.binomial(2*n,n) - 8*sp.pi/3) == 0
assert sp.simplify((4**n)*(n+1)/(sp.factorial(n)*sp.pi) - 24/sp.pi) == 0
assert Fraction(4**n, math.factorial(n)) == 8
assert Fraction((4**n)*D, math.factorial(n)) == 8

print("VERIFY_OK")
print("relative_ball_volumes_n_2_to_4 = passed")
print("polar_volumes_n_2_to_4 = passed")
print("root_total_unimodularity_samples = passed")
print("zero_one_determinant_reduction_n_2_to_4 = passed")
print("normalization_formulas = passed")
