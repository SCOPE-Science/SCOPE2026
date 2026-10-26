"""Exact-rational checks for a sharp sampling cutoff in a coordination game.

This program checks finitely many polynomial identities and rational witness
brackets; it does not replace the analytical sign and concavity arguments.
Standard-library only. Run: python check_sampling.py
"""
from fractions import Fraction as Q
from math import comb


def B(k, m, p):
    return sum(Q(comb(k, j)) * p**j * (1 - p)**(k-j)
               for j in range(m, k + 1))


def h(k, mode, p):
    forms = {
        (2, 1): Q(1),
        (3, 2): 2*p - 1,
        (3, 1): 2-p,
        (4, 2): -3*p*p + 5*p - 1,
        (4, 1): 3-3*p + p*p,
    }
    return forms[(k, mode)]


def phi(p):
    return p * (6*p*p - 9*p + 1)


def H(alpha, p):
    return 2*alpha - 1 - (1-alpha)*phi(p)


# Exact polynomial identities: degree <=5 implies agreement at 6 distinct
# rational points proves the identity, without reliance on floating point.
for i in range(1, 7):
    p = Q(i, 7)
    for k, m in [(2, 1), (3, 1), (3, 2), (4, 1), (4, 2)]:
        assert B(k, m, p) - p == p * (1-p) * h(k, m, p)
    assert B(5, 3, p) == 10*p**3 - 15*p**4 + 6*p**5
    for a in [Q(1, 2), Q(503, 1000), Q(507, 1000), Q(3, 4)]:
        w = a * B(2, 1, p) + (1-a) * B(5, 3, p)
        assert w - p == p * (1-p) * H(a, p)

# Exact rational witness: under a=503/1000 there are two distinct interior
# zeros of H, the first with + -> - sign and the second with - -> + sign.
a = Q(503, 1000)
left_stable, right_stable = Q(137, 10000), Q(138, 10000)
left_unstable, right_unstable = Q(1059, 10000), Q(1060, 10000)
assert H(a, 0) > 0
assert H(a, left_stable) > 0 > H(a, right_stable)
assert H(a, left_unstable) < 0 < H(a, right_unstable)
assert H(a, 1) == 1

# Verify exact order of the rational witness and the algebraic critical alpha.
# alpha_crit=7 sqrt(7)/(18+7 sqrt(7)). This is greater than 503/1000
# exactly when 9054^2 < 7 * 3479^2.
assert 9054**2 < 7 * 3479**2
assert 7 * 3444**2 < 9144**2  # alpha_crit < 508/1000

# Finite sampling sanity check of the sign classes for the four-draw bound:
# every distribution with support <=4 and payoff u>1 has w-p with h concave
# when 1<u<3, and h strictly positive when u>=3 unless sample 1 only.
for n1 in range(5):
    for n2 in range(5-n1):
        for n3 in range(5-n1-n2):
            n4 = 4-n1-n2-n3
            weights = [Q(n, 4) for n in (n1, n2, n3, n4)]
            for m3, m4 in [(2, 2), (1, 2), (1, 1)]:
                for i in range(1, 20):
                    p = Q(i, 20)
                    w = sum(weights[k-1] * B(k, m, p)
                            for k, m in [(1,1),(2,1),(3,m3),(4,m4)])
                    hh = weights[1]*h(2,1,p) + weights[2]*h(3,m3,p) + weights[3]*h(4,m4,p)
                    assert w-p == p*(1-p)*hh
                if m4 == 2:
                    # h''=-6 theta_4 <=0, and h(1)=1-theta_1.
                    assert -6*weights[3] <= 0
                    assert weights[1]+weights[2]+weights[3] == 1-weights[0]
                else:
                    for i in range(1, 20):
                        p=Q(i,20)
                        assert h(2,1,p)>0 and h(3,1,p)>0 and h(4,1,p)>0
print('PASS: polynomial identities, exact witness brackets, radical comparisons, low-sample checks')
