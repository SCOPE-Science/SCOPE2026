#!/usr/bin/env python3
"""Independent finite checks of the binary-cube two-particle collision-rank theorem."""
from math import comb, gcd
import numpy as np
from scipy.linalg import eigh


def claimed(d, a, b):
    if a == b:
        return 2 ** (d - 1) * (d + 2)
    generic = 2 ** (d - 2) * (d * d + 3 * d + 4)
    p, q = a + b, abs(a - b)
    z = gcd(p, q)
    p, q = p // z, q // z
    return int(round(generic)) - sum(
        comb(d, t) * max(0, d - t - q + 1) * max(0, t - p + 1)
        for t in range(d + 1)
    )


def independent_spectral_rank(d, a, b):
    n = 1 << d
    adjacency = np.zeros((n, n))
    for x in range(n):
        for j in range(d):
            adjacency[x, x ^ (1 << j)] = 1
    h = a * np.kron(adjacency, np.eye(n)) + b * np.kron(np.eye(n), adjacency)
    detection = np.zeros((n * n, n))
    for x in range(n):
        detection[x * n + x, x] = 1
    energies, states = eigh(h)
    answer = 0
    # Exact integer energies for positive integer rates; grouping tolerance
    # is safely below the minimum gap of 2.
    for energy in sorted(set(np.rint(energies).astype(int))):
        ix = np.where(abs(energies - energy) < 1e-7)[0]
        answer += int(np.linalg.matrix_rank(states[:, ix].T @ detection, tol=1e-8))
    return answer


def direct_sector_count(d, a, b):
    count = 0
    for mask in range(1 << d):
        energies = set()
        for k in range(1 << d):
            r = k.bit_count()
            s = (k ^ mask).bit_count()
            energies.add(a * (d - 2 * r) + b * (d - 2 * s))
        count += len(energies)
    return count


def main():
    cases = 0
    for d in range(1, 4):
        for a, b in [(1, 1), (1, 2), (1, 3), (2, 3), (3, 5)]:
            x, y = claimed(d, a, b), independent_spectral_rank(d, a, b)
            assert x == y, (d, a, b, x, y)
            cases += 1
    sector_cases = 0
    for d in range(2, 10):
        for a, b in [(1, 1), (1, 2), (1, 3), (2, 3), (3, 5), (2, 5)]:
            assert claimed(d, a, b) == direct_sector_count(d, a, b)
            sector_cases += 1
    for p, q in [(2, 1), (3, 1), (3, 2), (4, 1), (5, 2)]:
        a, b = p + q, p - q
        d = p + q
        generic = int(round(2 ** (d - 2) * (d * d + 3 * d + 4)))
        assert generic - claimed(d, a, b) == comb(d, p)
    print(f"VERIFY_OK independent_dense_spectra={cases} exact_sector_cases={sector_cases} onset_pairs=5")


if __name__ == "__main__":
    main()
