#!/usr/bin/env python3
"""Standalone exact homotopy certificate for the multipath complex of bidirected K(3,3).

Requires only the Python standard library. Enumeration, acyclicity and signed Morse
boundaries are rebuilt from the mathematical definition; no external data files.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations
import random

A = (0, 1, 2)
B = (3, 4, 5)
ARCS = tuple([(u, v) for u in A for v in B] + [(v, u) for u in A for v in B])


def valid(s):
    outgoing, incoming = {}, {}
    for index in s:
        u, v = ARCS[index]
        if u in outgoing or v in incoming:
            return False
        outgoing[u], incoming[v] = v, u
    for start in outgoing:
        visited, v = set(), start
        while v in outgoing:
            if v in visited:
                return False
            visited.add(v)
            v = outgoing[v]
    return True


FACES = set()
for size in range(1, 6):
    FACES.update(s for s in combinations(range(18), size) if valid(s))
COVERS = tuple((lo, up) for up in FACES for i in range(len(up))
               if (lo := up[:i] + up[i+1:]))


def match_lex(order):
    unmatched, pairs = set(FACES), {}
    for i in order:
        for lo in sorted(unmatched, key=lambda x: (len(x), x)):
            if i not in lo:
                up = tuple(sorted(lo + (i,)))
                if lo in unmatched and up in unmatched:
                    unmatched.remove(lo)
                    unmatched.remove(up)
                    pairs[lo] = up
    return pairs


def critical(pairs):
    return FACES - set(pairs) - set(pairs.values())


def acyclic(pairs):
    assert len(set(pairs.values())) == len(pairs)
    assert set(pairs).isdisjoint(pairs.values())
    degrees = {s: 0 for s in FACES}
    outgoing = {s: [] for s in FACES}
    for lo, up in COVERS:
        x, y = (lo, up) if pairs.get(lo) == up else (up, lo)
        outgoing[x].append(y)
        degrees[y] += 1
    todo = deque(s for s, degree in degrees.items() if degree == 0)
    total = 0
    while todo:
        x = todo.popleft()
        total += 1
        for y in outgoing[x]:
            degrees[y] -= 1
            if degrees[y] == 0:
                todo.append(y)
    return total == len(FACES)


def gradient_paths(upper, lower, pairs, limit=2):
    found = []
    size = len(upper)

    def walk(cur, trail, seen):
        if len(found) >= limit:
            return
        for j in range(size):
            down = cur[:j] + cur[j+1:]
            if pairs.get(down) == cur:
                continue
            if down == lower:
                found.append(tuple(trail + [(cur, down)]))
                continue
            nxt = pairs.get(down)
            if nxt is not None and nxt not in seen:
                walk(nxt, trail + [(cur, down), (down, nxt)], seen | {nxt})
    walk(upper, [], {upper})
    return found


def cancel(pairs, path):
    new = dict(pairs)
    for lo, up in path:
        if len(up) == len(lo) + 1 and new.get(lo) == up:
            del new[lo]
    for up, lo in path:
        if len(up) == len(lo) + 1:
            new[lo] = up
    assert acyclic(new)
    return new


def main():
    assert len(ARCS) == 18
    counts = dict(sorted(Counter(map(len, FACES)).items()))
    assert counts == {1: 18, 2: 108, 3: 264, 4: 252, 5: 72}, counts
    order = list(range(18))
    random.Random(0).shuffle(order)
    assert order == [11, 9, 0, 16, 2, 15, 10, 3, 5, 17, 14, 6, 7, 8, 4, 1, 13, 12]
    pairs = match_lex(order)
    assert acyclic(pairs)
    assert Counter(map(len, critical(pairs))) == {1: 1, 3: 4, 4: 23, 5: 12}
    history = []
    while True:
        c = critical(pairs)
        lower = sorted(s for s in c if len(s) == 3)
        if not lower:
            break
        upper = sorted(s for s in c if len(s) == 4)
        opts = []
        for lo in lower:
            for up in upper:
                paths = gradient_paths(up, lo, pairs)
                if len(paths) == 1:
                    opts.append((len(paths[0]), lo, up, paths[0]))
        assert opts, 'No unique gradient path available'
        _, lo, up, path = min(opts)
        pairs = cancel(pairs, path)
        history.append((lo, up, path))
        assert lo not in critical(pairs) and up not in critical(pairs)
    assert len(history) == 4
    c = critical(pairs)
    assert Counter(map(len, c)) == {1: 1, 4: 19, 5: 12}
    assert len(pairs) == 341 and len(FACES) == 714
    assert acyclic(pairs)
    uppermatched = set(pairs.values())

    @lru_cache(None)
    def reduce(face):
        if face in c:
            return {face: 1}
        if face in uppermatched:
            return {}
        high = pairs[face]
        extra = next(x for x in high if x not in face)
        j = high.index(extra)
        orientation = (-1) ** j
        coeff = Counter()
        for i in range(len(high)):
            if i == j:
                continue
            facet = high[:i] + high[i+1:]
            for target, value in reduce(facet).items():
                coeff[target] -= orientation * (-1) ** i * value
        return {t: v for t, v in coeff.items() if v}

    for dimension in range(1, 5):
        for high in sorted(s for s in c if len(s) == dimension + 1):
            vec = Counter()
            for j in range(len(high)):
                facet = high[:j] + high[j+1:]
                for target, value in reduce(facet).items():
                    vec[target] += (-1) ** j * value
            assert not any(vec.values()), (high, vec)
    print('PASS: 714 nonempty faces; f-cardinality counts', counts)
    print('PASS: 341 matched pairs; all 714 Hasse vertices acyclic')
    print('PASS: four unique-path cancellations, each acyclic')
    print('PASS: critical cells (dimension: count) = {0: 1, 3: 19, 4: 12}')
    print('PASS: EVERY integral Morse differential is the zero homomorphism')
    print('Deduction: simply connected 3-skeleton is wedge of nineteen 3-spheres;')
    print('12 four-cell attaching maps have zero integral degree and are null by Hurewicz.')
    print('Cancellation witnesses:', [(lo, up, len(path)) for lo, up, path in history])


if __name__ == '__main__':
    main()
