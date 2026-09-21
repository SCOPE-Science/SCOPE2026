#!/usr/bin/env python3
from fractions import Fraction


def scalar(a):
    a = Fraction(a)
    if a <= 1:
        p2 = a / 2
        p3 = Fraction(1, 2) - a * a / 6
        joint = a / 2 - a * a / 3
        closed_cov = a * (a - 1) * (a - 3) / 12
    else:
        p2 = 1 - Fraction(1, 2) / a
        p3 = Fraction(1, 3) / a
        joint = Fraction(1, 6) / a
        closed_cov = (1 - a) / (6 * a * a)
    cov = joint - p2 * p3
    assert cov == closed_cov
    return p2, p3, joint, cov


cases = [Fraction(1, 2), Fraction(1), Fraction(2)]
for a in cases:
    p2, p3, joint, cov = scalar(a)
    print(f"a={a}: P(I2=1)={p2}, P(I3=1)={p3}, P(I2=I3=1)={joint}, Cov={cov}")
    assert 0 <= p2 <= 1 and 0 <= p3 <= 1 and 0 <= joint <= 1

assert scalar(Fraction(1, 2))[3] == Fraction(5, 96)
assert scalar(Fraction(1))[3] == 0
assert scalar(Fraction(2))[3] == Fraction(-1, 24)

for a in [Fraction(1, 3), Fraction(1, 2), Fraction(2), Fraction(3)]:
    p2, p3, joint, cov = scalar(a)
    for d in range(1, 7):
        dcov = joint ** d - (p2 * p3) ** d
        assert (dcov > 0) == (cov > 0)
        assert (dcov < 0) == (cov < 0)
    print(f"dimension-sign check passed for a={a}, d=1..6")

print("all exact checks passed")
