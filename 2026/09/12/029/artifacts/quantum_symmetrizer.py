"""Quantum symmetrizer ranks for V (dim 4) with c = -flip.
S2 = id + c on V^2: rank 6 = C(4,2). S3 = sum_{w in S3} sgn(w) P_w: rank 4 = C(4,3).
Confirms braided exterior Hilbert slices in degrees 2,3.
"""
import itertools
import json

import numpy as np


def main():
    n = 4
    nn = n * n
    swap = np.zeros((nn, nn), dtype=int)
    for i in range(n):
        for j in range(n):
            swap[i * n + j, j * n + i] = 1
    s2 = np.eye(nn, dtype=int) - swap
    r2 = int(np.linalg.matrix_rank(s2))
    d = n**3
    s3 = np.zeros((d, d), dtype=int)
    for w in itertools.permutations(range(3)):
        m = np.zeros((d, d), dtype=int)
        for a in range(n):
            for b in range(n):
                for c in range(n):
                    src = (a, b, c)
                    dst = (src[w[0]], src[w[1]], src[w[2]])
                    m[dst[0] * n * n + dst[1] * n + dst[2],
                      src[0] * n * n + src[1] * n + src[2]] = 1
        inv = sum(1 for i in range(3) for j in range(i + 1, 3) if w[i] > w[j])
        s3 = s3 + ((-1) ** inv) * m
    r3 = int(np.linalg.matrix_rank(s3))
    assert r2 == 6, r2
    assert r3 == 4, r3
    with open("output/artifacts/quantum_symmetrizer_log.json", "w") as f:
        json.dump({"rank_S2": r2, "expect_S2": 6, "rank_S3": r3,
                   "expect_S3": 4}, f, indent=2)
    print("OK: S2 rank 6, S3 rank 4")


if __name__ == "__main__":
    main()
