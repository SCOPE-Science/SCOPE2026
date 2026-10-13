from fractions import Fraction
from collections import Counter
from itertools import product
from math import factorial

def rise(n, r):
    z = 1
    for j in range(r):
        z *= n + j
    return z

def edir(indices, n):
    c = Counter(indices)
    num = 1
    for v in c.values():
        num *= factorial(v)
    return Fraction(num, rise(n, len(indices)))

def e_linear(a):
    n = len(a)
    return sum((a[i] * edir((i,), n) for i in range(n)), Fraction(0))

def e_power(a, r):
    n = len(a)
    total = Fraction(0)
    for idx in product(range(n), repeat=r):
        coeff = Fraction(1)
        for i in idx:
            coeff *= a[i]
        total += coeff * edir(idx, n)
    return total

def e_two(a, b):
    n = len(a)
    total = Fraction(0)
    for i in range(n):
        for j in range(n):
            total += a[i] * b[j] * edir((i, j), n)
    return total

def e_three(a, b, c):
    n = len(a)
    total = Fraction(0)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                total += a[i] * b[j] * c[k] * edir((i, j, k), n)
    return total

def cmoment(xs, r):
    n = len(xs)
    mean = Fraction(sum(xs), n)
    return sum(((Fraction(x) - mean) ** r for x in xs), Fraction(0)) / n

def verify(xs):
    n = len(xs)
    mean = Fraction(sum(xs), n)
    y = [Fraction(x) - mean for x in xs]
    y2 = [z*z for z in y]

    EA = e_linear(y)
    EB = e_linear(y2)
    EA2 = e_power(y, 2)
    EA3 = e_power(y, 3)
    EA4 = e_power(y, 4)
    EAB = e_two(y, y2)
    EB2 = e_two(y2, y2)
    EBA2 = e_three(y2, y, y)

    mu2 = cmoment(xs, 2)
    mu3 = cmoment(xs, 3)
    mu4 = cmoment(xs, 4)

    EV = EB - EA2
    cov = EAB - EA3
    EV2 = EB2 - 2 * EBA2 + EA4
    varV = EV2 - EV * EV

    f_varM = mu2 / (n + 1)
    f_EV = Fraction(n, n + 1) * mu2
    f_cov = Fraction(n, (n + 1) * (n + 2)) * mu3
    f_varV = Fraction(
        n * ((n + 1) ** 2 * mu4 - (n * n - 3) * mu2 * mu2),
        (n + 1) ** 2 * (n + 2) * (n + 3),
    )

    assert EA == 0
    assert EA2 == f_varM
    assert EV == f_EV
    assert cov == f_cov
    assert varV == f_varV
    assert varV >= 0
    return 6

def run():
    datasets = 0
    assertions = 0
    for n in range(2, 9):
        cases = [
            list(range(n)),
            [i*i - 3*i for i in range(n)],
            [(-1)**i * (i + 1) for i in range(n)],
            [0] * (n - 1) + [n],
            [2*i + (1 if i == n - 1 else 0) for i in range(n)],
        ]
        for xs in cases:
            datasets += 1
            assertions += verify(xs)
    print("VERIFY_OK")
    print(f"datasets={datasets}")
    print(f"exact_assertions={assertions}")
    print("max_N=8")

if __name__ == "__main__":
    run()
