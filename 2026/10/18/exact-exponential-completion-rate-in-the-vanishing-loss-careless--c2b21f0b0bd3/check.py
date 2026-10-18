"""Exact small-state checks for a post-draw independent-loss coupon collector.

Standard-library only. These finite calculations do not establish asymptotic limits.
"""
from fractions import Fraction
from itertools import combinations
from math import expm1, log, log1p


def solve(matrix, vector):
    rows = [[Fraction(x) for x in row] + [Fraction(b)]
            for row, b in zip(matrix, vector)]
    n = len(rows)
    for col in range(n):
        pivot = next(i for i in range(col, n) if rows[i][col])
        rows[col], rows[pivot] = rows[pivot], rows[col]
        t = rows[col][col]
        rows[col] = [v / t for v in rows[col]]
        for i in range(n):
            if i != col:
                factor = rows[i][col]
                if factor:
                    rows[i] = [a - factor * b for a, b in zip(rows[i], rows[col])]
    return [row[-1] for row in rows]


def check_exact(n, p):
    m = 1 << n
    s = 1 - p
    P = [[Fraction(0) for _ in range(m)] for _ in range(m)]
    for old in range(m):
        for coin in range(n):
            before = old | (1 << coin)
            for new in range(m):
                if new & ~before:
                    continue
                retained, lost = new.bit_count(), before.bit_count() - new.bit_count()
                P[old][new] += s ** retained * p ** lost / n
        assert sum(P[old]) == 1
    A = [[P[j][i] - (i == j) for j in range(m)] for i in range(m)]
    A[-1] = [Fraction(1)] * m
    b = [Fraction(0)] * (m - 1) + [Fraction(1)]
    pi = solve(A, b)
    assert all(q > 0 for q in pi)
    for k in range(n + 1):
        formula = Fraction(1)
        for j in range(1, k+1):
            formula *= Fraction(j, n) * s ** j / (1 - (1 - Fraction(j, n)) * s ** j)
        for idxs in combinations(range(n), k):
            mask = sum(1 << i for i in idxs)
            exact = sum(pi[state] for state in range(m) if state & mask == mask)
            assert exact == formula, (n, p, k, exact, formula)
    # The rate of stationary new entries from outside into all-present is
    # exactly stationary full mass times its one-step departure probability.
    full = m - 1
    flux = sum(pi[old] * P[old][full] for old in range(full))
    assert flux == pi[full] * (1 - s ** n)
    return pi[full]


def rate_estimate(n,c):
    p = c/n
    s = 1-p
    return sum(log1p((n/j)*expm1(-j*log(s))) for j in range(1,n+1))/n

if __name__ == '__main__':
    tests=0
    for n in (2,3,4):
        for p in (Fraction(1,3), Fraction(2,5)):
            prob = check_exact(n,p)
            tests += 1
            print('EXACT',n,str(p),str(prob))
    import math
    c = 1.0
    # Composite Simpson integration of the continuous rate function.
    def f(x):
        return log(1+c) if x == 0 else log(1+math.expm1(c*x)/x)
    M = 10000
    h = 1/M
    integral = h/3*(f(0)+f(1)+4*sum(f(i*h) for i in range(1,M,2))+2*sum(f(i*h) for i in range(2,M,2)))
    for n in (100,500,2000):
        approx = rate_estimate(n,c)
        print('RATE',n,'stationary exponent',round(approx,10),'limiting integral',round(integral,10))
        assert abs(approx-integral) < 0.1
    assert integral > log(1+c)
    print('ALL CHECKS PASSED',tests,'exact stationary systems, plus convergence diagnostics')
