"""Independent finite-size checks for the prism average-mixing spectrum.

Requires numpy. The all-order theorem is established analytically in RESULT.md.
"""
import math
import numpy as np


def predicted(n, a, b):
    a %= n
    if b == 0:
        if a == 0:
            return 1.0
        return (1.0 / n if n % 2 else (2.0 / n if a % 2 == 0 else 0.0))
    value = 0.0
    if n % 4 == 0 and a in {n // 4, 3 * n // 4}:
        value += 2.0 / n
    if n % 6 == 0:
        if a in {n // 6, 5 * n // 6}:
            value += 1.0 / n
        if a == n // 2:
            value += 2.0 / n
    return value


def adjacency(n):
    A = np.zeros((2 * n, 2 * n), dtype=float)
    for j in range(n):
        for s in (0, 1):
            u = 2 * j + s
            A[u, 2 * ((j + 1) % n) + s] = 1.0
            A[u, 2 * ((j - 1) % n) + s] = 1.0
            A[u, 2 * j + 1 - s] = 1.0
    assert np.max(abs(A - A.T)) == 0
    return A


def independently_averaged(A):
    values, vectors = np.linalg.eigh(A)
    N = len(values)
    R = np.zeros((N, N), dtype=float)
    left = 0
    while left < N:
        right = left + 1
        while right < N and abs(values[right] - values[left]) < 1e-8:
            right += 1
        Q = vectors[:, left:right]
        E = Q @ Q.T
        R += E * E
        left = right
    return R


def numerical_eigenvalues(R, n):
    labels = np.indices((n, 2))
    j = labels[0].ravel()
    s = labels[1].ravel()
    output = {}
    for a in range(n):
        for b in (0, 1):
            v = np.exp((2j * np.pi * a / n) * j) * np.where(s == 0, 1, (-1) ** b)
            v = v / math.sqrt(2 * n)
            output[a, b] = (np.vdot(v, R @ v)).real
    return output


def equality_pair_counts(n):
    values = [2 * math.cos(2 * math.pi * k / n) for k in range(n)]
    counts = {(a, b): 0 for a in range(n) for b in (0, 1)}
    for k in range(n):
        for l in range(n):
            for s in (0, 1):
                for t in (0, 1):
                    e1 = values[k] + (1 if s == 0 else -1)
                    e2 = values[l] + (1 if t == 0 else -1)
                    if abs(e1 - e2) < 1e-8:
                        counts[(k - l) % n, (s - t) % 2] += 1
    return counts


def main():
    total_eigenmodes = 0
    total_pair_checks = 0
    total_entry_checks = 0
    worst = 0.0
    for n in range(3, 25):
        R = independently_averaged(adjacency(n))
        observed = numerical_eigenvalues(R, n)
        for a in range(n):
            for b in (0, 1):
                v = predicted(n, a, b)
                err = abs(observed[a, b] - v)
                worst = max(worst, err)
                assert err < 2e-9, (n, a, b, observed[a, b], v)
                total_eigenmodes += 1
        desired_rank = n if n % 2 else (n // 2 + 2 * (n % 4 == 0) + 3 * (n % 6 == 0))
        assert int(np.count_nonzero(np.linalg.eigvalsh(R) > 1e-8)) == desired_rank
        assert np.max(np.abs(R.sum(axis=1) - 1)) < 1e-10
        assert np.min(np.linalg.eigvalsh(R)) > -1e-10
        total_entry_checks += R.size
        if n <= 18:
            counts = equality_pair_counts(n)
            for (a, b), count in counts.items():
                assert abs(count / (2 * n) - predicted(n, a, b)) < 1e-10
                total_pair_checks += 1
    assert 11 == 12 // 2 + 2 + 3
    print(f"VERIFY_OK independent_graph_orders=3..24 modes={total_eigenmodes} "
          f"pair_modes={total_pair_checks} matrix_entries={total_entry_checks} "
          f"n12_rank=11/24 max_error={worst:.3g}")


if __name__ == "__main__":
    main()
