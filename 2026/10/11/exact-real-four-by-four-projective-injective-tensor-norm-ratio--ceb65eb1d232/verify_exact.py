#!/usr/bin/env python3
"""Exact rational verification for a sharp real 4-by-4 tensor-norm ratio.

Only standard-library integer and rational arithmetic is used. The attached
certificate consists of 512 explicit, nonnegative rational convex-gauge
representations. No optimization package is needed to verify the theorem.
"""
import itertools
import json
from fractions import Fraction
from pathlib import Path

N = 4
ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / 'endpoint_certificates.json').read_text(encoding='utf-8'))
assert DATA['side'] == N
assert DATA['sign_patterns'] == 512
assert DATA['sign_vertex_encoding'] == 'row0=+1, all 16 col ±1'
certificates = DATA['lambda_coefficients']
assert len(certificates) == 512

signs = (-1, 1)
vertices = []
for e in itertools.product(signs, repeat=N):
    if e[0] != 1:
        continue
    for f in itertools.product(signs, repeat=N):
        vertices.append(tuple(e[i] * f[j] for i in range(N) for j in range(N)))
assert len(vertices) == 128

max_mass = Fraction(0)
masses = set()
for index, tail in enumerate(itertools.product(signs, repeat=9)):
    target = [1] * (N * N)
    for k, s in enumerate(tail):
        row = 1 + k // 3
        col = 1 + k % 3
        target[row * N + col] = s
    coeffs = certificates[index]
    assert len(coeffs) <= 128 and len(coeffs) > 0
    indices = [int(j) for j, _ in coeffs]
    assert len(indices) == len(set(indices))
    assert all(0 <= j < 128 for j in indices)
    weights = [(j, Fraction(value)) for j, value in coeffs]
    assert all(value > 0 for _, value in weights)
    assert all(sum(value * vertices[j][k] for j, value in weights) == target[k]
               for k in range(16)), 'failed signed-vertex decomposition'
    mass = sum((v for _, v in weights), Fraction(0))
    assert mass <= Fraction(12, 5), 'upper bound failed'
    max_mass = max(max_mass, mass)
    masses.add(mass)
assert index == 511 and max_mass == Fraction(12, 5)

witness = ((2, 2, 1, 1), (2, -1, -1, -2),
           (1, -1, -2, 2), (1, -2, 2, 1))
entry_mass = sum(abs(witness[i][j]) for i in range(N) for j in range(N))
bilinear_norm = max(abs(sum(witness[i][j] * e[i] * f[j]
                            for i in range(N) for j in range(N)))
                    for e in itertools.product(signs, repeat=N)
                    for f in itertools.product(signs, repeat=N))
assert (entry_mass, bilinear_norm) == (24, 10)
assert Fraction(entry_mass, bilinear_norm) == Fraction(12, 5)
print('REAL_4x4_PROJECTIVE_INJECTIVE_EXACT_CERTIFICATE_OK')
print('Verified sign-orbit representatives:', len(certificates))
print('Verified rank-one sign vertices:', len(vertices))
print('Maximum exact certificate mass:', max_mass)
print('Witness entrywise sum and infinity-to-one norm:', entry_mass, bilinear_norm)
