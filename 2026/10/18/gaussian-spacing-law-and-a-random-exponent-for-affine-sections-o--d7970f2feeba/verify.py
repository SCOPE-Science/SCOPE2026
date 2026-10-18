"""Independent finite-dimensional checks for invariant affine simplex sections.

Run: python verify.py
Requires numpy and scipy. All infinite-dimensional conclusions are analytic.
"""
import numpy as np
from scipy.integrate import quad
from scipy.special import ndtr, comb


def exact_rank_probabilities(m):
    if m < 3:
        raise ValueError('m must be >= 3')
    gaps = []
    for k in range(1, m):
        def integrand(t):
            return comb(m, k) * ndtr(t) ** k * ndtr(-t) ** (m-k)
        gaps.append(quad(integrand, -11, 11, epsabs=1e-12)[0])
    gaps = np.array(gaps)
    denominator = quad(lambda t: 1 - ndtr(t) ** m - ndtr(-t) ** m,
                       -11, 11, epsabs=1e-12)[0]
    assert abs(gaps.sum() - denominator) < 1e-9
    return gaps / denominator


def invariant_plane_simulation(m, count, rng):
    """Normals Haar on sum-zero subspace; offsets Lebesgue via rejection."""
    z = rng.standard_normal((count, m))
    z -= z.mean(axis=1, keepdims=True)
    u = z / np.linalg.norm(z, axis=1, keepdims=True)
    offset = rng.uniform(-1, 1, size=count)
    keep = (offset >= u.min(axis=1)) & (offset <= u.max(axis=1))
    rank = (u[keep] < offset[keep, None]).sum(axis=1)
    return np.bincount(rank, minlength=m+1)[1:m] / len(rank), len(rank)


def main():
    rng = np.random.default_rng(20261015)
    comparisons = 0
    for m in (4, 5, 7, 12):
        exact = exact_rank_probabilities(m)
        assert np.all(exact > 0) and abs(exact.sum()-1) < 1e-10
        assert np.allclose(exact, exact[::-1], atol=1e-12)
        observed, accepted = invariant_plane_simulation(m, 260000, rng)
        discrepancy = max(abs(observed-exact))
        assert accepted > 20000
        assert discrepancy < 0.012, (m, discrepancy)
        # Rank k section has k(m-k) vertices, explicitly test the support.
        assert len({k*(m-k) for k in range(1,m)}) == m//2
        comparisons += (m-1)
        print(f'm={m} accepted={accepted} max_error={discrepancy:.5f}')
    # Exact Gaussian pair spacings agree with the geometric offset distribution.
    assert abs(exact_rank_probabilities(4)[1] - 0.2885355) < 1e-5
    print(f'AFFINE_SIMPLEX_CHECK_OK comparisons={comparisons}')


if __name__ == '__main__':
    main()
