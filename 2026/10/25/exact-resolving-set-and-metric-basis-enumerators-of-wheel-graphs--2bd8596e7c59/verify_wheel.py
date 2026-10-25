#!/usr/bin/env python3
"""Exact small-wheel resolution census and large-parameter integer identities."""
from collections import deque, Counter
from fractions import Fraction
from math import comb


def choose(a, b):
    return comb(a, b) if 0 <= b <= a else 0


def coefficient(m, k):
    """Exact coefficient in the wheel rim-resolving polynomial."""
    if k < 3 or k > m:
        return 0
    total = Fraction()
    for j in range(k // 2 + 1):
        placements = Fraction(k, k - j) * choose(k - j, j)
        d = m - k - 2 * j
        total += placements * (choose(k - j, d) + j * choose(k - j, d - 1))
    count = Fraction(m, k) * total
    assert count.denominator == 1, (m, k, count)
    return count.numerator


def predicted_bases(m):
    if m % 5 == 4:
        s = (m + 1) // 5
        value = Fraction(m) * (1 + Fraction(s * s, 2) + Fraction(s * (s*s-1)*(s+10), 24))
    elif m % 5 == 0:
        s = m // 5
        value = Fraction(5, 2) * (2 + s * s * (s + 1))
    elif m % 5 == 1:
        value = Fraction(m)
    elif m % 5 == 2:
        s = (m - 2) // 5
        value = Fraction(m) * (1 + Fraction(s*(s+1)*(s+5), 6))
    else:
        s = (m - 3) // 5
        value = Fraction(m * s)
    assert value.denominator == 1
    return value.numerator


def distances(m):
    """All-pairs graph distances from BFS, without using cyclic-gap rules."""
    adj = [set() for _ in range(m + 1)]
    hub = m
    for i in range(m):
        for j in ((i + 1) % m, hub):
            adj[i].add(j)
            adj[j].add(i)
    out = []
    for source in range(m + 1):
        dist = [-1] * (m + 1)
        dist[source] = 0
        q = deque([source])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] < 0:
                    dist[v] = dist[u] + 1
                    q.append(v)
        assert all(d >= 0 for d in dist)
        out.append(dist)
    return out


def original_resolves(dist, selected):
    columns = [i for i in range(len(dist)) if selected >> i & 1]
    codes = {tuple(dist[v][landmark] for landmark in columns) for v in range(len(dist))}
    return len(codes) == len(dist)


def gap_test(m, selected):
    ones = [i for i in range(m) if selected >> i & 1]
    k = len(ones)
    if k < 3:
        return False
    gaps = [(ones[(i+1)%k]-ones[i]-1) % m for i in range(k)]
    return (max(gaps) <= 3 and gaps.count(3) <= 1
            and all(not (gaps[i] >= 2 and gaps[(i+1)%k] >= 2) for i in range(k)))


def main():
    checked = 0
    for m in range(7, 17):
        d = distances(m)
        counts = Counter()
        for selected in range(1 << m):
            valid = original_resolves(d, selected)
            assert valid == gap_test(m, selected), (m, selected, valid)
            # Adding the hub must not change whether rim landmarks resolve.
            assert valid == original_resolves(d, selected | (1 << m)), (m, selected)
            if valid:
                counts[selected.bit_count()] += 1
            checked += 1
        assert counts == Counter({k: coefficient(m, k) for k in range(3, m+1) if coefficient(m, k)})
        k0 = 2 * (m+1) // 5
        assert min(counts) == k0
        assert counts[k0] == predicted_bases(m)
        print('m={} subsets={} metric_dimension={} bases={} total_rim_resolvers={}'.format(
            m, 1 << m, k0, counts[k0], sum(counts.values())))
    for m in range(7, 201):
        k0 = 2*(m+1)//5
        assert coefficient(m, k0) == predicted_bases(m), m
        assert all(coefficient(m, k) == 0 for k in range(3, k0))
        assert coefficient(m, m) == 1
        assert coefficient(m, m - 1) == m
        assert coefficient(m, m - 2) == choose(m, 2)
        assert coefficient(m, m - 3) == choose(m, 3)
    print('PASS: {} exhaustively tested rim subsets, both hub choices, exact coefficients and base counts; formula identities through m=200.'.format(checked))


if __name__ == '__main__':
    main()
