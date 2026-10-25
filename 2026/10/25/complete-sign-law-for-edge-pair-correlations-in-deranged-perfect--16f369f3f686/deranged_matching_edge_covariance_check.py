"""Exact arithmetic checks for edge-pair covariances in deranged perfect matchings.

Standalone Python >=3.9; no external modules.
"""
from fractions import Fraction
from itertools import combinations
from functools import lru_cache


def deranged_numbers(limit):
    result = [1, 0]
    for m in range(2, limit + 1):
        result.append(2 * (m - 1) * (result[m - 1] + result[m - 2]))
    return result


@lru_cache(None)
def perfect_matchings(vertices):
    if not vertices:
        return ((),)
    a, *others = vertices
    out = []
    for j, b in enumerate(others):
        remain = tuple(others[:j] + others[j + 1:])
        for tail in perfect_matchings(remain):
            out.append(((a, b),) + tail)
    return tuple(out)


def exact_covariance(n, kind, d):
    p = Fraction(1, 2 * (n - 1))
    c = Fraction(2 * (n - 1) * d[n - 2], d[n])
    if kind == 'meeting':
        return -p * p
    if kind == 2:
        return Fraction(d[n - 2], d[n]) - p * p
    if kind == 3:
        return p * Fraction(1 - c, 2 * (n - 2)) - p * p
    if kind == 4:
        return p * (n - 3 + c) / (2 * (n - 2) * (n - 3)) - p * p
    raise ValueError(kind)


def test_enumeration(n):
    d = deranged_numbers(n)
    edges = tuple((a, b) for a in range(2*n) for b in range(a+1, 2*n)
                  if a//2 != b//2)
    observed = {e: 0 for e in edges}
    observed_pairs = {}
    count = 0
    for m in perfect_matchings(tuple(range(2*n))):
        if any(a//2 == b//2 for a, b in m):
            continue
        count += 1
        for e in m:
            observed[e] += 1
        for x, y in combinations(sorted(m), 2):
            observed_pairs[x, y] = observed_pairs.get((x, y), 0) + 1
    checks = 0
    assert count == d[n], (n, count, d[n])
    checks += 1
    for e in edges:
        assert Fraction(observed[e], count) == Fraction(1, 2*(n-1))
        checks += 1
    for i, e in enumerate(edges):
        for f in edges[i+1:]:
            if set(e) & set(f):
                kind = 'meeting'
            else:
                kind = len({v//2 for v in (*e, *f)})
                assert kind in (2, 3, 4)
                checks += 1
            actual = Fraction(observed_pairs.get(tuple(sorted((e, f))), 0), count)
            actual -= Fraction(observed[e] * observed[f], count*count)
            expected = exact_covariance(n, kind, d)
            assert actual == expected, (n, e, f, kind, actual, expected)
            checks += 1
            sign_expected = (-1 if kind == 'meeting' or
                             (kind == 2 and n not in (2,4)) else 1)
            assert actual * sign_expected > 0, (n, kind, actual)
            checks += 1
    return count, checks


def test_recurrence():
    d = deranged_numbers(300)
    checks = 0
    for n in range(2, 301):
        assert d[n] == 2*(n-1)*(d[n-1]+d[n-2])
        checks += 1
        p = Fraction(1, 2*(n-1))
        c = Fraction(2*(n-1)*d[n-2], d[n])
        assert Fraction(d[n-2], d[n]) - p*p == p*(c-p)
        checks += 1
        assert (c < Fraction(1, n-1)) == (n >= 3)
        checks += 1
        if n >= 3:
            assert exact_covariance(n, 3, d) > 0
            checks += 1
        if n >= 4:
            assert (Fraction(d[n-2], d[n])-p*p ==
                    Fraction((n-3)*d[n-4]-d[n-3], (n-1)*d[n]))
            checks += 1
            assert exact_covariance(n, 4, d) > 0
            checks += 1
    return checks


if __name__ == '__main__':
    total = test_recurrence()
    for n in range(2, 8):
        count, checks = test_enumeration(n)
        total += checks
        print('n=%d matchings=%d exact assertions=%d' % (n, count, checks))
    print('TOTAL exact assertions:', total)
