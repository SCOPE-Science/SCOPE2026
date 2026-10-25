"""Exact reproducibility checks for the harmonic-entropy sensitivity identities.

Uses rational arithmetic only for finite identities; asymptotic claims are
proved separately and are not inferred from this finite check.
"""
from fractions import Fraction as Q
from random import Random
from math import floor, log


def harmonic_number(n):
    return sum((Q(1, j) for j in range(1, n + 1)), Q(0))


def f_level(x, ell):
    x = sorted((Q(z) for z in x if z > 0), reverse=True)
    partial = Q(0)
    vals = []
    for t, z in enumerate(x, 1):
        partial += z
        vals.append(partial / (ell + t))
    return max(vals)


def harmonic_entropy(x):
    x = [Q(z) for z in x if z > 0]
    assert x and sum(x) == 1
    d = len(x)
    # Once the full support is active it stays active for larger ell.
    L = 0
    while f_level(x, L) != Q(1, L + d):
        L += 1
        assert L < 20000
    return harmonic_number(L + d - 1) - sum(
        (f_level(x, ell) for ell in range(L)), Q(0)
    )


def verify():
    rng = Random(20261019)
    checked = 0
    for d in range(1, 7):
        for repeat in range(110):
            weights = [rng.randint(1, 11) for _ in range(d)]
            x = [Q(a, sum(weights)) for a in weights]
            m = rng.randrange(6, 200)
            eps = Q(1, m)
            if eps > (1 - eps) * min(x):
                continue
            y = [(1 - eps) * z for z in x] + [eps]
            M = 1 // eps
            value = ((1 - eps) * harmonic_entropy(x)
                     + eps * harmonic_number(M - 1) + Q(1, M))
            assert harmonic_entropy(y) == value, (x, eps)
            checked += 1
    assert checked > 300

    # Binary entropy exact formula, including reciprocal-integer ties.
    for denominator in range(2, 101):
        for numerator in range(1, denominator // 2 + 1):
            eps = Q(numerator, denominator)
            M = 1 // eps
            predicted = eps * harmonic_number(M - 1) + Q(1, M)
            assert harmonic_entropy([1 - eps, eps]) == predicted
            checked += 1

    # Sharp two-coordinate perturbations on a rational grid.
    for q in (7, 11, 17):
        levels = [Q(i, q) for i in range(q + 1)]
        for j in range(q // 2 + 1):
            radius = Q(j, q)
            M = 1 // radius if radius else 0
            bound = (radius * harmonic_number(M - 1) + Q(1, M)) if radius else Q(0)
            if radius > Q(1, 2):
                bound = Q(1)
            for a in levels:
                for b in levels:
                    if abs(a - b) <= radius:
                        assert abs(harmonic_entropy([a, 1-a]) -
                                   harmonic_entropy([b, 1-b])) <= bound
                        checked += 1
    print(f'PASS: {checked} exact-rational identity/bound comparisons')
    for denom in (20, 100, 1000):
        eps = Q(1, denom)
        ratio = float(harmonic_entropy([1-eps, eps]))/(float(eps)*log(1/float(eps)))
        print(f'eps=1/{denom}: normalized leading ratio={ratio:.12f}')

if __name__ == '__main__':
    verify()
