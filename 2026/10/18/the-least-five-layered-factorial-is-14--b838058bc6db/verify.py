#!/usr/bin/env python3
"""Exact certificate for the least five-layered factorial."""
from math import factorial, isqrt

SETS = (
    (87178291200, 1245404160, 73382400, 443520, 2016),
    (43589145600, 29059430400, 14529715200, 1210809600, 107627520, 793800, 1176),
    (21794572800, 17435658240, 12454041600, 10897286400, 9686476800,
     8717829120, 7264857600, 242161920, 4633200, 5616),
    (7925299200, 6706022400, 6227020800, 5811886080, 5448643200,
     4843238400, 4358914560, 4151347200, 3962649600, 3632428800,
     3487131648, 3353011200, 3228825600, 3113510400, 2905943040,
     2724321600, 2641766400, 2490808320, 2421619200, 2235340800,
     2179457280, 2075673600, 1981324800, 581188608, 10108800, 41600, 160),
)


def divisors(n):
    ds = set()
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            ds.add(d)
            ds.add(n // d)
    return ds


def prime_factorization(n):
    factors = []
    x = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            factors.append((p, e))
        p += 1 if p == 2 else 2
    if x > 1:
        factors.append((x, 1))
    return factors


def sigma_from_factors(n):
    result = 1
    for p, a in prime_factorization(n):
        result *= (p ** (a + 1) - 1) // (p - 1)
    return result


def main():
    n13, n14 = factorial(13), factorial(14)
    d13, d14 = divisors(n13), divisors(n14)
    s13, s14 = sum(d13), sum(d14)
    assert n13 == 6227020800 and n14 == 87178291200
    assert len(d14) == 2592
    assert prime_factorization(n14) == [(2, 11), (3, 5), (5, 2), (7, 2), (11, 1), (13, 1)]
    assert s13 == 31044179712 and s14 == 442487616480
    assert s13 == sigma_from_factors(n13)
    assert s14 == sigma_from_factors(n14)
    assert s13 < 5 * n13
    assert s14 % 5 == 0
    target = s14 // 5
    assert target == 88497523296
    used = set()
    for i, group in enumerate(SETS, 1):
        assert len(group) == len(set(group)), (i, 'repeated within group')
        assert all(x in d14 for x in group), (i, 'not divisor')
        assert not (used & set(group)), (i, 'groups overlap')
        assert sum(group) == target, (i, sum(group), target)
        used.update(group)
    assert len(used) == 49
    remaining = d14 - used
    assert len(remaining) == 2543
    assert sum(remaining) == target
    assert set.union(*(set(x) for x in SETS), remaining) == d14
    print('VERIFIED: 13! cannot be five-layered; 14! has five disjoint equal-sum divisor groups.')
    print('sigma(13!) =', s13, 'sigma(14!) =', s14, 'target =', target)
    print('group_sizes =', [len(x) for x in SETS] + [len(remaining)])


if __name__ == '__main__':
    main()
