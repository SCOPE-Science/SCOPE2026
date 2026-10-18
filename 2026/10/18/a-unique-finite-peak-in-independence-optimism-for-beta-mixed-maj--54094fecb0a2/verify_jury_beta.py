"""Exact-rational checks of a beta-mixed majority comparison.

Run with Python 3 standard library only:
    python verify_jury_beta.py
Finite tests support, but do not replace, the general algebraic proof.
"""
from fractions import Fraction
from math import comb


def rising(x, k):
    z = Fraction(1)
    for i in range(k):
        z *= x + i
    return z


def accuracies(a, b, r):
    n = 2 * r + 1
    mu, s = a / (a + b), a + b
    ind = sum(Fraction(comb(n, k)) * mu**k * (1 - mu)**(n-k)
              for k in range(r + 1, n + 1))
    mixed = sum(Fraction(comb(n, k)) * rising(a, k)
                * rising(b, n-k) / rising(s, n)
                for k in range(r + 1, n + 1))
    return ind, mixed


def step_ratio(a, b, r):
    assert a > 0 and b > 0 and a != b and r >= 0
    s = a + b
    return (s**(2*r+3) * rising(a, r+1) * rising(b, r+1)
            / ((a*b)**(r+1) * rising(s, 2*r+2) * (s+2*r+2)))


def ratio_recurrence(a, b, r):
    s = a + b
    return (s*s*(a+r+1)*(b+r+1)
            / (a*b*(s+2*r+3)*(s+2*r+4)))


def verify():
    tests = 0
    values = [Fraction(1, 3), Fraction(2, 3), Fraction(1),
              Fraction(3, 2), Fraction(2), Fraction(3),
              Fraction(5), Fraction(10)]
    for a in values:
        for b in values:
            if a == b:
                for r in range(4):
                    x, y = accuracies(a, b, r)
                    assert x == y == Fraction(1, 2)
                continue
            older = accuracies(a, b, 0)
            assert older[0] == older[1] == a/(a+b)
            old_ratio = None
            for r in range(6):
                nxt = accuracies(a, b, r+1)
                iid_gain = nxt[0] - older[0]
                mixed_gain = nxt[1] - older[1]
                assert iid_gain != 0
                actual = mixed_gain / iid_gain
                explicit = step_ratio(a, b, r)
                assert actual == explicit > 0, (a, b, r)
                if old_ratio is not None:
                    assert explicit == old_ratio * ratio_recurrence(a,b,r-1)
                old_ratio, older = explicit, nxt
                tests += 1
    # The displayed exact example has a unique peak at five jurors.
    a, b = Fraction(10), Fraction(1)
    gaps = [accuracies(a,b,r)[0] - accuracies(a,b,r)[1] for r in range(6)]
    assert gaps[0] == 0 < gaps[1] < gaps[2]
    assert gaps[2] > gaps[3] > gaps[4] > gaps[5] > 0
    assert gaps[1] == Fraction(525,34606)
    assert gaps[2] == Fraction(226461,14655641)
    assert step_ratio(a,b,1) < 1 < step_ratio(a,b,2)
    print(f"PASS: {tests} rational step and recurrence checks; 10:1 example peaks at 5")

if __name__ == '__main__':
    verify()
