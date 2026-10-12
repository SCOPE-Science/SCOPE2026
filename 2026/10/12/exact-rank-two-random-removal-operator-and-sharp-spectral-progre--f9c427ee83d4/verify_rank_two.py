"""Exact-rational and quadrature checks for the rank-two removal law.

Run with Python 3: python verify_rank_two.py
This script checks identities on a finite family; the document contains the proof
for all positive eigenvalues and arbitrary positive-semidefinite test matrices.
"""
from fractions import Fraction
from math import cos, sin, pi, sqrt


def exact_check(p: int, q: int) -> None:
    assert 1 <= p <= q
    denom = p*p + q*q
    a, b = Fraction(p*p, denom), Fraction(q*q, denom)
    expected_gamma = Fraction(p*q, denom)
    # Exact rank-two operator, in the eigenbasis of X.
    B_a = a * Fraction(q, p+q)
    B_b = b * Fraction(p, p+q)
    sharp_c = Fraction(p, p+q)
    assert B_a + B_b == expected_gamma
    assert B_a >= sharp_c*a
    assert B_b == sharp_c*b  # extremal test Q = e_b e_b^T
    assert sharp_c >= a/(2*b)  # source-style lower bound
    # The improvement diverges as q/p tends to infinity.
    assert sharp_c / (a/(2*b)) == Fraction(2*q*q, p*(p+q))


def quadrature_check(a: float, b: float) -> None:
    N = 20000  # periodic trapezoid on analytic integrands
    s_gamma = s_aa = s_bb = s_ab = 0.0
    for j in range(N):
        t = 2*pi*j/N
        c, s = cos(t), sin(t)
        gamma = 1.0/(c*c/a+s*s/b)
        s_gamma += gamma
        s_aa += gamma*c*c
        s_bb += gamma*s*s
        s_ab += gamma*c*s
        # The maximal removal has zero determinant (rank one).
        da = a - gamma*c*c
        db = b - gamma*s*s
        off = -gamma*c*s
        assert da >= -5e-15 and db >= -5e-15
        assert abs(da*db - off*off) < 5e-14
    gamma_mean = s_gamma/N
    baa, bbb, bab = s_aa/N, s_bb/N, s_ab/N
    target_aa = a*sqrt(b)/(sqrt(a)+sqrt(b))
    target_bb = b*sqrt(a)/(sqrt(a)+sqrt(b))
    assert abs(gamma_mean-sqrt(a*b)) < 2e-11
    assert abs(baa-target_aa) < 2e-11
    assert abs(bbb-target_bb) < 2e-11
    assert abs(bab) < 2e-11


def run() -> None:
    for p in range(1, 45):
        for q in range(p, 45):
            exact_check(p, q)
    for a, b in [(.5,.5),(.01,.99),(.1,.9),(.25,.75),(.001,.999),(.36,.64)]:
        quadrature_check(a, b)
    print("VERIFY_OK: 990 exact spectral-rational cases, six quadrature checks")

if __name__ == '__main__':
    run()
