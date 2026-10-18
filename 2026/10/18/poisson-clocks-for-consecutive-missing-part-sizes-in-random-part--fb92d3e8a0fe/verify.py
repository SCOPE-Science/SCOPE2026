#!/usr/bin/env python3
"""Finite checks for exact missing-run counting identities; no asymptotic proof is inferred."""
import math
from itertools import combinations


def partition_numbers(N):
    p = [1] + [0] * N
    for part in range(1, N + 1):
        for n in range(part, N + 1):
            p[n] += p[n - part]
    return p


def partitions(n, low=1):
    if n == 0:
        yield ()
        return
    for p in range(low, n + 1):
        for suffix in partitions(n - p, p):
            yield (p,) + suffix


def absent_count(n, missing, p):
    # Coefficient [z^n] product_(s in missing)(1-z^s) / product_(j>=1)(1-z^j).
    missing = sorted(set(missing))
    total = 0
    for mask in range(1 << len(missing)):
        shift = sum(s for b, s in enumerate(missing) if mask & (1 << b))
        if shift <= n:
            total += (-1 if mask.bit_count() % 2 else 1) * p[n - shift]
    return total


def exact_check():
    p = partition_numbers(36)
    ncases = 0
    for n in range(0, 29):
        parts = list(partitions(n))
        assert len(parts) == p[n]
        for r in (2, 3):
            for j in range(1, 9):
                pattern = set(range(j, j + r))
                from_parts = sum(not pattern.intersection(lam) for lam in parts)
                assert from_parts == absent_count(n, pattern, p), (n, r, j)
                ncases += 1
            for j, k in ((1, 2), (1, 4), (3, 5), (4, 8)):
                s = set(range(j, j + r)) | set(range(k, k + r))
                from_parts = sum(not s.intersection(lam) for lam in parts)
                assert from_parts == absent_count(n, s, p), (n, r, j, k)
                ncases += 1
            # All marked starts through 8, check factorial second moment exactly.
            m = 8
            a = sum(sum(not set(range(j, j + r)).intersection(lam)
                        for j in range(1, m + 1)) for lam in parts)
            b = sum(absent_count(n, range(j, j + r), p)
                    for j in range(1, m + 1))
            assert a == b, (n, r)
            ncases += 1
    return ncases


def boltzmann_check():
    c = math.pi / math.sqrt(6)
    reports = []
    for r in (2, 3, 4):
        # For each fixed r, choose two increasing N and check mean convergence
        # and the dependency-neighborhood overlap bound.
        results = []
        for N in (10**8, 10**12):
            a = N ** (r / (2 * (r + 1)))
            m = int(a)
            missing = [0.0] + [-math.expm1(-c * j / N**0.5)
                                for j in range(1, m + r + 1)]
            q = [math.prod(missing[j:j + r]) for j in range(1, m + 1)]
            mu = sum(q)
            # For each overlapping pair, union missing parts spans r+d sizes.
            b2 = sum(2 * math.prod(missing[j:j + r + d])
                     for j in range(1, m + 1)
                     for d in range(1, r)
                     if j + d <= m)
            target = c**r / (r + 1)
            results.append((abs(mu - target), b2))
        assert results[1][0] < results[0][0], (r, results)
        assert results[1][1] < results[0][1], (r, results)
        reports.append((r, results))
    return reports


def run():
    c = exact_check()
    print(f'PASS: {c} finite exact coefficient/partition comparisons (all exact integers).')
    for r, vals in boltzmann_check():
        print(f'PASS: r={r}: mean-error and overlapping-pair sum decrease: '
              f' N=1e8 {vals[0]}, N=1e12 {vals[1]}.')
    print('Finite computations do not establish the infinite point-process theorem; '
          'the proof uses a published total-variation approximation and factorial moments.')


if __name__ == '__main__':
    run()
