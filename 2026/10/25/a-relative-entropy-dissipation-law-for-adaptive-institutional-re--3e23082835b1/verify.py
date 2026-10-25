"""Exact-rational checks for the entropy dissipation identity in a two-variable
adaptive institutional-reward model; the accompanying analytical proof covers
all positive real admissible parameters.

Run with: python verify.py
"""
from fractions import Fraction as Q
from itertools import product


def S(n, x):
    return sum(((1-x)**k for k in range(n)), Q(0))


def S_prime(n, x):
    return -sum((k*(1-x)**(k-1) for k in range(1, n)), Q(0))


def run():
    count = 0
    for n, u, alpha, beta, eps, delta, x, a in product(
            range(2, 9), [Q(1,2), Q(2), Q(4)],
            [Q(1,5), Q(1,2)], [Q(3), Q(5)],
            [Q(1,7), Q(1), Q(13)], [Q(1,6), Q(3,2)],
            [Q(1,9), Q(2,5), Q(4,5), Q(8,9)],
            [Q(3,4), Q(2), Q(11,4)]):
        xstar = u/(1+u)
        # Set d by fixing an a* strictly between the reward boundaries.
        astar = (alpha+beta)/2
        d = delta*astar*S(n,xstar)
        if not (Q(0) < alpha < astar < beta and Q(0) < x < 1 and alpha < a < beta):
            continue
        f = x*(1-x)*(-d + delta*a*S(n,x))/eps
        g = (a-alpha)*(beta-a)*(u-(u+1)*x)
        vx = (x-xstar)/(x*(1-x))
        va = delta*S(n,xstar)*(a-astar)/(eps*(u+1)*(a-alpha)*(beta-a))
        lhs = vx*f + va*g
        rhs = delta*a*(x-xstar)*(S(n,x)-S(n,xstar))/eps
        assert lhs == rhs
        assert rhs <= -delta*alpha*(x-xstar)**2/eps
        if x != xstar:
            assert rhs < 0
        assert S_prime(n,x) <= -1
        assert d == delta*astar*S(n,xstar)
        count += 1
    assert count == 6048
    print('PASS: %d rational parameter/state configurations; exact dissipation and quadratic bound.'%count)

if __name__ == '__main__':
    run()
