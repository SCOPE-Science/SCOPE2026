"""Exact checks for volumes of ladder-graph Lipschitz dual balls.

The first computation uses the rational power series of the proposed
resolvent. The second uses a wholly discrete, independent Ehrhart leading-
coefficient calculation, based on counting integer Lipschitz potentials.
Only the Python standard library is required.
"""
from fractions import Fraction
from math import comb, factorial


def series_volumes(max_n):
    degree = max_n - 1
    den = [Fraction((-1)**j * (2**j) * (2*j + 1), factorial(2*j))
           for j in range(degree + 1)]
    num = [Fraction((-1)**j * (2**(j+1)), factorial(2*j + 1))
           for j in range(degree + 1)]
    ans = []
    for k in range(degree + 1):
        ans.append(num[k] - sum((den[j]*ans[k-j] for j in range(1, k+1)), Fraction()))
    return ans


def ehrhart_count(n, dilation):
    rungs = range(-dilation, dilation + 1)
    table = {r: 1 for r in rungs}
    for _ in range(n-1):
        table = {r: sum(v * (2*dilation + 1 - abs(r-s))
                        for s,v in table.items()) for r in rungs}
    return sum(table.values())


def ehrhart_volume(n):
    dim = 2*n - 1
    lead = sum((-1)**(dim-k) * comb(dim,k) * ehrhart_count(n,k)
               for k in range(dim + 1))
    return Fraction(lead, factorial(dim))


def main():
    predicted = series_volumes(8)
    expected = [Fraction(2), Fraction(16,3), Fraction(72,5),
                Fraction(12256,315), Fraction(298048,2835),
                Fraction(14764672,51975)]
    assert predicted[:6] == expected
    for n in range(2,8):
        counted = ehrhart_volume(n)
        assert predicted[n-1] == counted, (n,predicted[n-1],counted)
        print(f"n={n}; dimension={2*n-1}; volume={counted}; integral-Ehrhart=PASS")
    for n in range(2,7):
        assert predicted[n-2]*predicted[n] > predicted[n-1]**2
    print('LADDER_VOLUME_EXACT_CHECKS_PASS 6 dimensions; strict sample log-convexity PASS')

if __name__ == '__main__':
    main()
