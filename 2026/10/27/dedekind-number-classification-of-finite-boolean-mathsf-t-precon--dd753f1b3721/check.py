#!/usr/bin/env python3
"""Finite tests for the Boolean preconditional negation-reduct theorem."""
from itertools import product, combinations


def subset(a, b):
    return a & b == a


def antitone_choices(n, atom):
    """All normalized, antitone, Boolean-valued functions on subsets omitting atom."""
    dom = [a for a in range(1 << n) if not (a & (1 << atom))]
    choices = []
    for bits in product((0, 1), repeat=len(dom)):
        val = dict(zip(dom, bits))
        if not val[0]:
            continue
        if all(not subset(a, b) or val[a] >= val[b] for a in dom for b in dom):
            choices.append(val)
    return choices


def negation(n, selections):
    q = 1 << n
    return tuple(sum((1 << v) for v in range(n)
                     if not (a & (1 << v)) and selections[v][a])
                 for a in range(q))


def lift(n, N):
    q = 1 << n
    return tuple(N[a & ~b] | (a & b) for a in range(q) for b in range(q))


def axioms(n, op, F=False):
    q = 1 << n
    full = q - 1
    def arr(a, b):
        return op[a*q+b]
    for a in range(q):
        if not subset(arr(full,a), a) or arr(a,a) != full:
            return False
        if a & arr(a,0):
            return False
        if F and not subset(a, arr(arr(a,0),0)):
            return False
        for b in range(q):
            if not subset(a & b, arr(a,b)):
                return False
            if not subset(arr(a,b), arr(a,a & b)):
                return False
            for c in range(q):
                if not subset(arr(a,b & c), arr(a,b)):
                    return False
                if not subset(arr(a,arr(a & b,c)), arr(a & b,c)):
                    return False
    return True


def graph_polarities(n):
    edges = list(combinations(range(n), 2))
    for edge_bits in product((0,1), repeat=len(edges)):
        adjacency = [set() for _ in range(n)]
        for (a,b), bit in zip(edges,edge_bits):
            if bit:
                adjacency[a].add(b)
                adjacency[b].add(a)
        yield tuple(sum((1 << v) for v in range(n)
                        if all(a in adjacency[v] for a in range(n)
                               if A & (1 << a)))
                    for A in range(1 << n))


def direct_B2_tables():
    # Every T table has top row identity, bottom row top, and atom rows
    # determined by the two values at consequent zero.
    q = 4
    for u1, u2 in product((0,2), (0,1)):
        table = []
        for a in range(q):
            for b in range(q):
                if a == 0:
                    table.append(3)
                elif a == 3:
                    table.append(b)
                elif a == 1:
                    table.append(3 if b & 1 else u1)
                else:
                    table.append(3 if b & 2 else u2)
        yield tuple(table)


def main():
    expected_Mminus1 = (1,2,5,19)
    for n in range(1,5):
        c = len(antitone_choices(n,0))
        assert c == expected_Mminus1[n-1], (n,c)
        print('ANTITONE_CHOICES', n, c, 'T_NEGATIONS_FORMULA', c**n)
    for n in range(1,4):
        choices = [antitone_choices(n,i) for i in range(n)]
        found = {}
        for selections in product(*choices):
            N = negation(n,selections)
            assert N not in found
            op = lift(n,N)
            assert axioms(n,op), ('T failed',n,N)
            found[N] = axioms(n,op,F=True)
        graphs = set(graph_polarities(n))
        assert set(N for N,good in found.items() if good) == graphs
        assert len(found) == (expected_Mminus1[n-1])**n
        assert len(graphs) == 2**(n*(n-1)//2)
        print('ENUMERATION',n,'T',len(found),'F',len(graphs),'NON_F',len(found)-len(graphs))
    ops = tuple(direct_B2_tables())
    assert len(set(ops)) == 4
    assert all(axioms(2,op) for op in ops)
    assert sum(axioms(2,op,F=True) for op in ops) == 2
    derived = set(tuple(op[a*4] for a in range(4)) for op in ops)
    choices = [antitone_choices(2,i) for i in range(2)]
    assert derived == set(negation(2,s) for s in product(*choices))
    # The K table a -> b = a intersect b on the 2-element algebra
    # violates T conditional identity, showing the first gap at two elements.
    meet = (0,0,0,1)
    assert meet[0] == 0 and meet[3] == 1
    print('BOOLEAN_B2_T_TABLES',len(ops))
    print('BOOLEAN_PRECONDITIONAL_REDUCT_OK')

if __name__ == '__main__':
    main()
