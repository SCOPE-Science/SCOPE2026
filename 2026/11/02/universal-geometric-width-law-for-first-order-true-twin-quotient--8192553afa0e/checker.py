"""Reproducible finite checks for the circular true-twin quotient theorem.
No numerical experiment is used as a substitute for the limiting proof.
"""
import bisect
import collections
import math
import random


def gap_hist(points, radius):
    xs = sorted(points)
    n = len(xs)
    lifted = [x - 1 for x in xs] + xs + [x + 1 for x in xs] + [x + 2 for x in xs]
    good = []
    for i in range(n):
        x = xs[i]
        y = xs[(i + 1) % n] + (i == n - 1)
        if y - x >= radius:
            good.append(False)
            continue
        neg = bisect.bisect_left(lifted, y - radius) - bisect.bisect_right(lifted, x - radius)
        pos = bisect.bisect_left(lifted, y + radius) - bisect.bisect_right(lifted, x + radius)
        good.append(neg == 0 and pos == 0)
    assert not all(good)
    root = next(i for i, flag in enumerate(good) if not flag)
    result = collections.Counter()
    run = 1
    for step in range(1, n + 1):
        if good[(root + step) % n]:
            run += 1
        else:
            result[run] += 1
            run = 1
    assert sum(size * count for size, count in result.items()) == n
    return result


def direct_hist(points, radius):
    n = len(points)
    adjacency = []
    for x in points:
        adjacency.append(frozenset(j for j, y in enumerate(points)
                                   if min((x-y) % 1.0, (y-x) % 1.0) <= radius))
    return collections.Counter(collections.Counter(adjacency).values())


def verify():
    rng = random.Random(31415926)
    tests = 0
    for radius in (0.16, 0.27, 0.43):
        for _ in range(750):
            pts = [rng.random() for _ in range(85)]
            if direct_hist(pts, radius) != gap_hist(pts, radius):
                raise AssertionError((radius, sorted(pts)))
            tests += 1
    print('Exact graph-neighborhood versus gap-run checks:', tests)
    n, repetitions = 1200, 120
    for radius in (0.10, 0.24, 0.40, 0.49):
        totals = collections.Counter()
        pair_total = 0
        for _ in range(repetitions):
            hist = gap_hist([rng.random() for _ in range(n)], radius)
            totals.update(hist)
            pair_total += sum(size * (size-1) // 2 * count for size, count in hist.items())
        frequencies = [totals[j] / (n*repetitions) for j in range(1, 6)]
        theory = [4/9 * 3**(-(j-1)) for j in range(1, 6)]
        assert all(abs(obs - expect) < .02 for obs, expect in zip(frequencies, theory))
        assert abs(pair_total/(n*repetitions) - .5) < .08
        print('radius',radius,'frequencies',list(zip([round(x,5) for x in frequencies],
                                                         [round(x,5) for x in theory])),
              'pairs_per_vertex',round(pair_total/(n*repetitions),5))
    print('ALL_CHECKS_OK')


if __name__ == '__main__':
    verify()
