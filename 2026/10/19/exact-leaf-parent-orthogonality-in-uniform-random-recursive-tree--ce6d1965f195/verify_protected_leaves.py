#!/usr/bin/env python3
"""Exact checks of leaf/protection covariance in uniform random recursive trees."""
from fractions import Fraction
from itertools import product
from math import factorial


def counts(parents):
    """Return (leaf, protected, leaf-parent) counts, root indexed by zero."""
    n = len(parents) + 1
    children = [[] for _ in range(n)]
    for vertex, parent in enumerate(parents, start=1):
        children[parent].append(vertex)
    leaves = sum(not group for group in children)
    protected = sum(bool(group) and all(children[j] for j in group)
                    for group in children)
    leaf_parents = sum(any(not children[j] for j in group)
                       for group in children)
    assert leaves + protected + leaf_parents == n
    return leaves, protected, leaf_parents


def truncated_exp(n):
    return sum((Fraction(-1, 1) ** k) / factorial(k) for k in range(n + 1))


def check_exact(n):
    all_parents = product(*(range(vertex) for vertex in range(1, n)))
    N = factorial(n - 1)
    sL = sP = sQ = sLL = sLP = sLQ = 0
    number = 0
    for parents in all_parents:
        L, P, Q = counts(parents)
        sL += L
        sP += P
        sQ += Q
        sLL += L * L
        sLP += L * P
        sLQ += L * Q
        number += 1
    assert number == N
    meanL, meanP, meanQ = (Fraction(s, N) for s in (sL, sP, sQ))
    covLP = Fraction(sLP, N) - meanL * meanP
    covLQ = Fraction(sLQ, N) - meanL * meanQ
    varL = Fraction(sLL, N) - meanL ** 2
    if n >= 3:
        assert meanL == Fraction(n, 2)
        assert meanP == n * (Fraction(1, 2) - truncated_exp(n))
        assert covLP == -Fraction(n, 12)
        assert varL == Fraction(n, 12)
        assert covLQ == 0
    else:
        assert (covLP, covLQ, varL) == (0, 0, 0)
    return number


def check_formal_series(max_n):
    """Independently perform formal power-series arithmetic on the root ODE."""
    from fractions import Fraction as F
    # F_u=a, F_v=b, F_uv=c, and F(z,1,1)=-log(1-z).
    # Their differential equations are solved coefficient-by-coefficient.
    a, b, c = [[F(0) for _ in range(max_n + 1)] for _ in range(3)]
    e = [F((-1) ** k, factorial(k)) for k in range(max_n + 1)]
    for n in range(max_n):
        # a' = a/(1-z) + 1.
        a[n+1] = (sum(a[:n+1]) + (1 if n == 0 else 0)) / (n + 1)
        # b' = b/(1-z) + e^{-z}/(1-z)-1.
        b[n+1] = (sum(b[:n+1]) + sum(e[:n+1]) - (1 if n == 0 else 0)) / (n+1)
        # c' = c/(1-z) + a*b/(1-z) + e^{-z}(a-z)/(1-z).
        ab = sum(a[j]*b[k-j] for k in range(n+1) for j in range(k+1))
        ea = sum(e[j]*a[k-j] for k in range(n+1) for j in range(k+1))
        ez = sum(e[:n]) if n else F(0)
        cc = sum(c[:n+1])
        c[n+1] = (cc + ab + ea - ez) / (n+1)
    for n in range(3, max_n+1):
        meanL = n*a[n]
        meanP = n*b[n]
        ELP = n*c[n]
        assert meanL == F(n, 2), (n, 'leaf expectation')
        assert meanP == n*(F(1,2)-truncated_exp(n)), (n, 'protection expectation')
        assert ELP - meanL*meanP == -F(n,12), (n, 'covariance')
    return max_n-2


def main():
    checked = sum(check_exact(n) for n in range(2, 10))
    coefficients = check_formal_series(120)
    # Nonindependence example: for n=4, L=3 forces Q=1,
    # whereas L=2,Q=2 is possible.
    assert counts((0,0,0)) == (3,0,1)
    assert counts((0,0,1)) == (2,0,2)
    print(f'PASS: {checked} enumerated trees (n=2..9), '
          f'{coefficients} exact formal coefficient tests (n=3..120), '
          'nonindependence witness')


if __name__ == '__main__':
    main()
