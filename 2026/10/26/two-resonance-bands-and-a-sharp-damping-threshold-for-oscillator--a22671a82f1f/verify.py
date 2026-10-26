"""Finite and algebraic checks for damped cosines on regular trees.

Run with Python 3: python verify.py
Only the Python standard library is required.
The tests do not replace the all-parameter analytic proof.
"""
from collections import deque
from fractions import Fraction
from itertools import product
from math import cos, pi, sqrt


def p(q, r, c):
    return (1 - q*r**4 + (q-1)*r*r*(2*c*c-1)
            - 2*sqrt(q)*r*(1-r*r)*c)


def endpoints(q, r):
    return ((1+r*r)*(1-q*r*r), (1-r*r)*(1-sqrt(q)*r)**2)


def bound(q, r):
    t = r*r
    if t <= 1/(2*q-1):
        return True
    if t >= 1/q:
        raise ValueError('use only the subcritical regime')
    root = sqrt((q*t+q-2)*((2*q-1)*t-1))
    lo = (sqrt(q)*(1-t)-root)/(2*(q-1)*r)
    hi = (sqrt(q)*(1-t)+root)/(2*(q-1)*r)
    assert 0 < lo < hi < 1
    return lo, hi


def tree_ball(q, depth):
    adj = [[]]
    shell = [0]
    queue = deque([0])
    while queue:
        x = queue.popleft()
        if shell[x] >= depth:
            continue
        for _ in range(q+1 if x == 0 else q):
            y = len(adj)
            adj[x].append(y)
            adj.append([x])
            shell.append(shell[x]+1)
            queue.append(y)
    return adj, shell


def distances(adj, start):
    dist = [-1]*len(adj)
    dist[start] = 0
    queue = deque([start])
    while queue:
        x = queue.popleft()
        for y in adj[x]:
            if dist[y] < 0:
                dist[y] = dist[x]+1
                queue.append(y)
    return dist


def exact_witness():
    # The cosines of multiples of pi/3 are rational.
    adj, shells = tree_ball(2, 3)
    assert len(adj) == 22
    vec = [1, 2, 0, 1]
    cc = (Fraction(1), Fraction(1, 2), Fraction(-1, 2),
          Fraction(-1), Fraction(-1, 2), Fraction(1, 2))
    radial = [Fraction(2, 3)**n * cc[n % 6] for n in range(7)]
    total = Fraction(0)
    for x in range(len(adj)):
        ds = distances(adj, x)
        for y in range(len(adj)):
            total += vec[shells[x]]*vec[shells[y]]*radial[ds[y]]
    assert total == Fraction(-49, 243), total
    print('EXACT_FINITE_OBSTRUCTION', total)


def check_polynomial():
    for q in range(2, 15):
        for numer, denom in ((1, 10), (1, 5), (1, 3), (2, 5), (1, 2), (3, 5)):
            r = Fraction(numer, denom)
            if r*r >= Fraction(1, q):
                continue
            p0, p1 = endpoints(q, float(r))
            assert abs(p(q, float(r), 0)-p0) < 1e-12
            assert abs(p(q, float(r), 1)-p1) < 1e-12
            for i in range(101):
                c = i/100
                expected = p(q, float(r), c)
                A = 2*(q-1)*float(r)**2
                B = 2*sqrt(q)*float(r)*(1-float(r)**2)
                C = (1+float(r)**2)*(1-q*float(r)**2)
                assert abs(expected-(A*c*c-B*c+C)) < 1e-12
            if r*r > Fraction(1, 2*q-1):
                lo, hi = bound(q, float(r))
                assert abs(p(q, float(r), lo)) < 1e-10
                assert abs(p(q, float(r), hi)) < 1e-10
                assert p(q, float(r), (lo+hi)/2) < 0
                assert p(q, float(r), lo/2) > 0
                assert p(q, float(r), (1+hi)/2) > 0
    # A purely rational identity certifies the discriminant factorization.
    for q, num, den in product(range(2, 40), range(1, 12), range(12, 25)):
        t = Fraction(num, den)
        if t >= 1:
            continue
        lhs = (q*t+q-2)*((2*q-1)*t-1)
        rhs = q*(1-t)**2-2*(q-1)*(1+t)*(1-q*t)
        assert lhs == rhs
    print('POLYNOMIAL_AND_DISCRIMINANT_IDENTITIES_OK')


def check_boundaries():
    for q in range(2, 30):
        root = sqrt(q)
        at_spectral_edge = 1/root
        for j in range(1, 100):
            c = j/100
            target = -2*(q-1)/q*c*(1-c)
            assert abs(p(q, at_spectral_edge, c) - target) < 1e-11
            assert target < 0
        # The neighbor star has q+1 points, with off-diagonal -1/q:
        # its constant-vector eigenvalue is zero at the boundary.
        assert Fraction(1)-q*Fraction(1, q) == 0
    print('CRITICAL_BOUNDARY_AND_STAR_OK')


if __name__ == '__main__':
    check_polynomial()
    check_boundaries()
    exact_witness()
    print('ALL_CHECKS_PASSED')
