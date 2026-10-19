"""Reproducible finite checks of the Markov-hole escape variance theorem.

Requires Python 3 and NumPy. Finite checks corroborate; they do not prove
infinite-n limits, the uniform root estimate, or the Fine-Wilf step.
"""
import math
import numpy as np


def mobius(k):
    original = k
    sign = 1
    p = 2
    while p * p <= k:
        if k % p == 0:
            k //= p
            if k % p == 0:
                return 0
            sign = -sign
        while k % p == 0:
            k //= p
        p += 1
    if k > 1:
        sign = -sign
    return sign


def aperiodic_count(base, period):
    return sum(mobius(d) * base ** (period // d)
               for d in range(1, period + 1) if period % d == 0)


def constant(base, cutoff=60):
    return sum(aperiodic_count(base, p) / base ** (2 * p)
               for p in range(1, cutoff + 1))


def hole_rates(base, n):
    count = base ** n
    words = np.arange(count, dtype=np.int64)
    overlaps = [(words // (base ** p) == words % (base ** (n - p)))
                for p in range(1, n)]
    h = 1 / count
    low = np.full(count, h / 2)
    high = np.full(count, 2 * h)
    for _ in range(44):
        a = (low + high) / 2
        lam = 1 - a
        den = lam ** (n - 1)
        for p in range(1, n):
            den += base ** (-p) * overlaps[p - 1] * lam ** (n - p - 1)
        is_low = a * den < h
        low = np.where(is_low, a, low)
        high = np.where(is_low, high, a)
    rates = -np.log1p(-(low + high) / 2)
    return rates


def actual_pf_rate(base, n, word):
    # Independent de Bruijn transition construction; length-(n-1) states.
    size = base ** (n - 1)
    mat = np.zeros((size, size), dtype=float)
    for state in range(size):
        for digit in range(base):
            full = base * state + digit
            if full != word:
                next_state = full % size
                mat[state, next_state] += 1 / base
    root = max(abs(z) for z in np.linalg.eigvals(mat))
    return -math.log(root)


def check():
    for base, max_p in [(2, 9), (3, 7)]:
        for p in range(1, max_p + 1):
            count = 0
            for k in range(base ** p):
                digs = []
                x = k
                for _ in range(p):
                    digs.append(x % base)
                    x //= base
                if all(any(digs[i] != digs[i % d] for i in range(p))
                       for d in range(1, p) if p % d == 0):
                    count += 1
            assert count == aperiodic_count(base, p), (base, p)

    for base, n in [(2, 5), (2, 6), (3, 4)]:
        rates = hole_rates(base, n)
        for word in range(base ** n):
            assert abs(rates[word] - actual_pf_rate(base, n, word)) < 3e-10, (base, n, word)

    for base, n, max_error in [(2, 12, .015), (2, 14, .008),
                                (3, 7, .013), (3, 8, .008)]:
        rates = hole_rates(base, n)
        h = base ** (-n)
        scaled_variance = float(np.var(rates) / h ** 3)
        c = constant(base)
        assert abs(scaled_variance - c) < max_error, (base, n, scaled_variance, c)
        print(f"base={base} n={n} var/h^3={scaled_variance:.12f} C={c:.12f}")
    print('VERIFY_OK')


if __name__ == '__main__':
    check()
