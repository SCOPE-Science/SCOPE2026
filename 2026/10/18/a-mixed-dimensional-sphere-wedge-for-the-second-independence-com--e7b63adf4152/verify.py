#!/usr/bin/env python3
"""Reproduce a finite simplicial homotopy calculation over the integers.

Requires Python 3 standard library only.  Vertices of the simplicial complex
are the 15 edges (i,j), 0<=i<j<6, in lexicographic order.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations
from math import factorial

EDGES = tuple(combinations(range(6), 2))
VERTICES = len(EDGES)
ORDER = (6, 12, 5, 4, 2, 7, 1, 0, 10, 11, 14, 8, 3, 13, 9)
ADJ = tuple(sum(1 << j for j, f in enumerate(EDGES)
                if i != j and set(e).intersection(f))
            for i, e in enumerate(EDGES))


def allowed_direct(mask):
    """Each vertex of the selected induced line graph has degree <= 1."""
    return all((mask & ADJ[i]).bit_count() <= 1
               for i in range(VERTICES) if mask & (1 << i))


def allowed_bfs(mask):
    """Independent definition using connected components, not degrees."""
    remaining = {i for i in range(VERTICES) if mask & (1 << i)}
    while remaining:
        initial = next(iter(remaining))
        reached = {initial}
        frontier = [initial]
        remaining.remove(initial)
        while frontier:
            i = frontier.pop()
            for j in list(remaining):
                if ADJ[i] & (1 << j):
                    remaining.remove(j)
                    reached.add(j)
                    frontier.append(j)
        if len(reached) > 2:
            return False
    return True


def boundary(face):
    """Integral oriented simplicial boundary, with increasing edge indices."""
    indices = [i for i in range(VERTICES) if face & (1 << i)]
    return {face ^ (1 << i): (-1 if position & 1 else 1)
            for position, i in enumerate(indices)}


def mod2_rank(columns):
    leading = {}
    for column in columns:
        while column:
            k = column.bit_length() - 1
            if k not in leading:
                leading[k] = column
                break
            column ^= leading[k]
    return len(leading)


def main():
    # Exhaust the entire 15-bit Boolean cube, including the empty simplex.
    allowed = []
    for face in range(1 << VERTICES):
        direct = allowed_direct(face)
        assert direct == allowed_bfs(face), ("membership", face)
        if direct and face:
            allowed.append(face)
    cells = set(allowed)
    f = Counter(face.bit_count() - 1 for face in allowed)
    assert tuple(f[d] for d in range(4)) == (15, 105, 195, 90)
    assert len(allowed) == 405

    # Independent enumerative count via partitions into isolated K2 and P3
    # components in the selected graph on 6 underlying vertices.
    counts = [0, 0, 0, 0, 0]
    for twos in range(4):
        for threes in range(3):
            if 2 * twos + 3 * threes > 6:
                continue
            occupied = 2 * twos + 3 * threes
            amount = (factorial(6) * 3**threes //
                      (2**twos * 6**threes * factorial(twos) *
                       factorial(threes) * factorial(6 - occupied)))
            counts[twos + 2 * threes] += amount
    assert counts == [1, 15, 105, 195, 90], counts

    # Successive element matchings, explicitly on the NONEMPTY face poset.
    unmatched = set(cells)
    pairs = {}
    for vertex in ORDER:
        for face in sorted(unmatched):
            if face & (1 << vertex):
                continue
            other = face | (1 << vertex)
            if other in unmatched:
                assert face in unmatched
                unmatched.remove(face)
                unmatched.remove(other)
                pairs[face] = other
    assert len(pairs) == 185
    critical = Counter(face.bit_count() - 1 for face in unmatched)
    assert critical == Counter({0: 1, 2: 24, 3: 10}), critical

    # Verify matching is acyclic by enumerating EVERY oriented Hasse incidence.
    # Nonmatched cover arrows point high->low, matched arrows point low->high.
    outgoing = defaultdict(list)
    incoming = {face: 0 for face in cells}
    incidence_count = 0
    for upper in allowed:
        for lower in boundary(upper):
            if not lower:
                continue
            incidence_count += 1
            source, dest = ((lower, upper) if pairs.get(lower) == upper
                            else (upper, lower))
            outgoing[source].append(dest)
            incoming[dest] += 1
    queue = deque(face for face in allowed if incoming[face] == 0)
    seen = 0
    while queue:
        current = queue.popleft()
        seen += 1
        for nxt in outgoing[current]:
            incoming[nxt] -= 1
            if incoming[nxt] == 0:
                queue.append(nxt)
    assert seen == len(allowed), "matching orientation has a directed cycle"
    assert incidence_count == 2*105 + 3*195 + 4*90 == 1155

    # Exact signed Morse boundary C_3^{crit} -> C_2^{crit}.
    # Eliminating each lower 2-face paired to a 3-face uses a unit coefficient.
    low2_to_high3 = {lo: hi for lo, hi in pairs.items()
                     if lo.bit_count() == 3}
    cache = {}
    working = set()
    def normal_form(triangle):
        if triangle in cache:
            return cache[triangle]
        if triangle not in low2_to_high3:
            cache[triangle] = {triangle: 1}
            return cache[triangle]
        assert triangle not in working, "cyclic gradient descent"
        working.add(triangle)
        upper = low2_to_high3[triangle]
        faces_of_upper = boundary(upper)
        sign = faces_of_upper[triangle]
        assert sign in (-1, 1)
        accum = defaultdict(int)
        for neighbor, coeff in faces_of_upper.items():
            if neighbor == triangle:
                continue
            for low, value in normal_form(neighbor).items():
                accum[low] -= sign * coeff * value
        working.remove(triangle)
        cache[triangle] = {x: c for x, c in accum.items() if c}
        return cache[triangle]

    critical2 = {face for face in unmatched if face.bit_count() == 3}
    critical3 = sorted(face for face in unmatched if face.bit_count() == 4)
    assert len(critical3) == 10
    nonzero = 0
    for cell in critical3:
        reduced = defaultdict(int)
        for term, coeff in boundary(cell).items():
            for low, value in normal_form(term).items():
                reduced[low] += coeff * value
        reduced = {t: c for t, c in reduced.items() if c}
        morsed = {t: c for t, c in reduced.items() if t in critical2}
        nonzero += len(morsed)
        assert not morsed, ("nonzero Morse boundary", cell, morsed)
    assert nonzero == 0

    # Independent direct (unreduced) simplicial boundary ranks over F_2.
    rank = {}
    for dimension in range(1, 4):
        lower = sorted(face for face in allowed if face.bit_count() == dimension)
        upper = sorted(face for face in allowed if face.bit_count() == dimension+1)
        location = {face: i for i, face in enumerate(lower)}
        columns = []
        for face in upper:
            col = 0
            for term in boundary(face):
                col ^= 1 << location[term]
            columns.append(col)
        rank[dimension] = mod2_rank(columns)
    assert rank == {1: 14, 2: 91, 3: 80}, rank
    assert f[2] - rank[2] - rank[3] == 24
    assert f[3] - rank[3] == 10

    # Number of actual 2-dimensional facets versus maximal 3-dimensional facets.
    facets = [face for face in allowed
              if all((face | 1 << j) not in cells
                     for j in range(VERTICES) if not (face & 1 << j))]
    assert Counter(face.bit_count()-1 for face in facets) == Counter({2: 15, 3: 90})
    print("TRIANGULAR_T6_HIGHER_INDEPENDENCE_HOMOTOPY_VERIFIED")
    print("faces=405 pairs=185 critical=(1,0,24,10) hasse=1155")
    print("integral_morse_boundary=0 mod2_betti=(0,0,24,10)")


if __name__ == '__main__':
    main()
