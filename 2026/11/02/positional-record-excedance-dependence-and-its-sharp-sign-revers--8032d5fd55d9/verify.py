"""Standalone exact checks for record/excedance covariance formulas.
Run: python3 verify.py. Uses only Python standard library.
"""
from itertools import permutations
from fractions import Fraction
from math import comb, factorial

checks = 0
for n in range(1, 9):
    num = factorial(n)
    nr = [0] * (n + 1)
    ne = [0] * (n + 1)
    both = [[0] * (n + 1) for _ in range(n + 1)]
    for p in permutations(range(1, n + 1)):
        max_seen = 0
        r = [0] * (n + 1)
        e = [0] * (n + 1)
        for i, v in enumerate(p, 1):
            if v > max_seen:
                r[i] = 1
                max_seen = v
            e[i] = int(v > i)
            nr[i] += r[i]
            ne[i] += e[i]
        for i in range(1, n + 1):
            if r[i]:
                for j in range(1, n + 1):
                    both[i][j] += e[j]
    for i in range(1, n + 1):
        assert Fraction(nr[i], num) == Fraction(1, i)
        checks += 1
    for j in range(1, n + 1):
        assert Fraction(ne[j], num) == Fraction(n-j, n)
        checks += 1
    for i in range(1, n + 1):
        row = Fraction(0)
        for j in range(1, n + 1):
            observed = Fraction(both[i][j], num) - Fraction(nr[i]*ne[j], num*num)
            if i == 1 or j > i:
                expected = Fraction(0)
            elif j < i:
                expected = -Fraction(j, n*i*(i-1))
            else:
                expected = Fraction(1,n)-Fraction(1,i*comb(n,i))
            assert observed == expected, (n,i,j,observed,expected)
            checks += 1
            row += observed
        expected_row = Fraction(0) if i == 1 else Fraction(1, 2*n)-Fraction(1,i*comb(n,i))
        assert row == expected_row, (n,i,row,expected_row)
        checks += 1
    total_observed = sum((Fraction(both[i][j],num) - Fraction(nr[i]*ne[j],num*num)
                         for i in range(1,n+1) for j in range(1,n+1)), Fraction(0))
    expected_total = Fraction(n-1,2*n)-sum((Fraction(1,i*comb(n,i)) for i in range(2,n+1)),Fraction(0))
    assert total_observed == expected_total
    checks += 1

for n in range(2, 1001):
    expected_total = Fraction(n-1, 2*n) - sum((Fraction(1,i*comb(n,i)) for i in range(2,n+1)),Fraction(0))
    if n <= 4:
        assert expected_total < 0
    else:
        assert expected_total > 0
    checks += 1
    for i in range(2,n+1):
        value = Fraction(1, 2*n)-Fraction(1,i*comb(n,i))
        if i == n:
            assert value < 0
        elif n >= 4:
            assert value > 0
        elif n == 3:
            assert value == 0
        checks += 1

for n in (5,10,30,100,500,1000):
    c = Fraction(n-1, 2*n)-sum((Fraction(1,i*comb(n,i)) for i in range(2,n+1)),Fraction(0))
    assert 0 < c < Fraction(1,2)
    checks += 1
print(f"PASS: {checks} exact checks; exhaustive permutations n<=8 and formula checks n<=1000")
