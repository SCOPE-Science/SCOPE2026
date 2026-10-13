#!/usr/bin/env python3
"""Exact finite checks for the periodic base-power kernel-rank theorem.

No source data or external dependencies are required. The infinite theorem is
proved separately; this script checks constructive witnesses and small censuses.
"""
from collections import Counter


def least_period(word):
    n = len(word)
    for d in range(1, n + 1):
        if n % d == 0 and all(word[i] == word[i % d] for i in range(n)):
            return d
    raise AssertionError('unreachable')


def kernel_rank(word, base):
    n = len(word)
    assert least_period(word) == n
    states = set()
    step = 1
    while step <= n:
        for residue in range(step):
            word_at_level = tuple(word[i] for i in range(residue, n, step))
            d = least_period(word_at_level)
            states.add(word_at_level[:d])
        step *= base
    return len(states)


def build_witnesses(base, power):
    assert base >= 2 and power >= 1
    if power == 1:
        return {rank: tuple(list(range(1, rank-1)) + [0] * (base - (rank - 2)))
                for rank in range(3, base + 2)}
    if (base, power) == (2, 2):
        return {4: (0, 0, 0, 1), 5: (0, 1, 0, 2),
                6: (0, 0, 1, 2), 7: (0, 1, 2, 3)}
    prev = build_witnesses(base, power-1)
    low, upper = power+1, sum(base**i for i in range(power))
    assert set(prev) == set(range(low, upper+1))
    result = {}
    def assemble(ranks, unshare=0):
        childs = []
        unique_color = 1
        for r in ranks:
            seq = prev[r]
            nonzero = sorted(set(seq)-{0})
            mapping = {0: 0}
            for old in nonzero:
                mapping[old] = unique_color
                unique_color += 1
            childs.append([mapping[x] for x in seq])
        for c in range(unshare):
            child = childs[c]
            child[child.index(0)] = unique_color
            unique_color += 1
        childs += [[0]*(base**(power-1)) for _ in range(base-len(childs))]
        return tuple(childs[j][i] for i in range(base**(power-1)) for j in range(base))

    for m in range(1, base+1):
        lo, hi = 2+m*power, 2+m*(upper-1)
        for target in range(lo,hi+1):
            surplus = (target-2) - m*power
            ranks = []
            for _ in range(m):
                extra = min(surplus, upper-low)
                ranks.append(low+extra)
                surplus -= extra
            assert surplus == 0
            result[target] = assemble(ranks)
    top_start = 2+base*(upper-1)
    for extra in range(1,base):
        result[top_start+extra] = assemble([upper]*base, unshare=extra)
    assert set(result)==set(range(power+2, sum(base**i for i in range(power+1))+1))
    return result


def restricted_partitions(n):
    word=[0]*n
    def rec(i,largest):
        if i==n:
            yield tuple(word)
        else:
            for symbol in range(largest+2):
                word[i]=symbol
                yield from rec(i+1,max(largest,symbol))
    yield from rec(1,0)


def main():
    checked_witnesses=0
    for base,power in ((2,1),(2,2),(2,3),(2,4),(2,5),
                       (3,1),(3,2),(3,3),(4,1),(4,2)):
        witnesses=build_witnesses(base,power)
        n=base**power
        for expected,word in witnesses.items():
            assert len(word)==n
            assert least_period(word)==n
            actual=kernel_rank(word,base)
            assert actual==expected,(base,power,expected,actual,word)
            checked_witnesses+=1
    checked_census=0
    for base,power in ((2,1),(2,2),(2,3),(3,1),(3,2)):
        n=base**power
        histogram=Counter()
        for word in restricted_partitions(n):
            if least_period(word)==n:
                histogram[kernel_rank(word,base)]+=1
                checked_census+=1
        want=set(range(power+2, sum(base**i for i in range(power+1))+1))
        assert set(histogram)==want,(base,power,histogram)
    print('VERIFY_OK constructed_witnesses=%d primitive_partition_census=%d'%
          (checked_witnesses,checked_census))

if __name__=='__main__':
    main()
