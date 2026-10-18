"""Reproduce finite diagnostics for the critical-width Fock annulus formula.

Requires Python 3 and scipy. Finite diagnostics are not substitutes for the
analytic uniform Berry--Esseen and spectral arguments.
"""
from math import erf, exp, lgamma, log, pi, sqrt
from scipy.special import gammainc


def Phi(x):
    return (1.0 + erf(x / sqrt(2.0))) / 2.0


def phi(x):
    return exp(-x * x / 2.0) / sqrt(2.0 * pi)


def G(x):
    return x * Phi(x) + phi(x)


def Q(c, w):
    return 2.0 * (G((w + c) / 2.0) - G((w - c) / 2.0)) - c


def LAMBDA(c, w):
    return Phi((w + c) / 2.0) - Phi((c - w) / 2.0)


def tau(k, A, B):
    return float(gammainc(k + 1, B) - gammainc(k + 1, A))


def difference_exact(k, A, B):
    # This is the exact analytic integration-by-parts expression evaluated
    # numerically with log-gamma stabilization.
    q = lgamma(k + 2)
    return exp((k + 1) * log(A) - A - q) - exp((k + 1) * log(B) - B - q)


def trial(a, b, c, R):
    A = R + a * sqrt(R)
    B = R + b * sqrt(R)
    N = int(c * sqrt(R))
    assert 0 < A < B and N > 0
    window = sqrt(R)
    lo = max(0, int(R + min(a, b) * window - (12 + c) * window))
    hi = int(R + max(a, b) * window + (12 + c) * window)
    vals = [tau(k, A, B) for k in range(lo, hi + 1)]
    sorted_inds = sorted(range(len(vals)), key=lambda j: -vals[j])
    selected = sorted(sorted_inds[:N])
    # Only a finite window is examined here; the global statement is proved
    # analytically in RESULT.md by the exact adjacent-difference identity.
    assert selected[-1] - selected[0] + 1 == N
    partial = sum(vals[j] for j in selected)
    target = sqrt(R) * Q(c, b - a)
    assert abs(partial - target) < 3.0, (a, b, c, R, partial, target)
    edge = vals[sorted_inds[N - 1]]
    assert abs(edge - LAMBDA(c, b - a)) < 0.07, (edge, c, b - a)
    for shift in [-4, -2, 0, 2, 4]:
        k = int((A + B) / 2 + shift * sqrt(R))
        if k < 0:
            continue
        numeric_gap = tau(k + 1, A, B) - tau(k, A, B)
        exact_gap = difference_exact(k, A, B)
        assert abs(numeric_gap - exact_gap) < 4e-11, (numeric_gap, exact_gap)
    # A distributional check on the critical scale.
    for x in [(a + b) / 2 - c / 2, (a + b) / 2, (a + b) / 2 + c / 2]:
        k = round(R + x * sqrt(R))
        f = Phi(b - x) - Phi(a - x)
        assert abs(tau(k, A, B) - f) < 0.065
    return partial / sqrt(R), edge


def main():
    cases = [(-1., 1.5, 2.), (-2.5, -.1, 1.8), (0., .75, 3.5), (-.3, 3.1, .5)]
    checks = 0
    for a, b, c in cases:
        w = b - a
        assert 0 < Q(c, w) < min(c, w)
        assert abs(Q(c, w) - Q(w, c)) < 1e-12
        checks += 2
        for R in (400, 3600, 22500):
            partial, edge = trial(a, b, c, R)
            print(f"a={a:g} b={b:g} c={c:g} R={R}: partial/sqrtR={partial:.9f}, "
                  f"Q={Q(c,w):.9f}, last={edge:.9f}, limit={LAMBDA(c,w):.9f}")
            checks += 10
    print(f"PASS: {checks} finite diagnostic groups; proof is analytic, not enumerative.")


if __name__ == '__main__':
    main()
