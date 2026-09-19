#!/usr/bin/env python3
"""Numerical checks for the shifted cyclic obstruction asymptotics."""

import math

EULER_GAMMA = 0.577215664901532860606512090082402431
C_STAR = 8.0 * math.exp(EULER_GAMMA - 1.0) / math.pi
K_FACTOR = math.pi * math.exp(1.0 - EULER_GAMMA) / 8.0


def half_shift_weight(k):
    assert k >= 2 and k % 2 == 0
    return sum(1.0 / math.sin(math.pi * (j + 0.5) / k)
               for j in range(k)) / k


def half_shift_max_weight(k):
    return 1.0 / (2.0 * k * math.sin(math.pi / (2.0 * k)))


def certificate(H, k):
    W = half_shift_weight(k)
    M = half_shift_max_weight(k)
    if W <= H:
        return 0.0
    return min(1.0 / k, (W - H) / (2.0 * k * (H + 1.0) * M))


def predicted_k(H):
    k = int(round(K_FACTOR * math.exp(math.pi * H / 2.0)))
    if k % 2:
        k += 1
    return max(2, k)


def best_near_prediction(H, radius=80):
    k0 = predicted_k(H)
    candidates = []
    for dk in range(-2 * radius, 2 * radius + 1, 2):
        k = k0 + dk
        if k >= 2 and k % 2 == 0:
            candidates.append((certificate(H, k), k))
    return max(candidates)


def shifted_weight(k, a):
    assert 0.0 < a < 1.0
    s = 1.0 / math.sin(math.pi * a / k)
    for r in range(1, k):
        s += 1.0 / math.sin(math.pi * (r - a) / k)
    return math.sin(math.pi * a) * s / k


def phase_constants(a):
    A = 2.0 * math.sin(math.pi * a) / math.pi
    lam = 1.0 / A
    return A, lam


print("C_star =", format(C_STAR, ".15f"))
print("K_factor =", format(K_FACTOR, ".15f"))
print()
print("H  k_near  H*exp(pi H/2)*E  ratio_to_C_star")
for H in (3, 4, 5, 6, 7):
    E, k = best_near_prediction(float(H))
    scaled = H * math.exp(math.pi * H / 2.0) * E
    print(H, k, format(scaled, ".12f"), format(scaled / C_STAR, ".12f"))

print()
print("half-shift weight asymptotic:")
c0 = EULER_GAMMA + math.log(8.0 / math.pi)
for k in (100, 1000, 10000):
    W = half_shift_weight(k)
    residual = W - (2.0 / math.pi) * math.log(k)
    print(k, format(residual, ".12f"),
          "target", format((2.0 / math.pi) * c0, ".12f"))

print()
print("fixed-phase logarithmic slopes:")
for a in (0.30, 0.40, 0.50):
    A, lam = phase_constants(a)
    k1, k2 = 1000, 10000
    slope = (shifted_weight(k2, a) - shifted_weight(k1, a)) / math.log(k2 / k1)
    print(format(a, ".2f"),
          "A_est", format(slope, ".9f"),
          "A", format(A, ".9f"),
          "lambda", format(lam, ".9f"))
