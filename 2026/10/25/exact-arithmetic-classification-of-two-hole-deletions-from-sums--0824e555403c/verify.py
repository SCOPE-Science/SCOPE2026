#!/usr/bin/env python3
"""Exact finite checks for two-hole deletions in sums of two squares.

No third-party packages. The independent oracle enumerates integer square pairs;
the predictions instead factor integers and use Jacobi's multiplicity criterion.
Finite checks supplement but do not replace the proof for all positive integers.
"""
from math import gcd, isqrt


def factor(n):
    assert n >= 1
    result = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            result[d] = result.get(d, 0) + 1
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


def has_split_prime(n):
    return any(p % 4 == 1 for p in factor(n))


def split_product(n):
    out = 1
    for p, exponent in factor(n).items():
        if p % 4 == 1:
            out *= exponent + 1
    return out


def representation_pairs(n):
    out = []
    for a in range(isqrt(n // 2) + 1):
        b2 = n - a * a
        b = isqrt(b2)
        if b * b == b2 and a <= b:
            out.append((a, b))
    return out


def predicted_one_sided(u, v):
    return has_split_prime(u) and has_split_prime(v) and split_product(u*u + v*v) >= 3


def predicted_two_sided(u, v):
    return has_split_prime(u) and has_split_prime(v)


def observed_one_sided(u, v):
    forbidden = {u, v}
    for n in {2*u*u, u*u + v*v, 2*v*v}:
        if not any(a not in forbidden or b not in forbidden for a, b in representation_pairs(n)):
            return False
    return True


def observed_two_sided(u, v):
    for n in {2*u*u, u*u + v*v, 2*v*v}:
        if not any((a != u and b != v) or (b != u and a != v)
                   for a, b in representation_pairs(n)):
            return False
    return True


def run():
    count = 0
    one_yes = two_yes = mixed_block = 0
    for v in range(2, 121):
        for u in range(1, v):
            one = predicted_one_sided(u, v)
            two = predicted_two_sided(u, v)
            assert one == observed_one_sided(u, v), (u, v, 'one')
            assert two == observed_two_sided(u, v), (u, v, 'two')
            one_yes += one
            two_yes += two
            mixed_block += two and not one
            count += 1
    assert count == 7140
    assert predicted_one_sided(5, 37) and predicted_two_sided(5, 37)
    assert not predicted_one_sided(5, 13) and predicted_two_sided(5, 13)
    assert representation_pairs(50) == [(1, 7), (5, 5)]
    assert (13, 35) in representation_pairs(1394)
    assert (23, 47) in representation_pairs(2738)
    print('Pair oracle checks:', count)
    print('One-sided admissible:', one_yes)
    print('Two-sided admissible:', two_yes)
    print('Two-sided only:', mixed_block)
    print('Example one-sided (u,v)=(5,37):',
          [representation_pairs(n) for n in (50, 1394, 2738)])
    crt = next(v for v in range(14, 5*13*17*41+1)
               if v % 13 == 0 and v % 5 == 1 and v % 17 == 3 and v % 41 == 4)
    assert gcd(5, crt) == 1 and predicted_one_sided(5, crt)
    print('CRT base representative:', crt, 'modulus:', 5*13*17*41)
    print('CERTIFICATE_OK')


if __name__ == '__main__':
    run()
