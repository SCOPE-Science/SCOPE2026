"""Finite exact-arithmetic checks for quadratic divide-or-choose maps.

This program checks only finite instances of the lemmas; the asymptotic
claim is proved mathematically, not by computation.
"""

from math import gcd


def map_value(n, eps):
    return n // 2 if n % 2 == 0 else n * (n + eps) // 2


def odd_prime_product(r):
    found, product, p = 0, 1, 3
    while found < r:
        if all(p % d for d in range(3, int(p**0.5) + 1, 2)):
            product *= p
            found += 1
        p += 2
    return product


def check_return(y, eps):
    assert y >= 3 and y % 2 == 1
    h = y + eps
    j = (h & -h).bit_length() - 1
    k = h >> j
    assert j >= 1 and k % 2 == 1 and gcd(y, k) == 1
    z = y
    for t in range(j):
        z = map_value(z, eps)
        if t < j - 1:
            assert z % 2 == 0
        assert z >= y if k >= 3 else z >= 1
    assert z == y * k and z % 2 == 1
    return j, k, z


def run():
    checks, escaping_segments, checked_endpoints = 0, 0, 0
    for eps in (-1, 1):
        for y in range(3, 1200, 2):
            check_return(y, eps)
            checks += 1
        for y0 in range(3, 100, 2):
            y, multipliers = y0, []
            for r in range(11):
                if y.bit_length() > 20000:
                    break
                j, k, next_y = check_return(y, eps)
                checks += 1
                if k == 1:
                    break
                assert all(gcd(k, u) == 1 for u in multipliers)
                assert gcd(k, y0) == 1
                multipliers.append(k)
                escaping_segments += 1
                assert next_y >= odd_prime_product(r + 1)
                assert next_y == y0 * __import__('math').prod(multipliers)
                y = next_y
                checked_endpoints += 1
    print(f"PASS: {checks} exact odd-return identities; "
          f"{escaping_segments} pairwise-coprime multipliers; "
          f"{checked_endpoints} prime-product lower-bound comparisons")


if __name__ == '__main__':
    run()
