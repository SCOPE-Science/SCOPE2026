"""Independent finite checks for the deterministic majority-three ring theorem.

Run with Python 3.9+: python verify.py
All reported exhaustive checks are finite; the proof of the infinite claims is in RESULT.md.
"""
from itertools import product
from collections import Counter
from math import exp


def step(x):
    n = len(x)
    return tuple((x[(i - 1) % n] + x[i] + x[(i + 1) % n]) >= 2
                 for i in range(n))


def first_periodic_entry(x):
    seen = {}
    state = x
    for t in range(len(x) + 3):
        if state in seen:
            return seen[state], t - seen[state]
        seen[state] = t
        state = step(state)
    raise AssertionError('no entry within finite bound')


def run_prediction(x):
    n = len(x)
    zeros = [i for i in range(n) if x[i] == x[(i + 1) % n]]
    if not zeros:
        return 0, 2
    gaps = [((zeros[(j + 1) % len(zeros)] - zeros[j]) % n) or n
            for j in range(len(zeros))]
    return max((gap - 1) // 2 for gap in gaps), 1


def matmul(a, b):
    m = len(a)
    out = [[0] * m for _ in range(m)]
    for i in range(m):
        for k in range(m):
            if a[i][k] == 0:
                continue
            for j in range(m):
                out[i][j] += a[i][k] * b[k][j]
    return out


def trace_power(length_cap, ring_size, sign):
    dim = length_cap + 1
    a = [[0] * dim for _ in range(dim)]
    for j in range(dim):
        a[j][0] = 1
        if j < length_cap:
            a[j][j + 1] = sign
    out = [[int(i == j) for j in range(dim)] for i in range(dim)]
    n = ring_size
    while n:
        if n & 1:
            out = matmul(out, a)
        n //= 2
        if n:
            a = matmul(a, a)
    return sum(out[i][i] for i in range(dim))


def cdf_numerator(n, t):
    cap = 2 * t + 1
    return (trace_power(cap, n, 1) + trace_power(cap, n, -1)
            + (2 if n % 2 == 0 else 0))


total = 0
for n in range(3, 16):
    observed = Counter()
    for x in product((0, 1), repeat=n):
        t, period = first_periodic_entry(x)
        t2, period2 = run_prediction(x)
        assert (t, period) == (t2, period2), (n, x, t, period, t2, period2)
        observed[t] += 1
        total += 1
    for t in range(n):
        assert cdf_numerator(n, t) == sum(v for k, v in observed.items() if k <= t), (n, t)
    assert sum(observed.values()) == 2 ** n
    print('n=%2d exact first-entry histogram: %s' % (n, dict(sorted(observed.items()))))
print('exhaustive_spin_configurations=%d' % total)

for n, t in [(256, 3), (512, 4), (1024, 4), (1024, 5), (2048, 5)]:
    exact = cdf_numerator(n, t) / 2 ** n
    lam = n / 2 ** (2 * t + 3)
    print('large_n n=%d t=%d exact_cdf=%.9f poisson=%.9f lambda=%.6f' %
          (n, t, exact, exp(-lam), lam))
print('MAJORITY232_TRANSIENT_VERIFY_OK')
