#!/usr/bin/env python3
"""Exact orbit coefficients and independent finite transformation-pair census.

Only Python's standard library is required. Run: python verify.py
"""
from itertools import permutations, product
from collections import Counter


def convolution(a, b, cap):
    out = [0] * (cap + 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b[:cap + 1 - i]):
                out[i + j] += ai * bj
    return out


def multisets(f, cap):
    out = [1] + [0] * cap
    for degree in range(1, cap + 1):
        for _ in range(f[degree]):
            factor = [int(j % degree == 0) for j in range(cap + 1)]
            out = convolution(out, factor, cap)
    return out


def prediction(cap):
    a = [0] + [1] * cap
    b = [0] * (cap + 1)
    for left in range(cap + 1):
        for right in range(left, cap + 1):
            if 2 + left + right <= cap:
                b[2 + left + right] += 1
    root_no = convolution(a, multisets(a, cap), cap)
    root_all = convolution(a, multisets([x + y for x, y in zip(a, b)], cap), cap)
    no = multisets(root_no, cap)
    all_ = multisets(root_all, cap)
    plane = multisets([0] + list(range(1, cap + 1)), cap)
    parts = multisets(a, cap)
    return [all_[n] - no[n] for n in range(cap + 1)], [plane[n] - parts[n] for n in range(cap + 1)]


def compose(f, g):
    return tuple(f[g[i]] for i in range(len(f)))


def canonical_pair(t, e, group, inverses):
    n = len(t)
    return min(
        (tuple(p[t[inv[i]]] for i in range(n)), tuple(p[e[inv[i]]] for i in range(n)))
        for p, inv in zip(group, inverses)
    )


def enumerate_classes(n, independently_check_essential=False):
    identity = tuple(range(n))
    transformations = list(product(range(n), repeat=n))
    eligible_t = [t for t in transformations if compose(compose(t, t), t) == t]
    eligible_e = [e for e in transformations if compose(e, e) == e]
    group = list(permutations(range(n)))
    inverses = [tuple(p.index(i) for i in range(n)) for p in group]
    orbit_3 = set()
    orbit_2 = set()
    all_permissible = []
    possible_roots = set()
    for t in eligible_t:
        t2 = compose(t, t)
        for e in eligible_e:
            if compose(t, e) != e or compose(e, t) != e:
                continue
            if independently_check_essential:
                all_permissible.append((t, e))
            if t2 != t:
                orbit_3.add(canonical_pair(t, e, group, inverses))
                possible_roots.add((t2, e))
            elif t != e:
                non_red = [i for i in range(n) if t[i] == i and e[i] != i]
                red_counts = Counter(e[i] for i in non_red)
                predicted_essential = max(red_counts.values(), default=0) <= 1
                if predicted_essential:
                    orbit_2.add(canonical_pair(t, e, group, inverses))
    if independently_check_essential:
        # Independent characterization via actual square roots; do not rely on
        # the non-red-blue-root criterion for this check.
        assert all(compose(t, t) == t or (compose(t, t), e) in possible_roots
                   for t, e in all_permissible if compose(t, t) != t)
        for t, e in all_permissible:
            if compose(t, t) != t or t == e:
                continue
            fixed_outside = [i for i in range(n) if t[i] == i and e[i] != i]
            counts = Counter(e[i] for i in fixed_outside)
            predicted = max(counts.values(), default=0) <= 1
            actual = (t, e) not in possible_roots
            assert predicted == actual, (n, t, e, predicted, actual)
    return len(orbit_3), len(orbit_2)


def main():
    rank3, rank2 = prediction(12)
    expected = {3: (1, 3), 4: (4, 8), 5: (15, 17), 6: (46, 37)}
    for n, pair in expected.items():
        got = enumerate_classes(n, independently_check_essential=(n <= 5))
        assert got == pair == (rank3[n], rank2[n]), (n, got, pair)
        print('n', n, 'r3', got[0], 'essential_r2', got[1])
    for n in range(5, 13):
        print('minimal_rank', n, 3 + rank3[n] + rank2[n])
    assert [3 + rank3[n] + rank2[n] for n in range(5, 11)] == [35, 86, 207, 503, 1206, 2880]
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
