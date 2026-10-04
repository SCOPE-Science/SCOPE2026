#!/usr/bin/env python3
from math import factorial, isqrt


def castelnuovo_count(a, b):
    g = a * b
    num = factorial(g)
    den = 1
    for i in range(a):
        num *= factorial(i)
        den *= factorial(b + i)
    assert num % den == 0
    return num // den


def cumulative_hooks(a, b, t):
    if t <= 0:
        return 0
    if t <= a:
        return t * (t + 1) // 2
    if t <= b:
        return a * t - a * (a - 1) // 2
    if t <= a + b - 1:
        s = a + b - 1 - t
        return a * b - s * (s + 1) // 2
    return a * b


def hook_product(a, b):
    out = 1
    for i in range(a):
        out *= factorial(b + i) // factorial(i)
    return out


comparisons = 0
for g in range(2, 301):
    pairs = [(a, g // a) for a in range(1, isqrt(g) + 1) if g % a == 0]
    counts = [castelnuovo_count(a, b) for a, b in pairs]
    assert all(counts[i] < counts[i + 1] for i in range(len(counts) - 1))

    a0, b0 = pairs[-1]
    D = (a0 - 1) * (b0 + 1)
    r = a0 - 1
    Ddual = (b0 - 1) * (a0 + 1)
    rdual = b0 - 1
    assert D + Ddual == 2 * g - 2
    assert rdual == g - D + r - 1

    for i, (a, b) in enumerate(pairs):
        assert factorial(g) // hook_product(a, b) == castelnuovo_count(a, b)
        assert castelnuovo_count(a, b) == castelnuovo_count(b, a)
        for c, e in pairs[i + 1:]:
            limit = max(a + b, c + e)
            for t in range(limit + 1):
                assert cumulative_hooks(c, e, t) >= cumulative_hooks(a, b, t)
            assert any(
                cumulative_hooks(c, e, t) > cumulative_hooks(a, b, t)
                for t in range(limit + 1)
            )
            comparisons += 1

print('VERIFY_OK')
print('genera_checked=299')
print(f'factor_pair_comparisons={comparisons}')
print('max_genus=300')
