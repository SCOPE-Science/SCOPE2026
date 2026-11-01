#!/usr/bin/env python3
"""Exact regular-seven-tournament multipath homology certificate (Python + SymPy)."""
import collections
import itertools
import json
from functools import lru_cache
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

N = 7
PAIRS = list(itertools.combinations(range(N), 2))
EXPECTED = {
    17976: {'orbit': 720, 'faces': 2927, 'betti': [13, 43, 17], 'smith': {3: [1], 4: [1] * 18, 5: []}},
    22066: {'orbit': 1680, 'faces': 2923, 'betti': [12, 44, 15], 'smith': {3: [], 4: [1] * 11, 5: []}},
    85298: {'orbit': 240, 'faces': 2941, 'betti': [15, 38, 24], 'smith': {3: [1] * 3, 4: [1] * 18, 5: []}},
}


def tournament_arcs(mask):
    return sorted((i, j) if (mask >> k) & 1 else (j, i) for k, (i, j) in enumerate(PAIRS))


def regular_labeled_masks():
    results = set()
    def extend(k, mask, outdegree):
        if k == len(PAIRS):
            if outdegree == [3] * N:
                results.add(mask)
            return
        u, v = PAIRS[k]
        rem_u = sum(u in edge for edge in PAIRS[k + 1:])
        rem_v = sum(v in edge for edge in PAIRS[k + 1:])
        if outdegree[u] < 3 and outdegree[v] + rem_v >= 3:
            outdegree[u] += 1
            extend(k + 1, mask | (1 << k), outdegree)
            outdegree[u] -= 1
        if outdegree[v] < 3 and outdegree[u] + rem_u >= 3:
            outdegree[v] += 1
            extend(k + 1, mask, outdegree)
            outdegree[v] -= 1
    extend(0, 0, [0] * N)
    return results


def class_orbit(mask):
    arcs = set(tournament_arcs(mask))
    orbit = set()
    for p in itertools.permutations(range(N)):
        candidate = 0
        for k, (u, v) in enumerate(PAIRS):
            if (p[u], p[v]) in arcs:
                candidate |= 1 << k
        orbit.add(candidate)
    return orbit


def faces_by_edges(arcs):
    faces = set()
    def rec(k, mask, successor, predecessor):
        if k == len(arcs):
            faces.add(mask)
            return
        rec(k + 1, mask, successor, predecessor)
        u, v = arcs[k]
        if successor[u] != -1 or predecessor[v] != -1:
            return
        t = v
        while t != -1 and t != u:
            t = successor[t]
        if t == u:
            return
        successor[u], predecessor[v] = v, u
        rec(k + 1, mask | (1 << k), successor, predecessor)
        successor[u], predecessor[v] = -1, -1
    rec(0, 0, [-1] * N, [-1] * N)
    return faces


def faces_by_successors(arcs):
    choices = [[-1] for _ in range(N)]
    for u, v in arcs:
        choices[u].append(v)
    arc_index = {arc: i for i, arc in enumerate(arcs)}
    out = set()
    for successors in itertools.product(*choices):
        targets = [v for v in successors if v != -1]
        if len(set(targets)) != len(targets):
            continue
        mask = 0
        valid = True
        for u in range(N):
            visited = set()
            v = u
            while v != -1:
                if v in visited:
                    valid = False
                    break
                visited.add(v)
                v = successors[v]
            if not valid:
                break
        if valid:
            for u, v in enumerate(successors):
                if v != -1:
                    mask |= 1 << arc_index[u, v]
            out.add(mask)
    return out


def boundary(mask):
    for j, bit in enumerate(i for i in range(21) if (mask >> i) & 1):
        yield mask ^ (1 << bit), (-1 if j & 1 else 1)


def greedy_matching(faces):
    # Select disjoint pairs by adding each arc in fixed lexicographic order.
    unmatched = set(faces)
    pairs = []
    for i in range(21):
        bit = 1 << i
        for face in sorted(unmatched):
            if not (face & bit) and ((face | bit) in unmatched):
                unmatched.remove(face)
                unmatched.remove(face | bit)
                pairs.append((face, face | bit))
    # The augmented empty-face pair is replaced by a critical zero-cell.
    assert pairs[0][0] == 0
    selected_vertex = pairs[0][1]
    return pairs[1:], unmatched | {selected_vertex}


def assert_acyclic(faces, pairs):
    paired = {upper: lower for lower, upper in pairs}
    indegree = {face: 0 for face in faces if face}
    adj = {face: [] for face in faces if face}
    incidences = 0
    for upper in faces:
        if not upper:
            continue
        for lower, _ in boundary(upper):
            if not lower:
                continue
            if paired.get(upper) == lower:
                a, b = lower, upper
            else:
                a, b = upper, lower
            adj[a].append(b)
            indegree[b] += 1
            incidences += 1
    queue = collections.deque(a for a, d in indegree.items() if d == 0)
    checked = 0
    while queue:
        a = queue.popleft()
        checked += 1
        for b in adj[a]:
            indegree[b] -= 1
            if indegree[b] == 0:
                queue.append(b)
    assert checked == len(indegree), 'Morse matching contains a directed cycle'
    return incidences


def compute_morse_matrices(pairs, unmatched):
    low_to_high = dict(pairs)
    critical = collections.defaultdict(list)
    for face in unmatched:
        if face:
            critical[face.bit_count() - 1].append(face)
    for d in range(6):
        critical[d].sort()
    @lru_cache(maxsize=None)
    def descend(face):
        if face in unmatched:
            return {face: 1}
        if face not in low_to_high:
            return {}
        upper = low_to_high[face]
        pivot_bit = upper ^ face
        pivot_sign = -1 if (upper & (pivot_bit - 1)).bit_count() & 1 else 1
        result = collections.defaultdict(int)
        for lower, s in boundary(upper):
            if lower == face:
                continue
            for a, coeff in descend(lower).items():
                result[a] -= pivot_sign * s * coeff
        return {a: coeff for a, coeff in result.items() if coeff}
    matrices = {}
    for d in range(1, 6):
        target = critical[d - 1]
        rows = {f: i for i, f in enumerate(target)}
        matrix = sp.zeros(len(target), len(critical[d]))
        for j, face in enumerate(critical[d]):
            result = collections.defaultdict(int)
            for lower, s in boundary(face):
                for a, coeff in descend(lower).items():
                    result[a] += s * coeff
            for a, v in result.items():
                if v:
                    assert a in rows
                    matrix[rows[a], j] = v
        matrices[d] = matrix
    for d in range(2, 6):
        assert matrices[d - 1] * matrices[d] == sp.zeros(matrices[d - 1].rows, matrices[d].cols)
    return critical, matrices


def mod2_ranks_of_original(faces):
    by_size = {n: sorted(f for f in faces if f.bit_count() == n) for n in range(7)}
    ranks = {}
    for size in range(1, 7):
        idx = {face: i for i, face in enumerate(by_size[size - 1])}
        pivots = {}
        for face in by_size[size]:
            col = 0
            for lower, _ in boundary(face):
                col ^= 1 << idx[lower]
            while col:
                lead = col.bit_length() - 1
                if lead not in pivots:
                    pivots[lead] = col
                    break
                col ^= pivots[lead]
        ranks[size - 1] = len(pivots)
    betti = {d: len(by_size[d + 1]) - ranks[d] - ranks.get(d + 1, 0) for d in range(6)}
    # Reduced dimension 0: kernel of augmentation / image of boundary_1.
    betti[0] = len(by_size[1]) - ranks[0] - ranks[1]
    return ranks, betti


def main():
    labeled = regular_labeled_masks()
    assert len(labeled) == 2640
    orbits = [class_orbit(mask) for mask in EXPECTED]
    assert sum(map(len, orbits)) == 2640
    assert set.union(*orbits) == labeled
    assert all(orbits[i].isdisjoint(orbits[j]) for i in range(3) for j in range(i + 1, 3))
    record = {'total_regular_labeled': len(labeled), 'class_representatives': list(EXPECTED), 'cases': {}}
    for mask, expected in EXPECTED.items():
        assert len(class_orbit(mask)) == expected['orbit']
        arcs = tournament_arcs(mask)
        faces = faces_by_edges(arcs)
        assert faces == faces_by_successors(arcs)
        assert len(faces) == expected['faces']
        pairs, unmatched = greedy_matching(faces)
        assert len(faces) == 1 + 2 * len(pairs) + len(unmatched)  # empty face explicitly counted
        incidence_count = assert_acyclic(faces, pairs)
        critical, matrices = compute_morse_matrices(pairs, unmatched)
        ranks = {d: int(M.rank()) for d, M in matrices.items()}
        smith = {}
        for d, M in matrices.items():
            if not M.rows or not M.cols:
                smith[d] = []
                continue
            S = smith_normal_form(M, domain=ZZ)
            smith[d] = [abs(int(S[i, i])) for i in range(min(S.shape)) if S[i, i]]
        for d in range(1, 6):
            assert smith[d] == expected['smith'].get(d, [])
        betti = [len(critical[d]) - ranks.get(d, 0) - ranks.get(d + 1, 0) for d in (3, 4, 5)]
        assert betti == expected['betti']
        # Independent combinatorial count of cyclically oriented Hamiltonian cycles.
        arc_set = set(arcs)
        hamiltonian_cycles = sum(
            all((u, v) in arc_set for u, v in zip((0,) + perm, perm + (0,)))
            for perm in itertools.permutations(range(1, N))
        )
        assert hamiltonian_cycles == betti[2]
        mod2_ranks, mod2_betti = mod2_ranks_of_original(faces)
        assert [mod2_betti[d] for d in (3, 4, 5)] == betti
        assert all(mod2_betti.get(d, 0) == 0 for d in (0, 1, 2))
        result = {
            'orbit': expected['orbit'], 'aut_order': 5040 // expected['orbit'],
            'arcs': [list(a) for a in arcs], 'faces_including_empty': len(faces),
            'faces_by_dimension': {str(d): sum(f.bit_count() == d + 1 for f in faces) for d in range(6)},
            'morse_pairs': len(pairs), 'critical_cells': {str(d): len(critical[d]) for d in range(6)},
            'hasse_incidences': incidence_count, 'smith_by_boundary': {str(d): smith[d] for d in (3, 4, 5)},
            'mod2_original_ranks': {str(d): mod2_ranks[d] for d in sorted(mod2_ranks)},
            'reduced_integral_betti_345': betti, 'hamiltonian_cycles': hamiltonian_cycles,
            'critical_faces': {str(d): critical[d] for d in (2, 3, 4, 5)},
            'morse_matrices': {str(d): [[int(M[i, j]) for j in range(M.cols)] for i in range(M.rows)] for d, M in matrices.items() if d in (3, 4, 5)},
        }
        record['cases'][str(mask)] = result
        print('rep', mask, 'faces', len(faces), 'pairs', len(pairs), 'incidences', incidence_count,
              'betti', betti, 'smith', {d: smith[d] for d in (3, 4, 5)}, flush=True)
    outfile = Path(__file__).with_name('morse_certificate.json')
    if outfile.exists():
        saved = json.loads(outfile.read_text(encoding='utf-8'))
        assert saved == record, 'Morse certificate does not match independently recomputed data'
    else:
        outfile.write_text(json.dumps(record, separators=(',', ':'), sort_keys=True) + '\n', encoding='utf-8')
    print('ALL_THREE_REGULAR_TOURNAMENT_CLASSES_EXHAUSTIVE_INTEGRAL_HOMOLOGY_PASS')


if __name__ == '__main__':
    main()
