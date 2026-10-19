"""Exhaustive finite demonstration for a (16,6,2) biplane.

The theorem is valid for every symmetric design with these parameters;
this script constructs one explicit example from the Clebsch graph and
independently enumerates every five-point test set in that example.
"""
from collections import Counter
from itertools import combinations


def main():
    n = 16
    points = tuple(range(n))
    generators = (1, 2, 4, 8, 15)
    neighborhoods = [frozenset(v ^ g for g in generators) for v in points]
    blocks = [frozenset({v} | set(neighborhoods[v])) for v in points]
    assert len(set(blocks)) == n
    assert all(len(b) == 6 for b in blocks)
    assert all(sum(p in b for b in blocks) == 6 for p in points)
    for x, y in combinations(points, 2):
        assert sum(x in b and y in b for b in blocks) == 2
    for B, D in combinations(blocks, 2):
        assert len(B & D) == 2

    # Every five-subset of a block is part of the displayed family.
    predicted = {frozenset(B - {p}) for B in blocks for p in B}
    assert len(predicted) == n * 6

    # Exhaustive signature test over all 4368 five-subsets.
    actual = set()
    for tup in combinations(points, 5):
        C = frozenset(tup)
        signatures = [frozenset(B & C) for B in blocks]
        if all(signatures) and len(set(signatures)) == n:
            actual.add(C)
    assert len(actual) == 96
    assert actual == predicted
    for C in actual:
        profile = Counter(len(B & C) for B in blocks)
        assert profile == Counter({1: 5, 2: 10, 5: 1})

    # The one-point-exchange adjacency is computed without assuming
    # any relationship between graph components and design blocks.
    E = set()
    adj = {C: set() for C in actual}
    for C, D in combinations(actual, 2):
        if len(C & D) == 4:
            E.add(frozenset((C, D)))
            adj[C].add(D)
            adj[D].add(C)
    assert len(E) == 240
    assert all(len(adj[C]) == 5 for C in actual)
    components = []
    unseen = set(actual)
    while unseen:
        root = unseen.pop()
        reached = {root}
        stack = [root]
        while stack:
            for y in adj[stack.pop()]:
                if y not in reached:
                    reached.add(y)
                    unseen.discard(y)
                    stack.append(y)
        components.append(reached)
    assert len(components) == n
    assert all(len(component) == 6 for component in components)
    assert all(sum(len(adj[x] & component) for x in component) == 30 for component in components)
    assert {frozenset(component) for component in components} == {
        frozenset(frozenset(B - {p}) for p in B) for B in blocks
    }
    print("DESIGN: symmetric 2-(16,6,2)")
    print("LOWER_BOUND: 2^4-1=15 < 16")
    print("FIVE_SUBSETS_TESTED:", 4368)
    print("VALID_MINIMUM_TEST_SETS:", len(actual))
    print("SIGNATURE_SIZE_PROFILE: 1:5, 2:10, 5:1")
    print("EXCHANGE_GRAPH: 16 components isomorphic to K6, 240 edges")
    print("VERIFY_OK")


if __name__ == '__main__':
    main()
