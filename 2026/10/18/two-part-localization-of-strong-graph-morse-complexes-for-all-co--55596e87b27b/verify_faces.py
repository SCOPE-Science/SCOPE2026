"""Finite checks of the exact facet description for strong graph-Morse complexes.

The mathematical proof for all part sizes is independent of these tests.
Requires Python 3 standard library only. Run: python verify_complete_multipartite_strong_morse.py
"""
from collections import Counter
from itertools import combinations, permutations


def all_faces(generators):
    faces = {frozenset()}
    for simplex in generators:
        s = tuple(simplex)
        for k in range(1, len(s) + 1):
            faces.update(frozenset(sub) for sub in combinations(s, k))
    return faces


def order_matchings(part_labels):
    vertices = range(len(part_labels))
    found = set()
    for order in permutations(vertices):
        old, matches = [], []
        for v in order:
            earlier_neighbors = [w for w in old if part_labels[w] != part_labels[v]]
            if len(earlier_neighbors) == 1:
                matches.append((v, earlier_neighbors[0]))
            old.append(v)
        found.add(frozenset(matches))
    return found


def proposed_generators(part_labels):
    groups = {}
    for v, part in enumerate(part_labels):
        groups.setdefault(part, []).append(v)
    generators = set()
    for i, j in combinations(groups, 2):
        A, B = groups[i], groups[j]
        for a in A:
            generators.add(frozenset((b, a) for b in B))
        for b in B:
            generators.add(frozenset((a, b) for a in A))
        for a in A:
            for b in B:
                generators.add(frozenset({(b, a)} | {(ap, b) for ap in A if ap != a}))
                generators.add(frozenset({(a, b)} | {(bp, a) for bp in B if bp != b}))
    return generators


def ranks_mod2(faces):
    by_dim = {}
    for s in faces:
        if s:
            by_dim.setdefault(len(s)-1, []).append(tuple(sorted(s)))
    for simplices in by_dim.values():
        simplices.sort()
    ranks = {}
    for d, domain in sorted(by_dim.items()):
        if d == 0:
            ranks[d] = 0
            continue
        targets = {s: i for i, s in enumerate(by_dim[d - 1])}
        pivots = {}
        rank = 0
        for simplex in domain:
            mask = 0
            for face in combinations(simplex, d):
                mask ^= 1 << targets[face]
            while mask:
                high = mask.bit_length() - 1
                if high not in pivots:
                    pivots[high] = mask
                    rank += 1
                    break
                mask ^= pivots[high]
        ranks[d] = rank
    return {d: len(v) - ranks[d] - ranks.get(d+1, 0) for d, v in by_dim.items()}


def theoretical_betti(sizes):
    singles = sum(n == 1 for n in sizes)
    components = len(sizes) * (len(sizes) - 1) // 2 + singles * (singles-1) // 2
    beta1 = sum(2*a*b-a-b+1 for a,b in combinations(sizes, 2) if a>=2 and b>=2)
    return components, beta1


if __name__ == "__main__":
    cases = [(2,2,2), (1,2,2), (1,1,2), (1,1,1,1),
             (2,3,2), (2,2,1,1), (3,3), (1,4), (2,3), (1,1)]
    for sizes in cases:
        labels = [i for i, size in enumerate(sizes) for _ in range(size)]
        order_faces = all_faces(order_matchings(labels))
        formula_faces = all_faces(proposed_generators(labels))
        assert order_faces == formula_faces, (sizes, 'face equality failed')
        b = ranks_mod2(order_faces)
        c, h1 = theoretical_betti(sizes)
        assert b.get(0, 0) == c and b.get(1, 0) == h1, (sizes,b,c,h1)
        assert all(value == 0 for degree, value in b.items() if degree >= 2), (sizes,b)
        print(f"parts={sizes} faces={len(order_faces)-1} components={c} beta1={h1} verified")
    print('ALL COMPLETE: exact generated faces and mod-2 Betti numbers agree.')
