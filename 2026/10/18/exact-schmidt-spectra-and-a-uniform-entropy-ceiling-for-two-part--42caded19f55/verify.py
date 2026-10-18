#!/usr/bin/env python3
"""Independent arc-by-arc checks of the complete-bipartite Grover entropy law.

Requires Python 3 and NumPy. Runs the full tensor-arc evolution, rather than
building the reduced Kronecker formula. The tests are finite checks; the
all-size theorem is proved algebraically in RESULT.md.
"""
import math
import numpy as np


def exact_entropy(m, n, time):
    q = m * n
    determinant = 4 * (m - 1) * (n - 1) / (q * q)
    mu_minus = (1 - math.sqrt(max(0., 1 - 4 * determinant))) / 2
    if mu_minus <= 0:
        binary = 0.
    else:
        binary = -(mu_minus * math.log(mu_minus)
                   + (1 - mu_minus) * math.log1p(-mu_minus))
    return math.log(2) + (0, 1, 2, 1)[time % 4] * binary


def exact_spectrum(m, n, time):
    q = m * n
    determinant = 4 * (m - 1) * (n - 1) / (q * q)
    mu_minus = (1 - math.sqrt(max(0., 1 - 4 * determinant))) / 2
    mu = [1 - mu_minus, mu_minus]
    if time % 4 == 0:
        raw = [.5, .5]
    elif time % 4 in (1, 3):
        raw = [v / 2 for v in mu for _ in range(2)]
    else:
        raw = [u * v / 2 for u in mu for v in mu for _ in range(2)]
    return sorted([x for x in raw if x > 1e-12], reverse=True)


def full_evolution(m, n, sign):
    left_to_right = [(i, m + j) for i in range(m) for j in range(n)]
    right_to_left = [(m + j, i) for j in range(n) for i in range(m)]
    arcs = left_to_right + right_to_left
    index = {a: k for k, a in enumerate(arcs)}
    k = len(arcs)
    nbrs = {v: ([m + j for j in range(n)] if v < m
                else list(range(m))) for v in range(m + n)}
    amplitude = np.zeros((k, k))
    a0, b0 = index[left_to_right[0]], index[right_to_left[0]]
    amplitude[a0, b0] = 1 / math.sqrt(2)
    amplitude[b0, a0] = sign / math.sqrt(2)
    measurements = []
    for t in range(5):
        eigenvalues = np.linalg.svd(amplitude, compute_uv=False) ** 2
        nonzero = eigenvalues[eigenvalues > 1e-11]
        entropy = -sum(x * math.log(x) for x in nonzero)
        expected = exact_spectrum(m, n, t)
        got = sorted(nonzero.tolist(), reverse=True)
        assert len(got) == len(expected), (m, n, t, got, expected)
        assert np.allclose(got, expected, atol=2e-12, rtol=2e-12)
        assert abs(entropy - exact_entropy(m, n, t)) < 2e-11
        assert abs(np.linalg.norm(amplitude) - 1) < 3e-12
        measurements.append((t, entropy, len(got)))
        if t == 4:
            break
        nxt = np.zeros_like(amplitude)
        for (origin1, terminal1), row in index.items():
            for (origin2, terminal2), col in index.items():
                amp = amplitude[row, col]
                if abs(amp) < 1e-14:
                    continue
                for new1 in nbrs[terminal1]:
                    for new2 in nbrs[terminal2]:
                        coef = (2 / (len(nbrs[terminal1]) * len(nbrs[terminal2]))
                                - int(new1 == origin1 and new2 == origin2))
                        nxt[index[(terminal1, new1)],
                            index[(terminal2, new2)]] += amp * coef
        amplitude = nxt
    return measurements


def main():
    total = 0
    for m, n in ((1, 1), (1, 2), (1, 5), (2, 2), (2, 3),
                 (2, 4), (3, 3), (3, 4), (4, 3)):
        for sign in (+1, -1):
            series = full_evolution(m, n, sign)
            print(f'K_{{{m},{n}}}, sign={sign:+d}:', series)
            total += len(series)
    # Fixed edge counts: factors closest to sqrt(q) give the largest peak.
    for q in (4, 6, 12, 24, 36, 60):
        factorizations = [(m, q // m) for m in range(1, int(math.sqrt(q)) + 1)
                          if q % m == 0]
        values = [exact_entropy(m, n, 2) for m, n in factorizations]
        assert all(x <= y + 1e-13 for x, y in zip(values, values[1:]))
    print(f'PASS: {total} exact-time spectral and entropy comparisons, '
          'including both exchange symmetries and period-four checks.')


if __name__ == '__main__':
    main()
