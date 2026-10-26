#!/usr/bin/env python3
"""Exact independent coefficient expansion and iteration checks for Hurwitz Cartier ranks.
The universal theorem is proved in RESULT.md; this program tests finite prime-power cases."""
from math import factorial


def verify_case(p, e):
    assert p >= 2 and all(p % d for d in range(2, int(p**0.5) + 1))
    q = p ** e
    basis = [(i, j) for i in range(q) for j in range(q - i)]
    positions = set(basis)
    coeff_fact = factorial(p - 1)
    edges = {}
    for i, j in basis:
        terms = []
        # Expand (x^(q+1)y + y^(q+1) + x)^(p-1) independently,
        # retaining the x^(p-1),y^(p-1) congruence terms.
        for A in range(p):
            for B in range(p - A):
                C = p - 1 - A - B
                xx = (q + 1) * A + C + i
                yy = A + (q + 1) * B + j
                if xx % p == p - 1 and yy % p == p - 1:
                    u = (xx - p + 1) // p
                    v = (yy - p + 1) // p
                    scalar = (coeff_fact // (factorial(A) * factorial(B) * factorial(C))) % p
                    assert scalar != 0 and (u, v) in positions
                    terms.append(((u, v), scalar))
        assert len(terms) <= 1
        edges[(i, j)] = terms[0][0] if terms else None
    outputs = [z for z in edges.values() if z is not None]
    assert len(outputs) == len(set(outputs)), 'Nonmonomial rank cancellation possible'

    R = []
    for r in range(e + 2):
        image = set()
        for start in basis:
            z = start
            for _ in range(r):
                if z is None:
                    break
                z = edges[z]
            if z is not None:
                image.add(z)
        measured = len(image)
        t = min(r, e)
        T = p * (p + 1) // 2
        h = p ** (e - t)
        expected = T**t * h * (h + 1) // 2
        assert measured == expected, (p, e, r, measured, expected)
        R.append(measured)
    assert R[-1] == R[-2]
    s = q // p
    known_a = s * (s - 1) * p * (p - 1) // 4
    assert R[0] - R[1] == known_a
    jordan = [R[j - 1] - 2 * R[j] + R[j + 1] for j in range(1, e + 1)]
    assert all(m >= 0 for m in jordan)
    assert sum((j + 1) * m for j, m in enumerate(jordan)) == R[0] - R[-1]
    print('p=', p, 'e=', e, 'g=', len(basis), 'rank_profile=', R, 'nilpotent_blocks=', jordan)


if __name__ == '__main__':
    for p, exponents in [(2, [1, 2, 3, 4, 5]),
                         (3, [1, 2, 3, 4]), (5, [1, 2, 3]),
                         (7, [1, 2]), (11, [1, 2])]:
        for e in exponents:
            verify_case(p, e)
    print('VERIFY_OK')
