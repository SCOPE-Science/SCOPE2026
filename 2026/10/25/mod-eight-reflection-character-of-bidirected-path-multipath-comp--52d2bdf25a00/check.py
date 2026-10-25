#!/usr/bin/env python3
"""Finite reproducibility checks for the reflection action on path multipath complexes.

Only Python's standard library is required. Here n counts undirected path edges;
a signed word encodes each edge as empty, right-oriented, or left-oriented.
"""
from collections import defaultdict
from itertools import product


def faces(n):
    for word in product((0, 1, -1), repeat=n):
        if any(word[i] and word[i+1] and word[i] != word[i+1]
               for i in range(n-1)):
            continue
        yield word


def simplices_by_size(n):
    levels = defaultdict(list)
    for w in faces(n):
        simplex = tuple(2*i + (a == -1) for i, a in enumerate(w) if a)
        if simplex:
            levels[len(simplex)].append(simplex)
    return levels


def boundary_ranks_mod2(n):
    levels = simplices_by_size(n)
    ranks = {1: 1}  # augmented boundary on zero-dimensional chains
    for k in range(2, n+1):
        low = {simplex: j for j, simplex in enumerate(levels[k-1])}
        pivots = {}
        rank = 0
        for simplex in levels[k]:
            column = 0
            for j in range(k):
                face = simplex[:j] + simplex[j+1:]
                column ^= 1 << low[face]
            while column:
                pivot = column.bit_length()-1
                if pivot in pivots:
                    column ^= pivots[pivot]
                else:
                    pivots[pivot] = column
                    rank += 1
                    break
        ranks[k] = rank
    return {k-1: len(levels[k]) - ranks.get(k,0) - ranks.get(k+1,0)
            for k in levels}


def reflection_trace(n):
    total = 0
    invariant = 0
    for word in faces(n):
        if all(word[i] == -word[n-1-i] for i in range(n)):
            invariant += 1
            pairs = sum(a != 0 for a in word)//2
            total -= (-1)**pairs
    return total, invariant


def epsilon(n):
    return -1 if n % 8 in (1, 2, 3, 4) else 1


def main():
    for n in range(1, 13):
        d = (n-1)//2
        trace, count = reflection_trace(n)
        assert trace == ((-1)**d)*epsilon(n), (n, trace)
        m = d
        left_count = sum(1 for _ in faces(m))
        assert count == left_count, (n, count, left_count)
        if n <= 9:
            betti = boundary_ranks_mod2(n)
            assert betti.get(d,0) == 1 and sum(betti.values()) == 1, (n,betti)
        print(f'n={n} dimension={d} reflection={epsilon(n):+d} '
              f'fixed_faces_including_empty={count} reduced_trace={trace:+d}')
    print('REFLECTION_CHARACTERS_OK')


if __name__ == '__main__':
    main()
