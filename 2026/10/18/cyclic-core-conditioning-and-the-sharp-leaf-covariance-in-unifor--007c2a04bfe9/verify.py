#!/usr/bin/env python3
"""Exact finite verification of a random-mapping cyclic-core/leaf theorem."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial, exp, pi, sqrt


def cyclic_vertex_count(mapping):
    n = len(mapping)
    count = 0
    for x in range(n):
        y = x
        for _ in range(n):
            y = mapping[y]
            if y == x:
                count += 1
                break
    return count


def terminal_vertex_count(mapping):
    return len(mapping) - len(set(mapping))


def conditional_leaf_pmf(n, k):
    m = n - k
    if m == 0:
        return {0: Fraction(1)}
    ans = {}
    for ell in range(m + 1):
        num = comb(m, ell) * sum(
            (-1) ** j * comb(m - ell, j) * (n - ell - j) ** (m - 1)
            for j in range(m - ell + 1)
        )
        ans[ell] = Fraction(num, n ** (m - 1))
    return ans


def check():
    assertions = 0
    for n in range(2, 7):
        observed = Counter()
        by_core = Counter()
        for mapping in product(range(n), repeat=n):
            core = cyclic_vertex_count(mapping)
            leaves = terminal_vertex_count(mapping)
            observed[core, leaves] += 1
            by_core[core] += 1
        for k in range(1, n + 1):
            expected_count = factorial(n) if k == n else Fraction(k * factorial(n) * n ** (n-k-1), factorial(n-k))
            assert by_core[k] == expected_count
            assertions += 1
            pmf = conditional_leaf_pmf(n, k)
            assert sum(pmf.values()) == 1
            assertions += 1
            for ell in range(n + 1):
                assert Fraction(observed[k, ell], by_core[k]) == pmf.get(ell, 0)
                assertions += 1
            m = n - k
            if m > 0:
                for r in range(m + 1):
                    lhs = sum(
                        Fraction(factorial(ell), factorial(ell - r)) * pmf[ell]
                        for ell in range(r, m + 1)
                    )
                    rhs = Fraction(factorial(m), factorial(m-r)) * Fraction((n-r)**(m-1), n**(m-1))
                    assert lhs == rhs
                    assertions += 1
        means = [sum(ell * conditional_leaf_pmf(n,k).get(ell,0)
                     for ell in range(n-k+1)) for k in range(1,n+1)]
        assert all(means[k-1] > means[k] for k in range(1,n))
        assertions += 1
        ek = Fraction(sum(k * v for k,v in by_core.items()), n**n)
        el = Fraction(sum(ell * count for (k,ell),count in observed.items()), n**n)
        ekl = Fraction(sum(k*ell*count for (k,ell),count in observed.items()), n**n)
        assert ekl - ek*el < 0
        assertions += 1
        assert el == n * Fraction((n-1)**n, n**n)
        assertions += 1
        print('n=%d: %d mappings; conditional laws, moments, and negative covariance verified' % (n,n**n))
    for n in (100, 1000, 10000):
        survival = 1.0
        ek = el = ekl = 0.0
        for k in range(1,n+1):
            p = survival*k/n
            m=n-k
            conditional_mean = 0 if m==0 else m*(1-1/n)**(m-1)
            ek +=k*p;el+=p*conditional_mean;ekl+=k*p*conditional_mean
            survival*=1-k/n
            if survival < 1e-200:
                break
        scaled=(ekl-ek*el)/sqrt(n)
        limit=-sqrt(pi/2)/(2*exp(1))
        assert abs(scaled-limit)<0.002
        assertions+=1
        print('n=%d: scaled covariance %.10f; proposed limit %.10f' % (n,scaled,limit))
    print('PASS: %d exact or numerical checks' % assertions)


if __name__ == '__main__':
    check()
