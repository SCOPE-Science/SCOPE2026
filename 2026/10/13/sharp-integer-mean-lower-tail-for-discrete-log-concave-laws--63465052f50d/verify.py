#!/usr/bin/env python3
import math


def mean_truncated(n, r):
    weights = [r ** j for j in range(n + 1)]
    z = sum(weights)
    return sum(j * w for j, w in enumerate(weights)) / z


def solve_ratio(k, n):
    lo = k / (k + 1.0)
    hi = 1.0
    assert n > 2 * k
    assert mean_truncated(n, lo) < k
    for _ in range(180):
        mid = (lo + hi) / 2.0
        if mean_truncated(n, mid) < k:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def tail(n, k, r):
    return (r ** k) * (1.0 - r ** (n - k + 1)) / (1.0 - r ** (n + 1))


def main():
    max_mean_error = 0.0
    for k in (1, 2, 5, 10, 25, 50):
        n = max(2 * k + 1, 20 * k)
        r = solve_ratio(k, n)
        mu = mean_truncated(n, r)
        t = tail(n, k, r)
        target = (k / (k + 1.0)) ** k
        max_mean_error = max(max_mean_error, abs(mu - k))
        assert k / (k + 1.0) < r < 1.0
        assert abs(mu - k) < 2e-11
        assert abs(t - target) < 2e-5
        assert t > 1.0 / math.e
    k = 100
    n = 3000
    r = solve_ratio(k, n)
    t = tail(n, k, r)
    assert 1.0 / math.e < t < 0.37
    print('VERIFY_OK', 'max_mean_error=%.3e' % max_mean_error, 'k100_tail=%.12f' % t)


if __name__ == '__main__':
    main()
