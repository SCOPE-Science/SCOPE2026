#!/usr/bin/env python3
"""Finite checks for the sharp two-null coefficient-amplitude theorem.

The proof covers all primes; this script checks finite orders only.
"""
import cmath
import itertools
import math

PRIMES = (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
tests = 0
null_checks = 0
for p in PRIMES:
    q = p // 3
    sharp = math.sin(math.pi * (q + 1) / p) / math.sin(math.pi * q / p)
    root = [cmath.exp(2j * math.pi * r / p) for r in range(p)]
    xs = (0, 1, 2)
    optimal_deltas = []
    for da, db in itertools.product(range(p), repeat=2):
        if (da, db) == (0, 0):
            continue
        k = [(da * x * x + db * x) % p for x in xs]
        if len(set(k)) != 3:
            continue
        a, b, c = (abs(root[k[1]] - root[k[2]]),
                   abs(root[k[2]] - root[k[0]]),
                   abs(root[k[0]] - root[k[1]]))
        val = max(a, b, c) / min(a, b, c)
        assert val >= sharp - 2e-12, (p, da, db, val, sharp)
        tests += 1
        if abs(val - sharp) < 2e-12:
            optimal_deltas.append((da, db))
            # Cofactors vanish at both origin and this frequency.
            u = [root[z] for z in k]
            coeff = (u[1] - u[2], u[2] - u[0], u[0] - u[1])
            assert abs(sum(coeff)) < 1e-11
            assert abs(sum(v * w for v, w in zip(coeff, u))) < 1e-11
            assert abs(max(map(abs, coeff)) / min(map(abs, coeff)) - sharp) < 1e-11
            null_checks += 1
    assert len(optimal_deltas) == (12 if p == 5 else 6), (p, len(optimal_deltas))
    if p <= 13:
        # Exact cardinality of the two prescribed Fourier zeros,
        # checked numerically on the full finite grid for each optimal delta.
        for da, db in optimal_deltas:
            u = [root[(da*x*x+db*x) % p] for x in xs]
            coeff = (u[1]-u[2],u[2]-u[0],u[0]-u[1])
            zeros = 0
            for a, b in itertools.product(range(p),repeat=2):
                z = sum(coeff[j] * root[(a*x*x+b*x) % p] for j,x in enumerate(xs))
                zeros += abs(z) < 1e-9
            assert zeros == 2, (p,da,db,zeros)
            null_checks += p*p
print(f'VERIFY_OK finite_chord_comparisons={tests}; constructed_null_and_grid_checks={null_checks}; primes={len(PRIMES)}; p5_delta=12; p_ge7_delta=6')
