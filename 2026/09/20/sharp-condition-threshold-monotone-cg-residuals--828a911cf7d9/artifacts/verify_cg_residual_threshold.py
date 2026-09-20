#!/usr/bin/env python3
import math
import numpy as np

TOL = 5e-11

def endpoint_ratio(kappa):
    mu = 1.0
    L = float(kappa)
    A = np.diag([mu, L])
    r = np.array([math.sqrt(L), math.sqrt(mu)], dtype=float)
    alpha = float(r @ r) / float(r @ A @ r)
    r1 = r - alpha * (A @ r)
    return np.linalg.norm(r1) / np.linalg.norm(r)

def cg_checks(A, r0):
    eigs = np.linalg.eigvalsh(A)
    mu = float(eigs[0])
    L = float(eigs[-1])
    kappa = L / mu
    K2 = (L + mu) ** 2 / (4.0 * L * mu)
    global_sq = K2 - 1.0

    r = r0.astype(float).copy()
    p = r.copy()
    rr = float(r @ r)
    d = 1.0
    max_global_excess = -float("inf")
    max_history_excess = -float("inf")
    steps = 0

    for _ in range(A.shape[0]):
        if rr <= 1e-26 * float(r0 @ r0):
            break
        Ap = A @ p
        pap = float(p @ Ap)
        alpha = rr / pap
        r_new = r - alpha * Ap
        rr_new = float(r_new @ r_new)
        ratio_sq = rr_new / rr

        max_global_excess = max(max_global_excess, ratio_sq - global_sq)
        history_rhs = K2 / d - 1.0
        max_history_excess = max(max_history_excess, ratio_sq - history_rhs)
        if ratio_sq > global_sq + TOL:
            raise AssertionError("global factor bound failed")
        if ratio_sq > history_rhs + TOL:
            raise AssertionError("history-aware bound failed")

        steps += 1
        if rr_new <= 1e-26 * float(r0 @ r0):
            break

        beta = rr_new / rr
        p_new = r_new + beta * p
        d_new_direct = float(p_new @ p_new) / rr_new
        d_new_recur = 1.0 + beta * d
        if abs(d_new_direct - d_new_recur) > 2e-10 * max(1.0, d_new_direct):
            raise AssertionError("direction-history recurrence failed")

        r, p, rr, d = r_new, p_new, rr_new, d_new_direct

    return steps, max_global_excess, max_history_excess

def main():
    threshold = 3.0 + 2.0 * math.sqrt(2.0)
    print("threshold =", format(threshold, ".15g"))
    for kappa in [2.0, threshold, 6.0, 10.0, 100.0]:
        measured = endpoint_ratio(kappa)
        predicted = (kappa - 1.0) / (2.0 * math.sqrt(kappa))
        print(
            "endpoint",
            "kappa=" + format(kappa, ".15g"),
            "measured=" + format(measured, ".15g"),
            "predicted=" + format(predicted, ".15g"),
            "difference=" + format(measured - predicted, ".3e"),
        )
        if abs(measured - predicted) > TOL:
            raise AssertionError("endpoint sharpness check failed")

    rng = np.random.default_rng(271828)
    worst_global = -float("inf")
    worst_history = -float("inf")
    checked_steps = 0
    for _ in range(300):
        n = int(rng.integers(3, 15))
        log_kappa = float(rng.uniform(math.log(1.05), math.log(1000.0)))
        kappa = math.exp(log_kappa)
        Q, _ = np.linalg.qr(rng.normal(size=(n, n)))
        interior = np.exp(rng.uniform(0.0, math.log(kappa), size=max(0, n - 2)))
        eigs = np.concatenate(([1.0], interior, [kappa]))
        rng.shuffle(eigs)
        A = Q @ np.diag(eigs) @ Q.T
        r0 = rng.normal(size=n)
        steps, global_excess, history_excess = cg_checks(A, r0)
        checked_steps += steps
        worst_global = max(worst_global, global_excess)
        worst_history = max(worst_history, history_excess)

    print("random_spd_cases = 300")
    print("checked_cg_steps =", checked_steps)
    print("max_global_bound_excess =", format(worst_global, ".3e"))
    print("max_history_bound_excess =", format(worst_history, ".3e"))
    print("all checks passed")

if __name__ == "__main__":
    main()
