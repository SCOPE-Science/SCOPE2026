"""Exact finite checks for squarefree multiplicative collisions in F_q[T].
Run with Python 3 (standard library only). Finite tests are not the proof of the theorem.
"""
from itertools import product
from collections import Counter
from functools import lru_cache
from math import isqrt, log, exp


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a)


def mul(a, b, q):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % q
    return tuple(out)


def mod(a, b, q):
    a = list(a)
    inv = pow(b[-1], -1, q)
    while len(a) >= len(b) and a != [0]:
        c = a[-1] * inv % q
        for j, bj in enumerate(b):
            a[j + len(a) - len(b)] = (a[j + len(a) - len(b)] - c * bj) % q
        a = list(trim(a))
    return tuple(a)


def gcd(a, b, q):
    while b != (0,):
        a, b = b, mod(a, b, q)
    return a


def is_squarefree(a, q):
    if len(a) == 1:
        return True
    derivative = trim(tuple((i * a[i]) % q for i in range(1, len(a))))
    return len(gcd(a, derivative, q)) == 1


@lru_cache(None)
def monics(q, n):
    return tuple((*p, 1) for p in product(range(q), repeat=n))


def direct(q, n):
    squarefree = [f for f in monics(q, n) if is_squarefree(f, q)]
    products = Counter(mul(f, g, q) for f in squarefree for g in squarefree)
    return sum(v * v for v in products.values())


def canonical(q, n):
    count = 0
    for a in range(n + 1):
        b = n - a
        a_polys, b_polys = monics(q, a), monics(q, b)
        for A in a_polys:
            for D in a_polys:
                if not is_squarefree(A, q) or not is_squarefree(D, q):
                    continue
                for B in b_polys:
                    if not is_squarefree(B, q) or not is_squarefree(mul(A, B, q), q):
                        continue
                    if not is_squarefree(mul(B, D, q), q):
                        continue
                    for C in b_polys:
                        if (len(gcd(B, C, q)) == 1
                                and is_squarefree(mul(A, C, q), q)
                                and is_squarefree(mul(C, D, q), q)):
                            count += 1
    return count


def mobius(n):
    sign = 1
    for p in range(2, isqrt(n) + 1):
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
    return -sign if n > 1 else sign


def irreducible_count(q, d):
    return sum(mobius(k) * q ** (d // k) for k in range(1, d + 1) if d % k == 0) // d


def truncated_constant(q, max_d=28):
    return exp(sum(irreducible_count(q, d) * (
        4 * log(1 - q ** (-d)) + log(1 + 4 * q ** (-d) + q ** (-2 * d)))
        for d in range(1, max_d + 1)))


def main():
    for q, upper in ((2, 6), (3, 4), (5, 3)):
        for n in range(1, upper + 1):
            observed = direct(q, n)
            unrestr = ((n + 1) * q ** (2 * n) - n * q ** (2 * n - 1))
            assert 0 <= observed <= unrestr
            if (q == 2 and n <= 4) or (q == 3 and n <= 3) or (q == 5 and n <= 2):
                assert observed == canonical(q, n), (q, n, observed)
            print('EXACT', q, n, observed, unrestr)
        c = truncated_constant(q)
        rho = c / (1 - 1 / q)
        assert 0 < rho < (1 - 1 / q) ** 4
        print('PRODUCT', q, format(c, '.12g'), format(rho, '.12g'))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
