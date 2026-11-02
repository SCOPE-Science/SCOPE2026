"""Reproduce exact EF1 probabilities and numerical root checks using Python 3 stdlib."""
from fractions import Fraction
from itertools import product
import math


def is_ef1(rows, n):
    """rows[i][g] is agent i's binary utility for good g; bundle j = (2j,2j+1)."""
    for i in range(n):
        own = rows[i][2*i] + rows[i][2*i+1]
        for j in range(n):
            if i == j:
                continue
            a, b = rows[i][2*j], rows[i][2*j+1]
            if own < min(a, b):
                return False
    return True


def probability(n, p):
    return (1 - (1-p)**2*(1 - (1-p*p)**(n-1)))**n


def agent_failure_exact(n, p):
    ans = Fraction(0)
    for row in product((0, 1), repeat=2*n):
        bad = row[0] == row[1] == 0 and any(
            row[2*j] == row[2*j+1] == 1 for j in range(1, n))
        if bad:
            ones = sum(row)
            ans += p**ones * (1-p)**(2*n-ones)
    return ans


def full_probability_exact(n, p):
    # Enumerates all 2^(2*n*n) utility matrices (only n <= 3).
    weights = [p**k*(1-p)**(2*n-k) for k in range(2*n+1)]
    rows = [(v, weights[sum(v)]) for v in product((0, 1), repeat=2*n)]
    ans = Fraction(0)
    for selection in product(rows, repeat=n):
        block = [x[0] for x in selection]
        if is_ef1(block, n):
            w = Fraction(1)
            for _, wt in selection:
                w *= wt
            ans += w
    return ans


def derivative_sign(n, p):
    m = n - 1
    r = 1-p*p
    return m*p*(1-p)*(r**(m-1)) - (1-r**m)


def root(n):
    lo, hi = 0.0, 1.0
    for _ in range(90):
        mid = (lo+hi)/2
        if derivative_sign(n, mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def test():
    count = 0
    for n in range(2, 7):
        for p in (Fraction(1, 5), Fraction(1, 2), Fraction(3, 4)):
            expected_bad = (1-p)**2*(1-(1-p*p)**(n-1))
            assert agent_failure_exact(n, p) == expected_bad
            count += 1
    for n, p in ((2, Fraction(1, 3)), (2, Fraction(2, 3)), (3, Fraction(1, 2))):
        assert full_probability_exact(n, p) == probability(n, p)
        count += 1
    roots = [root(n) for n in range(2, 201)]
    assert abs(roots[0]-0.5) < 1e-13
    assert all(a > b for a, b in zip(roots, roots[1:]))
    for n, a in zip(range(2, 201), roots):
        eps = min(0.00001, a/2, (1-a)/2)
        assert derivative_sign(n, a-eps) > 0
        assert derivative_sign(n, a+eps) < 0
    for n in (1000, 10000, 100000):
        p = root(n)
        t = (n-1)*p*p
        estimate = (math.log(n)+math.log(math.log(n))-math.log(2))/2
        assert abs(t-estimate) < 0.2
    print('PASS:', count, 'rational enumeration checks; uniqueness, monotonicity, scale checks n<=100000')
    for n in (2, 3, 4, 10, 100, 1000):
        p = root(n)
        print('n=', n, 'p_n=', format(p, '.10f'),
              'log minimum probability=', format(n*math.log(1-(1-p)**2*(1-(1-p*p)**(n-1))), '.7f'))


if __name__ == '__main__':
    test()
