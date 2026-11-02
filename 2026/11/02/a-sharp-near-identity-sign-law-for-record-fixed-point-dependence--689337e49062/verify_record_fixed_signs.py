"""Exact checks of the record--fixed-point conditional sign law.

Run: python verify_record_fixed_signs.py
Uses only the Python 3 standard library.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import comb, factorial

checks = 0
for n in range(2, 10):
    counts = Counter()
    for p in permutations(range(1, n + 1)):
        top = 0
        records = 0
        for val in p:
            if val > top:
                top = val
                records += 1
        fixed = sum(val == j for j, val in enumerate(p, 1))
        counts[(records, fixed)] += 1
    assert sum(counts.values()) == factorial(n)
    checks += 1
    if n >= 3:
        for r in range(1, n):
            a = (2*r-1)*n - 2*r*r
            b = r
            assert counts[(r, n-3)] == a, (n, r, a, counts[(r,n-3)])
            assert counts[(r, n-2)] == b, (n, r, b, counts[(r,n-2)])
            checks += 2
        for r in range(1, n-1):
            determinant = (counts[(r,n-3)]*counts[(r+1,n-2)]
                           -counts[(r,n-2)]*counts[(r+1,n-3)])
            assert determinant == 2*r*(r+1)-n
            checks += 1
    if n <= 4:
        # Sharpness: no negative 2x2 minor anywhere in the entire table.
        for r in range(1,n+1):
            for s in range(r+1,n+1):
                for f in range(n+1):
                    for g in range(f+1,n+1):
                        determinant = counts[(r,f)]*counts[(s,g)]-counts[(r,g)]*counts[(s,f)]
                        assert determinant >= 0, (n,r,s,f,g,determinant)
                        checks += 1
    # Every fixed point indicator has expected value 1/n. Verify
    # the exact covariance formula with an integer numerator calculation.
    sum_rf = sum(r*f*v for (r,f),v in counts.items())
    sum_r = sum(r*v for (r,f),v in counts.items())
    sum_f = sum(f*v for (r,f),v in counts.items())
    cov = Fraction(sum_rf, factorial(n))-Fraction(sum_r*sum_f,factorial(n)**2)
    target = sum((Fraction(1,comb(n-1,j)) for j in range(1,n)),Fraction(0,1))/n
    assert cov == target and cov > 0
    checks += 1

# Further symbolic integer identities at large sizes, not relying on enumeration.
for n in range(3, 250):
    wa = sum((2*r-1)*n-2*r*r for r in range(1,n))
    wb = sum(r for r in range(1,n))
    assert wa == 2*comb(n,3)
    assert wb == comb(n,2)
    checks += 2
    for r in range(1,n-1):
        a = (2*r-1)*n - 2*r*r
        ap = (2*(r+1)-1)*n-2*(r+1)**2
        assert a*(r+1)-r*ap == 2*r*(r+1)-n
        checks += 1
print('PASS:',checks,'exact assertions; exhaustive permutations n=2..9; entire 2x2 minor tables n=2..4; symbolic integer checks to n=249')
