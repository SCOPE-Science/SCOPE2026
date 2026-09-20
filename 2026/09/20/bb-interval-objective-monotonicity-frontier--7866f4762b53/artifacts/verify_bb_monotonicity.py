import numpy as np

def gap_from_gradient(A, g):
    return 0.5 * float(g @ np.linalg.solve(A, g))

def bb1(A, v):
    return float(v @ v / (v @ A @ v))

def bb2(A, v):
    Av = A @ v
    return float(v @ Av / (Av @ Av))

def construction(kappa, r, theta):
    A = np.diag([1.0, kappa])
    g0 = np.array([1.0, np.sqrt(r)])
    eta0 = bb1(A, g0)
    g1 = (np.eye(2) - eta0 * A) @ g0
    e1 = bb1(A, g0)
    e2 = bb2(A, g0)
    eta1 = theta * e1 + (1.0 - theta) * e2
    g2 = (np.eye(2) - eta1 * A) @ g1
    ratio = gap_from_gradient(A, g2) / gap_from_gradient(A, g1)
    formula = (
        kappa * r * (1.0 - eta1) ** 2
        + (1.0 - kappa * eta1) ** 2
    ) / (1.0 + kappa * r)
    return eta0, e1, e2, eta1, ratio, formula

rng = np.random.default_rng(20260920)
max_excess = -np.inf
max_normalized = 0.0
checks = 0

for n in (2, 4, 8):
    for _ in range(300):
        kappa = float(rng.uniform(1.001, 30.0))
        Q, _ = np.linalg.qr(rng.normal(size=(n, n)))
        eig = 1.0 + (kappa - 1.0) * rng.random(n)
        eig[0] = 1.0
        eig[-1] = kappa
        A = Q @ np.diag(eig) @ Q.T
        previous_gradient = rng.normal(size=n)
        current_gradient = rng.normal(size=n)
        eta_lo = bb2(A, previous_gradient)
        eta_hi = bb1(A, previous_gradient)
        theta = float(rng.random())
        eta = theta * eta_hi + (1.0 - theta) * eta_lo
        next_gradient = (np.eye(n) - eta * A) @ current_gradient
        ratio = gap_from_gradient(A, next_gradient) / gap_from_gradient(A, current_gradient)
        bound = (kappa - 1.0) ** 2
        max_excess = max(max_excess, ratio - bound)
        if bound > 0:
            max_normalized = max(max_normalized, ratio / bound)
        checks += 1

assert max_excess < 2e-11

print("random_bound_checks", checks)
print("max_bound_excess", f"{max_excess:.3e}")
print("max_ratio_over_sharp_bound", f"{max_normalized:.12f}")

r = 1e-10
for kappa in (1.5, 2.0, 2.1, 3.0, 10.0):
    vals = []
    for theta in (0.0, 0.25, 0.5, 0.75, 1.0):
        eta0, e1, e2, eta1, ratio, formula = construction(kappa, r, theta)
        assert abs(ratio - formula) < 5e-10
        vals.append(ratio)
    print(
        "construction",
        f"kappa={kappa:.1f}",
        f"min_selector_ratio={min(vals):.12f}",
        f"max_selector_ratio={max(vals):.12f}",
        f"sharp_sup={(kappa-1.0)**2:.12f}",
    )
    if kappa <= 2.0:
        assert max(vals) <= 1.0 + 1e-8
    else:
        assert min(vals) > 1.0

print("all_checks_passed")
