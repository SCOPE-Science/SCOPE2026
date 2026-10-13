from fractions import Fraction
from math import factorial, comb

def degree(k, n):
    r = n-k
    x = Fraction(factorial(k*r), 1)
    for i in range(1, k):
        x *= factorial(i)
    for j in range(k):
        x /= factorial(r+j)
    assert x.denominator == 1
    return x.numerator

checks = ratio_k_checks = ratio_n_checks = central_checks = 0

for n in range(2, 101):
    for k in range(1, n):
        D = degree(k, n)
        E = comb(n, k)
        s = min(k, n-k)
        expected_less = (s == 1) or (s == 2 and n <= 6)
        expected_greater = not expected_less
        assert (D < E) == expected_less, (n, k, D, E)
        assert (D > E) == expected_greater, (n, k, D, E)
        assert D != E
        checks += 1

    # Toward-center degree quotient.
    for k in range(1, n//2):
        r = n-k
        M = k*r
        q = r-k-1
        lhs = Fraction(degree(k+1, n), degree(k, n))
        if q == 0:
            rhs = Fraction(1, 1)
        else:
            rhs = Fraction(1, 1)
            for s in range(1, q+1):
                rhs *= Fraction(M+s, k+s)
        assert lhs == rhs
        assert lhs >= 1
        ratio_k_checks += 1

for n in range(4, 100):
    Dn = degree(2, n)
    Dnext = degree(2, n+1)
    Rn = Fraction(Dn, comb(n, 2))
    Rnext = Fraction(Dnext, comb(n+1, 2))
    rhs = Fraction(2*(2*n-3)*(n-1), n*(n+1))
    assert Rnext / Rn == rhs
    assert rhs > 1
    ratio_n_checks += 1

for n in range(6, 101):
    assert degree(3, n) > comb(n, n//2)
    central_checks += 1

assert degree(2, 6) == 14 and comb(6, 2) == 15
assert degree(2, 7) == 42 and comb(7, 2) == 21
assert degree(3, 6) == 42 and comb(6, 3) == 20

print("VERIFY_OK", checks, ratio_k_checks, ratio_n_checks, central_checks)
