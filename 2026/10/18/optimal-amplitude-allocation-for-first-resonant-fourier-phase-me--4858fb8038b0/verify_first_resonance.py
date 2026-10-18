"""Exact checks for the first resonant phase-moment amplitude theorem.
Uses only the Python standard library. The all-frequency argument is the proof text;
these enumerations check independently chosen finite instances and sharp samples.
"""
from math import comb, factorial, gcd
from fractions import Fraction


def multinomial(r, u):
    return factorial(r) // (factorial(u[0]) * factorial(u[1]) * factorial(u[2]))


def terms(r, A, B):
    out = {}
    for j in range(r + 1):
        for k in range(r - j + 1):
            i = r - j - k
            out.setdefault(A * j + B * k, []).append(((i, j, k), multinomial(r, (i, j, k))))
    return out


cases = 0
for B in range(2, 15):
    for A in range(1, B):
        if gcd(A, B) != 1:
            continue
        for r in range(1, B + 1):
            table = terms(r, A, B)
            collisions = [v for v in table.values() if len(v) > 1]
            if r < B:
                assert collisions == [], (A, B, r)
            else:
                assert len(collisions) == 1
                assert len(collisions[0]) == 2
                pairs = {x[0]: x[1] for x in collisions[0]}
                assert pairs == {(0, B, 0): 1, (B - A, 0, A): comb(B, A)}
                for middle in [1, -1, 1j, -1j]:
                    S = 2 + abs(middle) ** 2
                    vals = []
                    for entries in table.values():
                        z = sum(k * middle ** u[1] for u, k in entries)
                        vals.append(z.real * z.real + z.imag * z.imag)
                    moment = int(round(sum(vals)))
                    diag = sum(k * k for entries in table.values() for _, k in entries)
                    response = 2 * comb(B, A) * (middle ** B).real
                    assert moment == diag + int(response), (A, B, middle)
            cases += 1
        # Square of the optimal normalized cosine amplitude, an exact rational number.
        sq = Fraction(4 * comb(B, A) ** 2 * (B - A) ** (B - A) * A ** A,
                      2 ** (2 * B) * B ** B)
        assert sq > 0
        if (A, B) == (1, 2):
            assert sq == Fraction(1, 4)
        if (A, B) == (1, 3):
            assert sq == Fraction(1, 12)
        # Check that optimal allocation strictly improves upon equal amplitudes.
        equal_sq = Fraction(4 * comb(B, A) ** 2, 3 ** (2 * B))
        assert sq > equal_sq, (A, B, sq, equal_sq)
print(f'VERIFY_OK collision_cases={cases} B_max=14 exact_first_response_and_allocation')
