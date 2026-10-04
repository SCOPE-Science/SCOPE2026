#!/usr/bin/env python3
from itertools import product
from math import comb

def relation_from_thresholds(t):
    n = len(t)
    return {(i, j) for i in range(n) for j in range(n) if j >= t[i]}

def le_relation(n):
    return {(i, j) for i in range(n) for j in range(n) if i <= j}

def compose(A, B):
    return {(x, z) for (x, y) in A for (yy, z) in B if y == yy}

def reflexive(A, n):
    return all((i, i) in A for i in range(n))

def transitive(A):
    for x, y in A:
        for yy, z in A:
            if y == yy and (x, z) not in A:
                return False
    return True

def symbolic_ok(t):
    n = len(t)
    m = [min(t[i:]) for i in range(n)] + [n]
    if any(m[i] > i for i in range(n)):
        return False
    for q in set(t):
        if q < n and m[q] != q:
            return False
    return True

def direct_ok(t):
    n = len(t)
    R = relation_from_thresholds(t)
    le = le_relation(n)
    return reflexive(compose(le, R), n) and transitive(R)

# Bell numbers by the standard binomial recurrence.
def bell_numbers(N):
    B = [0] * (N + 1)
    B[0] = 1
    for n in range(N):
        B[n + 1] = sum(comb(n, k) * B[k] for k in range(n + 1))
    return B

# Direct exhaustive relation-level replay through n=6.
B = bell_numbers(13)
direct_counts = []
for n in range(1, 7):
    count = 0
    for t in product(range(n + 1), repeat=n):
        d = direct_ok(t)
        s = symbolic_ok(t)
        assert d == s, (n, t, d, s)
        count += int(d)
    expected = B[n + 1] - B[n]
    assert count == expected, (n, count, expected)
    direct_counts.append(count)

assert direct_counts == [1, 3, 10, 37, 151, 674]

# Fixed-point-set / composition formula.
def composition_count(n):
    total = 0
    # A fixed-point set is {0,n} plus an arbitrary subset of 1..n-1.
    for mask in range(1 << max(0, n - 1)):
        F = [0]
        for x in range(1, n):
            if (mask >> (x - 1)) & 1:
                F.append(x)
        F.append(n)
        s = len(F) - 1
        ways = 1
        for j in range(s):
            d = F[j + 1] - F[j]
            ways *= (s - j + 1) ** (d - 1)
        total += ways
    return total

for n in range(1, 13):
    got = composition_count(n)
    expected = B[n + 1] - B[n]
    assert got == expected, (n, got, expected)

print("COUNTS", direct_counts + [B[8] - B[7]])
print("VERIFY_OK")
