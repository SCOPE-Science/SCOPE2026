#!/usr/bin/env python3
"""Exact finite simplicial-Morse certificate for a bidirected complete bipartite graph."""
from collections import Counter, deque
from functools import lru_cache

LEFT = (0, 1, 2)
RIGHT = (3, 4, 5)
ARCS = tuple(sorted([(i, j) for i in LEFT for j in RIGHT] +
                    [(j, i) for i in LEFT for j in RIGHT]))
ORDER = (7, 13, 2, 12, 5, 9, 10, 15, 6, 11, 16, 14, 1, 0, 8, 4, 3, 17)
assert len(ARCS) == 18 and sorted(ORDER) == list(range(18))


def admissible(mask):
    """Independent definition: degree constraints and no directed circuits."""
    succ = [-1] * 6
    prev = [-1] * 6
    for a, (u, v) in enumerate(ARCS):
        if mask & (1 << a):
            if succ[u] != -1 or prev[v] != -1:
                return False
            succ[u], prev[v] = v, u
    for v in range(6):
        seen = set()
        p = v
        while p != -1:
            if p in seen:
                return False
            seen.add(p)
            p = succ[p]
    return True


def independently_generated_faces():
    """Construct faces by extending directed vertex-disjoint paths."""
    result = set()

    def visit(pos, mask, outgoing, incoming, succ):
        if pos == len(ARCS):
            if mask:
                result.add(mask)
            return
        visit(pos + 1, mask, outgoing, incoming, succ)
        u, v = ARCS[pos]
        if outgoing & (1 << u) or incoming & (1 << v):
            return
        p = v
        while p != -1 and p != u:
            p = succ[p]
        if p == u:
            return
        arr = list(succ)
        arr[u] = v
        visit(pos + 1, mask | (1 << pos), outgoing | (1 << u),
              incoming | (1 << v), tuple(arr))

    visit(0, 0, 0, 0, (-1,) * 6)
    return result


def incidence(simplex):
    """Every signed codimension-one face, standard ascending arc ordering."""
    result = []
    pos = 0
    m = simplex
    while m:
        b = m & -m
        m ^= b
        if simplex != b:
            result.append((simplex ^ b, -1 if pos % 2 else 1))
        pos += 1
    return tuple(result)


def match(faces):
    unmatched = set(faces)
    pair = {}
    for a in ORDER:
        bit = 1 << a
        for s in sorted(unmatched):
            if s & bit:
                continue
            t = s | bit
            if t in unmatched:
                unmatched.remove(s)
                unmatched.remove(t)
                pair[s] = t
    return pair, unmatched


def check_dag(faces, pair):
    """Full oriented Hasse digraph, with each matched arrow reversed."""
    indeg = {s: 0 for s in faces}
    outgoing = {s: [] for s in faces}
    total = 0
    for t in faces:
        for s, _ in incidence(t):
            assert s in faces
            if pair.get(s) == t:
                u, v = s, t
            else:
                u, v = t, s
            outgoing[u].append(v)
            indeg[v] += 1
            total += 1
    q = deque([s for s, deg in indeg.items() if deg == 0])
    removed = 0
    while q:
        s = q.popleft()
        removed += 1
        for v in outgoing[s]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    assert removed == len(faces), (removed, len(faces))
    return total


def critical_boundary(pair, critical):
    """Exact signed gradient-path differential from critical 4-cells to critical 3-cells."""
    upper = {t for t in pair.values()}
    critical3 = {s for s in critical if s.bit_count() == 4}
    critical4 = [s for s in critical if s.bit_count() == 5]

    @lru_cache(None)
    def image(s):
        if s in critical3:
            return {s: 1}
        if s in upper:
            return {}
        if s not in pair:
            raise AssertionError(('unexpected lower chain', s))
        t = pair[s]
        boundary = incidence(t)
        unit = next(c for x, c in boundary if x == s)
        result = Counter()
        for x, c in boundary:
            if x == s:
                continue
            for v, a in image(x).items():
                result[v] -= unit * c * a
        return {v: a for v, a in result.items() if a}

    matrix = []
    for t in critical4:
        result = Counter()
        for s, c in incidence(t):
            for v, a in image(s).items():
                result[v] += c * a
        result = {v: a for v, a in result.items() if a}
        matrix.append(result)
    assert all(not row for row in matrix), matrix
    return len(matrix), len(critical3)


def mod_two_betti(faces):
    """Independent simplicial boundary reductions over the field with two elements."""
    by_size = {k: [] for k in range(1, 6)}
    for s in faces:
        by_size[s.bit_count()].append(s)
    for arr in by_size.values():
        arr.sort()
    ranks = {}
    for k in range(2, 6):
        lower_indices = {s: i for i, s in enumerate(by_size[k-1])}
        pivots = {}
        for s in by_size[k]:
            col = 0
            for t, _ in incidence(s):
                col ^= 1 << lower_indices[t]
            while col:
                pivot = col.bit_length() - 1
                if pivot in pivots:
                    col ^= pivots[pivot]
                else:
                    pivots[pivot] = col
                    break
        ranks[k] = len(pivots)
    return [len(by_size[k]) - ranks.get(k, 0) - ranks.get(k+1, 0)
            - (1 if k == 1 else 0) for k in range(1, 6)]


def main():
    faces = {s for s in range(1, 1 << 18) if admissible(s)}
    second_faces = independently_generated_faces()
    assert faces == second_faces
    counts = Counter(s.bit_count() - 1 for s in faces)
    assert [counts[i] for i in range(5)] == [18, 108, 264, 252, 72]
    pair, critical = match(faces)
    assert len(pair) == 341
    assert Counter(s.bit_count()-1 for s in critical) == {0: 1, 3: 19, 4: 12}
    incidences = check_dag(faces, pair)
    assert incidences == 2376
    cols, rows = critical_boundary(pair, critical)
    assert (cols, rows) == (12, 19)
    betti = mod_two_betti(faces)
    assert betti == [0, 0, 0, 19, 12], betti
    assert sum((-1)**k*counts[k] for k in counts) == 1-19+12
    print('VERIFY_OK arcs=18 faces=714 f_vector=(18,108,264,252,72)')
    print('VERIFY_OK incidences=2376 pairs=341 critical=(1_0,19_3,12_4) directed_acyclic=714')
    print('VERIFY_OK integral_Morse_differential_4_to_3=zero_19x12; GF2_betti=(0,0,0,19,12)')


if __name__ == '__main__':
    main()
