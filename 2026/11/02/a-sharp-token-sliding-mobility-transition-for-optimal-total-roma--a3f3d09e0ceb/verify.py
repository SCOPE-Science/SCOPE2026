#!/usr/bin/env python3
"""Independent finite checks for the Kneser minimum-Roman sliding theorem.

Runs with Python 3 only. The general theorem is established by its written proof;
these finite computations are consistency and boundary tests, not an infinite certificate.
"""
from itertools import combinations
from collections import Counter
from math import comb, factorial


def configurations(n, k=2):
    # Only used for k=2, where 3 pairwise-disjoint pairs are manageable.
    assert k == 2
    e = list(combinations(range(n), 2))
    return [tuple(sorted(t)) for t in combinations(e, 3)
            if len(set().union(*(set(x) for x in t))) == 6]


def edges_of_Kneser(n, k):
    return list(combinations(range(n), k))


def adjacent_configurations(s, n, sliding=True):
    current = set(s)
    for old in s:
        retained = current - {old}
        covered = set().union(*(set(block) for block in retained))
        available = set(range(n)) - covered
        for new in combinations(sorted(available), len(old)):
            if new == old:
                continue
            if sliding and not set(new).isdisjoint(old):
                continue
            assert set(new).isdisjoint(covered)
            yield tuple(sorted(retained | {new}))


def roman_6_support_is_matching(n):
    # Every 3-label-2, no-label-1 labeling of weight six is examined
    # directly under the total-Roman definition, including positive vertices.
    vertices = edges_of_Kneser(n, 2)
    valid = set()
    for triple in combinations(vertices, 3):
        defenders = set(triple)
        ok = True
        for v in vertices:
            # The all-zero remainder requires a defender disjoint from v.
            # A defender itself must also have a positive neighbor.
            if not any(set(v).isdisjoint(d) for d in defenders):
                ok = False
                break
        if ok:
            valid.add(tuple(sorted(triple)))
    expected = set(configurations(n))
    assert valid == expected, (n, len(valid), len(expected))


def connected_component_sizes(n):
    V = configurations(n)
    remaining = set(V)
    component_sizes = Counter()
    degrees = Counter()
    for s in V:
        neighbors = set(adjacent_configurations(s, n, True))
        assert s not in neighbors
        degrees[len(neighbors)] += 1
    while remaining:
        root = remaining.pop()
        q = [root]
        for s in q:
            for t in adjacent_configurations(s, n, True):
                if t in remaining:
                    remaining.remove(t)
                    q.append(t)
        component_sizes[len(q)] += 1
    return len(V), component_sizes, degrees


def test_connectivity_of_one_token_KG(N, k):
    # Independent reconstruction of the Kneser graph on k-subsets.
    V = set(combinations(range(N), k))
    todo = set(V)
    start = todo.pop()
    q = [start]
    for A in q:
        for B in V:
            if B in todo and set(A).isdisjoint(B):
                todo.remove(B)
                q.append(B)
    assert not todo, (N, k, len(todo))


def main():
    for n in range(6, 11):
        count, components, degrees = connected_component_sizes(n)
        s = n - 6
        predicted = factorial(n) // (factorial(s) * 2**3 * factorial(3))
        assert count == predicted == 15 * comb(n, 6)
        assert degrees == Counter({3 * comb(s, 2) if s >= 2 else 0: count})
        if s < 2:
            assert components == Counter({1: count})
        elif s == 2:
            assert components == Counter({4: 105})
        else:
            assert components == Counter({count: 1})
        print(f'k=2 n={n}: configurations={count}, components={dict(components)}, degrees={dict(degrees)}')
    for n in range(6, 10):
        roman_6_support_is_matching(n)
        print(f'k=2 n={n}: all 3-defender total Roman supports are matchings')
    for k in (2, 3, 4):
        test_connectivity_of_one_token_KG(2*k + 1, k)
        print(f'KG({2*k+1},{k}) connected')
    for k in range(2, 15):
        n = k * (k + 2)
        partitions = factorial(n) // (factorial(k)**(k+2) * factorial(k+2))
        total_states = factorial(n) // (factorial(k)**(k+1) * factorial(k+1) * factorial(k))
        assert total_states == (k+2)*partitions
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
