"""Finite boundary checks for an infinitary polyadic modal construction.

This code tests finite approximations; it does not prove the infinite-arity theorem.
"""
from functools import lru_cache

TOP = ('top',)


def neg(a):
    return ('not', a)


def conj(a, b):
    return ('and', a, b)


def modality(*args):
    return ('diamond', args)


def make_height_formulas(arity):
    def possibility(phi):
        return modality(phi, *(TOP for _ in range(arity - 1)))

    def power(n):
        phi = TOP
        for _ in range(n):
            phi = possibility(phi)
        return phi

    return [conj(power(n), neg(power(n + 1))) for n in range(arity)]


def test(arity):
    assert arity >= 1
    height_formulas = make_height_formulas(arity)
    # Worlds are -1 (root) and the natural numbers 0,...,arity-1.
    # The root witnesses every height simultaneously.
    edges = {-1: [tuple(range(arity))]}
    for n in range(1, arity):
        edges[n] = [(n - 1,) + (0,) * (arity - 1)]
    edges[0] = []

    @lru_cache(None)
    def holds(world, phi):
        kind = phi[0]
        if kind == 'top':
            return True
        if kind == 'not':
            return not holds(world, phi[1])
        if kind == 'and':
            return holds(world, phi[1]) and holds(world, phi[2])
        assert kind == 'diamond'
        return any(all(holds(children[i], phi[1][i])
                       for i in range(arity)) for children in edges[world])

    for n, phi in enumerate(height_formulas):
        assert [w for w in range(arity) if holds(w, phi)] == [n]
    witness = modality(*height_formulas)
    assert holds(-1, witness)
    assert len(edges) == arity + 1
    # An all-arity instance forces the worlds satisfying each chi_n distinct.
    for i in range(arity):
        for j in range(i + 1, arity):
            assert not any(holds(w, height_formulas[i]) and
                           holds(w, height_formulas[j]) for w in edges)


if __name__ == '__main__':
    for arity in range(1, 10):
        test(arity)
    print('INFINITE_ARITY_FMP_VERIFY_OK')
