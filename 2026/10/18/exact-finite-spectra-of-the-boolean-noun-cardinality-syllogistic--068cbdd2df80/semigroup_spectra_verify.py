#!/usr/bin/env python3
"""Finite checks of Boolean-noun syllogistic spectrum construction.

The arbitrary-size theorem is proved mathematically; these bounded checks are
independent diagnostics, not a substitute for the proof.
"""
from itertools import combinations_with_replacement, product


def nonnegative_compositions(total, count):
    if count == 1:
        yield (total,)
        return
    # Stars and bars, enumerated without any algebraic assumptions.
    for bars in combinations_with_replacement(range(total + 1), count - 1):
        yield tuple(bars[i] - (bars[i - 1] if i else 0)
                    for i in range(count - 1)) + (total - bars[-1],)


def encode_conditions(generators):
    # Boolean atoms are indexed by all binary truth assignments to raw nouns.
    num_used = sum(generators)
    k = max(1, (num_used - 1).bit_length())
    total_atoms = 1 << k
    blocks, pos = [], 0
    for size in generators:
        blocks.append(tuple(range(pos, pos + size)))
        pos += size
    assert pos == num_used
    return total_atoms, blocks, set(range(pos, total_atoms))


def theory_truth(cell_sizes, blocks, forbidden):
    # Semantics of the actual allowed atomic sentences: cardinality equality
    # is two opposite >= comparisons; emptiness is All(A, complement A).
    for cell in forbidden:
        # In a finite universe, All(atom, complement atom) iff atom is empty.
        if cell_sizes[cell] != 0:
            return False
    for block in blocks:
        first = cell_sizes[block[0]]
        for cell in block[1:]:
            if not (cell_sizes[cell] >= first and first >= cell_sizes[cell]):
                return False
    return True


def is_generated(n, generators):
    # Independent unbounded-knapsack dynamic-programming membership check.
    reachable = [False] * (n + 1)
    reachable[0] = True
    for j in range(1, n + 1):
        reachable[j] = any(j >= g and reachable[j-g] for g in generators)
    return reachable[n]


def verify_spectrum(generators, max_n):
    atom_count, blocks, forbidden = encode_conditions(generators)
    checked = 0
    outcomes = []
    for n in range(1, max_n + 1):
        exists_model = False
        for counts in nonnegative_compositions(n, atom_count):
            checked += 1
            if theory_truth(counts, blocks, forbidden):
                exists_model = True
        expected = is_generated(n, generators)
        assert exists_model == expected, (generators, n, exists_model, expected)
        outcomes.append(int(exists_model))
    return checked, ''.join(map(str, outcomes))


def term_set(assignment, truthmask):
    return {i for i, a in enumerate(assignment) if truthmask & (1 << a)}


def holds(assignment, operation, u, v):
    U, V = term_set(assignment, u), term_set(assignment, v)
    if operation == 'all':
        return U <= V
    if operation == 'some':
        return len(U & V) > 0
    if operation == 'ge':
        return len(U) >= len(V)
    if operation == 'gt':
        return len(U) > len(V)
    raise AssertionError(operation)


def verify_disjoint_union():
    checked = 0
    for s in (1, 2):
        for t in (1, 2):
            for x in product(range(4), repeat=s):
                for y in product(range(4), repeat=t):
                    for u in range(16):
                        for v in range(16):
                            for op in ('all', 'some', 'ge', 'gt'):
                                checked += 1
                                if holds(x, op, u, v) and holds(y, op, u, v):
                                    assert holds(x + y, op, u, v), (x, y, u, v, op)
    return checked


if __name__ == '__main__':
    for gens, max_n in [((3, 5), 12), ((2, 3), 11), ((4,), 16), ((1,), 10)]:
        checked, bits = verify_spectrum(gens, max_n)
        print('GENERATORS', gens, 'N', max_n, 'CELL_VECTORS', checked, 'SPECTRUM_BITS', bits)
    assert is_generated(8, (3, 5)) and not is_generated(7, (3, 5))
    print('DISJOINT_UNION_ATOMIC_TESTS', verify_disjoint_union())
    print('VERIFY_OK')
