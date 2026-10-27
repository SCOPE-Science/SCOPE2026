"""Independent finite checks of multiset deletion-ball fluctuations.

Run with Python 3: python verify.py
Finite checks corroborate, but do not prove, the asymptotic theorem.
"""
from collections import Counter
from itertools import product
from math import comb
from fractions import Fraction


def compositions(n, q):
    if q == 1:
        yield (n,)
    else:
        for a in range(n + 1):
            for rest in compositions(n - a, q - 1):
                yield (a,) + rest


def moves(q, r):
    return tuple(z for z in product(range(-r, r + 1), repeat=q)
                 if sum(z) == 0 and sum(max(v, 0) for v in z) <= r)


def k_count(d, s, u):
    if u == 0:
        return comb(s + d - 1, d - 1)
    return sum(comb(d, j) * comb(u - 1, j - 1)
               * comb(s + u + d - j - 1, d - j - 1)
               for j in range(1, min(d - 1, u) + 1))


def delta(q, r, a):
    return sum(k_count(q - 1, s, u) for s in range(a + 1, r + 1)
               for u in range(r - s + 1))


def omega(q, r, a, b):
    if q == 2:
        return 0
    return sum(k_count(q - 2, s + t, u)
               for s in range(a + 1, r + 1)
               for t in range(b + 1, r - s + 1)
               for u in range(r - s - t + 1))


def volume(x, zs):
    return sum(all(x[i] + z[i] >= 0 for i in range(len(x))) for z in zs)


def check():
    total_centers = 0
    for q in range(2, 6):
        for r in range(1, 4):
            zs = moves(q, r)
            h = len(zs)
            for a in range(r):
                x = (a,) + (r,) * (q - 1)
                assert h - volume(x, zs) == delta(q, r, a)
                assert delta(q, r, a) == sum(z[0] < -a for z in zs)
                for b in range(r):
                    assert omega(q, r, a, b) == sum(z[0] < -a and z[1] < -b for z in zs)
            for n in range(1, 10):
                for x in compositions(n, q):
                    total_centers += 1
                    vol = volume(x, zs)
                    expected = h - sum(delta(q, r, x[i]) for i in range(q) if x[i] < r)
                    # Inclusion-exclusion is exact for at most two small coordinates.
                    small = [i for i in range(q) if x[i] < r]
                    if len(small) <= 2:
                        if len(small) == 2:
                            expected += omega(q, r, x[small[0]], x[small[1]])
                        assert vol == expected, (q, r, n, x, vol, expected)
    for n in range(6, 22):
        zs = moves(3, 2)
        hist = Counter(volume(x, zs) for x in compositions(n, 3))
        wanted = {19: comb(n-4,2),16: 3*(n-4),13: 3,
                  12: 3*(n-3),9: 6,6: 3}
        assert hist == wanted, (n, hist, wanted)
        den = comb(n+2,2)
        ed = sum((19-v)*m for v,m in hist.items())
        ed2 = sum((19-v)**2*m for v,m in hist.items())
        assert Fraction(ed,den) == Fraction(60*n+36,(n+1)*(n+2))
        assert Fraction(ed2,den) == Fraction(348*n+1332,(n+1)*(n+2))
        var = Fraction(ed2,den) - Fraction(ed,den)**2
        formula = Fraction(348*n+1332,(n+1)*(n+2)) - Fraction(60*n+36,(n+1)*(n+2))**2
        assert var == formula
    assert delta(3,2,0) == 7 and delta(3,2,1) == 3
    assert omega(3,2,0,0) == 1
    print('EXHAUSTIVE_CENTER_CHECKS',total_centers)
    print('TERNARY_SPECTRA_CHECKED',16)
    print('TERNARY_RADIUS_TWO_COEFFICIENTS','mean_deficit',60,-144,'variance',348,-3312)
    print('VERIFY_OK')

if __name__ == '__main__':
    check()
