"""Reconstruct exact pentagon orientation-intersection automaton certificates.

Python 3 standard library only. All orientations, reachable subset states,
Myhill-Nerode refinement, quotient transitions and formal series are checked.
"""

from itertools import product

N = 5
FULL = (1 << N) - 1

EXPECTED_DFA = [
    (1, 2), (3, 2), (1, 4), (5, 6), (7, 5), (5, 5),
    (8, 4), (3, 9), (5, 10), (11, 5), (12, 4), (3, 13),
    (14, 10), (11, 15), (5, 16), (17, 5), (14, 4), (3, 15),
]
EXPECTED_DEAD = 5
EXPECTED_SERIES = [
    1, 2, 4, 6, 10, 14, 22, 32, 50, 74, 114, 170,
    258, 386, 580, 870, 1300, 1954,
]
# P(z)=(1+z)(1-z^2+z^7), Q(z)=(1-z)(1-3z^2+2z^4-z^7).
P = [1, 1, -1, -1, 0, 0, 0, 1, 1]
Q = [1, -1, -3, 3, 2, -2, 0, -1, 1]


def transition_tables(n, orientation):
    """For every edge i--(i+1 mod n), choose the forward label bit.

    Traversal in the reverse direction has the complementary label.
    States are vertices, and all vertices are initially and finally allowed.
    """
    step = [[0, 0] for _ in range(n)]
    for i in range(n):
        j = (i + 1) % n
        bit = (orientation >> i) & 1
        step[i][bit] |= 1 << j
        step[j][1-bit] |= 1 << i
    tables = []
    for letter in (0, 1):
        t = [0] * (1 << n)
        for subset in range(1, 1 << n):
            bit = subset & -subset
            index = bit.bit_length() - 1
            t[subset] = t[subset ^ bit] | step[index][letter]
        tables.append(tuple(t))
    return tuple(tables)


def product_automaton(n):
    tabs = [transition_tables(n, mask) for mask in range(1 << n)]
    initial = tuple([(1 << n) - 1] * (1 << n))
    visited = {initial: 0}
    states = [initial]
    moves = []
    for state in states:
        row = []
        for letter in (0, 1):
            nxt = tuple(t[letter][s] for t, s in zip(tabs, state))
            if 0 in nxt:
                row.append(-1)
            else:
                if nxt not in visited:
                    visited[nxt] = len(states)
                    states.append(nxt)
                row.append(visited[nxt])
        moves.append(tuple(row))
    # -1 is a single absorbing state, representing failure of at least one orientation.
    dead = len(states)
    moves = [tuple(dead if x == -1 else x for x in row) for row in moves]
    moves.append((dead, dead))
    accepting = [True] * dead + [False]
    return states, moves, accepting


def minimize(moves, accepting):
    color = [int(a) for a in accepting]
    history = []
    while True:
        signatures = [
            (color[i], color[row[0]], color[row[1]])
            for i, row in enumerate(moves)
        ]
        names = {s: i for i, s in enumerate(sorted(set(signatures)))}
        refined = [names[s] for s in signatures]
        if refined == color:
            break
        assert len(set(refined)) > len(set(color))
        color = refined
        history.append(len(set(color)))
    assert len(set(color)) == len(set(tuple((color[i], color[a], color[b])) for i, (a, b) in enumerate(moves)))
    # All states that share a final color have the same acceptance and successors.
    for i in range(len(color)):
        for j in range(i):
            if color[i] == color[j]:
                assert accepting[i] == accepting[j]
                assert all(color[moves[i][k]] == color[moves[j][k]] for k in (0, 1))
    reps = {v: color.index(v) for v in set(color)}
    order = [color[0]]
    idx = {color[0]: 0}
    reduced, final = [], []
    for c in order:
        source = reps[c]
        row = []
        for k in (0, 1):
            d = color[moves[source][k]]
            if d not in idx:
                idx[d] = len(order)
                order.append(d)
            row.append(idx[d])
        reduced.append(tuple(row))
        final.append(accepting[source])
    assert len(order) == len(set(color)), 'all quotient states must be reachable'
    return reduced, final, history


def count_words(moves, accepting, n):
    # v_i(k) counts accepted continuations of length k from state i.
    v = [int(flag) for flag in accepting]
    counts = []
    for _ in range(n):
        counts.append(v[0])
        v = [v[a] + v[b] for a, b in moves]
    return counts


def accepts_direct(n, mask, word):
    trans = transition_tables(n, mask)
    reachable = (1 << n) - 1
    for ch in word:
        reachable = trans[int(ch)][reachable]
    return reachable != 0


def main():
    states, moves, accepting = product_automaton(N)
    assert len(states) == 23
    assert len(moves) == 24
    reduced, finals, rounds = minimize(moves, accepting)
    assert rounds == [4, 7, 9, 11, 13, 16, 18]
    assert len(reduced) == 18
    assert reduced == EXPECTED_DFA
    assert [i for i, a in enumerate(finals) if not a] == [EXPECTED_DEAD]
    sequence = count_words(reduced, finals, 27)
    assert sequence[:18] == EXPECTED_SERIES
    # Rational identity proof: F(z)=e0^T(I-zM)^(-1)f.
    # Its denominator divides det(I-zM), degree <=18; its numerator
    # has degree <=17. Therefore QF-P has numerator degree <=26.
    # Vanishing coefficients through z^26 prove QF=P identically.
    for k in range(27):
        coeff = sum(Q[j] * sequence[k-j] for j in range(min(8, k) + 1))
        assert coeff == (P[k] if k < len(P) else 0), (k, coeff)
    # Directly compare the minimized acceptor to ALL independent
    # orientation walks for every binary word through length 12.
    for length in range(13):
        for word_tuple in product('01', repeat=length):
            word = ''.join(word_tuple)
            direct = all(accepts_direct(N, mask, word) for mask in range(32))
            state = 0
            for ch in word:
                state = reduced[state][int(ch)]
            assert direct == finals[state], word
    for w, expected_three, expected_five in [
        ('00100', True, False),
        ('11011', True, False),
    ]:
        assert all(accepts_direct(3, mask, w) for mask in range(8)) == expected_three
        assert all(accepts_direct(5, mask, w) for mask in range(32)) == expected_five
    print('orientations=32; reachable_non_sinks=23; reachable_total=24')
    print('refinement_class_counts=' + str(rounds))
    print('minimal_dfa_states=18; unique_rejecting_sink=5')
    print('count_prefix=' + str(sequence[:18]))
    print('rational_identity_coefficients=0..26 verified; numerator_degree_bound=26')
    print('direct_walk_comparison=8191 words, lengths 0..12')
    print('triangle_pentagon_distinguishers=00100,11011')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
