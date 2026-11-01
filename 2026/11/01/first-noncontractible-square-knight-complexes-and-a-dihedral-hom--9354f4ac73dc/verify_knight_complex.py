#!/usr/bin/env python3
"""Reproducible exhaustive finite checks of square-board knight complexes.
Only the Python standard library is required. Row-major vertices are 0..n*n-1.
"""
from collections import Counter, deque

MOVES = ((1, 2), (1, -2), (-1, 2), (-1, -2),
         (2, 1), (2, -1), (-2, 1), (-2, -1))


def adjacency(n):
    nbr = [0] * (n * n)
    for i in range(n):
        for j in range(n):
            a = i * n + j
            for di, dj in MOVES:
                u, v = i + di, j + dj
                if 0 <= u < n and 0 <= v < n:
                    nbr[a] |= 1 << (u * n + v)
    for a in range(n * n):
        for b in range(n * n):
            assert bool(nbr[a] & (1 << b)) == bool(nbr[b] & (1 << a))
    return nbr


def faces_incremental(nbr):
    faces = [0]
    for v in range(len(nbr)):
        bit = 1 << v
        faces += [s | bit for s in faces if s & nbr[v] == 0]
    assert len(faces) == len(set(faces))
    return faces


def faces_independent_backtrack(nbr):
    # Independently generated from a depth-first search, without a face set.
    out = []
    N = len(nbr)
    def visit(v, selected):
        if v == N:
            out.append(selected)
            return
        visit(v + 1, selected)
        if selected & nbr[v] == 0:
            visit(v + 1, selected | (1 << v))
    visit(0, 0)
    return out


def matching_and_acyclicity(faces, n):
    alive = set(faces)
    pairs = []
    history = []
    N = n * n
    # All eligible toggles at one vertex are paired before the next vertex.
    # This matching is independently verified by the directed Hasse DAG below.
    while True:
        scores = [(sum(1 for s in alive
                       if not (s & (1 << v)) and (s | (1 << v)) in alive), v)
                  for v in range(N)]
        count, v = max(scores)
        if not count:
            break
        bit = 1 << v
        stage = [(s, s | bit) for s in alive
                 if not (s & bit) and (s | bit) in alive]
        assert len(stage) == count
        for a, b in stage:
            assert a in alive and b in alive and b.bit_count() == a.bit_count() + 1
            alive.remove(a)
            alive.remove(b)
        pairs.extend(stage)
        history.append((v, count, len(alive)))
    assert 2 * len(pairs) + len(alive) == len(faces)
    lower_to_upper = dict(pairs)
    assert len(lower_to_upper) == len(pairs)
    index = {s: k for k, s in enumerate(faces)}
    indeg = [0] * len(faces)
    outgoing = [[] for _ in faces]
    incidence_count = 0
    for s in faces:
        a = index[s]
        for v in range(N):
            bit = 1 << v
            if s & bit:
                continue
            t = s | bit
            if t not in index:
                continue
            b = index[t]
            incidence_count += 1
            if lower_to_upper.get(s) == t:
                outgoing[b].append(a)
                indeg[a] += 1
            else:
                outgoing[a].append(b)
                indeg[b] += 1
    assert incidence_count == sum(s.bit_count() for s in faces)
    todo = deque(i for i, d in enumerate(indeg) if d == 0)
    visited = 0
    while todo:
        a = todo.popleft()
        visited += 1
        for b in outgoing[a]:
            indeg[b] -= 1
            if indeg[b] == 0:
                todo.append(b)
    assert visited == len(faces), 'Morse orientation has a directed cycle'
    assert sum(1 for a, b in pairs if a == 0) == 1
    # Deleting (empty simplex, matched vertex) turns the latter into a
    # critical zero-cell; all other critical cells retain their dimensions.
    return pairs, alive, history, incidence_count


def transformations(n):
    return {
        'identity': lambda i, j: (i, j),
        'r90': lambda i, j: (j, n - 1 - i),
        'r180': lambda i, j: (n - 1 - i, n - 1 - j),
        'r270': lambda i, j: (n - 1 - j, i),
        'horizontal': lambda i, j: (n - 1 - i, j),
        'vertical': lambda i, j: (i, n - 1 - j),
        'diagonal': lambda i, j: (j, i),
        'antidiagonal': lambda i, j: (n - 1 - j, n - 1 - i),
    }


def reduced_lefschetz_character(n, faces, nbr):
    classes = {}
    for name, fun in transformations(n).items():
        perm = [fun(i, j)[0] * n + fun(i, j)[1]
                for i in range(n) for j in range(n)]
        assert len(set(perm)) == n * n
        for a in range(n * n):
            for b in range(n * n):
                assert bool(nbr[a] & (1 << b)) == bool(nbr[perm[a]] & (1 << perm[b]))
        lefschetz = -1  # augmented empty face in degree -1
        fixed_nonempty = 0
        for s in faces:
            if not s:
                continue
            vertices = [v for v in range(n * n) if s & (1 << v)]
            images = [perm[v] for v in vertices]
            if sum(1 << v for v in images) != s:
                continue
            fixed_nonempty += 1
            inversions = sum(1 for a in range(len(images))
                             for b in range(a + 1, len(images))
                             if images[a] > images[b])
            lefschetz += (-1 if ((len(vertices) - 1 + inversions) & 1) else 1)
        # All reduced rational homology is in degree 3.
        classes[name] = (-lefschetz, fixed_nonempty + 1)
    return classes


def main():
    expected = {
        4: {
            'num_faces': 1365, 'num_pairs': 680, 'crit': [102, 240, 562, 1220, 3840],
            'incidences': 5788,
            'f_vector': [1, 16, 96, 276, 412, 340, 170, 48, 6],
            'character': [5, -1, 1, -1, 3, 3, -1, -1],
            'order': [15, 12, 10, 14, 9, 13, 11, 8],
        },
        5: {
            'num_faces': 55213, 'num_pairs': 27605,
            'crit': [30720, 137344, 1060992], 'incidences': 353749,
            'f_vector': [1, 25, 252, 1360, 4436, 9386, 13384,
                         12996, 8526, 3679, 994, 158, 15, 1],
            'character': [3, 1, -1, 1, -1, -1, -1, -1],
            'order': [24, 15, 0, 23, 17, 22, 16, 20, 14],
        },
    }
    ops = list(transformations(4))
    for n in (4, 5):
        ex = expected[n]
        nbr = adjacency(n)
        assert sum(x.bit_count() for x in nbr) // 2 == (24 if n == 4 else 48)
        faces = faces_incremental(nbr)
        second = faces_independent_backtrack(nbr)
        assert set(second) == set(faces) and len(second) == len(faces)
        vector = [Counter(s.bit_count() for s in faces)[i]
                  for i in range(max(s.bit_count() for s in faces) + 1)]
        assert vector == ex['f_vector']
        pairs, critical, history, incidences = matching_and_acyclicity(faces, n)
        assert len(faces) == ex['num_faces']
        assert len(pairs) == ex['num_pairs']
        assert sorted(critical) == ex['crit']
        assert all(s.bit_count() == 4 for s in critical)
        assert incidences == ex['incidences']
        assert [v for v, _, _ in history] == ex['order']
        ch = reduced_lefschetz_character(n, faces, nbr)
        assert [ch[o][0] for o in ops] == ex['character']
        # Irreducible characters A1,A2,B1,B2,E under the stated D4 convention
        names = ["A1", "A2", "B1", "B2", "E"]
        irrep = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, -1, -1, -1, -1],
            [1, -1, 1, -1, 1, 1, -1, -1],
            [1, -1, 1, -1, -1, -1, 1, 1],
            [2, 0, -2, 0, 0, 0, 0, 0],
        ]
        char = [ch[o][0] for o in ops]
        mul = [sum(a * b for a, b in zip(char, r)) // 8 for r in irrep]
        assert all(sum(a * b for a, b in zip(char, r)) % 8 == 0 for r in irrep)
        assert mul == ([1, 0, 2, 0, 1] if n == 4 else [0, 1, 0, 0, 1])
        assert sum(char) == (8 if n == 4 else 0)
        print(f"n={n} faces={len(faces)} f_vector={vector}")
        print(f"n={n} Morse_pairs={len(pairs)} incidences={incidences} acyclic=true")
        print(f"n={n} critical_masks={sorted(critical)}")
        print(f"n={n} toggle_vertices={ex['order']}")
        print(f"n={n} H3_D4_character={char} invariant_dimension={sum(char)//8}")
        print(f"n={n} D4_irrep_multiplicities={dict(zip(names,mul))}")
    # n=1,2 have no knight moves; n=3 has an isolated central square.
    for n in (1, 2, 3):
        nbr = adjacency(n)
        assert (all(x == 0 for x in nbr) if n < 3 else nbr[4] == 0)
    print('SMALL_BOARDS_CONTRACTIBLE')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
