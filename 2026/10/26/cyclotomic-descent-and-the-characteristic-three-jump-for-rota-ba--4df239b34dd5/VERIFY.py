"""Finite-field cross-check for a cyclic evolution algebra Rota--Baxter classification.

The proof over arbitrary fields is symbolic; finite enumeration is supplemental.
"""
from itertools import product


def finite_field(p, degree=1):
    if degree == 1:
        elems = range(p)
        add = lambda a, b: (a + b) % p
        neg = lambda a: (-a) % p
        mul = lambda a, b: (a * b) % p
    else:
        assert p == 2 and degree == 2
        elems = range(4)
        add = lambda a, b: a ^ b
        neg = lambda a: a
        def mul(a, b):
            out = 0
            while b:
                if b & 1:
                    out ^= a
                b >>= 1
                a <<= 1
                if a & 4:
                    a ^= 7  # relation z^2=z+1 over GF(2)
            return out
    sub = lambda a, b: add(a, neg(b))
    def power(a, n):
        v = 1
        for _ in range(n):
            v = mul(v, a)
        return v
    def inverse(a):
        assert a
        return next(v for v in elems if mul(a, v) == 1)
    return list(elems), add, neg, sub, mul, power, inverse


def verify(p, degree):
    elements, add, neg, sub, mul, power, inverse = finite_field(p, degree)
    zero, one = 0, 1
    two = add(one, one)
    for lam in (zero, one):
        def is_rb(M):
            a, b, c, d = M
            equ = [
                sub(power(c, 2), mul(add(mul(two, a), lam), b)),
                sub(power(a, 2), mul(add(mul(two, a), lam), d)),
                sub(power(d, 2), mul(add(mul(two, d), lam), a)),
                sub(power(b, 2), mul(add(mul(two, d), lam), c)),
                sub(mul(c, d), add(mul(c, a), power(b, 2))),
                sub(mul(a, b), add(power(c, 2), mul(b, d))),
            ]
            return all(x == zero for x in equ)
        actual = {tuple(M) for M in product(elements, repeat=4) if is_rb(M)}
        if lam == zero:
            if p == 3:
                predicted = {
                    (s, zero, zero, neg(s)) for s in elements
                } | {
                    (s, neg(s), s, neg(s)) for s in elements
                }
            else:
                predicted = {(zero, zero, zero, zero)}
        else:
            predicted = {(zero, zero, zero, zero), (neg(lam), zero, zero, neg(lam))}
            T = [t for t in elements if add(sub(power(t, 2), t), one) == 0 and add(t, one) != zero]
            mu3 = [u for u in elements if power(u, 3) == one]
            for t in T:
                d = neg(mul(lam, inverse(add(one, t))))
                a = mul(t, d)
                delta = sub(a, d)
                predicted.add((a, zero, zero, d))
                for u in mu3:
                    predicted.add((a, mul(delta, power(u, 2)), neg(mul(delta, u)), d))
        assert predicted == actual, (p, degree, lam, len(actual), len(predicted), predicted ^ actual)
        print('FIELD', p, degree, 'WEIGHT', lam, 'COUNT', len(actual))


if __name__ == '__main__':
    for p in (2, 3, 5, 7, 11, 13):
        verify(p, 1)
    verify(2, 2)
    print('VERIFY_OK')
