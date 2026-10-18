"""Exact finite verification for finite-path centered maximal variation on valley data.

Analytic proof in RESULT.md establishes the statement for every path length and
all nonnegative real inputs of the stated shape. These tests are supplementary.
"""
from fractions import Fraction
from itertools import product


def valley(a):
    return any(
        all(a[j] >= a[j+1] for j in range(p))
        and all(a[j] <= a[j+1] for j in range(p, len(a)-1))
        for p in range(len(a))
    )


def centered_maximal(a):
    n = len(a)
    return [max(sum(a[max(0, i-r):min(n, i+r+1)]) /
                (min(n, i+r+1)-max(0, i-r))
                for r in range(n)) for i in range(n)]


def variation(a):
    return sum(abs(a[j+1]-a[j]) for j in range(len(a)-1))


def check(a):
    n = len(a)
    assert n >= 3 and valley(a)
    b = centered_maximal(a)
    h = min(a)
    A, B = a[0]-h, a[-1]-h
    mu = sum(a)/n
    t = mu-h
    assert valley(b), (a, b)
    assert b[0] == max(a[0], mu)
    assert b[-1] == max(a[-1], mu)
    assert variation(a) == A+B
    assert t >= (A+B)/n
    assert variation(b) <= max(A-t, 0)+max(B-t, 0)
    delta = (1-Fraction(1,n))*variation(a)-variation(b)
    assert delta >= 0, (a, b, delta)
    assert delta >= (min((n-1)*A, B)+min((n-1)*B, A))/n
    if A+B > 0 and delta == 0:
        assert (a[0] > h and all(v == h for v in a[1:])) or (a[-1] > h and all(v == h for v in a[:-1]))
    for e in (0, n-1):
        spike = [Fraction(2)]*n
        spike[e] += Fraction(7, 3)
        assert variation(centered_maximal(spike)) == (1-Fraction(1,n))*variation(spike)
    return b


def run():
    total = 0
    nonconstant = 0
    for n in range(3, 11):
        count = 0
        for raw in product(range(4), repeat=n):
            if not valley(raw):
                continue
            a = list(map(Fraction, raw))
            check(a)
            count += 1
            if variation(a):
                nonconstant += 1
        total += count
        print(f'n={n}: {count} valley inputs checked')
    extras = [
        [Fraction(7,3), Fraction(2), Fraction(0), Fraction(0), Fraction(5,4)],
        [Fraction(4), Fraction(1,9), Fraction(1,9), Fraction(1,9), Fraction(3)],
        [Fraction(3), Fraction(1), Fraction(0), Fraction(1), Fraction(3)],
        [Fraction(11,7), Fraction(1,6), Fraction(0), Fraction(1,10), Fraction(4)],
    ]
    for a in extras:
        # Nonnegative valley profiles, with arbitrary rational amplitudes.
        if min(a) >= 0 and valley(a):
            check(a)
        else:
            raise AssertionError('Unexpected invalid supplementary input')
    print(f'VERIFY_OK valley_profiles={total} nonconstant={nonconstant} rational_profiles={len(extras)}')


if __name__ == '__main__':
    run()
