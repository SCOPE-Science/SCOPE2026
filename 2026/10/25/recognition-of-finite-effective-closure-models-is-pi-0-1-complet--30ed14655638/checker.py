"""Finite diagnostic tests for a one-world effective closure construction.

Proof of the universal computability statement is mathematical, not experimental.
"""
from itertools import product

# Atoms are ('p', index); other constructors are ('not', f),
# ('imp', f, g), ('box', f), and ('top',).
TOP = ('top',)
BOT = ('not', TOP)

def atom(i): return ('p', i)
def neg(a): return ('not', a)
def imp(a, b): return ('imp', a, b)
def box(a): return ('box', a)
def conj(a, b): return neg(imp(a, neg(b)))

def vars_in(f):
    if f[0] == 'p': return {f[1]}
    if f[0] == 'top': return set()
    if f[0] in ('not', 'box'): return vars_in(f[1])
    return vars_in(f[1]) | vars_in(f[2])

def truth(f, true_atoms, halt_after):
    op = f[0]
    if op == 'top': return True
    if op == 'p': return f[1] in true_atoms
    if op == 'not': return not truth(f[1], true_atoms, halt_after)
    if op == 'imp': return not truth(f[1], true_atoms, halt_after) or truth(f[2], true_atoms, halt_after)
    if op == 'box': return in_H(f[1], halt_after)
    raise ValueError(op)

def in_H(f, halt_after):
    # This finite implementation models programs with prescribed halting stage,
    # or a program that loops forever. Every queried formula sees finitely many
    # atomic indices; all unseen singleton variations act as the zero valuation.
    if not truth(f, frozenset(), halt_after): return False
    for i in vars_in(f):
        if halt_after is not None and i >= halt_after:
            if not truth(f, frozenset({i}), halt_after): return False
    return True

def kripke_truth(f, true_atoms, loop):
    op = f[0]
    if op == 'top': return True
    if op == 'p': return f[1] in true_atoms
    if op == 'not': return not kripke_truth(f[1], true_atoms, loop)
    if op == 'imp': return not kripke_truth(f[1], true_atoms, loop) or kripke_truth(f[2], true_atoms, loop)
    if op == 'box': return not loop or kripke_truth(f[1], true_atoms, loop)
    raise ValueError(op)

def check():
    fs = [TOP, BOT] + [atom(i) for i in range(4)]
    fs += [neg(atom(i)) for i in range(4)]
    fs += [box(atom(i)) for i in range(4)]
    fs += [box(neg(atom(i))) for i in range(4)]
    fs += [imp(atom(i), atom(j)) for i in range(4) for j in range(4)]
    fs += [conj(atom(i), atom(j)) for i in range(4) for j in range(4)]
    fs += [box(box(atom(i))) for i in range(4)]
    checks = 0
    for halt_stage in [None, 0, 1, 2, 4]:
        for f in fs:
            value = in_H(f, halt_stage)
            alternatives = [frozenset()]
            if halt_stage is not None:
                alternatives += [frozenset({i}) for i in vars_in(f) if i >= halt_stage]
            assert value == all(truth(f, v, halt_stage) for v in alternatives)
            assert not value or truth(f, frozenset(), halt_stage)
            checks += 2
        for a in fs:
            assert in_H(imp(a, a), halt_stage)
            for b in fs:
                A, B = in_H(a, halt_stage), in_H(b, halt_stage)
                assert in_H(conj(a,b), halt_stage) == (A and B)
                assert not (A and in_H(imp(a,b),halt_stage)) or B
                checks += 3
        for f in fs:
            # Frame validity ranges over all valuations on the one-world frame.
            if all(truth(f, frozenset(i for i,b in enumerate(bits) if b), halt_stage)
                   for bits in product([False,True],repeat=4)):
                assert in_H(f, halt_stage)
            checks += 1
        assert not in_H(BOT, halt_stage)
        if halt_stage is None:
            for f in fs:
                assert truth(f,frozenset(),halt_stage) == kripke_truth(f,frozenset(),True)
                checks += 1
        else:
            n = max(halt_stage, 1)
            witness = box(neg(atom(n)))
            assert truth(neg(atom(n)),frozenset(),halt_stage)
            assert not truth(witness,frozenset(),halt_stage)
            assert not truth(box(BOT),frozenset(),halt_stage)
            assert kripke_truth(witness,frozenset(),True)
            assert kripke_truth(box(BOT),frozenset(),False)
            checks += 5
    print(f'ALL_CHECKS_OK ({checks} finite diagnostic assertions)')

if __name__ == '__main__': check()
