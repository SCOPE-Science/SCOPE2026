#!/usr/bin/env python3
"""Independent, standard-library-only exact checks for the perfect-matching complex of Q4.
Run: python3 q4_verifier.py. No downloads, input files, or optional packages needed.
"""
from collections import Counter, defaultdict, deque
import heapq

N = 16
EDGES = [(a, a ^ (1 << bit)) for a in range(N) for bit in range(4) if a < (a ^ (1 << bit))]
EDGE_ID = {edge: j for j, edge in enumerate(EDGES)}
ADJ = [tuple(a ^ (1 << bit) for bit in range(4)) for a in range(N)]


def perfect_matchings():
    def rec(remaining, matching):
        if remaining == 0:
            yield matching
            return
        lo = remaining & -remaining
        a = lo.bit_length() - 1
        for b in ADJ[a]:
            if remaining & (1 << b):
                e = (a, b) if a < b else (b, a)
                yield from rec(remaining ^ (1 << a) ^ (1 << b), matching | (1 << EDGE_ID[e]))
    return tuple(rec((1 << N) - 1, 0))


def all_faces(facets):
    out = {0}
    for facet in facets:
        s = facet
        while s:
            out.add(s)
            s = (s - 1) & facet
    return out


def toggle_certificate(faces):
    remaining = set(faces) - {0}
    partner = {}
    order = []
    for _ in range(len(EDGES)):
        choices = []
        for v in range(len(EDGES)):
            bit = 1 << v
            pairs = [(f, f | bit) for f in remaining if not f & bit and (f | bit) in remaining]
            choices.append((len(pairs), -v, v, pairs))
        pairs_n, _, v, pairs = max(choices, key=lambda x: (x[0], x[1]))
        if not pairs_n:
            break
        for a, b in pairs:
            assert a not in partner and b not in partner
            partner[a] = b
            partner[b] = a
            remaining.remove(a)
            remaining.remove(b)
        order.append(v)
    degree = {f: 0 for f in faces if f}
    arrows = defaultdict(list)
    incidence = 0
    for upper in degree:
        x = upper
        while x:
            bit = x & -x
            x -= bit
            lower = upper ^ bit
            if lower == 0:
                continue
            if partner.get(upper) == lower:
                a, b = lower, upper
            else:
                a, b = upper, lower
            arrows[a].append(b)
            degree[b] += 1
            incidence += 1
    queue = deque(v for v, d in degree.items() if d == 0)
    visited = 0
    while queue:
        x = queue.popleft()
        visited += 1
        for y in arrows[x]:
            degree[y] -= 1
            if degree[y] == 0:
                queue.append(y)
    assert visited == len(faces) - 1, 'Morse pairing contains a directed cycle'
    critical = Counter(face.bit_count() - 1 for face in remaining)
    assert critical == {0: 1, 3: 114, 4: 84, 5: 3}, critical
    assert len(partner) // 2 == 15179
    return critical, len(partner) // 2, incidence, tuple(order)


def simplicial_collapse(faces):
    live = set(faces)
    coface_count = Counter()
    only_coface = {}
    for upper in live:
        x = upper
        while x:
            bit = x & -x
            x -= bit
            sub = upper ^ bit
            coface_count[sub] += 1
            only_coface[sub] = upper if coface_count[sub] == 1 else None
    heap = [(-s.bit_count(), s) for s, n in coface_count.items() if n == 1 and s != 0]
    heapq.heapify(heap)
    removed_pairs = 0
    while heap:
        _, lower = heapq.heappop(heap)
        if lower not in live or coface_count[lower] != 1:
            continue
        upper = only_coface[lower]
        assert upper in live and lower & upper == lower and (upper ^ lower).bit_count() == 1
        live.remove(lower)
        live.remove(upper)
        for face in (lower, upper):
            x = face
            while x:
                bit = x & -x
                x -= bit
                sub = face ^ bit
                if sub not in live:
                    continue
                coface_count[sub] -= 1
                if coface_count[sub] == 1:
                    choices = [sub | (1 << i) for i in range(len(EDGES))
                               if not sub & (1 << i) and (sub | (1 << i)) in live]
                    assert len(choices) == 1
                    only_coface[sub] = choices[0]
                    heapq.heappush(heap, (-sub.bit_count(), sub))
                elif coface_count[sub] == 0:
                    only_coface[sub] = None
        removed_pairs += 1
    summary = Counter(f.bit_count() - 1 for f in live)
    assert removed_pairs == 10974
    assert summary == {-1: 1, 0: 32, 1: 397, 2: 2069, 3: 3925, 4: 2189}, summary
    return live, removed_pairs


def boundary_columns(degree, gens):
    columns = {}
    rows = gens[degree - 1]
    for upper in gens[degree]:
        x = upper
        sign = 1
        col = {}
        while x:
            bit = x & -x
            x -= bit
            sub = upper ^ bit
            if sub in rows:
                col[sub] = sign
            sign = -sign
        columns[upper] = col
    return columns


def unimodular_cancellation(columns):
    reverse = defaultdict(dict)
    for col, terms in columns.items():
        for row, value in terms.items():
            reverse[row][col] = value
    removed_rows = set()
    count = 0
    while True:
        pivot = None
        best = None
        for col, terms in columns.items():
            for row, value in terms.items():
                if abs(value) == 1:
                    quality = ((len(reverse[row]) - 1) * (len(terms) - 1),
                               len(terms) + len(reverse[row]), col, row)
                    if best is None or quality < best:
                        best = quality
                        pivot = (col, row)
        if pivot is None:
            break
        col, row = pivot
        eps = columns[col][row]
        top = dict(columns[col])
        others = dict(reverse[row])
        for other, coeff in others.items():
            if other == col:
                continue
            scalar = coeff // eps
            for i, value in top.items():
                if i == row:
                    continue
                new_value = columns[other].get(i, 0) - scalar * value
                if new_value:
                    columns[other][i] = new_value
                    reverse[i][other] = new_value
                else:
                    columns[other].pop(i, None)
                    reverse[i].pop(other, None)
            columns[other].pop(row, None)
        for i in top:
            reverse[i].pop(col, None)
        del columns[col]
        del reverse[row]
        removed_rows.add(row)
        count += 1
    assert all(not terms for terms in columns.values()), 'Uncancelled non-unit differential'
    return set(columns), removed_rows, count


def integral_certificate(live):
    gens = {d: {f for f in live if f.bit_count() - 1 == d} for d in range(5)}
    pivots = {}
    for degree in range(4, 0, -1):
        cols = boundary_columns(degree, gens)
        survivors, removed_rows, pivots[degree] = unimodular_cancellation(cols)
        gens[degree] = survivors
        gens[degree - 1] -= removed_rows
    expected = {0: 1, 1: 0, 2: 0, 3: 54, 4: 21}
    assert {d: len(gens[d]) for d in gens} == expected
    assert pivots == {4: 2168, 3: 1703, 2: 366, 1: 31}
    return expected, pivots


def main():
    pm = perfect_matchings()
    assert len(EDGES) == 32 and len(pm) == len(set(pm)) == 272
    faces = all_faces(pm)
    fvector = tuple(sum(f.bit_count() == k for f in faces) for k in range(1, 9))
    assert fvector == (32, 400, 2496, 7776, 10560, 6848, 2176, 272)
    assert len(faces) == 30561
    critical, matched, incidences, order = toggle_certificate(faces)
    remnant, simplicial_pairs = simplicial_collapse(faces)
    gen_counts, pivots = integral_certificate(remnant)
    print('Q4 graph vertices=16, edges=32; perfect matchings=272')
    print('Faces including empty=30561; f-vector=', fvector)
    print('Morse acyclic pairing: matched pairs=', matched,
          '; critical counts=', dict(sorted(critical.items())),
          '; Hasse incidences=', incidences)
    print('Elementary simplicial-collapse pairs=', simplicial_pairs,
          '; remaining faces including empty=', len(remnant))
    print('Exact unit cancellations by degree=', dict(sorted(pivots.items())),
          '; remaining integral chain generators=', dict(sorted(gen_counts.items())))
    print('CONCLUSION: H~_3=Z^54, H~_4=Z^21, all other H~=0; pi_1=pi_2=0.')
    print('ALL CHECKS PASSED')

if __name__ == '__main__':
    main()
