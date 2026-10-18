#!/usr/bin/env python3
"""Standalone finite verification for a ternary negative-orientable order-three theorem.

Finite enumerations provide reproducible checks, not the infinite proof.
"""
from itertools import product
from collections import Counter

Q = range(3)

def twist(t):
    return tuple((-x) % 3 for x in reversed(t))

def canon(t):
    return min(t, twist(t))

def orbits():
    classes = {}
    for t in product(Q, repeat=3):
        if t != twist(t):
            classes.setdefault(canon(t), set()).add(t)
    return classes

F = ((0,0),(1,2),(2,1))
T = {(0,2),(1,0)}

def fixed_signature(t):
    v, w = t[:2], t[1:]
    return ''.join(str((int(v == f) + int(w == f)) % 2) for f in F)

def crosses_cut(t):
    return int((t[:2] in T) != (t[1:] in T))

def is_negative_orientable(word):
    m = len(word)
    classes = []
    for i in range(m):
        t = (word[i],word[(i+1)%m],word[(i+2)%m])
        if t == twist(t):
            return False
        classes.append(canon(t))
    return len(set(classes)) == m

c = orbits()
assert len(c) == 12 and all(len(v) == 2 for v in c.values())
assert {t for t in product(Q, repeat=3) if t == twist(t)} == {(0,0,0),(1,0,2),(2,0,1)}
for t in c:
    for v in c[t]:
        assert fixed_signature(v) == fixed_signature(t)
        assert crosses_cut(v) == crosses_cut(t)
print('TWISTED_ORBITS 12')
print('FIXED_VERTICES', F, 'INVARIANT_CUT', sorted(T))
print('representative signature crossing')
for rep in sorted(c):
    print(''.join(map(str,rep)), fixed_signature(rep), crosses_cut(rep))

sig_total = ''.join(str(sum(int(fixed_signature(t)[j]) for t in c) % 2) for j in range(3))
cut_total = sum(crosses_cut(t) for t in c)
assert sig_total == '011' and cut_total == 5
missing = [t for t in c if fixed_signature(t) == sig_total]
assert missing == [(1,2,1)] and crosses_cut(missing[0]) == 0
print('ALL_12_PARITY', sig_total, 'ALL_12_CUT_CROSSINGS', cut_total)
print('ONLY_11_POSSIBLE_OMISSION', ''.join(map(str,missing[0])))
print('REMAINING_11_CUT_CROSSINGS', cut_total - crosses_cut(missing[0]))

w = tuple(map(int, '0100112111'))
assert is_negative_orientable(w)
print('WITNESS', ''.join(map(str,w)), 'LENGTH', len(w), 'TWIST_CLASSES', len(set(canon((w[i],w[(i+1)%10],w[(i+2)%10])) for i in range(10))))

# Independent brute force not using orbit parity signatures, checking each cyclic word.
for n in (10,11,12):
    count = sum(map(is_negative_orientable, product(Q, repeat=n)))
    if n == 10:
        assert count > 0
    else:
        assert count == 0
    print('BRUTE_PERIOD', n, 'TESTED', 3**n, 'ADMISSIBLE_LABELED', count)
print('CHECK_OK')
