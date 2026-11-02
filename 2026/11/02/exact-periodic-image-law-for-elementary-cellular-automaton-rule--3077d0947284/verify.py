#!/usr/bin/env python3
"""Replay the finite exact image-enumeration certificate for cyclic Rule 30.

Only Python's standard library is required. See RESULT.md for the proof
that the finite coefficient identity certifies the infinite generating function.
"""
import json
from pathlib import Path


def compose_after(s, t):
    return tuple(s[t[i]] for i in range(4))


def monoid():
    pairs = [(i >> 1, i & 1) for i in range(4)]
    T = [tuple((2 * (v ^ (a | b)) + a) for a, b in pairs)
         for v in range(2)]
    assert T == [(0, 2, 3, 3), (2, 0, 1, 1)]
    states = [(0, 1, 2, 3)]
    ids = {states[0]: 0}
    trans = []
    for state in states:
        row = []
        for t in T:
            new = compose_after(state, t)
            if new not in ids:
                ids[new] = len(states)
                states.append(new)
            row.append(ids[new])
        trans.append(row)
    accepting = [int(any(s[i] == i for i in range(4))) for s in states]
    assert len(states) == 41 and sum(accepting) == 30
    return states, trans, accepting


def product(*factors):
    out = [1]
    for f in factors:
        nxt = [0] * (len(out) + len(f) - 1)
        for i, a in enumerate(out):
            for j, b in enumerate(f):
                nxt[i+j] += a*b
        out = nxt
    return out


def rational_coefficients(P, Q, count):
    assert Q[0] == 1
    values = []
    for n in range(count):
        c = P[n] if n < len(P) else 0
        for j in range(1, min(n, len(Q)-1)+1):
            c -= Q[j] * values[n-j]
        values.append(c)
    return values


def automaton_coefficients(trans, accepting, count):
    v = [0]*len(trans)
    v[0] = 1
    counts = []
    for _ in range(count):
        counts.append(sum(w*a for w,a in zip(v, accepting)))
        new = [0]*len(trans)
        for state, ways in enumerate(v):
            for target in trans[state]:
                new[target] += ways
        v = new
    return counts


def rule30(x,n):
    mask = (1 << n)-1
    left = ((x << 1) & mask) | (x >> (n-1))
    right = (x >> 1) | ((x & 1) << (n-1))
    return left ^ (x | right)


def brute(n):
    return len({rule30(x,n) for x in range(1<<n)})


def main():
    with open(Path(__file__).with_name('certificate.json'), encoding='utf-8') as f:
        saved = json.load(f)
    states, trans, accepting = monoid()
    P = [1,-2,2,-5,6,-1,2,-4]
    Q = product([1,-1],[1,-2],[1,1,1],[1,-1,0,-2])
    assert saved['T0'] == [0,2,3,3] and saved['T1'] == [2,0,1,1]
    assert saved['states'] == [list(s) for s in states]
    assert saved['transitions'] == trans
    assert saved['accepting'] == accepting
    assert saved['gf_numerator'] == P and saved['gf_denominator'] == Q
    assert len(P)==len(Q)==8 and Q[0]==1
    counts = automaton_coefficients(trans, accepting, 49)
    assert saved['coefficients_n0_to_48'] == counts
    assert counts == rational_coefficients(P,Q,49)
    # A 41-state automaton has H/D with deg(H)<=40 and deg(D)<=41.
    # The numerator of H/D-P/Q has degree <=48. Its first 49
    # coefficients are zero; hence the numerator is identically zero.
    assert [brute(n) for n in range(1,18)] == counts[1:18]
    assert counts[1:18] == [1,3,5,11,26,52,106,223,455,923,
                            1882,3816,7710,15571,31395,63199,127110]
    assert [(1<<n)-counts[n] for n in (8,12,16)] == [33,280,2337]
    # Published finite census: Faulkenberry (2016), Appendix A, Table 6.
    # The table is a cross-check only, not the proof for arbitrary n.
    published_orphans_1_to_27 = [
        1,1,3,5,6,12,22,33,57,101,166,280,482,813,1373,
        2337,3962,6708,11382,19305,32721,55485,94094,
        159536,270506,458693,777765]
    through_27 = automaton_coefficients(trans, accepting, 28)
    assert [2**n-through_27[n] for n in range(1,28)] == published_orphans_1_to_27
    print('VERIFY_OK: 41 transformations; 49 exact coefficients; independent rings 1..17; external 2016 census 1..27')


if __name__ == '__main__':
    main()
