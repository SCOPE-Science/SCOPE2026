from fractions import Fraction
from math import factorial


def evolve_scaled(n, steps):
    # B = sqrt(n) * amplitude, so B starts rational and stays rational.
    N = 1 << n
    a = [[Fraction(0) for _ in range(n)] for _ in range(N)]
    for i in range(n):
        a[0][i] = Fraction(1)
    for _ in range(steps):
        coined = [[Fraction(0) for _ in range(n)] for _ in range(N)]
        for x in range(N):
            s = sum(a[x])
            for i in range(n):
                coined[x][i] = Fraction(2, n) * s - a[x][i]
        b = [[Fraction(0) for _ in range(n)] for _ in range(N)]
        for x in range(N):
            for i in range(n):
                b[x ^ (1 << i)][i] += coined[x][i]
        a = b
    return a


def q_formula(n, w):
    return Fraction(factorial(w) * factorial(w - 1) * 4 ** (w - 1), n ** (2 * w - 1))


def c_formula(n, w):
    return Fraction(factorial(w), n ** w)


checks = 0
for n in range(2, 8):
    for w in range(1, n + 1):
        a = evolve_scaled(n, w)
        x = (1 << w) - 1
        # Actual probability is sum(B^2)/n because B=sqrt(n)*amplitude.
        p = sum(v * v for v in a[x]) / n
        q = q_formula(n, w)
        if p != q:
            raise AssertionError((n, w, p, q))
        ratio = q / c_formula(n, w)
        expected_ratio = Fraction(4 ** (w - 1) * factorial(w - 1), n ** (w - 1))
        if ratio != expected_ratio:
            raise AssertionError((n, w, ratio, expected_ratio))
        checks += 1

# Exact antipode identity in two algebraically different forms.
for n in range(2, 20):
    a = q_formula(n, n)
    b = Fraction((2 ** (n - 1) * factorial(n - 1)) ** 2, n ** (2 * n - 2))
    if a != b:
        raise AssertionError((n, a, b))

print(f"VERIFY_OK cases={checks} antipode_checks=18")
