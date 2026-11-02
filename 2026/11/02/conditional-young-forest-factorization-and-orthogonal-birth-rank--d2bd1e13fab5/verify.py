#!/usr/bin/env python3
"""Exact finite replay of conditional fringe-subtree identities (stdlib only)."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import factorial


def subtree_sizes(parents, n):
    # parents[v] for v >=2; each parent is smaller than its child.
    sizes = [0] + [1] * n
    for v in range(n, 1, -1):
        sizes[parents[v]] += sizes[v]
    return sizes


def forest_data(parents, i, n):
    # Canonical restriction to edges with both endpoints >i.
    forest = tuple(parents[v] if parents[v] > i else 0
                   for v in range(i + 1, n + 1))
    counts = {v: 1 for v in range(i + 1, n + 1)}
    for v in range(n, i, -1):
        if parents[v] > i:
            counts[parents[v]] += counts[v]
    roots = [v for v in range(i + 1, n + 1) if parents[v] <= i]
    return forest, tuple(sorted(counts[v] for v in roots))


def check(n):
    assertions = 0
    number = factorial(n - 1)
    sums = [0] * (n + 1)
    second = [0] * (n + 1)
    cross = [[0] * (n + 1) for _ in range(n + 1)]
    forests = [defaultdict(Counter) for _ in range(n + 1)]
    components = [dict() for _ in range(n + 1)]
    joint = Counter()
    for choices in product(*(range(1, v) for v in range(2, n + 1))):
        par = [0, 0] + list(choices)
        sub = subtree_sizes(par, n)
        for i in range(1, n + 1):
            sums[i] += sub[i]
            second[i] += sub[i] ** 2
            for j in range(i + 1, n + 1):
                cross[i][j] += sub[i] * sub[j]
            if i >= 2:
                forest, sizes = forest_data(par, i, n)
                forests[i][forest][sub[i]] += 1
                components[i][forest] = sizes
        if n == 4:
            joint[(sub[2], sub[3])] += 1
    assert sum(sum(c.values()) for c in forests[2].values()) == number
    assertions += 1
    for i in range(1, n + 1):
        assert Fraction(sums[i], number) == Fraction(n, i)
        assertions += 1
        expected_var = Fraction(n * (n - i) * (i - 1), i * i * (i + 1))
        assert Fraction(second[i], number) - Fraction(n * n, i * i) == expected_var
        assertions += 1
        for j in range(i + 1, n + 1):
            assert Fraction(cross[i][j], number) == Fraction(n * n, i * j)
            assertions += 1
    for i in range(2, n + 1):
        for forest, hist in forests[i].items():
            comps = components[i][forest]
            count = sum(hist.values())
            assert count % (i ** len(comps)) == 0
            assertions += 1
            polynomial = {0: 1}
            for size in comps:
                update = Counter()
                for power, coef in polynomial.items():
                    update[power] += (i - 1) * coef
                    update[power + size] += coef
                polynomial = update
            # Exact conditional *distribution* (not only conditional mean)
            for degree in range(n - i + 1):
                lhs = Fraction(hist.get(degree + 1, 0), count)
                rhs = Fraction(polynomial.get(degree, 0), i ** len(comps))
                assert lhs == rhs, (n, i, forest, degree, lhs, rhs)
                assertions += 1
            cond_mean = sum(x * f for x, f in hist.items())
            assert Fraction(cond_mean, count) == Fraction(n, i)
            assertions += 1
    if n == 4:
        assert Fraction(joint[(3, 2)], number) == Fraction(1, 6)
        assertions += 1
    # Weighted path lengths can be read off the same diagonal covariance form.
    for weights in ([1] * n, [k % 3 - 1 for k in range(1, n + 1)],
                    [(-1) ** k * k for k in range(1, n + 1)]):
        total_mean = sum(Fraction(weights[i - 1] * n, i) for i in range(1, n + 1))
        total_var = sum(Fraction(weights[i - 1] ** 2 * n * (n - i) * (i - 1),
                                 i * i * (i + 1)) for i in range(1, n + 1))
        direct_mean = Fraction(sum(weights[i - 1] * sums[i]
                                   for i in range(1, n + 1)), number)
        direct_second = Fraction(sum(weights[i - 1] ** 2 * second[i]
                           for i in range(1, n + 1)) +
                           2 * sum(weights[i - 1] * weights[j - 1] * cross[i][j]
                          for i in range(1, n + 1) for j in range(i + 1, n + 1)), number)
        assert (direct_mean, direct_second - direct_mean ** 2) == (total_mean, total_var)
        assertions += 1
    return number, assertions


def main():
    objects = checks = 0
    for n in range(2, 9):
        num, a = check(n)
        objects += num
        checks += a
        print(f'n={n}: {num} recursive trees, {a} exact checks')
    print(f'PASS: {objects} trees, {checks} exact assertions; all conditional forest laws and covariance identities hold in these finite tests.')


if __name__ == '__main__':
    main()
