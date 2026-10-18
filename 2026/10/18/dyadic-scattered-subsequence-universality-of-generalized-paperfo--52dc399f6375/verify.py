#!/usr/bin/env python3
"""Independent finite checks for dyadic subsequence universality in paperfolding words."""

from itertools import product
from random import Random


def bits_by_valuation(directions, k):
    """Produce the first 2**k bits from the valuation formula."""
    out = []
    for t in range(1, 1 << k):
        v = (t & -t).bit_length() - 1
        odd = t >> v
        out.append(((odd - 1) // 2 & 1) ^ directions[v])
    out.append(directions[k])
    return out


def bits_by_folds(directions, k):
    """Independently form P_{d_0...d_{k-1}} then append d_k."""
    out = []
    for d in directions[:k]:
        out = out + [d] + [1 - b for b in out[::-1]]
    return out + [directions[k]]


def arch_count(bits):
    state = None
    count = 0
    for b in bits:
        if state is None:
            state = b
        elif state != b:
            state = None
            count += 1
    return count


def formula(directions, k):
    return 3 * (1 << (k-3)) - int(directions[0] == directions[1] != directions[k])


def verify_local_blocks():
    """Check the 8-block transition table for all binary boundary choices."""
    table = {}
    for a, b, x, y in product((0, 1), repeat=4):
        block = [a, b, 1-a, x, a, 1-b, 1-a, y]
        for start in (None, 0, 1):
            state, count = start, 0
            for bit in block:
                if state is None:
                    state = bit
                elif state != bit:
                    state = None
                    count += 1
            table[(a,b,x,y,start)] = (count,state)
    for a, b, x, y in product((0,1), repeat=4):
        if a != b:
            for start in (None,0,1):
                assert table[(a,b,x,y,start)] == (3,y)
        else:
            # Reachable incoming states: empty, or the bit opposite a.
            assert table[(a,b,x,y,None)] == (3-int(y!=a), None if y==a else y)
            assert table[(a,b,x,y,1-a)] == (4-int(y!=a), None if y==a else y)
    return len(table)


def verify_small_subsequences():
    """Exhaustive direct subsequence-set test, independent of arch theory."""
    for k in (3,4):
        for d in product((0,1), repeat=k+1):
            word = bits_by_folds(d,k)
            expected = formula(d,k)
            for ell in (expected,expected+1):
                reachable = {()}
                for b in word:
                    reachable |= {u+(b,) for u in reachable if len(u)<ell}
                found = sum(len(u)==ell for u in reachable)
                assert (found == (1<<ell)) == (ell == expected)


def run():
    print('local_block_transition_cases', verify_local_blocks())
    verify_small_subsequences()
    print('direct_scattered_subsequence_tests', 'OK')
    checks = 0
    for k in range(3,11):
        for d in product((0,1), repeat=k+1):
            direct = bits_by_valuation(d,k)
            alternate = bits_by_folds(d,k)
            assert direct == alternate
            assert arch_count(direct) == formula(d,k), (k,d)
            checks += 1
        print('all_instruction_words_at_k',k,1<<(k+1))
    rng = Random(70253)
    for k,samples in ((11,64),(13,64),(16,32),(19,12)):
        for _ in range(samples):
            d = [rng.randrange(2) for _ in range(k+1)]
            direct = bits_by_valuation(d,k)
            assert direct == bits_by_folds(d,k)
            assert arch_count(direct) == formula(d,k)
            checks += 1
        print('random_instruction_words_at_k',k,samples)
    print('instruction_words_checked',checks)
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
