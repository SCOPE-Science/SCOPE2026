#!/usr/bin/env python3
"""Finite checks for the first nonunique F-preconditional negation fibre.

Requires only the Python 3 standard library.  Proof of exhaustion at three
atoms is mathematical (the six-flag normal form), not inferred from testing.
"""
from itertools import permutations, product


def subset(a, b):
    return a & b == a


def axioms(f, n):
    top = (1 << n) - 1
    lattice = range(top + 1)
    for a, b, c in product(lattice, repeat=3):
        if not subset(f(top, b), b):
            return False
        if not subset(a & b, f(a, b)):
            return False
        if not subset(f(a, b), f(a, a & b)):
            return False
        if not subset(f(a, b & c), f(a, b)):
            return False
        if not subset(f(a, f(a & b, c)), f(a & b, c)):
            return False
    return all(
        f(a, a) == top
        and a & f(a, 0) == 0
        and subset(a, f(f(a, 0), 0))
        for a in lattice
    )


def make_three_atom_operation(choices):
    """Six independent flags; each takes one of three allowed values."""
    top = 7
    values = {}
    index = 0
    for a in (3, 5, 6):
        outside = top ^ a
        for atom in (1, 2, 4):
            if atom & a:
                values[a, atom] = (atom, atom | outside, top)[choices[index]]
                index += 1
    assert index == 6

    def conditional(a, b):
        b &= a
        if a == 0:
            return top
        if a == top:
            return b
        if a in (1, 2, 4):
            return top if b == a else 0
        if b == 0:
            return 0
        if b == a:
            return top
        return values[a, b]

    return conditional


def table(f, n):
    size = 1 << n
    return tuple(f(a, b) for a in range(size) for b in range(size))


def permutation_on_masks(p, mask):
    return sum(1 << p[i] for i in range(len(p)) if mask & (1 << i))


def move_table(t, p):
    size = 1 << len(p)
    inverse = {permutation_on_masks(p, a): a for a in range(size)}
    return tuple(
        permutation_on_masks(p, t[size * inverse[a] + inverse[b]])
        for a in range(size) for b in range(size)
    )


def check_two_atom_carrier():
    """All operations after the formally proved P1--P4 row reduction."""
    found = set()
    for h, p, q, r, s in product(range(4), repeat=5):
        def f(a, b):
            if a == 0:
                return h
            if a == 3:
                return b
            if a == 1:
                return q if b & 1 else p
            return s if b & 2 else r

        if axioms(f, 2):
            found.add(table(f, 2))
    assert len(found) == 2, len(found)
    assert len({tuple(t[4 * a] for a in range(4)) for t in found}) == 2
    return found


def main():
    lower = check_two_atom_carrier()
    assert len(lower) == 2
    # Single-atom carrier: top row identity, empty row top by ID.
    one = lambda a, b: 1 if a == 0 else b
    assert axioms(one, 1)

    tables = set()
    for choices in product(range(3), repeat=6):
        f = make_three_atom_operation(choices)
        assert axioms(f, 3), choices
        assert tuple(f(a, 0) for a in range(8)) == (7, 0, 0, 0, 0, 0, 0, 0)
        tables.add(table(f, 3))
    assert len(tables) == 729

    group = list(permutations(range(3)))
    fixed = []
    for p in group:
        n = sum(move_table(t, p) == t for t in tables)
        fixed.append(n)
        fixed_atoms = sum(p[i] == i for i in range(3))
        expected = {3: 729, 1: 27, 0: 9}[fixed_atoms]
        assert n == expected
    assert sorted(fixed) == [9, 9, 27, 27, 27, 729]
    assert sum(fixed) // len(group) == 138
    print('VERIFY_OK: B2=1, B4=2 distinct negations, B8 fibre=729, isomorphism classes=138')


if __name__ == '__main__':
    main()
