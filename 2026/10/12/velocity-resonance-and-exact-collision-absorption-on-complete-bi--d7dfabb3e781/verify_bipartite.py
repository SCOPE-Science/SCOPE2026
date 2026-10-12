"""Independent finite-dimensional checks for biclique two-walker capture laws.
Requires numpy and scipy.  Does not establish the infinite-family theorem.
"""
import numpy as np
from scipy.linalg import eigh, eigvals


def numerical_absorbing_projector(p, q, a, b):
    n = p + q
    adjacency = np.zeros((n, n), dtype=float)
    adjacency[:p, p:] = 1
    adjacency[p:, :p] = 1
    h = a * np.kron(adjacency, np.eye(n)) + b * np.kron(np.eye(n), adjacency)
    d = np.eye(n * n)[:, [i * n + i for i in range(n)]]
    eig, vec = eigh(h)
    proj = np.zeros_like(h)
    k = 0
    while k < len(eig):
        j = k + 1
        while j < len(eig) and abs(eig[j] - eig[k]) < 1e-7:
            j += 1
        v = vec[:, k:j]
        x = v.T @ d
        u, sig, _ = np.linalg.svd(x, full_matrices=False)
        rank = int(np.count_nonzero(sig > 1e-8))
        z = v @ u[:, :rank]
        proj += z @ z.T
        k = j
    return h, proj


def expected_probability(p, q, a, b, i, j):
    if i == j:
        return 1.0
    if a != b:
        if i < p and j < p:
            return (2 * p - 1) / (p * (p - 1))
        if i >= p and j >= p:
            return (2 * q - 1) / (q * (q - 1))
        return (p + q - 1) / (p * q)
    denominator = 2 * p * q - p - q
    if i < p and j < p:
        return (2 * q - 1) / denominator
    if i >= p and j >= p:
        return (2 * p - 1) / denominator
    return (p + q - 1) / (2 * p * q)


def check():
    spectral_cases = 0
    localized_cases = 0
    loss_cases = 0
    max_error = 0.0
    for p, q in [(3, 3), (3, 4), (3, 5), (4, 4), (4, 5), (5, 3), (5, 5)]:
        n = p + q
        for a, b in [(1., 1.), (1., 2.), (2., 1.), (2., 3.), (1., np.sqrt(2))]:
            h, proj = numerical_absorbing_projector(p, q, a, b)
            formula_rank = (3 * n - 2) if a == b else (5 * n - 4)
            assert abs(np.trace(proj) - formula_rank) < 1e-7
            assert np.max(np.abs(proj @ proj - proj)) < 2e-9
            assert np.max(np.abs(h @ proj - proj @ h)) < 2e-8
            spectral_cases += 1
            diag = np.diag(proj).reshape(n, n)
            for i in range(n):
                for j in range(n):
                    err = abs(diag[i, j] - expected_probability(p, q, a, b, i, j))
                    max_error = max(max_error, err)
                    assert err < 1e-8, (p, q, a, b, i, j, err)
                    localized_cases += 1
            if (p, q) in ((3, 3), (3, 4)) and (a, b) in ((1., 1.), (1., 2.), (2., 3.)):
                rates = 0.2 + 0.17 * np.arange(n)
                gamma = np.zeros(n*n)
                for i in range(n):
                    gamma[i*n+i] = rates[i]
                loss_spectrum = eigvals(h - 1j * np.diag(gamma))
                neutral = np.count_nonzero(np.abs(loss_spectrum.imag) < 1e-8)
                assert neutral == n*n-formula_rank, (p, q, a, b, neutral)
                assert loss_spectrum.imag.max() < 1e-8
                loss_cases += 1
    print('VERIFY_OK spectral_cases=%d localized_probabilities=%d loss_spectra=%d max_error=%.3g'
          % (spectral_cases, localized_cases, loss_cases, max_error))


if __name__ == '__main__':
    check()
