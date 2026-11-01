"""Independent finite-dimensional checks for Chebyshev-observable compressions.

Run: python verify.py. Requires numpy; checks finite examples, not an infinite theorem.
"""
import math
import numpy as np


def direct_cosine_matrix(m, K):
    C = np.zeros((K, K), dtype=float)
    for i in range(K):
        for j in range(K):
            if i == 0 and j == m or j == 0 and i == m:
                C[i, j] = 1 / math.sqrt(2)
            elif i > 0 and j > 0:
                C[i, j] = (int(abs(i - j) == m) + int(i + j == m)) / 2
    return C


def predicted_cosine_eigenvalues(m, K):
    roots = []
    L0 = 1 + (K - 1) // m
    roots.extend(math.cos((2*r - 1) * math.pi / (2*L0)) for r in range(1, L0 + 1))
    for r in range(1, (m + 1) // 2):
        L = sum(j % m in (r, m-r) for j in range(1, K))
        roots.extend(math.cos(j * math.pi / (L + 1)) for j in range(1, L+1))
    if m % 2 == 0:
        L = sum(j % m == m//2 for j in range(1, K))
        roots.extend(math.cos((2*j - 1)*math.pi / (2*L+1)) for j in range(1,L+1))
    assert len(roots) == K
    return np.sort(np.asarray(roots))


def sharp_low_rank_eigenvalues(m, K):
    assert 1 <= K <= m
    p = max(0, K - m//2 - 1)
    central = int((m % 2 == 0) and (K > m//2))
    return np.sort(np.asarray([.25]*(p+central) + [.5]*(K-2*p-central) + [.75]*p))


def star_discrepancy_from_uniform_angles(cosine_eigenvalues):
    a = np.sort(np.arccos(np.clip(cosine_eigenvalues, -1, 1)) / math.pi)
    K = len(a)
    return max(np.max((np.arange(K)+1)/K - a), np.max(a - np.arange(K)/K))


def quadrature_cosine_matrix(m, K):
    # Exact for these cosines with sufficiently many midpoint samples.
    N = max(160, 8*(m + 2*K))
    theta = (np.arange(N) + .5) * math.pi / N
    E = np.cos(np.outer(theta, np.arange(K)))
    E[:, 1:] *= math.sqrt(2)
    return E.T @ (np.cos(m * theta)[:,None] * E) / N


def main():
    count = 0
    for m in range(2, 26):
        for K in range(1, 4*m + 5):
            C = direct_cosine_matrix(m, K)
            actual = np.linalg.eigvalsh(C)
            predicted = predicted_cosine_eigenvalues(m, K)
            assert np.allclose(actual, predicted, atol=3e-12, rtol=0), (m,K)
            assert np.all((-1.000000001 <= actual) & (actual <= 1.000000001))
            if K <= m:
                assert np.allclose(np.sort((1-actual)/2), sharp_low_rank_eigenvalues(m,K), atol=3e-12,rtol=0), (m,K)
            if K <= (m+1)//2:
                assert np.max(abs(C)) < 1e-13
            else:
                assert np.max(abs(C)) >= .4999999
            discrepancy = star_discrepancy_from_uniform_angles(actual)
            assert discrepancy < (m//2 + 1)/K + 1e-10, (m,K,discrepancy)
            count += 1
    checks = 0
    for m,K in [(2,3),(3,2),(5,6),(8,7),(16,14),(23,32),(37,41)]:
        C=direct_cosine_matrix(m,K)
        assert np.max(abs(C-quadrature_cosine_matrix(m,K))) < 4e-14, (m,K)
        checks+=1
    for n in range(1,9):
        m=2**n
        K=(m+1)//2
        assert np.allclose(direct_cosine_matrix(m,K), np.zeros((K,K)))
        K+=1
        assert np.linalg.norm(direct_cosine_matrix(m,K),2) >= .499999999
    print('PASS:', count, 'finite spectral/cutoff/discrepancy cases;')
    print('PASS:', checks, 'independent Chebyshev quadrature cases;')
    print('PASS: 8 exact logistic-iterate resolution thresholds.')
    print('These checks are finite corroboration; the general claims require the written proof.')


if __name__ == '__main__':
    main()
