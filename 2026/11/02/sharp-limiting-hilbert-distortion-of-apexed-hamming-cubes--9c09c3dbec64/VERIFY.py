"""Exact finite checks for the apexed Hamming-cube distortion theorem.

This script checks instances of identities proved analytically in RESULT.md.
It does not replace the proof for all dimensions or all Hilbert embeddings.
Python 3 standard library only.
"""
from fractions import Fraction as F
from math import comb


def normalized_krawtchouk(d, j, k):
    numerator = sum(
        (-1) ** r * comb(k, r) * comb(d - k, j - r)
        for r in range(max(0, j - d + k), min(k, j) + 1)
    )
    return F(numerator, comb(d, j))


def check():
    assertions = 0
    for d in range(2, 41):
        t = F(8, 3)
        # The tensor embedding: hub/leaf squared norm and every distance orbit.
        hub_sq = t
        assert 1 <= hub_sq <= t
        assertions += 2
        for k in range(1, d + 1):
            edge_sq = F(16, 3) * (1 - F(1, 2 ** k))
            graph_sq = 1 if k == 1 else 4
            assert edge_sq >= graph_sq
            assert edge_sq <= t * graph_sq
            assertions += 2
        # Sharp lower-bound algebra and every Fourier basis's weight-one/two energy.
        lower = F(8 * (d - 1), 3 * d)
        assert lower <= t
        assert F(3 * d, 2 * (d - 1)) * lower == 4
        assertions += 2
        for j in range(1, d + 1):
            q1 = normalized_krawtchouk(d, j, 1)
            q2 = normalized_krawtchouk(d, j, 2)
            assert 2 * (1 - q1) == F(4 * j, d)
            assert 2 * (1 - q2) == F(8 * j * (d - j), d * (d - 1))
            assertions += 2
    # For rational weights verify Parseval's two-shell energy identity and its
    # Cauchy-Schwarz upper envelope, without assuming concentration in one mode.
    for d in range(2, 15):
        for seed in range(1, 24):
            ws = [F((seed * (j + 3) + 5 * j * j) % 13 + 1, 97)
                  for j in range(d + 1)]
            R = sum(ws)
            U = sum(j * ws[j] for j in range(d + 1))
            V = sum(j * j * ws[j] for j in range(d + 1))
            lhs = F(8, d * (d - 1)) * (d * U - V)
            rhs = sum(ws[j] * 2 * (1 - normalized_krawtchouk(d, j, 2))
                      for j in range(d + 1))
            assert lhs == rhs
            assert V * R >= U * U
            assertions += 2
    print('CHECK_OK exact_rational_assertions=', assertions,
          'dimensions_tensor=2..40 dimensions_fourier=2..40')


if __name__ == '__main__':
    check()
