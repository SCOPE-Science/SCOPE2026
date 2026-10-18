"""Exact independent finite checks for joint trace/cotrace/derivative counts.

No external dependencies. Run with: python3 verify_three_jets.py
Finite enumeration is a diagnostic, not a substitute for the infinite proof.
"""
from collections import Counter
from itertools import product

BITS = tuple(product((0, 1), repeat=3))


def mobius(n):
    r = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0:
                return 0
            r = -r
        p += 1
    return -r if n > 1 else r


def poly_mod(a, b):
    k = b.bit_length() - 1
    while a.bit_length() > k:
        a ^= b << (a.bit_length() - k - 1)
    return a


def poly_mul(a, b):
    c = 0
    while b:
        if b & 1:
            c ^= a
        a <<= 1
        b >>= 1
    return c


def poly_gcd(a, b):
    while b:
        a, b = b, poly_mod(a, b)
    return a


def is_irreducible(p, n):
    t = 2
    for i in range(1, n + 1):
        t = poly_mod(poly_mul(t, t), p)
        if i <= n // 2 and n % i == 0 and poly_gcd(t ^ 2, p) != 1:
            return False
    return t == 2


def irreducibles(n):
    for mid in range(1 << (n - 1)):
        p = (1 << n) | 1 | (mid << 1)
        if is_irreducible(p, n):
            yield p


def K(n):
    x, y = -2, 1
    for _ in range(2, n + 1):
        x, y = y, -y - 2 * x
    return y if n >= 1 else x


def H(n):
    if n & 1:
        return 0
    x, y = -2, 14
    if n == 2:
        return x
    for _ in range(6, n + 1, 2):
        x, y = y, y - 4 * x
    return y


def moment(n, r, s, t):
    if not (r or s or t):
        return (1 << n) - 2
    if r + s + t == 1:
        return -1 - (-1) ** n
    if r + s + t == 2:
        return ((-1) ** n if r and t else 1) * (K(n) - 1)
    return H(n)


def all_field(n):
    return {bits: sum((-1) ** sum(x * y for x, y in zip(bits, uvw))
                      * moment(n, *uvw) for uvw in BITS) // 8 for bits in BITS}


def predicted(n):
    arr = {}
    for abc in BITS:
        z = 0
        for d in range(1, n + 1):
            if n % d:
                continue
            h = n // d
            term = (all_field(d)[abc] if h & 1 else
                    ((1 << d) - 2 if abc == (0, 0, 0) else 0))
            z += mobius(h) * term
        assert z % n == 0
        arr[abc] = z // n
    return arr


def field_mul(a, b, p):
    return poly_mod(poly_mul(a, b), p)


def field_inverse(a, p, n):
    ans, base, exponent = 1, a, (1 << n) - 2
    while exponent:
        if exponent & 1:
            ans = field_mul(ans, base, p)
        base = field_mul(base, base, p)
        exponent >>= 1
    return ans


def field_trace(a, p, n):
    s, t = 0, a
    for _ in range(n):
        s ^= t
        t = field_mul(t, t, p)
    assert s in (0, 1)
    return s


def main():
    for n in range(2, 16):
        observed = Counter()
        for p in irreducibles(n):
            triple = ((p >> (n - 1)) & 1,
                      (p >> 1) & 1,
                      sum((p >> j) & 1 for j in range(1, n + 1, 2)) & 1)
            observed[triple] += 1
        formula = predicted(n)
        assert all(observed[x] == formula[x] for x in BITS), n
        if n >= 7:
            assert all(formula[x] > 0 for x in BITS)
        else:
            assert any(formula[x] == 0 for x in BITS)
        print('degree', n, 'counts', *(formula[x] for x in BITS))
    for n in range(2, 11):
        p = next(irreducibles(n))
        direct_k = 0
        direct_h = 0
        for x in range(1, 1 << n):
            ix = field_inverse(x, p, n)
            direct_k += (-1) ** field_trace(x ^ ix, p, n)
            if x != 1:
                direct_h += (-1) ** field_trace(
                    x ^ ix ^ field_inverse(x ^ 1, p, n), p, n)
        assert (direct_k, direct_h) == (K(n), H(n)), n
    print('VERIFY_OK: degree 2..15 polynomial counts; degree 2..10 character sums')


if __name__ == '__main__':
    main()
