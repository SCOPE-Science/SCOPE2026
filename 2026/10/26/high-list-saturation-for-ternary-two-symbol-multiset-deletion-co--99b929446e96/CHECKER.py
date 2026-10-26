#!/usr/bin/env python3
"""Independent finite checks for a ternary two-trace multiset list code theorem.

A word is a triple of nonnegative multiplicities. A received pair y is
possible exactly when each coordinate of y does not exceed the corresponding
source coordinate. All checks use integer arithmetic.
"""
from collections import Counter
from itertools import combinations_with_replacement

TRACES = tuple(combinations_with_replacement(range(3), 2))


def signature(x):
    assert len(x) == 3 and min(x) >= 0
    return frozenset(y for y in TRACES
                     if all(x[j] >= y.count(j) for j in range(3)))


def all_words(n):
    return [(i, j, n-i-j) for i in range(n+1) for j in range(n-i+1)]


def lift_one(x):
    """Increase the lowest-index coordinate of maximal multiplicity."""
    i = min(j for j in range(3) if x[j] == max(x))
    y = list(x)
    y[i] += 1
    return tuple(y)


def lift(code, times):
    for _ in range(times):
        code = [lift_one(x) for x in code]
        assert len(code) == len(set(code))
    return code


def capacity_upper_bound(L):
    return (3*L + 12)//2


def construction(L, n):
    assert L >= 5 and n >= (L+1)//2 + 1
    if L == 5:
        # All fifteen length-four words except two whose received-pair
        # signatures jointly cover all six possible received pairs.
        excluded = {(2, 2, 0), (1, 1, 2)}
        return lift([x for x in all_words(4) if x not in excluded], n-4)
    code = []
    for i in range(3):
        v = [0]*3
        v[i] = n
        code.append(tuple(v))
        for j in range(3):
            if j != i:
                v = [0]*3
                v[i] = n-1
                v[j] = 1
                code.append(tuple(v))
        v = [1]*3
        v[i] = n-2
        code.append(tuple(v))
    d = L-4
    edges = ((0, 1, d//2), (0, 2, (d+1)//2), (1, 2, d//2))
    for i, j, t in edges:
        assert t <= n-3
        for a in range(2, t+2):
            v = [0]*3
            v[i] = a
            v[j] = n-a
            assert v[i] >= 2 and v[j] >= 2
            code.append(tuple(v))
    return code


def validate(L, n):
    code = construction(L, n)
    assert len(code) == len(set(code))
    assert all(sum(x) == n for x in code)
    counts = Counter(y for x in code for y in signature(x))
    assert max(counts.values()) <= L
    assert len(code) == capacity_upper_bound(L)
    if L % 2 == 0:
        assert all(counts[(i, i)] == L for i in range(3))
        assert sum(sum(a >= 2 for a in x) == 1 for x in code) == 12
        assert all(sum(a >= 2 for a in x) <= 2 for x in code)
    return len(code), max(counts.values())


def test():
    assert len(all_words(4)) == 15
    assert set(Counter(y for x in all_words(4) for y in signature(x)).values()) == {6}
    assert signature((2, 2, 0)) | signature((1, 1, 2)) == set(TRACES)
    checked = 0
    for n in range(4, 37):
        images = {x: lift_one(x) for x in all_words(n)}
        assert len(images) == len(set(images.values()))
        assert all(signature(x) == signature(y) for x, y in images.items())
        checked += len(images)
    for L in range(5, 71):
        n0 = (L+1)//2 + 1
        for n in (n0, n0+1, n0+2):
            validate(L, n)
    # Directly enumerate all subcodes at length four (2^15 possibilities)
    # to cross-check the computed capacity at the first nontrivial level.
    words = all_words(4)
    incidence = tuple(signature(x) for x in words)
    best = {L:0 for L in range(1, 8)}
    for mask in range(1 << len(words)):
        cnt = [0]*len(TRACES)
        total = 0
        for j, sig in enumerate(incidence):
            if (mask >> j) & 1:
                total += 1
                for i, pair in enumerate(TRACES):
                    if pair in sig: cnt[i] += 1
        peak = max(cnt)
        for L in range(max(peak, 1), 8):
            if total > best[L]: best[L] = total
    assert best == {1:3, 2:6, 3:9, 4:11, 5:13, 6:15, 7:15}
    print("PASS: lifting checked on", checked, "source words, n=4..36")
    print("PASS: 198 construction parameter cases, L=5..70")
    print("PASS: exhaustive length-four subcode census:", best)
    print("PASS: even-list equality structural checks")


if __name__ == "__main__":
    test()
