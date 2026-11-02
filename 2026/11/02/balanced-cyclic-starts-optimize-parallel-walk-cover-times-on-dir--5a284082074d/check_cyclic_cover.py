"""Exact finite checks for cyclic-class parallel-walk cover times.

Run: python3 check_cyclic_cover.py
Standard-library only. These tests check finite instances; the proof for all sizes
is given in RESULT.md.
"""
from fractions import Fraction
from itertools import product
from math import factorial


def stirling_second(nmax, kmax):
    a = [[0] * (kmax + 1) for _ in range(nmax + 1)]
    a[0][0] = 1
    for m in range(1, nmax + 1):
        for j in range(1, min(kmax, m) + 1):
            a[m][j] = j * a[m - 1][j] + a[m - 1][j - 1]
    return a


def coupon_prob(n, m, stirling=None):
    if m < n:
        return Fraction(0)
    if stirling is None:
        stirling = stirling_second(m, n)
    return Fraction(factorial(n) * stirling[m][n], n**m)


def circular_allocations(d, k):
    if d == 1:
        yield (k,)
    else:
        for j in range(k + 1):
            for rest in circular_allocations(d - 1, k - j):
                yield (j,) + rest


def mechanical(d, k):
    return tuple((j + 1) * k // d - j * k // d for j in range(d))


def class_visits(h, t):
    d = len(h)
    k = sum(h)
    q, s = divmod(t + 1, d)
    return tuple(q * k + sum(h[(j - i) % d] for i in range(s))
                 for j in range(d))


def balanced_windows(h):
    d = len(h)
    for s in range(1, d):
        w = [sum(h[(j - i) % d] for i in range(s)) for j in range(d)]
        if max(w) - min(w) > 1:
            return False
    return True


def cover_probability(n, h, t, stirling):
    out = Fraction(1)
    for m in class_visits(h, t):
        out *= coupon_prob(n, m, stirling)
    return out


def brute_force_walk_probability(n, h, t):
    """Enumerate all actual walker trajectories, not using coupon formulas."""
    d = len(h)
    starts = [j for j, v in enumerate(h) for _ in range(v)]
    k = len(starts)
    hits = 0
    total = n ** (k * (t + 1))
    for labels in product(range(n), repeat=k * (t + 1)):
        masks = [0] * d
        for a, initial in enumerate(starts):
            for step in range(t + 1):
                part = (initial + step) % d
                masks[part] |= 1 << labels[a * (t + 1) + step]
        hits += int(all(mask == (1 << n) - 1 for mask in masks))
    return Fraction(hits, total)


def main():
    checks = 0
    # Strict log-concavity of coupon-collector CDF after it becomes positive.
    for n in range(2, 13):
        S = stirling_second(112, n)
        for m in range(n, 110):
            f0 = coupon_prob(n, m - 1, S)
            f1 = coupon_prob(n, m, S)
            f2 = coupon_prob(n, m + 1, S)
            assert f1 * f1 > f0 * f2, (n, m)
            checks += 1
    # Mechanical placement gives nearly equal sample counts at every horizon.
    for d in range(3, 17):
        for k in range(1, 39):
            h = mechanical(d, k)
            assert sum(h) == k and balanced_windows(h)
            for t in range(0, 2 * d):
                w = class_visits(h, t)
                assert max(w) - min(w) <= 1
                assert sum(w) == k * (t + 1)
                checks += 2
    # Check exact CDF and global optimization over all starting allocations.
    for n in range(2, 6):
        for d in range(3, 7):
            for k in range(1, 7):
                hi = mechanical(d, k)
                all_h = list(circular_allocations(d, k))
                T = 4 * d + 2
                S = stirling_second(k * (T + 1), n)
                for t in range(T + 1):
                    pbest = cover_probability(n, hi, t, S)
                    for h in all_h:
                        ph = cover_probability(n, h, t, S)
                        assert pbest >= ph, (n, d, k, t, h)
                        if balanced_windows(h):
                            assert ph == pbest
                        checks += 1
                # If the cyclic balance condition fails, high-time optimality is strict.
                for h in all_h:
                    if balanced_windows(h):
                        continue
                    tbad = next(q * d + s - 1 for s in range(1, d)
                                if max(sum(h[(j - i) % d] for i in range(s))
                                       for j in range(d)) -
                                   min(sum(h[(j - i) % d] for i in range(s))
                                       for j in range(d)) > 1
                                for q in [4])
                    assert cover_probability(n, hi, tbad, S) > cover_probability(n, h, tbad, S)
                    checks += 1
    # Independent direct enumeration of the underlying walk trajectories.
    for n, d, k, max_t in [(2, 3, 2, 5), (2, 4, 2, 5),
                            (3, 3, 2, 4), (2, 3, 3, 3),
                            (3, 4, 2, 3)]:
        S = stirling_second(k * (max_t + 1), n)
        for h in circular_allocations(d, k):
            for t in range(max_t + 1):
                if n ** (k * (t + 1)) > 150000:
                    continue
                brute = brute_force_walk_probability(n, h, t)
                formula = cover_probability(n, h, t, S)
                assert brute == formula, (n, d, k, h, t, brute, formula)
                checks += 1
    print(f'PASS: {checks:,} exact finite assertions')


if __name__ == '__main__':
    main()
