"""Exact finite certification of an odd-height extremum for modified Dedekind psi.

Python >=3.9. No dependencies beyond the standard library.
"""
from array import array
from math import isqrt

LIMIT = 1 << 23


def main():
    # Smallest odd prime factor, or zero if the odd integer is prime.
    spf = array('I', [0]) * LIMIT
    for p in range(3, isqrt(LIMIT - 1) + 1, 2):
        if not spf[p]:
            for j in range(p * p, LIMIT, 2 * p):
                if not spf[j]:
                    spf[j] = p

    # H(n) is completely additive, H(2)=1 and H(p)=1+H((p+1)/2)
    # for odd primes p. For odd n it equals the iterate count lambda(n).
    H = bytearray(LIMIT)
    H[2] = 1
    B = [0] * 24
    P = [0] * 24
    C = [0] * 24
    for n in range(3, LIMIT):
        if n & 1:
            p = spf[n]
            if p:
                value = H[p] + H[n // p]
            else:
                value = H[(n + 1) // 2] + 1
            H[n] = value
            if value <= 23:
                B[value] = n
                if not p:
                    P[value] = n
                    C[value] += 1
        else:
            H[n] = H[n >> 1] + 1
    assert all(B[k] == P[k] for k in range(2, 23))
    assert B[23] == 8193151, (B[23], P[23])
    assert P[23] == 8126431
    assert 127 * 64513 == B[23]
    assert H[127] == 7 and H[64513] == 16
    assert B[23] < LIMIT

    # Two independent arithmetic identities for the factorization and
    # the original iteration, not inferred from the H recurrence.
    small_primes = [p for p in range(2, isqrt(2 * LIMIT) + 1)
                    if p == 2 or (p & 1 and not spf[p])]

    def factor(n):
        result = []
        for p in small_primes:
            if p * p > n:
                break
            if n % p == 0:
                power = 0
                while n % p == 0:
                    n //= p
                    power += 1
                result.append((p, power))
        if n > 1:
            # In all checks performed below the remaining number fits the
            # previously sieved bound, or is prime by trial division.
            result.append((n, 1))
        return result

    def psi(n):
        ans = 1
        for p, exponent in factor(n):
            ans *= p ** (exponent - 1) if p == 2 else p ** (exponent - 1) * (p + 1)
        return ans

    def trajectory(n):
        t = [n]
        while t[-1] != 2:
            assert len(t) < 100
            t.append(psi(t[-1]))
        return t

    for n, height in [(127, 7), (64513, 16),
                      (8126431, 23), (8193151, 23)]:
        assert len(trajectory(n)) == height + 1
        assert H[n] == height
    assert factor(8193151) == [(127, 1), (64513, 1)]
    assert factor(8126431) == [(8126431, 1)]

    # An independent direct-iteration check of every possible larger
    # odd competitor in the provable finite bound for height 23.
    upper_checks = 0
    for n in range(8193153, LIMIT, 2):
        assert len(trajectory(n)) - 1 != 23, n
        upper_checks += 1
    assert upper_checks == 97728

    print('EXACT_CERTIFICATE_OK first_composite_class=23 B23=8193151 '
          'prime_max_23=8126431 suffix_checked=' + str(upper_checks))
    print('k B(k) P(k) prime_count')
    for k in range(2, 24):
        print(k, B[k], P[k], C[k])


if __name__ == '__main__':
    main()
