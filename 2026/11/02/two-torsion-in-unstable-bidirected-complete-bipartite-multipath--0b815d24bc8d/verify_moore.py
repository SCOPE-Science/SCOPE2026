#!/usr/bin/env python3
"""Exact integer discrete-Morse verification of bidirected K_{2,n} multipath complexes.

Pure Python 3 standard library; run: python3 verify_moore.py
All arc masks, face incidences, and integral Morse coefficients are reconstructed.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations
from math import gcd
from functools import reduce


def arcs_of(n):
    return ([(a, b) for a in range(2) for b in range(2, n + 2)]
            + [(b, a) for a in range(2) for b in range(2, n + 2)])


def is_multipath(indices, arcs):
    outgoing, incoming, successor = set(), set(), {}
    for i in indices:
        a, b = arcs[i]
        if a in outgoing or b in incoming:
            return False
        outgoing.add(a); incoming.add(b); successor[a] = b
    for origin in successor:
        x, seen = origin, set()
        while x in successor and x not in seen:
            seen.add(x); x = successor[x]
        if x in seen:
            return False
    return True


def all_faces(n):
    arcs = arcs_of(n)
    by_dim = [[] for _ in range(4)]
    for size in range(1, 5):
        for inds in combinations(range(len(arcs)), size):
            if is_multipath(inds, arcs):
                by_dim[size - 1].append(sum(1 << i for i in inds))
    faces = set().union(*(set(a) for a in by_dim))
    # Any simplex has at most four arcs because the two left-side vertices
    # each have at most one outgoing and one incoming arc.
    assert all(all((F ^ (1 << i)) in faces for i in range(F.bit_length())
                   if F & (1 << i) and F.bit_count() > 1) for F in faces)
    return arcs, by_dim, faces


def boundary(F):
    bits = [1 << i for i in range(F.bit_length()) if F & (1 << i)]
    return [(F ^ bit, -1 if index % 2 else 1)
            for index, bit in enumerate(bits)]


def greedy_element_matching(faces, count):
    unmatched = set(faces)
    lower_to_upper = {}
    for i in range(count):
        bit = 1 << i
        # Disjoint pairs at each stage; the order of visiting is immaterial.
        for F in sorted(unmatched):
            if F & bit:
                continue
            larger = F | bit
            if larger in unmatched:
                unmatched.remove(F)
                unmatched.remove(larger)
                lower_to_upper[F] = larger
    assert 2 * len(lower_to_upper) + len(unmatched) == len(faces)
    assert not (set(lower_to_upper) & set(lower_to_upper.values()))
    return lower_to_upper, unmatched


def verify_hasse_acyclic(faces, matched):
    indegree = {F: 0 for F in faces}
    adjacent = defaultdict(list)
    count = 0
    for high in faces:
        if high.bit_count() == 1:
            continue
        for low, _ in boundary(high):
            assert low in faces
            if matched.get(low) == high:
                source, dest = low, high
            else:
                source, dest = high, low
            adjacent[source].append(dest)
            indegree[dest] += 1
            count += 1
    queue = deque(F for F, degree in indegree.items() if degree == 0)
    visited = 0
    while queue:
        v = queue.popleft()
        visited += 1
        for w in adjacent[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                queue.append(w)
    assert visited == len(faces), (visited, len(faces))
    return count


def verify_boundary_squared(by_dim):
    for level in range(2, len(by_dim)):
        for F in by_dim[level]:
            second = defaultdict(int)
            for lower, c in boundary(F):
                for lower2, c2 in boundary(lower):
                    second[lower2] += c * c2
            assert all(value == 0 for value in second.values())


def morse_chain_data(critical, lower_to_upper):
    upper_cells = set(lower_to_upper.values())

    @lru_cache(None)
    def project(cell):
        if cell in critical:
            return {cell: 1}
        if cell in upper_cells:
            return {}
        paired_upper = lower_to_upper[cell]
        incidence = dict(boundary(paired_upper))[cell]
        assert abs(incidence) == 1
        coefficients = defaultdict(int)
        for lower, sign in boundary(paired_upper):
            if lower == cell:
                continue
            for target, coefficient in project(lower).items():
                coefficients[target] -= incidence * sign * coefficient
        return {k: v for k, v in coefficients.items() if v != 0}

    differentials = {}
    for high in critical:
        if high.bit_count() == 1:
            continue
        result = defaultdict(int)
        for low, sign in boundary(high):
            for critical_low, coefficient in project(low).items():
                result[critical_low] += sign * coefficient
        differentials[high] = {k: v for k, v in result.items() if v != 0}
    assert all(all(high.bit_count() == low.bit_count() + 1
                   for low in cols) for high, cols in differentials.items())
    return differentials


def mod_rank(by_dim, dim, p):
    lower = {F: i for i, F in enumerate(by_dim[dim - 1])}
    pivots = {}
    for high in by_dim[dim]:
        vec = {lower[F]: c % p for F, c in boundary(high)}
        while vec:
            row = max(vec)
            if row not in pivots:
                inverse = pow(vec[row], -1, p)
                pivots[row] = {i: (v * inverse) % p
                               for i, v in vec.items()}
                break
            multiplier = vec[row]
            for i, v in pivots[row].items():
                new = (vec.get(i, 0) - multiplier * v) % p
                if new:
                    vec[i] = new
                else:
                    vec.pop(i, None)
    return len(pivots)


def check_n(n):
    arcs, by_dim, faces = all_faces(n)
    verify_boundary_squared(by_dim)
    matched, critical = greedy_element_matching(faces, len(arcs))
    incidence = verify_hasse_acyclic(faces, matched)
    diffs = morse_chain_data(critical, matched)
    histogram = dict(sorted(Counter(F.bit_count() - 1 for F in critical).items()))
    critical2 = sorted(F for F in critical if F.bit_count() == 3)
    critical3 = sorted(F for F in critical if F.bit_count() == 4)
    nonzero_entries = sorted(v for d in diffs.values() for v in d.values())
    gcd_coefficients = reduce(gcd, (abs(x) for x in nonzero_entries), 0)
    ranks2 = [mod_rank(by_dim, dim, 2) for dim in (1, 2, 3)]
    ranks3 = [mod_rank(by_dim, dim, 3) for dim in (1, 2, 3)]
    print(f'n={n} f={tuple(map(len, by_dim))} matched_pairs={len(matched)} '
          f'critical={histogram} hasse={incidence} Morse_nonzeros={len(nonzero_entries)} '
          f'Morse_gcd={gcd_coefficients} ranks2={ranks2} ranks3={ranks3}', flush=True)
    if n == 4:
        assert tuple(map(len, by_dim)) == (16, 80, 144, 72)
        assert histogram == {0: 1, 2: 8, 3: 1}
        assert len(nonzero_entries) == 6
        assert set(abs(a) for a in nonzero_entries) == {2}
        assert ranks2 == [15, 65, 71] and ranks3 == [15, 65, 72]
        assert incidence == 880
    if n == 5:
        assert tuple(map(len, by_dim)) == (20, 130, 320, 240)
        assert histogram == {0: 1, 2: 1, 3: 32}
        assert len(nonzero_entries) == 26
        assert gcd_coefficients == 2 and all(a % 2 == 0 for a in nonzero_entries)
        assert ranks2 == [19, 111, 208] and ranks3 == [19, 111, 209]
        assert incidence == 2180
    if n == 6:
        assert histogram == {0: 1, 3: 169}
        assert incidence == 4584
    if n == 3:
        assert histogram == {0: 1, 1: 1, 2: 6}
        assert not nonzero_entries
    if n == 2:
        assert histogram == {0: 1, 1: 3, 2: 2}
        assert not nonzero_entries
    return histogram, gcd_coefficients


def main():
    for n in range(1, 7):
        check_n(n)
    print('BIDIRECTED_K2N_TWO_TORSION_UNSTABLE_MODULE_MOORE_VERIFIED')


if __name__ == '__main__':
    main()
