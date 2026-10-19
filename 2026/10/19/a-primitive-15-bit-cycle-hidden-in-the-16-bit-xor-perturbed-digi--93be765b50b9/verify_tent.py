#!/usr/bin/env python3
"""Exact finite-state and finite-field checks for a 16-bit XOR-perturbed tent circuit.

Run: python3 verify_tent.py . No external dependencies are needed.
"""

K = 16
N = 1 << K
TOP = 1 << (K - 1)
MASK = N - 1
Q = (1 << 15) | ((1 << 14) - 1)  # t^15 + t^13 + ... + t + 1


def gate_map(x):
    """Direct gate semantics: conditional ones-complement, shift, last-bit XOR."""
    first = bool(x & TOP)
    selected = (x ^ MASK) if first else x
    shifted = (selected << 1) & MASK
    feedback = ((x >> 1) ^ x) & 1
    return shifted | feedback


def linear_map(x):
    """Independently written GF(2) matrix formula for the same gate logic."""
    b = [(x >> (K - 1 - j)) & 1 for j in range(K)]
    c = [b[0] ^ b[j+1] for j in range(K-1)]
    c.append(b[-2] ^ b[-1])
    y = 0
    for v in c:
        y = (y << 1) | v
    return y


def in_image(x):
    return (((x >> 2) ^ (x >> 1) ^ x) & 1) == 0


def poly_mod(a, modulus):
    while a.bit_length() >= modulus.bit_length():
        a ^= modulus << (a.bit_length() - modulus.bit_length())
    return a


def poly_mul(a, b):
    v = 0
    while b:
        if b & 1:
            v ^= a
        b >>= 1
        a <<= 1
    return v


def poly_pow(a, n, modulus):
    r = 1
    while n:
        if n & 1:
            r = poly_mod(poly_mul(r, a), modulus)
        a = poly_mod(poly_mul(a, a), modulus)
        n >>= 1
    return r


def poly_gcd(a, b):
    while b:
        a, b = b, poly_mod(a, b)
    return a


def main():
    assert Q == 0xBFFF
    successors = [gate_map(x) for x in range(N)]
    for x, y in enumerate(successors):
        assert y == linear_map(x), (x, y)
        assert in_image(y)
    image = set(successors)
    assert len(image) == (N // 2)
    assert all(in_image(x) == (x in image) for x in range(N))
    assert successors[0] == 0
    assert successors[MASK] == 0

    # Irreducibility (Rabin test, degree 15, distinct prime divisors 3,5).
    x = 2
    r32768 = poly_pow(x, 1 << 15, Q)
    assert r32768 == x
    irreducibility_gcds = {
        3: poly_gcd(Q, poly_pow(x, 1 << 5, Q) ^ x),
        5: poly_gcd(Q, poly_pow(x, 1 << 3, Q) ^ x),
    }
    assert irreducibility_gcds == {3: 1, 5: 1}
    factors = (7, 31, 151)
    assert 7*31*151 == (1 << 15)-1
    primitivity_residues = {p: poly_pow(x, 32767//p, Q) for p in factors}
    assert all(v != 1 for v in primitivity_residues.values())
    assert poly_pow(x, 32767, Q) == 1

    # Exhaustive orbit classification, independent of characteristic polynomial.
    nonzero_cycle = []
    visited = set()
    y = successors[1]
    seed = y
    while y not in visited:
        assert y and in_image(y)
        visited.add(y)
        nonzero_cycle.append(y)
        y = successors[y]
    assert y == seed
    assert len(nonzero_cycle) == 32767
    assert visited == image - {0}
    assert len({successors[x] for x in image}) == len(image)
    assert all(successors[x] in image for x in range(N))
    assert sum(not in_image(x) for x in range(N)) == 32768
    print('bits:', K)
    print('characteristic polynomial: t * Q(t), Q mask:', hex(Q))
    print('Rabin modular residue for 2^15:', hex(r32768))
    print('Rabin gcds:', irreducibility_gcds)
    print('primitivity residues:', {p: hex(v) for p,v in primitivity_residues.items()})
    print('states:', N, 'periodic:', len(image), 'transient:', N - len(image))
    print('cycles: one fixed point and one period-32767 cycle')
    print('maximum transient length: 1')
    print('complete gate-to-linear comparison: 65536/65536')
    print('VERIFICATION_OK')


if __name__ == '__main__':
    main()
