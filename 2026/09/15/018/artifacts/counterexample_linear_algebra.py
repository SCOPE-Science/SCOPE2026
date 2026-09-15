"""Verify linear-algebra core of the counterexample:
Q = (-E8) (+) H, b+ = 1, sigma = -8, and -id on the H summand acts as -1 on H+.
Self-contained reproducibility check for the disproof.
"""
import numpy as np

# Cartan matrix of E8 (positive definite); our block is -E8
E8 = np.array([
    [2,-1,0,0,0,0,0,0],
    [-1,2,-1,0,0,0,0,0],
    [0,-1,2,-1,0,0,0,0],
    [0,0,-1,2,-1,0,0,0],
    [0,0,0,-1,2,-1,0,-1],
    [0,0,0,0,-1,2,-1,0],
    [0,0,0,0,0,-1,2,0],
    [0,0,0,0,-1,0,0,2],
], dtype=float)
negE8 = -E8
H = np.array([[0.,1.],[1.,0.]])
Q = np.zeros((10,10))
Q[:8,:8] = negE8
Q[8:,8:] = H

eig = np.linalg.eigvalsh(Q)
b_plus = int((eig > 1e-9).sum())
b_minus = int((eig < -1e-9).sum())
sigma = b_plus - b_minus
print("eigenvalues:", np.round(eig,3))
print("b+ =", b_plus, "b- =", b_minus, "sigma =", sigma)
assert b_plus == 1 and sigma == -8, "form check failed"

# H+ line of H block spanned by (1,1); -id acts as -1
v = np.array([1.,1.])
assert np.allclose(-v, -1*v)
# positivity: v^T H v = 2 > 0
assert v @ H @ v > 0
# -E8 block negative definite: all eigenvalues negative
assert (np.linalg.eigvalsh(negE8) < 0).all()
print("H+-reversal check passed: -id on H summand negates the positive line.")
print("OK")
