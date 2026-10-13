"""Numerical checks for adjacency-weighted wheel trapping formulas.

The analytic theorem is proved in RESULT.md. Float spectral grouping is a check,
not a general finite/infinite proof. Run: python verify.py
"""
import math
import numpy as np


def wheel_h(n, g):
    H = np.zeros((n + 1, n + 1))
    for j in range(n):
        H[j, (j + 1) % n] = 1.0
        H[(j + 1) % n, j] = 1.0
        H[j, n] = g
        H[n, j] = g
    return H


def bright_data(n, g, sinks):
    vals, eigenvectors = np.linalg.eigh(wheel_h(n, g))
    P = np.zeros((n + 1, n + 1))
    i = 0
    while i < n + 1:
        j = i + 1
        while j < n + 1 and abs(vals[j] - vals[i]) < 2e-8:
            j += 1
        V = eigenvectors[:, i:j]
        overlap = V[list(sinks), :]
        _, singular, right = np.linalg.svd(overlap, full_matrices=False)
        rank = int(sum(singular > 1e-8))
        if rank:
            B = V @ right[:rank, :].T
            P += B @ B.T
        i = j
    return float(np.trace(P)), float(1 - P[n, n])


def check_close(actual, expected, label):
    if not abs(actual - expected) < 5e-7:
        raise AssertionError((label, actual, expected))


def run():
    n_generic = n_resonance = 0
    n_two_sinks = n_survival = 0
    for n in range(3, 31):
        R = n // 2 + 2
        for g in (0.19, 0.53, 1.69):
            m, hub_surv = bright_data(n, g, (0,))
            check_close(m, R, ("generic-rank", n, g))
            check_close(hub_surv, 0, ("generic-hub", n, g))
            n_generic += 1
            m2, _ = bright_data(n, g, (0, n))
            check_close(m2, R, ("generic-two-sinks", n, g))
            n_two_sinks += 1
        count = 0
        for k in range(n // 4 + 1, n // 2 + 1):
            lam = 2 * math.cos(2 * math.pi * k / n)
            assert lam < -1e-10
            g = math.sqrt(lam * (lam - 2) / n)
            d = 1 if n % 2 == 0 and k == n // 2 else 2
            expected = d * lam * (lam - 2) / (d * lam * (lam - 2) + (d + 1) * lam * lam)
            m, hub_surv = bright_data(n, g, (0,))
            check_close(m, R - 1, ("resonant-rank", n, k))
            check_close(hub_surv, expected, ("resonant-hub", n, k))
            n_survival += 1
            m2, _ = bright_data(n, g, (0, n))
            check_close(m2, R, ("resonant-two-sinks", n, k))
            n_two_sinks += 1
            n_resonance += 1
            count += 1
        assert count == n // 2 - n // 4
        if n >= 5:
            k = n // 4 + 1
            lam = 2 * math.cos(2 * math.pi * k / n)
            eps = -lam
            assert eps <= 4 * math.pi / n + 1e-10
            g = math.sqrt(lam * (lam - 2) / n)
            _, s = bright_data(n, g, (0,))
            assert s + 1e-9 >= 1 - 3 * math.pi / n
    print(f"VERIFY_OK generic={n_generic} resonances={n_resonance} "
          f"two_sinks={n_two_sinks} hub_resonances={n_survival}")


if __name__ == "__main__":
    run()
