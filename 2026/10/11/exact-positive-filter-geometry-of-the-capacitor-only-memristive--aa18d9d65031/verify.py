from fractions import Fraction


def check_filter(alpha, d, n, R, C):
    # C stands for cosh(x/(2n)); R stands for exp(u/(2n)).
    kappa = alpha * d / (2 * n)
    udot = alpha * d * (C / R - 1)
    chain = R * udot / (2 * n)
    target = kappa * (C - R)
    assert chain == target


def check_quadratic_coefficient(n):
    # cosh(r) >= 1 + r^2/2 and r=x/(2n).
    coeff = Fraction(1, 2) * Fraction(1, (2 * n) ** 2)
    assert coeff == Fraction(1, 8 * n * n)


for alpha in map(Fraction, [1, 2, 7]):
    for d in map(Fraction, [1, 3, 5]):
        for n in map(Fraction, [1, 2, 11]):
            for R in map(Fraction, [1, 2, 9]):
                for C in map(Fraction, [1, 3, 10]):
                    check_filter(alpha, d, n, R, C)
for n in (1, 2, 11):
    check_quadratic_coefficient(n)
print("VERIFY_OK")
