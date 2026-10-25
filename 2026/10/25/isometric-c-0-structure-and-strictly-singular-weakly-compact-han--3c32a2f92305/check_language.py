"""Finite exact checks of the derivative normal form for matched-block languages.

These finite checks are diagnostics, not a proof of the infinite-dimensional result.
Run: python3 check_language.py
"""
from itertools import product


def words(maxlen):
    return [''] + [''.join(bits) for n in range(1, maxlen + 1)
                   for bits in product('01', repeat=n)]


def q(prefix, suffix, S):
    return int(any(prefix + suffix == '0' * n + '1' * n for n in S))


def delta(j, v):
    return int(v == '1' * j)


def h(a, v, S):
    return int(any(v == '0' * k + '1' * (a + k)
                   for k in range(1, max(S) + 1) if a + k in S))


def q_normal_form(u, v, S):
    if not u:
        return h(0, v, S)
    if set(u) == {'0'}:
        a = len(u)
        return h(a, v, S) + int(a in S) * delta(a, v)
    if u[0] != '0' or '10' in u:
        return 0
    a = len(u) - len(u.lstrip('0'))
    b = len(u) - a
    return int(a in S and 1 <= b <= a) * delta(a - b, v)


def check(S):
    assert len(S) == len(set(S)) and all(i >= 1 for i in S)
    seen = set()
    W = words(2 * max(S) + 2)
    test_prefixes = words(max(S) + 2)
    count = 0
    for u in test_prefixes:
        for v in W:
            assert q(u, v, S) == q_normal_form(u, v, S), (S, u, v)
            count += 1
    for a in range(0, max(S) + 1):
        for v in W:
            if h(a, v, S):
                assert not v.startswith('1')
                assert v not in seen
                seen.add(v)
                count += 2
    for j in range(max(S) + 1):
        assert '1'*j not in seen
        count += 1
    return count


if __name__ == '__main__':
    # Finite analogues of the derivative formulas (finite S gives finite rank).
    # Restrict lengths so the exhaustive computations remain small.
    total = 0
    for S in ({1}, {2}, {1, 3}, {2, 3}):
        total += check(S)
    print(f'PASS: {total} exact prefix-suffix and disjointness assertions')
