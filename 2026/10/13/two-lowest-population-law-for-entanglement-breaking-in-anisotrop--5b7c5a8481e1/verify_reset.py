"""Finite consistency checks for an exact quantum reset-channel separability theorem.

This script supports (but does not replace) the stated all-dimensional proof.
Run with Python 3 and NumPy; all examples are explicitly deterministic.
"""
import itertools
import math
import numpy as np


def choi(p, s):
    p = np.asarray(p, dtype=float)
    p = p / p.sum()
    d = len(p)
    omega = np.eye(d).reshape(d * d)
    return s * np.outer(omega, omega) + (1 - s) * np.kron(np.eye(d), np.diag(p))


def partial_transpose_second(matrix, d):
    return matrix.reshape(d, d, d, d).transpose(0, 3, 2, 1).reshape(d * d, d * d)


def phase_separable_matrix(p, s):
    p = np.asarray(p, dtype=float)
    p = p / p.sum()
    d = len(p)
    answer = np.zeros((d * d, d * d), dtype=complex)
    for exponents in itertools.product(range(3), repeat=d):
        phases = np.exp((2j * np.pi / 3) * np.asarray(exponents))
        a = p ** (-0.25) * phases
        b = np.sqrt(s) * p ** (0.25) * phases.conj()
        product = np.kron(a, b)
        answer += np.outer(product, product.conj()) / 3**d
    return answer


def check_fullrank(p):
    p = np.asarray(p, dtype=float)
    p = p / p.sum()
    assert np.all(p > 0) and len(np.unique(p)) >= 3
    d = len(p)
    order = np.sort(p)
    r = math.sqrt(order[0] * order[1])
    threshold = r / (1 + r)
    count = 0
    for s in [0., threshold * .4, threshold, threshold * 1.08]:
        j = choi(p, s)
        assert np.max(np.abs(j - j.T.conj())) < 1e-11
        assert abs(np.trace(j) - d) < 1e-11
        block_eigs = np.linalg.eigvalsh(partial_transpose_second(j, d))
        if s <= threshold:
            assert block_eigs[0] >= -2e-11
            sep = phase_separable_matrix(p, s)
            residue = j - sep
            predicted = np.zeros_like(residue)
            for i in range(d):
                for k in range(d):
                    at = d * i + k
                    if i == k:
                        predicted[at, at] = (1 - s) * p[k]
                    else:
                        predicted[at, at] = (1 - s) * p[k] - s * math.sqrt(p[k] / p[i])
            assert np.max(np.abs(residue - predicted)) < 8e-11
            assert np.min(np.real(np.diag(predicted))) >= -2e-11
        else:
            assert block_eigs[0] < -1e-7
        count += 1
    return count


def test_lindblad():
    p = np.array([.05, .25, .7])
    gamma = 1.3
    r = math.sqrt(p[0] * p[1])
    predicted_time = math.log(1 + 1/r) / gamma
    for delta in [-.15, 0., .15]:
        t = predicted_time + delta
        s = math.exp(-gamma * t)
        lam = min(np.linalg.eigvalsh(partial_transpose_second(choi(p, s), 3)))
        if delta < 0:
            assert lam < -1e-7
        elif delta > 0:
            assert lam >= -1e-12
        else:
            assert abs(lam) < 1e-10
    return 3


def main():
    spectra = [[.2, .3, .5], [.04, .16, .8], [.02, .08, .2, .7],
               [.005, .025, .07, .2, .7]]
    n = sum(check_fullrank(p) for p in spectra)
    assert n == 16
    print(f'VERIFY_OK fullrank_PPT_and_phase_decomposition={n} Lindblad_thresholds={test_lindblad()}')


if __name__ == '__main__':
    main()
