"""Exact finite-binomial checks for the binary two-class separation threshold.

This verifier supplies finite checks only; the asymptotic theorem rests on
Harper's isoperimetric theorem and the uniform binomial normal approximation.
"""
from math import comb, floor
from statistics import NormalDist


def quantile_index(prefix, threshold):
    return next(i for i, v in enumerate(prefix) if v >= threshold)


def finite_bounds(s, t, n):
    if s < 1 or t < 1 or n <= s:
        raise ValueError('require s>=1, t>=1, n>s')
    values = [comb(n, i) for i in range(n + 1)]
    prefix = []
    total = 0
    for v in values:
        total += v
        prefix.append(total)
    assert total == 1 << n
    def V(j):
        return 0 if j < 0 else prefix[min(j, n)]
    M = 1 << (n-s-1)   # equally-sized classes, expressed relative to cube
    j = quantile_index(prefix, M)
    forced_neighborhood = V(j - 1 + 2 * t)
    balanced_capacity = (1 << n) - M
    # The source's isoperimetric criterion forces nonexistence when the
    # radius-2t neighborhood exceeds the capacity of the balanced class.
    certified_failure = forced_neighborhood > balanced_capacity
    # Uniform one-sphere enclosure, valid for EVERY allowed class size.
    max_interval = max(V(u + 2 * t) - V(u - 1) for u in range(j + 1))
    universal_allowance = (1 << n) - (1 << (n-s))
    certified_success = max_interval <= universal_allowance
    assert not (certified_failure and certified_success)
    return certified_failure, certified_success, j, forced_neighborhood, balanced_capacity, max_interval, universal_allowance


def verify_neighborhood_enclosure():
    # Directly enumerate small binary cubes to check the ball enclosures.
    from itertools import combinations
    for n in range(3, 8):
        words = list(range(1 << n))
        order = sorted(words, key=lambda w: (w.bit_count(), tuple(i for i in range(n) if w & (1 << i))))
        for m in [1, 2, 3, min(5, (1 << n) // 4)]:
            if m > len(order):
                continue
            A = set(order[:m])
            j = max(x.bit_count() for x in A)
            radius = 1
            N = {w for w in words if any((w ^ x).bit_count() <= radius for x in A)}
            inner = {w for w in words if w.bit_count() <= j - 1 + radius}
            outer = {w for w in words if w.bit_count() <= j + radius}
            assert inner <= N <= outer
    print('LOCAL_ENCLOSURES_OK')


def main():
    verify_neighborhood_enclosure()
    q = NormalDist()
    for s in (1, 2, 3, 4):
        p = 2**(-s-1)
        z = q.inv_cdf(1-p)
        c = 4/z**2
        print(f's={s} p={p:.8f} z={z:.12f} c={c:.12f}')
        for t in (5, 10, 20):
            n_low = floor(0.75*c*t*t)
            n_high = floor(1.25*c*t*t)
            lo = finite_bounds(s, t, n_low)
            hi = finite_bounds(s, t, n_high)
            print(f' t={t:2d} n_low={n_low:5d} balanced_obstruction={lo[0]} n_high={n_high:5d} universal_certificate={hi[1]}')
            assert lo[0], (s,t,n_low,'lower obstruction missing')
            assert hi[1], (s,t,n_high,'upper certificate missing')
    print('EXACT_BINOMIAL_BRACKETS_OK')


if __name__ == '__main__':
    main()
