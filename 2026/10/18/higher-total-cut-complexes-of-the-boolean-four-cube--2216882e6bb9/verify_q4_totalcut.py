#!/usr/bin/env python3
"""Exact finite certificates for the total-cut tower of the four-cube.

Usage: python3 verify_q4_totalcut.py certificate_q4_totalcut.json
Only Python 3's standard library is needed. The vertex x is the 4-bit
word x (integer 0,...,15). Edges join words at Hamming distance one.
"""
import collections
import hashlib
import itertools
import json
import sys

N = 16
UNIVERSE = (1 << N) - 1
ADJ = tuple(sum(1 << w for w in range(N) if (v ^ w).bit_count() == 1)
            for v in range(N))
EXPECTED = {4: (228, 58670, 529, 8),
            5: (128, 39958, 937, 6),
            6: (56, 17574, 441, 4),
            7: (16, 4526, 49, 2),
            8: (2, 510, 2, 0)}


def independence_numbers():
    # Dynamic programming using the include/exclude recurrence at the least bit.
    alpha = bytearray(1 << N)
    for mask in range(1, 1 << N):
        bit = mask & -mask
        v = bit.bit_length() - 1
        without = mask ^ bit
        yes = 1 + alpha[without & ~ADJ[v]]
        no = alpha[without]
        alpha[mask] = max(yes, no)
    assert alpha[UNIVERSE] == 8
    return alpha


def independent_ksets(k):
    out = []
    for vs in itertools.combinations(range(N), k):
        if all((ADJ[a] & (1 << b)) == 0
               for a, b in itertools.combinations(vs, 2)):
            out.append(sum(1 << v for v in vs))
    return out


def complex_faces(k, alpha, independent):
    by_duality = {face for face in range(1, 1 << N)
                  if alpha[UNIVERSE ^ face] >= k}
    by_facets = set()
    for iset in independent:
        facet = UNIVERSE ^ iset
        subset = facet
        while subset:
            by_facets.add(subset)
            subset = (subset - 1) & facet
    assert by_duality == by_facets, 'two face constructors disagree'
    return by_duality


def matching_and_acyclicity(faces):
    # Stagewise vertex matching, in the vertex order 0,...,15.
    # For a fixed stage, pair every currently free face s with s+{v}.
    remaining = set(faces)
    pair = [0] * (1 << N)
    matched_pairs = []
    for v in range(N):
        bit = 1 << v
        lower_faces = [s for s in remaining if not s & bit and s | bit in remaining]
        for s in lower_faces:
            t = s | bit
            assert pair[s] == 0 and pair[t] == 0
            assert s in remaining and t in remaining
            pair[s] = t
            pair[t] = s
            remaining.remove(s)
            remaining.remove(t)
            matched_pairs.append((s, t))
    critical = sorted(remaining)
    # Exhaustive independent acyclicity check on the full oriented Hasse graph.
    # An unmatched cover is directed downward; a matched cover upward.
    active = bytearray(1 << N)
    for s in faces:
        active[s] = 1
    indeg = [0] * (1 << N)
    covers = 0
    for t in faces:
        bits = t
        while bits:
            bit = bits & -bits
            bits ^= bit
            s = t ^ bit
            if not active[s]:
                continue
            covers += 1
            if pair[s] == t:
                indeg[t] += 1
            else:
                indeg[s] += 1
    queue = collections.deque(s for s in faces if indeg[s] == 0)
    visited = 0
    while queue:
        t = queue.popleft()
        visited += 1
        # All downward covers except the matched cover.
        bits = t
        while bits:
            bit = bits & -bits
            bits ^= bit
            s = t ^ bit
            if active[s] and pair[t] != s:
                indeg[s] -= 1
                assert indeg[s] >= 0
                if indeg[s] == 0:
                    queue.append(s)
        # The only upward cover is a matched pair, if t is its lower face.
        s = pair[t]
        if s and s.bit_count() == t.bit_count() + 1:
            indeg[s] -= 1
            assert indeg[s] >= 0
            if indeg[s] == 0:
                queue.append(s)
    assert visited == len(faces), f'acyclicity failed: {visited}/{len(faces)}'
    assert 2 * len(matched_pairs) + len(critical) == len(faces)
    c = collections.Counter(s.bit_count() - 1 for s in critical)
    digest = hashlib.sha256()
    for s, t in sorted(matched_pairs):
        digest.update(s.to_bytes(2, 'little') + t.to_bytes(2, 'little'))
    return {
        'number_faces': len(faces),
        'number_matched_pairs': len(matched_pairs),
        'number_cover_incidences': covers,
        'acyclicity_topological_nodes': visited,
        'critical_by_dimension': {str(d): v for d, v in sorted(c.items())},
        'critical_faces_as_bitmasks': critical,
        'matched_pairs_sha256': digest.hexdigest(),
    }


def full_certificate():
    alpha = independence_numbers()
    result = {'definitions': 'Q4 vertices are 0..15; an edge joins a pair whose XOR has popcount 1; total k-cut facets complement independent k-sets; 0 is not a nonempty face.',
              'checks': {}}
    for k in range(4, 9):
        independent = independent_ksets(k)
        faces = complex_faces(k, alpha, independent)
        m = matching_and_acyclicity(faces)
        m['number_independent_ksets'] = len(independent)
        count_ind, count_face, ncritical, d = EXPECTED[k]
        assert len(independent) == count_ind
        assert len(faces) == count_face
        if k < 8:
            assert m['critical_by_dimension'] == {'0': 1, str(d): ncritical}
        else:
            assert m['critical_by_dimension'] == {'0': 2}
        result['checks'][str(k)] = m
        print(f'k={k}: independent={len(independent)} faces={len(faces)} '
              f'covers={m["number_cover_incidences"]} pairs={m["number_matched_pairs"]} '
              f'critical={m["critical_by_dimension"]} DAG={m["acyclicity_topological_nodes"]}',
              flush=True)
    return result


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python3 verify_q4_totalcut.py certificate_q4_totalcut.json')
    produced = full_certificate()
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        expected = json.load(f)
    assert produced == expected, 'saved exact certificate differs'
    print('All exact finite certificates match and all oriented Hasse DAGs are acyclic.')
