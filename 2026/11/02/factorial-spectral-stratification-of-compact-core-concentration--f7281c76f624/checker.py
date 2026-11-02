"""Exact finite checks for compact-core concentration in polyanalytic Bergman spaces.

Standard-library-only.  The checks establish the indicated finite identities;
they do not replace the all-orders asymptotic proof in RESULT.md.
"""
from fractions import Fraction
from math import factorial


def determinant(rows):
    n = len(rows)
    a = [[Fraction(x) for x in row] for row in rows]
    out = Fraction(1)
    for j in range(n):
        p = next((i for i in range(j, n) if a[i][j]), None)
        if p is None:
            return Fraction(0)
        if p != j:
            a[j], a[p] = a[p], a[j]
            out = -out
        pivot = a[j][j]
        out *= pivot
        for i in range(j + 1, n):
            v = a[i][j] / pivot
            for col in range(j + 1, n):
                a[i][col] -= v * a[j][col]
            a[i][j] = Fraction(0)
    return out


def reciprocal_factorial(d):
    return Fraction(0) if d < 0 else Fraction(1, factorial(d))


def gram(q, m, radius_sq):
    return [[radius_sq ** (m + i + j + 1) / Fraction(m + i + j + 1)
             for j in range(q)] for i in range(q)]


def checks():
    n = 0
    for q in range(3, 9):
        for k in range(1, q + 1):
            rows = [[reciprocal_factorial(q-k+j-i) for j in range(k)]
                    for i in range(k)]
            predicted = Fraction(1)
            for r in range(k):
                predicted *= factorial(r)
            for r in range(q - k, q):
                predicted /= factorial(r)
            assert determinant(rows) == predicted, ('minor', q, k)
            n += 1
    for q in range(3, 7):
        for m in (0, 1, 3, 7, 13):
            for s in (Fraction(1, 2), Fraction(2, 3), Fraction(4, 5)):
                base = determinant(gram(q, m, Fraction(1)))
                local = determinant(gram(q, m, s))
                assert base > 0 and local > 0
                assert local / base == s ** (q * (m + q)), ('Gram', q, m, s)
                n += 1
    for q in range(3, 9):
        for k in range(1, q + 1):
            a = Fraction(1)
            for r in range(k):
                a *= factorial(r)
            for r in range(q-k, q):
                a /= factorial(r)
            if k == 1:
                prev = Fraction(1)
            else:
                prev = Fraction(1)
                for r in range(k-1):
                    prev *= factorial(r)
                for r in range(q-k+1, q):
                    prev /= factorial(r)
            assert a/prev == Fraction(factorial(k-1), factorial(q-k))
            n += 1
    print(f'PASS: {n} exact rational determinant and factorial identities')

if __name__ == '__main__':
    checks()
