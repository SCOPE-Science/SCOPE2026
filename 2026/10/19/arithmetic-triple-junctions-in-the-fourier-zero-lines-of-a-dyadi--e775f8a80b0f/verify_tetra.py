"""Exact congruence checks for the tetrahedral four-map Fourier mask.

The infinite assertions in the accompanying theorem follow from the proof,
not from finite enumeration here. Python 3.9 or later; no dependencies.
"""
from itertools import product


def valuation2(x):
    if x == 0:
        return float('inf')
    x = abs(x)
    return (x & -x).bit_length() - 1


def zero_pivots_at_level(point, level):
    """Mask vanishing tested by its two independent odd-mod-2 congruences."""
    mod = 1 << level
    half = mod >> 1
    pivots = []
    for i in range(3):
        j, k = [t for t in range(3) if t != i]
        if (point[i] % mod == half and
                (point[j] - point[k]) % mod == half):
            pivots.append(i)
    return pivots


def classify_by_levels(point):
    levels = []
    for level in range(1, 12):
        pivots = zero_pivots_at_level(point, level)
        if pivots:
            levels.append((level, pivots))
    return levels


def classify_by_valuations(point):
    """Independent 2-adic junction criterion; returns number of lines/order."""
    ranked = sorted((valuation2(n), i) for i, n in enumerate(point))
    low, next_low, high = ranked
    if low[0] != next_low[0] or high[0] <= next_low[0]:
        return 0, 0
    x, y = point[low[1]], point[next_low[1]]
    z = point[high[1]]
    triple = z != 0 and x != y and valuation2(x - y) == valuation2(z)
    return (3, 2) if triple else (2, 1)


def main():
    for radius in (7, 15, 31):
        counts = dict(total=0, crossings=0, triples=0, doubles=0)
        for point in product(range(-radius, radius + 1), repeat=3):
            levels = classify_by_levels(point)
            lines = sum(len(pivots) for _, pivots in levels)
            order = len(levels)
            prediction = classify_by_valuations(point)
            observed = (lines, order) if lines >= 2 else (0, 0)
            assert observed == prediction, (point, levels, prediction)
            assert order <= 2, point
            counts['total'] += 1
            counts['crossings'] += lines >= 2
            counts['triples'] += lines == 3
            counts['doubles'] += lines == 2
        assert counts['crossings'] == counts['triples'] + counts['doubles']
        print(f"cube radius {radius}: {counts}")
    assert classify_by_levels((1, 3, 2)) == [(1, [0, 1]), (2, [2])]
    assert classify_by_levels((1, 1, 2)) == [(1, [0, 1])]
    assert classify_by_levels((1, 1, 0)) == [(1, [0, 1])]
    assert sum(2.0 ** (-3 * a - 3) for a in range(75)) * 3 == 3 / 7
    assert abs(3 * sum(2.0 ** (-3 * a - 2 * j - 3)
                       for a in range(75) for j in range(1, 75))
               - 1 / 7) < 1e-14
    print('All exact congruence and density-series checks passed.')


if __name__ == '__main__':
    main()
