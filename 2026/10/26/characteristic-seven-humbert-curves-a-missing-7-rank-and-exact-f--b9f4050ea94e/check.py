"""Exact finite-field checks for five-point harmonic quartets in characteristic seven.

No third-party packages are needed. This code tests finite cases; the theorem
for all algebraically closed fields rests on the separate geometric proof.
"""
from collections import Counter
from itertools import combinations
from math import comb

P = 7


def add(x, y):
    return ((x[0] + y[0]) % P, (x[1] + y[1]) % P)


def neg(x):
    return ((-x[0]) % P, (-x[1]) % P)


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    # u^2 = -1, irreducible over F_7.
    a, b = x
    c, d = y
    return ((a*c - b*d) % P, (a*d + b*c) % P)


def powf(x, n):
    ans = (1, 0)
    while n:
        if n & 1:
            ans = mul(ans, x)
        x = mul(x, x)
        n //= 2
    return ans


def divide(x, y, q):
    if y == (0, 0):
        raise ZeroDivisionError
    return mul(x, powf(y, q - 2))


INF = None
ZERO = (0, 0)
ONE = (1, 0)
ROOTS = {(2, 0), (4, 0), (6, 0)}


def cross_ratio(points, q):
    a, b, c, d = points
    # (a-c)(b-d)/((a-d)(b-c)), with correct limits for infinity.
    if a is INF:
        return divide(sub(b, d), sub(b, c), q)
    if b is INF:
        return divide(sub(a, c), sub(a, d), q)
    if c is INF:
        return divide(sub(b, d), sub(a, d), q)
    if d is INF:
        return divide(sub(a, c), sub(b, c), q)
    return divide(mul(sub(a, c), sub(b, d)),
                  mul(sub(a, d), sub(b, c)), q)


def count_harmonic(points, q):
    return sum(cross_ratio(s, q) in ROOTS
               for s in combinations(points, 4))


def check_field(size):
    if size == 7:
        elems = [(a, 0) for a in range(P)]
    elif size == 49:
        elems = [(a, b) for a in range(P) for b in range(P)]
    else:
        raise ValueError(size)
    # Verify Hasse polynomial sum binom(3,j)^2 t^j has roots -1,2,4.
    for z in elems:
        hz = ZERO
        for j in range(4):
            hz = add(hz, mul((comb(3, j)**2 % P, 0), powf(z, j)))
        assert (hz == ZERO) == (z in ROOTS)
    print('HASSE_POLYNOMIAL_OK', size)

    U = [z for z in elems if z != ZERO and z != ONE]
    counts = Counter()
    per_quartet = [0] * 5
    for a in U:
        for b in U:
            if b == a:
                continue
            points = [INF, ZERO, ONE, a, b]
            valid = []
            for i in range(5):
                quartet = [points[j] for j in range(5) if j != i]
                valid.append(cross_ratio(quartet, size) in ROOTS)
            for i, truth in enumerate(valid):
                per_quartet[i] += truth
            counts[sum(valid)] += 1
    assert sum(counts.values()) == (size-2)*(size-3)
    assert all(n == 3*(size-3) for n in per_quartet), per_quartet
    assert counts == Counter({3:20, 1:15*(size-7), 0:(size-7)*(size-13)})
    print('STRATA_COUNTS_OK', size, dict(sorted(counts.items())))
    print('INCIDENCE_COUNTS_OK', per_quartet)
    print('RANK_COUNTS_OK', {5-s: counts[s] for s in sorted(counts)})


if __name__ == '__main__':
    for q in (7, 49):
        check_field(q)
    print('CHECK_OK')
