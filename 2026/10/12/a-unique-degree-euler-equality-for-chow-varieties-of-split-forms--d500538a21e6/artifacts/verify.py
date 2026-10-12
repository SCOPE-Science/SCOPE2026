from math import factorial, comb, prod
from fractions import Fraction

def degree(n, d):
    return factorial(n*d) // (factorial(d) * factorial(n)**d)

def euler(n, d):
    return comb(n+d, d)

def sign_expected(n, d):
    if n == 1 or d == 1 or (n, d) == (2, 2):
        return -1
    if (n, d) == (3, 2):
        return 0
    return 1

checks = ratio_checks = 0
for n in range(1, 61):
    for d in range(1, 61):
        D = degree(n, d)
        E = euler(n, d)
        sign = (D > E) - (D < E)
        assert sign == sign_expected(n, d), (n, d, D, E, sign)

        # Independent multinomial top-intersection reconstruction.
        top = factorial(n*d) // (factorial(n)**d)
        assert top % factorial(d) == 0
        assert top // factorial(d) == D
        checks += 1

for n in range(2, 40):
    for d in range(2, 40):
        R = Fraction(degree(n, d), euler(n, d))

        Rd = Fraction(degree(n, d+1), euler(n, d+1))
        rhs_d = Fraction(
            prod(n*d + j for j in range(1, n+1)),
            factorial(n) * (n+d+1)
        )
        assert Rd / R == rhs_d
        assert rhs_d > 1

        Rn = Fraction(degree(n+1, d), euler(n+1, d))
        rhs_n = Fraction(
            prod(n*d + j for j in range(1, d+1)),
            (n+1)**(d-1) * (n+d+1)
        )
        assert Rn / R == rhs_n
        assert rhs_n > 1
        ratio_checks += 2

assert degree(2, 2) == 3 and euler(2, 2) == 6
assert degree(3, 2) == 10 and euler(3, 2) == 10
assert degree(2, 3) == 15 and euler(2, 3) == 10

print("VERIFY_OK", checks, ratio_checks)
