"""Reproducible numerical and rational checks for the scaled antilinear-isometry q-range formulas.

Requires Python 3 and NumPy. These finite checks supplement, but do not replace,
the proof valid in every Hilbert-space dimension.
"""
from fractions import Fraction
from math import sqrt
import numpy as np

J = np.array([[0, 1], [-1, 0]], dtype=complex)
rng = np.random.default_rng(261016823)
assert Fraction(4, 5)*Fraction(4, 5)-Fraction(3, 5)*Fraction(3, 5) == Fraction(7, 25)
assert Fraction(3, 5)*Fraction(4, 5)+Fraction(4, 5)*Fraction(3, 5) == Fraction(24, 25)
assert Fraction(3, 5)**2+Fraction(4, 5)**2 == 1
count = 3
for a in (0.0, 0.25, 0.6, 0.9, 1.0):
    b = sqrt(max(0, 1-a*a))
    U = a*np.eye(2, dtype=complex)+b*J
    assert np.allclose(U.conj().T@U, np.eye(2))
    for q in (0.0, .15, .35, .6, .8, 1.0):
        s = sqrt(max(0, 1-q*q))
        inn = max(0., b*s-a*q)
        out = 1. if q <= a else a*q+b*s
        in_seen, out_seen = 2., -1.
        for _ in range(10000):
            x = rng.normal(size=2)+1j*rng.normal(size=2)
            x /= np.linalg.norm(x)
            u = np.array([-np.conj(x[1]),np.conj(x[0])])
            Ax = U@np.conj(x)
            assert abs(np.vdot(x, u)) < 1e-11
            t = abs(np.vdot(x, Ax))
            parallel = q*t
            transverse = s*abs(np.vdot(u, Ax))
            in_seen = min(in_seen, abs(parallel-transverse))
            out_seen = max(out_seen, parallel+transverse)
            assert abs(parallel-transverse)+1e-10 >= inn
            assert parallel+transverse <= out+1e-10
            count += 2
        assert in_seen-inn < .028, (a,q,inn,in_seen)
        assert out-out_seen < .028, (a,q,out,out_seen)
        count += 2
print(f'PASS: {count} exact-rational or finite numerical checks; all 2D annulus bounds and near-extrema agree.')
