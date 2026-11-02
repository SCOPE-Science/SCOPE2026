#!/usr/bin/env python3
"""Finite checks for unlabelled coloured partial-injection structures.
This is finite experimental evidence, not a proof of the general limit theorem.
"""
from itertools import combinations, permutations, product
from math import gcd, comb, isqrt
from fractions import Fraction


def phi(n):
    return sum(gcd(k, n) == 1 for k in range(1, n + 1))


def necklace_count(q, n):
    return sum(phi(d) * q ** (n // d) for d in range(1, n + 1) if n % d == 0) // n


def coefficient_counts(q, nmax):
    b = [0] + [q ** n + necklace_count(q, n) for n in range(1, nmax + 1)]
    a = [1]
    for n in range(1, nmax + 1):
        s = sum(sum(d * b[d] for d in range(1, k + 1) if k % d == 0) * a[n - k]
                for k in range(1, n + 1))
        assert s % n == 0
        a.append(s // n)
    return a


def canon(n, edge, color):
    indeg = [0] * n
    for x, y in edge.items():
        indeg[y] += 1
    used = set()
    parts = []
    for x in range(n):
        if indeg[x] == 0:
            path = []
            t = x
            while t not in used:
                used.add(t)
                path.append(color[t])
                t = edge.get(t)
                if t is None:
                    break
            parts.append(('P', tuple(path)))
    for x in range(n):
        if x in used:
            continue
        cyc = []
        t = x
        while t not in used:
            used.add(t)
            cyc.append(color[t])
            t = edge[t]
        parts.append(('C', min(tuple(cyc[j:] + cyc[:j]) for j in range(len(cyc)))))
    return tuple(sorted(parts))


def brute_unlabelled(q, n):
    seen = set()
    carrier = range(n)
    for k in range(n + 1):
        for domain in combinations(carrier, k):
            for image in combinations(carrier, k):
                for image_perm in permutations(image):
                    f = dict(zip(domain, image_perm))
                    for colors in product(range(q), repeat=n):
                        seen.add(canon(n, f, colors))
    return seen


def polynomial_times_a(a, factors):
    coeff = [1]
    for factor in factors:
        new = [0] * (len(coeff) + len(factor) - 1)
        for i, x in enumerate(coeff):
            for j, y in enumerate(factor):
                new[i + j] += x * y
        coeff = new
    return [sum(coeff[k] * a[n - k] for k in range(min(n, len(coeff) - 1) + 1))
            for n in range(len(a))]


def one_minus_z_power(k):
    return [1] + [0] * (k - 1) + [-1]


def run():
    for q in [1, 2, 3]:
        a = coefficient_counts(q, 100)
        for n in range(0, 5 if q == 2 else 4):
            brute = brute_unlabelled(q, n)
            assert a[n] == len(brute), (q, n, a[n], len(brute))
        assert all(a[n] > 0 for n in range(101))
        if q == 2:
            assert a[:9] == [1, 4, 17, 60, 203, 640, 1959, 5776, 16650]
        # Inclusion-exclusion for the probability of at least one specified coloured singleton.
        remove = polynomial_times_a(a, [one_minus_z_power(1)])
        for n in range(1, 100):
            assert a[n] - remove[n] == a[n - 1]
            assert Fraction(a[n - 1], a[n]) > 0
        # Exact joint multiplicity of two distinct component types, of sizes 1 and 2.
        rem2 = polynomial_times_a(a, [one_minus_z_power(1), one_minus_z_power(2)])
        for n in range(4, 100):
            assert 0 < rem2[n] < a[n]
        print(f'q={q}: coefficients, independent enumeration, and marked-component algebra OK; '
              f'a_100={a[100]}, singleton_100={float(Fraction(a[99],a[100])):.9f}')
    print('ALL_CHECKS_OK')

if __name__ == '__main__':
    run()
