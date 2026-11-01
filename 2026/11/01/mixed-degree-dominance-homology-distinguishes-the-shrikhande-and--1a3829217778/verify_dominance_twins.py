"""Exact integral homology verification for two 16-vertex dominance complexes.

All arithmetic uses Python integers. No external packages or downloaded data.
Run: python3 verify_dominance_twins.py
"""
import collections
import hashlib
import heapq
import json

NVERT = 16
FULL = (1 << NVERT) - 1


def graphs():
    vertices = [(i, j) for i in range(4) for j in range(4)]
    shrikhande_steps = {(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)}
    result = {}
    for name in ("rook", "shrikhande"):
        adjacency = []
        for i, a in enumerate(vertices):
            neighbors = 0
            for j, b in enumerate(vertices):
                if name == "rook":
                    edge = i != j and (a[0] == b[0] or a[1] == b[1])
                else:
                    edge = ((b[0] - a[0]) % 4, (b[1] - a[1]) % 4) in shrikhande_steps
                if edge:
                    neighbors |= 1 << j
            adjacency.append(neighbors)
        for i in range(NVERT):
            assert adjacency[i].bit_count() == 6
            assert not (adjacency[i] >> i) & 1
            for j in range(i + 1, NVERT):
                assert bool(adjacency[i] & (1 << j)) == bool(adjacency[j] & (1 << i))
                assert (adjacency[i] & adjacency[j]).bit_count() == 2
        result[name] = adjacency
    return result


def faces_of_open_complement(adjacency):
    # Open neighborhoods in the graph complement have nine vertices each.
    closed = [adjacency[i] | 1 << i for i in range(NVERT)]
    facets = [FULL ^ c for c in closed]
    assert len(set(facets)) == NVERT
    assert all(f.bit_count() == 9 for f in facets)
    faces = {0}
    for facet in facets:
        sub = facet
        while True:
            faces.add(sub)
            if sub == 0:
                break
            sub = (sub - 1) & facet
    # Different membership test: a face belongs precisely when it misses
    # at least one closed neighborhood of the original graph.
    for mask in range(1 << NVERT):
        assert (mask in faces) == any((mask & c) == 0 for c in closed)
    return faces, closed


def independent_dominance_check(faces, closed):
    # A mask is in the dominance complex iff its complement dominates.
    dominance = {s for s in range(1 << NVERT) if all((s & c) != c for c in closed)}
    for s in range(1 << NVERT):
        assert (s in dominance) == ((FULL ^ s) not in faces)
    fv = collections.Counter(s.bit_count() - 1 for s in dominance)
    euler_reduced = sum(((-1) ** k) * v for k, v in fv.items())
    return len(dominance), dict(sorted(fv.items())), int(euler_reduced)


def face_vector(faces):
    return {k: v for k, v in sorted(collections.Counter(m.bit_count() - 1 for m in faces).items())}


def collapse(faces):
    active = set(faces) - {0}
    coface_counts = {m: 0 for m in active}
    for upper in active:
        z = upper
        while z:
            bit = z & -z
            z -= bit
            lower = upper ^ bit
            if lower in active:
                coface_counts[lower] += 1
    heap = [(m.bit_count(), m) for m in active if coface_counts[m] == 1]
    heapq.heapify(heap)
    pairs = []
    while heap:
        _, lower = heapq.heappop(heap)
        if lower not in active or coface_counts[lower] != 1:
            continue
        parents = [lower | (1 << v) for v in range(NVERT)
                   if not (lower >> v) & 1 and (lower | (1 << v)) in active]
        assert len(parents) == 1
        upper = parents[0]
        assert upper.bit_count() == lower.bit_count() + 1
        pairs.append((lower, upper))
        for gone in (lower, upper):
            active.remove(gone)
            z = gone
            while z:
                bit = z & -z
                z -= bit
                face = gone ^ bit
                if face in active:
                    coface_counts[face] -= 1
                    assert coface_counts[face] >= 0
                    if coface_counts[face] == 1:
                        heapq.heappush(heap, (face.bit_count(), face))
    assert 2 * len(pairs) + len(active) == len(faces) - 1
    assert not any(coface_counts[m] == 1 for m in active)
    return active, pairs


def signed_boundary(core):
    boundaries = {}
    cofaces = {face: {} for face in core}
    for upper in core:
        boundary = {}
        if upper.bit_count() > 1:
            bits = upper
            sign = 1
            while bits:
                bit = bits & -bits
                bits -= bit
                lower = upper ^ bit
                assert lower in core
                boundary[lower] = sign
                cofaces[lower][upper] = sign
                sign = -sign
        boundaries[upper] = boundary
    return boundaries, cofaces


def check_chain_complex(active, differential, transpose):
    for face in active:
        for lower, c in differential[face].items():
            assert lower in active
            assert face.bit_count() == lower.bit_count() + 1
            assert c != 0 and transpose[lower].get(face) == c
        for upper, c in transpose[face].items():
            assert upper in active and differential[upper].get(face) == c
    for upper in active:
        d2 = {}
        for middle, u in differential[upper].items():
            for lower, v in differential[middle].items():
                d2[lower] = d2.get(lower, 0) + u * v
        assert all(v == 0 for v in d2.values())


def integral_unit_reduction(core):
    active = set(core)
    d, co = signed_boundary(active)
    check_chain_complex(active, d, co)
    pairs = []
    max_coefficient = 1
    while True:
        options = []
        for lower in active:
            for upper, a in co[lower].items():
                if abs(a) == 1:
                    fill_cost = (len(co[lower]) - 1) * (len(d[upper]) - 1)
                    options.append((fill_cost, len(d[upper]) + len(co[lower]),
                                    lower.bit_count(), lower, upper))
        if not options:
            break
        _, _, _, lower, upper = min(options)
        pivot = d[upper][lower]
        assert abs(pivot) == 1
        original_column = d[upper]
        # Schur-complement cancellation of one integral unit incidence.
        for other_upper, coeff in list(co[lower].items()):
            if other_upper == upper:
                continue
            multiple = coeff * pivot
            for other_lower, val in original_column.items():
                new_val = d[other_upper].get(other_lower, 0) - multiple * val
                if new_val:
                    d[other_upper][other_lower] = new_val
                    co[other_lower][other_upper] = new_val
                    max_coefficient = max(max_coefficient, abs(new_val))
                else:
                    d[other_upper].pop(other_lower, None)
                    co[other_lower].pop(other_upper, None)
        # Remove the cancelled column, row, and their adjacent incidences.
        for other_lower in original_column:
            co[other_lower].pop(upper, None)
        for below in d[lower]:
            co[below].pop(lower, None)
        for other_upper in list(co[lower]):
            d[other_upper].pop(lower, None)
        for above in list(co[upper]):
            d[above].pop(upper, None)
        active.remove(upper)
        active.remove(lower)
        del d[upper], d[lower], co[upper], co[lower]
        pairs.append((lower, upper, pivot))
        if len(pairs) % 50 == 0:
            check_chain_complex(active, d, co)
    check_chain_complex(active, d, co)
    assert all(not d[x] for x in active)
    return active, pairs, max_coefficient


def mod2_betti(faces):
    bydim = collections.defaultdict(list)
    for face in faces:
        if face:
            bydim[face.bit_count() - 1].append(face)
    ranks = {}
    for k in sorted(bydim):
        if k <= 0:
            continue
        rows = {m: i for i, m in enumerate(sorted(bydim[k - 1]))}
        pivots = {}
        for upper in sorted(bydim[k]):
            column = 0
            sub = upper
            while sub:
                bit = sub & -sub
                sub -= bit
                column ^= 1 << rows[upper ^ bit]
            while column:
                leading = column.bit_length() - 1
                if leading not in pivots:
                    pivots[leading] = column
                    break
                column ^= pivots[leading]
        ranks[k] = len(pivots)
    betti = {k: len(bydim[k]) - ranks.get(k, 0) - ranks.get(k + 1, 0)
             for k in bydim}
    return ranks, betti


def run():
    output = {}
    for name, adj in graphs().items():
        faces, closed = faces_of_open_complement(adj)
        d_num, d_faces, d_euler = independent_dominance_check(faces, closed)
        core, collapse_pairs = collapse(faces)
        critical, algebra_pairs, max_coefficient = integral_unit_reduction(core)
        ranks, beta_mod2 = mod2_betti(faces)
        critical_vector = collections.Counter(x.bit_count() - 1 for x in critical)
        assert critical_vector[0] == 1
        integral_beta = {k: v for k, v in sorted(critical_vector.items()) if k > 0}
        for k, v in integral_beta.items():
            assert beta_mod2[k] == v
        assert all(v == 0 for k, v in beta_mod2.items() if k > 0 and k not in integral_beta)
        dual_beta = {NVERT - k - 3: v for k, v in integral_beta.items()}
        assert sum((-1) ** k * v for k, v in dual_beta.items()) == d_euler
        if name == 'rook':
            assert len(faces) == 5789 and len(collapse_pairs) == 2568
            assert len(core) == 652 and len(algebra_pairs) == 324
            assert integral_beta == {2: 2, 4: 1}
            assert dual_beta == {11: 2, 9: 1}
            assert d_num == 59747
        if name == 'shrikhande':
            assert len(faces) == 5717 and len(collapse_pairs) == 2322
            assert len(core) == 1072 and len(algebra_pairs) == 530
            assert integral_beta == {4: 11}
            assert dual_beta == {9: 11}
            assert d_num == 59819
        proof_pairs = collapse_pairs + [(l, u) for l, u, _ in algebra_pairs]
        pair_hash = hashlib.sha256(json.dumps(proof_pairs, separators=(',', ':')).encode()).hexdigest()
        output[name] = {
            'graph_vertices': NVERT,
            'graph_degree': 6,
            'open_complement_neighborhood_faces_including_empty': len(faces),
            'open_complement_neighborhood_face_vector': face_vector(faces),
            'elementary_collapse_pairs': len(collapse_pairs),
            'remaining_core_faces': len(core),
            'integral_unit_cancellation_pairs': len(algebra_pairs),
            'maximum_absolute_intermediate_boundary_coefficient': max_coefficient,
            'remaining_chain_generators_by_degree': dict(sorted(critical_vector.items())),
            'remaining_differential': 'zero',
            'neighborhood_reduced_integral_betti': integral_beta,
            'neighborhood_mod2_boundary_ranks': ranks,
            'dominance_faces_including_empty': d_num,
            'dominance_face_vector': d_faces,
            'dominance_reduced_euler_characteristic': d_euler,
            'dominance_reduced_integral_betti': dict(sorted(dual_beta.items())),
            'ordered_cancellation_pairs_sha256': pair_hash,
        }
    assert output['rook']['dominance_reduced_integral_betti'] != output['shrikhande']['dominance_reduced_integral_betti']
    print(json.dumps(output, indent=2, sort_keys=True))
    print('DOMINANCE_SHRIKHANDE_ROOK_EXACT_INTEGRAL_HOMOLOGY_OK')


if __name__ == '__main__':
    run()
