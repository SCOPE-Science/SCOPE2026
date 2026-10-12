from __future__ import annotations
import math


def rate(x: float) -> float:
    if not x > 2.0:
        raise ValueError("x must exceed 2")
    if x <= 3.0:
        return (x - 1.0) * math.log(2.0 * (x - 1.0) / x) + math.log(2.0 / x)
    return x * math.log(4.0 / 3.0) - math.log(2.0)


def tail_probability(n: int, x: float) -> float:
    # Dynamic program for P(sum_{r=1}^n G_r > floor(x n)).
    # The array stores probabilities strictly below or at the cutoff.
    cutoff = math.floor(x * n)
    pmf = [0.0] * (cutoff + 1)
    pmf[0] = 1.0
    for r in range(1, n + 1):
        p = (1.0 - 2.0 ** (-r)) / 2.0
        q = 1.0 - p
        nxt = [0.0] * (cutoff + 1)
        # Convolution with a geometric distribution on {1,2,...} via recurrence.
        for t in range(1, cutoff + 1):
            nxt[t] = q * nxt[t - 1] + p * pmf[t - 1]
        pmf = nxt
    inside = math.fsum(pmf)
    return max(0.0, 1.0 - inside)


a = math.log(4.0 / 3.0)
i3_left = 2.0 * math.log(4.0 / 3.0) + math.log(2.0 / 3.0)
i3_right = 3.0 * a - math.log(2.0)
assert abs(i3_left - i3_right) < 1e-14
assert abs(math.log(2.0 * (3.0 - 1.0) / 3.0) - a) < 1e-14

for x in (2.1, 2.5, 3.0, 3.5, 4.0):
    assert rate(x) > 0.0

# Finite-n convergence checks. The tolerances are deliberately loose because
# these calculations corroborate an analytic large-deviation proof.
checks = [
    (50, 2.5, 0.03),
    (50, 3.0, 0.02),
    (50, 3.5, 0.02),
    (100, 2.5, 0.02),
    (100, 3.0, 0.015),
]
for n, x, tol in checks:
    tail = tail_probability(n, x)
    assert tail > 0.0
    empirical = -math.log(tail) / n
    assert abs(empirical - rate(x)) < tol, (n, x, empirical, rate(x))

print("VERIFY_OK")
