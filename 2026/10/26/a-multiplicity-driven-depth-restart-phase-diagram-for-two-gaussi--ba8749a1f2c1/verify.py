"""Reproduce two-query Gaussian eigenray selection comparisons.

Only Python's standard library is required. Finite checks corroborate the
explicit probabilities; they do not establish the universal inequalities.
"""
import math
import random

PI = math.pi


def cdf(m, x):
    assert m in (1, 2) and x >= 0
    if m == 1:
        return 2 * math.atan(x) / PI
    return 1 - 1 / math.sqrt(1 + x * x)


def probabilities(m, kappa, epsilon):
    deep = cdf(m, kappa * kappa * epsilon)
    shallow = 1 - (1 - cdf(m, kappa * epsilon)) ** 2
    return deep, shallow


def contrast(u):
    return math.tan(2 * u - 2 * u * u / PI) / math.tan(u)


def simulate(m, kappa, epsilon, sample_count=24000, seed=101):
    rng = random.Random(seed)
    count_deep = 0
    count_shallow = 0
    for _ in range(sample_count):
        probes = [[rng.gauss(0, 1) for _ in range(m + 1)] for j in range(2)]
        g = probes[0]
        # Two sequential products of diag(kappa,1,...,1).
        ag = [kappa * g[0]] + g[1:]
        aag = [kappa * ag[0]] + ag[1:]
        error_deep = math.hypot(*aag[1:]) / abs(aag[0])
        # Two independently applied products, selected by the observable gain.
        scores = []
        images = []
        for probe in probes:
            image = [kappa * probe[0]] + probe[1:]
            scores.append(math.hypot(*image) / math.hypot(*probe))
            images.append(image)
        best = images[max(range(2), key=lambda j: scores[j])]
        error_shallow = math.hypot(*best[1:]) / abs(best[0])
        count_deep += error_deep <= epsilon
        count_shallow += error_shallow <= epsilon
    return count_deep / sample_count, count_shallow / sample_count


def run():
    # Exact equality definition and sign criterion at sampled interior angles.
    for j in range(1, 400):
        u = PI * j / 800
        kappa = contrast(u)
        epsilon = math.tan(u) / kappa
        p, r = probabilities(1, kappa, epsilon)
        assert abs(p - r) < 2e-13, (u, p, r)
        assert kappa > 1

    # The dimension-three threshold follows from squaring positive terms.
    for kappa in (1.1, 1.4, math.sqrt(2), 1.95, 3.0):
        for epsilon in (0.01, 0.1, 0.4, 0.9, 2.0, 9.0):
            deep, shallow = probabilities(2, kappa, epsilon)
            exact_sign = kappa * kappa * (1 - epsilon * epsilon) - 2
            if abs(exact_sign) > 1e-7:
                assert (deep > shallow) == (exact_sign > 0), (kappa, epsilon)

    # An explicit two-dimensional reentrant example.
    low = probabilities(1, 1.95, 0.01)
    mid = probabilities(1, 1.95, 0.1)
    high = probabilities(1, 1.95, 1)
    assert low[0] < low[1] and mid[0] > mid[1] and high[0] < high[1]
    assert contrast(PI / 12) < 1.95
    assert contrast(1e-5) < 2
    assert contrast(1e-6) > 1.99

    checks = 0
    for m in (1, 2):
        for kappa, epsilon in ((1.4, .1), (1.95, .1), (1.95, 1.), (3., .1)):
            expected = probabilities(m, kappa, epsilon)
            observed = simulate(m, kappa, epsilon, seed=17 + m + int(100 * kappa))
            assert all(abs(a - b) < 0.022 for a, b in zip(expected, observed)), (m, kappa, epsilon, expected, observed)
            checks += 1
    print(f"VERIFY_OK: 399 exact-angle identities, 30 dimension-three sign checks, {checks} seeded simulations")


if __name__ == '__main__':
    run()
