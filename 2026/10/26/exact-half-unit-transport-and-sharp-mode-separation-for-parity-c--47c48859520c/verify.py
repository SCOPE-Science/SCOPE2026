"""Finite exact check of parity-conditional CDF sandwich and sharp modes.

Checks do not replace the infinite-family Hermite--Biehler proof.
"""
from fractions import Fraction
from itertools import product


def convolve(a, b):
    c = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def verify(factors):
    d = [Fraction(1)]
    for f in factors:
        d = convolve(d, f)
    ev, od = d[::2], d[1::2]
    pe, po = sum(ev), sum(od)
    if not pe or not po:
        return False
    ev, od = [v / pe for v in ev], [v / po for v in od]
    cum_e = cum_o = Fraction(0)
    # J <=st K <=st J+1: F_K(k) <= F_J(k) <= F_K(k+1).
    for k in range(len(od)):
        cum_e += ev[k]
        cum_o += od[k]
        assert cum_e <= cum_o
        assert cum_o <= cum_e + ev[k + 1]
    modes_e = [i for i, p in enumerate(ev) if p == max(ev)]
    modes_o = [Fraction(2 * i + 1, 2) for i, p in enumerate(od) if p == max(od)]
    assert all(abs(e - o) <= Fraction(3, 2) for e in modes_e for o in modes_o)
    return True


def main():
    for denominator in (2, 3):
        triples = [tuple(Fraction(v, denominator) for v in (l, t, denominator - l - t))
                   for l in range(denominator + 1)
                   for t in range(denominator + 1 - l)]
        count = 0
        for n in range(1, 6):
            for factors in product(triples, repeat=n):
                count += verify(factors)
        print(f'Grid denominator {denominator}: {count} nondegenerate instances passed')
    a = (Fraction(0), Fraction(1, 4), Fraction(3, 4))
    b = (Fraction(1, 2), Fraction(0), Fraction(1, 2))
    assert verify((a, b))
    d = convolve(a, b)
    ev, od = d[::2], d[1::2]
    assert [v / sum(ev) for v in ev] == [Fraction(0), Fraction(1, 2), Fraction(1, 2)]
    assert [v / sum(od) for v in od] == [Fraction(1, 2), Fraction(1, 2)]
    print('Sharp 3/2 mode separation witness passed')


if __name__ == '__main__':
    main()
