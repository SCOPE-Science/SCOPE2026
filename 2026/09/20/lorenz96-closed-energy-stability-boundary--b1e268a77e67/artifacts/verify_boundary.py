import math
import numpy as np

def G(y):
    return np.roll(y, 1) * (np.roll(y, -1) - np.roll(y, 2))

def A(y):
    return np.roll(y, -1) - np.roll(y, 2)

def s_values(n):
    k = np.arange(n)
    theta = 2.0 * np.pi * k / n
    return np.cos(theta) - np.cos(2.0 * theta)

rng = np.random.default_rng(20260920)
max_energy_residual = 0.0
max_mean_residual = 0.0

for n in range(4, 65):
    for _ in range(20):
        y = rng.normal(size=n)
        gy = G(y)
        ay = A(y)
        max_energy_residual = max(max_energy_residual, abs(float(y @ gy)))
        max_mean_residual = max(max_mean_residual, abs(float(np.sum(gy) + y @ ay)))

    s = s_values(n)
    alpha = float(np.max(s))
    beta = float(np.min(s))
    fp = 1.0 / alpha
    fm = 1.0 / beta
    assert np.min(1.0 - fp * s) > -2e-13
    assert np.min(1.0 - fm * s) > -2e-13
    if n % 2 == 0:
        beta_formula = -2.0
    else:
        beta_formula = -(math.cos(math.pi / n) + math.cos(2.0 * math.pi / n))
    assert abs(beta - beta_formula) < 2e-13
    delta = min(abs(math.cos(2.0 * math.pi * k / n) - 0.25) for k in range(n))
    alpha_formula = 9.0 / 8.0 - 2.0 * delta * delta
    assert abs(alpha - alpha_formula) < 2e-13

print(f"max |y.G(y)|: {max_energy_residual:.3e}")
print(f"max |sum G(y) + y.A(y)|: {max_mean_residual:.3e}")
print("checked N=4,...,64")
print("boundary semidefiniteness: OK")
print("finite-N endpoint formulas: OK")
