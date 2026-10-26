"""Reproducible tests for the two-input variation modulus of cyclic running medians.
Requires only Python 3 standard library. All enumerated inputs are exact integers.
The all-dimension theorem is proved analytically; these are finite regressions.
"""
from itertools import permutations


def tv(v):
    return sum(abs(v[(j + 1) % len(v)] - v[j]) for j in range(len(v)))


def median3(a, b, c):
    return a + b + c - min(a, b, c) - max(a, b, c)


def selector(f):
    n = len(f)
    indices = []
    for j in range(n):
        candidates = ((f[(j - 1) % n], (j - 1) % n),
                      (f[j], j),
                      (f[(j + 1) % n], (j + 1) % n))
        indices.append(sorted(candidates)[1][1])
    return indices


def median_filter(f):
    n = len(f)
    return [median3(f[(j - 1) % n], f[j], f[(j + 1) % n]) for j in range(n)]


def arcs(n):
    for start in range(n):
        for size in range(1, n):
            yield tuple(int((j - start) % n < size) for j in range(n))


def max_selector_components(f):
    s = selector(f)
    return max(tv([h[s[j]] for j in range(len(f))]) // 2 for h in arcs(len(f)))


def witness(n):
    if n == 4:
        return (0, 2, 1, 3), (1, 1, 0, 0), 2
    if n == 5:
        return (0, 1, 3, 2, 4), (1, 1, 1, 0, 0), 2
    if n == 6:
        return (0, 2, 1, 5, 3, 4), (0, 0, 1, 1, 1, 0), 3
    if n >= 7:
        f = [10 + j for j in range(n)]
        values = {n - 2: 0, 0: 1, n - 1: 2, 1: 3, 3: 4, 2: 5, 4: 6}
        for j, value in values.items():
            f[j] = value
        return tuple(f), tuple(int(j in (0, 1, 2)) for j in range(n)), 3
    raise ValueError('witness domain is n>=4')


def main():
    expected = {3: 0, 4: 2, 5: 2, 6: 3, 7: 3}
    tested = 0
    for n in range(3, 8):
        best = 0
        for f in permutations(range(n)):
            best = max(best, max_selector_components(f))
            tested += 1
        assert best == expected[n], (n, best)

    witness_count = 0
    for n in range(4, 41):
        f, h, expected_ratio = witness(n)
        s = selector(f)
        ratio = tv([h[j] for j in s]) // 2
        assert tv(h) == 2
        assert ratio == expected_ratio, (n, ratio, expected_ratio)
        # Both samples have the same strict coordinate ordering; exact fractions
        # could be used, but scaling the base by ten gives integer samples.
        scaled = [10 * z for z in f]
        displaced = [scaled[j] + h[j] for j in range(n)]
        assert tv([median_filter(displaced)[j] - median_filter(scaled)[j]
                   for j in range(n)]) == 2 * expected_ratio
        witness_count += 1

    tvd_count = 0
    for n in range(3, 13):
        for mask in range(1 << n):
            h = [(mask >> j) & 1 for j in range(n)]
            assert tv(median_filter(h)) <= tv(h)
            tvd_count += 1

    print('PASS: exhaustive selector/arc tests for n=3,...,7:', tested)
    print('PASS: exact attaining pairs for n=4,...,40:', witness_count)
    print('PASS: binary one-input TV contraction tests:', tvd_count)
    print('Finite checks complement, and do not replace, the analytic all-n proof.')

if __name__ == '__main__':
    main()
