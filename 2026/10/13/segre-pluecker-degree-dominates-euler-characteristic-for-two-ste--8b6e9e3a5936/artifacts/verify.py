from fractions import Fraction
from math import factorial

def degree_closed(n, k):
    a = k - 1
    b = n - k
    N = a*b + a + b
    num = factorial(N) * (2 ** b)
    for r in range(a):
        num *= factorial(r)
    den = factorial(a + b)
    for r in range(a):
        den *= factorial(b + r)
    assert num % den == 0
    return num // den

def degree_weyl(n, k):
    lam = [2] + [1] * (k - 1) + [0] * (n - k)
    prod = Fraction(1, 1)
    N = 0
    for i in range(n):
        for j in range(i + 1, n):
            d = lam[i] - lam[j]
            if d:
                N += 1
                prod *= Fraction(d, j - i)
    val = factorial(N) * prod
    assert val.denominator == 1
    return val.numerator

def euler(n, k):
    return factorial(n) // (factorial(k - 1) * factorial(n - k))

def ratio(a, b):
    n = a + b + 1
    k = a + 1
    return Fraction(degree_closed(n, k), euler(n, k))

family_checks = 0
for n in range(3, 81):
    for k in range(2, n):
        dc = degree_closed(n, k)
        dw = degree_weyl(n, k)
        e = euler(n, k)
        assert dc == dw
        if (n, k) == (3, 2):
            assert dc == e == 6
        else:
            assert dc > e
        family_checks += 1

ratio_checks = 0
for a in range(1, 61):
    for b in range(1, 61):
        N = a*b + a + b

        lhs_a = ratio(a + 1, b) / ratio(a, b)
        rhs_a_num = factorial(a + 1)
        for j in range(1, b + 2):
            rhs_a_num *= N + j
        rhs_a = Fraction(rhs_a_num, factorial(a + b + 2))
        assert lhs_a == rhs_a
        assert lhs_a > 1

        lhs_b = ratio(a, b + 1) / ratio(a, b)
        rhs_b_num = 2 * factorial(b + 1)
        for j in range(1, a + 2):
            rhs_b_num *= N + j
        rhs_b = Fraction(rhs_b_num, factorial(a + b + 2))
        assert lhs_b == rhs_b
        assert lhs_b > 1

        ratio_checks += 2

print("VERIFY_OK", family_checks, ratio_checks)
