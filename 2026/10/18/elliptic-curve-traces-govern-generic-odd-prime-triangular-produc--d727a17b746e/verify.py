"""Exact finite-field and modular checks for triangular-product local densities.

Run with Python 3 (standard library only): python verify.py
The proof of the theorem for every prime is mathematical; finite tests
are supplementary checks, not a replacement for that proof.
"""
from fractions import Fraction


def character(t, p):
    t %= p
    if t == 0:
        return 0
    return 1 if pow(t, (p - 1) // 2, p) == 1 else -1


def data(p, n):
    m = (1 + 64 * n) % p
    assert p >= 5 and n % p and m
    A = Z = S_actual = 0
    for u in range(p):
        for v in range(p):
            F = ((u * u - 1) * (v * v - 1) + 64 * n) % p
            c = character(F, p)
            S_actual += c
            A += c == 1
            Z += c == 0
    S = 1 + p * character(n, p) * (3 + character(m, p))
    quartic = sum(character((u*u - 1) * (u*u - m), p) for u in range(p))
    trace = -1 - quartic
    assert S_actual == S
    assert Z == p - 3 - trace
    assert S_actual == 2*A + Z - p*p
    assert trace*trace <= 4*p
    density = Fraction(A, p*p) + Fraction(Z, 2*p*p*(p+1))
    predicted = (Fraction(1,2) + Fraction(S, 2*p*p)
                 - Fraction(p-3-trace, 2*p*(p+1)))
    assert density == predicted
    return density, Z, trace


number_cases = 0
for p in (5, 7, 11, 13, 17, 19, 23, 29):
    for n in range(1, p):
        if (1 + 64*n) % p:
            data(p, n)
            number_cases += 1
assert data(5,2)[0] == Fraction(4,75)
assert data(7,1)[0] == Fraction(149,196)

modular_checks = 0
for p, k, n in ((5,3,2), (7,3,1), (11,2,1), (13,2,2), (17,2,1)):
    modulus = p**k
    square_residues = {t*t % modulus for t in range(modulus)}
    count_lower = count_upper = count_zero = 0
    triangles = [t*(t+1)//2 % modulus for t in range(modulus)]
    for T1 in triangles:
        for T2 in triangles:
            q = (T1*T2 + n) % modulus
            if q in square_residues:
                count_upper += 1
                if q != 0:
                    count_lower += 1
            if q == 0:
                count_zero += 1
    density, Z, _ = data(p, n)
    lower = Fraction(count_lower, modulus*modulus)
    upper = Fraction(count_upper, modulus*modulus)
    assert lower <= density <= upper
    assert count_zero == Z * p**(k-1)
    assert upper - lower == Fraction(Z, p**(k+1))
    modular_checks += 1
print('VERIFICATION_OK')
print('finite_field_cases:', number_cases)
print('modular_bracketing_cases:', modular_checks)
print('examples: delta_5(2)=4/75, delta_7(1)=149/196')
