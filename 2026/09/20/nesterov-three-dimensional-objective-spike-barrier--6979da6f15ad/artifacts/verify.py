import math
import numpy as np


def beta_from_kappa(kappa):
    q = 1.0 / math.sqrt(kappa)
    return q, (1.0 - q) / (1.0 + q)


def p_values(t, beta, steps):
    p = [1.0, 1.0 - t]
    for _ in range(1, steps):
        p.append((1.0 - t) * ((1.0 + beta) * p[-1] - beta * p[-2]))
    return np.array(p[: steps + 1])


def nag_trajectory(A, x0, steps, kappa):
    L = np.linalg.eigvalsh(A)[-1]
    _, beta = beta_from_kappa(kappa)
    xs = [np.array(x0, dtype=float)]
    y = xs[0].copy()
    for _ in range(steps):
        xnew = y - (A @ y) / L
        xs.append(xnew)
        y = xnew + beta * (xnew - xs[-2])
    return xs


def objective(A, x):
    return 0.5 * float(x @ A @ x)


rng = np.random.default_rng(271828)
kappas = [1.01, 1.1, 2.0, 10.0, 100.0, 10000.0]
max_low_formula_error = 0.0
max_endpoint_increase = 0.0
max_revival_error = 0.0
max_small_eps_asymptotic_error = 0.0
rows = []

for kappa in kappas:
    q, beta = beta_from_kappa(kappa)
    r = 1.0 - q

    p_low = p_values(q * q, beta, 20)
    closed = np.array([(1.0 + k * q) * r**k for k in range(21)])
    max_low_formula_error = max(max_low_formula_error, float(np.max(np.abs(p_low - closed))))

    theta = rng.uniform(0.0, 2.0 * math.pi)
    Q = np.array([[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]])
    A2 = Q @ np.diag([q * q, 1.0]) @ Q.T
    for _ in range(300):
        x0 = rng.normal(size=2)
        xs = nag_trajectory(A2, x0, 20, kappa)
        fs = np.array([objective(A2, x) for x in xs])
        max_endpoint_increase = max(max_endpoint_increase, float(np.max(np.diff(fs))))
        assert np.all(np.diff(fs) <= 5e-13 * max(1.0, fs[0]))

    tstar = 0.5 * (1.0 + q)
    pmid = p_values(tstar, beta, 3)
    exact_p3 = -(r**3) / (4.0 * (1.0 + q))
    max_revival_error = max(max_revival_error, abs(float(pmid[2])), abs(float(pmid[3] - exact_p3)))

    asymptotic = r * r / (32.0 * q * q * (1.0 + q) * (1.0 + 2.0 * q) ** 2)
    last_ratio = None
    last_scaled = None
    for eps in [1e-2, 1e-3, 1e-4, 1e-5]:
        A3 = np.diag([q * q, tstar, 1.0])
        xs = nag_trajectory(A3, np.array([eps, 1.0, 0.0]), 3, kappa)
        f2 = objective(A3, xs[2])
        f3 = objective(A3, xs[3])
        assert f2 > 0.0
        ratio = f3 / f2
        scaled = ratio * eps * eps
        if eps == 1e-5:
            max_small_eps_asymptotic_error = max(max_small_eps_asymptotic_error, abs(scaled - asymptotic))
        last_ratio, last_scaled = ratio, scaled
    rows.append((kappa, tstar, last_ratio, last_scaled, asymptotic))

assert max_low_formula_error < 2e-14
assert max_revival_error < 2e-14
assert max_endpoint_increase < 1e-12
assert max_small_eps_asymptotic_error < 1e-8

print('NumPy', np.__version__)
print('PASS')
print('max low-mode closed-form error:', format(max_low_formula_error, '.17g'))
print('max endpoint-spectrum objective increase:', format(max_endpoint_increase, '.17g'))
print('max annihilation/revival identity error:', format(max_revival_error, '.17g'))
print('max eps^2-scaled asymptotic deviation at eps=1e-5:', format(max_small_eps_asymptotic_error, '.17g'))
print('kappa t_star ratio(eps=1e-5) eps^2*ratio asymptotic_constant')
for row in rows:
    print(' '.join(format(v, '.12g') for v in row))
