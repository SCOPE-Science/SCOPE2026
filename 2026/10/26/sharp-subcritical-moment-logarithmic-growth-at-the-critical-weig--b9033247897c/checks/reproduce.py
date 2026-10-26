"""Finite-horizon diagnostics for a critical backward shift; not an asymptotic proof."""
from math import log


def sample(p, q, N):
    if not (p >= 1 and 0 < q < p and N >= 2):
        raise ValueError("Require p >= 1, 0 < q < p, N >= 2")
    r = q / p
    exponent = r / (1 - r)
    raw = [(j / N) ** exponent for j in range(1, N + 1)]
    total = sum(raw)
    mass = [v / total for v in raw]
    assert abs(sum(mass) - 1) < 1e-12
    # F_k = sum_{i>k} (i/(i-k)) mass_i, using one-based i.
    moment = sum(
        (sum(i / (i - k) * mass[i - 1] for i in range(k + 1, N + 1))) ** r
        for k in range(N)
    ) / N
    observed = moment ** (1 / q) / log(N) ** (1 / p)
    predicted = (1 - r) ** ((1 - r) / q)
    return observed, predicted


if __name__ == "__main__":
    for p, q in [(2, 1), (3, 1), (1, 0.5)]:
        for N in [40, 100, 240]:
            measured, theory = sample(p, q, N)
            print(f"p={p}, q={q}, N={N}: witness/log^(1/p)={measured:.8f}; limiting constant={theory:.8f}")
