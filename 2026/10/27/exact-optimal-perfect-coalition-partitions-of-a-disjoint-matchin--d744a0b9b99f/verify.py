#!/usr/bin/env python3
"""Independent exhaustive test of the matching perfect-coalition census.

Uses the original vertex-neighborhood definition, not the proof's edge-type
classification. Runs with Python 3 standard library only.
"""
from collections import Counter
from math import factorial


def partitions(v):
    # Restricted-growth strings, one per unlabeled set partition.
    a = [0] * v
    def rec(i, high):
        if i == v:
            yield tuple(a)
        else:
            for j in range(high + 2):
                a[i] = j
                yield from rec(i + 1, max(high, j))
    yield from rec(1, 0)


def stirling(n, k):
    s = [[0] * (k + 1) for _ in range(n + 1)]
    s[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            s[i][j] = j * s[i - 1][j] + s[i - 1][j - 1]
    return s[n][k]


def formula(n):
    return (2 ** n // 4) * stirling(n, 2) + 3 * (2 ** n) * (stirling(n, 3) + stirling(n, 4))


def count(n):
    v = 2 * n
    adj = [0] * v
    for i in range(n):
        adj[2*i] = 1 << (2*i + 1)
        adj[2*i + 1] = 1 << (2*i)
    allbits = (1 << v) - 1
    # Compute domination, perfect domination and limited-crossing conditions
    dom, perfect, bounded = [], [], []
    for mask in range(1 << v):
        out = allbits ^ mask
        counts = [(adj[j] & mask).bit_count() for j in range(v) if out & (1 << j)]
        dom.append(all(c >= 1 for c in counts))
        perfect.append(all(c == 1 for c in counts))
        bounded.append(all(c <= 1 for c in counts))
    result = Counter()
    types = Counter()
    for a in partitions(v):
        k = max(a) + 1
        masks = [0] * k
        for j, color in enumerate(a):
            masks[color] |= 1 << j
        coalitions = set()
        for i in range(k):
            for j in range(i + 1, k):
                if not dom[masks[i]] and not dom[masks[j]] \
                   and bounded[masks[i]] and bounded[masks[j]] \
                   and perfect[masks[i] | masks[j]]:
                    coalitions.add((i, j))
        valid = True
        for i in range(k):
            if dom[masks[i]] and masks[i].bit_count() == 1:
                continue
            if not any(i in edge for edge in coalitions):
                valid = False
                break
        if valid:
            result[k] += 1
            if k == 4:
                degrees = tuple(sorted(sum(i in edge for edge in coalitions)
                                       for i in range(4)))
                assert degrees in {(1,1,1,1), (1,1,2,2), (2,2,2,2)}, degrees
                types[degrees] += 1
    return result, types


if __name__ == '__main__':
    for n in range(2, 6):
        counts, types = count(n)
        predicted = formula(n)
        assert counts[4] == predicted, (n, counts, predicted)
        expected = {
            (1,1,1,1): 3 * 2**n * stirling(n, 4),
            (1,1,2,2): 3 * 2**n * stirling(n, 3),
            (2,2,2,2): (2**n // 4) * stirling(n, 2)
        }
        assert dict(types) == {a:b for a,b in expected.items() if b}, (n,types,expected)
        assert all(k <= 4 for k in counts)
        print('n=', n, 'optimal=', counts[4], 'types=', dict(types))
    print('All direct vertex-level checks passed for 2 <= n <= 5.')
