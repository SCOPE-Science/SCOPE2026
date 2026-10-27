"""Finite checks of the radical bound for signatures of cyclic permutations.

Run: python3 VERIFY.py. All computations use exact integers.
"""
from itertools import permutations
from math import gcd
from collections import Counter


def prime_powers(n):
    factors = []
    t = n
    p = 2
    while p * p <= t:
        if t % p == 0:
            a = 0
            while t % p == 0:
                a += 1
                t //= p
            factors.append((p, a))
        p += 1
    if t > 1:
        factors.append((t, 1))
    return factors


def mixed_radix_order(n):
    pp = prime_powers(n)

    def key(j):
        out = []
        for p, a in pp:
            v = j % (p ** a)
            for _ in range(a):
                out.append(v % p)
                v //= p
        return tuple(out)

    return sorted(range(n), key=key)


def has_same_signature(n, position, u):
    for j in range(n):
        initial = position[j]
        for t in range(1, n):
            if (position[(j+t) % n] - initial) * (
                    position[(j+u*t) % n] - initial) < 0:
                return False
    return True


def radical(n):
    prod = 1
    for p, _ in prime_powers(n):
        prod *= p
    return prod


def power_equivalences(n, position):
    return tuple(u for u in range(n) if gcd(u, n) == 1
                 and has_same_signature(n, position, u))


def main():
    tests = 0
    # Constructive sharpness, including nonsquarefree mixed-prime moduli.
    for n in range(2, 81):
        orbit_order = mixed_radix_order(n)
        pos = [None] * n
        for rank, j in enumerate(orbit_order):
            pos[j] = rank
        observed = power_equivalences(n, pos)
        predicted = tuple(u for u in range(n) if u % radical(n) == 1 % radical(n))
        assert observed == predicted, (n, observed, predicted)
        tests += 1

    # Independent exhaustive search over all oriented cycles through n=8.
    enumerated_cycles = 0
    for n in range(2, 9):
        histogram = Counter()
        for tail in permutations(range(1, n)):
            pos = [None] * n
            for rank, time in enumerate((0,) + tail):
                pos[time] = rank
            k = len(power_equivalences(n, pos))
            assert 1 <= k <= n // radical(n), (n, tail, k)
            histogram[k] += 1
            enumerated_cycles += 1
        assert max(histogram) == n // radical(n), (n, histogram)
        tests += sum(histogram.values())

    print('PASS:', tests, 'exact finite checks;', enumerated_cycles,
          'oriented cycles exhaustively classified (n=2..8)')


if __name__ == '__main__':
    main()
