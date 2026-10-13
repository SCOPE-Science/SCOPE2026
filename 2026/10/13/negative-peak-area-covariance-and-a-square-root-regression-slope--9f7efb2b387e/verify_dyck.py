"""Exhaustive exact verification of mixed peak/area moments for Dyck excursions.

Area is the integer sum of step heights, with each downstep contributing its
ending height; equivalently twice the usual cell-area of a Dyck excursion.
This finite verification complements, but does not replace, the formal-series proof.
"""
from fractions import Fraction
from math import comb
from collections import defaultdict


def moments(n):
    data = [0, 0, 0, 0, 0]  # count, peak, area, peak*area, peak^2
    def visit(up, down, height, peaks, area, previous_up):
        if up == down == n:
            data[0] += 1
            data[1] += peaks
            data[2] += area
            data[3] += peaks * area
            data[4] += peaks * peaks
            return
        if up < n:
            visit(up+1, down, height+1, peaks, area+height, True)
        if down < up:
            visit(up, down+1, height-1, peaks+int(previous_up), area+height-1, False)
    visit(0, 0, 0, 0, 0, False)
    return data


def verify(n):
    cat = comb(2*n, n)//(n+1)
    b = comb(2*n, n)
    m = moments(n)
    assert m[0] == cat, (n, m[0], cat)
    assert m[1] == Fraction(n+1,2)*cat
    assert m[2] == 4**n-Fraction(3*n+1,n+1)*b
    assert m[3] == Fraction(2*n+1,4)*4**n-Fraction(3*n,2)*b
    assert m[4] == (Fraction(n+1,2)**2+Fraction(n*n-1,4*(2*n-1)))*cat
    if n >= 2:
        covariance = Fraction(m[3], cat)-Fraction(m[1]*m[2], cat*cat)
        target = Fraction(n+1,2)-Fraction((n+1)*4**(n-1),b)
        assert covariance == target and covariance < 0
    return m[0]


if __name__ == '__main__':
    total=0
    for n in range(1,13):
        count=verify(n)
        total+=count
        print(f'n={n} paths={count} exact_total_and_mixed_moments=PASS')
    print(f'EXACT_DYCK_VERIFICATION_PASS enumerated_paths={total}')
