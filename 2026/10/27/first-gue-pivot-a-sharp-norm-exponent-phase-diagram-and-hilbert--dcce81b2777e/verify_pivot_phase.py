"""Deterministic numerical checks for the GUE first-pivot norm phase diagram."""
import math
import numpy as np
from scipy.special import roots_legendre, gamma
from scipy.integrate import simpson

ANGLE_NODES = 400
THETA, ANGLE_WEIGHTS = roots_legendre(ANGLE_NODES)
THETA = (THETA + 1) * (math.pi / 4)
ANGLE_WEIGHTS = ANGLE_WEIGHTS / 2
COS, SIN = np.cos(THETA), np.sin(THETA)
TGRID = np.linspace(0, 9, 11000)
DIAGONAL_DENSITY = math.sqrt(2 / math.pi) * np.exp(-TGRID**2 / 2)
NUM_CHECKS = 0


def check(condition, label):
    global NUM_CHECKS
    NUM_CHECKS += 1
    if not condition:
        raise AssertionError(label)


def angular_amplitudes(p):
    if math.isinf(p):
        return np.maximum(COS, SIN)
    return (COS**p + SIN**p)**(1 / p)


def first_pivot_probability(n, p):
    a = angular_amplitudes(p)
    surv = np.exp(-((TGRID[:, None] / a[None, :]) ** 2)) @ ANGLE_WEIGHTS
    cdf = np.maximum(0, 1 - surv)
    return float(simpson(DIAGONAL_DENSITY * cdf**(n - 1), x=TGRID))


def asymptotic(n, p):
    if p < 2:
        lam = 2 ** (1 - 2 / p)
        alp = 1 / (2 * lam)
        k = (gamma(alp) / math.sqrt(2 * math.pi * lam)) * (
            math.sqrt(math.pi * (2 - p)) / 2
        ) ** alp
        return k * n**(-alp) * math.log(n) ** ((alp - 1) / 2)
    if p == 2:
        return (2 * n * math.log(n)) ** (-0.5)
    return math.pi ** 0.25 / 2 * n**(-0.5) * math.log(n) ** (-0.25)


def m_profile(beta):
    c2 = COS * COS
    s2 = SIN * SIN
    entropy = -c2 * np.log(c2) - s2 * np.log(s2)
    return float(ANGLE_WEIGHTS @ np.exp(-beta * entropy / 2))


# Angular coordinates have normalized uniform measure on a quadrant.
check(abs(float(ANGLE_WEIGHTS.sum()) - 1) < 1e-14, "angle quadrature")
check(np.max(abs(angular_amplitudes(2) - 1)) < 1e-14, "Euclidean angular norm")
for n in [2, 3, 10, 100, 1000]:
    got = first_pivot_probability(n, 1)
    exact = 1 / (2 * n - 1)
    check(abs(got / exact - 1) < 0.0002, f"exact l1 pivot n={n}: {got}")
    print(f"l1 n={n}: quadrature={got:.12g}; known_exact={exact:.12g}")

for n in [2, 3, 5, 10]:
    exact = sum(
        (-1) ** j * math.comb(n - 1, j) / math.sqrt(1 + 2 * j)
        for j in range(n)
    )
    got = first_pivot_probability(n, 2)
    check(abs(got - exact) < 1e-8, f"exact l2 pivot n={n}")

for p in [1.5, 4.0, math.inf]:
    a = angular_amplitudes(p)
    lam = 2 ** (1 - 2 / p) if p < 2 else 1.0
    tail_const = (
        2 / math.sqrt(math.pi * lam * (2 - p))
        if p < 2 else 2 / math.sqrt(math.pi)
    )
    for t in [5.0, 8.0]:
        actual = float(ANGLE_WEIGHTS @ np.exp(-(t / a) ** 2))
        predicted = tail_const * math.exp(-lam * t * t) / t
        tolerance = 0.05 if (p == 4 or math.isinf(p) or p == 1.5) else 0.1
        check(abs(actual / predicted - 1) < tolerance, f"angular tail p={p}, t={t}")
        print(f"angular-tail p={p}, t={t}: ratio={actual / predicted:.9f}")

for p in [1.5, 3.0, 4.0, math.inf]:
    n = 10_000_000
    actual = first_pivot_probability(n, p)
    predicted = asymptotic(n, p)
    check(0.83 < actual / predicted < 1.1, f"fixed-p scaling p={p}")
    print(f"fixed p={p}, n={n}: ratio={actual / predicted:.9f}")

check(abs(m_profile(0) - 1) < 1e-14, "critical profile at zero")
check(m_profile(-1) > 1 > m_profile(1) > 0, "critical profile monotonicity")
for beta in [-1.0, 0.0, 1.0]:
    n = 10_000_000
    p = 2 + beta / math.log(n)
    exact_integral = m_profile(beta)
    predicted = (2 * n * math.log(n) * exact_integral) ** (-0.5)
    actual = first_pivot_probability(n, p)
    check(0.88 < actual / predicted < 1.1, f"critical window beta={beta}")
    print(f"window beta={beta}, n={n}: M={exact_integral:.9f}; ratio={actual / predicted:.9f}")

for p in [1, 1.2, 1.5, 1.99, 2, 2.01, 3, math.inf]:
    predicted = asymptotic(100000, p)
    check(math.isfinite(predicted) and predicted > 0, f"asymptotic positivity p={p}")

print(f"ALL {NUM_CHECKS} deterministic assertions passed")
