"""Exact checks for variance-optimal ecological incidence networks.

Python 3 standard library only. Run: python VERIFY.py
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import comb


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def projective_plane(p):
    assert p in (2, 3, 5, 7)
    triples = set()
    for a, b, c in product(range(p), repeat=3):
        x = (a, b, c)
        if x == (0, 0, 0):
            continue
        first = next(y for y in x if y)
        inv = pow(first, -1, p)
        triples.add(tuple((y * inv) % p for y in x))
    points = sorted(triples)
    lines = list(points)
    rows = [frozenset(j for j, L in enumerate(lines)
                      if sum(x * y for x, y in zip(P, L)) % p == 0)
            for P in points]
    return rows


def switch(rows):
    for i in range(len(rows)):
        for j in range(i + 1, len(rows)):
            for a in sorted(rows[i] - rows[j]):
                for b in sorted(rows[j] - rows[i]):
                    other = list(rows)
                    other[i] = frozenset((rows[i] - {a}) | {b})
                    other[j] = frozenset((rows[j] - {b}) | {a})
                    if all(len(s) == len(rows[i]) for s in other):
                        return other
    raise AssertionError('No legal degree-preserving switch')


def pair_statistics(rows):
    v = len(rows)
    k = len(rows[0])
    assert all(len(s) == k for s in rows)
    assert all(sum(j in row for row in rows) == k for j in range(v))
    return Counter(len(a & b) for a, b in combinations(rows, 2))


def predicted_variance(rows, m):
    v = len(rows)
    k = len(rows[0])
    den = choose(v, m)
    a = Fraction(choose(v-k, m-k), den)
    e1 = v * a
    e2 = e1 + 2 * sum(
        Fraction(choose(v - (2*k-len(a1 & a2)), m - (2*k-len(a1 & a2))), den)
        for a1, a2 in combinations(rows, 2)
    )
    return e2-e1*e1


def direct_variance(rows, m):
    v = len(rows)
    counter = Counter()
    for dead in combinations(range(v), m):
        dead = set(dead)
        killed = sum(s <= dead for s in rows)
        counter[killed] += 1
    den = choose(v, m)
    mean = sum(Fraction(count * killed, den) for killed, count in counter.items())
    var = sum(Fraction(count * (killed * killed), den)
              for killed, count in counter.items()) - mean*mean
    return var, counter


def baseline(v, k, m):
    den = choose(v, m)
    a = Fraction(choose(v-k, m-k), den)
    b = Fraction(choose(v-(2*k-1), m-(2*k-1)), den)
    return v*a*(1-a) + v*(v-1)*(b-a*a)


def checks():
    count = 0
    for p in (2, 3, 5, 7):
        rows = projective_plane(p)
        v = p*p + p+1
        k = p+1
        assert len(rows) == v
        assert pair_statistics(rows) == {1: choose(v,2)}
        competitor = switch(rows)
        stats = pair_statistics(competitor)
        assert stats != {1: choose(v, 2)}
        assert sum(t*num for t, num in stats.items()) == choose(v, 2)
        for m in range(v+1):
            assert predicted_variance(rows, m) == baseline(v, k, m)
            assert predicted_variance(competitor, m) >= baseline(v, k, m)
            if 2*k-2 <= m <= v-2:
                assert predicted_variance(competitor, m) > baseline(v, k, m)
            count += 1
            if p in (2, 3):
                for example in (rows, competitor):
                    actual, _ = direct_variance(example, m)
                    assert actual == predicted_variance(example, m)
                    count += 1
            # Convexity check for the exact without-replacement joint-loss kernel.
            f = [Fraction(choose(v-2*k+t, v-m), choose(v, v-m))
                 for t in range(k+1)]
            for t in range(k-1):
                assert f[t+2]-2*f[t+1]+f[t] == Fraction(
                    choose(v-2*k+t, v-m-2), choose(v, v-m))
                count += 1
        if p in (2, 3):
            m = 2*k-2
            _, dist_projective = direct_variance(rows, m)
            _, dist_competitor = direct_variance(competitor, m)
            assert max(dist_projective) <= 1
            assert max(dist_competitor) >= 2
            print(f'prime={p}, v={v}, k={k}, m={m}, '
                  f'plane_var={baseline(v,k,m)}, '
                  f'competitor_var={predicted_variance(competitor,m)}, '
                  f'distributions={dict(sorted(dist_projective.items()))} '
                  f'vs {dict(sorted(dist_competitor.items()))}')
        print(f'prime={p}: all exact identities and strict bounds passed')
    print(f'PASS: {count} symbolic and exact-rational checks')


if __name__ == '__main__':
    checks()
