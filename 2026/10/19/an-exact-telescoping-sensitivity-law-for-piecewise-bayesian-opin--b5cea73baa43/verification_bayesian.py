#!/usr/bin/env python3
"""Reproduce finite-state derivative identities for biased Bayesian updating.

The analytical statements apply to all dimensions and step counts; these finite
checks only cross-check algebra and a representative branching implementation.
"""
from fractions import Fraction as F
from random import Random
from math import log


def posterior(b, gamma):
    return b / (b + gamma * (1 - b))


def q(b):
    return b * (1 - b)


def gamma_choice(x, receiver, sender):
    # Confirmation and proximity decisions are intentionally discontinuous.
    if x[receiver] >= F(1, 2) and abs(x[receiver] - x[sender]) < F(1, 7):
        return F(3, 5)
    if x[receiver] < F(1, 2) and abs(x[receiver] - x[sender]) < F(1, 7):
        return F(5, 3)
    return F(7, 4)


def evolve(x0, steps):
    x = list(x0)
    prod = [F(1) for _ in x]
    for receiver, sender in steps:
        g = gamma_choice(x, receiver, sender)
        old = x[receiver]
        new = posterior(old, g)
        factor = g / (old + g*(1-old))**2
        assert factor == q(new)/q(old)
        prod[receiver] *= factor
        x[receiver] = new
    return x, prod


def main():
    rng = Random(210716)
    counts = 0
    for n in range(2, 7):
        for case in range(96):
            x0 = [F(rng.randint(10, 90), 101) for _ in range(n)]
            steps = []
            for _ in range(14):
                i = rng.randrange(n)
                j = rng.randrange(n-1)
                if j >= i:
                    j += 1
                steps.append((i,j))
            xt, prod = evolve(x0, steps)
            for i in range(n):
                assert prod[i] == q(xt[i]) / q(x0[i])
                assert prod[i] <= 1/(4*q(x0[i]))
                counts += 1
    for T in range(1, 25):
        gam = F(1, 2)
        b0 = gam**T/(1+gam**T)
        bt = b0
        product = F(1)
        for _ in range(T):
            nxt = posterior(bt,gam)
            product *= gam/(bt+gam*(1-bt))**2
            bt = nxt
        assert bt == F(1, 2)
        assert product == (1+gam**T)**2 / (4*gam**T)
        assert product > 1 or T==1 and product == F(9,8)
        counts += 3
    for T in (80, 200, 500):
        log_finite = (2*log(1+2.0**(-T)) + T*log(2)-log(4))/T
        assert 0 < log(2)-log_finite < .02
        counts += 1
    print('PASSED', counts, 'exact rational and analytic-limit spot checks')


if __name__ == '__main__':
    main()
