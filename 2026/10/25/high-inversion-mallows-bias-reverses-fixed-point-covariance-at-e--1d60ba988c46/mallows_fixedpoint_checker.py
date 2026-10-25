"""Exact finite permutation checks for fixed points/inversions under Mallows weights.

Independent finite computations are diagnostic, not a proof for arbitrary n.
Only the Python standard library is needed. Run: python mallows_fixedpoint_checker.py
"""
from fractions import Fraction
from itertools import permutations
from math import factorial

checks = 0


def verify(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def polynomial_mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def value(a, x):
    y = Fraction(0)
    for c in reversed(a):
        y = y * x + c
    return y


def deriv(a):
    return [j * a[j] for j in range(1, len(a))]


def reversal_coeff(n):
    r = tuple(range(n - 1, -1, -1))
    delta = n % 2
    total = 0
    for j in range(n - 1):
        s = list(r)
        s[j], s[j + 1] = s[j + 1], s[j]
        total += sum(s[i] == i for i in range(n)) - delta
    return total


for n in range(2, 9):
    N = n * (n - 1) // 2
    a = [0] * (N + 1)
    f = [0] * (N + 1)
    for p in permutations(range(n)):
        k = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        a[k] += 1
        f[k] += sum(p[i] == i for i in range(n))
    verify(sum(a) == factorial(n), f'factorial n={n}')
    product = [1]
    for j in range(1, n + 1):
        product = polynomial_mul(product, [1] * j)
    verify(a == product, f'q-factorial n={n}')
    verify(a[0] == a[-1] == 1 and a[1] == n - 1,
           f'extremal inversion levels n={n}')
    verify(f[0] == n and f[-1] == n % 2,
           f'extremal fixed points n={n}')
    verify(f[1] - n * a[1] == -2 * (n - 1),
           f'near-identity derivative n={n}')
    verify(reversal_coeff(n) == (-2 if n % 2 else 2),
           f'near-reversal derivative n={n}')
    for k, count in enumerate(a):
        verify(count <= n ** k, f'inversion coefficient bound n={n} k={k}')
        verify(abs(f[k] - n * count) <= 2 * k * count,
               f'near-identity Lipschitz n={n} k={k}')
        verify(abs(f[N - k] - (n % 2) * a[N - k]) <= 2 * k * a[N - k],
               f'near-reversal Lipschitz n={n} k={k}')
    da, df = deriv(a), deriv(f)
    for q in (Fraction(1, 4), Fraction(1, 2), Fraction(1),
              Fraction(2), Fraction(4), Fraction(1, 100 * n * n),
              Fraction(100 * n * n)):
        z = value(a, q)
        numerator = value(df, q) * z - value(f, q) * value(da, q)
        cov = q * numerator / (z * z)
        e_f = value(f, q) / z
        e_inv = q * value(da, q) / z
        e_both = q * value(df, q) / z
        verify(cov == e_both - e_f * e_inv,
               f'covariance direct-vs-derivative n={n} q={q}')
        if q == 1:
            verify(cov == Fraction(-(n + 1), 6),
                   f'uniform covariance n={n}')
        if q == Fraction(1, 100 * n * n):
            verify(cov < 0, f'weak tilt sign n={n}')
        if q == Fraction(100 * n * n):
            verify(cov > 0 if n % 2 else cov < 0,
                   f'strong tilt parity sign n={n}')

# First odd sample size: exact rational identity at every q, not just sampled q.
n = 3
numerator_poly = [0] * 7
A = [1, 2, 2, 1]
# Regenerate polynomials from complete enumeration as an independent pathway.
a = [0] * 4
f = [0] * 4
for p in permutations(range(3)):
    k = sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))
    a[k] += 1
    f[k] += sum(p[i] == i for i in range(3))
verify(a == A, 'n=3 q-factorial')
for q in (Fraction(1, 7), Fraction(1, 2), Fraction(1), Fraction(2),
          Fraction(3), Fraction(4), Fraction(13, 2)):
    direct = q * (value(deriv(f), q) * value(a, q) -
                  value(f, q) * value(deriv(a), q)) / value(a, q) ** 2
    formula = 2 * q * (q * q - 2 * q - 2) / (q * q + q + 1) ** 2
    verify(direct == formula, f'n=3 exact formula q={q}')

print(f'PASS: {checks} exact checks; n=2..8; finite checks supplement analytic all-n proof.')
