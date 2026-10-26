"""Exact arithmetic checks for finite-horizon two-species lottery competition."""
from fractions import Fraction as Q
from itertools import permutations
from random import Random


def step(x, r, delta):
    return (1 - delta)*x + delta*r*x/(1 + (r-1)*x)


def outcome(order, x, delta):
    for r in order:
        x = step(x, r, delta)
    return x


def commutator(x, a, b, delta):
    lhs = step(step(x, b, delta), a, delta) - step(step(x, a, delta), b, delta)
    A = 1 + (a-1)*x
    B = 1 + (b-1)*x
    E = A*B + delta*(a-1)*(b-1)*x*(1-x)
    rhs = -delta**2*(1-delta)*(a-b)*(a-1)*(b-1)*x**2*(1-x)**2/(A*B*E)
    return lhs, rhs, E


def key_max(r):
    # The weak-season group comes first; within either group, descending ratio.
    return (int(r > 1), -r)


def key_min(r):
    return (int(r < 1), r)


def main():
    rng = Random(582871)
    checks = 0
    for _ in range(2500):
        a = Q(rng.randint(1, 30), rng.randint(1, 30))
        b = Q(rng.randint(1, 30), rng.randint(1, 30))
        x = Q(rng.randint(1, 20), rng.randint(21, 50))
        delta = Q(rng.randint(1, 12), rng.randint(13, 35))
        l, r, E = commutator(x, a, b, delta)
        assert E > 0 and l == r
        checks += 1
    for n in (3, 4, 5, 6):
        for _ in range({3:90, 4:50, 5:22, 6:8}[n]):
            ratios = rng.sample([Q(k, 8) for k in range(1, 24) if k != 8], n)
            x = Q(rng.randint(1, 9), 10)
            delta = Q(rng.randint(1, 9), 10)
            maximum = outcome(sorted(ratios, key=key_max), x, delta)
            minimum = outcome(sorted(ratios, key=key_min), x, delta)
            assert minimum < maximum
            for order in permutations(ratios):
                val = outcome(order, x, delta)
                assert minimum <= val <= maximum
                checks += 1
    ratios = (Q(1,3), Q(2,3), Q(3,2), Q(3))
    x = delta = Q(1,2)
    pmax = (Q(2,3), Q(1,3), Q(3), Q(3,2))
    pmin = (Q(3,2), Q(3), Q(1,3), Q(2,3))
    valmax = outcome(pmax, x, delta)
    valmin = outcome(pmin, x, delta)
    assert valmax == Q(43307611041,83947961440)
    assert valmin == Q(40640350399,83947961440)
    assert valmax-valmin == Q(1333630321,41973980720)
    checks += 3
    for r in (Q(1,5),Q(1),Q(5)):
        for x in (Q(0),Q(1,2),Q(1)):
            assert step(x, r, Q(1)) == r*x/(1+(r-1)*x)
    assert outcome((Q(1,3),Q(3)),Q(1,2),Q(1)) == outcome((Q(3),Q(1,3)),Q(1,2),Q(1))
    print('PASS: %d exact checks; example max=%s, min=%s, gap=%s' % (checks,str(valmax),str(valmin),str(valmax-valmin)))

if __name__ == '__main__':
    main()
