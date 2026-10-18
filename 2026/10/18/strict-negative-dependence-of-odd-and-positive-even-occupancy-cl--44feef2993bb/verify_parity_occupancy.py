"""Exact checks for parity-class occupancy covariance.
Run with: python verify_parity_occupancy.py
Requires only Python's standard library.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial


def formula(m, n):
    assert m >= 2 and n >= 1
    a, b, c, d = (F(m - j, m) for j in (1, 2, 3, 4))
    return F(m, 4) * (
        -1 - (m - 1) * d ** n + 2 * a ** n + 2 * (m - 1) * c ** n
        + m * b ** (2 * n) - 2 * m * a ** n * b ** n
    )


def by_enumeration(m, n):
    sample = m ** n
    o_total = e_total = oe_total = 0
    for outcome in product(range(m), repeat=n):
        counts = [0] * m
        for x in outcome:
            counts[x] += 1
        odd = sum(x % 2 != 0 for x in counts)
        positive_even = sum(x >= 2 and x % 2 == 0 for x in counts)
        o_total += odd
        e_total += positive_even
        oe_total += odd * positive_even
    return F(oe_total, sample) - F(o_total * e_total, sample * sample)


def cross(m, n):
    a, b, c, d = (F(m - j, m) for j in (1, 2, 3, 4))
    return (b ** (2*n) - d ** n + 2*c ** n - 2*(a*b) ** n) / 4


def proof_checks():
    checks = 0
    for m in range(2, 7):
        for n in range(1, 9):
            if m**n > 500_000:
                continue
            assert by_enumeration(m, n) == formula(m, n), (m,n)
            checks += 1
    for m in range(2, 51):
        for n in range(1, 80):
            f = formula(m, n)
            if n == 1 or (m == 2 and n % 2 == 1):
                assert f == 0, (m,n,f)
            else:
                assert f < 0, (m,n,f)
            if m >= 4 and n >= 2:
                assert cross(m,n) < 0, (m,n)
            checks += 1
    return checks

if __name__ == '__main__':
    k=proof_checks()
    print(f'Passed {k} exact checks (enumeration and rational identities/signs).')


def nonuniform_pair_cov(probabilities, n, i, j):
    """Covariance of odd occupancy of i with positive even occupancy of j."""
    p, q = probabilities[i], probabilities[j]
    s, t = 1-2*p, 1-2*q
    d, c = 1-2*p-2*q, 1-2*p-q
    aj = 1-q
    return ((s*t)**n-d**n+2*c**n-2*(s*aj)**n)/4


def nonuniform_checks():
    cases = [
        [F(1,4)]*4,
        [F(1,10), F(1,5), F(3,10), F(2,5)],
        [F(1,6), F(1,6), F(1,3), F(1,3)],
        [F(1,10), F(1,10), F(1,5), F(1,5), F(2,5)],
        [F(1,5)]*5,
        [F(1,10)]*10,
    ]
    checks = 0
    for ps in cases:
        assert sum(ps) == 1
        if all(ps[i]+ps[j] <= F(1,2)
               for i in range(len(ps)) for j in range(i+1,len(ps))):
            for n in range(2, 9):
                for i in range(len(ps)):
                    for j in range(len(ps)):
                        if i != j:
                            assert nonuniform_pair_cov(ps,n,i,j)<0
                            checks+=1
    return checks


if __name__ == '__main__':
    print(f'Passed {nonuniform_checks()} additional exact nonuniform cross-covariance sign checks.')
