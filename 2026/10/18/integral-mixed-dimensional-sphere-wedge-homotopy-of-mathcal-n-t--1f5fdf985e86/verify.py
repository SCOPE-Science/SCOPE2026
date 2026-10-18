"""Exact finite simplicial-Morse certificate for the Lovasz neighborhood complex
of the triangular graph on the two-element subsets of a seven-element set.
All calculations use arbitrary-precision integers; no external packages.
"""
from collections import Counter, defaultdict, deque
from hashlib import sha256
from itertools import combinations
import json

N = 7
EDGES = list(combinations(range(N), 2))
VERTICES = len(EDGES)


def open_neighborhood_masks():
    result = []
    for e in EDGES:
        result.append(sum(1 << j for j, f in enumerate(EDGES)
                          if f != e and len(set(e).intersection(f)) == 1))
    return result


def all_faces_from_witnesses(witnesses):
    simplices = set()
    for nb in witnesses:
        sub = nb
        while sub:
            simplices.add(sub)
            sub = (sub - 1) & nb
    return sorted(simplices)


def alternating_boundary(simplex):
    original = simplex
    remainder = simplex
    position = 0
    while remainder:
        atom = remainder & -remainder
        yield original ^ atom, 1 if position % 2 == 0 else -1
        remainder ^= atom
        position += 1


def sequential_toggles(faces):
    unpaired = set(faces)
    pairs = []
    counts = Counter()
    for vertex in range(VERTICES):
        atom = 1 << vertex
        for low in sorted(unpaired):
            if low & atom or low not in unpaired:
                continue
            high = low | atom
            if high in unpaired:
                unpaired.remove(low)
                unpaired.remove(high)
                pairs.append((low, high))
                counts[vertex] += 1
    return pairs, unpaired, counts


def directed_hasse_toposort(faces, pairs):
    face_set = set(faces)
    matched_low_high = dict(pairs)
    indeg = {face: 0 for face in faces}
    arrows = defaultdict(list)
    incidences = 0
    for high in faces:
        if high.bit_count() <= 1:
            continue
        for low, _ in alternating_boundary(high):
            if low not in face_set:
                continue
            incidences += 1
            if matched_low_high.get(low) == high:
                a, b = low, high
            else:
                a, b = high, low
            arrows[a].append(b)
            indeg[b] += 1
    ready = deque(x for x in faces if indeg[x] == 0)
    order = []
    while ready:
        x = ready.popleft()
        order.append(x)
        for y in arrows[x]:
            indeg[y] -= 1
            if indeg[y] == 0:
                ready.append(y)
    assert len(order) == len(faces), 'matched Hasse orientation contains a cycle'
    return order, incidences


def exact_morse_boundary(pairs, critical, topological_order, source_dim):
    # For each critical source cell, eliminate all matched codimension-one
    # faces via signed unit-pivot cancellations in topological order.
    low_high = {lo: hi for lo, hi in pairs if lo.bit_count() == source_dim}
    elimination_order = [x for x in topological_order if x in low_high]
    targets = sorted(x for x in critical if x.bit_count() == source_dim)
    sources = sorted(x for x in critical if x.bit_count() == source_dim + 1)
    columns = []
    for source in sources:
        chain = defaultdict(int)
        for low, c in alternating_boundary(source):
            chain[low] += c
        for low in elimination_order:
            amount = chain.get(low, 0)
            if not amount:
                continue
            high = low_high[low]
            missing_bit = high ^ low
            assert missing_bit & (missing_bit - 1) == 0
            removal_index = (high & (missing_bit - 1)).bit_count()
            pivot_sign = 1 if removal_index % 2 == 0 else -1
            for term, c in alternating_boundary(high):
                chain[term] -= amount * pivot_sign * c
                if chain[term] == 0:
                    chain.pop(term, None)
        assert all(x in critical for x in chain)
        columns.append({str(x): c for x, c in sorted(chain.items()) if c})
    return targets, sources, columns



def independently_trace_gradient(pairs, critical, topological_order):
    """Different algorithm: recurse along gradient paths (memoized on the DAG).

    For each 3-simplex, compute its coefficient vector in the free group
    on critical 3-simplices. Recurrences are evaluated in reverse DAG order.
    Noncritical upper 3-simplices paired with 2-simplices project to zero.
    """
    lower_to_upper = {lo: hi for lo, hi in pairs if lo.bit_count() == 4}
    critical3 = {x for x in critical if x.bit_count() == 4}
    projections = {}
    for face in reversed(topological_order):
        if face.bit_count() != 4:
            continue
        if face in critical3:
            projections[face] = {face: 1}
        elif face not in lower_to_upper:
            projections[face] = {}
        else:
            high = lower_to_upper[face]
            missing = high ^ face
            pivot_sign = -1 if (high & (missing - 1)).bit_count() % 2 else 1
            terms = defaultdict(int)
            for gamma, coeff in alternating_boundary(high):
                if gamma == face:
                    continue
                assert gamma in projections, 'gradient order not topological'
                for target, val in projections[gamma].items():
                    terms[target] -= pivot_sign * coeff * val
            projections[face] = {target: v for target, v in terms.items() if v}
    output = []
    for source in sorted(x for x in critical if x.bit_count() == 5):
        result = defaultdict(int)
        for gamma, coeff in alternating_boundary(source):
            for target, val in projections[gamma].items():
                result[target] += coeff * val
        output.append({str(x): v for x, v in result.items() if v})
    return output


def digest_ints(values):
    return sha256(('\n'.join(str(x) for x in values) + '\n').encode()).hexdigest()


def main():
    witnesses = open_neighborhood_masks()
    assert VERTICES == 21
    assert len(set(witnesses)) == 21
    assert [w.bit_count() for w in witnesses] == [10] * 21
    faces = all_faces_from_witnesses(witnesses)
    face_set = set(faces)
    assert len(faces) == 18494
    # Independent membership definition, instead of only witness subset generation.
    # Check every one of the 2^21 candidate subsets.
    exhaustive_count = 0
    for mask in range(1, 1 << VERTICES):
        expected = any(mask & ~nb == 0 for nb in witnesses)
        actual = mask in face_set
        assert actual == expected, f'face mismatch: {mask}'
        exhaustive_count += expected
    assert exhaustive_count == len(faces)
    f_vector = [0] * 10
    for face in faces:
        f_vector[face.bit_count() - 1] += 1
    assert f_vector == [21, 210, 1190, 3780, 5187, 4410, 2520, 945, 210, 21]
    matching, critical, toggle_counts = sequential_toggles(faces)
    assert len(matching) == 9120 and len(critical) == 254
    assert len(critical) + 2 * len(matching) == len(faces)
    assert len(set(matching)) == len(matching)
    critical_counts = Counter(face.bit_count() - 1 for face in critical)
    assert critical_counts == {0: 1, 3: 246, 4: 7}
    topo, incidences = directed_hasse_toposort(faces, matching)
    assert incidences == 98805
    targets, sources, columns = exact_morse_boundary(matching, critical, topo, 4)
    assert len(targets) == 246 and len(sources) == 7
    assert columns == [{}] * 7, 'nontrivial integral attaching degree'
    gradient_columns = independently_trace_gradient(matching, critical, topo)
    assert gradient_columns == columns, 'two exact integer methods disagree'
    reduced_euler = sum((-1)**i * n for i, n in enumerate(f_vector)) - 1
    assert reduced_euler == -246 + 7
    stats = {
        'graph': 'T_7 = L(K_7)',
        'complex': 'Lovasz open-neighborhood complex',
        'vertices': 21,
        'full_subset_membership_checks': (1 << VERTICES) - 1,
        'simplices_nonempty': len(faces),
        'face_vector': f_vector,
        'hasse_incidences': incidences,
        'matching_pairs': len(matching),
        'critical_cells_by_dimension': {str(k): critical_counts[k] for k in sorted(critical_counts)},
        'integral_morse_boundary_4_to_3_nonzero_entries': sum(map(len, columns)),
        'integral_morse_boundary_columns': columns,
        'independent_gradient_path_boundary_columns': gradient_columns,
        'reduced_euler': reduced_euler,
        'faces_sha256': digest_ints(faces),
        'matched_pairs_sha256': digest_ints(f'{lo}:{hi}' for lo, hi in matching),
        'critical_sha256': digest_ints(sorted(critical)),
        'acyclic': True,
        'all_checks': 'PASS',
    }
    print(json.dumps(stats, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
