#!/usr/bin/env python3
"""Finite exhaustive checks of a universal medial quotient for generalized-dihedral conjugation quandles.

Usage: python3 verify.py.  Requires the Python standard library only.
These checks are finite evidence; the accompanying proof is valid for all abelian groups.
"""
from itertools import product
from math import gcd, prod


def elements(moduli):
    return list(product(*[range(m) for m in moduli]))


def operation(x, y, moduli):
    e, a = x
    d, b = y
    return e, tuple(((-1 if d else 1) * aa + 2 * e * bb) % m
                    for aa, bb, m in zip(a, b, moduli))


def expected_class(e, a, moduli):
    if e == 0:
        return e, a
    return e, tuple(v % gcd(m, 4) for v, m in zip(a, moduli))


def test(moduli):
    aa = elements(moduli)
    xs = [(e, a) for e in range(2) for a in aa]
    index = {a: i for i, a in enumerate(xs)}
    tab = [[index[operation(x, y, moduli)] for y in xs] for x in xs]

    # Independent multiplication of the underlying semidirect-product group.
    def multiply(x, y):
        e, a = x
        d, b = y
        return ((e + d) % 2,
                tuple(((-1 if d else 1) * aa + bb) % m
                      for aa, bb, m in zip(a, b, moduli)))

    def inverse(x):
        e, a = x
        if e:
            return x
        return (0, tuple(-aa % m for aa, m in zip(a, moduli)))

    for x in xs:
        for y in xs:
            assert operation(x, y, moduli) == multiply(multiply(inverse(y), x), y)
    expected = [expected_class(*x, moduli) for x in xs]
    n = len(xs)
    par = list(range(n))

    def root(i):
        while par[i] != i:
            par[i] = par[par[i]]
            i = par[i]
        return i

    def join(i, j):
        i, j = root(i), root(j)
        if i != j:
            par[i] = j

    # Brute-force all quadruples and collect the equalities imposed by mediality.
    for i in range(n):
        for j in range(n):
            ij = tab[i][j]
            for k in range(n):
                ik = tab[i][k]
                for l in range(n):
                    left = tab[ij][tab[k][l]]
                    right = tab[ik][tab[j][l]]
                    assert expected[left] == expected[right]
                    join(left, right)

    # Compute congruence closure under the binary operation, not only equation pairs.
    while True:
        before = len({root(i) for i in range(n)})
        blocks = {}
        for i in range(n):
            blocks.setdefault(root(i), []).append(i)
        for b in blocks.values():
            rep = b[0]
            for j in b[1:]:
                for k in range(n):
                    join(tab[rep][k], tab[j][k])
                    join(tab[k][rep], tab[k][j])
        after = len({root(i) for i in range(n)})
        if before == after:
            break

    classes = {}
    for i in range(n):
        classes.setdefault(root(i), set()).add(i)
    targets = {}
    for i, classid in enumerate(expected):
        targets.setdefault(classid, set()).add(i)
    assert {frozenset(c) for c in classes.values()} == {
        frozenset(c) for c in targets.values()}
    expected_count = len(aa) + prod(gcd(m, 4) for m in moduli)
    assert len(classes) == expected_count
    return len(aa), len(classes)


def main():
    cases = [(2,), (3,), (4,), (5,), (6,), (7,), (8,),
             (2, 2), (2, 3), (2, 4), (3, 3), (2, 2, 2)]
    for moduli in cases:
        size, quotient = test(moduli)
        print('A=' + 'x'.join('Z/' + str(v) for v in moduli),
              '|A|=', size, 'medial quotient=', quotient, 'OK')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
