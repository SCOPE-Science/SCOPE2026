import math
import random


def v_total(delta, mu):
    return sum((d / m) ** 2 for d, m in zip(delta, mu))


def mu_product(delta, mu):
    V = v_total(delta, mu)
    return max(delta) / math.sqrt(V)


def check_case(delta, mu):
    V = v_total(delta, mu)
    L = V / 2.0
    mp = mu_product(delta, mu)
    dm = max(delta)
    assert math.isclose(2.0 * L * mp * mp, dm * dm, rel_tol=1e-12, abs_tol=1e-12)
    for d, m in zip(delta, mu):
        mean = d * d / (2.0 * m * m)
        var = d * d / (m * m)
        log_mgf_minus_one = -mean + var / 2.0
        assert math.isclose(log_mgf_minus_one, 0.0, abs_tol=1e-14)


def frontier(delta, b, bar):
    V0 = v_total(delta, b)
    T = max(delta) ** 2 / (bar * bar)
    Vstar = max(V0, T)
    if V0 >= T:
        mu = list(b)
    else:
        j = 0
        invsq = 1.0 / (b[j] * b[j]) + (T - V0) / (delta[j] * delta[j])
        mu = list(b)
        mu[j] = 1.0 / math.sqrt(invsq)
    V = v_total(delta, mu)
    assert math.isclose(V, Vstar, rel_tol=1e-12, abs_tol=1e-12)
    assert all(m <= cap * (1.0 + 1e-12) for m, cap in zip(mu, b))
    assert mu_product(delta, mu) <= bar * (1.0 + 1e-12)
    return Vstar, mu


# Deterministic examples for both frontier branches.
delta = [0.4, 0.9, 1.3]
mu = [0.7, 1.1, 0.8]
check_case(delta, mu)
frontier(delta, [0.5, 0.6, 0.7], 2.0)  # local caps already dominate
frontier(delta, [2.0, 2.4, 1.8], 0.35)  # aggregate cap requires extra noise

# Fixed-seed randomized positive instances.
rng = random.Random(20261001)
for _ in range(500):
    K = rng.randint(1, 8)
    delta = [10 ** rng.uniform(-1.5, 0.8) for _ in range(K)]
    mu = [10 ** rng.uniform(-1.5, 0.8) for _ in range(K)]
    check_case(delta, mu)
    b = [10 ** rng.uniform(-1.0, 0.8) for _ in range(K)]
    bar = 10 ** rng.uniform(-1.0, 0.8)
    frontier(delta, b, bar)

print("VERIFY_OK")
