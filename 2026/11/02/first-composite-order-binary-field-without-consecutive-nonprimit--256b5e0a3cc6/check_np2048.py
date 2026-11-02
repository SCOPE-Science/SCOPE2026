#!/usr/bin/env python3
"""Exact standalone certificate for characteristic-two nonprimitive adjacency at 2048."""

MODULUS = 0x805  # t^11+t^2+1 over F_2
BEZOUT = {
    (23, 23): (0xfeff, 0x8101),
    (23, 89): (0x16d4b3de4c40fc98972d82d, 0x6df116),
    (89, 23): (0x6d89f3, 0x16c591d9c33949f6cda888b),
    (89, 89): (0x355f8a2bfd500aa0202023, 0x264c993ebd7af5f264c991),
}

def degree(a):
    return a.bit_length() - 1

def polynomial_multiply(a, b):
    ans = 0
    while b:
        if b & 1:
            ans ^= a
        a <<= 1
        b >>= 1
    return ans

def polynomial_remainder(a, b):
    assert b
    while degree(a) >= degree(b):
        a ^= b << (degree(a) - degree(b))
    return a

def polynomial_gcd(a, b):
    while b:
        a, b = b, polynomial_remainder(a, b)
    return a

def shifted_binomial(n):
    """Polynomial (t+1)^n, coefficients encoded as binary digits."""
    answer = 1
    for j in range(n.bit_length()):
        if (n >> j) & 1:
            answer = polynomial_multiply(answer, (1 << (1 << j)) | 1)
    return answer

def field_multiply(a, b):
    return polynomial_remainder(polynomial_multiply(a, b), MODULUS)

def field_power(a, n):
    answer = 1
    while n:
        if n & 1:
            answer = field_multiply(answer, a)
        a = field_multiply(a, a)
        n >>= 1
    return answer

# Check every displayed Bezout identity, not only a gcd routine's output.
for (a, b), (u, v) in BEZOUT.items():
    f = (1 << a) | 1
    g = shifted_binomial(b) ^ 1
    assert polynomial_multiply(u, f) ^ polynomial_multiply(v, g) == 1
    assert polynomial_gcd(f, g) == 1

# Degree-eleven irreducibility: Frobenius identity and prime-degree Rabin test.
assert degree(MODULUS) == 11
z = 2
for _ in range(11):
    z = polynomial_remainder(polynomial_multiply(z, z), MODULUS)
assert z == 2
assert polynomial_gcd(MODULUS, (1 << 2) | (1 << 1)) == 1

# The class t is a generator: 2047=23*89, and neither prime index passes.
assert field_power(2, 2047) == 1
assert field_power(2, 89) != 1
assert field_power(2, 23) != 1

H23 = {field_power(2, 89 * j) for j in range(23)}
H89 = {field_power(2, 23 * j) for j in range(89)}
A = H23 | H89
assert (len(H23), len(H89), len(H23 & H89), len(A)) == (23, 89, 1, 111)
assert H23 & H89 == {1}
assert all((x ^ 1) not in A for x in A)

# Independent complete check over all 2047 nonzero field elements.
B = {x for x in range(1, 2048)
     if field_power(x, 89) == 1 or field_power(x, 23) == 1}
assert B == A
assert sum(1 for x in range(1, 2048) if x in B and (x ^ 1) in B) == 0

# Every smaller exponent with composite 2^k-1 is itself composite.
for k in range(2, 11):
    order = (1 << k) - 1
    if any(order % d == 0 for d in range(2, int(order ** 0.5) + 1)):
        assert any(k % d == 0 for d in range(2, k))
print('VERIFY_OK bezout=4 irreducible_degree=11 primitive_generator=yes '
      'nonprimitive=111 exhaustive_elements=2047 ordered_NP_pairs=0')
