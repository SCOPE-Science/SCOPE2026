"""Reproduce fourth-moment and inverse tests for a switching-diffusivity harmonic trap.

Requires Python 3 standard library only. All checks concern exact model observables;
Monte Carlo sampling is not used to infer universal validity.
"""
import math
import random


def kernel(kappa, rate, lag):
    a = math.exp(-2 * kappa * lag)
    if abs(rate - kappa) < 1e-11 * max(rate, kappa):
        return a * (1 + 2 * kappa * lag)
    return (kappa * math.exp(-2 * rate * lag) - rate * a) / (kappa - rate)


def simpson(f, length, n=240):
    step = length / n
    return step / 3 * (f(0.0) + f(length) + 4 * sum(f((2 * j - 1) * step) for j in range(1, n // 2 + 1)) + 2 * sum(f(2 * j * step) for j in range(1, n // 2)))


def moment_solve(kappa, mean_diff, contrast, rate, lag):
    # Independently solve the 2x2 stationary generator equations for raw moments.
    d1, d2 = mean_diff * (1 + contrast), mean_diff * (1 - contrast)
    def solve(order, rhs1, rhs2):
        diagonal = order * kappa + rate
        det = diagonal**2 - rate**2
        return ((diagonal * rhs1 + rate * rhs2) / det, (rate * rhs1 + diagonal * rhs2) / det)
    x1, x2 = solve(2, d1, d2)
    y1, y2 = solve(4, 12 * d1 * x1, 12 * d2 * x2)
    a = math.exp(-2 * kappa * lag)
    j = simpson(lambda u: math.exp(-2 * kappa * (lag - u) - 2 * rate * u), lag)
    future_mean_noise = mean_diff * (1 - a) / kappa
    future_state_noise = 2 * mean_diff * contrast * j
    v = x1 + x2
    k = (y1 + y2) / v**2 - 3
    square_covar = a * (y1 + y2) + future_mean_noise * (x1 + x2) + future_state_noise * (x1 - x2) - v * v
    return v, k, square_covar / v**2


def analytical(kappa, mean_diff, contrast, rate, lag):
    v = mean_diff / kappa
    k = 3 * contrast**2 * kappa / (kappa + rate)
    a = math.exp(-2 * kappa * lag)
    c = 2 * a + (k / 3) * (2 * a + kernel(kappa, rate, lag))
    return v, k, c


def reconstruct(kappa, lag, v, k, c):
    a = math.exp(-2 * kappa * lag)
    if not (v > 0 and 0 < k < 3):
        raise ValueError('Not realizable')
    upper = kappa * (3 / k - 1)
    target = 3 * (c - 2 * a) / k - 2 * a
    if not (kernel(kappa, upper, lag) < target < 1):
        raise ValueError('Not realizable')
    low, high = 0.0, upper
    for _ in range(85):
        mid = (low + high) / 2
        if kernel(kappa, mid, lag) > target:
            low = mid
        else:
            high = mid
    rate = (low + high) / 2
    contrast = math.sqrt(k * (kappa + rate) / (3 * kappa))
    return kappa * v, contrast, rate


def main():
    rng = random.Random(78142)
    maximal = [0.0, 0.0, 0.0]
    for _ in range(600):
        kap = math.exp(rng.uniform(-0.8, 0.8))
        diff = math.exp(rng.uniform(-0.8, 0.8))
        contrast = rng.uniform(0.15, 0.85)
        rate = kap * math.exp(rng.uniform(-1.4, 1.4))
        lag = rng.uniform(0.15, 1.3) / kap
        direct = moment_solve(kap, diff, contrast, rate, lag)
        theorem = analytical(kap, diff, contrast, rate, lag)
        errs = [abs(x-y) for x, y in zip(direct, theorem)]
        maximal = [max(a, b) for a, b in zip(maximal, errs)]
        assert max(errs) < 3e-9, (direct, theorem, errs)
        recovered = reconstruct(kap, lag, *theorem)
        assert abs(recovered[0]-diff) < 1e-9
        assert abs(recovered[1]-contrast) < 1e-9
        assert abs(recovered[2]-rate) < 1e-9
    for kappa, h in [(1.0,0.7), (0.8,1.7), (4,0.1)]:
        for s in (0.15*kappa, kappa, 3*kappa):
            q = [kernel(kappa, rate, h) for rate in (s/1.01, s, s*1.01)]
            assert q[0] > q[1] > q[2]
            integral = math.exp(-2*kappa*h) + 2*kappa*simpson(lambda u: math.exp(-2*kappa*(h-u)-2*s*u), h)
            assert abs(integral - kernel(kappa,s,h)) < 1e-10
    print('PASS: 600 independent Markov-moment comparisons and inverse reconstructions')
    print('Maximum absolute discrepancies (V, K, C):', *('%.3g' % e for e in maximal))
    print('PASS: monotonic kernel and removable singularity spot checks')


if __name__ == '__main__':
    main()
