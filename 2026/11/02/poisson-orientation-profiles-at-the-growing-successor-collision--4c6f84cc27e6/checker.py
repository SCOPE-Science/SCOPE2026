"""Finite checks for multi-successor adjacency-overlap formulas.

Run with Python 3.10 or later.  All tests are independent finite checks;
Poisson limits require the separate symbolic factorial-moment proof.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb


def counts_from_paths(paths, j):
    """Enumerate witnesses directly over relation-index subsets and pairs."""
    k = len(paths)
    n = len(paths[0])
    orientations = []
    for path in paths:
        d = {}
        for a, b in zip(path, path[1:]):
            d[tuple(sorted((a, b)))] = 1 if a < b else -1
        orientations.append(d)
    hist = Counter()
    for u in range(n):
        for v in range(u + 1, n):
            e = (u, v)
            for inds in combinations(range(k), j):
                vals = [orientations[i].get(e, 0) for i in inds]
                if 0 in vals:
                    continue
                h = min(vals.count(1), vals.count(-1))
                hist[h] += 1
    return tuple(hist[h] for h in range(j // 2 + 1))


def counts_from_edge_frequencies(paths, j):
    """Independently aggregate successor orientations and choose subsets."""
    freq = defaultdict(lambda: [0, 0])
    for path in paths:
        for a, b in zip(path, path[1:]):
            slot = 0 if a < b else 1
            freq[tuple(sorted((a, b)))][slot] += 1
    total = [0] * (j // 2 + 1)
    for pos, neg in freq.values():
        for h in range(j // 2 + 1):
            allowed = [h] if 2 * h == j else [h, j - h]
            for r in allowed:
                if r <= pos and j - r <= neg:
                    total[h] += comb(pos, r) * comb(neg, j - r)
    return tuple(total)


def weight(j, h):
    return comb(j, h) if j == 2 * h else 2 * comb(j, h)


def exact_small_enumeration(n, k, j):
    paths = list(permutations(range(n)))
    numerators = [0] * (j // 2 + 1)
    checked = 0
    for choices in product(paths, repeat=k):
        a = counts_from_paths(choices, j)
        b = counts_from_edge_frequencies(choices, j)
        assert a == b, (n, k, j, choices, a, b)
        for h, v in enumerate(a):
            numerators[h] += v
        checked += 1
    for h, numerator in enumerate(numerators):
        empirical = Fraction(numerator, checked)
        analytic = Fraction(comb(n, 2) * comb(k, j) * weight(j, h), n ** j)
        assert empirical == analytic, (n, k, j, h, empirical, analytic)
    return checked, tuple(Fraction(x, checked) for x in numerators)


def exact_adjacency_probabilities():
    for n in range(2, 8):
        all_paths = list(permutations(range(n)))
        e = (0, 1)
        n_fwd = sum(any(x == 0 and y == 1 for x, y in zip(p, p[1:])) for p in all_paths)
        n_bwd = sum(any(x == 1 and y == 0 for x, y in zip(p, p[1:])) for p in all_paths)
        assert Fraction(n_fwd, len(all_paths)) == Fraction(1, n)
        assert Fraction(n_bwd, len(all_paths)) == Fraction(1, n)
        if n >= 4:
            targets = {(0, 1), (2, 3)}
            n_both = sum(targets.issubset({tuple(sorted((x, y))) for x, y in zip(p, p[1:])}) for p in all_paths)
            assert Fraction(n_both, len(all_paths)) == Fraction(4, n * (n - 1))
        if n >= 3:
            targets = {(0, 1), (1, 2)}
            n_both = sum(targets.issubset({tuple(sorted((x, y))) for x, y in zip(p, p[1:])}) for p in all_paths)
            assert Fraction(n_both, len(all_paths)) == Fraction(2, n * (n - 1))


def main():
    exact_adjacency_probabilities()
    checks = [(2, 3, 3), (3, 3, 3), (4, 3, 3), (3, 4, 4), (4, 4, 4)]
    for n, k, j in checks:
        count, averages = exact_small_enumeration(n, k, j)
        print(f'n={n} k={k} j={j} checked={count} means={averages}')
    for j in range(3, 12):
        assert sum(weight(j, h) for h in range(j // 2 + 1)) == 2 ** j
    print('ALL_CHECKS_OK')


if __name__ == '__main__':
    main()
