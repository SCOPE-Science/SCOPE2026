"""Exact checks illustrating weighted variation for discrete nonlinear cycle heat.

This checks finite instances and a complete finite sign certificate for one
five-cycle at exponent p=3; the general theorem requires the written proof.
"""
from fractions import Fraction as Q
from itertools import product


def derivative(weights, x, p=3):
    """Exact right derivative for integer exponents p=2 or p=3."""
    n = len(x)
    assert sum(x) == 0 and p in (2, 3)
    flux = list(x) if p == 2 else [z * abs(z) for z in x]
    dx = [flux[(i-1) % n] + flux[(i+1) % n] - 2*flux[i]
          for i in range(n)]
    return sum(weights[i] * (dx[i] if x[i] > 0 else
                             -dx[i] if x[i] < 0 else abs(dx[i]))
               for i in range(n))


def quadratic_simplex_max(coefficients):
    """Exact maximum of sum c_i t_i^2 for t_i>=0, sum t_i=1."""
    if max(coefficients) >= 0:
        return max(coefficients)
    return -Q(1) / sum(-Q(1) / c for c in coefficients)


def sign_bound(weights, power):
    """Exact supremum of the right derivative at fixed total positive mass 1.

    The sign vector runs through all strictly signed chambers, with zero-valued
    coordinates included through their limits. power=1 handles p=2, and
    power=2 handles p=3. The zero-sum edge constraint is enforced.
    """
    n = len(weights)
    maxima = []
    for signs in product((-1, 1), repeat=n):
        if min(signs) == max(signs):
            continue
        c = [signs[i] * (weights[(i-1)%n]*signs[(i-1)%n]
                + weights[(i+1)%n]*signs[(i+1)%n]) - 2*weights[i]
             for i in range(n)]
        pos = [c[i] for i in range(n) if signs[i] > 0]
        neg = [c[i] for i in range(n) if signs[i] < 0]
        if power == 1:
            z = max(pos) + max(neg)
        else:
            z = quadratic_simplex_max(pos) + quadratic_simplex_max(neg)
        maxima.append((z, signs))
    return max(maxima)


def main():
    count = 0
    for n in range(3, 9):
        w = [Q(1)] * n
        for vals in product((-2, -1, 0, 1, 2), repeat=n):
            if sum(vals) != 0 or all(v == 0 for v in vals):
                continue
            d = derivative(w, [Q(v) for v in vals], 3)
            assert d <= 0, (n, vals, d)
            if n <= 5:
                assert d < 0, (n, vals, d)
            count += 1
    print('Uniform p=3 cycle derivative tests:', count)

    w5 = [Q(1), Q(3, 2), Q(1), Q(3, 2), Q(1)]
    sharp5, signs5 = sign_bound(w5, 2)
    assert sharp5 == -Q(1, 4)
    print('Complete five-cycle p=3 sign certificate:',
          'maximum =', sharp5, 'attaining signs =', signs5)

    w6 = [Q(1), Q(3, 2)] * 3
    linear, _ = sign_bound(w6, 1)
    cubic, signs6 = sign_bound(w6, 2)
    assert linear == 0 and cubic == Q(1, 2)
    print('Alternating six-cycle p=2 sign maximum:', linear)
    print('Alternating six-cycle p=3 sign maximum:', cubic,
          'signs:', signs6)

    for denominator in (10, 100, 1000):
        eps = Q(1, denominator)
        x = [-eps, -(1-eps), Q(0), Q(0), Q(1), Q(0)]
        d3 = derivative(w6, x, 3)
        assert d3 == 2*eps - 3*eps*eps, (eps, d3)
        assert d3 > 0
        count += 1
    print('Explicit six-cycle p=3 right-derivative witness:',
          '2 epsilon - 3 epsilon^2 > 0 (tested exactly)')
    print('All exact tests passed.')


if __name__ == '__main__':
    main()
