"""Exact determinant identity and independent numerical Choi checks.
Run with Python 3, sympy and numpy: python verify.py
"""
import sympy as S
import numpy as np

h, g, k, ell, c, s = S.symbols('h g k ell c s', real=True)
A0 = S.diag(1, h)
A1 = S.Matrix([[0, k], [0, 0]])
B0 = S.diag(1, g)
B1 = S.Matrix([[0, ell], [0, 0]])
U = S.Matrix([[c, -s], [s, c]])
K = [A * U * B for A in (A0, A1) for B in (B0, B1)]
J = S.zeros(4)
for i in range(2):
    for j in range(2):
        eij = S.zeros(2)
        eij[i, j] = 1
        out = sum((L * eij * L.T for L in K), S.zeros(2)) / 2
        for x in range(2):
            for y in range(2):
                J[2 * i + x, 2 * j + y] = out[x, y]
T = S.zeros(4)
for i in range(2):
    for j in range(2):
        for x in range(2):
            for y in range(2):
                T[2 * i + y, 2 * j + x] = J[2 * i + x, 2 * j + y]
actual = S.factor(16 * T.det())
expected = h**4 * (k**4 * ell**4 * s**8 - g**4)
assert S.factor((actual - expected).subs(c**2, 1 - s**2)) == 0
assert S.simplify(sum((L.T * L for L in K), S.zeros(2)).subs(
    k**2, 1 - h**2).subs(ell**2, 1-g**2).subs(c**2, 1-s**2) - S.eye(2)) == S.zeros(2)


def numeric_choi(a, b, t):
    co, si = np.sqrt(1-t), np.sqrt(t)
    rot = np.array([[co, -si], [si, co]])
    def ad(x):
        return [np.diag([1., np.sqrt(x)]),
                np.array([[0., np.sqrt(1-x)], [0., 0.]])]
    ks = [ka @ rot @ kb for ka in ad(a) for kb in ad(b)]
    vec = np.array([1., 0., 0., 1.])/np.sqrt(2.)
    projector = np.outer(vec, vec)
    choi = sum((np.kron(np.eye(2), M) @ projector @
                np.kron(np.eye(2), M.T) for M in ks), np.zeros((4,4)))
    pt = choi.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)
    return choi, pt

cases = [(0.5, 1/9, 0.25), (0.5, 1/9, 0.5),
         (0.5, 1/9, 0.75), (1/9, 0.5, 1),
         (0.35, 0.35, 1), (0.5, 0.5, 1),
         (0.8, 0.01, 0.3), (0.8, 0.01, 1)]
for a,b,t in cases:
    choi, pt = numeric_choi(a,b,t)
    eig = np.linalg.eigvalsh(pt)
    det = a*a/16 * ((1-a)**2 * (1-b)**2 * t**4 - b*b)
    assert abs(np.linalg.det(pt) - det) < 1e-11
    assert abs(np.trace(choi)-1) < 1e-11
    assert np.linalg.eigvalsh(choi)[0] > -1e-11
    if (1-a)*(1-b)*t*t >= b + 1e-8:
        assert eig[0] > -1e-10
    if (1-a)*(1-b)*t*t < b - 1e-8:
        assert eig[0] < -1e-10
# An exact transition t=1/2 and an exact order-sensitive witness.
assert S.Rational(1,2) * S.Rational(8,9) * S.Rational(1,2)**2 == S.Rational(1,9)
assert S.Rational(8,9) * S.Rational(1,2) < S.Rational(1,2)
print('VERIFY_OK symbolic_Choi_determinant=passed Kraus_trace=passed numerical_cases=8 order_boundary=passed')
