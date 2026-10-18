#!/usr/bin/env python3
"""Exhaustive finite-field check of weight-one Rota--Baxter maps on K[t]/(t^n).

Requires only Python's standard library. Finite fields are represented by binary
polynomials modulo an irreducible polynomial; matrix columns are packed integers.
The exhaustive computation verifies all K-linear maps, not just projections.
"""
from itertools import product

IRREDUCIBLE = {1: 0b11, 2: 0b111, 3: 0b1011, 4: 0b10011}


def check(field_degree, n):
    q = 1 << field_degree
    poly = IRREDUCIBLE[field_degree]
    mask = q - 1
    chunk = field_degree
    vec_count = q ** n

    def gf_mul(x, y):
        z = 0
        for _ in range(field_degree):
            if y & 1:
                z ^= x
            y >>= 1
            x <<= 1
            if x & q:
                x ^= poly
        return z & mask

    fm = [[gf_mul(a, b) for b in range(q)] for a in range(q)]
    digits = [tuple((v >> (chunk * i)) & mask for i in range(n))
              for v in range(vec_count)]
    scalar = [[sum(fm[s][d] << (chunk * i) for i, d in enumerate(v))
               for v in digits] for s in range(q)]
    table = [[0] * vec_count for _ in range(vec_count)]
    for a in range(vec_count):
        for b in range(vec_count):
            acc = [0] * n
            for i, da in enumerate(digits[a]):
                for j, db in enumerate(digits[b][:n-i]):
                    acc[i+j] ^= fm[da][db]
            table[a][b] = sum(x << (chunk*i) for i, x in enumerate(acc))

    basis = [1 << (chunk * i) for i in range(n)]
    pairs = [(i, j) for i in range(n) for j in range(i, n)]
    identities = []
    for cols in product(range(vec_count), repeat=n):
        ok = True
        for i, j in pairs:
            lhs = table[cols[i]][cols[j]]
            argument = (table[basis[i]][cols[j]]
                        ^ table[cols[i]][basis[j]]
                        ^ table[basis[i]][basis[j]])
            rhs = 0
            for k, coeff in enumerate(digits[argument]):
                rhs ^= scalar[coeff][cols[k]]
            if lhs != rhs:
                ok = False
                break
        if ok:
            identities.append(cols)

    zero = (0,) * n
    identity = tuple(basis)
    constants = tuple([basis[0]] + [0] * (n-1))
    radical = tuple([0] + basis[1:])
    expected = {zero, identity, constants, radical}
    assert set(identities) == expected, (q, n, identities)
    return q, n, len(identities), vec_count**n


def main():
    cases = [(1, 2), (1, 3), (1, 4),
             (2, 2), (2, 3), (3, 2), (4, 2)]
    for degree, n in cases:
        q, n, found, tested = check(degree, n)
        print(f"F_{q}, dimension {n}: {found} solutions among {tested} maps")
    print("ALL_EXHAUSTIVE_CHECKS_PASSED")


if __name__ == '__main__':
    main()
