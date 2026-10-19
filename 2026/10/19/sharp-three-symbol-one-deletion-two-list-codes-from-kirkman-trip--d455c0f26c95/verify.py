"""Standalone exact checker for short two-list single-deletion code constructions."""
from collections import Counter
from itertools import combinations, product


def descendants(word):
    return {word[:i] + word[i+1:] for i in range(3)}


def build(q, triples, special):
    vertices = set(range(q))
    blocks = {frozenset(b) for b in triples}
    chosen = {frozenset(b) for b in special}
    assert len(blocks) == q * (q - 1) // 6
    assert chosen <= blocks
    assert len(chosen) == q // 3
    assert len(set().union(*chosen)) == q
    pair_degrees = Counter(tuple(sorted(p)) for b in blocks for p in combinations(b, 2))
    assert all(pair_degrees[p] == 1 for p in combinations(range(q), 2))
    code = {(a, a, a) for a in vertices}
    for b in blocks:
        a, c, d = sorted(b)
        if b in chosen:
            code.update([(a, a, d), (c, c, a), (d, d, c),
                         (a, c, d), (c, d, a), (d, a, c)])
        else:
            # Four permutations obtained by omitting the mutually reversed
            # ordered triples (a,c,d) and (d,c,a).
            code.update([(a, d, c), (c, a, d), (c, d, a), (d, a, c)])
    assert len(code) == q + 2 * q * q // 3, (q, len(code))
    y_count = Counter(y for w in code for y in descendants(w))
    assert len(y_count) == q * q
    assert all(y_count[(a, b)] == 2 for a, b in product(range(q), repeat=2))
    # The independent universal counting upper bound is floor(2 q^2/3)+q.
    assert len(code) == q + (2*q*q)//3
    return len(code)


def affine_plane_9():
    pts = list(product(range(3), repeat=2))
    coord = {p: i for i, p in enumerate(pts)}
    directions = ((1,0), (0,1), (1,1), (1,2))
    all_blocks = set()
    for dx, dy in directions:
        for x, y in pts:
            line = frozenset(coord[((x + t * dx) % 3, (y + t * dy) % 3)] for t in range(3))
            all_blocks.add(line)
    selected = [frozenset(coord[(x,y)] for y in range(3)) for x in range(3)]
    return all_blocks, selected


def main():
    assert build(3, [(0,1,2)], [(0,1,2)]) == 9
    blocks, parallel = affine_plane_9()
    assert build(9, blocks, parallel) == 63
    print('VERIFY_OK q=3:9 q=9:63; each ordered two-symbol descendant occurs exactly twice')


if __name__ == '__main__':
    main()
