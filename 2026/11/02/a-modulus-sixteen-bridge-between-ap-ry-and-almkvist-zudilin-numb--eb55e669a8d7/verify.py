"""Independent integer and binary checks for a modulus-16 Apéry/Almkvist--Zudilin identity.

Requires Python 3.9+ and only the standard library.  Finite tests corroborate,
but do not replace, the proof for all nonnegative integer indices.
"""
from itertools import groupby
from math import comb


def apery(n):
    return sum((comb(n, k) * comb(n + k, k)) ** 2 for k in range(n + 1))


def almkvist_original(n):
    return sum((-3) ** (n - 3 * k) * comb(n, 3 * k) * comb(n + k, k)
               * comb(2 * k, k) * comb(3 * k, k)
               for k in range(n // 3 + 1))


def almkvist_second(n):
    return sum((-27) ** (n - k) * comb(n + 3 * k, 4 * k)
               * comb(2 * k, k) ** 2 * comb(4 * k, 2 * k)
               for k in range(n + 1))


def runs(n):
    return sum(1 for _ in groupby(bin(n)[2:])) if n else 0


def h_parity(n):
    result = 0
    for j in range(n.bit_length() + 2):
        result ^= (n + 3 * (1 << j) >> (j + 2)) & 1
    return result


def witness(d):
    t = 0
    m = d
    while m % 2 == 0:
        m //= 2
        t += 1
    s = 1
    if m > 1:
        z = 2 % m
        while z != 1:
            z = (z * 2) % m
            s += 1
    r = max(1, t)
    a = (1 << r) * ((1 << s) - 1)
    n = 1 << (r + s + 4)
    assert a % d == 0 and a % 2 == 0
    assert runs(a) == 2 and runs(n) == 2 and runs(n + a) == 4
    assert (1 + 4*runs(n) + 8*n - (1 + 4*runs(n+a) + 8*(n+a))) % 16 == 8
    return n, a


def main():
    for n in range(257):
        a, b1, b2 = apery(n), almkvist_original(n), almkvist_second(n)
        assert b1 == b2, (n, b1, b2)
        assert (b1 - a - 8*n) % 16 == 0, n
        assert b1 % 16 == (1 + 4*runs(n) + 8*n) % 16, n
    for n in range(100000):
        assert (2*h_parity(n) - n - runs(n)) % 4 == 0, n
    for d in range(1, 513):
        witness(d)
    print('VERIFY_OK exact_integer_indices=257 binary_lemma_indices=100000 arbitrary_period_witnesses=512')


if __name__ == '__main__':
    main()
