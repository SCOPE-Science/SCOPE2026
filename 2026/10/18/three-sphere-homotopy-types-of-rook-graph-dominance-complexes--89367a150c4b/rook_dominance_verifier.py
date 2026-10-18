#!/usr/bin/env python3
"""Finite checks for the dominance complex of rectangular rook graphs.

Run with Python 3.10+. All calculations are exact integer or GF(2) arithmetic.
The all-parameter homotopy statement is established separately by proof,
not inferred from these finite tests.
"""
from collections import defaultdict


def predicted_dims(p, q):
    return [p * q - p - 1, p * q - q - 1, p * q - p - q + 1]


def face_data(p, q):
    n = p * q
    row = [sum(1 << (i * q + j) for j in range(q)) for i in range(p)]
    col = [sum(1 << (i * q + j) for i in range(p)) for j in range(q)]
    closed = [row[i] | col[j] for i in range(p) for j in range(q)]
    faces = defaultdict(list)
    for mask in range(1 << n):
        by_dominating = all((mask & neighborhood) != neighborhood for neighborhood in closed)
        a = all(mask & r != r for r in row)
        b = all(mask & c != c for c in col)
        assert by_dominating == (a or b), (p, q, mask)
        if by_dominating:
            faces[mask.bit_count() - 1].append(mask)
    return faces


def reduced_betti_mod2(faces):
    top = max(faces)
    ranks = {0: 0}
    for k in range(1, top + 1):
        below = {mask: idx for idx, mask in enumerate(faces[k - 1])}
        pivots = {}
        for mask in faces[k]:
            vector = 0
            bits = mask
            while bits:
                bit = bits & -bits
                bits -= bit
                vector ^= 1 << below[mask ^ bit]
            while vector:
                lead = vector.bit_length() - 1
                if lead not in pivots:
                    pivots[lead] = vector
                    break
                vector ^= pivots[lead]
        ranks[k] = len(pivots)
    betti = [len(faces[k]) - ranks.get(k, 0) - ranks.get(k + 1, 0)
             for k in range(top + 1)]
    betti[0] -= 1
    return {k: b for k, b in enumerate(betti) if b}


def main():
    for p, q in ((2, 2), (2, 3), (2, 4), (2, 5),
                 (3, 3), (3, 4), (4, 4)):
        faces = face_data(p, q)
        dims = predicted_dims(p, q)
        expected = defaultdict(int)
        for d in dims:
            expected[d] += 1
        chi_tilde = sum((-1) ** k * len(faces[k]) for k in range(max(faces) + 1)) - 1
        pred_chi_tilde = sum((-1) ** d for d in dims)
        assert chi_tilde == pred_chi_tilde, (p, q, chi_tilde, pred_chi_tilde)
        if p * q <= 12:
            got = reduced_betti_mod2(faces)
            assert got == dict(expected), (p, q, got, dict(expected))
            print(f'{p}x{q} PASS: {sum(len(faces[k]) for k in range(max(faces) + 1))} nonempty faces; '
                  f'GF2 Betti={got}; reduced Euler={chi_tilde}')
        else:
            print(f'{p}x{q} PASS: {sum(len(faces[k]) for k in range(max(faces) + 1))} nonempty faces; '
                  f'reduced Euler={chi_tilde}; mod2 ranks not enumerated')
    print('ALL FINITE CHECKS PASSED')


if __name__ == '__main__':
    main()
