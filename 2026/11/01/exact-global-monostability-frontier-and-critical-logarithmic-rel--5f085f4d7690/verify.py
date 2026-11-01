"""Independent reproducible algebraic and numerical checks for a logistic feedback-network theorem.

Run: python verify.py (requires sympy, numpy and scipy).
The checks are finite illustrations, not substitutes for the proof.
"""
import math
import numpy as np
import sympy as sp
from scipy.special import expit
from scipy.integrate import solve_ivp

u = sp.symbols('u')
scalar = sp.Rational(1, 2) * sp.tanh(2 * u) - u
assert sp.expand(sp.series(scalar, u, 0, 8).removeO()).coeff(u, 3) == -sp.Rational(4, 3)
assert sp.expand(sp.series(scalar, u, 0, 8).removeO()).coeff(u, 5) == sp.Rational(32, 15)
assert sp.Rational(2, 1) * sp.Rational(4, 3) == sp.Rational(8, 3)
assert -sp.Rational(32, 15) / sp.Rational(4, 3) == -sp.Rational(8, 5)

for beta in (4.01, 5.0, 9.0):
    discriminant = math.sqrt(1 - 4 / beta)
    qm, qp = (1 - discriminant) / 2, (1 + discriminant) / 2
    alow = math.log(qp / (1 - qp)) - beta * qp
    ahigh = math.log(qm / (1 - qm)) - beta * qm
    assert alow < ahigh
    for q, aa in ((qm, ahigh), (qp, alow)):
        assert abs(expit(aa + beta * q) - q) < 1e-12
        assert abs(beta * q * (1 - q) - 1) < 1e-12

matrices = (
    np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=float),
    np.array([[0.5, 0.5, 0], [0, 0.25, 0.75], [0.2, 0, 0.8]], dtype=float),
)
for W in matrices:
    assert np.allclose(W.sum(axis=1), 1)
    eig = np.linalg.eigvals(W)
    assert sum(abs(z-1)<1e-8 for z in eig) == 1
    assert all(z.real < 1-1e-8 for z in eig if abs(z-1)>1e-8)
    for init in ([0.9, 0.8, 0.4], [0.2, 0.35, 0.44]):
        rhs = lambda _, x: -x + expit(-2 + 4 * (W @ x))
        sol = solve_ivp(rhs, (0, 6000), init, t_eval=[2000, 6000], rtol=2e-11, atol=2e-12)
        assert sol.success
        distances = np.linalg.norm(sol.y.T - 0.5, axis=1, ord=np.inf)
        assert distances[1] < distances[0]
        assert abs(6000 * distances[1] ** 2 - 3/8) < 0.03
        residuals = [1/(z[0]-0.5)**2-8*t/3+8*math.log(t)/5 for t,z in zip(sol.t,sol.y.T)]
        assert abs(residuals[-1]-residuals[0]) < 1.0
print('PASS: exact fold identities and critical coefficients; finite irreducible-network illustrations')
