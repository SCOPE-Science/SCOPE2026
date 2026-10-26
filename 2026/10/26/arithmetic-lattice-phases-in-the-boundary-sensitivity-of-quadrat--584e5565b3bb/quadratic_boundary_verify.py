"""Reproduce exact boundary sensitivity checks for quadratic discrete least squares.

Only Python's standard library is required. Finite tests supplement, but do not
replace, the mathematical argument for all sample counts.
"""
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction


def inverse3(matrix):
    a = [[Fraction(x) for x in row] + [Fraction(i == j) for j in range(3)]
         for i, row in enumerate(matrix)]
    for k in range(3):
        pivot = next(i for i in range(k, 3) if a[i][k])
        a[k], a[pivot] = a[pivot], a[k]
        z = a[k][k]
        a[k] = [x / z for x in a[k]]
        for i in range(3):
            if i != k:
                t = a[i][k]
                a[i] = [x - t * y for x, y in zip(a[i], a[k])]
    return [row[3:] for row in a]


def exact_row_from_gram(m):
    v = [[Fraction(1), Fraction(j), Fraction(j*j)] for j in range(m)]
    g = [[sum(v[j][a]*v[j][b] for j in range(m)) for b in range(3)]
         for a in range(3)]
    inv = inverse3(g)
    return [sum(inv[0][a]*v[j][a] for a in range(3)) for j in range(m)]


def exact_row_formula(m, j):
    q = 10*j*j + (6-12*m)*j + 3*m*m - 3*m + 2
    return Fraction(3*q, m*(m+1)*(m+2))


def bernoulli2(t):
    return t*t-t+Decimal(1)/6


def bernoulli3(t):
    return t*t*t-Decimal(3)*t*t/2+t/2


def asymptotic_and_phase_formula(m):
    with localcontext() as ctx:
        ctx.prec = 75
        M = Decimal(m)
        d = Decimal(6*m*m - 6*m - 11)
        root = d.sqrt()
        rlo = (6*M-3-root)/10
        rhi = (6*M-3+root)/10
        ceil_lo = rlo.to_integral_value(rounding=ROUND_CEILING)
        floor_hi = rhi.to_integral_value(rounding=ROUND_FLOOR)
        delta_lo = ceil_lo-rlo
        delta_hi = rhi-floor_hi
        gap = root/5
        den = M*(M+1)*(M+2)
        value = (Decimal(1) + 2*d*root/(25*den)
                 -30*gap*(bernoulli2(delta_lo)+bernoulli2(delta_hi))/den
                 +20*(bernoulli3(delta_lo)+bernoulli3(delta_hi))/den)
        return +value


def run():
    for m in range(3, 51):
        row = exact_row_from_gram(m)
        assert all(row[j] == exact_row_formula(m, j) for j in range(m)), m
    print('PASS: all 1175 Gram-inverse kernel coefficients, m=3,...,50')
    with localcontext() as ctx:
        ctx.prec = 70
        for m in range(3, 251):
            exact = sum(abs(exact_row_formula(m, j)) for j in range(m))
            derived = asymptotic_and_phase_formula(m)
            error = abs(Decimal(exact.numerator)/Decimal(exact.denominator)-derived)
            assert error < Decimal('1e-60'), (m, error)
        print('PASS: 248 boundary norm values match the Bernoulli identity to 60 digits')
        sqrt6 = Decimal(6).sqrt()
        lower = 119*sqrt6/50
        upper = 269*sqrt6/50
        assert Decimal(5) < lower < Decimal(6)
        assert Decimal(13) < upper < Decimal(14)
        print('Analytic second-order liminf and limsup:', lower, upper)
    print('NOTE: irrational equidistribution and infinite asymptotics require the proof.')


if __name__ == '__main__':
    run()
