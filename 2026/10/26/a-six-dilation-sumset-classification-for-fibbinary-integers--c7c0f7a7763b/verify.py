#!/usr/bin/env python3
"""Finite-state certificate for six fibbinary dilated sumsets.

Pure Python standard library. Run: python3 verify.py
Use --write-certificate PATH to write the complete reachable product-state table.
"""

from collections import deque
import sys


def missing_next(d, state, bit):
    """DFA for exceptional binary words, least-significant bit first."""
    dead = 99
    if d in (1, 2, 3):
        return 0
    if d == 4:
        table = {0: (2, 1), 1: (2, 3), 2: (2, 2), 3: (3, 3)}
        return table[state][bit]
    if d == 5:
        table = {0: {1: 1}, 1: {1: 2}}
        return table.get(state, {}).get(bit, dead)
    if d == 6:
        table = {0: {1: 1}, 1: {1: 2}, 2: {0: 3},
                 3: {0: 4}, 4: {1: 5}, 5: {0: 6}, 6: {1: 5}}
        return table.get(state, {}).get(bit, dead)
    raise ValueError('d must be between 1 and 6')


def missing_accept(d, state):
    return (d == 4 and state == 3 or
            d == 5 and state == 2 or
            d == 6 and state in (2, 5))


def next_representations(d, states, bit):
    """One binary column of a+db=n, recording previous summand bits and carry."""
    result = set()
    for previous_a, previous_b, carry in states:
        assert 0 <= carry <= d
        for a in (0, 1):
            if a and previous_a:
                continue
            for b in (0, 1):
                if b and previous_b:
                    continue
                z = a + d * b + carry
                if z % 2 == bit:
                    new_carry = z // 2
                    assert 0 <= new_carry <= d
                    result.add((a, b, new_carry))
    return frozenset(result)


def represented(states):
    return any(carry == 0 for _, _, carry in states)


def enumerate_product(d):
    root = (frozenset(((0, 0, 0),)), 0)
    seen = {root: 0}
    order = [root]
    edges = []
    i = 0
    while i < len(order):
        summands, target = order[i]
        successors = []
        for bit in (0, 1):
            nxt = (next_representations(d, summands, bit),
                   missing_next(d, target, bit))
            if nxt not in seen:
                seen[nxt] = len(order)
                order.append(nxt)
            successors.append(seen[nxt])
            if bit == 1:
                # All binary numerals for n>0 end in 1 when read LSB-first.
                assert represented(nxt[0]) != missing_accept(d, nxt[1]), (d, i)
        edges.append(tuple(successors))
        i += 1
    # Unique canonical zero representation is the single digit '0'.
    zero = next_representations(d, root[0], 0)
    assert represented(zero) and not missing_accept(d, missing_next(d, 0, 0))
    return order, edges


def certificate():
    result = []
    for d in range(1, 7):
        order, edges = enumerate_product(d)
        result.append('d=%d states=%d' % (d, len(order)))
        result.append('id | target | representation_subset | transition_0 | transition_1 | R | E')
        for idx, ((states, target), (u, v)) in enumerate(zip(order, edges)):
            subset = ','.join('%d%d:%d' % (pa, pb, c) for pa, pb, c in sorted(states))
            result.append('%d | %d | {%s} | %d | %d | %d | %d' %
                          (idx, target, subset, u, v,
                           int(represented(states)), int(missing_accept(d, target))))
        result.append('')
    return '\n'.join(result) + '\n'


def direct_test():
    bound = 10000
    fib = [n for n in range(bound + 1) if not (n & (n >> 1))]
    for d in range(1, 7):
        attainable = bytearray(bound + 1)
        for b in fib:
            if d * b > bound:
                break
            for a in fib:
                t = a + d * b
                if t > bound:
                    break
                attainable[t] = 1
        missing6 = set()
        k = 2
        while (4**k - 7)//3 <= bound:
            missing6.add((4**k - 7)//3)
            k += 1
        for n in range(bound + 1):
            predicted = (False if d in (1, 2, 3) else
                         n % 4 == 3 if d == 4 else
                         n == 3 if d == 5 else n in missing6)
            assert (not attainable[n]) == predicted, (d, n)
    return bound


def main():
    out = certificate()
    if len(sys.argv) == 3 and sys.argv[1] == '--write-certificate':
        with open(sys.argv[2], 'w', encoding='utf-8', newline='\n') as handle:
            handle.write(out)
    else:
        assert len(sys.argv) == 1, 'Usage: python3 verify.py [--write-certificate PATH]'
    for d in range(1, 7):
        order, edges = enumerate_product(d)
        print('PASS multiplier=%d reachable_states=%d' % (d, len(order)))
    print('PASS independent enumeration through %d' % direct_test())
    print('PASS all canonical binary inputs by exact exhaustive finite-state comparison')


if __name__ == '__main__':
    main()
