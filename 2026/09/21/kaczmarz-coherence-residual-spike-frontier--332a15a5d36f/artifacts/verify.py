import math
import platform
import numpy as np

SEED = 20260921
rng = np.random.default_rng(SEED)


def gamma_exact(m, mu):
    d = m - 1
    if mu <= 1.0 / d:
        return math.sqrt(d * (1.0 + mu) ** 2 / m)
    return math.sqrt(1.0 + d * mu * mu)


def gamma_theta(m, mu, theta):
    d = m - 1
    T = 1.0 / theta
    if mu <= theta / d:
        return math.sqrt(d * (T + mu) ** 2 / (1.0 + d * T * T))
    return math.sqrt(1.0 + d * mu * mu)


def sharp_matrix(m, mu):
    A = np.zeros((m, m), dtype=float)
    A[0, 0] = 1.0
    s = math.sqrt(1.0 - mu * mu)
    for j in range(1, m):
        A[j, 0] = -mu
        A[j, j] = s
    return A


def residual_step(A, r, i):
    G = A @ A.T
    return r - r[i] * G[:, i]


max_equality_error = 0.0
for m in (2, 3, 5, 9):
    d = m - 1
    for mu in (0.0, 0.05, 0.2, 0.4, 0.8):
        if mu >= 1.0:
            continue
        A = sharp_matrix(m, mu)
        off = A @ A.T - np.eye(m)
        coherence = np.max(np.abs(off))
        assert abs(coherence - mu) < 5e-15
        t = 1.0 if mu <= 1.0 / d else 1.0 / (d * mu)
        r = np.array([1.0] + [t] * d)
        rp = residual_step(A, r, 0)
        ratio = np.linalg.norm(rp) / np.linalg.norm(r)
        max_equality_error = max(max_equality_error, abs(ratio - gamma_exact(m, mu)))

max_random_ratio_to_bound = 0.0
random_cases = 0
for m in (2, 3, 5, 8):
    for n in (m, m + 3):
        for _ in range(750):
            A = rng.normal(size=(m, n))
            A /= np.linalg.norm(A, axis=1, keepdims=True)
            G = A @ A.T
            mu = np.max(np.abs(G - np.eye(m)))
            r = rng.normal(size=m)
            i = int(np.argmax(np.abs(r)))
            rp = r - r[i] * G[:, i]
            ratio = np.linalg.norm(rp) / np.linalg.norm(r)
            bound = gamma_exact(m, mu)
            assert ratio <= bound + 2e-12
            max_random_ratio_to_bound = max(max_random_ratio_to_bound, ratio / bound)
            random_cases += 1

max_theta_error = 0.0
for m in (3, 5, 9):
    d = m - 1
    for theta in (0.4, 0.7, 1.0):
        T = 1.0 / theta
        for mu in (0.02, 0.08, 0.2, 0.5):
            A = sharp_matrix(m, mu)
            t = T if mu <= theta / d else 1.0 / (d * mu)
            r = np.array([1.0] + [t] * d)
            assert abs(r[0]) + 1e-14 >= theta * np.max(np.abs(r))
            rp = residual_step(A, r, 0)
            ratio = np.linalg.norm(rp) / np.linalg.norm(r)
            max_theta_error = max(max_theta_error, abs(ratio - gamma_theta(m, mu, theta)))

threshold_checks = []
for m in (2, 3, 5, 10, 50):
    mu_star = math.sqrt(m / (m - 1.0)) - 1.0
    below = gamma_exact(m, mu_star * (1 - 1e-8))
    above = gamma_exact(m, mu_star * (1 + 1e-8))
    assert below < 1.0 + 1e-12
    assert above > 1.0 - 1e-12
    threshold_checks.append((m, mu_star, below, above))

print('python=' + platform.python_version())
print('numpy=' + np.__version__)
print('seed=' + str(SEED))
print('sharp_equality_max_abs_error=%.3e' % max_equality_error)
print('random_cases=%d' % random_cases)
print('max_random_ratio_to_bound=%.12f' % max_random_ratio_to_bound)
print('approximate_rule_equality_max_abs_error=%.3e' % max_theta_error)
for m, mu_star, below, above in threshold_checks:
    print('m=%d mu_star=%.15g gamma_below=%.12f gamma_above=%.12f' % (m, mu_star, below, above))
print('status=PASS')
