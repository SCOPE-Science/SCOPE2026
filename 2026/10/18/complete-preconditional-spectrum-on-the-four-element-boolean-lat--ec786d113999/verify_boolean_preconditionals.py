#!/usr/bin/env python3
"""Finite Boolean preconditional theorem: exhaustive independent checks.

The underlying Boolean lattice is represented by bit masks 0, 1, 2, 3.
This program tests the five defining inequalities, the symbolic normal
form, the induced subclass, and the two stronger conditional subclasses.
"""
from collections import Counter
from itertools import product

B = range(4)
ATOMS = (1, 2)
le = lambda a, b: (a & b) == a
swap = lambda z: ((z & 1) << 1) | ((z & 2) >> 1)


def normal_form_operations():
    """P1--P4 candidates, before testing P5."""
    choices = {}
    for a in ATOMS:
        choices[a] = [(u, v) for v in (a, 3) for u in B if le(u, v)]
    for t, x, y in product(B, choices[1], choices[2]):
        u1, v1 = x
        u2, v2 = y
        def arrow(a, b):
            return (
                t if a == 0 else
                b if a == 3 else
                (v1 if a & b else u1) if a == 1 else
                (v2 if a & b else u2)
            )
        table = tuple(tuple(arrow(a, b) for b in B) for a in B)
        yield (t, u1, v1, u2, v2), table


def axioms(table):
    f = lambda a,b: table[a][b]
    for a, b, c in product(B, repeat=3):
        if not le(f(3, a), a): return False
        if not le(a & b, f(a,b)): return False
        if not le(f(a,b), f(a,a & b)): return False
        if not le(f(a,b & c),f(a,b)): return False
        if not le(f(a,f(a & b,c)), f(a & b,c)): return False
    return True


def symbolic_condition(z):
    t, u1, v1, u2, v2 = z
    if not (v1 in (1,3) and v2 in (2,3)): return False
    if not (le(u1,v1) and le(u2,v2)): return False
    for a,u,v in ((1,u1,v1),(2,u2,v2)):
        if (a & u) and u != v: return False
        if a & t:
            if not le(v,t): return False
        elif not le(u,t): return False
    return True


def swap_table(table):
    return tuple(tuple(swap(table[swap(a)][swap(b)]) for b in B) for a in B)


def is_T(table):
    return all(table[a][a] == 3 and (a & table[a][0]) == 0 for a in B)


def is_F(table):
    if not is_T(table): return False
    return all(le(a,table[table[a][0]][0]) for a in B)


def is_induced(table):
    return all(table[a][b] == (table[a][0] | (a & b)) for a,b in product(B,repeat=2))


def collect():
    all_candidates = list(normal_form_operations())
    assert len(all_candidates) == 144
    for z,table in all_candidates:
        assert axioms(table) == symbolic_condition(z), z
    good = [(z,table) for z,table in all_candidates if axioms(table)]
    assert len(good)==41
    assert Counter(z[0] for z,table in good) == {0:4,1:6,2:6,3:25}
    assert len({table for z,table in good}) == len(good)
    assert len({min(table, swap_table(table)) for z,table in good})==24
    assert sum(table==swap_table(table) for z,table in good)==7
    induced=[(z,table) for z,table in good if is_induced(table)]
    assert len(induced)==25
    assert len({min(table,swap_table(table)) for z,table in induced})==15
    Ts=[(z,table) for z,table in good if is_T(table)]
    Fs=[(z,table) for z,table in good if is_F(table)]
    assert len(Ts)==4 and len(Fs)==2
    assert len({min(table,swap_table(table)) for z,table in Ts})==3
    assert len({min(table,swap_table(table)) for z,table in Fs})==2
    assert {(z[1],z[3]) for z,table in Ts}=={(0,0),(0,1),(2,0),(2,1)}
    assert {(z[1],z[3]) for z,table in Fs}=={(0,0),(2,1)}
    assert len([1 for z,tab in Ts if not is_F(tab)])==2
    assert all(le(table[a][0],table[0][0]) for z,table in good for a in ATOMS)
    witness_T_not_F=next(tab for z,tab in Ts if z[1]==0 and z[3]==1)
    assert not is_F(witness_T_not_F)
    witness_F_not_Heyting=next(tab for z,tab in Fs if z[1]==z[3]==0)
    assert not le(2,witness_F_not_Heyting[1][2])
    print('P1--P4 normal-form candidates:',len(all_candidates))
    print('K-preconditionals by P1--P5:',len(good),'isomorphism classes: 24')
    print('K-preconditionals split by bottom-row value:',dict(Counter(z[0] for z,tab in good)))
    print('Precomplementation-induced:',len(induced),'isomorphism classes: 15')
    print('Not precomplementation-induced:',len(good)-len(induced),'isomorphism classes: 9')
    print('T-algebra operations:',len(Ts),'isomorphism classes: 3')
    print('F-algebra operations:',len(Fs),'isomorphism classes: 2')
    print('T but not F:',len(Ts)-len(Fs))
    print('Symbolic P5 criteria match direct P1--P5 checking on all 144 candidates.')
    print('PASS')


if __name__ == '__main__':
    collect()
