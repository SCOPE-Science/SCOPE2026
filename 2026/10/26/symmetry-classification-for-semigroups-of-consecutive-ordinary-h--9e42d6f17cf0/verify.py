#!/usr/bin/env python3
"""Exact arithmetic certificate for consecutive ordinary hexagonal semigroups."""
from math import gcd
from heapq import heappop, heappush

EXCEPTIONS = {2, 3, 6, 7, 8, 18}
CANDIDATES = {
    "AB": [2, 5, 8, 11],
    "AC": [2, 3, 4, 6, 8, 9, 12, 13, 18, 24, 28, 33, 38, 48, 78, 108],
    "BC": [4, 7, 10, 13],
}
SUCCESS = {
    "AB": {2},
    "AC": {2, 3, 6, 8, 18},
    "BC": {7},
}
OEIS_A069758 = [
    65, 377, 395, 797, 1589, 6029, 3347, 4571, 6035,
    10997, 10979, 12212, 19409, 47246, 24023, 29003,
    35357, 52112, 50603, 50411, 73049, 158207, 78155,
    90203, 102005, 144443, 138467, 131474, 183077
]

def hexagon(n):
    return n * (2 * n - 1)


def gluing_test(u, v, z):
    d = gcd(u, v)
    if d == 1:
        return False, (d, None, None)
    assert gcd(z, d) == 1
    x, y = u // d, v // d
    assert gcd(x, y) == 1
    s_min = (z * pow(x, -1, y)) % y
    t = (z - s_min * x) // y
    return t >= 0, (d, s_min, t)


def apery_invariants(a, b, c):
    # The distance to residue r modulo a equals its least semigroup element.
    w = [None] * a
    w[0] = 0
    todo = [(0, 0)]
    while todo:
        value, residue = heappop(todo)
        if w[residue] != value:
            continue
        for step in (b, c):
            nxt = (residue + step) % a
            newval = value + step
            if w[nxt] is None or newval < w[nxt]:
                w[nxt] = newval
                heappush(todo, (newval, nxt))
    assert all(v is not None for v in w)
    F = max(w) - a
    assert (2 * sum(w) - a * (a - 1)) % (2 * a) == 0
    genus = (2 * sum(w) - a * (a - 1)) // (2 * a)
    return F, genus


def main():
    found = set()
    found_by_pair = {pair: set() for pair in CANDIDATES}
    observed_candidates = {pair: [] for pair in CANDIDATES}
    oeis_checks = 0
    for n in range(2, 122):
        a, b, c = [hexagon(n + j) for j in range(3)]
        assert gcd(gcd(a, b), c) == 1
        assert gcd(a, b) == (3 if n % 3 == 2 else 1)
        assert gcd(b, c) == (3 if n % 3 == 1 else 1)
        dac = (2 if n % 2 == 0 else 1) * (3 if n % 3 == 0 else 1) * (5 if n % 5 == 3 else 1)
        assert gcd(a, c) == dac
        for pair, (u, v, z) in {
            "AB": (a, b, c), "AC": (a, c, b), "BC": (b, c, a)
        }.items():
            d = gcd(u, v)
            if d > 1 and a <= d * (c - a):
                observed_candidates[pair].append(n)
                success, (gd, s, t) = gluing_test(u, v, z)
                assert gd == d and (success == (n in SUCCESS[pair]))
                assert success == (s * (u // d) <= z)
                if success:
                    assert z == s * (u // d) + t * (v // d)
                    found_by_pair[pair].add(n)
                    found.add(n)
        # Apéry computation is independent of the three-generator gluing test.
        F, g = apery_invariants(a, b, c)
        assert (2 * g == F + 1) == (n in EXCEPTIONS), (n, F, g)
        if n <= 30:
            assert F == OEIS_A069758[n - 2], (n, F)
            oeis_checks += 1
    assert observed_candidates == CANDIDATES, observed_candidates
    assert found_by_pair == SUCCESS, found_by_pair
    assert found == EXCEPTIONS, found
    assert (2 * 122 * 122 - 241 * 122 - 180) > 0
    assert (4 * 122 - 239) > 0
    # Only corroboration of the symbolic gcd bounds; not an infinite proof.
    for n in range(122, 2001):
        a, b, c = [hexagon(n + j) for j in range(3)]
        assert a > 30 * (c - a)
        assert gcd(a, b) <= 30 and gcd(a, c) <= 30 and gcd(b, c) <= 30
    print("VERIFY_OK: 120 exact three-pair gluing cases, 120 independent Apery/genus computations,")
    print(f"{oeis_checks} OEIS Frobenius values, 24 reduced gcd-candidate pairs, and a symbolic cutoff check")
    print("SYMMETRIC_INDICES:", sorted(found))
    for n in sorted(found):
        a, b, c = [hexagon(n + j) for j in range(3)]
        print("INDEX", n, "GENS", a, b, c, "F,G", apery_invariants(a, b, c))


if __name__ == "__main__":
    main()
