#!/usr/bin/env python3
"""Reproduce exact counts of forward-confluent relations on two-level posets.

Only Python's standard library is required.  Direct verifications check the
original FIK frame condition without using the classification formula.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from math import comb, factorial, gcd, prod


def partitions(n, least=1):
    if n == 0:
        yield ()
    else:
        for k in range(least, n + 1):
            for rest in partitions(n - k, k):
                yield (k,) + rest


def z_factor(lam):
    return prod(size ** multiplicity * factorial(multiplicity)
                for size, multiplicity in Counter(lam).items())


def fixed_formula(lam, mu):
    """Fixed relations for permutations with cycle-length profiles lam, mu."""
    k = lambda cycles, d: sum(gcd(e, d) for e in cycles)
    aa = sum(k(lam, d) for d in lam)
    ba = sum(k(lam, d) for d in mu)
    bb = sum(k(mu, d) for d in mu)

    with_top = 2 ** (aa + ba) * (
        prod(2 ** k(mu, d) + 2 ** k(lam, d) - 1 for d in mu)
        - 2 ** bb
    )
    without_top = 0
    for chosen in product((False, True), repeat=len(lam)):
        bottom_weight = prod(2 ** k(lam, f) - 1
                             for index, f in enumerate(lam) if chosen[index])
        top_weight = prod(
            2 ** k(lam, d) * (2 ** k(mu, d) - 1)
            + 2 ** sum(gcd(f, d) for index, f in enumerate(lam)
                       if not chosen[index])
            for d in mu
        )
        without_top += bottom_weight * top_weight
    return with_top + without_top


def labelled_closed(p, q):
    a = 2 ** p - 1
    without_top = sum(comb(p, u) * a ** u
                      * (2 ** p * (2 ** q - 1) + 2 ** (p - u)) ** q
                      for u in range(p + 1))
    with_top = 2 ** (p * p) * sum(
        comb(q, t) * a ** t * 2 ** (q * (p + q - t))
        for t in range(1, q + 1)
    )
    return without_top + with_top


def unlabelled_cycle_index(p, q):
    answer = sum((Fraction(fixed_formula(lam, mu), z_factor(lam) * z_factor(mu))
                  for lam in partitions(p) for mu in partitions(q)),
                 Fraction())
    assert answer.denominator == 1
    return answer.numerator


def up_masks(p, q):
    n = p + q
    top = ((1 << q) - 1) << p
    return tuple((1 << y) | (top if y < p else 0) for y in range(n))


def original_fc(rows, p, q):
    """Literal original FC quantifiers, evaluated on the specified poset."""
    n = p + q
    up = up_masks(p, q)
    for z in range(n):
        for x in range(n):
            if not (z == x or (z < p and x >= p)):
                continue
            for y in range(n):
                if rows[z] & (1 << y) and not (rows[x] & up[y]):
                    return False
    return True


def direct_full(p, q):
    n = p + q
    count = 0
    for mask in range(1 << (n * n)):
        rows = tuple((mask >> (n * i)) & ((1 << n) - 1) for i in range(n))
        count += original_fc(rows, p, q)
    return count


def direct_row_independent(p, q):
    """Check FC by actual quantifiers for each proposed top row, then multiply."""
    n = p + q
    count = 0
    for lower in product(range(1 << n), repeat=p):
        possible_top_rows = 0
        for top_row in range(1 << n):
            all_rows = tuple(lower) + tuple([top_row] * q)
            if original_fc(all_rows, p, q):
                possible_top_rows += 1
        count += possible_top_rows ** q
    return count


def cycle_lengths(perm):
    seen = set()
    lengths = []
    for point in range(len(perm)):
        if point in seen:
            continue
        x = point
        length = 0
        while x not in seen:
            seen.add(x)
            length += 1
            x = perm[x]
        lengths.append(length)
    return tuple(sorted(lengths))


def pair_orbits(perm):
    n = len(perm)
    seen = set()
    orbits = []
    for i in range(n):
        for j in range(n):
            if (i, j) in seen:
                continue
            x, y = i, j
            positions = []
            while (x, y) not in seen:
                seen.add((x, y))
                positions.append((x, y))
                x, y = perm[x], perm[y]
            orbits.append(positions)
    return orbits


def direct_fixed_nonidentity(perm, p, q):
    """Enumerate all permutation-invariant relations via ordered-pair orbits."""
    n = p + q
    assert perm != tuple(range(n))
    masks = []
    for orbit in pair_orbits(perm):
        rowbits = [0] * n
        for i, j in orbit:
            rowbits[i] |= 1 << j
        masks.append(tuple(rowbits))
    count = 0
    for choices in range(1 << len(masks)):
        rows = [0] * n
        for index, pattern in enumerate(masks):
            if choices & (1 << index):
                for i, contribution in enumerate(pattern):
                    rows[i] |= contribution
        count += original_fc(rows, p, q)
    return count


def direct_burnside(p, q):
    group = [tuple(a) + tuple(p + j for j in b)
             for a in permutations(range(p))
             for b in permutations(range(q))]
    total = direct_row_independent(p, q)
    for perm in group:
        if perm == tuple(range(p + q)):
            continue
        fixed = direct_fixed_nonidentity(perm, p, q)
        lam = cycle_lengths(perm[:p])
        mu = cycle_lengths(tuple(x - p for x in perm[p:]))
        prediction = fixed_formula(lam, mu)
        assert fixed == prediction, (p, q, lam, mu, fixed, prediction)
        total += fixed
    assert total % len(group) == 0
    return total // len(group)


def run():
    sample = [(1, 1), (1, 2), (2, 1), (2, 2),
              (1, 3), (3, 1), (2, 3), (3, 2), (3, 3), (2, 4)]
    for p, q in sample:
        assert labelled_closed(p, q) == fixed_formula((1,) * p, (1,) * q)
        print('EXACT', p, q, labelled_closed(p, q), unlabelled_cycle_index(p, q))
    for p, q in [(1, 1), (2, 1), (1, 2), (2, 2), (1, 3), (3, 1)]:
        assert direct_full(p, q) == labelled_closed(p, q)
        print('FULL_FC_OK', p, q)
    for p, q in [(2, 2), (2, 3), (3, 2)]:
        assert direct_row_independent(p, q) == labelled_closed(p, q)
        print('ROW_FC_OK', p, q)
    for p, q in [(1, 3), (2, 2), (2, 3)]:
        assert direct_burnside(p, q) == unlabelled_cycle_index(p, q)
        print('ORBIT_FC_OK', p, q)
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
