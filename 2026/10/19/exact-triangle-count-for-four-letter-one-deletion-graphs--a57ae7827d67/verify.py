#!/usr/bin/env python3
"""Exact finite-state certificate for four-letter one-deletion graph triangles.

Python 3 standard library only. No network, packages, or external files.
"""
from collections import defaultdict
from itertools import product
from math import comb

Q = 4


def pair_machine(q):
    """Determinize a finite alignment nondeterministic automaton.

    Bit 0: aligned without deletions (A).
    Bit 1: aligned after one deletion in both words (B).
    Bits 2..2+q-1: one unmatched letter from word y.
    Bits 2+q..2+2*q-1: one unmatched letter from word x.
    """
    def nfa_move(mask, a, b):
        out = 0
        if mask & 1:
            if a == b:
                out |= 1
            out |= 2  # delete both current letters
            out |= 1 << (2+b)    # delete x_a, store y_b
            out |= 1 << (2+q+a)  # delete y_b, store x_a
        if mask & 2 and a == b:
            out |= 2
        for letter in range(q):
            if mask & (1 << (2+letter)) and a == letter:
                out |= 2 | (1 << (2+b))
            if mask & (1 << (2+q+letter)) and b == letter:
                out |= 2 | (1 << (2+q+a))
        return out

    states = [1]
    index = {1: 0}
    transitions = []
    for state in states:
        row = []
        for a, b in product(range(q), repeat=2):
            nxt = nfa_move(state, a, b)
            if nxt not in index:
                index[nxt] = len(states)
                states.append(nxt)
            row.append(index[nxt])
        transitions.append(row)
    accepting = [bool(state & 3) for state in states]
    return states, transitions, accepting


def triple_machine(q, pair_trans, pair_accept):
    states = [(0, 0, 0)]
    indices = {states[0]: 0}
    transitions = []
    for state in states:
        row = []
        for x, y, z in product(range(q), repeat=3):
            nxt = (
                pair_trans[state[0]][x*q+y],
                pair_trans[state[1]][y*q+z],
                pair_trans[state[2]][z*q+x],
            )
            if nxt not in indices:
                indices[nxt] = len(states)
                states.append(nxt)
            row.append(indices[nxt])
        transitions.append(row)
    accepting = [all(pair_accept[k] for k in s) for s in states]
    return states, transitions, accepting


def counted_transitions(rows):
    out = []
    for row in rows:
        counter = defaultdict(int)
        for j in row:
            counter[j] += 1
        out.append(tuple(counter.items()))
    return out


def transfer_sequence(transitions, accepting, top):
    d = len(transitions)
    weights = counted_transitions(transitions)
    vec = [0]*d
    vec[0] = 1
    out = []
    for n in range(top+1):
        out.append(sum(v for v, ok in zip(vec, accepting) if ok))
        if n == top:
            break
        new = [0]*d
        for i, v in enumerate(vec):
            if v:
                for j, weight in weights[i]:
                    new[j] += v*weight
        vec = new
    return out


def mul(a, b):
    r = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i+j] += x*y
    return r


def annihilator(q, pow_q, pow_1):
    out = [1]
    for _ in range(pow_q):
        out = mul(out, [-q,1])
    for _ in range(pow_1):
        out = mul(out, [-1,1])
    return out


def verify_ch_recurrence(seq, dimension, coeff):
    """Cayley-Hamilton: dim(M) successive zeros of u M^n Q(M) f suffice."""
    deg = len(coeff)-1
    assert len(seq) > dimension+deg
    for n in range(1,dimension+1):
        lhs = sum(coeff[k]*seq[n+k] for k in range(deg+1))
        assert lhs == 0, ('annihilator', n, lhs)


def pair_closed(n):
    num = 4**n * (27*n*n-3*n+28)-16
    assert num%12 == 0
    return num//12


def triple_closed(n):
    num = 4**n*(405*n**3+405*n*n+446*n-2104)+1920*n*n+2176*n+2368
    assert num%48 == 0
    return num//48


def triangle_closed(n):
    num = 4**n*(405*n**3+81*n*n+482*n-2344)+1920*n*n+2176*n+2560
    assert num%288 == 0
    return num//288


def brute_counts(q, n):
    """Independent deletion-ball definition, not using either DFA."""
    words = list(product(range(q), repeat=n))
    balls = [frozenset(w[:j]+w[j+1:] for j in range(n)) for w in words]
    adjacent = [[bool(balls[i] & balls[j]) for j in range(len(words))]
                for i in range(len(words))]
    p = sum(sum(row) for row in adjacent)
    triangles = sum(adjacent[i][j] and adjacent[j][k] and adjacent[k][i]
                    for i in range(len(words))
                    for j in range(i+1, len(words))
                    for k in range(j+1, len(words)))
    return p, triangles


def main():
    pair_states, pair_trans, pair_accept = pair_machine(Q)
    triple_states, triple_trans, triple_accept = triple_machine(Q,pair_trans,pair_accept)
    assert len(pair_states) == 27 and len(triple_states) == 1549
    ppoly = annihilator(Q,3,1)
    apoly = annihilator(Q,4,3)
    p = transfer_sequence(pair_trans,pair_accept,len(pair_states)+len(ppoly)-1)
    a = transfer_sequence(triple_trans,triple_accept,len(triple_states)+len(apoly)-1)
    verify_ch_recurrence(p,len(pair_states),ppoly)
    verify_ch_recurrence(a,len(triple_states),apoly)
    assert all(p[n] == pair_closed(n) for n in range(1,len(p)))
    assert all(a[n] == triple_closed(n) for n in range(1,len(a)))
    for n in range(1,5):
        brute_p, brute_t = brute_counts(Q,n)
        assert brute_p == p[n] == pair_closed(n)
        assert brute_t == triangle_closed(n)
    for n in range(1,20):
        assert 6*triangle_closed(n) == triple_closed(n)-3*pair_closed(n)+2*Q**n
    print('VERIFIED q=4 pair DFA states=27, triple DFA states=1549')
    print('Pair recurrence:', ppoly, '; triple recurrence:', apoly)
    print('Cayley-Hamilton certificate: 27 pair zeros and 1549 triple zeros')
    print('Direct deletion-ball triangles n=1..4:',[triangle_closed(n) for n in range(1,5)])
    print('Exact closed forms checked for all transfer terms used in certificate.')


if __name__ == '__main__':
    main()
