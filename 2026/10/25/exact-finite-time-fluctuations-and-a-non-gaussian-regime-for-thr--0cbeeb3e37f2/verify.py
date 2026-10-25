"""Exact finite-time reproduction checks for the 3-agent sampled-neighbor FTL model.

Python >= 3.9; standard library only. Run: python verify.py
"""
from fractions import Fraction as F
from itertools import product
from math import gamma, sqrt


def one_step(x, s, alpha, sign, t):
    """Direct synchronous Follow-the-Leader update at completed round t+1."""
    w = F(t, t + 1)
    incoming = (
        x[1],
        x[0] if sign == 1 else x[2],
        x[1],
    )
    return tuple(w * x[i] + (1-w) * (alpha * s[i] + (1-alpha) * incoming[i])
                 for i in range(3))


def exact_coeffs(alpha, s, t):
    """Independently construct coefficients in the solved scalar recurrence."""
    d = (1-alpha)*(s[0]-s[2])/4
    cs = []
    for j in range(1, t+1):
        coefficient = (d if j == 1 else alpha*d)/j
        for k in range(j+1, t+1):
            coefficient *= 1-alpha/F(k)
        cs.append(coefficient)
    return cs


def check():
    total = 0
    for alpha in (F(1,4), F(1,2), F(3,4)):
        for s in ((F(0), F(1,2), F(1)),
                  (F(0), F(0), F(1)),
                  (F(1), F(0), F(0))):
            center = (s[0]+2*s[1]+s[2])/4
            for t in range(1,9):
                cs = exact_coeffs(alpha, s, t)
                outcomes = []
                for signs in product((-1,1), repeat=t):
                    x = s
                    for k, sign in enumerate(signs):
                        x = one_step(x, s, alpha, sign, k)
                    observed = (x[0]+2*x[1]+x[2])/4 - center
                    predicted = sum((co * sign for co, sign in zip(cs, signs)), F(0))
                    assert observed == predicted, (alpha,s,t,signs,observed,predicted)
                    assert x[0]-x[2] == alpha*(s[0]-s[2])
                    assert all(0 <= y <= 1 for y in x)
                    outcomes.append(observed)
                    total += 3
                n = len(outcomes)
                mean = sum(outcomes, F(0))/n
                var = sum((v*v for v in outcomes), F(0))/n
                target_var = sum((v*v for v in cs), F(0))
                assert mean == 0
                assert var == target_var
                total += 2
    alpha = F(1,2)
    s = (F(0),F(1,2),F(1))
    assert exact_coeffs(alpha, s, 2) == [F(-3,32), F(-1,32)]
    assert sum((c*c for c in exact_coeffs(alpha, s, 2)),F(0)) == F(5,512)
    total += 2
    return total


if __name__ == '__main__':
    count = check()
    print(f'PASS: {count} independent exact rational assertions; all 3-vertex update histories through 8 rounds.')
