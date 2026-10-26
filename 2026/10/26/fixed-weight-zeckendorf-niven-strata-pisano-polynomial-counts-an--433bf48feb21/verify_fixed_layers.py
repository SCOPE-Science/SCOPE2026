"""Exact integer checks for fixed-weight Zeckendorf-Niven strata.

No external dependencies. Enumerations are finite consistency checks, not
substitutes for the general combinatorial proof.
"""
from fractions import Fraction
from itertools import combinations
from math import factorial


def fib_mod_cycle(modulus):
    a, b = 0, 1
    out = []
    while True:
        out.append(a)
        a, b = b % modulus, (a + b) % modulus
        if (a, b) == (0, 1 % modulus):
            return out


def convolution(x, y):
    m = len(x)
    return [sum(x[j] * y[(r-j) % m] for j in range(m)) for r in range(m)]


def period_coefficients(m):
    residues = fib_mod_cycle(m)
    h = len(residues)
    a = [residues.count(r) for r in range(m)]
    b = [sum(2 * f % m == r for f in residues) for r in range(m)]
    power = [[1] + [0] * (m - 1)]
    for _ in range(m):
        power.append(convolution(power[-1], a))
    t_m = power[m][0]
    u_m = convolution(b, power[m - 2])[0]
    t_prev = power[m - 1][0]
    leading = Fraction(t_m, factorial(m))
    second = -Fraction(u_m, 2 * factorial(m - 2)) - Fraction(t_prev, factorial(m - 2))
    return h, leading, second, Fraction(t_m, h**m)


def count_dp(m, length):
    a, b = 0, 1
    residues = []
    for i in range(length + 2):
        residues.append(a)
        a, b = b % m, (a + b) % m
    d0 = [[0] * m for _ in range(m + 1)]
    d1 = [[0] * m for _ in range(m + 1)]
    d0[0][0] = 1
    for i in range(2, length + 2):
        n0 = [[d0[k][r] + d1[k][r] for r in range(m)] for k in range(m + 1)]
        n1 = [[0] * m for _ in range(m + 1)]
        f = residues[i]
        for k in range(1, m + 1):
            for r in range(m):
                n1[k][(r + f) % m] += d0[k - 1][r]
        d0, d1 = n0, n1
    return d0[m][0] + d1[m][0]


def count_brute(m, length):
    fib = [0, 1]
    for _ in range(length + 2):
        fib.append(fib[-1] + fib[-2])
    good = 0
    for inds in combinations(range(2, length + 2), m):
        if any(y == x + 1 for x, y in zip(inds, inds[1:])):
            continue
        good += sum(fib[i] for i in inds) % m == 0
    return good


def newton_top_coefficients(values, degree):
    # Integer-valued polynomial evaluated at q=1,2,...,degree+1.
    # The forward-difference expansion uses binomial(q-1,k).
    differences = []
    row = list(values)
    while row:
        differences.append(row[0])
        row = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    a = Fraction(differences[degree], factorial(degree))
    b = (Fraction(differences[degree - 1], factorial(degree - 1))
         - Fraction(degree * (degree + 1) * differences[degree],
                    2 * factorial(degree)))
    return a, b


def main():
    formulas = {
        2: lambda q: Fraction(5*q*q-5*q+2, 2),
        3: lambda q: Fraction(85*q**3-99*q*q+35*q-6, 3),
        4: lambda q: Fraction(28*q**4-84*q**3+91*q*q-45*q+10, 2),
        5: lambda q: (Fraction(16000, 3)*q**5-8000*q**4+
                      Fraction(14200,3)*q**3-1380*q*q+
                      Fraction(559,3)*q-14),
    }
    expected = {
        2: (3, Fraction(5,2), Fraction(-5,2), Fraction(5,9)),
        3: (8, Fraction(85,3), Fraction(-33), Fraction(85,256)),
        4: (6, Fraction(14), Fraction(-42), Fraction(7,27)),
        5: (20, Fraction(16000,3), Fraction(-8000), Fraction(1,5)),
    }
    direct = 0
    for m in range(2, 8):
        for length in range(0, 19):
            assert count_dp(m, length) == count_brute(m, length), (m, length)
            direct += 1
    form_checks = 0
    for m, formula in formulas.items():
        h, leading, second, probability = period_coefficients(m)
        assert (h, leading, second, probability) == expected[m], (m, h, leading, second, probability)
        for q in range(1, 17):
            target = formula(q)
            assert target.denominator == 1
            assert count_dp(m, q*h) == int(target), (m, q)
            form_checks += 1
    # Independent extraction of leading and second coefficients from exact
    # finite-index transfer counts, for additional natural weights.
    top_checks = 0
    for m in range(2, 11):
        h, lead, second, _ = period_coefficients(m)
        if h <= m:
            continue
        values = [count_dp(m, q * h) for q in range(1, m + 2)]
        assert newton_top_coefficients(values, m) == (lead, second)
        top_checks += 1
    print(f'VERIFY_OK brute_vs_dp={direct} exact_polynomial_checks={form_checks} '+
          f'Pisano_convolutions=4 two_top_coefficients={top_checks} rational_arithmetic=PASS')


if __name__ == '__main__':
    main()
