"""Exact input checks for a family of monomial automorphisms.

The theorem about arbitrary projective models is established by the written
mathematical argument, not by this finite computation.
"""
from itertools import permutations

A = ((0, -1, 1), (1, 0, 0), (0, 1, 0))

def sign_perm(p):
    return -1 if sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p))) % 2 else 1

def det_poly(M):
    """Determinant of a 3x3 matrix of integer-coefficient polynomials."""
    total = [0, 0, 0, 0]
    for perm in permutations(range(3)):
        p = [1]
        for i, j in enumerate(perm):
            q = M[i][j]
            z = [0] * (len(p) + len(q) - 1)
            for a, x in enumerate(p):
                for b, y in enumerate(q):
                    z[a + b] += x * y
            p = z
        for i, v in enumerate(p):
            total[i] += sign_perm(perm) * v
    return total

assert det_poly([[[A[i][j]] for j in range(3)] for i in range(3)]) == [1, 0, 0, 0]
char = det_poly([[[(-A[i][j]), 1] if i == j else [-A[i][j]]
                  for j in range(3)] for i in range(3)])
assert char == [-1, 1, 0, 1], char  # t^3 + t - 1
# Cubic discriminant of t^3 + p*t + q is -4*p^3 -27*q^2.
assert -4 * 1**3 - 27 * (-1)**2 == -31
assert all(v**3 + v - 1 != 0 for v in (-1, 1))  # rational-root theorem
print("IDENTITY_MONOMIAL_INPUT_CHECK_OK")
