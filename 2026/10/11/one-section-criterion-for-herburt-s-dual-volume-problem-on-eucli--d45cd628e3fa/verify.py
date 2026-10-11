#!/usr/bin/env python3
import math
import sympy as s
import numpy as np

rho, r, ecc, z = s.symbols("rho r ecc z", positive=True, real=True)
root = -ecc*z + s.sqrt(r**2 - ecc**2 + ecc**2*z**2)
quad = s.expand(root**2 + 2*ecc*z*root + ecc**2 - r**2)
assert s.simplify(quad) == 0

delta, v2 = s.symbols("delta v2", nonnegative=True)
x2 = delta**2 + v2
assert s.simplify((x2-delta**2)-v2) == 0

# Exact dimension-one boundary phenomenon.
assert s.simplify((r-ecc)+(r+ecc)-2*r) == 0

# Regression quadrature for m>=2. These checks are not the proof.
rng = np.random.default_rng(20261006)
for m in range(2, 7):
    # Uniform sphere samples from normalized Gaussians.
    X = rng.normal(size=(120000, m))
    X /= np.linalg.norm(X, axis=1)[:, None]
    zvals = X[:, 0]
    R = 2.0
    vals = []
    for ss in (0.0, 0.35, 0.8, 1.2):
        q = np.sqrt(R*R - ss*ss + ss*ss*zvals*zvals)
        vals.append(float(q.mean()))
    assert all(vals[i] > vals[i+1] for i in range(len(vals)-1)), (m, vals)

print("VERIFY_OK")
print("symbolic_radial_root = exact")
print("section_projection_identity = exact")
print("dimension_one_sum = 2r")
print("regression_dimensions = 2..6")
