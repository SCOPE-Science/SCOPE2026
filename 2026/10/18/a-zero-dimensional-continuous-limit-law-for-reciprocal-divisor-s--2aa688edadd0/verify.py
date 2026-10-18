"""Finite exact checks for the reciprocal-divisor law over prime fields.

No infinite or independence assertion is certified by finite computation.
"""
from fractions import Fraction
from math import comb


def degree(poly, q):
    k = 0
    while poly >= q:
        poly //= q
        k += 1
    return k


def coeffs(poly, q):
    out = []
    while poly:
        out.append(poly % q)
        poly //= q
    return out or [0]


def divides(f, d, q):
    a = coeffs(f, q)
    b = coeffs(d, q)
    while len(a) >= len(b):
        lead = a[-1] * pow(b[-1], -1, q) % q
        shift = len(a) - len(b)
        for j, bj in enumerate(b):
            a[shift + j] = (a[shift + j] - lead * bj) % q
        while a and a[-1] == 0:
            a.pop()
    return not a


def second_expected(q, n):
    # [u^n] (1-u^2/q)/((1-qu)(1-u)^2(1-u/q)) / q^n.
    def coef(k):
        if k < 0:
            return Fraction(0)
        return sum((Fraction(q**a) * (b+1) / q**c
                    for a in range(k+1)
                    for b in range(k-a+1)
                    for c in [k-a-b]), Fraction(0))
    return (coef(n) - coef(n-2)/q) / q**n

for q, max_n in [(2, 8), (3, 5)]:
    for n in range(max_n + 1):
        monic_n = [q**n + t for t in range(q**n)]
        all_monic = [(q**j + t, j) for j in range(n+1) for t in range(q**j)]
        A = []
        for f in monic_n:
            v = sum((Fraction(1, q**j) for d, j in all_monic if divides(f, d, q)), Fraction(0))
            A.append(v)
        mean = sum(A, Fraction(0))/len(A)
        sec = sum((a*a for a in A), Fraction(0))/len(A)
        assert mean == sum((Fraction(1, q**j) for j in range(n+1)), Fraction(0)), (q,n,mean)
        assert sec == second_expected(q,n), (q,n,sec,second_expected(q,n))
        print(f'q={q} degree={n} monic={len(A)} mean={mean} second={sec}')
print('VERIFY_OK')
