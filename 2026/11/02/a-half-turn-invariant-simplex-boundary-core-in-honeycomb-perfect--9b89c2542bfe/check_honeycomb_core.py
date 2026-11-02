"""Finite checks for a rotationally invariant sphere core in a honeycomb matching complex.

Checks finite instances of a theorem proved for all n in the accompanying text.
Requires Python 3.10+; no third-party dependencies.
"""
from collections import deque


def perfect_matching_facets(n):
    assert n >= 2
    facets = []
    for p in range(n + 1):
        for q in range(p + 1):
            h = (p, q)
            f = {('a', i, h[i - 1]) for i in (1, 2)}
            for j in range(1, n + 1):
                if j > p:
                    f.add(('b', 0, j))
                if p >= j > q:
                    f.add(('b', 1, j))
                if j <= q:
                    f.add(('b', 2, j))
            for i in (0, 1, 2):
                for j in range(n + 1):
                    if (i, j) in {(0, n), (2, 0)}:
                        continue
                    if ((i == 0 and j < p) or
                        (i == 1 and (j > p or j < q)) or
                        (i == 2 and j > q)):
                        f.add(('d', i, j))
            facets.append((h, frozenset(f)))
    return facets


def half_turn(edge, n):
    c, i, j = edge
    if c == 'a':
        return ('a', 3 - i, n - j)
    if c == 'b':
        return ('b', 2 - i, n + 1 - j)
    return ('d', 2 - i, n - j)


def compute(n, check_acyclic=False):
    facets = perfect_matching_facets(n)
    assert len(facets) == (n + 1) * (n + 2) // 2
    fsets = {f for _, f in facets}
    for (p, q), face in facets:
        reflected = frozenset(half_turn(a, n) for a in face)
        assert reflected in fsets
        assert reflected == next(F for h, F in facets if h == (n - q, n - p))
    edges = sorted(set().union(*(f for _, f in facets)))
    loc = {e: i for i, e in enumerate(edges)}
    assert len(edges) == 8 * n + 3
    face_masks = []
    for _, f in facets:
        face_masks.append(sum(1 << loc[e] for e in f))
    K = set()
    for f in face_masks:
        bits = []
        while f:
            b = f & -f
            bits.append(b)
            f -= b
        for mask in range(1 << len(bits)):
            K.add(sum(b for j, b in enumerate(bits) if mask >> j & 1))
    x = 1 << loc[('d', 0, 0)]
    y = 1 << loc[('d', 2, n)]
    significant = [1 << loc[('d', 1, j)] for j in range(1, n)]
    core_vertices = [x, y, *significant]
    all_core = sum(core_vertices)
    L = {sum(b for j, b in enumerate(core_vertices) if mask >> j & 1)
         for mask in range((1 << (n + 1)) - 1)}
    assert all_core not in K
    assert L.issubset(K)
    remaining = set(K)
    matched = {}
    for toggle in (x, y):
        pairs = [(a, a | toggle) for a in remaining
                 if not a & toggle and (a | toggle) in remaining]
        for a, b in pairs:
            remaining.remove(a)
            remaining.remove(b)
            assert (a in L) == (b in L)
            if a not in L:
                matched[a] = b
    assert remaining == {y | sum(significant)}
    assert len(matched) * 2 == len(K) - len(L)
    assert len(L) == (1 << (n + 1)) - 1
    if check_acyclic:
        outside = K - L
        indeg = dict.fromkeys(outside, 0)
        for upper in outside:
            tmp = upper
            while tmp:
                bit = tmp & -tmp
                tmp -= bit
                lower = upper ^ bit
                if lower not in outside:
                    continue
                if matched.get(lower) == upper:
                    indeg[upper] += 1
                else:
                    indeg[lower] += 1
        todo = deque(k for k, deg in indeg.items() if deg == 0)
        removed = 0
        while todo:
            a = todo.popleft()
            removed += 1
            # Outgoing edges from an upper face through each unmatched facet.
            tmp = a
            while tmp:
                bit = tmp & -tmp
                tmp -= bit
                lower = a ^ bit
                if lower in outside and matched.get(lower) != a:
                    indeg[lower] -= 1
                    if indeg[lower] == 0:
                        todo.append(lower)
            # Outgoing reversed matching edge, when this is a lower face.
            b = matched.get(a)
            if b is not None:
                indeg[b] -= 1
                if indeg[b] == 0:
                    todo.append(b)
        assert removed == len(outside), (removed, len(outside))
    expected_degree = (-1) ** (n * (n + 1) // 2)
    perm = [half_turn(e, n) for e in [('d', 0, 0), ('d', 2, n)] +
            [('d', 1, j) for j in range(1, n)]]
    assert perm[0] == ('d', 2, n) and perm[1] == ('d', 0, 0)
    assert perm[2:] == [('d', 1, n - j) for j in range(1, n)]
    assert expected_degree == (-1) ** (1 + (n - 1) // 2)
    print(f'n={n} facets={len(facets)} complex_faces={len(K)} '
          f'core_faces={len(L)} outside_pairs={len(matched)} '
          f'half_turn_degree={expected_degree} '
          f'acyclicity_checked={check_acyclic}')


if __name__ == '__main__':
    for parameter in (2, 3, 4):
        compute(parameter, check_acyclic=(parameter <= 3))
    print('HONEYCOMB_INVARIANT_SPHERE_CORE_CHECKS_OK')
