"""Reproducible exact checks for the two-component quadratic reshuffling result."""
from fractions import Fraction as Q
from itertools import product
import math


def step(x, sign, eta):
    return (1 - eta) * x + eta * sign


def epochs(m, eta):
    xs = [Q(0)]
    for _ in range(m):
        xs = [step(step(x, a, eta), -a, eta) for x in xs for a in (-1, 1)]
    return xs


def replacement(n, eta):
    xs = [Q(0)]
    for _ in range(n):
        xs = [step(x, s, eta) for x in xs for s in (-1, 1)]
    return xs


def variance(xs):
    return sum(x*x for x in xs)/len(xs)


for eta in (Q(1,3), Q(2,5), Q(1,2), Q(3,5), Q(3,4)):
    r = 1 - eta
    q = r*r
    for m in range(1, 7):
        a = epochs(m, eta)
        b = replacement(2*m, eta)
        assert len(a) == 2**m and len(b) == 2**(2*m)
        theory_rr = eta**4 * (1-q**(2*m))/(1-q*q)
        theory_sgd = eta**2 * (1-r**(4*m))/(1-r*r)
        assert variance(a) == theory_rr
        assert variance(b) == theory_sgd
        assert variance(a)/variance(b) == eta**2/(1+r*r)
        if q < Q(1,2):
            min_rad = eta*eta*(1-q*2+q**m)/(1-q)
            assert min(abs(x) for x in a) == min_rad
            assert min_rad > eta*eta*(1-2*q)/(1-q)

eta = Q(1,2)
for m in range(1, 8):
    a = epochs(m, eta)
    b = replacement(2*m, eta)
    assert min(abs(x) for x in a) == Q(1,6)+Q(1,3)*Q(1,4)**m
    assert variance(a)*5 == variance(b)
    assert len(set(a)) == 2**m
assert sorted(set(epochs(2,Q(1,2)))) == [Q(-5,16),Q(-3,16),Q(3,16),Q(5,16)]
assert sum(abs(z) < Q(1,8) for z in epochs(2,Q(1,2))) == 0
assert Q(sum(abs(z) < Q(1,8) for z in replacement(4,Q(1,2))),16) == Q(1,8)
assert 0 < 1-1/math.sqrt(2) < 1/2
print('PASS: 30 full exact distributions (5 step sizes x 6 epochs), 7 half-step gap cases, and finite small-ball contrast.')
# At the half step, every reshuffled path yields one of 2**m distinct
# with-replacement states, all of which have equal unconditional mass.
for m in range(1, 8):
    a = set(epochs(m, Q(1, 2)))
    b = set(replacement(2*m, Q(1, 2)))
    assert a <= b
    assert len(a) == 2**m and len(b) == 2**(2*m)
    tv = Q(1, 2)*(
        sum(abs(Q(1,2**m)-Q(1,2**(2*m))) for _ in a)
        + sum(Q(1,2**(2*m)) for _ in b-a))
    assert tv == 1 - Q(1, 2**m)
print('PASS: seven exact finite-horizon total-variation identities.')
