"""Exact independent finite checks of a gap-indexed inverse-monoid representation formula.

Runs with Python 3's standard library; no online resources or external files.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import product
from math import comb


def gap_type(g):
    return '1' if g == 1 else ('E' if g % 2 == 0 else 'O')


def signature(a):
    if not a:
        return ('empty',)
    return (a[0] % 2, ''.join(gap_type(b - a0) for a0, b in zip(a, a[1:])))


def all_sets(n):
    return [tuple(i + 1 for i in range(n) if mask & (1 << i))
            for mask in range(1 << n)]


def block_degree(n, parity, word):
    start = 1 if parity == 1 else 2
    minimum_span = start + sum({'1': 1, 'E': 2, 'O': 3}[c] for c in word)
    if minimum_span > n:
        return 0
    variable_gaps = sum(c != '1' for c in word)
    dimension = variable_gaps + 1  # starting position, then flexible gaps
    budget = (n - minimum_span) // 2
    return comb(budget + dimension, dimension)


def check_direct(a, b):
    if len(a) != len(b):
        return False
    if not all(x % 2 == y % 2 for x, y in zip(a, b)):
        return False
    for i in range(len(a) - 1):
        x = a[i+1] - a[i]
        y = b[i+1] - b[i]
        if (x == 1) != (y == 1):
            return False
        if (x % 2) != (y % 2):
            return False
    return True


def all_maps(n):
    subsets = all_sets(n)
    return [tuple(zip(a, b)) for a in subsets for b in subsets
            if check_direct(a, b)]


def compose(s, t):
    """Ordinary partial-function composition: apply t, then s."""
    sd = dict(s)
    return tuple((x, sd[y]) for x, y in t if y in sd)


@lru_cache(None)
def mobius_basis(s):
    answer = {}
    r = len(s)
    for mask in range(1 << r):
        t = tuple(s[i] for i in range(r) if mask & (1 << i))
        answer[t] = (-1) ** (r - len(t))
    return answer


def product_in_algebra(s, t):
    result = defaultdict(int)
    for a, x in mobius_basis(s).items():
        for b, y in mobius_basis(t).items():
            result[compose(a, b)] += x * y
    return {key: value for key, value in result.items() if value}


def check_all():
    classes_by_n = {}
    dprev = [1]  # n=0: the empty map only
    for n in range(1, 12):
        groups = defaultdict(list)
        for s in all_sets(n):
            groups[signature(s)].append(s)
        assert len(groups) == (len({signature(s) for s in all_sets(n)}))
        assert len(groups) == 1 + sum(block_degree(n, p, ''.join(word)) > 0
                                     for r in range(1, n + 1)
                                     for word in product('1EO', repeat=r-1)
                                     for p in (0, 1))
        for key, values in groups.items():
            if key == ('empty',):
                continue
            p, w = key
            assert len(values) == block_degree(n, p, w), (n, p, w, values)
        d = len(groups)
        if n >= 3:
            assert d == sum(dprev[-3:]), (n, d, dprev)
        dprev.append(d)
        monoid_size = sum(len(values) ** 2 for values in groups.values())
        if n <= 7:
            direct_maps = all_maps(n)
            assert len(direct_maps) == monoid_size
            for s in direct_maps:
                a = tuple(x for x, _ in s)
                b = tuple(y for _, y in s)
                assert signature(a) == signature(b)
        classes_by_n[n] = (d, monoid_size)
    print('CLASSIFICATION_OK', classes_by_n)

    for n in range(1, 7):
        maps = all_maps(n)
        for s in maps:
            for t in maps:
                # The groupoid basis has matrix-unit multiplication.
                ans = product_in_algebra(s, t)
                if tuple(y for x, y in t) == tuple(x for x, y in s):
                    expected = mobius_basis(compose(s, t))
                else:
                    expected = {}
                assert ans == expected, (n, s, t, ans, expected)
        print('MOBIUS_PRODUCT_OK', n, len(maps), len(maps)**2)
    print('VERIFY_OK: matrix-block census and integral Mobius multiplication')


if __name__ == '__main__':
    check_all()
