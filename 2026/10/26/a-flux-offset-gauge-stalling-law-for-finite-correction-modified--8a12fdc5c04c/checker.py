"""Exact-rational reproduction of finite-stage positivity and flux-offset tests.

The infinite-offset asymptotic theorem follows from the supplied proof,
not from this finite computation.
"""
from fractions import Fraction as Q

LO2 = [[Q(1, 2), Q(1, 2)]]
LO3 = [[Q(5, 24), Q(1, 3), -Q(1, 24)],
       [Q(1, 6), Q(2, 3), Q(1, 6)]]

def step(a, b, h, c, weights, corrections):
    a, b, h, c = (Q(x) for x in (a, b, h, c))
    assert a > 0 and b > 0 and h > 0 and c >= 0 and corrections >= 1
    previous = [(a, b) for _ in weights]
    history = []
    for _ in range(corrections):
        updated = []
        for ell, row in enumerate(weights):
            z1, z2 = previous[ell]
            incoming, outgoing = Q(0), Q(0)
            for k, theta in enumerate(row):
                old1, old2 = ((a, b) if k == 0 else previous[k - 1])
                if theta >= 0:
                    incoming += theta * (old2 + c) / z2
                    outgoing += theta * (old1 + c) / z1
                else:
                    incoming -= theta * (old1 + c) / z2
                    outgoing -= theta * (old2 + c) / z1
            denominator = 1 + h * (incoming + outgoing)
            next1 = (a + h * (a + b) * incoming) / denominator
            next2 = (b + h * (a + b) * outgoing) / denominator
            assert next1 > 0 and next2 > 0 and next1 + next2 == a + b
            assert next1 == a + h * (incoming * next2 - outgoing * next1)
            assert next2 == b + h * (outgoing * next1 - incoming * next2)
            updated.append((next1, next2))
        previous = updated
        history.append(updated)
    return previous, history

def check():
    cases = 0
    for weights in [LO2, LO3]:
        for a, b, h in [(Q(1), Q(2), Q(3, 10)),
                        (Q(2, 3), Q(5, 2), Q(1, 7)),
                        (Q(4), Q(1), Q(2))]:
            for m in (1, 2, 3, 4, 6):
                for c in (0, 1, 10, 100, 1000, 10000):
                    terminal, history = step(a, b, h, c, weights, m)
                    assert len(history) == m
                    eta = sum(weights[-1]); B = sum(map(abs, weights[-1]))
                    assert eta == 1 and B == 1
                    # Each C sequence tends monotonically to a finite asymptotic
                    # coefficient; these bounds are numerical tests, not a proof.
                    if c >= 1000:
                        target = Q(m) * a * b * (b-a) / (a+b)
                        empirical = Q(c) * (terminal[-1][0]-a)
                        assert abs(empirical-target) < Q(100) * abs(target) / Q(c)
                    if m == 1:
                        predicted = h * (b-a) / (1+h*(2+c*(1/a+1/b)))
                        assert terminal[-1][0] - a == predicted
                    cases += 1
    print('PASS', cases, 'exact-rational configurations; all stage balances, mass, positivity, one-correction formula, and large-offset coefficients checked')

if __name__ == '__main__':
    check()
