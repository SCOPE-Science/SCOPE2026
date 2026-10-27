"""Independent finite-tree moment enumeration and variance-asymptotic diagnostics.

Run: python3 verify.py . No third-party packages.
Finite checks do not establish the infinite-dimensional limit claims.
"""
from fractions import Fraction
from itertools import product
from math import gamma, log
from random import Random


def moments_enumerated(p):
    """Exact E[T], E[T^2] for all independent recursive-tree parent choices."""
    n = len(p) - 1
    W = [Fraction(0), Fraction(1)]
    w = [Fraction(0), Fraction(1)]
    for j in range(2, n + 1):
        W.append(W[-1] / (1 - p[j]))
        w.append(p[j] * W[-1])
    choices = [range(1, j) for j in range(2, n + 1)]
    E = E2 = Fraction(0)
    count = 0
    for parents in product(*choices):
        depths = [0] * (n + 1)
        prob = Fraction(1)
        total = 0
        for j, parent in enumerate(parents, start=2):
            depths[j] = depths[parent] + 1
            total += depths[j]
            prob *= w[parent] / W[j - 1]
        E += prob * total
        E2 += prob * total * total
        count += 1
    return E, E2 - E * E, count


def moments_recursion(p):
    n = len(p) - 1
    mean = sum((n - j) * p[j] for j in range(1, n))
    v = Fraction(0)
    variance = Fraction(0)
    for j in range(2, n + 1):
        variance += (1 + (n - j) * p[j])**2 * v
        v = (1 - p[j]**2) * v + p[j] * (1 - p[j])
    return mean, variance


def beta(a, b):
    return gamma(a) * gamma(b) / gamma(a + b)


def variance_phase(a, c, n):
    v = 0.0
    Var = 0.0
    Q = 0.0
    for j in range(2, n + 1):
        p = c / (j**a + c)
        Var += (1 + (n - j) * p)**2 * v
        Q += p*p*v
        v = (1 - p*p) * v + p * (1 - p)
    return Var, Q, v


def main():
    rng = Random(314159)
    tested = 0
    configurations = 0
    for n in range(3, 8):
        for case in range(7):
            p = [Fraction(0), Fraction(1)]
            for j in range(2, n + 1):
                d = rng.randint(3, 11)
                p.append(Fraction(rng.randint(1, d - 1), d))
            exact_mean, exact_var, count = moments_enumerated(p)
            recurrence_mean, recurrence_var = moments_recursion(p)
            assert exact_mean == recurrence_mean, (n, case, 'mean')
            assert exact_var == recurrence_var, (n, case, 'variance')
            tested += 1
            configurations += count
    print(f'EXACT PASS: {tested} input sequences, {configurations} parent configurations.')

    c = 0.8
    for a in (0.35, 0.50, 0.60, 2.0/3.0, 0.80):
        n = 300000
        var, q, v = variance_phase(a, c, n)
        if a < .5:
            exponent = 3 - a
            limit = c * beta(1-a,3)
            measured = var / n**exponent
        elif a == .5:
            exponent = 2.5
            limit = (c**3/(c*c+.5))*beta(.5,3)
            measured = var / n**exponent
        elif a < 2.0/3.0:
            exponent = 4 - 3*a
            limit = c**3/(1-a)*beta(2-3*a,3)
            measured = var / n**exponent
        elif a == 2.0/3.0:
            exponent = 2.0
            limit = 3*c**3
            measured = var / (n*n*log(n))
        else:
            exponent = 2.0
            limit = float('nan')  # model-dependent limit, not known a priori
            measured = var / (n*n)
        assert measured > 0
        print(f'asymptotic illustration a={a:.5f}, scaled={measured:.7f}, theoretical={limit:.7f}, finite_Q={q:.7f}, finite_v={v:.4f}')
    print('FINITE COMPUTATIONS COMPLETED; NOT A PROOF OF ASYMPTOTICS.')


if __name__ == '__main__':
    main()
