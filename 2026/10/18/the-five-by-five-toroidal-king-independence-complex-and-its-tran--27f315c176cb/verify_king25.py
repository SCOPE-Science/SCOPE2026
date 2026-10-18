#!/usr/bin/env python3
"""Exact, standalone finite verification for the toroidal 5-by-5 king complex.

Run: python verify_king25.py
The adjacent JSON certificate is read without relying on external software.
"""
import collections
import itertools
import json
import pathlib

P = 5
VERTICES = tuple(range(P * P))


def vertex(r, c):
    return P * (r % P) + (c % P)


def adjacency():
    ans = []
    for v in VERTICES:
        r, c = divmod(v, P)
        mask = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if (dr, dc) != (0, 0):
                    mask |= 1 << vertex(r + dr, c + dc)
        ans.append(mask)
    return ans


def all_faces(neighbors):
    ans = set()

    def visit(face, candidates):
        if face:
            ans.add(face)
        while candidates:
            bit = candidates & -candidates
            candidates -= bit
            v = bit.bit_length() - 1
            visit(face | bit, candidates & ~neighbors[v])

    visit(0, (1 << (P * P)) - 1)
    return ans


def codimension_one(face):
    bits = face
    while bits:
        bit = bits & -bits
        bits -= bit
        if face ^ bit:
            yield face ^ bit


def verify_morse(faces, certificate):
    matches = [tuple(z) for z in certificate['matching_pairs']]
    critical = certificate['critical_faces']
    assert len(matches) == 634 and len(critical) == 142
    marked = set()
    matched_pairs = set()
    for lower, upper in matches:
        assert lower in faces and upper in faces
        assert lower & upper == lower and upper.bit_count() == lower.bit_count() + 1
        assert lower not in marked and upper not in marked
        marked.update((lower, upper))
        matched_pairs.add((lower, upper))
    assert len(marked) == 2 * len(matches)
    assert len(set(critical)) == len(critical)
    assert marked.isdisjoint(critical)
    assert marked | set(critical) == faces
    assert collections.Counter(f.bit_count() - 1 for f in critical) == {0: 1, 3: 141}

    # Standard gradient orientation: matched covers point upward, all other
    # codimension-one inclusions point downward. Acyclicity is checked on
    # every Hasse cover, not inferred from face counts.
    indegree = {f: 0 for f in faces}
    arrows = {f: [] for f in faces}
    edges = 0
    for upper in faces:
        for lower in codimension_one(upper):
            assert lower in faces
            source, target = ((lower, upper) if (lower, upper) in matched_pairs
                              else (upper, lower))
            arrows[source].append(target)
            indegree[target] += 1
            edges += 1
    frontier = [f for f in faces if indegree[f] == 0]
    seen = 0
    while frontier:
        f = frontier.pop()
        seen += 1
        for g in arrows[f]:
            indegree[g] -= 1
            if indegree[g] == 0:
                frontier.append(g)
    assert seen == len(faces), 'Gradient cycle found'
    return len(matches), edges, seen


def mod_two_rank(faces, size):
    lower = sorted(f for f in faces if f.bit_count() == size - 1)
    lookup = {f: i for i, f in enumerate(lower)}
    basis = {}
    for face in (f for f in faces if f.bit_count() == size):
        col = 0
        for small in codimension_one(face):
            col ^= (1 << lookup[small])
        while col:
            pivot = col.bit_length() - 1
            if pivot in basis:
                col ^= basis[pivot]
            else:
                basis[pivot] = col
                break
    return len(basis)


def translate_vertex(v, dr, dc):
    r, c = divmod(v, P)
    return vertex(r + dr, c + dc)


def lefschetz_for_translation(faces, dr, dc):
    red_lefschetz = -1  # empty face in reduced chain complex
    invariant = collections.Counter()
    for f in faces:
        old = [v for v in VERTICES if f & (1 << v)]
        new = [translate_vertex(v, dr, dc) for v in old]
        transformed = sum(1 << v for v in new)
        if transformed != f:
            continue
        inversion_count = sum(a > b for i, a in enumerate(new) for b in new[i + 1:])
        sign = -1 if inversion_count % 2 else 1
        red_lefschetz += (-1 if (len(old) % 2 == 0) else 1) * sign
        invariant[len(old)] += 1
    return red_lefschetz, dict(invariant)


def line(direction):
    r, c = direction
    return [(k * r % P, k * c % P) for k in range(P)]


def run():
    cert = json.loads(pathlib.Path(__file__).with_name('morse_certificate.json').read_text())
    faces = all_faces(adjacency())
    fvector = [sum(f.bit_count() == k for f in faces) for k in range(1, 6)]
    assert fvector == [25, 200, 600, 575, 10]
    assert len(faces) == 1410
    matching, cover_edges, acyclic_nodes = verify_morse(faces, cert)
    assert matching == 634 and acyclic_nodes == 1410
    ranks = [mod_two_rank(faces, sz) for sz in range(2, 6)]
    assert ranks == [24, 176, 424, 10]
    top = [f for f in faces if f.bit_count() == 5]
    predicted_top = set()
    for slope in (2, 3):
        for shift in range(5):
            predicted_top.add(sum(1 << vertex(row, slope * row + shift) for row in range(5)))
    assert set(top) == predicted_top

    traces = {}
    fixed_count = collections.Counter()
    for dr in range(P):
        for dc in range(P):
            lefs, invariant = lefschetz_for_translation(faces, dr, dc)
            trace = -lefs  # H_3 is the only nonzero reduced rational homology
            special = (dr != 0 and dc % P in ((2 * dr) % P, (3 * dr) % P))
            expected = 141 if (dr, dc) == (0, 0) else (-4 if special else 1)
            assert trace == expected, ((dr, dc), trace, expected)
            if (dr, dc) != (0, 0):
                assert invariant == ({5: 5} if special else {})
            traces[(dr, dc)] = trace
            fixed_count[trace] += 1
    assert fixed_count == {141: 1, -4: 8, 1: 16}

    quotient_lines = {}
    for direction in [(0, 1)] + [(1, s) for s in range(5)]:
        subgroup = line(direction)
        rank = sum(traces[e] for e in subgroup) // 5
        assert sum(traces[e] for e in subgroup) % 5 == 0
        expected = 25 if direction in ((1, 2), (1, 3)) else 29
        assert rank == expected
        quotient_lines[str(direction)] = rank
    full_quotient_rank = sum(traces.values()) // 25
    assert full_quotient_rank == 5 and sum(traces.values()) == 125
    print('vertices=25, faces=1410, f_vector=', fvector)
    print('critical_cells={dim0:1, dim3:141}, matched_pairs=', matching)
    print('gradient_cover_edges=', cover_edges, ', DAG_nodes_verified=', acyclic_nodes)
    print('mod2_boundary_ranks=', ranks)
    print('maximum_independent_faces=10 (two slope families)')
    print('translation_character_value_counts=', dict(sorted(fixed_count.items())))
    print('order5_quotient_H3_ranks=', quotient_lines)
    print('full_translation_quotient_H3_rank=', full_quotient_rank)
    print('ALL CHECKS PASS')


if __name__ == '__main__':
    run()
