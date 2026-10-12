#!/usr/bin/env python3
"""Finite checks for the classification of bounded-height modal algebras.

Run with Python 3 standard library only.  The proof for every atom size is
mathematical; these finite checks serve as independent falsification tests.
"""
from itertools import combinations, permutations, product
from math import comb, factorial


def no_three_step_path(rows, n):
    """Checks that R composed with itself three times is empty."""
    for x in range(n):
        for y in range(n):
            if (rows[x] >> y) & 1:
                for z in range(n):
                    if ((rows[y] >> z) & 1) and rows[z]:
                        return False
    return True


def is_subdirectly_irreducible(rows, n):
    """Enumerates Boolean congruence ideals stable under the diamond."""
    nonzero_ideals = []
    for subset in range(1, 1 << n):
        # Each such ideal is the powerset of the chosen set of atoms.
        if all(not (rows[x] & subset) or ((subset >> x) & 1)
               for x in range(n)):
            nonzero_ideals.append(subset)
    return any(all((candidate & other) == candidate
                   for other in nonzero_ideals)
               for candidate in nonzero_ideals)


def labeled_formula(n):
    return (1 if n == 1 else
            n * sum(comb(n - 1, k) * (2 * (2**k - 1))**(n - 1 - k)
                    for k in range(1, n)))


def canonical_constructions(n):
    if n == 1:
        return {(0,)}
    out = set()
    for root in range(n):
        others = [i for i in range(n) if i != root]
        for k in range(1, n):
            for level_one in combinations(others, k):
                level_two = [i for i in others if i not in level_one]
                base = [0] * n
                for x in level_one:
                    base[root] |= 1 << x
                for choices in product(range(2 * (2**k - 1)),
                                       repeat=len(level_two)):
                    rows = base[:]
                    for x, value in zip(level_two, choices):
                        parents = 1 + value // 2
                        if value % 2:
                            rows[root] |= 1 << x
                        for j, parent in enumerate(level_one):
                            if (parents >> j) & 1:
                                rows[parent] |= 1 << x
                    out.add(tuple(rows))
    return out


def graph_canonical_form(rows, n):
    best = None
    for pi in permutations(range(n)):
        transformed = [0] * n
        for i in range(n):
            for j in range(n):
                if (rows[i] >> j) & 1:
                    transformed[pi[i]] |= 1 << pi[j]
        result = tuple(transformed)
        if best is None or result < best:
            best = result
    return best


def unlabeled_burnside(n):
    if n == 1:
        return 1
    total = 0
    for k in range(1, n):
        m = n - 1 - k
        types = [(sub, bit) for sub in range(1, 1 << k)
                 for bit in range(2)]
        fixed_sum = 0
        for pi in permutations(range(k)):
            seen = set()
            cycle_lengths = []
            for base in types:
                if base in seen:
                    continue
                t = base
                length = 0
                while t not in seen:
                    seen.add(t)
                    sub, bit = t
                    image = sum(1 << pi[j] for j in range(k)
                                if (sub >> j) & 1)
                    t = (image, bit)
                    length += 1
                cycle_lengths.append(length)
            coefficient = [0] * (m + 1)
            coefficient[0] = 1
            for ell in cycle_lengths:
                # Multiplying by (1 - t^ell)^(-1).
                for j in range(ell, m + 1):
                    coefficient[j] += coefficient[j - ell]
            fixed_sum += coefficient[m]
        assert fixed_sum % factorial(k) == 0
        total += fixed_sum // factorial(k)
    return total


def run():
    for n in range(1, 5):
        selected = set()
        for bits in range(1 << (n * n)):
            rows = tuple((bits >> (i * n)) & ((1 << n) - 1)
                         for i in range(n))
            admissible = no_three_step_path(rows, n)
            if admissible and is_subdirectly_irreducible(rows, n):
                selected.add(rows)
        independent = canonical_constructions(n)
        assert selected == independent
        assert len(selected) == labeled_formula(n)
        orbits = len({graph_canonical_form(rows, n)
                      for rows in selected})
        assert orbits == unlabeled_burnside(n)
        print(f'n={n}: exhaustive={1 << (n*n)}, '
              f'labeled={len(selected)}, isomorphism_types={orbits}')
    for n in range(5, 9):
        print(f'n={n}: labeled_formula={labeled_formula(n)}, '
              f'isomorphism_formula={unlabeled_burnside(n)}')
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
