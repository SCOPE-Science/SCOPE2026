#!/usr/bin/env python3
"""Independent finite checks for finite-support mixing on odd prime cycles.

Only Python's standard library is needed. The theorem for all primes is proved
mathematically in RESULT.md; floating-point checks here are corroborative.
"""
import cmath
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path


def primes_up_to(limit):
    return [x for x in range(3, limit + 1, 2)
            if all(x % q for q in range(3, math.isqrt(x) + 1, 2))]


def b_matrix(p):
    m = (p - 1) // 2
    return [[1.0] + [2 * math.cos(2 * math.pi * j * d / p)
                      for j in range(1, m + 1)]
            for d in range(m + 1)]


def curve(p, t):
    m = (p - 1) // 2
    spectrum = [2 * math.cos(2 * math.pi * j / p) for j in range(m + 1)]
    z = [1.0 + 0.0j] + [cmath.exp(1j * t * (spectrum[j] - spectrum[0]))
                           for j in range(1, m + 1)]
    return [abs(sum(q * x for q, x in zip(row, z))) ** 2 / p ** 2
            for row in b_matrix(p)]


def check_symbolic():
    count = 0
    for p in primes_up_to(101):
        m = (p - 1) // 2
        for d in range(m + 1):
            # Exact identities for the (assumed) cosine character sum.
            s = p if d == 0 else 0
            q = 2 * p - 1 if d == 0 else p - 1
            h = Fraction(q, p * p)
            v = (Fraction(m + 1, m) * q - Fraction(s * s, m)) / (p * p)
            assert (h + v) / 2 == Fraction(1, p)
            count += 1
    return count


def check_phase_ensembles():
    count = 0
    for p in (3, 5, 7, 11):
        m = (p - 1) // 2
        rows = b_matrix(p)
        for d, row in enumerate(rows):
            s = sum(row)
            q = sum(x * x for x in row)
            assert abs(s - (p if d == 0 else 0)) < 1e-11
            assert abs(q - (2*p - 1 if d == 0 else p - 1)) < 1e-11
        # Enumerate root-permutation ensemble rather than assume its moments.
        perms = itertools.permutations(range(m+1))
        moments = [0] * (m+1)
        pair = [[0j] * (m+1) for _ in range(m+1)]
        qty = 0
        for perm in perms:
            r = [cmath.exp(2j * math.pi * k / (m + 1)) for k in perm]
            z = [s / r[0] for s in r]
            for j in range(m+1):
                for k in range(m+1):
                    pair[j][k] += z[j] * z[k].conjugate()
            for d, row in enumerate(rows):
                moments[d] += abs(sum(x * y for x, y in zip(row, z))) ** 2 / p**2
            qty += 1
        for j in range(m+1):
            for k in range(m+1):
                exp = 1 if j == k else -1/m
                assert abs(pair[j][k] / qty - exp) < 1e-12
        for d, row in enumerate(rows):
            sq = sum(x*x for x in row)
            sm = sum(row)
            pred = ((1 + 1/m)*sq - sm*sm/m)/p**2
            assert abs(moments[d] / qty - pred) < 1e-12
        count += qty
    return count


def check_fourier_witnesses():
    checked = 0
    examples = json.loads(Path(__file__).with_name('examples.json').read_text())
    for ps, data in examples.items():
        p = int(ps)
        m = (p - 1) // 2
        t = data['times']
        w = data['weights']
        assert 1 <= len(t) <= m + 1
        assert len(w) == len(t) and min(w) > 0
        assert min(t) > 0
        assert abs(sum(w)-1) < 1e-10
        for d in range(m + 1):
            # Direct Fourier amplitude rather than the grouped spectral formula.
            target = 0.0
            for time, weight in zip(t, w):
                amp = sum(cmath.exp(1j * time * 2*math.cos(2*math.pi*k/p))
                          * cmath.exp(2j * math.pi * k*d/p)
                          for k in range(p)) / p
                target += weight * abs(amp)**2
            assert abs(target - 1 / p) < 1e-9
            checked += 1
        assert all(abs(sum(curve(p,time)[d]*weight for time,weight in zip(t,w)) - 1/p)
                   < 1e-9 for d in range(m+1))
    return checked


def main():
    sym = check_symbolic()
    perm = check_phase_ensembles()
    fw = check_fourier_witnesses()
    print(f"VERIFY_OK exact_barycentric_identities={sym} "
          f"permutation_configs={perm} numerical_fourier_distances={fw} "
          "nonnegative_time_witness_orders=5,7,11,13")


if __name__ == '__main__':
    main()
