import math
import random


def momo_direct(a, beta, x1, alpha, n):
    fbar = 0.5 * a * x1 * x1
    d = a * x1
    gamma = d * x1
    x = x1
    rows = []
    for k in range(1, n + 1):
        f = 0.5 * a * x * x
        g = a * x
        fbar = (1 - beta) * f + beta * fbar
        gamma = (1 - beta) * g * x + beta * gamma
        d = (1 - beta) * g + beta * d
        h = fbar + d * x - gamma
        proposal = max(h, 0.0) / (d * d)
        tau = min(alpha, proposal)
        xn = x - tau * d
        rows.append((k, x, xn, d, h, tau, proposal))
        x = xn
    return rows


def z_reduced(beta, x1, n):
    if beta == 0.0:
        return [0.5**k * x1 for k in range(n + 1)]
    xs = [x1, 0.5 * x1]
    z = 2 * beta / (1 - beta)
    while len(xs) < n + 1:
        q = (z + 0.5) / (z + 1.0)
        xs.append(xs[-1] * q)
        z = beta * (1 + z) * (1 + z) / (z + 0.5)
    return xs


rng = random.Random(350065)

# Direct source iteration agrees with the reduced recurrence over a bounded
# horizon where ordinary floating point remains a faithful transcription guard.
for _ in range(200):
    a = 10 ** rng.uniform(-1.0, 1.0)
    beta = rng.uniform(0.0, 0.98)
    x1 = rng.choice((-1.0, 1.0)) * 10 ** rng.uniform(-1.0, 1.0)
    alpha = 1.0 / (2 * a) * rng.uniform(1.0, 5.0)
    rows = momo_direct(a, beta, x1, alpha, 50)
    xs = z_reduced(beta, x1, 50)
    for j, row in enumerate(rows):
        _, x, xn, d, h, tau, proposal = row
        assert abs(x - xs[j]) < 2e-10 * max(1.0, abs(x))
        assert abs(xn - xs[j + 1]) < 2e-10 * max(1.0, abs(xn))
        assert proposal <= alpha * (1 + 2e-10)
        assert x * xn > 0.0
        assert abs(xn) < abs(x)

# Zero momentum is exact halving.
for a in (0.2, 1.0, 7.0):
    rows = momo_direct(a, 0.0, 3.0, 1.0 / (2 * a), 20)
    for k, x, xn, *_ in rows:
        assert abs(xn - 0.5 * x) < 1e-14 * max(1.0, abs(x))

# The exact reduced state converges to the claimed fixed point.
for beta in (0.01, 0.1, 0.5, 0.9, 0.99):
    q_target = (1 + math.sqrt(1 + 8 * beta)) / 4
    z = 2 * beta / (1 - beta)
    for _ in range(6000):
        z = beta * (1 + z) * (1 + z) / (z + 0.5)
    q_observed = (z + 0.5) / (z + 1.0)
    at_observed = 1.0 / (2 * (1 - beta) * (1 + z) ** 2)
    at_target = 2 * (1 - q_target) / (2 * q_target + 1)
    assert abs(q_observed - q_target) < 2e-12
    assert abs(at_observed - at_target) < 2e-12

# Default source momentum constants.
beta = 0.9
q = (1 + math.sqrt(1 + 8 * beta)) / 4
assert abs(q - 0.9658910531638176) < 5e-16
assert abs(q * q - 0.9329455265819088) < 5e-16
target_at = 2 * (1 - q) / (2 * q + 1)
assert abs(target_at - 0.02326840508547029) < 5e-16

# The factor worsens strictly with beta.
grid = [i / 1000 for i in range(1000)]
qs = [(1 + math.sqrt(1 + 8 * b)) / 4 for b in grid]
assert all(qs[i + 1] > qs[i] for i in range(len(qs) - 1))

print("verification passed")
