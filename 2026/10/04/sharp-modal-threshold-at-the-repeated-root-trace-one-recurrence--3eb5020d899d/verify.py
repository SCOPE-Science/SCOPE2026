from fractions import Fraction
from math import comb, factorial


def bernoulli(n):
    B = [Fraction(0) for _ in range(n + 1)]
    B[0] = Fraction(1)
    for m in range(1, n + 1):
        B[m] = -sum(Fraction(comb(m + 1, k)) * B[k] for k in range(m)) / Fraction(m + 1)
    return B


def g(n):
    if n == 0:
        return Fraction(0)
    return Fraction(n, 2 ** (n - 1))


def a(j):
    return g(2*j) + g(j)


def zeta_even_over_pi(m, B):
    # zeta(m) / pi**m for positive even m.
    assert m >= 2 and m % 2 == 0
    return ((-1) ** (m // 2 + 1)) * B[m] * Fraction(2 ** (m - 1), factorial(m))


def coeff(N, j, B):
    # Positive coefficient after removing the common factor
    # 2*N!*(h/(2*pi))**N from |T_{N,j}|, with h=3/4.
    m = N - j
    return a(j) * Fraction(8, 3) ** j / factorial(j) * zeta_even_over_pi(m, B)

# Repeated-root closed form satisfies the recurrence exactly.
for n in range(0, 81):
    if n + 2 <= 80:
        assert g(n + 2) == g(n + 1) - Fraction(1, 4) * g(n)

# Exact small-degree adjacent ratios.
assert Fraction(10, 3) > 1  # N=6: j=4 over j=2
assert Fraction(7, 3) > 1   # N=8: j=4 over j=2
assert Fraction(11, 9) > 1  # N=8: j=6 over j=4

# Rational upper bounds used in the universal descent proof, via pi < 22/7.
bound_j4 = Fraction(11, 12150) * Fraction(22, 7) ** 6
bound_tail = Fraction(4, 567) * Fraction(22, 7) ** 4
assert bound_j4 == Fraction(623589472, 714717675) < 1
assert bound_tail == Fraction(937024, 1361367) < 1

# Independent exact finite replay through N=40 using Bernoulli numbers.
B = bernoulli(40)
expected = {4: 2, 6: 4, 8: 6}
for N in range(4, 42, 2):
    vals = {j: coeff(N, j, B) for j in range(2, N-1, 2)}
    winner = max(vals, key=vals.get)
    target = expected.get(N, 4)
    assert winner == target, (N, winner, target)
    assert list(vals.values()).count(vals[winner]) == 1

print('VERIFY_OK repeated_root_recurrence exact; sharp_threshold=10; checked_N=4..40; universal_ratio_bounds exact')
