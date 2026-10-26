"""Standalone finite checks of the cone-affine projector identities.
The universal statement is proved analytically in RESULT.md; this program is a diagnostic.
"""
from fractions import Fraction
import math
import numpy as np
from scipy.special import roots_jacobi


def constants(d):
    m = d + 1
    z = Fraction(m + 1, m + 2)
    apex = 2 * (m + 1) * z**m - 1
    base_sq = Fraction(1) + Fraction((m + 2)**2, m)
    return m, apex, base_sq


def row_quadrature(d, s, r, n=240):
    """Rotational reduction; evaluate at (r,0,...,0,s), with 0<=r<=s."""
    m, _, _ = constants(d)
    jt, wt = roots_jacobi(n, 0, m - 1)
    ju, wu = roots_jacobi(n, (d - 1) / 2, (d - 1) / 2)
    tt = (jt + 1) / 2
    wt = wt / np.sum(wt)
    wu = wu / np.sum(wu)
    eta = m / (m + 1)
    var_t = m / ((m + 1)**2 * (m + 2))
    c = (m + 1) * (m + 2) / m
    center = 1 + (s - eta) * (tt - eta) / var_t
    k = center[:, None] + c * r * tt[:, None] * ju[None, :]
    return float(np.sum(wt[:, None] * wu[None, :] * np.abs(k)))


def run():
    count_exact = 0
    for d in range(2, 161):
        m, a, b2 = constants(d)
        assert a * a > b2, (d, a, b2)
        count_exact += 1
        mu = Fraction(m, m + 1)
        var = Fraction(m, (m + 1)**2 * (m + 2))
        et2 = Fraction(m, m + 2)
        assert et2 - mu * mu == var
        assert et2 * Fraction(1, d + 2) == Fraction(m, (m + 1) * (m + 2))
        # Exact evaluation kernel reproduction of coordinates, for s=2/5, r=1/4.
        s, r = Fraction(2, 5), Fraction(1, 4)
        coeff = Fraction((m + 1) * (m + 2), m)
        assert 1 + (s - mu) * (mu - mu) / var == 1
        assert mu + (s - mu) * (et2 - mu * mu) / var == s
        assert coeff * r * et2 / (d + 2) == r
        count_exact += 4
    count_num = 0
    for d in (2, 3, 4, 5, 8, 12):
        m, exact_a, b2 = constants(d)
        a = float(exact_a)
        b = math.sqrt(float(b2))
        num_a = row_quadrature(d, 0, 0)
        assert abs(num_a - a) < 0.004, (d, num_a, a)
        for s in (.1, .4, .85, 1.0):
            for f in (0, .5, 1):
                val = row_quadrature(d, s, s * f)
                assert val <= (1 - s) * a + s * b + 0.003, (d,s,f,val,(1-s)*a+s*b)
                assert val >= (1 - s) * a - s * b - 0.003, (d,s,f,val,(1-s)*a-s*b)
                count_num += 1
    print(f"PASS: {count_exact} exact rational checks; {count_num} quadrature row checks; 6 apex integrals")


if __name__ == '__main__':
    run()
