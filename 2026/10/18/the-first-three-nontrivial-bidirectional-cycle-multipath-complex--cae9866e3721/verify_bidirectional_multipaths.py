#!/usr/bin/env python3
"""Finite certificates for the homotopy classification of small bidirectional cycle multipath complexes.
Only the Python standard library is required. Directed edge indices are 0:(0,1), 1:(1,0),
2:(1,2), 3:(2,1), and so forth cyclically.
"""
from collections import Counter, deque
from itertools import combinations

PIVOTS = {
    4: tuple(range(8)),
    5: (0, 4, 9, 7, 6, 1, 8, 5, 2, 3),
    6: tuple(range(12)),
}
EXPECTED = {
    4: (33, 14, {1: 3, 2: 2}),
    5: (81, 39, {2: 1, 3: 2}),
    6: (197, 97, {2: 1, 4: 2}),
}
# An integral 2-cocycle in X(BP_5): the labels are indices of directed edges.
COCHAIN = {
    (0, 2, 4): 1,
    (0, 2, 6): 1,
    (2, 4, 8): 1,
    (2, 6, 8): 1,
    (0, 4, 9): -1,
    (2, 4, 10): 1,
    (2, 6, 10): 1,
}


def edge_list(n):
    return tuple(edge for i in range(n)
                 for edge in ((i, (i + 1) % n), ((i + 1) % n, i)))


def is_multipath(n, edges, mask):
    outgoing = [-1] * n
    incoming = [-1] * n
    for j, (a, b) in enumerate(edges):
        if mask & (1 << j):
            if outgoing[a] != -1 or incoming[b] != -1:
                return False
            outgoing[a] = b
            incoming[b] = a
    for a in range(n):
        seen = set()
        cur = a
        while outgoing[cur] != -1:
            if cur in seen:
                return False
            seen.add(cur)
            cur = outgoing[cur]
    return True


def all_faces(n):
    edges = edge_list(n)
    return {s for s in range(1 << len(edges)) if is_multipath(n, edges, s)}


def element_matching(faces, ordering):
    remaining = set(faces)
    pairs = []
    for j in ordering:
        todo = [(s, s | (1 << j)) for s in sorted(remaining)
                if not (s & (1 << j)) and (s | (1 << j)) in remaining]
        for lo, hi in todo:
            assert lo in remaining and hi in remaining
            remaining.remove(lo)
            remaining.remove(hi)
        pairs.extend(todo)
    assert len(set(x for pair in pairs for x in pair)) == 2 * len(pairs)
    return pairs, remaining


def acyclic_hasse(n, faces, pairs):
    paired = set(pairs)
    arcs = {s: [] for s in faces}
    indeg = {s: 0 for s in faces}
    for upper in faces:
        for j in range(2 * n):
            if upper & (1 << j):
                lower = upper ^ (1 << j)
                assert lower in faces
                a, b = (lower, upper) if (lower, upper) in paired else (upper, lower)
                arcs[a].append(b)
                indeg[b] += 1
    queue = deque(s for s in faces if indeg[s] == 0)
    count = 0
    while queue:
        x = queue.popleft()
        count += 1
        for y in arcs[x]:
            indeg[y] -= 1
            if indeg[y] == 0:
                queue.append(y)
    assert count == len(faces), (n, count, len(faces))
    return sum(map(len, arcs.values()))


def ordered_vertices(mask, n):
    return tuple(j for j in range(2 * n) if mask & (1 << j))


def row_basis(rows):
    pivots = {}
    for x in rows:
        while x:
            top = x.bit_length() - 1
            if top in pivots:
                x ^= pivots[top]
            else:
                pivots[top] = x
                break
    return pivots


def is_in_span(vector, basis):
    while vector:
        top = vector.bit_length() - 1
        if top not in basis:
            return False
        vector ^= basis[top]
    return True


def verify_n4(faces):
    forwards = {0, 2, 4, 6}
    backwards = {1, 3, 5, 7}
    triangles = {ordered_vertices(s, 4) for s in faces if s.bit_count() == 3}
    expected = {t for directions in (forwards, backwards)
                for t in combinations(sorted(directions), 3)}
    assert triangles == expected and len(triangles) == 8
    cross_edges = [ordered_vertices(s, 4) for s in faces if s.bit_count() == 2
                   and len(set(ordered_vertices(s, 4)) & forwards) == 1]
    assert len(cross_edges) == 4
    assert len({j for ij in cross_edges for j in ij}) == 8
    print('N=4: two disjoint tetrahedral boundaries and four bridging edges')


def verify_top_cycles(n, faces):
    top = {s for s in faces if s.bit_count() == n-1}
    expected = set()
    for parity in (0, 1):
        big = sum(1 << j for j in range(parity, 2*n, 2))
        expected |= {big ^ (1 << j) for j in range(parity, 2*n, 2)}
    assert top == expected and len(top) == 2*n
    assert not any(s.bit_count() >= n for s in faces)
    print(f'N={n}: two independent top cycles, each a simplex boundary')


def verify_n6_cup(faces):
    n = 6
    three = sorted(s for s in faces if s.bit_count() == 3)
    two = sorted(s for s in faces if s.bit_count() == 2)
    four = sorted(s for s in faces if s.bit_count() == 4)
    five = sorted(s for s in faces if s.bit_count() == 5)
    tr_index = {s: i for i, s in enumerate(three)}
    cochain = {sum(1 << j for j in support): c for support, c in COCHAIN.items()}
    assert len(cochain) == 7
    for support in cochain:
        assert support in three
    # Integral coboundary d(phi) = 0 on every oriented 3-simplex.
    for m in four:
        e = ordered_vertices(m, n)
        value = sum((-1)**k * cochain.get(m ^ (1 << j), 0)
                    for k, j in enumerate(e))
        assert value == 0, ('not cocycle', m, value)
    # Integer Alexander-Whitney cup square: phi(first three)phi(last three).
    for m in five:
        e = ordered_vertices(m, n)
        a = sum(1 << j for j in e[:3])
        b = sum(1 << j for j in e[2:])
        assert cochain.get(a, 0) * cochain.get(b, 0) == 0
    # Nonzero mod 2 cohomology class (thus nonzero integral class).
    coboundaries = []
    for edge in two:
        vector = 0
        for j, tr in enumerate(three):
            if (tr & edge) == edge:
                vector |= 1 << j
        coboundaries.append(vector)
    basis = row_basis(coboundaries)
    vector = sum(1 << tr_index[s] for s in cochain)
    assert not is_in_span(vector, basis)
    assert len(basis) == 37 and len(three) == 76
    print('N=6: integral 2-cocycle (7 supported triangles), nonzero mod 2; exact integral cup square is zero')


def main():
    for n in (4, 5, 6):
        faces = all_faces(n)
        pairs, unmatched = element_matching(faces, PIVOTS[n])
        number, paired, critdim = EXPECTED[n]
        assert len(faces) == number and len(pairs) == paired
        assert dict(Counter(s.bit_count()-1 for s in unmatched)) == critdim
        assert 0 not in unmatched and sum(1 for s in faces if s.bit_count()==1) == 2*n
        arcs = acyclic_hasse(n, faces, pairs)
        print(f'N={n}: {len(faces)} augmented faces, {len(pairs)} pairs, '
              f'critical={critdim}, Hasse arrows={arcs}, acyclic=PASS')
        if n == 4:
            verify_n4(faces)
        if n in (5, 6):
            verify_top_cycles(n, faces)
        if n == 6:
            verify_n6_cup(faces)
    print('VERIFY_OK: exact discrete Morse, top-cycle and Hopf-cup certificates')


if __name__ == '__main__':
    main()
