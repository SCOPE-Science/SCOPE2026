#!/usr/bin/env python3
"""Reproduce the classification of optimum identifying-code exchanges in K3 square Km.
Run with Python 3.9+; no external packages are required.
"""
from collections import Counter, deque
from itertools import combinations, permutations, product
from math import comb, factorial


def closed_neighborhoods(m):
    return tuple(sum(1 << (r * m + j) for r in range(3) for j in range(m)
                     if r == i or j == c)
                 for i in range(3) for c in range(m))


def valid(code, neighborhoods):
    seen = set()
    for neighborhood in neighborhoods:
        signature = code & neighborhood
        if not signature or signature in seen:
            return False
        seen.add(signature)
    return True


def predicted_words(m):
    # S_i means a singleton containing row i, D_i a double missing row i.
    for loc in permutations(range(m), 3):
        word = [None] * m
        for i, position in enumerate(loc):
            word[position] = i
        double_positions = [j for j, x in enumerate(word) if x is None]
        for missing in product(range(3), repeat=m - 3):
            a = word[:]
            for position, color in zip(double_positions, missing):
                a[position] = color + 3
            yield tuple(a)


def as_mask(word):
    m = len(word)
    chosen = 0
    for j, t in enumerate(word):
        for row in range(3):
            if (t < 3 and t == row) or (t >= 3 and t - 3 != row):
                chosen |= 1 << (row * m + j)
    return chosen


def symbolic_neighbors(word):
    m = len(word)
    loc = {t: j for j, t in enumerate(word) if t < 3}
    for j, missing in enumerate(word):
        if missing < 3:
            continue
        a = missing - 3
        for b in range(3):
            if b != a:
                next_word = list(word)
                next_word[j] = 3 + b
                yield tuple(next_word)
        for moving in range(3):
            if moving == a:
                continue
            old = loc[moving]
            for replacement_missing in range(3):
                if replacement_missing == moving:
                    continue
                next_word = list(word)
                next_word[old] = replacement_missing + 3
                next_word[j] = moving
                yield tuple(next_word)


def direct_neighbors(mask, m, admissible):
    width = 3 * m
    for old in range(width):
        if not mask & (1 << old):
            continue
        for new in range(width):
            if mask & (1 << new):
                continue
            changed = mask ^ (1 << old) ^ (1 << new)
            if changed in admissible:
                yield changed


def exhaustive(m):
    k = 2 * m - 3
    neighborhoods = closed_neighborhoods(m)
    minimum = set()
    checks = 0
    for size in range(k + 1):
        for indices in combinations(range(3 * m), size):
            mask = sum(1 << x for x in indices)
            checks += 1
            if valid(mask, neighborhoods):
                if size != k:
                    raise AssertionError(('smaller_code', m, size, indices))
                minimum.add(mask)
    predicted = {as_mask(word) for word in predicted_words(m)}
    assert minimum == predicted, (m, len(minimum), len(predicted))
    assert len(predicted) == factorial(m) // factorial(m-3) * 3**(m-3)
    print('EXHAUSTIVE', m, 'checked_subsets', checks, 'minimum_size', k,
          'minimum_codes', len(minimum), flush=True)
    return minimum


def graph_check(m, exact_codes=None):
    words = list(predicted_words(m))
    masks = {as_mask(w): w for w in words}
    assert len(masks) == len(words)
    if exact_codes is not None:
        assert set(masks) == exact_codes
    degrees = Counter()
    edge_sum = 0
    edges = {}
    all_codes = set(masks)
    for mask, word in masks.items():
        symbolic = {as_mask(next_word) for next_word in symbolic_neighbors(word)}
        direct = set(direct_neighbors(mask, m, all_codes))
        assert symbolic == direct, (m, word, symbolic ^ direct)
        assert len(direct) == 6*(m-3)
        degrees[len(direct)] += 1
        edge_sum += len(direct)
        edges[mask] = direct
    root = next(iter(masks))
    seen = {root}
    queue = deque([root])
    while queue:
        here = queue.popleft()
        for other in edges[here]:
            if other not in seen:
                seen.add(other)
                queue.append(other)
    assert len(seen) == len(words)
    assert edge_sum//2 == 3*(m-3)*len(words)
    orbit_profiles = Counter(tuple(sorted(Counter(t for t in w if t >= 3).values()))
                             for w in words)
    assert sum(orbit_profiles.values()) == len(words)
    print('EXCHANGE',m,'states',len(words),'edges',edge_sum//2,
          'degree',6*(m-3),'components',1,'natural_orbits',len(orbit_profiles),
          flush=True)


def main():
    # Directly enumerate every vertex subset through the claimed optimum.
    for m in range(4, 8):
        minimum = exhaustive(m)
        graph_check(m, minimum)
    # A larger complete configuration-level check, without exhaustive smaller sets.
    graph_check(8)
    print('ALL_VERIFY_OK')

if __name__ == '__main__':
    main()
