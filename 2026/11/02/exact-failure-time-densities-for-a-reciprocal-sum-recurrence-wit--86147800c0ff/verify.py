"""Exact checks of a finite-field failure-time theorem for reciprocal-sum sequences.

Run: python3 verify.py. Requires only the Python standard library.
The unrestricted result is proved mathematically; these are finite cross-checks.
"""
from fractions import Fraction
from math import gcd, isqrt


def factors(n):
    out = {}
    p = 2
    while p * p <= n:
        if n % p == 0:
            a = 0
            while n % p == 0:
                n //= p
                a += 1
            out[p] = a
        p += 1 if p == 2 else 2
    if n > 1:
        out[n] = 1
    return out


def local_prediction(h, x0):
    result = set()
    for p, a in factors(h).items():
        if (p != 2 and p != 5 and p % 20 not in (13, 17)):
            continue
        if x0 % (p ** a) or (x0 // (p ** a)) % p == 0:
            continue
        z = (x0 // (p ** a)) * pow(h // (p ** a), -1, p) % p
        if p == 5:
            if z in (2, 3):
                result.add(2)
            elif z in (1, 4):
                result.add(3)
        elif z * z % p == p - 1 or p == 2:
            result.add(2)
    return frozenset(result)


def predicted_counts(h):
    ff = factors(h)
    modulus = 1
    for p, a in ff.items():
        if p == 2 or p == 5 or p % 20 in (13, 17):
            modulus *= p ** (a + 1)
    rden = 1
    rnum = 0
    if 5 in ff:
        rden = 5 ** (ff[5] + 1)
        rnum = 2
    q = Fraction(1)
    for p, a in ff.items():
        if p == 2 or p % 20 in (13, 17):
            q *= 1 - Fraction(1 if p == 2 else 2, p ** (a + 1))
    r = Fraction(rnum, rden)
    densities = {
        frozenset(): (1 - 2 * r) * q,
        frozenset((2,)): r + (1 - 2 * r) * (1 - q),
        frozenset((3,)): r * q,
        frozenset((2, 3)): r * (1 - q),
    }
    assert sum(densities.values()) == 1
    return modulus, {s: int(z * modulus) for s, z in densities.items()}


def failure_set_from_pair_recursion(h, x0, max_index=6):
    g = gcd(x0, h)
    u, v = x0 // g, h // g
    out = set()
    for n in range(1, max_index):
        u, v = u * u + v * v, u * v
        if gcd(h, u) != 1:
            out.add(n + 1)
    return frozenset(out)


def failure_set_from_rational_recurrence(h, x0, max_index=5):
    total = Fraction(x0)
    bad = set()
    for n in range(1, max_index + 1):
        x = Fraction(h * h, 1) / total
        if n >= 2:
            a, b = x.numerator, x.denominator
            q = Fraction(b) + Fraction(2 * a, h)
            if q.denominator != 1 or isqrt(q.numerator) ** 2 != q.numerator:
                bad.add(n)
        total += x
    return frozenset(bad)


def main():
    hh = [1, 2, 3, 4, 5, 6, 7, 10, 12, 13, 14, 15, 17, 20,
          25, 26, 30, 39, 65, 78, 85, 91, 102, 130, 143, 170,
          195, 221, 238, 255, 260, 286, 325, 390, 455, 510,
          770, 1020]
    checked = 0
    examples = 0
    for h in hh:
        assert all(p == 2 or p == 5 or p % 20 in (13, 17) or p % 4 == 3 for p in factors(h))
        modulus, exp = predicted_counts(h)
        if modulus > 100000:
            continue
        got = {s: 0 for s in exp}
        for x0 in range(1, modulus + 1):
            observed = failure_set_from_pair_recursion(h, x0)
            expected = local_prediction(h, x0)
            assert observed == expected, (h, x0, observed, expected)
            got[observed] += 1
            checked += 1
        assert got == exp, (h, modulus, got, exp)
        examples += 1
        if h == 65:
            assert got == {frozenset(): 3507, frozenset((2,)): 380,
                           frozenset((3,)): 334, frozenset((2, 3)): 4}
    rational_checks = 0
    for h in (2, 5, 13, 17, 65, 130):
        for x0 in range(1, 80):
            assert failure_set_from_rational_recurrence(h, x0, 5) == \
                   failure_set_from_pair_recursion(h, x0, 5)
            rational_checks += 1
    print(f'VERIFY_OK moduli={examples} reduced_pair_inputs={checked} '
          f'original_fraction_inputs={rational_checks} exact_arithmetic=yes')


if __name__ == '__main__':
    main()
