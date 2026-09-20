import math
import numpy as np

TOL = 2e-11
rng = np.random.default_rng(20260920)

def normalized_hessian(A):
    d = np.diag(A)
    Dm = np.diag(1.0 / np.sqrt(d))
    return Dm @ A @ Dm

def rho(C, p):
    s = np.sqrt(p)
    M = (s[:, None] * C) * s[None, :]
    return np.linalg.eigvalsh(M)[0]

def closed_form(C):
    q = np.linalg.solve(C, np.ones(C.shape[0]))
    p = q / q.sum()
    return p, 1.0 / q.sum(), q

def make_stieltjes(n):
    R = rng.uniform(0.0, 1.0, size=(n, n))
    W = np.triu(R, 1)
    W = W + W.T
    margin = rng.uniform(0.3, 1.4, size=n)
    A = np.diag(W.sum(axis=1) + margin) - W
    return A

max_formula_error = 0.0
max_random_excess = -math.inf
for n in (2, 3, 4, 6, 10):
    for _ in range(20):
        A = make_stieltjes(n)
        C = normalized_hessian(A)
        Cinv = np.linalg.inv(C)
        assert Cinv.min() > -TOL
        pstar, target, q = closed_form(C)
        assert q.min() > 0.0
        err = abs(rho(C, pstar) - target)
        max_formula_error = max(max_formula_error, err)
        for _ in range(500):
            p = rng.dirichlet(np.ones(n))
            max_random_excess = max(max_random_excess, rho(C, p) - target)

# Verify the expected A-energy decrement identity on one deterministic instance.
A = make_stieltjes(7)
C = normalized_hessian(A)
pstar, target, _ = closed_form(C)
e = rng.normal(size=7)
energy = e @ A @ e
expected_direct = 0.0
for i, pi in enumerate(pstar):
    g_i = A[i, :] @ e
    eplus = e.copy()
    eplus[i] -= g_i / A[i, i]
    expected_direct += pi * (eplus @ A @ eplus)
S = np.diag(pstar / np.diag(A))
expected_matrix = energy - e @ A @ S @ A @ e
identity_error = abs(expected_direct - expected_matrix)

# Dirichlet 1D Poisson formula.
poisson_rows = []
for n in (2, 3, 5, 10, 50, 200):
    A = 2.0 * np.eye(n)
    if n > 1:
        A += -np.eye(n, k=1) - np.eye(n, k=-1)
    C = A / 2.0
    pstar, target, q = closed_form(C)
    i = np.arange(1, n + 1, dtype=float)
    q_exact = i * (n + 1 - i)
    p_exact = 6.0 * q_exact / (n * (n + 1) * (n + 2))
    rho_exact = 6.0 / (n * (n + 1) * (n + 2))
    assert np.max(np.abs(q - q_exact)) < 2e-8
    assert np.max(np.abs(pstar - p_exact)) < 2e-12
    assert abs(target - rho_exact) < 2e-12
    uniform = (1.0 - math.cos(math.pi / (n + 1))) / n
    poisson_rows.append((n, target / uniform))

limit = 12.0 / math.pi**2
assert max_formula_error < TOL
assert max_random_excess <= 5e-12
assert identity_error < 2e-10
assert abs(poisson_rows[-1][1] - limit) < 0.02

print("closed_form_random_stieltjes: PASS")
print(f"max_abs_formula_error: {max_formula_error:.3e}")
print(f"max_sampled_rho_minus_optimum: {max_random_excess:.3e}")
print(f"energy_identity_abs_error: {identity_error:.3e}")
for n, ratio in poisson_rows:
    print(f"poisson_n={n}: rho_opt/rho_uniform={ratio:.12f}")
print(f"poisson_limit_12_over_pi2={limit:.12f}")
print("verification: PASS")
