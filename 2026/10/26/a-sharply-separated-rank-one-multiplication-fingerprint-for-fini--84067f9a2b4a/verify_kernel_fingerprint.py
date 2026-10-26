#!/usr/bin/env python3
"""Independent exact checks of rank-one product fingerprints for full transformation variants."""
from itertools import product, permutations
from math import factorial


def partitions(n, minimum=1):
    if n == 0:
        yield ()
    else:
        for part in range(minimum, n + 1):
            for rest in partitions(n - part, part):
                yield (part,) + rest


def representative(partition):
    # Standard function with consecutive kernel blocks and distinct image labels.
    return tuple(i for i, size in enumerate(partition) for _ in range(size))


def compose(f, g):
    # f after g
    return tuple(f[x] for x in g)


def image_rank(f):
    return len(set(f))


def fingerprint(partition, n):
    return sum(size ** n for size in partition)


def decode(fingerprint_value, n):
    remain = fingerprint_value
    result = []
    for m in range(n, 1, -1):
        count, remain = divmod(remain, m ** n)
        result.extend([m] * count)
    result.extend([1] * remain)
    assert sum(result) == n
    return tuple(sorted(result))


def direct_count(partition):
    n = sum(partition)
    a = representative(partition)
    count = 0
    for y in product(range(n), repeat=n):
        count += image_rank(compose(a, y)) == 1
    return count


def direct_outer_count(partition):
    n = sum(partition)
    a = representative(partition)
    count = 0
    for u in permutations(range(n)):
        for y in product(range(n), repeat=n):
            count += image_rank(compose(u, compose(a, y))) == 1
    return count


def test():
    direct = 0
    for n in range(1, 7):
        for lam in partitions(n):
            assert direct_count(lam) == fingerprint(lam, n), (n, lam)
            direct += 1
    outer = 0
    for n in range(1, 5):
        for lam in partitions(n):
            assert direct_outer_count(lam) == factorial(n) * fingerprint(lam, n)
            outer += 1
    total = 0
    for n in range(1, 33):
        arr = sorted((fingerprint(p, n), p) for p in partitions(n))
        assert len({a for a, _ in arr}) == len(arr)
        for value, lam in arr:
            assert decode(value, n) == lam
            total += 1
        if n >= 2:
            mindiff = min(arr[i + 1][0] - arr[i][0] for i in range(len(arr) - 1))
            assert mindiff == 2 ** n - 2, (n, mindiff)
    print(f'VERIFY_OK_KERNEL_FINGERPRINT direct_profiles={direct} direct_outer_profiles={outer} partition_decodes={total} sharp_gaps_n=2..32')


if __name__ == '__main__':
    test()
