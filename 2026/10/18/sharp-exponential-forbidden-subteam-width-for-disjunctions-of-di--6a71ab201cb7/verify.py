#!/usr/bin/env python3
"""Finite computational tests for the exact constancy-disjunction coherence theorem.

This is a finite check, not a substitute for the unrestricted proof.
Requires only the Python standard library.
"""
from itertools import product, combinations
from random import Random


def covering_choice(rows, n):
    if not rows:
        return ()
    alphabets = [sorted({r[i] for r in rows}) for i in range(n)]
    for a in product(*alphabets):
        if all(any(row[i] == a[i] for i in range(n)) for row in rows):
            return a
    return None


def tensor(vecs):
    out = (1,)
    for vec in vecs:
        out = tuple(x * y for x in out for y in vec)
    return out


def certificate(rows, n):
    """Check an actual invertible diagonal dual-pairing minor."""
    witness = []
    points = []
    for u in rows:
        w = covering_choice([v for v in rows if v != u], n)
        assert w is not None
        assert all(u[i] != w[i] for i in range(n))
        witness.append(w)
        points.append(tensor([(1, int(u[i])) for i in range(n)]))
    for iu, w in enumerate(witness):
        covec = tensor([(-int(w[i]), 1) for i in range(n)])
        for iv, p in enumerate(points):
            pairing = sum(x * y for x, y in zip(covec, p))
            assert (pairing != 0) == (iu == iv)
    assert len(rows) <= (1 << n)
    return len(rows) * len(rows)


def exhaustive(n, q):
    universe = tuple(product(range(q), repeat=n))
    assert len(universe) <= 9
    m, minimal, pairings, failed = len(universe), 0, 0, 0
    for mask in range(1 << m):
        rows = [universe[i] for i in range(m) if mask & (1 << i)]
        if covering_choice(rows, n) is not None:
            continue
        failed += 1
        if all(covering_choice(rows[:i] + rows[i + 1:], n) is not None for i in range(len(rows))):
            minimal += 1
            pairings += certificate(rows, n)
    return (1 << m, failed, minimal, pairings)


def random_check(n, q, trials, seed):
    rng = Random(seed)
    universe = list(product(range(q), repeat=n))
    certs, pairings = 0, 0
    for _ in range(trials):
        rows = [row for row in universe if rng.getrandbits(1)]
        if covering_choice(rows, n) is not None:
            continue
        rng.shuffle(rows)
        for row in list(rows):
            reduced = [v for v in rows if v != row]
            if covering_choice(reduced, n) is None:
                rows = reduced
        assert covering_choice(rows, n) is None
        assert all(covering_choice([v for v in rows if v != u], n) is not None for u in rows)
        certs += 1
        pairings += certificate(rows, n)
    return certs, pairings


def binary_cube(n):
    cube = list(product((0, 1), repeat=n))
    assert covering_choice(cube, n) is None
    for r in cube:
        assert covering_choice([v for v in cube if v != r], n) is not None
    return certificate(cube, n)


def main():
    totals = [exhaustive(n, q) for n, q in ((1, 2), (2, 2), (3, 2), (2, 3))]
    assert all(a > 0 and m > 0 and p > 0 for a, f, m, p in totals)
    random_tests = [random_check(n, q, 140, 1000 + 17*n + q) for n,q in ((3,3),(4,3))]
    cubes = [binary_cube(n) for n in range(1, 7)]
    print('CONSTANCY_COHERENCE_VERIFY_OK exhaustive_teams=%d failures=%d minimal=%d random_minimal=%d tensor_pairings=%d cube_levels=1..6' % (
        sum(v[0] for v in totals), sum(v[1] for v in totals), sum(v[2] for v in totals),
        sum(v[0] for v in random_tests),
        sum(v[3] for v in totals)+sum(v[1] for v in random_tests)+sum(cubes)))


if __name__ == '__main__':
    main()
