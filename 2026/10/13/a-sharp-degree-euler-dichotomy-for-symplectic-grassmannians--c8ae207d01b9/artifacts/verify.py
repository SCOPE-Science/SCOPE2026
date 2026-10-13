from fractions import Fraction
from math import factorial, comb

def degree_formula(n, k):
    d = k*(4*n - 3*k + 1)//2
    x = Fraction(2**(k*(k-1)//2) * factorial(d), 1)
    for i in range(k):
        x *= factorial(i)
    for i in range(1, k+1):
        x /= factorial(2*n - 2*i + 1)
    assert x.denominator == 1
    return x.numerator

def degree_root_product(n, k):
    d = k*(4*n - 3*k + 1)//2
    x = Fraction(factorial(d), 1)

    # Coroots e_i-e_j with i<=k<j.
    for i in range(1, k+1):
        for j in range(k+1, n+1):
            x /= (j-i)

    # Coroots e_i+e_j with i<j<=k contribute numerator 2.
    for i in range(1, k+1):
        for j in range(i+1, k+1):
            x *= Fraction(2, 2*n-i-j+2)

    # Coroots e_i+e_j with i<=k<j contribute numerator 1.
    for i in range(1, k+1):
        for j in range(k+1, n+1):
            x /= (2*n-i-j+2)

    # Long roots 2e_i have coroot e_i.
    for i in range(1, k+1):
        x /= (n-i+1)

    assert x.denominator == 1
    return x.numerator

def euler(n, k):
    return 2**k * comb(n, k)

pair_checks = root_checks = adjacent_checks = lagrangian_checks = 0

for n in range(1, 41):
    for k in range(1, n+1):
        D = degree_formula(n, k)
        assert D == degree_root_product(n, k)
        E = euler(n, k)

        below = (k == 1) or (n == 2 and k == 2)
        assert (D < E) == below
        assert (D > E) == (not below)
        assert D != E

        pair_checks += 1
        root_checks += 1

for k in range(2, 40):
    for n in range(k, 40):
        d = k*(4*n - 3*k + 1)//2
        a = n-k

        lhs = Fraction(degree_formula(n+1, k), degree_formula(n, k))
        rhs = Fraction(1, 1)
        for s in range(1, 2*k+1):
            rhs *= Fraction(d+s, 2*a+1+s)
        assert lhs == rhs

        normalized_now = Fraction(degree_formula(n, k), euler(n, k))
        normalized_next = Fraction(degree_formula(n+1, k), euler(n+1, k))
        assert normalized_next > normalized_now
        adjacent_checks += 1

for k in range(2, 40):
    K = k*(k+1)//2
    lhs = Fraction(degree_formula(k+1, k+1), degree_formula(k, k))
    rhs = Fraction(2**k * comb(K+k+1, k+1), comb(2*k+1, k+1))
    assert lhs == rhs
    if k >= 3:
        assert Fraction(degree_formula(k, k), 2**k) > 1
    lagrangian_checks += 1

assert degree_formula(2, 2) == 2 and euler(2, 2) == 4
assert degree_formula(3, 2) == 14 and euler(3, 2) == 12
assert degree_formula(3, 3) == 16 and euler(3, 3) == 8

print("VERIFY_OK", pair_checks, root_checks, adjacent_checks, lagrangian_checks)
