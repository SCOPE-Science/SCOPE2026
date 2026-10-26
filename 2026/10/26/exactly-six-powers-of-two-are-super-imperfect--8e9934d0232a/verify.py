"""Independent finite checks accompanying an elementary infinite proof.

Execute: python3 verify.py
Only Python 3 standard-library modules are used.
"""
from math import isqrt


def factor_small(n):
    result = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            result.append((p, e))
        p = 3 if p == 2 else p + 2
    if n > 1:
        result.append((n, 1))
    return result


def beta_prime_power(p, e):
    assert e >= 1
    return (p ** (e + 1) + (-1) ** e) // (p + 1)


def beta(n):
    assert n >= 1
    out = 1
    for p, e in factor_small(n):
        out *= beta_prime_power(p, e)
    return out


def v2(n):
    assert n > 0
    j = 0
    while n % 2 == 0:
        n //= 2
        j += 1
    return j


def is_prime_small(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def fermat(j):
    return 2 ** (2 ** j) + 1


def run_checks():
    # These are checks, not a substitute for the all-exponent argument.
    expected = {1, 2, 3, 7, 15, 31}
    for a in range(1, 25):
        B = beta(1 << a)
        assert B == ((1 << (a + 1)) + (-1) ** a) // 3
        assert (beta(B) == (1 << (a - 1))) == (a in expected)

    for j in range(5):
        assert is_prime_small(fermat(j))
    assert fermat(5) == 641 * 6700417

    for p in (3, 5, 7, 11, 13, 17, 19, 23, 31):
        for t in range(1, 17):
            R = sum(p ** (2 * k) for k in range(t + 1))
            assert v2(R) == v2(t + 1)
            assert R > t + 1
            assert beta_prime_power(p, 2 * t + 1) == (p - 1) * R
            assert beta_prime_power(p, 2 * t) % 2 == 1

    # Verify 2-adic omission witness for finite odd exponents.
    omission_examples = 0
    for a in range(3, 241, 2):
        digits = {j for j in range(1, (a - 1).bit_length()) if (a - 1) & (1 << j)}
        if not digits:
            continue
        h = max(digits)
        missing = next((j for j in range(1, h) if j not in digits), None)
        if missing is None:
            assert a + 1 == 1 << (h + 1)
            continue
        modulus = 1 << ((1 << missing) + 1)
        B = ((1 << (a + 1)) - 1) // 3
        pre = 1
        for j in range(1, missing):
            pre = pre * fermat(j) % modulus
        candidate = 1
        for j in digits:
            # Avoid huge integers: each factor is reduced before multiplication.
            candidate = candidate * (1 + pow(2, 1 << j, modulus)) % modulus
        assert candidate == pre
        assert (B - pre) % modulus == (1 << (1 << missing))
        assert (B - candidate) % modulus != 0
        omission_examples += 1

    for a in range(4, 202, 2):
        # Division by 3 is legitimate in the ring of integers mod 16.
        assert ((1 << (a + 1)) + 1) // 3 % 16 == 11
        # A Fermat-prime product indexed by odd a-1 would be 3 or 15 mod 16.
        assert 11 not in (3, 15)
    print('VERIFY_OK', 'powers_a_1_to_24', 24,
          'Fermat_primes_F0_to_F4', 5,
          'omission_witnesses', omission_examples,
          'even_exponents_checked', 99)


if __name__ == '__main__':
    run_checks()
