"""Finite independent checks for the cyclic three-variable representation formula.

Only Python's standard library is required; this is not an infinite proof.
"""
from math import comb, gcd


def phi(n):
    return sum(gcd(n, k) == 1 for k in range(1, n + 1))


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def formulas(m):
    if m % 4:
        return (0, 0)
    h = m // 2
    intersect = choose(m // 4, m // 8) ** 2 if m % 8 == 0 else 0
    total = choose(h, m // 4) ** 2 + choose(h, m // 4) - intersect
    e = sum(phi(m // d) * choose(d // 2, d // 4) ** 2
            for d in divisors(m) if d % 4 == 0)
    t = 2 * sum(phi(h // d) * choose(d, d // 2)
                for d in divisors(h) if d % 2 == 0)
    et = 2 * sum(phi(h // d) * choose(d // 2, d // 4) ** 2
                 for d in divisors(h) if d % 4 == 0)
    assert (e + t - et) % m == 0
    return total, (e + t - et) // m


def reps(a, m):
    # Exact cyclic convolution of the indicator of A twice, then dilated A once.
    v = [0] * m
    for x in a:
        for y in a:
            for z in a:
                v[(x + y + (m // 2) * z) % m] += 1
    return v


def test(m):
    from itertools import combinations
    h = m // 2
    universe = set(range(m))
    witnesses = set()
    predicted = set()
    for c in combinations(range(m), h):
        a = set(c)
        balance = m % 4 == 0 and sum(x % 2 == 0 for x in a) == m // 4
        translate = {(x + h) % m for x in a} == a
        if balance or translate:
            predicted.add(c)
        if reps(a, m) == reps(universe - a, m):
            witnesses.add(c)
    assert witnesses == predicted, (m, 'wrong classification')
    unseen = set(witnesses)
    orbits = 0
    while unseen:
        a = set(unseen.pop())
        orbit = {tuple(sorted((x + s) % m for x in a)) for s in range(m)}
        assert orbit <= witnesses
        unseen.difference_update(orbit)
        orbits += 1
    expected = formulas(m)
    assert (len(witnesses), orbits) == expected, (m, (len(witnesses), orbits), expected)
    print(f'm={m} labeled={len(witnesses)} shift_orbits={orbits}')


if __name__ == '__main__':
    for modulus in (2, 4, 6, 8, 10, 12, 16):
        test(modulus)
    print('VERIFY_OK')
