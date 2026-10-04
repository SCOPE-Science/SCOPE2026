#!/usr/bin/env python3
from collections import defaultdict

def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return n == d
        d += 1
    return True

def oriented_solution_count(a, p, b):
    S = 2 ** (a + 1) - 1
    ys = range(-S, S + 1, 2)
    dp = {0: 1}
    for j in range(b + 1):
        w = p ** j
        nxt = defaultdict(int)
        # A remaining-magnitude cutoff keeps the state space modest.
        for s, c in dp.items():
            for y in ys:
                nxt[s + y * w] += c
        dp = nxt
    return dp.get(0, 0)

def unordered_count(a, p, b):
    c = oriented_solution_count(a, p, b)
    assert c % 2 == 0
    return c // 2

cases = []
for a in range(1, 4):
    for p in range(2 ** a + 1, 2 ** (a + 1)):
        if is_prime(p):
            for b in (1, 3, 5):
                cases.append((a, p, b))

for a, p, b in cases:
    got = unordered_count(a, p, b)
    want = 2 ** ((b - 1) // 2)
    assert got == want, (a, p, b, got, want)

# Scope sensitivity: this prime is below the strict upper-strip threshold.
assert unordered_count(3, 7, 3) == 6
print("VERIFY_OK")
