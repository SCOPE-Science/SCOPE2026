"""Numerical consistency checks for the exact calibration formulas."""

import math


def alpha_n(N):
    A = 2.0 ** N
    t = 1.0 / A
    disc = (1.0 - t * t) ** 2 + 12.0 * t * (2.0 + t * t)
    return ((1.0 - t * t) + math.sqrt(disc)) / (2.0 * (2.0 + t * t))


def quantities(N):
    A = 2.0 ** N
    a = alpha_n(N)
    p = (1.0 - A ** -2) / 3.0
    lam = (1.0 + a) / a
    r = p * lam
    y = (4.0 / 3.0) * A + (2.0 / 3.0) / A
    gamma = (1.0 + 1.0 / (A * a)) ** -0.5

    one_block = y * y / (A * (A + a))
    input_sq = one_block * (1.0 - r ** A) / (1.0 - r)
    input_sq += 4.0 * r ** A / a * gamma

    characteristic = 1.0 + A / a

    phase_one = []
    for n in range(N + 1):
        x_n = (2.0 ** (N - n) - 2.0 ** (n - N)) / 3.0 + 1.0 / a
        phase_one.append(x_n * (2.0 ** n + a))
    phase_two = [a * (2.0 ** k + 1.0 / a) for k in range(N + 1)]
    state_max = max(phase_one + phase_two)

    return a, r, input_sq, characteristic, state_max


for N in range(2, 18):
    a, r, input_sq, characteristic, state_max = quantities(N)
    assert abs(characteristic - state_max) <= 1e-9 * max(1.0, characteristic)

input_limit = (4.0 / 9.0) * (1.0 - math.exp(-4.0))
critical_lower = math.exp(-2.0) * math.sqrt(
    27.0 / (64.0 * (1.0 - math.exp(-4.0)) * math.log(2.0))
)

print("input_norm_squared_over_2^N limit =", format(input_limit, ".15f"))
print("normalized_critical_lower_bound  =", format(critical_lower, ".15f"))
print()
print(" N    alpha_N        [w]_A2/2^N    ||f||^2/2^N    r_N^(2^N)")
for N in (6, 10, 14, 17):
    a, r, input_sq, characteristic, _ = quantities(N)
    A = 2.0 ** N
    print(
        f"{N:2d}  {a:.10f}    {characteristic/A:.10f}"
        f"      {input_sq/A:.10f}      {r**A:.10f}"
    )
