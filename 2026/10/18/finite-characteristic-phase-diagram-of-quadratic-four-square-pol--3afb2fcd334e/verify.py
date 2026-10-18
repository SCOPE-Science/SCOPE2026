"""Exact checks for quadratic four-square polynomial triples over prime fields.

All computations use the Python standard library and integer modular arithmetic.
"""
from math import isqrt


def isprime(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b, p):
    return trim([((a[i] if i < len(a) else 0) +
                  (b[i] if i < len(b) else 0)) % p
                 for i in range(max(len(a), len(b)))])


def mul(a, b, p):
    z = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            z[i + j] = (z[i + j] + ai * bj) % p
    return trim(z)


def scale(a, c, p):
    return trim([(v * c) % p for v in a])


def plus_one(a, p):
    return add(a, [1], p)


def G(k, p):
    return (16 * k**3 + 55 * k**2 - 64 * k + 16) % p


def roots(p):
    return [k for k in range(p) if G(k, p) == 0]


def normalized_triple(p, k):
    assert G(k, p) == 0
    inv = lambda n: pow(n % p, -1, p)
    sigma = (k * (8 * k - 3) * inv(4 * (2 * k - 1))) % p
    P = ((sigma + 1) * inv(2)) % p
    Q = ((sigma - 1) * inv(2)) % p
    a = [(-inv(k)**2) % p, 0, 1]
    b = add(scale(a, P**2, p), [2 * P % p], p)
    c = add(scale(a, Q**2, p), [2 * Q % p], p)
    r = add(scale(a, P, p), [1], p)
    s = add(scale(a, Q, p), [1], p)
    t = add(scale(a, P * Q, p), [(P + Q) % p], p)
    u = mul([0, 1], add(scale(a, P * Q, p), [k], p), p)
    return (a, b, c), (r, s, t, u)


def check_squares(p, abc, roots4):
    a, b, c = abc
    assert all(len(z) == 3 and z[2] != 0 for z in abc)
    assert len({tuple(z) for z in abc}) == 3
    assertions = [mul(a, b, p), mul(a, c, p),
                  mul(b, c, p), mul(mul(a, b, p), c, p)]
    for pol, r in zip(assertions, roots4):
        assert plus_one(pol, p) == mul(r, r, p)


def center(a, p):
    return -a[1] * pow(2 * a[2] % p, -1, p) % p


def exceptional_examples():
    # Coefficients are in ascending degree order.
    ex5 = ([4, 0, 1], [0, 3, 1], [2, 1, 4])
    sq5 = ([1, 1, 4], [2, 1, 3], [4, 2, 2], [4, 3, 2, 2])
    ex13 = ([4, 0, 1], [4, 4, 10], [4, 9, 10])
    sq13 = ([2, 4, 7], [11, 4, 6], [2, 0, 3], [0, 8, 0, 3])
    for p, abc, roots4 in [(5, ex5, sq5), (13, ex13, sq13)]:
        check_squares(p, abc, roots4)
        assert len({center(z, p) for z in abc}) == 3
    return 2


def cubic_discriminant(a, b, c, d):
    return b*b*c*c - 4*a*c**3 - 4*b**3*d - 27*a*a*d*d + 18*a*b*c*d


def main():
    assert cubic_discriminant(16, 55, -64, 16) == 728**2
    assert [G(k, 3) for k in range(3)] == [1, 2, 2]
    assert exceptional_examples() == 2
    count, split, inert, identities = 0, 0, 0, 0
    for p in range(17, 601):
        if not isprime(p):
            continue
        count += 1
        rr = roots(p)
        assert len(rr) in (0, 3), (p, rr)
        if rr:
            split += 1
            for k in rr:
                abc, roots4 = normalized_triple(p, k)
                check_squares(p, abc, roots4)
                assert len({center(z, p) for z in abc}) == 1
                identities += 4
        else:
            inert += 1
    print('VERIFY_OK')
    print('exceptional_distinct_center_fields=2 (characteristics 5 and 13)')
    print('prime_fields_tested=', count, 'split=', split, 'inert=', inert)
    print('exact_four_square_identities_tested=', identities)
    print('polynomial_discriminant=', 728**2)


if __name__ == '__main__':
    main()
