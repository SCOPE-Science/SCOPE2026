#!/usr/bin/env python3
"""Exact finite consistency checks for bounded-independence complexes of chorded cycles.
Run: python3 verify.py. Requires Python standard library only.
"""
from itertools import combinations


def faces(n, chord):
    edges = {frozenset((i, (i + 1) % n)) for i in range(n)}
    if chord:
        edges.add(frozenset((0, 2)))
    out = {frozenset()}
    # Every face has at most 5 vertices for n >= 7, proved separately.
    for size in range(1, 7):
        for subset in combinations(range(n), size):
            if all(any(frozenset(e) in edges for e in combinations(t, 2))
                   for t in combinations(subset, 3)):
                out.add(frozenset(subset))
    return out


def predicted_new(n):
    return ({frozenset((0, 2, j)) for j in range(4, n - 1)}
            | {frozenset((0, 1, 2, j)) for j in range(4, n - 1)}
            | {frozenset((0, 2, j, j + 1)) for j in range(3, n - 1)}
            | {frozenset((0, 1, 2, j, j + 1)) for j in range(3, n - 1)})


def collapse(n, old, new):
    current = set(new)
    for j in range(3, n - 1):
        top = frozenset((0, 1, 2, j, j + 1))
        free = frozenset((0, 2, j, j + 1))
        assert top in current and free in current
        assert sum(free <= f and len(f) == 5 for f in current) == 1
        current.remove(top)
        current.remove(free)
    for j in range(4, n - 1):
        top = frozenset((0, 1, 2, j))
        free = frozenset((0, 2, j))
        assert top in current and free in current
        assert sum(free <= f and len(f) == 4 for f in current) == 1
        current.remove(top)
        current.remove(free)
    assert current == old


def verify_six():
    current = faces(6, True)
    current.discard(frozenset())
    moves = []
    while True:
        facets = [f for f in current if not any(f < other for other in current)]
        facets.sort(key=lambda f: (-len(f), tuple(sorted(f))))
        choice = None
        for top in facets:
            for v in sorted(top):
                free = top - {v}
                if free in current and sum(free <= f for f in facets) == 1:
                    choice = free, top
                    break
            if choice:
                break
        if choice is None:
            break
        free, top = choice
        assert sum(free <= f for f in facets) == 1
        current.remove(free)
        current.remove(top)
        moves.append(choice)
    assert len(moves) == 27, len(moves)
    assert current == {frozenset((0,))}, current
    return len(moves)


def run():
    six = verify_six()
    total = 0
    for n in range(7, 19):
        before = faces(n, False)
        after = faces(n, True)
        extra = after - before
        predicted = predicted_new(n)
        assert extra == predicted, (n, extra ^ predicted)
        assert all(len(f) <= 5 for f in after)
        assert len(extra) == 4 * n - 18, (n, len(extra))
        collapse(n, before, after)
        total += 1
    print(f'VERIFY_OK {six} six-vertex collapses; {total} full enumerations and exact two-stage elementary collapses')


if __name__ == '__main__':
    run()
