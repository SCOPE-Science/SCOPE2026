"""Reproduce exact chirp-basis fourth-potential identities and finite tests.

Run with Python 3 standard library: python check.py
This tests bounded examples; the infinite-range proof is in RESULT.md.
"""
from collections import Counter
from itertools import combinations
from math import comb, gcd, pi
from cmath import exp
from random import Random


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def phi(n):
    return sum(gcd(x, n) == 1 for x in range(1, n + 1))


def balanced_collisions(r, m):
    q, s = divmod(r, m)
    return (m-s)*comb(q, 2) + s*comb(q+1, 2)


def optimal_potential(n, r):
    return r*n + 2*sum(phi(d)*balanced_collisions(r,d) for d in divisors(n))


def direct_potential(n, slopes):
    return len(slopes)*n + 2*sum(gcd(a-b,n) for a,b in combinations(slopes,2))


def divisor_potential(n, slopes):
    pair_sum = 0
    for d in divisors(n):
        counts = Counter(a%d for a in slopes)
        pair_sum += phi(d)*sum(comb(x,2) for x in counts.values())
    return len(slopes)*n + 2*pair_sum


def is_balanced(n, slopes):
    for d in divisors(n):
        counts = Counter(a%d for a in slopes)
        x = [counts.get(j,0) for j in range(d)]
        if max(x) - min(x) > 1:
            return False
    return True


def verify():
    subset_cases = 0
    equality_cases = 0
    for n in [3,5,7,9,11,15]:
        minima = {r:optimal_potential(n,r) for r in range(1,n+1)}
        for r in range(1,n+1):
            assert direct_potential(n,tuple(range(r))) == minima[r]
            for slopes in combinations(range(n),r):
                f = direct_potential(n,slopes)
                assert f == divisor_potential(n,slopes)
                is_eq = f == minima[r]
                assert is_eq == is_balanced(n,slopes)
                assert f >= minima[r]
                subset_cases += 1
                equality_cases += is_eq

    rng = Random(20261010)
    random_cases = 0
    for n in [21,25,27,35,45,63,75,105]:
        for r in range(1,n+1):
            opt = optimal_potential(n,r)
            assert direct_potential(n,tuple(range(r))) == opt
            for _ in range(5):
                slopes = tuple(sorted(rng.sample(range(n),r)))
                f=direct_potential(n,slopes)
                assert f == divisor_potential(n,slopes)
                assert (f == opt) == is_balanced(n,slopes)
                random_cases += 1
    gauss_cases = 0
    max_error = 0.0
    for n in [3,5,7,9,11,15,21]:
        slope_pairs = list(combinations(range(n),2))
        if n > 15:
            slope_pairs = slope_pairs[:30]
        for a,c in slope_pairs:
            g = gcd(a-c,n)
            for ell in range(n):
                gauss = sum(exp(2j*pi*((a-c)*x*x+ell*x)/n) for x in range(n))
                expected = n*g if ell%g == 0 else 0
                error = abs(abs(gauss)**2 - expected)
                max_error=max(max_error,error)
                assert error < 3e-9
                gauss_cases += 1
            # every value ell occurs for exactly n pairs of modulations
            fourth_sum = n*sum((g/n)**2 if ell%g == 0 else 0 for ell in range(n))
            assert abs(fourth_sum-g)<1e-10
    print(f"VERIFY_OK exhaustive_nonempty_subsets={subset_cases} equality_cases={equality_cases} randomized_sets={random_cases} exact_cross_moment_cases={gauss_cases} max_gauss_abs_squared_error={max_error:.2e} status=PASS")

if __name__ == '__main__':
    verify()
