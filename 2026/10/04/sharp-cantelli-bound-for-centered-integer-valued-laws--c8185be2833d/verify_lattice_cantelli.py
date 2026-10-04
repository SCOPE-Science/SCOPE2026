#!/usr/bin/env python3
from fractions import Fraction

def sharp_bound(v, k):
    j = v // k
    return Fraction(v + j * (j + 1), (k + j) * (k + j + 1))

def masses(v, k):
    j = v // k
    a = Fraction(v + j * (j + 1), (k + j) * (k + j + 1))
    b = Fraction(k * (j + 1) - v, k + j)
    c = Fraction(v - k * j, k + j + 1)
    return j, a, b, c

def certificate(x, k, j):
    return Fraction((x + j) * (x + j + 1), (k + j) * (k + j + 1))

def run():
    cases = 0
    lattice_checks = 0
    for k in range(1, 21):
        for den in range(1, 13):
            for num in range(0, 121):
                v = Fraction(num, den)
                j, a, b, c = masses(v, k)
                assert a >= 0 and b >= 0 and c >= 0
                assert a + b + c == 1
                assert k * a - j * b - (j + 1) * c == 0
                assert k * k * a + j * j * b + (j + 1) * (j + 1) * c == v
                assert a == sharp_bound(v, k)

                r = v - k * j
                cantelli = Fraction(v, v + k * k) if v != 0 else Fraction(0)
                gap = cantelli - a
                rhs = Fraction(r * (k - r), (k + j) * (k + j + 1) * (v + k * k))
                assert gap == rhs
                assert gap >= 0
                assert (gap == 0) == (r == 0)

                for x in range(-60, 81):
                    assert certificate(x, k, j) >= (1 if x >= k else 0)
                    lattice_checks += 1

                for x in (-(j + 1), -j, k):
                    assert certificate(x, k, j) == (1 if x >= k else 0)

                cases += 1
    print(f"VERIFY_OK cases={cases} lattice_checks={lattice_checks}")

if __name__ == "__main__":
    run()
