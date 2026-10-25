#!/usr/bin/env python3
"""Exact small matching checks for coloured cycle motif factorial moments.

No asymptotic theorem is inferred from finite enumeration.
"""
from fractions import Fraction
from itertools import product
from math import prod


def matchings(vertices):
    if not vertices:
        yield ()
        return
    first = vertices[0]
    for j in range(1, len(vertices)):
        mate = vertices[j]
        rest = vertices[1:j] + vertices[j+1:]
        for tail in matchings(rest):
            yield ((first, mate),) + tail


def chord_sets(n, lengths=(1, 2, 3)):
    return [tuple(frozenset((i, (i + d) % n)) for i in range(n)) for d in lengths]


def factorial(v, k):
    return prod(v - j for j in range(k))


def match_probability(n, k):
    return Fraction(1, prod(n - (2*j + 1) for j in range(k)))


def prescribed_moment(n, chords, powers):
    groups = []
    for candidates, k in zip(chords, powers):
        if not k:
            groups.append(((),))
        elif k == 1:
            groups.append(tuple((x,) for x in candidates))
        elif k == 2:
            groups.append(tuple((x, y) for x in candidates for y in candidates if x != y))
        else:
            raise ValueError('Designed for moment orders <=2 per type')
    viable = 0
    for selected in product(*groups):
        chosen = [e for group in selected for e in group]
        if len(set().union(*chosen)) == 2 * len(chosen):
            viable += 1
    return viable * match_probability(n, sum(powers))


def main():
    tests = 0
    total = 0
    powers_list = [(1,0,0),(0,1,0),(0,0,1),(2,0,0),(0,2,0),
                   (0,0,2),(1,1,0),(1,0,1),(0,1,1),(1,1,1),(2,1,0)]
    for n in (8, 10, 12):
        chords = chord_sets(n)
        sums = {p:0 for p in powers_list}
        parallel = crossed = 0
        count = 0
        for matching in matchings(tuple(range(n))):
            count += 1
            edge_set = {frozenset(pair) for pair in matching}
            mate = {}
            for i,j in matching:
                mate[i] = j; mate[j] = i
            vals = [sum(1 for e in es if e in edge_set) for es in chords]
            for p in powers_list:
                sums[p] += prod(factorial(v,k) for v,k in zip(vals,p))
            for i in range(n):
                for j in range(i+1,n):
                    if len({i,(i+1)%n,j,(j+1)%n}) != 4:
                        continue
                    if mate[i] == j and mate[(i+1)%n] == (j+1)%n:
                        parallel += 1
                    if mate[i] == (j+1)%n and mate[(i+1)%n] == j:
                        crossed += 1
        total += count
        for p in powers_list:
            observed = Fraction(sums[p], count)
            predicted = prescribed_moment(n, chords, p)
            assert observed == predicted, ('moment',n,p,observed,predicted)
            tests += 1
        expected_pair = Fraction(n, 2*(n-1))
        assert Fraction(parallel, count) == expected_pair
        assert Fraction(crossed, count) == expected_pair
        tests += 2
        assert count == prod(range(1,n,2))
    print('CHORD_SUCCESSOR_MATCHING_EXACT_OK', total, tests)


if __name__ == '__main__':
    main()
