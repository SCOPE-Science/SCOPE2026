#!/usr/bin/env python3
"""Exact finite-state identity checks for binary two-step conjugate separation.
The 12-element closure is an infinite-language proof via transition saturation.
"""
from collections import deque
from itertools import product

I = (0, 1, 2)
Z = (0, 0, 1)
O = (2, 0, 2)

def compose(g, f):
    return tuple(g[v] for v in f)

def action(word, maps=(Z, O), degree=3):
    acc = tuple(range(degree))
    for letter in word:
        acc = compose(maps[int(letter)], acc)
    return acc

def mono_graph():
    # Generate *all* transformations reachable by arbitrary binary words.
    states = [I]
    ids = {I: 0}
    edges = []
    for state in states:
        row = []
        for trans in (Z, O):
            next_state = compose(trans, state)
            if next_state not in ids:
                ids[next_state] = len(states)
                states.append(next_state)
            row.append(ids[next_state])
        edges.append(tuple(row))
    assert len(states) == 12
    assert len(edges) == 12
    A = action('01')
    commuting = {ids[x] for x in states if compose(A, x) == compose(x, A)}
    assert commuting == {0, 4, 10}
    # A 3-state DFA for (01)*: phase 0 accepts, phase 1 needs 1, phase 2 dead.
    dfa = ((1, 2), (2, 0), (2, 2))
    pending = deque([(0, 0)])
    seen = {(0, 0)}
    while pending:
        trans_state, regex_state = pending.popleft()
        assert (trans_state in commuting) == (regex_state == 0), (trans_state, regex_state)
        for bit in (0, 1):
            target = (edges[trans_state][bit], dfa[regex_state][bit])
            if target not in seen:
                seen.add(target)
                pending.append(target)
    assert len(seen) == 12
    return states, edges, commuting, len(seen)

def distinguish_in_2(w, v):
    for z in product((0, 1), repeat=2):
        for o in product((0, 1), repeat=2):
            maps = (z, o)
            fw, fv = action(w, maps, degree=2), action(v, maps, degree=2)
            if fw != fv:
                return True
    return False

def differentiate_with_3(w, v):
    # The two-letter prefix is A, the rotated remainder is B.
    A, B = w[:2], w[2:]
    assert v == B + A and w != v
    if A in ('00', '11'):
        cyc = (1, 2, 0)
        reset = (0, 0, 0)
        maps = (cyc, reset) if A == '00' else (reset, cyc)
    elif A == '01':
        maps = (Z, O)
    else:
        # Exchange binary labels in the (01) witness.
        maps = (O, Z)
    return action(w, maps) != action(v, maps)

def verify():
    states, edges, commuting, witness_count = mono_graph()
    assert states[4] == action('01')
    assert states[10] == action('0101')
    total_one = total_two = 0
    for n in range(2, 13):
        for bits in product('01', repeat=n):
            w = ''.join(bits)
            v = w[1:] + w[:1]
            if w != v:
                assert distinguish_in_2(w, v), ('one-step', w, v)
                total_one += 1
            if n > 2:
                v = w[2:] + w[:2]
                if w != v:
                    assert differentiate_with_3(w, v), ('two-step', w, v)
                    total_two += 1
    for n in range(4, 401):
        w = '0'*(n-2) + '10'
        v = w[2:] + w[:2]
        assert not distinguish_in_2(w, v)
        assert differentiate_with_3(w, v)
    print('transition_monoid_states', len(states))
    print('commuting_states', *sorted(commuting))
    print('product_DFA_reachable_states', witness_count)
    print('exact_two_symbol_commutant_language', '(01)*')
    print('nontrivial_one_shift_pairs_tested', total_one)
    print('nontrivial_two_shift_pairs_tested', total_two)
    print('two_state_lower_bound_witnesses_n', '4..400')
    print('PASS')

if __name__ == '__main__':
    verify()
