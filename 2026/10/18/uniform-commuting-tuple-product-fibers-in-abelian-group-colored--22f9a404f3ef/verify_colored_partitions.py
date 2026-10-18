#!/usr/bin/env python3
"""Independent finite checks of commuting colored ordered-partition fiber laws.
Python 3 standard library only. Run: python3 verify_colored_partitions.py
"""
from collections import Counter
from itertools import product
from math import comb, factorial


def ordered_partitions(n):
    for assignment in product(range(n), repeat=n):
        if set(assignment) != set(range(max(assignment) + 1)):
            continue
        yield tuple(frozenset(i + 1 for i, a in enumerate(assignment) if a == j)
                    for j in range(max(assignment) + 1))


def elements(n, group):
    for blocks in ordered_partitions(n):
        for colors in product(group, repeat=len(blocks)):
            yield tuple(zip(blocks, colors))


def cyclic(k):
    return tuple(range(k)), lambda a, b: (a + b) % k


def klein_four():
    return ((0, 0), (0, 1), (1, 0), (1, 1)), lambda a, b: ((a[0]+b[0])%2, (a[1]+b[1])%2)


def multiply(A, B, mul):
    return tuple((a & b, mul(x, y)) for a, x in A for b, y in B if a & b)


def expected_weights(r, g, m):
    """Polynomial in r block-count variables; exponent tuples -> coefficients."""
    result = Counter({(1,) * r: g ** (r-1)})
    for _ in range(m-1):
        following = Counter()
        for exponent, count in result.items():
            for mask in range(1, 1 << r):
                active = tuple(int(bool(mask & (1 << i))) for i in range(r))
                factor = g ** (sum(active)-1)
                exponent_new = tuple(exponent[i]+active[i] for i in range(r))
                following[exponent_new] += count*factor
        result = following
    return result


def test(n, group, mul, r):
    objects = tuple(elements(n, group))
    g = len(group)
    fibers = {}
    for tup in product(objects, repeat=r):
        if not all(multiply(tup[i], tup[j], mul) == multiply(tup[j], tup[i], mul)
                   for i in range(r) for j in range(i+1, r)):
            continue
        result = tup[0]
        for factor in tup[1:]:
            result = multiply(result, factor, mul)
        if result not in fibers:
            fibers[result] = Counter()
        fibers[result][tuple(len(f) for f in tup)] += 1
    assert len(fibers) == len(objects), (n, g, r, len(fibers), len(objects))
    for target, weights in fibers.items():
        expected = expected_weights(r, g, len(target))
        assert weights == expected, (n, g, r, target, weights, expected)
    total = sum(sum(w.values()) for w in fibers.values())
    from_stirling = 0
    # Number of ordered unlabeled partitions into m blocks: m! S(n,m).
    # Compute the values S(n,m) directly from the standard recurrence.
    stirling = [[0]*(n+1) for _ in range(n+1)]
    stirling[0][0] = 1
    for a in range(1, n+1):
        for m in range(1, a+1):
            stirling[a][m] = stirling[a-1][m-1]+m*stirling[a-1][m]
    for m in range(1, n+1):
        from_stirling += (factorial(m)*stirling[n][m]*g**r
                          *(((g+1)**r-1)**(m-1)))
    assert total == from_stirling, (n, g, r, total, from_stirling)
    print(f'n={n} |G|={g} r={r}: {len(objects)} objects; {total} commuting tuples; all prescribed-product weighted fibers match')


def main():
    for g in (1, 2, 3):
        group, op = cyclic(g)
        for n in (1, 2, 3):
            test(n, group, op, 2)
    for g in (1, 2, 3):
        group, op = cyclic(g)
        for n in (1, 2):
            test(n, group, op, 3)
    c4, op4 = cyclic(4)
    v4, opv = klein_four()
    test(2, c4, op4, 2)
    test(2, v4, opv, 2)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
