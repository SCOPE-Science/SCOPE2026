"""Finite numerical cross-checks for the affine regular-simplex section law.

All mathematical statements for arbitrary dimension and all asymptotics are proved
analytically in RESULT.md; these quadratures and seeded trials only test examples.
Run: python3 verify.py
"""
import math
import random


def integrated_law(n, step=0.004, cutoff=11.0):
    counts = [0.0] * (n + 1)
    x = -cutoff + 0.5 * step
    while x < cutoff:
        p = 0.5 * math.erfc(-x / math.sqrt(2.0))
        q = 0.5 * math.erfc(x / math.sqrt(2.0))
        # Each binomial term is an unconditional joint density (up to normalization).
        for k in range(1, n):
            counts[k] += math.comb(n, k) * p**k * q**(n-k) * step
        x += step
    m = sum(counts)
    return [v / m for v in counts], m


def verify(n):
    p, m = integrated_law(n)
    assert abs(sum(p) - 1.0) < 1e-11
    assert max(abs(p[k] - p[n - k]) for k in range(1,n)) < 1e-10
    e_faces = sum(k*(n-k)*p[k] for k in range(1,n))
    e_edges = n*(n-1)/(math.sqrt(math.pi)*m)
    assert abs(e_faces - e_edges) < 1e-8
    if n == 3:
        assert abs(e_faces - 2.0) < 1e-9
    if n == 4:
        angle = math.acos(1/3)
        exact = 2*math.pi/(math.pi-angle) - 3
        assert abs(p[2] - exact) < 1e-8
        assert abs(e_faces-(3+exact)) < 1e-8
    return p, m, e_faces


def weighted_normal_trials(n, trials, seed):
    rng = random.Random(seed)
    numerator = [0.0] * (n + 1)
    denominator = 0.0
    for _ in range(trials):
        points = sorted(rng.gauss(0, 1) for _ in range(n))
        width = points[-1] - points[0]
        denominator += width
        for k in range(1, n):
            numerator[k] += points[k] - points[k-1]
    return [x / denominator for x in numerator]


if __name__ == '__main__':
    for n in (3, 4, 5, 8, 16, 64):
        p, m, mean = verify(n)
        print('n_vertices=%d mean_gaussian_range=%.10f expected_section_vertices=%.10f' % (n,m,mean))
        if n in (4, 8):
            trial = weighted_normal_trials(n, 35000, 123456+n)
            err = max(abs(trial[k] - p[k]) for k in range(1,n))
            print('  max_weighted_MC_probability_error=%.5f' % err)
            assert err < 0.012
    print('CHECKS PASS (finite tests; limiting theorem requires analytic proof)')
