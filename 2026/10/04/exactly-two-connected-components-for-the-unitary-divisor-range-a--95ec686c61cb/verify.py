from fractions import Fraction
import math

# Classical Archimedean enclosure.
pi2_lo = Fraction(223 * 223, 71 * 71)
pi2_hi = Fraction(22 * 22, 7 * 7)
assert pi2_lo < Fraction.from_float(math.pi * math.pi) < pi2_hi
assert pi2_lo > Fraction(246, 25)

# First primes through the range needed for fixed inequalities.
small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
for m in (3, 4, 6, 9):
    p = small_primes[m - 1]
    P = Fraction(1, 1)
    for q in small_primes[:m]:
        P *= Fraction(q*q + 1, q*q)
    L = Fraction(p**4 + p**2, p**4 + 1)
    B = Fraction(15, 1) / (P * L)
    assert pi2_hi < B

# Finite part of Defant's prime-ratio lemma: for j<3100 and outside
# the stated exceptional indices, p_{j+1}/p_j < 2^(1/3).
def first_primes(n):
    limit = 40000
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[0:2] = b'\x00\x00'
    r = int(limit ** 0.5)
    for k in range(2, r + 1):
        if sieve[k]:
            start = k*k
            sieve[start:limit+1:k] = b'\x00' * (((limit - start)//k) + 1)
    ps = [k for k, flag in enumerate(sieve) if flag]
    assert len(ps) >= n
    return ps[:n]

ps = first_primes(3101)
exceptions = {1, 2, 3, 4, 6, 9}
for j in range(1, 3100):  # j is 1-indexed
    if j in exceptions:
        continue
    p, q = ps[j-1], ps[j]
    assert q**3 < 2 * p**3

# Exact overlap/separation implications using pi^2 bounds.
# c2 < R = 54/(5*pi^2)
assert pi2_hi < Fraction(2187, 205)
# c2*R < c1, and final gap L < 25/18
assert pi2_lo > Fraction(246, 25)
# d4*A reaches B: pi^2 < 379332/38400
assert pi2_hi < Fraction(379332, 38400)
# d2*B starts before B ends: pi^2 < 864/85
assert pi2_hi < Fraction(864, 85)
# d1*A starts before d2*B ends: pi^2 < 51/5
assert pi2_hi < Fraction(51, 5)

lo = 41 / (3 * math.pi**2)
hi = 25 / 18
right = 15 / math.pi**2
assert lo < hi < right
print(f"VERIFY_OK gap=({lo:.12f},{hi:.12f}) right={right:.12f} prime_ratio_checks=3093")
