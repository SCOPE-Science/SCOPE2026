#!/usr/bin/env python3
"""Exact integral cup products in the six-vertex bidirected wheel complex.

The zero pairings on a complete top-dimensional integral homology basis,
together with the verified unit 3-to-2 Morse boundary and zero 4-to-3
boundary, determine its integral wedge-of-spheres homotopy type.
Only Python standard-library arithmetic is used.
"""
from collections import defaultdict
from functools import lru_cache
from verify_wheel_homology import (
    arcs_and_neighbours, enumerate_by_extension, greedy_matching,
    check_acyclicity, morse_chain_matrices, oriented_boundary,
    exact_unit_smith_rank,
)


def main():
    arcs, _ = arcs_and_neighbours(5)
    faces = enumerate_by_extension(arcs)
    pairs, critical = greedy_matching(faces, len(arcs))
    check_acyclicity(faces, pairs)
    bydegree, matrices = morse_chain_matrices(pairs, critical)
    assert {k: len(v) for k, v in bydegree.items()} == {2:12,3:33,4:10}
    assert exact_unit_smith_rank(matrices[3]) == 10
    assert exact_unit_smith_rank(matrices[4]) == 0
    lower_to_upper = dict(pairs)
    upper_cells = {y for x, y in pairs}

    # Two exact integer vectors spanning the rational left nullspace of d_3.
    # They were obtained by exact linear algebra, then checked below against
    # all columns. Since rank d_3=10 and these vectors are independent,
    # they give a rational basis of the full two-dimensional H^2.
    alpha = (-1, 0, 0, -1, 1, -1, 1, 1, 1, 0, 0, 0)
    beta = (0, -1, -1, 0, -1, 1, -1, 0, 0, 0, 0, 1)
    assert alpha != beta and any(a*b != a*a for a,b in zip(alpha,beta))
    for v in (alpha, beta):
        assert all(sum(v[i] * matrices[3][i][j] for i in range(12)) == 0
                   for j in range(33))

    @lru_cache(None)
    def project(face):
        if face in upper_cells:
            return {}
        if face not in lower_to_upper:
            return {face: 1}
        high = lower_to_upper[face]
        incidence = dict(oriented_boundary(high))[face]
        out = defaultdict(int)
        for z, sign in oriented_boundary(high):
            if z == face:
                continue
            for t, val in project(z).items():
                out[t] -= incidence * sign * val
        return {k: v for k, v in out.items() if v}

    pos = {c: i for i, c in enumerate(bydegree[2])}
    @lru_cache(None)
    def cochain(face, j):
        vec = (alpha, beta)[j]
        return sum(vec[pos[z]] * s for z,s in project(face).items())

    # Verify the pulled-back cochains are cocycles on EVERY 3-simplex.
    checked = 0
    for f in faces:
        if f.bit_count() == 4:
            checked += 1
            for j in range(2):
                assert sum(sign * cochain(low, j)
                           for low, sign in oriented_boundary(f)) == 0
    assert checked == 310  # 4 arcs = dimension 3

    def top_cycle(critical_top):
        chain = defaultdict(int, {critical_top: 1})
        boundary = defaultdict(int)
        for f, sign in oriented_boundary(critical_top):
            boundary[f] += sign
        while True:
            low = next((z for z, coef in boundary.items()
                        if coef and z in lower_to_upper), None)
            if low is None:
                break
            high = lower_to_upper[low]
            coeff = -boundary[low] * dict(oriented_boundary(high))[low]
            chain[high] += coeff
            for f, sign in oriented_boundary(high):
                boundary[f] += coeff * sign
        assert all(c == 0 for c in boundary.values())
        out = {z: c for z, c in chain.items() if c}
        assert out[critical_top] == 1
        assert all((c == critical_top or c not in critical)
                   for c in out)
        return out

    pairings = []
    lengths = []
    for top in bydegree[4]:
        cycle = top_cycle(top)
        lengths.append(len(cycle))
        this = []
        for i in range(2):
            for j in range(2):
                evaluation = 0
                for face, coefficient in cycle.items():
                    verts = [k for k in range(len(arcs)) if face & (1<<k)]
                    assert len(verts) == 5
                    first = sum(1 << k for k in verts[:3])
                    last = sum(1 << k for k in verts[2:])
                    evaluation += (coefficient * cochain(first, i)
                                   * cochain(last, j))
                this.append(evaluation)
        assert this == [0,0,0,0], this
        pairings.append(this)
    assert len(pairings) == 10
    print('critical_dimensions_2_3_4 12 33 10')
    print('unimodular_boundary_rank_3_to_2 10')
    print('boundary_rank_4_to_3 0')
    print('original_dimension_three_cocycle_checks',checked)
    print('top_integral_cycles',len(lengths),'support_sizes',lengths)
    print('cup_pairings_10_by_4',pairings)
    print('ALL_INTEGRAL_CUP_PAIRINGS_ZERO')


if __name__ == '__main__':
    main()
