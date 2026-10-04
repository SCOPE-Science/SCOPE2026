#!/usr/bin/env python3
import sympy as sp

X = sp.symbols("X0:5")
M = sp.Matrix([
    [0, -(X[2] + X[4]), X[1], -X[4], X[1] + X[3]],
    [X[2] + X[4], 0, -(X[0] + X[3]), X[2], -X[0]],
    [-X[1], X[0] + X[3], 0, -(X[1] + X[4]), X[3]],
    [X[4], -X[2], X[1] + X[4], 0, -(X[0] + X[2])],
    [-(X[1] + X[3]), X[0], -X[3], X[0] + X[2], 0],
])
S = sum(X)
assert M + M.T == sp.zeros(5)
assert sp.expand(M.det()) == 0
for r in range(5):
    for c in range(5):
        lhs = sp.expand(M.minor_submatrix(r, c).det())
        rhs = sp.expand(((-1) ** (r + c)) * X[r] * X[c] * S**2)
        assert sp.expand(lhs - rhs) == 0, (r, c)
print("VERIFY_OK: alternating; det=0; all 25 cofactors match (-1)^(r+c) X_r X_c S^2")
