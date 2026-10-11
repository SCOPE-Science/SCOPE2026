"""Finite diagnostics for an analytic numerical-range compression theorem.

Requires sympy, numpy, scipy. The numerical cases are illustrative, not a proof
of the universal statement; the symbolic identity is exact for the 3-4-5 example.
"""
import math
import numpy as np
import sympy as sp
from scipy.linalg import null_space

w = sp.symbols('w')
vertices_exact = (sp.Integer(0), sp.Integer(3), 4*sp.I)
center_exact = 1 + sp.I
weights_exact = (sp.Rational(1, 6), sp.Rational(1, 3), sp.Rational(1, 2))
P = sum(weights_exact[i] * sp.prod(w-vertices_exact[j]
         for j in range(3) if j != i) for i in range(3))
assert sp.expand(P - (w-center_exact)**2) == 0
assert sum(weights_exact) == 1

triangles = [
    (0+0j, 3+0j, 0+4j),
    (-1+0j, 1+0j, 0+0.1j),
    (0+0j, 2+0.1j, 1+3j),
    (1+2j, -3+1j, 2-2j),
    (-2-1j, 1+2j, 4-3j),
]
for vertices in triangles:
    z = np.asarray(vertices, dtype=complex)
    side = np.asarray([abs(z[1]-z[2]), abs(z[2]-z[0]),
                       abs(z[0]-z[1])], dtype=float)
    c = (side @ z) / sum(side)
    area = abs(np.imag(np.conj(z[1]-z[0])*(z[2]-z[0]))) / 2
    r = 2*area/sum(side)
    p = np.asarray([((z[i]-c)**2 / ((z[i]-z[(i+1)%3]) *
        (z[i]-z[(i+2)%3]))).real for i in range(3)])
    assert np.all(p > 0)
    assert abs(sum(p)-1) < 3e-12
    for i in range(3):
        v = (z[i]-c)**2/((z[i]-z[(i+1)%3])*(z[i]-z[(i+2)%3]))
        assert abs(v-p[i]) < 3e-12
    Q = null_space(np.sqrt(p).reshape(1,3))
    C = Q.conj().T @ np.diag(z) @ Q
    assert np.max(abs(np.linalg.eigvals(C)-c)) < 2e-7
    assert np.max(abs((C-c*np.eye(2))@(C-c*np.eye(2)))) < 2e-12
    circle_radius = np.linalg.norm(C-c*np.eye(2), ord='fro')/2
    assert math.isclose(circle_radius,r,rel_tol=1e-10,abs_tol=1e-11)
print('INCIRCLE_COMPRESSION_EXACT_AND_FINITE_OK')
