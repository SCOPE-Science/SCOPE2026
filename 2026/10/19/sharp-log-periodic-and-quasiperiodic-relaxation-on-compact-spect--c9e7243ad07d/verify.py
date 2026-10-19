"""Independent numerical consistency checks for geometric spectral relaxation envelopes.

Run: python3 verify.py. Requires only Python's standard library.
All infinite-dimensional assertions in the accompanying proof are analytic.
"""
import math
import random


def level(r, a):
    return a * math.log(r) / (r - 1.0)


def peak_index(r, a, n):
    L = level(r, a)
    if not n >= L:
        raise ValueError('n below threshold')
    return max(0, math.floor(math.log(n / L) / math.log(r) + 1e-12))


def weight(r, a, n, k):
    return math.exp(-a * k * math.log(r) - n * r ** (-k))


def envelope(r, a, n):
    k = peak_index(r, a, n)
    return weight(r, a, n, k)


def profile(r, a, n):
    L = level(r, a)
    k = peak_index(r, a, n)
    u = n * (r ** (-k))
    return u ** a * math.exp(-u)


checks = 0
rng = random.Random(181417)
for r, a in [(2.0, 1.0), (1.5, 1.0), (3.0, 0.5), (2.0, 4.0),
             (1.25, 4.5), (5.0, 3.0), (1.0625, 0.37)]:
    L = level(r, a)
    low, high = L ** a * math.exp(-L), a ** a * math.exp(-a)
    assert 0 < low < high
    checks += 1
    for _ in range(101):
        n = rng.randint(max(1, math.ceil(L)), 1_000_000)
        k = peak_index(r, a, n)
        # The checked neighborhood contains the analytically identified optimum.
        # Global optimality beyond it is proved by the adjacent-ratio lemma.
        direct = max(weight(r, a, n, j) for j in range(max(0, k - 4), k + 5))
        assert abs(direct - envelope(r, a, n)) < 2e-14 * max(direct, 1e-200)
        scaled = n ** a * envelope(r, a, n)
        assert abs(scaled - profile(r, a, n)) < 1e-8 * max(1, scaled)
        assert low - 1e-10 <= scaled <= high + 1e-10
        checks += 3

# Sparse subsequences approach every single-ladder phase.
for r, a in [(2.0, 1.0), (1.5, 1.0), (3.0, 1.7)]:
    for phase in (0.0, 0.173, 0.421, 0.823):
        L = level(r, a)
        m = max(7, int(17 / math.log(r)))
        n = max(1, round(L * r ** (m + phase)))
        observed = n ** a * envelope(r, a, n)
        u = L * r ** phase
        desired = u ** a * math.exp(-u)
        assert abs(observed - desired) < 1.0e-4 * max(1, desired)
        checks += 1

# The two-ladder envelope is the maximum of the independently checked levels.
for a in (0.5, 1.0, 2.0):
    r1, r2 = 2.0, 1.5
    for _ in range(100):
        n = rng.randint(max(2, math.ceil(level(r1, a)), math.ceil(level(r2, a))), 500000)
        dual = max(envelope(r1, a, n), envelope(r2, a, n))
        scaled = n ** a * dual
        floor = max(level(r1, a) ** a * math.exp(-level(r1, a)),
                    level(r2, a) ** a * math.exp(-level(r2, a)))
        ceil = a ** a * math.exp(-a)
        assert floor - 1e-10 <= scaled <= ceil + 1e-10
        checks += 1

print(f'PASS {checks} finite consistency assertions; no infinite proof is claimed.')
