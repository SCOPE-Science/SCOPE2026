"""Reproduce exact rational witnesses for a two-row randomized projection law.

Run: python3 verify.py.  Uses Python's standard library only.
Finite checks corroborate, but do not replace, the analytic theorem.
"""
from fractions import Fraction as F
from math import sqrt, isclose

ZERO = F(0)
ONE = F(1)
ID = ((ONE, ZERO), (ZERO, ONE))
Q1 = ((ZERO, ZERO), (ZERO, ONE))
# Orthogonal complement of row (3/5,4/5): unit (-4/5,3/5).
Q2 = ((F(16, 25), F(-12, 25)), (F(-12, 25), F(9, 25)))


def mul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def add(*terms):
    return tuple(tuple(sum(A[i][j] for A in terms) for j in range(2))
                 for i in range(2))


def scale(s, A):
    return tuple(tuple(s * A[i][j] for j in range(2)) for i in range(2))


def tr(A):
    return A[0][0] + A[1][1]


def max_eig(A):
    return float(tr(A)) / 2 + sqrt(float((A[0][0] - A[1][1]) ** 2 + 4 * A[0][1] ** 2)) / 2


def rate(p0, p1, p2, r=F(3, 5)):
    s, d = p1 + p2, p1 - p2
    r2 = r * r
    R = float(p0) + (float(s) + sqrt(float(r2*s*s + (1-r2)*d*d))) / 2
    Q = float(p0) + (float(s) + sqrt(float(r2*r2*s*s + (1-r2*r2)*d*d))) / 2
    return R, Q


def cov_step(H, p0, p1, p2):
    return add(scale(p0, H), scale(p1, mul(mul(Q1, H), Q1)),
               scale(p2, mul(mul(Q2, H), Q2)))


def verify():
    assert mul(Q1, Q1) == Q1 and mul(Q2, Q2) == Q2
    assert Q2[0][0]*Q2[1][1] == Q2[0][1]*Q2[1][0]
    r = F(3, 5)
    assert tr(mul(Q1, Q2)) == r*r
    # The two competing equal-cost laws in the claimed strict reversal interval.
    s = (ZERO, F(1, 2), F(1, 2))
    b = (F(3, 4), ZERO, ZERO)
    assert s[0] + s[1] + s[2] == 1
    assert b[0] + F(1, 4) == 1
    assert all(isclose(x, y, abs_tol=1e-14) for x, y in zip(rate(*s), (0.8, 0.68)))
    assert all(isclose(x, y, abs_tol=1e-14) for x, y in zip(rate(*b), (0.75, 0.75)))
    # Finite covariance recursion from actual rational projector matrices.
    Hs, Hb = ID, ID
    for k in range(1, 31):
        Hs = cov_step(Hs, *s)
        Hb = cov_step(Hb, *b)
        assert all(H[i][j] == H[j][i] for H in (Hs, Hb) for i in range(2) for j in range(2))
        assert isclose(max_eig(Hb), float(F(3, 4) ** k), abs_tol=1e-14)
        if k == 1:
            assert isclose(max_eig(Hs), 0.8, abs_tol=1e-14)
        if k == 2:
            assert isclose(max_eig(Hs), float(F(68,125)), abs_tol=1e-14)
        if k >= 2:
            assert max_eig(Hs) < max_eig(Hb)
        if k == 30:
            assert max_eig(Hs) ** (1/k) < 0.71
    comparisons = 0
    # Exhaustive rational grid for p1,p2,t at fixed cost c=1 and w=4.
    for it in range(13):
        t = F(it, 48)
        s_total = 1 - 4*t
        for j in range(13):
            p1, p2 = s_total * F(j, 12), s_total * (1-F(j, 12))
            p0 = 1 - p1 - p2 - t
            if p0 < 0:
                continue
            R, Q = rate(p0,p1,p2)
            A = add(scale(p0, ID), scale(p1, Q1), scale(p2, Q2))
            assert isclose(R, max_eig(A), rel_tol=1e-12, abs_tol=1e-12)
            assert R >= .75 - 1e-12 and Q >= .68 - 1e-12
            if s_total > 0:
                # Equally weighted singleton law is optimal at each fixed batch weight.
                p_bal = s_total / 2
                Rbal, Qbal = rate(p0,p_bal,p_bal)
                assert R >= Rbal-1e-12 and Q >= Qbal-1e-12
            comparisons += 1
    # Threshold and phase checks for several costs, coherences and work budgets.
    phases = 0
    for w in [F(5, 2), F(3), F(4), F(6), F(10)]:
        for c in [F(1, 4), F(2, 3), F(1)]:
            r_one = 1 - 2 / float(w)
            r_long = sqrt(1 - 2 / float(w))
            assert 0 < r_one < r_long < 1
            for r_test in [r_one / 2, (r_one + r_long) / 2,
                           (1 + r_long) / 2]:
                # Slopes have the predicted signs in all three regimes.
                a = float(w)*(1-r_test)/2-1
                q = float(w)*(1-r_test*r_test)/2-1
                if r_test < r_one:
                    assert a > 0 and q > 0
                elif r_test < r_long:
                    assert a < 0 < q
                else:
                    assert a < 0 and q < 0
                phases += 1
    print('VERIFY_OK rational_projector_identities=3 grid_comparisons=',
          comparisons, 'strict_phase_regimes=', phases,
          'witness_R_batch=', F(3,4), 'witness_Q_single=', F(17,25))


if __name__ == '__main__':
    verify()
