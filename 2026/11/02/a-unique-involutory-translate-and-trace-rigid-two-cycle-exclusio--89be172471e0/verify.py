"""Independent finite-field checks for the additive-translate cycle theorem.

Usage: python3 verify.py  (Python standard library only).
Tests are finite corroboration, not a proof of the all-degree statement.
"""

def polynomial_remainder(a, modulus):
    degree = modulus.bit_length() - 1
    while a.bit_length() - 1 >= degree:
        a ^= modulus << (a.bit_length() - 1 - degree)
    return a


def polynomial_gcd(a, b):
    while b:
        a, b = b, polynomial_remainder(a, b)
    return a


def polynomial_multiply(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        a <<= 1
        b >>= 1
    return out


def polynomial_powmod(a, n, modulus):
    result = 1
    while n:
        if n & 1:
            result = polynomial_remainder(polynomial_multiply(result, a), modulus)
        a = polynomial_remainder(polynomial_multiply(a, a), modulus)
        n >>= 1
    return result


def is_irreducible(modulus, m):
    if modulus.bit_length() != m + 1:
        return False
    x = 2
    if polynomial_powmod(x, 1 << m, modulus) != x:
        return False
    distinct_primes = [p for p in range(2, m+1) if m % p == 0 and all(p % d for d in range(2, int(p**0.5)+1))]
    return all(polynomial_gcd(polynomial_powmod(x, 1 << (m//p), modulus) ^ x, modulus) == 1 for p in distinct_primes)


def field_multiply(a, b, modulus, m):
    result = 0
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & (1 << m):
            a ^= modulus
    return result


def field_power(a, n, modulus, m):
    result = 1
    while n:
        if n & 1:
            result = field_multiply(result, a, modulus, m)
        a = field_multiply(a, a, modulus, m)
        n >>= 1
    return result


def absolute_trace(a, modulus, m):
    acc = 0
    v = a
    for _ in range(m):
        acc ^= v
        v = field_multiply(v, v, modulus, m)
    assert acc in (0, 1)
    return acc


def main():
    fields = [(3,0x00b),(5,0x025),(7,0x083),(9,0x203),(11,0x805),(13,0x201b)]
    total_cases = total_points = involution_points = 0
    for m, modulus in fields:
        assert is_irreducible(modulus, m), (m, 'modulus is reducible')
        q = 1 << m
        d = (m + 1) // 2
        r = (1 << d) - 1
        f = [x ^ field_power(x, r, modulus, m) ^ field_power(x, q-r, modulus, m)
             for x in range(q)]
        assert len(set(f)) == q
        offsets = list(range(q)) if m <= 9 else sorted({0,1,2,3,5,17,q-1})
        for offset in offsets:
            expected_fixed = 2 if absolute_trace(offset, modulus, m) == 0 else 0
            fixed = second_period = 0
            for x in range(q):
                y = f[x] ^ offset
                z = f[y] ^ offset
                fixed += (y == x)
                second_period += (z == x and y != x)
                if offset == 1:
                    assert z == x
                elif z == x:
                    assert y == x
            if offset == 1:
                assert fixed == 0 and second_period == q, (m, offset, fixed, second_period)
                involution_points += q
            else:
                assert fixed == expected_fixed and second_period == 0, (m,offset,fixed,second_period)
            total_cases += 1
            total_points += q
        print('field_degree', m, 'size', q, 'offsets_checked', len(offsets))
    print('VERIFY_OK degrees=6 translate_cases=', total_cases,
          'state_checks=', total_points, 'exceptional_involution_points=', involution_points)

if __name__ == '__main__':
    main()
