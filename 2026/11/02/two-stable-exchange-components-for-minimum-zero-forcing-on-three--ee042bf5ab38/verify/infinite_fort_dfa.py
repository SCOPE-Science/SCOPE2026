#!/usr/bin/env python3
"""Exact finite-automaton certificate for zero forcing on P_3 square P_n.

No external packages. The exhaustive search is over a finite set of automaton
states for arbitrary word lengths, not a bounded list of rectangular grids.
"""
from collections import Counter, deque

TEMPLATES = (
    (0, 3, 1), (0, 6, 4), (1, 1, 1), (1, 3, 0),
    (3, 0, 1), (3, 2, 0), (4, 4, 4), (4, 6, 0),
    (5, 1, 0), (5, 4, 0), (6, 0, 4), (6, 2, 0),
    (7, 0, 0),
)
assert len(TEMPLATES) == 13
assert all(sum(mask.bit_count() for mask in p) == 3 for p in TEMPLATES)


def valid(a, b, c):
    """Fort condition in the middle column b; a,c its neighbors."""
    for r in range(3):
        if (b >> r) & 1:
            continue
        q = ((a >> r) & 1) + ((c >> r) & 1)
        if r > 0: q += (b >> (r - 1)) & 1
        if r < 2: q += (b >> (r + 1)) & 1
        if q == 1:
            return False
    return True


def state_id(a, b, z):
    return 16 * a + 2 * b + int(bool(z))

# Nondeterministic state (a,b,z) stores the last two candidate fort masks
# and whether any examined fort mask has a nonzero bit.
FORT_T = [[0] * 8 for _ in range(128)]
for a in range(8):
    for b in range(8):
        for z in range(2):
            i = state_id(a, b, z)
            for s in range(8):
                dst = 0
                for c in range(8):
                    if not (c & s) and valid(a, b, c):
                        dst |= 1 << state_id(b, c, z or c != 0)
                FORT_T[i][s] = dst

FIRST = []
for s in range(8):
    dst = 0
    for c in range(8):
        if not (c & s):
            dst |= 1 << state_id(0, c, c != 0)
    FIRST.append(dst)


def fort_next(st, symbol):
    dst = 0
    while st:
        bit = st & -st
        dst |= FORT_T[bit.bit_length() - 1][symbol]
        st ^= bit
    return dst


def has_fort(st):
    while st:
        bit = st & -st
        i = bit.bit_length() - 1
        a, b, z = i // 16, (i // 2) % 8, i % 2
        if z and valid(a, b, 0):
            return True
        st ^= bit
    return False

# An independent NFA recognizes the explicit union of pattern languages:
#     p[0],p[1],p[2],0,0,...  or  0,0,...,p[2],p[1],p[0]
# for one of the thirteen p above. Its accepted words are restricted later
# to length at least five and total Hamming weight exactly three.
NFA_STATES = []
for i in range(13):
    for j in range(3):
        NFA_STATES.append(('L', i, j))
NFA_STATES += [('L_DONE',), ('R_WAIT',)]
for i in range(13):
    for j in range(1, 3):
        NFA_STATES.append(('R', i, j))
    NFA_STATES.append(('R_DONE', i))
NFA_INDEX = {v: k for k, v in enumerate(NFA_STATES)}
NFA_START = (1 << NFA_INDEX[('R_WAIT',)]) | sum(
    1 << NFA_INDEX[('L', i, 0)] for i in range(13)
)
NFA_FINAL = (1 << NFA_INDEX[('L_DONE',)]) | sum(
    1 << NFA_INDEX[('R_DONE', i)] for i in range(13)
)
NFA_T = [[0] * 8 for _ in NFA_STATES]
for k, node in enumerate(NFA_STATES):
    for s in range(8):
        dst = 0
        if node[0] == 'L':
            _, i, j = node
            if s == TEMPLATES[i][j]:
                dest = ('L', i, j + 1) if j < 2 else ('L_DONE',)
                dst |= 1 << NFA_INDEX[dest]
        elif node[0] == 'L_DONE':
            if s == 0:
                dst |= 1 << k
        elif node[0] == 'R_WAIT':
            if s == 0:
                dst |= 1 << k
            for i in range(13):
                if s == TEMPLATES[i][2]:
                    dst |= 1 << NFA_INDEX[('R', i, 1)]
        elif node[0] == 'R':
            _, i, j = node
            if s == TEMPLATES[i][2 - j]:
                dest = ('R', i, j + 1) if j < 2 else ('R_DONE', i)
                dst |= 1 << NFA_INDEX[dest]
        NFA_T[k][s] = dst


def nfa_next(st, s):
    dst = 0
    while st:
        bit = st & -st
        dst |= NFA_T[bit.bit_length() - 1][s]
        st ^= bit
    return dst


def prove_all_lengths():
    # Length coordinate is saturated at five. The state space is finite,
    # so this BFS checks infinitely many input lengths by exact closure.
    initial = (None, NFA_START, 0, 0)
    seen = {initial}
    queue = deque([initial])
    while queue:
        F, N, budget, length = queue.popleft()
        if budget == 3 and length == 5:
            predicted = bool(N & NFA_FINAL)
            actual = not has_fort(F)
            assert actual == predicted, (F, N, budget, length)
        for s in range(8):
            newbudget = budget + s.bit_count()
            if newbudget > 3:
                continue
            F2 = FIRST[s] if F is None else fort_next(F, s)
            N2 = nfa_next(N, s)
            nxt = (F2, N2, newbudget, min(5, length + 1))
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    assert len(seen) == 926, len(seen)

    # Similarly, every initial set of size at most two fails to force.
    # Only length >= 3 is needed here; length is saturated at three.
    states = set()
    queue = deque()
    for s in range(8):
        if s.bit_count() <= 2:
            state = (FIRST[s], s.bit_count(), 1)
            if state not in states:
                states.add(state)
                queue.append(state)
    while queue:
        F, budget, length = queue.popleft()
        if length == 3:
            assert has_fort(F), (budget, length)
        for s in range(8):
            b2 = budget + s.bit_count()
            if b2 > 2:
                continue
            nxt = (fort_next(F, s), b2, min(3, length + 1))
            if nxt not in states:
                states.add(nxt)
                queue.append(nxt)
    assert len(states) == 245, len(states)
    print('FORT_AUTOMATON_ALL_LENGTHS_PASS')
    print('LANGUAGE_PRODUCT_STATES', len(seen))
    print('LOWER_BOUND_STATES', len(states))

if __name__ == '__main__':
    prove_all_lengths()
