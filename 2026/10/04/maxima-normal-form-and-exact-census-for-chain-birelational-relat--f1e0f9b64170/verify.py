#!/usr/bin/env python3
from itertools import combinations_with_replacement

def direct_ok(R, n):
    # Definition 3.1, first interaction condition.
    for v, w in R:
        for wp in range(w, n):
            if not any((vp, wp) in R for vp in range(v, n)):
                return False

    # Definition 3.1, second interaction condition.
    for v, w in R:
        for vp in range(v, n):
            if not any((vp, wp) in R for wp in range(w, n)):
                return False

    return True

def maxima(R, n):
    a = []
    b = []
    for i in range(n):
        row = [j for j in range(n) if (i, j) in R]
        a.append(max(row) if row else -1)
    for j in range(n):
        col = [i for i in range(n) if (i, j) in R]
        b.append(max(col) if col else -1)
    return tuple(a), tuple(b)

def maxima_ok(R, n):
    a, b = maxima(R, n)
    return (
        all(a[i] <= a[i + 1] for i in range(n - 1))
        and all(b[j] <= b[j + 1] for j in range(n - 1))
    )

direct_counts = []
for n in range(1, 5):
    count = 0
    for mask in range(1 << (n * n)):
        R = {
            (i, j)
            for i in range(n)
            for j in range(n)
            if (mask >> (i * n + j)) & 1
        }
        d = direct_ok(R, n)
        m = maxima_ok(R, n)
        assert d == m, (n, R, maxima(R, n), d, m)
        count += int(d)
    direct_counts.append(count)

assert direct_counts == [2, 9, 118, 4849]

def pair_admissible(a, b):
    for i, x in enumerate(a):
        if x >= 0 and i > b[x]:
            return False
    for j, x in enumerate(b):
        if x >= 0 and j > a[x]:
            return False
    return True

def pair_weight(a, b):
    n = len(a)
    allowed = {
        (i, j)
        for i in range(n)
        for j in range(n)
        if j <= a[i] and i <= b[j]
    }
    forced = {
        (i, a[i])
        for i in range(n)
        if a[i] >= 0
    } | {
        (b[j], j)
        for j in range(n)
        if b[j] >= 0
    }
    assert forced <= allowed
    return 1 << (len(allowed) - len(forced))

def formula_count(n):
    seqs = list(combinations_with_replacement(range(-1, n), n))
    total = 0
    for a in seqs:
        for b in seqs:
            if pair_admissible(a, b):
                total += pair_weight(a, b)
    return total

formula_counts = [formula_count(n) for n in range(1, 7)]
assert formula_counts == [2, 9, 118, 4849, 697066, 378458905]
assert formula_counts[:4] == direct_counts

print("DIRECT_COUNTS", direct_counts)
print("FORMULA_COUNTS", formula_counts)
print("VERIFY_OK")
