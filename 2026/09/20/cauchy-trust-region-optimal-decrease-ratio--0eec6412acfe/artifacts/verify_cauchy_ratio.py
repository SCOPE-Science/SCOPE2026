"""Deterministic checks for the SPD Cauchy trust-region decrease ratio.

Requires Python 3 and NumPy.  No random sampling is used.
"""
import numpy as np


def exact_tr(B, g, delta):
    """Exact SPD trust-region solution via eigendecomposition and scalar bisection."""
    w, V = np.linalg.eigh(B)
    gh = V.T @ g
    p_newton = -(V @ (gh / w))
    if np.linalg.norm(p_newton) <= delta * (1.0 + 1e-14):
        return p_newton

    def norm_p(lam):
        return np.linalg.norm(gh / (w + lam))

    lo, hi = 0.0, 1.0
    while norm_p(hi) > delta:
        hi *= 2.0
        if hi > 1e16:
            raise RuntimeError("failed to bracket secular root")
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if norm_p(mid) > delta:
            lo = mid
        else:
            hi = mid
    lam = 0.5 * (lo + hi)
    return -(V @ (gh / (w + lam)))


def decrease(B, g, p):
    return -g @ p - 0.5 * p @ (B @ p)


def cauchy(B, g, delta):
    G = np.linalg.norm(g)
    alpha = min((G * G) / (g @ (B @ g)), delta / G)
    return -alpha * g


def fixed_gradient_bound(B, g):
    G = np.linalg.norm(g)
    u = g / G
    return 1.0 / ((u @ (B @ u)) * (u @ np.linalg.solve(B, u)))


print(f"NumPy {np.__version__}")

for kappa in [1.5, 2.0, 5.0, 10.0, 100.0]:
    B = np.diag([1.0, kappa])
    g = np.array([1.0, 1.0]) / np.sqrt(2.0)
    delta = 2.0 * np.linalg.norm(np.linalg.solve(B, g))
    ratio = decrease(B, g, cauchy(B, g, delta)) / decrease(
        B, g, exact_tr(B, g, delta)
    )
    target = 4.0 * kappa / (kappa + 1.0) ** 2
    assert abs(ratio - target) < 5e-13
    print(f"sharp kappa={kappa:g}: ratio={ratio:.15g}, target={target:.15g}")

angles = [0.13, 0.47, 0.91]
for kappa in [1.2, 2.0, 5.0, 20.0, 100.0]:
    condition_bound = 4.0 * kappa / (kappa + 1.0) ** 2
    for theta in angles:
        c, s = np.cos(theta), np.sin(theta)
        Q = np.array([[c, -s], [s, c]])
        B = Q @ np.diag([1.0, kappa]) @ Q.T
        for phi in [0.07, 0.31, 0.79, 1.23]:
            g = np.array([np.cos(phi), np.sin(phi)])
            fixed_bound = fixed_gradient_bound(B, g)
            assert fixed_bound + 2e-13 >= condition_bound
            newton_norm = np.linalg.norm(np.linalg.solve(B, g))
            q = (g @ (B @ g)) / (g @ g)
            cauchy_threshold = np.linalg.norm(g) / q
            for scale in [0.02, 0.1, 0.4, 0.9, 1.0, 1.5, 4.0]:
                delta = scale * min(newton_norm, cauchy_threshold)
                ratio = decrease(B, g, cauchy(B, g, delta)) / decrease(
                    B, g, exact_tr(B, g, delta)
                )
                assert ratio + 2e-12 >= fixed_bound
print("deterministic 2D radius grid: PASS")

B = np.array(
    [
        [5.0, 1.0, 0.2, 0.0],
        [1.0, 3.0, 0.4, 0.1],
        [0.2, 0.4, 2.0, 0.3],
        [0.0, 0.1, 0.3, 1.2],
    ]
)
g = np.array([1.0, -0.4, 0.7, 0.2])
fixed_bound = fixed_gradient_bound(B, g)
for delta in np.geomspace(1e-3, 10.0, 41):
    ratio = decrease(B, g, cauchy(B, g, delta)) / decrease(
        B, g, exact_tr(B, g, delta)
    )
    assert ratio + 2e-11 >= fixed_bound
print(f"4D fixed-gradient bound: PASS, bound={fixed_bound:.15g}")
print("ALL CHECKS PASS")
