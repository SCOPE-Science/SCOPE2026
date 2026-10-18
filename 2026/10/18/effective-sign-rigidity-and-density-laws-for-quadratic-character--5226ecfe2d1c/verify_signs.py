#!/usr/bin/env python3
"""Exact-integer finite checks of quadratic-character binomial sign laws."""
import math


def odd_primes_upto(bound):
    for p in range(3, bound + 1, 2):
        if all(p % d for d in range(3, math.isqrt(p) + 1, 2)):
            yield p


def character(k, p):
    v = pow(k % p, (p - 1) // 2, p)
    return 0 if v == 0 else (1 if v == 1 else -1)


def predicted_sign(n, p):
    r = n % (2 * p)
    if p % 4 == 1:
        return 1 if 2 * r < p or 2 * r > 3 * p else -1
    if r in (0, p):
        return 0
    return 1 if r < p else -1


def sgn(v):
    return (v > 0) - (v < 0)


def main():
    for p in odd_primes_upto(37):
        cutoff = 0 if p == 3 else (1 + math.floor(p*p / 6 * math.log(p * (p-3) / 2)))
        upper = cutoff + 3 * p
        coefficients = [1]
        values = []
        chars = [character(k, p) for k in range(upper + 1)]
        for n in range(upper + 1):
            val = sum(x * y for x, y in zip(coefficients, chars))
            values.append(val)
            if n >= cutoff:
                assert sgn(val) == predicted_sign(n, p), (p, n, val)
            if p % 4 == 3 and n % p == 0:
                assert val == 0, (p, n, val)
            if n < upper:
                coefficients = ([1] + [coefficients[i-1] + coefficients[i]
                                     for i in range(1, len(coefficients))] + [1])
        signs = [predicted_sign(n, p) for n in range(2*p)]
        counts = tuple(signs.count(t) for t in (1, -1, 0))
        assert counts == ((p, p, 0) if p % 4 == 1 else (p-1, p-1, 2))
        if p == 3:
            assert values[:7] == [0, 1, 1, 0, -1, -1, 0]
        print(f"p={p} cutoff={cutoff} exact_integer_indices=0..{upper} period_sign_counts={counts} OK")
    print("All finite checks passed; infinite proof is separate.")

if __name__ == '__main__':
    main()
