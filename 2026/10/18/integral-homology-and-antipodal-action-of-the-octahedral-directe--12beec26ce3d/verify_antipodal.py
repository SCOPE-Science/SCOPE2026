#!/usr/bin/env python3
"""Exact antipodal eigenspace dimensions using finite-field boundary certificates."""
from verify_complex import ARCS, build_faces, boundary

PERM = tuple(v ^ 1 for v in range(6))
MOD = 1009


def rank(columns):
    pivots = {}
    for c in columns:
        vec = {i: value % MOD for i, value in c.items() if value % MOD}
        while vec:
            k = max(vec)
            coefficient = vec[k]
            if k not in pivots:
                inv = pow(coefficient, -1, MOD)
                pivots[k] = {i: x * inv % MOD for i, x in vec.items()}
                break
            for i, x in pivots[k].items():
                y = (vec.get(i, 0) - coefficient * x) % MOD
                if y:
                    vec[i] = y
                else:
                    vec.pop(i, None)
    return len(pivots)


def main():
    faces = build_faces() - {0}
    levels = {k: sorted(f for f in faces if f.bit_count() == k + 1) for k in range(5)}
    index = {k: {f: i for i, f in enumerate(levels[k])} for k in levels}
    arcindex = {arc: i for i, arc in enumerate(ARCS)}
    action = {}
    chain_eigens = {}
    for k in levels:
        mapping, signs = [], []
        for f in levels[k]:
            old = [j for j in range(24) if f >> j & 1]
            new = [arcindex[PERM[ARCS[j][0]], PERM[ARCS[j][1]]] for j in old]
            mask = sum(1 << j for j in new)
            mapping.append(index[k][mask])
            signs.append(-1 if sum(new[i] > new[j] for i in range(len(new))
                                   for j in range(i + 1, len(new))) % 2 else 1)
        assert all(mapping[mapping[i]] == i and signs[i] * signs[mapping[i]] == 1
                   for i in range(len(mapping)))
        action[k] = (mapping, signs)
        tr = sum(signs[i] for i in range(len(mapping)) if mapping[i] == i)
        chain_eigens[k] = ((len(mapping) + tr) // 2, (len(mapping) - tr) // 2)
    assert chain_eigens == {
        0: (12, 12), 1: (90, 102), 2: (308, 308),
        3: (384, 360), 4: (120, 120)}
    print('chain_eigens:', chain_eigens)

    # Projection (1 ± antipodal) sends the full boundary image onto its ± part.
    ranks = {0: (0, 0), 5: (0, 0)}
    for d in range(1, 5):
        mapping, signs = action[d - 1]
        projected = [[], []]
        for f in levels[d]:
            b = {}
            for lo, s in boundary(f):
                b[index[d - 1][lo]] = s
            for parity in (1, -1):
                v = dict(b)
                for j, s in b.items():
                    i = mapping[j]
                    v[i] = (v.get(i, 0) + parity * signs[j] * s) % MOD
                projected[0 if parity == 1 else 1].append(v)
        ranks[d] = (rank(projected[0]), rank(projected[1]))
    assert ranks == {
        0: (0, 0), 1: (11, 12), 2: (79, 90),
        3: (227, 217), 4: (108, 100), 5: (0, 0)}
    # Totals agree with integral ranks deduced from the unit Morse matching,
    # hence the finite-field eigen-rank lower bounds are sharp over Q.
    assert [sum(ranks[d]) for d in (1, 2, 3, 4)] == [23, 169, 444, 208]
    print('boundary_image_eigens:', [ranks[d] for d in (1, 2, 3, 4)])
    homology = {d: (chain_eigens[d][0] - ranks[d][0] - ranks[d + 1][0],
                    chain_eigens[d][1] - ranks[d][1] - ranks[d + 1][1])
                for d in levels}
    assert homology == {0: (1, 0), 1: (0, 0), 2: (2, 1),
                        3: (49, 43), 4: (12, 20)}
    print('homology_eigens:', homology)
    print('RESULT: PASS')


if __name__ == '__main__':
    main()
