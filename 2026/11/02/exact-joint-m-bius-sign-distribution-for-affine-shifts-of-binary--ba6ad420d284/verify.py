"""Independently enumerate finite-field cubic factorization patterns and affine-shift joint Mobius signs.
Run: python3 verify.py. Standard library only.
"""
from collections import Counter
from itertools import product

MODULI = {1: 0b11, 2: 0b111, 3: 0b1011, 4: 0b10011, 5: 0b100101, 6: 0b1000011}


def gf_mul(x, y, q, modulus):
    out = 0
    while y:
        if y & 1:
            out ^= x
        y >>= 1
        x <<= 1
        if x & q:
            x ^= modulus
    return out


def gf_power(x, exponent, q, modulus):
    result = 1
    while exponent:
        if exponent & 1:
            result = gf_mul(result, x, q, modulus)
        x = gf_mul(x, x, q, modulus)
        exponent //= 2
    return result


def classify_cubics(q, modulus):
    # Factorization-type determination by direct root enumeration and the
    # ordinary derivative, independently of Berlekamp discriminants.
    elements = range(q)
    squares = [gf_mul(x, x, q, modulus) for x in elements]
    cubes = [gf_mul(squares[x], x, q, modulus) for x in elements]
    sqrt = [gf_power(b, q // 2, q, modulus) for b in elements]
    assert all(squares[sqrt[b]] == b for b in elements)
    product_table = [[gf_mul(x, y, q, modulus) for y in elements] for x in elements]
    mobius = [0] * (q**3)
    squarefree = 0
    for a, b, c in product(elements, repeat=3):
        # Evaluate T^3 + a T^2 + b T + c directly.
        root_count = 0
        repeated_root = sqrt[b]  # The only zero of 3T^2+2aT+b = T^2+b.
        rep_val = cubes[repeated_root] ^ product_table[a][squares[repeated_root]] ^ product_table[b][repeated_root] ^ c
        if rep_val != 0:
            root_count = sum(
                (cubes[x] ^ product_table[a][squares[x]] ^ product_table[b][x] ^ c) == 0
                for x in elements
            )
            assert root_count in (0, 1, 3), (q, a, b, c, root_count)
            val = 1 if root_count == 1 else -1
            squarefree += 1
        else:
            val = 0
        mobius[(a * q + b) * q + c] = val
    assert squarefree == q**3 - q**2
    return mobius


def predicted(q):
    out = {}
    for s, t in product((-1, 0, 1), repeat=2):
        if s == t == 0:
            n = q
        elif s == 0 or t == 0:
            n = q * (q - 1) // 2
        elif s == t:
            n = q * q * (q - 2) // 4
        else:
            n = q * (q * q - 2 * q + 2) // 4
        out[(s, t)] = n
    assert sum(out.values()) == q**3
    return out


def run():
    shifts_checked = 0
    poly_pairs_checked = 0
    for degree, modulus in MODULI.items():
        q = 1 << degree
        mu = classify_cubics(q, modulus)
        if q <= 16:
            shifts = list(product(range(1, q), range(q)))
        elif q == 32:
            shifts = list(product((1, 2, 4, 7, 13, 31), (0, 1, 2, 7, 15, 31)))
        else:
            shifts = [(1, 0), (1, 1), (2, 7), (3, 25), (31, 63), (63, 0)]
        want = predicted(q)
        for u, v in shifts:
            # No use of cubic coefficient translation, character sums, or the
            # theorem's internal factorization. Direct full enumeration.
            counts = Counter()
            for a, b, c in product(range(q), repeat=3):
                index = (a * q + b) * q + c
                other = (a * q + (b ^ u)) * q + (c ^ v)
                counts[(mu[index], mu[other])] += 1
            assert all(counts[pair] == expected for pair, expected in want.items()), (q, u, v, counts, want)
            assert sum(s * t * n for (s, t), n in counts.items()) == -q
            shifts_checked += 1
            poly_pairs_checked += q**3
        print(f'PASS q={q} shifts={len(shifts)} full_polynomials_per_shift={q**3}')
    print(f'VERIFY_OK degrees={len(MODULI)} shifts={shifts_checked} cubic_pairs={poly_pairs_checked}')


if __name__ == '__main__':
    run()
