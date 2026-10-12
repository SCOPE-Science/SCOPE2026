#!/usr/bin/env python3
from math import isqrt

T = 1000

def u(n):
    assert n >= 1
    return (n + isqrt(5*n*n)) // 2

def v(n):
    return u(n) + n

max_n = v(T)
U = {u(h) for h in range(1, max_n + 2) if u(h) <= max_n}
V = [v(k) for k in range(1, T + 2)]

def r(n):
    if n <= 0:
        return 0
    total = 0
    for x in V:
        if x >= n:
            break
        if n - x in U:
            total += 1
    return total

for t in range(1, T + 1):
    N = v(t)
    A = 0
    for j in range(1, t):
        if v(j) + v(t-j) == N:
            A += 1
        else:
            assert v(j) + v(t-j) == N - 1
    left = r(N - 1)
    right = r(N)
    assert left == A, (t, N, left, A)
    assert right == t - 1 - A, (t, N, right, t - 1 - A)
    assert left + right == t - 1

print(f"VERIFY_OK t_max={T} identities={T} rank_formulas={T} max_v={max_n}")
