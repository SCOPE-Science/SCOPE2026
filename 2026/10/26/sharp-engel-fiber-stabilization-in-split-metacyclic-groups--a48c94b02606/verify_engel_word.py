"""Independent finite checks of the stated metacyclic Engel-word formulas.
Run with Python 3; no third-party dependencies.
"""
from math import gcd
from collections import Counter


def order_mod(u, m):
    if m == 1:
        return 1
    z, o = u % m, 1
    while z != 1:
        z = z * u % m
        o += 1
    return o


def exact_fibers(m, h, u, k):
    ds = [gcd(m, (pow(u, j, m) - 1) ** k,
              (pow(u, j, m) - 1) ** (k - 1) * (pow(u, i, m) - 1))
          for j in range(h) for i in range(h)]
    return {c: m * sum(d for d in ds if c % d == 0) for c in range(m)}, ds


def mul(x, y, m, h, u):
    return ((x[0] + pow(u, x[1], m) * y[0]) % m,
            (x[1] + y[1]) % h)


def inv(x, m, h, u):
    return ((-pow(u, -x[1], m) * x[0]) % m, (-x[1]) % h)


def comm(x, y, m, h, u):
    return mul(mul(inv(x, m, h, u), inv(y, m, h, u), m, h, u),
               mul(x, y, m, h, u), m, h, u)


def brute(m, h, u, k):
    G = [(a, i) for a in range(m) for i in range(h)]
    out = Counter()
    for x in G:
        for y in G:
            z = x
            for _ in range(k):
                z = comm(z, y, m, h, u)
            out[z] += 1
    return out


def prime_powers(n):
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            yield p, e
        p += 1
    if n > 1:
        yield n, 1


def predicted_cutoff(m, u):
    candidates = []
    for p, e in prime_powers(m):
        t = order_mod(u % p, p)
        v = pow(u, t, p ** e) - 1
        s = 0
        if v == 0:
            s = e
        else:
            while v % p == 0:
                s += 1
                v //= p
        assert s >= 1
        candidates.append((e + s - 1) // s + int(t > 1))
    return max(candidates)


def eventual_d(m, h, u, j):
    ans = 1
    for p, e in prime_powers(m):
        if pow(u, j, p) == 1:
            ans *= p ** e
    return ans


def check_cutoffs():
    total = 0
    for m in range(2, 81):
        for u in range(1, m):
            if gcd(m, u) != 1:
                continue
            h = order_mod(u, m)
            K = predicted_cutoff(m, u)
            limit = [eventual_d(m, h, u, j) for j in range(h) for _ in range(h)]
            assert sorted(exact_fibers(m, h, u, K)[1]) == sorted(limit)
            if K > 1:
                ds = exact_fibers(m, h, u, K - 1)[1]
                assert sum(ds) < sum(limit)
            assert K <= 1 + max(e for _, e in prime_powers(m))
            for k in (1, K, K + 1):
                fibers, ds = exact_fibers(m, h, u, k)
                assert sum(fibers.values()) == (m * h) ** 2
                assert fibers[0] == m * sum(ds)
            total += 1
    return total


def check_bruteforce():
    samples = [(3, 2), (4, 3), (5, 4), (8, 3), (9, 2),
               (9, 4), (15, 4), (16, 5), (21, 2), (25, 6)]
    count = 0
    for m, u in samples:
        h = order_mod(u, m)
        for k in range(1, min(4, predicted_cutoff(m, u) + 1) + 1):
            brute_values = brute(m, h, u, k)
            formula, _ = exact_fibers(m, h, u, k)
            assert all(brute_values.get((c, 0), 0) == formula[c] for c in range(m))
            assert all(v[1] == 0 for v in brute_values)
            count += 1
    return count


def check_same_limit_different_cutoffs():
    m, h = 27, 18
    results = []
    for u, expected in [(2, 4), (8, 3)]:
        assert pow(u, h, m) == 1
        assert predicted_cutoff(m, u) == expected
        fibers, _ = exact_fibers(m, h, u, expected)
        assert fibers[0] * 27 == (m * h) ** 2 * 14
        results.append((u, expected, fibers[0]))
    assert results[0][2] == results[1][2]
    return results


if __name__ == '__main__':
    a = check_cutoffs()
    b = check_bruteforce()
    c = check_same_limit_different_cutoffs()
    print('VERIFY_OK: exact cutoff checked for', a, 'units modulo 2..80;',
          'exhaustive group-pair computations:', b, '; lift comparison:', c)
