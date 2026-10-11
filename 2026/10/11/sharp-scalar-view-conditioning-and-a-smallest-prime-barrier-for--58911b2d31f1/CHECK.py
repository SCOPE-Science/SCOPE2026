#!/usr/bin/env python3
"""Finite checks for weighted projective Radon line sums over Z/NZ.

This is finite corroboration of the algebraic proof, not a proof for all N.
Requires Python 3 standard library only.
"""
from collections import Counter
from cmath import exp
from math import gcd, pi, prod


def factorization(n):
    q = n
    factors = []
    p = 2
    while p * p <= q:
        if q % p == 0:
            k = 0
            while q % p == 0:
                q //= p
                k += 1
            factors.append((p, k))
        p += 1
    if q > 1:
        factors.append((q, 1))
    return factors


def directions(n):
    units = [u for u in range(n) if gcd(u, n) == 1]
    seen, representatives = set(), []
    for a in range(n):
        for b in range(n):
            if gcd(gcd(a, b), n) != 1 or (a, b) in seen:
                continue
            orbit = {(u * a % n, u * b % n) for u in units}
            assert len(orbit) == len(units)
            seen.update(orbit)
            representatives.append(min(orbit))
    return representatives


def reduction(a, b, p):
    return min((u * a % p, u * b % p) for u in range(1, p))


def valuation_pair(x, y, p, k):
    m = p ** k
    if x % m == y % m == 0:
        return None
    v = 0
    while x % (p ** (v + 1)) == y % (p ** (v + 1)) == 0:
        v += 1
    return v


def verify_modulus(n):
    fac = factorization(n)
    direct = directions(n)
    dcount = len(direct)
    predicted_count = prod(p ** (k - 1) * (p + 1) for p, k in fac)
    assert dcount == predicted_count
    weights = [1 + ((7 * j * j + 11 * j + n) % 17) for j in range(dcount)]
    eigenvalues = {}
    uniform = {}
    for x in range(n):
        for y in range(n):
            compatible = [i for i, (a, b) in enumerate(direct)
                          if (a * x + b * y) % n == 0]
            eigenvalues[x, y] = sum(weights[i] for i in compatible)
            uniform[x, y] = len(compatible)
            predicted = 1
            for p, k in fac:
                v = valuation_pair(x, y, p, k)
                predicted *= p ** (k - 1) * (p + 1) if v is None else p ** v
            assert len(compatible) == predicted, (n, x, y)
    assert eigenvalues[0, 0] == sum(weights)
    nonzero = [z for frequency, z in eigenvalues.items() if frequency != (0, 0)]
    assert min(nonzero) == min(weights)
    fiber_masses = []
    for p, k in fac:
        groups = Counter()
        cardinalities = Counter()
        for (a, b), w in zip(direct, weights):
            cls = reduction(a, b, p)
            groups[cls] += w
            cardinalities[cls] += 1
        assert len(groups) == p + 1
        assert set(cardinalities.values()) == {dcount // (p + 1)}
        fiber_masses.extend(groups.values())
    assert max(nonzero) == max(fiber_masses)
    pmin = min(p for p, k in fac)
    flat_nonzero = [z for frequency, z in uniform.items() if frequency != (0, 0)]
    assert min(flat_nonzero) == 1
    assert max(flat_nonzero) == dcount // (pmin + 1)
    assert max(nonzero) / min(nonzero) >= dcount / (pmin + 1) - 1e-12
    # Exact local-valuation multiplicities, combined by CRT.
    spectrum = Counter({1: 1})
    for p, k in fac:
        local = Counter()
        local[p ** (k - 1) * (p + 1)] += 1
        for v in range(k):
            local[p ** v] += p ** (2 * (k - v)) - p ** (2 * (k - v - 1))
        next_spectrum = Counter()
        for a, count_a in spectrum.items():
            for b, count_b in local.items():
                next_spectrum[a * b] += count_a * count_b
        spectrum = next_spectrum
    assert Counter(uniform.values()) == spectrum
    # Direct line-incidence Gram kernel Fourier check for selected small cases.
    if n <= 8:
        subgroup_directions = [
            {(t * a % n, t * b % n) for t in range(n)}
            for a, b in direct
        ]
        assert all(len(H) == n for H in subgroup_directions)
        kernel = {}
        for x in range(n):
            for y in range(n):
                kernel[x, y] = sum(w for H, w in zip(subgroup_directions, weights)
                                   if (x, y) in H) / n
        for r in range(n):
            for s in range(n):
                # Fourier diagonalization of the exact normal-matrix kernel.
                derived = sum(kernel[x, y] * exp(-2j * pi * (r*x + s*y) / n)
                              for x in range(n) for y in range(n))
                assert abs(derived - eigenvalues[r, s]) < 2e-9
    return dcount


if __name__ == '__main__':
    checked = 0
    for n in range(2, 31):
        if verify_modulus(n) > 0:
            checked += 1
    print('VERIFY_OK moduli=%d weighted_endpoints=PASS CRT_multiplicities=PASS ' 
          'direct_Gram_Fourier=PASS flat_optimum=PASS' % checked)
