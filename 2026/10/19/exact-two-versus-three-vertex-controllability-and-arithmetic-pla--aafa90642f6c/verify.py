"""Independent finite checks for actuator selection on uniformly weighted wheel graphs.

Run: python verify.py
Dependencies: numpy, sympy. Finite testing does not prove the all-size theorem.
"""
from itertools import combinations
from math import cos, pi, gcd
import numpy as np
import sympy as sp

checks = 0


def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def wheel_float(m, a, b=1.0):
    L = np.zeros((m + 1, m + 1))
    for i in range(m):
        for j, w in (((i + 1) % m, a), (m, b)):
            L[i, i] += w
            L[j, j] += w
            L[i, j] -= w
            L[j, i] -= w
    return L


def good_numpy(L, S):
    vals, U = np.linalg.eigh(L)
    groups = []
    for i, val in enumerate(vals):
        if not groups or abs(val - vals[groups[-1][-1]]) > 1e-7:
            groups.append([i])
        else:
            groups[-1].append(i)
    return all(np.linalg.matrix_rank(U[np.ix_(S, inds)], tol=1e-8) == len(inds)
               for inds in groups)


def regime(m, ratio):
    resonances = [j for j in range(1, m // 2 + 1)
                  if abs(ratio * (2 - 2 * cos(2 * pi * j / m)) - m) < 1e-7]
    three = bool(resonances and 2 * resonances[0] < m)
    antipodal = bool(resonances and 2 * resonances[0] == m)
    return three, antipodal


# Eigenvalues and eigenvectors are independently recovered from the assembled matrix.
# Enumerate every two-vertex choice, including choices using the hub.
for m in range(4, 19):
    ratios = [0.63, 1.19, 2.71]
    ratios += [m / (2 - 2 * cos(2 * pi * j / m)) for j in range(1, m // 2 + 1)]
    for a in ratios:
        L = wheel_float(m, a)
        three, antipodal = regime(m, a)
        winners = 0
        for i, j in combinations(range(m + 1), 2):
            observed = good_numpy(L, [i, j])
            t = j - i
            predicted = (i < m and j < m and not three and
                         gcd(t, m if m % 2 else m // 2) == 1 and
                         (not antipodal or t % 2 == 1))
            check(observed == predicted, f"pair mismatch m={m}, a={a}, pair={i,j}")
            winners += observed
        from sympy import totient
        predicted_count = 0 if three else (m * int(totient(m)) // 2 if m % 2 or antipodal
                                            else m * int(totient(m // 2)))
        check(winners == predicted_count, f"pair count mismatch m={m}, a={a}")
        S = [m, 0, 1] if three else [0, 1]
        check(good_numpy(L, S), f"explicit actuator placement fails m={m}, a={a}")


# Exact arithmetic: independent Kalman-matrix ranks for rational spoke/rim ratios.
def wheel_exact(m, a):
    L = sp.zeros(m + 1)
    for i in range(m):
        for j, w in (((i + 1) % m, a), (m, sp.Integer(1))):
            L[i, i] += w
            L[j, j] += w
            L[i, j] -= w
            L[j, i] -= w
    return L


def kalman_rank(L, S):
    B = sp.eye(L.rows)[:, list(S)]
    blocks = [B]
    for _ in range(L.rows - 1):
        blocks.append(L * blocks[-1])
    return sp.Matrix.hstack(*blocks).rank()


for m, a in [(4, sp.Integer(2)), (4, sp.Integer(1)),
             (6, sp.Integer(2)), (6, sp.Integer(6)), (6, sp.Integer(1)),
             (8, sp.Integer(2)), (8, sp.Integer(4)), (8, sp.Rational(1, 2))]:
    L = wheel_exact(m, a)
    for S in combinations(range(m + 1), 2):
        predicted = good_numpy(np.array(L, dtype=float), list(S))
        check((kalman_rank(L, S) == m + 1) == predicted,
              f"exact Kalman disagreement m={m}, a={a}, S={S}")


# Every triple on a prime wheel is controllable at any non-antipodal resonance.
for m in (5, 7, 11):
    for k in range(1, (m + 1) // 2):
        a = m / (2 - 2 * cos(2 * pi * k / m))
        L = wheel_float(m, a)
        for S in combinations(range(m + 1), 3):
            check(good_numpy(L, list(S)), f"prime triple fails m={m}, k={k}, S={S}")

# A noncoprime pair can work at nonresonant even order.
check(good_numpy(wheel_float(6, 0.63), [0, 2]), "noncoprime pair witness")
check(not good_numpy(wheel_float(6, 1.5), [0, 2]), "antipodal resonance failure")

print(f"VERIFY_OK {checks} checks")
