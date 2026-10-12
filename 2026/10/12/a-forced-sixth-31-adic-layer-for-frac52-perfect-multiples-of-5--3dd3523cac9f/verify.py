from fractions import Fraction
from math import isqrt

def sigma_prime_power(p, e):
    return (p ** (e + 1) - 1) // (p - 1)

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d <= isqrt(n):
        if n % d == 0:
            return False
        d += 2
    return True

# Theorem 7 of Almeida--Cardoso is the external input: 2^4 || N,
# 5^2 || N, and 31^2 | N.  Everything below checks the new deductions.
I_core_c2 = Fraction(31, 16) * Fraction(31, 25) * Fraction(sigma_prime_power(31, 2), 31 ** 2)
assert I_core_c2 == Fraction(993, 400)

# If q is an additional prime divisor, 5/2 >= (993/400)(q+1)/q.
# Hence 7q >= 993, so q >= 142; the least prime at least 142 is 149.
assert 7 * 141 < 993 <= 7 * 142
least_prime = next(q for q in range(142, 1000) if is_prime(q))
assert least_prime == 149

expected = {
    2: Fraction(1000, 993),
    3: Fraction(3875, 3848),
    4: Fraction(192200, 190861),
    5: Fraction(3723875, 3697932),
}
small_obstructor = {2: 3, 3: 2, 4: 11, 5: 2}
for c in range(2, 6):
    I_u = Fraction(1000 * 31 ** c, 31 ** 2 * sigma_prime_power(31, c))
    assert I_u == expected[c]
    A, B = I_u.numerator, I_u.denominator
    assert B % small_obstructor[c] == 0
    assert small_obstructor[c] < 149
    # Reducedness is supplied by Fraction; B | u follows from B*sigma(u)=A*u.
    assert A > 0 and B > 1

print("VERIFY_OK core=993/400 cutoff_prime=149 rejected_31_exponents=2,3,4,5")
