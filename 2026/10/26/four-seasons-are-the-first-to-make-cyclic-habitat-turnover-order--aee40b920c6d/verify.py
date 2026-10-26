"""Exact rational checks for cyclic two-state habitat turnover formulas.

No third-party dependencies. Run: python verify.py
These checks are finite diagnostics, not a substitute for the proof.
"""
from fractions import Fraction as F
from itertools import permutations
from random import Random


def excess(order, q, u):
    """Expected extinctions minus sum of within-season equilibrium fluxes.

    q[i] is equilibrium occupancy and u[i] the contraction factor, both in (0,1).
    """
    product = F(1)
    offset = F(0)
    for i in order:
        product *= u[i]
        offset = u[i] * offset + (1-u[i]) * q[i]
    p = offset / (1-product)
    amount = F(0)
    for i in order:
        delta = (1-u[i]) * (q[i]-p)
        amount += q[i]*delta
        p += delta
    assert p == offset/(1-product)
    return amount


def factor(u):
    prod = F(1)
    num = F(1)
    for x in u:
        prod *= x
        num *= 1-x
    return num / (1-prod)


def checks():
    rng = Random(680913)
    tests = 0
    for n in range(1,10):
        for _ in range(120):
            q = [F(rng.randint(1,19),20) for i in range(n)]
            u = [F(rng.randint(1,19),20) for i in range(n)]
            order = list(range(n))
            val = excess(order,q,u)
            assert val == excess(order[::-1],q,u)
            assert val >= 0
            if len(set(q)) > 1:
                assert val > 0
            if n == 3:
                assert len({excess(order1,q,u) for order1 in permutations(order)}) == 1
            if n == 4:
                R = factor(u)
                A = excess((0,1,2,3),q,u)
                B = excess((0,2,1,3),q,u)
                C = excess((0,1,3,2),q,u)
                assert A-B == -R*(q[0]-q[3])*(q[1]-q[2])
                assert A-C == R*(q[0]-q[1])*(q[2]-q[3])
            tests += 1

    q = [F(1,5),F(2,5),F(3,5),F(4,5)]
    u = [F(1,2)]*4
    low = excess((0,1,3,2),q,u)
    mid = excess((0,1,2,3),q,u)
    high = excess((0,2,1,3),q,u)
    assert (low,mid,high) == (F(3,25),F(46,375),F(49,375))
    assert mid-low == F(1,375) and high-mid == F(1,125)
    vals = {order:excess(order,q,u) for order in permutations(range(4))}
    assert len(set(vals.values())) == 3
    assert min(vals.values()) == low and max(vals.values()) == high
    print(f'PASS: {tests} exact rational test sets for reversal, nonnegative excess, three/four-block formulas')
    print('PASS: all 24 four-block arrangements and exact example')
    print('Exact excess extinction levels:',low,mid,high)

if __name__ == '__main__':
    checks()
