import math
import numpy as np


def objective_ratio(A, e, gamma):
    s1 = e @ A @ e
    s2 = e @ A @ A @ e
    alpha = 0.5 * gamma * s1 / s2
    ep = e - alpha * (A @ e)
    return (ep @ A @ ep) / s1


def sharp_bound(kappa, gamma):
    return 1.0 - gamma + (gamma * gamma) * (kappa + 1.0) ** 2 / (16.0 * kappa)


def safety_gamma(kappa):
    return 16.0 * kappa / (kappa + 1.0) ** 2


def main():
    rng = np.random.default_rng(20260920)
    kappas = [1.0, 2.0, 5.0, 10.0, 7.0 + 4.0 * math.sqrt(3.0), 20.0, 100.0]
    gammas = [0.5, 1.0, 2.0]

    worst_violation = -math.inf
    equality_error = 0.0
    for kappa in kappas:
        Aeq = np.diag([1.0, kappa])
        eeq = np.array([kappa, 1.0])
        for gamma in gammas:
            r = objective_ratio(Aeq, eeq, gamma)
            q = sharp_bound(kappa, gamma)
            equality_error = max(equality_error, abs(r - q))

        for _ in range(500):
            n = 5
            Q, _ = np.linalg.qr(rng.normal(size=(n, n)))
            vals = np.exp(rng.uniform(0.0, math.log(max(kappa, 1.0)), size=n))
            vals[0] = 1.0
            vals[-1] = kappa
            A = Q @ np.diag(vals) @ Q.T
            e = rng.normal(size=n)
            for gamma in gammas:
                r = objective_ratio(A, e, gamma)
                q = sharp_bound(kappa, gamma)
                worst_violation = max(worst_violation, r - q)

    k_std = 7.0 + 4.0 * math.sqrt(3.0)
    k_twice = 3.0 + 2.0 * math.sqrt(2.0)
    assert abs(sharp_bound(k_std, 1.0) - 1.0) < 2e-14
    assert abs(sharp_bound(k_twice, 2.0) - 1.0) < 2e-14

    for kappa in [1.0, 2.0, 5.0, 20.0, 100.0]:
        gamma_star = 8.0 * kappa / (kappa + 1.0) ** 2
        q_star = sharp_bound(kappa, gamma_star)
        q_line = ((kappa - 1.0) / (kappa + 1.0)) ** 2
        assert abs(q_star - q_line) < 2e-14
        assert abs(2.0 * gamma_star - safety_gamma(kappa)) < 2e-14

    assert equality_error < 2e-12
    assert worst_violation < 2e-12

    print("PASS")
    print(f"NumPy version: {np.__version__}")
    print(f"max equality error: {equality_error:.3e}")
    print(f"max random bound violation: {worst_violation:.3e}")
    print(f"standard Polyak threshold: {k_std:.15f}")
    print(f"twice-Polyak threshold: {k_twice:.15f}")
    print(f"Q_standard(kappa=20): {sharp_bound(20.0, 1.0):.15f}")
    print(f"Q_twice(kappa=10): {sharp_bound(10.0, 2.0):.15f}")


if __name__ == "__main__":
    main()
