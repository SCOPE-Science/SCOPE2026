"""Finite numerical diagnostics for the logistic scalar proximal bifurcation.

Requires Python 3, NumPy and SciPy. The proof of the global claims is in RESULT.md.
"""
import math
from scipy.integrate import quad
from scipy.optimize import brentq


def run_case(a):
    def p(t):
        return 1 / (1 + math.exp(-a * (t - 1)))

    def h(t):
        return t * p(t)

    def dh(t):
        z = p(t)
        return z + a * t * z * (1 - z)

    def ddh(t):
        z = p(t)
        return a * z * (1 - z) * (2 - a * t * math.tanh(a * (t - 1) / 2))

    t0 = brentq(ddh, 1, 1 + 5/a, xtol=1e-14)
    L = dh(t0)
    p0 = p(t0)
    H = a * a * p0 * (1 - p0) * (
        math.tanh(a * (t0 - 1) / 2)
        + (a * t0 / 2) / math.cosh(a * (t0 - 1) / 2) ** 2
    )
    bc = L / (L - 1)
    q = (L - 1) * math.sqrt(2 / H)
    assert H > 0 and L > 1 and t0 > 1
    assert abs(bc - p0 / (1 - p0)) < 1e-10
    assert abs(bc * t0 + (1 - bc) * h(t0) - 2 * h(t0)) < 1e-10
    print(f"a={a}: t0={t0:.12f}, L={L:.12f}, beta_c={bc:.12f}")

    for eps in (0.1, 0.02, 0.002):
        beta = bc + eps

        def S(t):
            return beta * t + (1 - beta) * h(t)

        target = beta / (beta - 1)
        left_fold = brentq(lambda t: dh(t) - target, 0, t0)
        right_fold = brentq(lambda t: dh(t) - target, t0, 30)
        smax, smin = S(left_fold), S(right_fold)
        assert smax > smin > 0

        def roots(s):
            left = brentq(lambda t: S(t) - s, 0, left_fold)
            right = brentq(lambda t: S(t) - s, right_fold, 30)
            return left, right

        def energy_gap(s):
            x, y = roots(s)
            return quad(lambda t: (S(t) - s) * dh(t), x, y,
                        epsabs=1e-13, epsrel=1e-12)[0]

        sstar = brentq(energy_gap, smin + 1e-8 * (smax - smin),
                        smax - 1e-8 * (smax - smin), xtol=1e-13)
        lo, hi = roots(sstar)
        jump = h(hi) - h(lo)
        predicted_gap = (4 / 3) * (L - 1) * q * eps ** 1.5
        predicted_jump = 2 * math.sqrt(3) * L * q * math.sqrt(eps)
        assert abs(energy_gap(sstar)) < 1e-8
        assert smin < sstar < smax
        assert abs((smax - smin) / predicted_gap - 1) < 0.1
        assert abs(jump / predicted_jump - 1) < 0.12
        if eps < 0.01:
            assert abs((sstar - S(t0)) / eps ** 1.5) < 0.01
        print(f"  offset={eps:.4g}, folds={smax-smin:.8g}, "
              f"fold/pred={(smax-smin)/predicted_gap:.8f}, "
              f"jump={jump:.8g}, jump/pred={jump/predicted_jump:.8f}")


if __name__ == "__main__":
    for aa in (1.5, 4, 8):
        run_case(aa)
    print("All finite diagnostics passed.")
