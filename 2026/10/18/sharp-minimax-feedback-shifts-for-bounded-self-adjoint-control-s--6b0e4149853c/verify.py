"""Independent finite checks of the finite-interval feedback-shift theorem.

Run: python verify.py. The continuum and minimax assertions have an analytic proof.
"""
import math
import numpy as np
import sympy as sp


def spectral_design(alpha, lower, upper):
    lo = math.atan(math.sqrt(alpha) * lower)
    hi = math.atan(math.sqrt(alpha) * upper)
    mid = (lo + hi) / 2
    delta = (1 / math.tan(mid)) / math.sqrt(alpha)
    central = math.tan(mid) / math.sqrt(alpha)
    guarantee = 1 / (math.cos((hi - lo) / 2) ** 2)
    return delta, central, guarantee


def ratio(alpha, lower, upper, delta):
    central = 1 / (alpha * delta)
    args = [lower, upper]
    if lower < central < upper:
        args.append(central)
    vals = [(1 + alpha * a * a) / (a + delta) ** 2 for a in args]
    return max(vals) / min(vals)


def check():
    tests = 0
    sq2 = sp.sqrt(2)
    delta = 1 + sq2
    core = sq2 - 1
    q = lambda t: (1 + t ** 2) / (t + delta) ** 2
    assert sp.simplify(q(sp.Integer(0)) - q(sp.Integer(1))) == 0
    assert sp.simplify(q(sp.Integer(0)) / q(core) - (4 - 2 * sq2)) == 0
    assert sp.simplify(delta * core - 1) == 0
    tests += 3

    rng = np.random.default_rng(20260713)
    for _ in range(420):
        alpha = 10.0 ** rng.uniform(-2.8, 2.8)
        lower = 0.0 if rng.integers(3) == 0 else 10.0 ** rng.uniform(-3, 1)
        upper = lower + 10.0 ** rng.uniform(-3, 2.6)
        delta, central, optimum = spectral_design(alpha, lower, upper)
        assert lower < central < upper
        assert 1 <= optimum < 2
        exact = ratio(alpha, lower, upper, delta)
        assert math.isclose(exact, optimum, rel_tol=3e-12, abs_tol=2e-12)
        tests += 3

        for multiplier in [0.01, 0.05, 0.1, 0.3, 0.75, 0.9, 1.0, 1.1, 1.4, 3, 10, 100]:
            actual = ratio(alpha, lower, upper, delta * multiplier)
            assert actual >= optimum - 4e-10
            if multiplier != 1:
                assert actual > optimum - 1e-11
            tests += 1

        # Orthogonally rotated matrix direct Hessian calculation.
        vals = [lower, central, upper]
        z = rng.normal(size=(3, 3))
        frame, _ = np.linalg.qr(z)
        a = frame @ np.diag(vals) @ frame.T
        dmat = np.linalg.solve(a + delta * np.eye(3), np.eye(3))
        h = dmat @ (np.eye(3) + alpha * (a @ a)) @ dmat
        w = np.linalg.eigvalsh(h)
        assert abs(w[-1] / w[0] - optimum) < 1e-8 * optimum
        tests += 1

        # Exactly two endpoint eigenvalues are made equal by this shift.
        f0 = (1 + alpha * lower * lower) / (lower + delta) ** 2
        f1 = (1 + alpha * upper * upper) / (upper + delta) ** 2
        assert math.isclose(f0, f1, rel_tol=2e-11)
        tests += 1

    # The parameter-uniform dimensionless threshold tends to two.
    for big in [10, 100, 1000]:
        _, _, optimum = spectral_design(1, 0, big)
        assert optimum < 2 and optimum > 1.8
        tests += 1
    print(f"PASS {tests} exact-symbolic and finite-matrix/scalar checks")


if __name__ == '__main__':
    check()
