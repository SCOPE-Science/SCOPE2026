"""Numerical cross-checks for a sharp angular-jump dissipation tradeoff.

Uses only Python's standard library. Execute: python verify.py
The analytic result is proved in RESULT.md; finite tests are corroboration only.
"""
import cmath
import math
import random


def f(u):
    assert -1 < u < 1
    return 0.0 if u == 0 else u * math.log((1 + u) / (1 - u))


def sharp_lower(c, s):
    assert c * c + s * s < 1 + 1e-12
    if abs(c) >= 1:
        assert abs(s) < 1e-13
        return 0.0
    return f(abs(s) / math.sqrt(1 - c * c))


def paired_data(angles, weights, oddness):
    c = sum(w * math.cos(t) for t, w in zip(angles, weights))
    s = sum(w * math.sin(t) * u for t, w, u in zip(angles, weights, oddness))
    ep = sum(w * f(u) for w, u in zip(weights, oddness))
    return c, s, ep


def test_random_kernels():
    rng = random.Random(140240)
    count = 0
    for n in (1, 2, 3, 6, 20, 100):
        for _ in range(40):
            angles = [rng.uniform(0.05, math.pi - 0.05) for _ in range(n)]
            raw = [rng.expovariate(1) for _ in range(n)]
            weights = [a / sum(raw) for a in raw]
            oddness = [rng.uniform(-0.98, 0.98) for _ in range(n)]
            c, s, ep = paired_data(angles, weights, oddness)
            assert c*c + s*s < 1
            lower = sharp_lower(c, s)
            assert ep >= lower - 5e-12, (n, c, s, ep, lower)
            count += 1
    return count


def test_exact_optimizers():
    count = 0
    for c, s in ((0., .5), (.6, .4), (-.4, .7), (.8, -.25), (-.9, .01), (.2, 0.)):
        theta = math.acos(c)
        u = s / math.sin(theta)
        got_c, got_s, got_ep = paired_data([theta], [1.], [u])
        assert abs(got_c - c) < 3e-15
        assert abs(got_s - s) < 3e-15
        assert abs(got_ep - sharp_lower(c, s)) < 3e-15
        count += 1
    return count


def test_smooth_approximation_moments():
    # Each pair of narrow, disjoint smooth even bumps can be approximated
    # by the four discrete points here; the first moments are exact.
    c, s = .32, .45
    optimal = sharp_lower(c, s)
    errs = []
    for eps in (.2, .1, .05, .025, .0125):
        rho = math.cos(eps)
        theta = math.acos(c / rho)
        oddness = s / (rho * math.sin(theta))
        c1, s1, ep = paired_data([theta-eps, theta+eps], [.5, .5], [oddness, oddness])
        assert abs(c1-c) < 1e-12
        assert abs(s1-s) < 1e-12
        assert ep >= optimal - 1e-12
        errs.append(ep - optimal)
    assert all(errs[j] > errs[j+1] > 0 for j in range(len(errs)-1)), errs
    return len(errs)


def test_finite_ring_stationarity():
    rng = random.Random(41138)
    count = 0
    for n in (9, 12, 37, 100):
        for _ in range(16):
            raw = [rng.uniform(.01, 1.0) for _ in range(n)]
            p = [x / sum(raw) for x in raw]
            theta = [2 * math.pi * j / n for j in range(n)]
            c = sum(p[j] * math.cos(theta[j]) for j in range(n))
            s = sum(p[j] * math.sin(theta[j]) for j in range(n))
            ep_direct = sum(p[j] * math.log(p[j]/p[(-j)%n]) for j in range(n))
            ep_flow = sum((p[j]-p[(-j)%n])*math.log(p[j]/p[(-j)%n]) for j in range(n)) / 2
            assert abs(ep_direct-ep_flow) < 5e-13
            assert ep_direct >= sharp_lower(c, s) - 5e-12
            count += 1
    return count


def test_small_chirality():
    alpha, c = 2.4, .65
    for s in (1e-3, 3e-4, 1e-4):
        r = s / math.sqrt(1-c*c)
        exact = alpha*f(r)
        leading = 2*alpha*r*r
        assert abs(exact/leading-1) < 2e-6
    return 3


if __name__ == '__main__':
    checks = [
        ('random reflected turning kernels', test_random_kernels),
        ('exact two-angle optimizers', test_exact_optimizers),
        ('constrained narrow bump approximation', test_smooth_approximation_moments),
        ('finite cyclic orientation Markov chains', test_finite_ring_stationarity),
        ('quadratic weak-chirality asymptotic', test_small_chirality),
    ]
    total = 0
    for label, run in checks:
        n = run()
        total += n
        print(f'PASS {label}: {n} comparisons')
    print(f'TOTAL {total} checks passed')
