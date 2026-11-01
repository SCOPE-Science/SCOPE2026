"""Reproduce finite algebraic and numerical checks of an Arnoldi coefficient theorem.

Infinite moment and tail assertions are proved in RESULT.md, not by this test.
"""
import math
import numpy as np
import sympy as sp

r11, r12, r13, r22, r23, r33 = sp.symbols(
    "r11 r12 r13 r22 r23 r33", positive=True
)
R = sp.Matrix([[r11, r12, r13], [0, r22, r23], [0, 0, r33]])
A = sp.Matrix([[2, 1, 0], [1, 2, 1], [0, 1, 2]])
expected = -(
    r11**2 * r23 - r11*r12*r22 + r11*r13*r23
    - r12**2*r23 + r12*r13*r22
) / (r11*r22*r33)
assert sp.cancel((R*A*R.inv())[0, 2] - expected) == 0
assert A.det() == 4 and A[:2, :2].det() == 3
assert sp.simplify(sp.expand((R*A*R.inv())[0, 2]) - expected) == 0
print('symbolic similarity and positive-definiteness checks: PASS')

rng = np.random.default_rng(20330215)
nchecks = 0
for ell in [3, 4, 5, 7, 12, 40]:
    for _ in range(150):
        G = rng.normal(size=(ell, 3))
        Q, RR = np.linalg.qr(G, mode='reduced')
        signs = np.sign(np.diag(RR))
        assert np.all(signs != 0)
        RR = signs[:, None] * RR
        Q = Q * signs[None, :]
        Af = np.array(A).astype(float)
        H = RR @ Af @ np.linalg.inv(RR)
        a, b, c = RR[0]
        d, e = RR[1, 1:]
        f = RR[2, 2]
        exact = - (a*a*e-a*b*d+a*c*e-b*b*e+b*c*d)/(a*d*f)
        assert np.isclose(H[0, 2], exact, atol=4e-8, rtol=3e-9)
        # Independently replay the sketched modified Gram-Schmidt Arnoldi algorithm.
        v1 = np.array([1., 0., 0.]) / np.linalg.norm(G[:, 0])
        basis = [v1]
        qb = [G @ v1]
        h13 = None
        for j in range(3):
            z = Af @ basis[j]
            sketched = G @ z
            h = []
            for i in range(j + 1):
                hij = qb[i] @ sketched
                h.append(hij)
                sketched = sketched - hij * qb[i]
            if j == 2:
                h13 = h[0]
            else:
                z = z - np.column_stack(basis) @ np.array(h)
                norm = np.linalg.norm(G @ z)
                basis.append(z/norm)
                qb.append(G @ z/norm)
        assert np.isclose(h13, exact, atol=4e-8, rtol=3e-9)
        nchecks += 1
    print(f'sketch rows {ell}: 150 QR and direct-Arnoldi comparisons PASS')

# The chi small-ball limit is obtained from an elementary convergent integral;
# compare its exact coefficient to a numerical incomplete gamma evaluation.
for k in (1, 2, 3, 4, 6):
    const = 1/(2**(k/2)*math.gamma(k/2+1))
    x = sp.Rational(1, 10000)
    cdf = sp.lowergamma(sp.Rational(k, 2), x*x/2)/sp.gamma(sp.Rational(k, 2))
    rel = float(cdf) / (float(x)**k * const)
    assert 0.9999998 < rel <= 1.0000001, (k, rel)
print(f'PASS: {nchecks} direct Gaussian-sketch Arnoldi regression checks, '+
      '3 symbolic checks, 5 independent chi small-ball checks')
