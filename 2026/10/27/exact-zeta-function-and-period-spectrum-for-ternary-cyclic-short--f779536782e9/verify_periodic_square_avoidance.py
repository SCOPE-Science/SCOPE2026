#!/usr/bin/env python3
"""Exact stand-alone verification of periodic ternary short-square avoidance."""
from itertools import product
from math import gcd

ALPHABET = (0, 1, 2)


def no_square_at_end(w):
    return all(w[-2 * k:-k] != w[-k:] for k in (1, 2, 3) if len(w) >= 2 * k)


def square_free_short(w):
    return all(w[i:i + k] != w[i + k:i + 2 * k]
               for k in (1, 2, 3) for i in range(len(w) - 2 * k + 1))


def periodic_ok(w):
    n = len(w)
    return all(any(w[(i + t) % n] != w[(i + k + t) % n] for t in range(k))
               for i in range(n) for k in (1, 2, 3))


def adjacency():
    states = [w for w in product(ALPHABET, repeat=5) if square_free_short(w)]
    index = {w: i for i, w in enumerate(states)}
    n = len(states)
    matrix = [[0] * n for _ in range(n)]
    for i, w in enumerate(states):
        for letter in ALPHABET:
            v = w + (letter,)
            if no_square_at_end(v):
                matrix[i][index[v[1:]]] += 1
    return states, matrix


def matmul(a, b):
    n = len(a)
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for k, aik in enumerate(a[i]):
            if aik:
                for j, bkj in enumerate(b[k]):
                    if bkj:
                        c[i][j] += aik * bkj
    return c


def tr(a):
    return sum(a[i][i] for i in range(len(a)))


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def coeffs_newton(a):
    n = len(a)
    b = identity(n)
    power_traces = []
    coeffs = [1]
    for k in range(1, n + 1):
        b = matmul(b, a)
        power_traces.append(tr(b))
        total = sum(coeffs[k - j] * power_traces[j - 1] for j in range(1, k + 1))
        assert total % k == 0
        coeffs.append(-total // k)
    return coeffs, power_traces


def coeffs_faddeev(a):
    n = len(a)
    b = identity(n)
    coeffs = [1]
    for k in range(1, n + 1):
        c = matmul(a, b)
        assert tr(c) % k == 0
        ck = -tr(c) // k
        coeffs.append(ck)
        for i in range(n):
            c[i][i] += ck
        b = c
    return coeffs


def mul_poly(p, q):
    r = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i + j] += a * b
    return r


def expected_det_coeffs():
    # det(I-zA)=(1+z)(1-z-z^3)(1+z^2+z^3+z^4)
    #              (1-z^4+z^5+z^7-z^8)^2.
    factors = [[1, 1], [1, -1, 0, -1], [1, 0, 1, 1, 1],
               [1, 0, 0, 0, -1, 1, 0, 1, -1]]
    p = [1]
    for f in factors + [factors[-1]]:
        p = mul_poly(p, f)
    return p


def count_direct(n):
    return sum(periodic_ok(w) for w in product(ALPHABET, repeat=n))


def phi(n):
    return sum(gcd(j, n) == 1 for j in range(1, n + 1))


def necklace_count(c, n):
    return sum(phi(d) * c[n // d] for d in range(1, n + 1) if n % d == 0) // n


def direct_necklaces(n):
    seen = set()
    for w in product(ALPHABET, repeat=n):
        if periodic_ok(w):
            seen.add(min(w[i:] + w[:i] for i in range(n)))
    return len(seen)


def base_loops(states, a):
    idx = {w: i for i, w in enumerate(states)}
    v = (0, 1, 2, 1, 0)
    assert v in idx
    bases = ['0121', '012102', '01210120102', '0121012010212']
    for word in bases:
        t = tuple(map(int, word))
        assert periodic_ok(t)
        assert tuple(t[i % len(t)] for i in range(5)) == v
        for k in range(len(t)):
            source = tuple(t[(k + i) % len(t)] for i in range(5))
            target = tuple(t[(k + i + 1) % len(t)] for i in range(5))
            assert source in idx and target in idx
            assert no_square_at_end(source + (t[(k + 5) % len(t)],))
            assert a[idx[source]][idx[target]] == 1
        assert tuple(t[i % len(t)] for i in range(5)) == tuple(
            t[(len(t) + i) % len(t)] for i in range(5))
    return bases


def main():
    states, a = adjacency()
    assert len(states) == 30
    assert sum(map(sum, a)) == 42
    newton, t = coeffs_newton(a)
    faddeev = coeffs_faddeev(a)
    q = expected_det_coeffs()
    assert newton == faddeev == q + [0] * (len(states) - len(q) + 1)
    counts = [0] + t
    for n in range(1, 12):
        assert count_direct(n) == counts[n], (n, count_direct(n), counts[n])
    for n in range(1, 10):
        assert necklace_count(counts, n) == direct_necklaces(n)
    assert counts[1:16] == [0, 0, 0, 12, 0, 18, 0, 36, 0, 60,
                             66, 174, 78, 210, 210]
    assert all(counts[n] == 0 for n in (1, 2, 3, 5, 7, 9))
    assert all(counts[n] > 0 for n in range(4, 31) if n not in (5, 7, 9))
    bases = base_loops(states, a)
    print('TERNARY_PERIODIC_SHORT_SQUARE_PASS states=30 edges=42',
          'charpoly_methods=2 direct_lengths=1..11 necklaces=1..9',
          'loops=' + ','.join(str(len(w)) for w in bases))
    print('first_20_periodic_counts=', counts[1:21])
    print('det_coefficients=', q)


if __name__ == '__main__':
    main()
