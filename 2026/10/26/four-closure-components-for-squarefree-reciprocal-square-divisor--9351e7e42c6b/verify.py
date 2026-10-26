from fractions import Fraction


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


# Each row records a finite subset of primes q>p.  The exact product is
# checked against 1+p^{-2}; this certifies the corresponding tail inequality.
rows = [
    (5,  [7, 11, 13, 17, 19], Fraction(6403780000, 6149280137)),
    (7,  [11, 13, 17, 19],     Fraction(128075600, 125495513)),
    (11, [13, 17],             Fraction(2900, 2873)),
    (13, [17, 19],             Fraction(104980, 104329)),
    (17, [19, 23],             Fraction(191860, 190969)),
    (19, [23, 29],             Fraction(446260, 444889)),
    (23, [29, 31],             Fraction(810004, 808201)),
    (29, [31, 37],             Fraction(35620, 35557)),
]

for p, qs, stated_product in rows:
    assert is_prime(p)
    assert all(is_prime(q) and q > p for q in qs)
    product = Fraction(1, 1)
    for q in qs:
        product *= Fraction(q * q + 1, q * q)
    assert product == stated_product, (p, product, stated_product)
    assert product > Fraction(p * p + 1, p * p), (p, product)

# The bound 3.14 < pi implies pi^2 > 243/25 and pi^2 > 48/5,
# which are the only lower bounds needed to separate the intervals.
pi_lower_squared = Fraction(314, 100) ** 2
assert pi_lower_squared > Fraction(243, 25)
assert pi_lower_squared > Fraction(48, 5)

# Exact algebraic endpoint identities, with the common factor pi^{-2}
# left symbolic: B=54/(5*pi^2), (10/9)B=12/pi^2,
# (5/4)B=27/(2*pi^2), (25/18)B=15/pi^2.
assert Fraction(10, 9) * Fraction(54, 5) == Fraction(12, 1)
assert Fraction(5, 4) * Fraction(54, 5) == Fraction(27, 2)
assert Fraction(25, 18) * Fraction(54, 5) == Fraction(15, 1)

print("PASS: eight exact prime-tail product inequalities")
print("PASS: rational endpoint identities and interval-separation bounds")
print("LIMIT: the infinite tail for p>=31 uses the cited prime-counting theorem")
