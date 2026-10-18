#!/usr/bin/env python3
"""Exact finite-chain and acyclic-matching verification for the bidirected octahedron."""
from collections import Counter, defaultdict, deque
from functools import lru_cache

ARCS = tuple((u, v) for u in range(6) for v in range(6) if u // 2 != v // 2)
ORDER = (6, 16, 21, 14, 1, 5, 19, 10, 9, 13, 23, 12, 3, 8, 20, 22, 0, 2, 15, 11, 4, 17, 18, 7)


def build_faces():
    faces = {0}
    layer = [0]
    while layer:
        next_layer = set()
        for f in layer:
            indegree = set()
            outdegree = set()
            next_of = {}
            for j, (u, v) in enumerate(ARCS):
                if f >> j & 1:
                    outdegree.add(u)
                    indegree.add(v)
                    next_of[u] = v
            for j, (u, v) in enumerate(ARCS):
                if f >> j & 1 or u in outdegree or v in indegree:
                    continue
                w = v
                while w in next_of:
                    w = next_of[w]
                if w == u:
                    continue
                g = f | (1 << j)
                if g not in faces:
                    next_layer.add(g)
        layer = sorted(next_layer)
        faces.update(layer)
    return faces


def boundary(f):
    return [(f ^ (1 << i), -1 if j % 2 else 1)
            for j, i in enumerate(i for i in range(24) if f >> i & 1)]


def gf2_rank(columns):
    piv = {}
    for col in columns:
        while col:
            k = col.bit_length() - 1
            if k in piv:
                col ^= piv[k]
            else:
                piv[k] = col
                break
    return len(piv)


def main():
    faces = build_faces()
    nonempty = faces - {0}
    levels = {d: sorted(f for f in nonempty if f.bit_count() == d + 1)
              for d in range(5)}
    assert [len(levels[d]) for d in range(5)] == [24, 192, 616, 744, 240]
    assert len(nonempty) == 1816
    for f in nonempty:
        for g, _ in boundary(f):
            assert g in faces
    print('f_vector:', *(len(levels[d]) for d in range(5)))

    unmatched = set(nonempty)
    pairs = []
    for vertex in ORDER:
        for lo in sorted(unmatched, key=lambda f: (f.bit_count(), f)):
            if lo not in unmatched or lo & (1 << vertex):
                continue
            hi = lo | (1 << vertex)
            if hi in unmatched:
                unmatched.remove(lo)
                unmatched.remove(hi)
                pairs.append((lo, hi))
    upward = dict(pairs)
    assert len(pairs) == 843
    crit = {d: sorted(f for f in unmatched if f.bit_count() == d + 1)
            for d in range(5)}
    assert [len(crit[d]) for d in range(5)] == [1, 0, 4, 93, 32]
    print('matched_pairs:', len(pairs))
    print('critical_cells:', *(len(crit[d]) for d in range(5)))

    # Every incidence is reversed precisely when it belongs to the matching.
    indegree = dict.fromkeys(nonempty, 0)
    directed = defaultdict(list)
    covers = 0
    for hi in nonempty:
        for lo, _ in boundary(hi):
            if not lo:
                continue
            covers += 1
            a, b = (lo, hi) if upward.get(lo) == hi else (hi, lo)
            directed[a].append(b)
            indegree[b] += 1
    fringe = deque(f for f in nonempty if indegree[f] == 0)
    visited = 0
    while fringe:
        f = fringe.popleft()
        visited += 1
        for g in directed[f]:
            indegree[g] -= 1
            if indegree[g] == 0:
                fringe.append(g)
    assert visited == 1816
    assert covers == 6408  # all covering relations between nonempty faces
    print('directed_cover_relations:', covers)
    print('acyclic_toposort:', visited)

    def morse_boundary(d):
        targets = {f: i for i, f in enumerate(crit[d - 1])}
        @lru_cache(None)
        def project(lo):
            if lo in targets:
                return {targets[lo]: 1}
            if lo not in upward:
                return {}  # an upper cell in a matching of lower dimension
            hi = upward[lo]
            signed = dict(boundary(hi))
            pivot = signed[lo]
            answer = defaultdict(int)
            for sub, coefficient in signed.items():
                if sub == lo:
                    continue
                for row, val in project(sub).items():
                    answer[row] -= pivot * coefficient * val
            return {i: x for i, x in answer.items() if x}
        rows = [[0] * len(crit[d]) for _ in targets]
        for col, hi in enumerate(crit[d]):
            for lo, coefficient in boundary(hi):
                for row, val in project(lo).items():
                    rows[row][col] += coefficient * val
        return rows

    d3 = morse_boundary(3)
    d4 = morse_boundary(4)
    assert all(x == 0 for row in d4 for x in row)
    nonzero = [(i, j, x) for i, row in enumerate(d3)
               for j, x in enumerate(row) if x]
    assert nonzero
    assert all(abs(x) <= 1 for _, _, x in nonzero)
    # Rank one: every nonzero row is plus or minus the first nonzero row.
    first = next(row for row in d3 if any(row))
    assert all(row == first or row == [-x for x in first] or not any(row)
               for row in d3)
    assert any(abs(x) == 1 for row in d3 for x in row)
    print('morse_d3_rank_and_unit_smith:', 1, 1)
    print('morse_d4_nonzero:', 0)
    print('integral_reduced_betti:', 0, 0, 3, 92, 32)

    # A wholly separate boundary calculation over the field with two elements.
    bdranks = [0]
    for d in range(1, 5):
        idx = {f: j for j, f in enumerate(levels[d - 1])}
        columns = [sum(1 << idx[lo] for lo, _ in boundary(f))
                   for f in levels[d]]
        bdranks.append(gf2_rank(columns))
    assert bdranks == [0, 23, 169, 444, 208]
    print('independent_mod2_boundary_ranks:', *bdranks[1:])
    print('RESULT: PASS')


if __name__ == '__main__':
    main()
