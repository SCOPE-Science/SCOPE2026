"""Finite checks for semantic support maps of single-agent S5 announcements.

Run with Python 3: python checker.py. No third-party packages.
"""
from itertools import product
from math import comb, factorial


def all_maps(m):
    n = 1 << m
    options = [tuple(sub for sub in range(n) if sub & ~s == 0) for s in range(n)]
    for choices in product(*options):
        yield choices


def ending(f, start):
    s = start
    rounds = 0
    while f[s] != s:
        assert f[s] & ~s == 0
        assert rounds < len(f)
        s = f[s]
        rounds += 1
    return s, rounds


def modal_support_check(f, m):
    """Directly evaluate a propositional modal formula from its DNF of support tests."""
    for s in range(1 << m):
        worlds = tuple(t for t in range(m) if (s >> t) & 1)
        # chi_R: conjunction of K-not-tau for absent types and not-K-not-tau for present types.
        support_tests = {}
        for r in range(1 << m):
            ok = True
            for t in range(m):
                knows_not_type = all(v != t for v in worlds)
                required = not bool((r >> t) & 1)
                if knows_not_type != required:
                    ok = False
                    break
            support_tests[r] = ok
        for t in worlds:
            phi = any(support_tests[r] and ((f[r] >> t) & 1)
                      for r in range(1 << m))
            assert phi == bool((f[s] >> t) & 1), (m, f, s, t)


def check(m):
    expected = 1 << (m * (1 << (m - 1)))
    expected_universal = 1
    for j in range(1, m + 1):
        expected_universal *= (2**j - 1)**comb(m, j)
    expected_maxround = factorial(m) * 2**(m * (1 << (m - 1)) - m * (m + 1) // 2)
    actual = universal = maxround = 0
    endpoint_counts = [0] * (1 << m)
    for f in all_maps(m):
        actual += 1
        nonzero_fixed = [s for s in range(1, 1 << m) if f[s] == s]
        if not nonzero_fixed:
            universal += 1
        for s in range(1, 1 << m):
            end, steps = ending(f, s)
            assert steps <= s.bit_count()
            if end == 0:
                endpoint_counts[s] += 1
        if ending(f, (1 << m) - 1)[1] == m:
            maxround += 1
        if actual <= 32 or actual % 257 == 0:
            modal_support_check(f, m)
    assert actual == expected, (actual, expected)
    assert universal == expected_universal, (universal, expected_universal)
    assert maxround == expected_maxround, (maxround, expected_maxround)
    assert endpoint_counts[0] == 0
    assert all(x * 2 == actual for x in endpoint_counts[1:]), endpoint_counts
    print(f'm={m}: maps={actual}, universal_extinguish={universal}, '
          f'maximal_full_support_rounds={maxround}; all nonempty starts extinct in exactly half')


if __name__ == '__main__':
    for m in (1, 2, 3):
        check(m)
    print('ALL_CHECKS_OK')
