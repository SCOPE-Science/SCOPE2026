"""Exact-rational finite consistency checks for an all-to-all weighted-median flow.

The tests supplement, but do not replace, the proof of the general theorem.
Run: python3 verify.py
"""
from fractions import Fraction as Q
from random import Random


def median(values, focal, own_weight):
    n = len(values)
    other = (Q(1) - own_weight) / (n - 1)
    possible = []
    for v in sorted(set(values)):
        below = sum((own_weight if j == focal else other for j in range(n)
                     if values[j] < v), Q(0))
        above = sum((own_weight if j == focal else other for j in range(n)
                     if values[j] > v), Q(0))
        if below <= Q(1, 2) and above <= Q(1, 2):
            possible.append(v)
    assert possible
    return min(possible, key=lambda v: abs(v - values[focal]))


def formula(z, a, u):
    n = len(z)
    q = min(n - 1, (Q(n-1) / (2 * (1-a))).__floor__())
    left, right = n-q-1, q
    y, dt = [], []
    if left <= right:
        for i, zi in enumerate(z):
            j = max(left, min(i, right))
            yy = z[j] + (zi-z[j])*u
            dy = (z[j]-zi)*u
            y.append(yy)
            dt.append(dy)
        return y, dt
    assert n % 2 == 0 and left == right + 1
    mid = n//2
    c = (z[mid-1]+z[mid])/2
    d = (z[mid]-z[mid-1])/2
    for i, zi in enumerate(z):
        s = 1 if i < mid else -1
        coeff = zi-c+s*d
        y.append(c + coeff*u-s*d*u*u)
        dt.append(-coeff*u + 2*s*d*u*u)
    return y, dt


def test():
    rng = Random(78241)
    profiles = 0
    derivative_checks = 0
    for n in range(2, 15):
        for den in range(1, 10):
            for num in range(den):
                a = Q(num, den)
                for kind in range(3):
                    z = []
                    current = Q(-5)
                    for j in range(n):
                        inc = rng.randrange(1, 9) if kind == 0 else rng.randrange(0, 4)
                        current += Q(inc, 3)
                        z.append(current)
                    profiles += 1
                    for u in (Q(1), Q(2, 3), Q(1, 2), Q(1, 4), Q(0)):
                        y, deriv = formula(z, a, u)
                        assert y == sorted(y), (n, a, z, u, y)
                        if u == 0:
                            assert all(v == 0 for v in deriv)
                            continue
                        for i in range(n):
                            actual = median(y, i, a)
                            assert actual - y[i] == deriv[i], (n, a, z, u, i)
                            derivative_checks += 1
    print(f'PASS: {profiles} exact-rational initial profiles; '
          f'{derivative_checks} median/ODE checks at rational exponential times; '
          'distinct and tied initial opinions.')

if __name__ == '__main__':
    test()
