#!/usr/bin/env python3
"""Reproducible verification of the refuting witnesses for
Phi2: a->b, b->ca, c->d, d->a in Aut(F4).

Checks:
  1. Phi swaps the complementary rank-2 free factors A=<a,c>, B=<b,d>.
  2. Phi^2 preserves each of A, B (with explicit generation).
  3. The commutator w=[a,c] has Phi^4(w)=w (tightened) -> periodic class.
  4. Transition matrix M^2 is block-diagonal over the partition {a,c}|{b,d}.
"""
inv = {'a': 'A', 'A': 'a', 'b': 'B', 'B': 'b',
       'c': 'C', 'C': 'c', 'd': 'D', 'D': 'd'}
Phi = {'a': 'b', 'b': 'ca', 'c': 'd', 'd': 'a'}
for x in ['A', 'B', 'C', 'D']:
    Phi[x] = ''.join(inv[c] for c in reversed(Phi[inv[x]]))


def apply_phi(w):
    return ''.join(Phi[ch] for ch in w)


def tight(w):
    st = []
    for ch in w:
        if st and st[-1] == inv[ch]:
            st.pop()
        else:
            st.append(ch)
    return ''.join(st)


def phi_pow(w, k):
    for _ in range(k):
        w = tight(apply_phi(w))
    return w


# 1. Swap at generator level (all positive words, no cancellation).
assert phi_pow('a', 1) == 'b', phi_pow('a', 1)
assert phi_pow('c', 1) == 'd', phi_pow('c', 1)
assert phi_pow('b', 1) == 'ca', phi_pow('b', 1)
assert phi_pow('d', 1) == 'a', phi_pow('d', 1)
# <ca,a> = <a,c> since (ca)a^{-1} = c; <db,b> = <b,d> since (db)b^{-1} = d.
assert tight('caA') == 'c'
assert tight('dbB') == 'd'
print('1. swap Phi(<a,c>)=<b,d>, Phi(<b,d>)=<a,c>: OK')

# 2. Phi^2 preserves each factor (positive words again).
assert phi_pow('a', 2) == 'ca', phi_pow('a', 2)
assert phi_pow('c', 2) == 'a', phi_pow('c', 2)
assert phi_pow('b', 2) == 'db', phi_pow('b', 2)
assert phi_pow('d', 2) == 'b', phi_pow('d', 2)
print('2. Phi^2 fixes <a,c> and <b,d> setwise: OK')

# 3. Commutator orbit closes up after 4 steps.
w = 'acAC'
orb = [phi_pow(w, k) for k in range(1, 5)]
assert orb[0] == 'bdBD', orb
assert orb[1] == 'caCA', orb
assert orb[2] == 'dbDB', orb
assert orb[3] == w, orb
assert tight(w) == w and w != ''
print('3. Phi-orbit of [a,c]: acAC -> bdBD -> caCA -> dbDB -> acAC: OK')

# 4. Transition matrix certificate. Rows = images, order a,b,c,d.
M = [[0, 1, 0, 0],
     [1, 0, 1, 0],
     [0, 0, 0, 1],
     [1, 0, 0, 0]]


def mat_mul(X, Y):
    return [[sum(X[i][k] * Y[k][j] for k in range(4))
             for j in range(4)] for i in range(4)]


M2 = mat_mul(M, M)
assert M2 == [[1, 0, 1, 0],
              [0, 1, 0, 1],
              [1, 0, 0, 0],
              [0, 1, 0, 0]], M2
# Reorder to (a,c,b,d): must be block-diagonal with [[1,1],[1,0]] blocks.
perm = [0, 2, 1, 3]
R = [[M2[i][j] for j in perm] for i in perm]
assert R == [[1, 1, 0, 0],
             [1, 0, 0, 0],
             [0, 0, 1, 1],
             [0, 0, 1, 0]], R
print('4. M^2 block-diagonal over {a,c}|{b,d}: OK')

# 5. Phi is an automorphism with explicit inverse
# Psi: a->d, b->a, c->bD, d->c.
Psi = {'a': 'd', 'b': 'a', 'c': 'bD', 'd': 'c'}
for x in ['A', 'B', 'C', 'D']:
    Psi[x] = ''.join(inv[c] for c in reversed(Psi[inv[x]]))


def apply_psi(w):
    return ''.join(Psi[ch] for ch in w)


for g in ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']:
    assert tight(apply_psi(apply_phi(g))) == g, g
    assert tight(apply_phi(apply_psi(g))) == g, g
print('5. two-sided inverse a->d,b->a,c->bD,d->c: OK')

print('ALL CHECKS PASSED')
