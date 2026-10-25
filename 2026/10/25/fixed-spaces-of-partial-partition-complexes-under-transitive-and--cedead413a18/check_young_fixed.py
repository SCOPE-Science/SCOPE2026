"""Independent finite checks for Young-subgroup geometric fixed spaces.

Run: python3 check_young_fixed.py; no third-party modules.
The exhaustive tests cover specified small parameters, not the universal proof.
"""
from itertools import combinations
from math import comb
from check_fixed_points import partitions_of_partial_set, apply


def complex_faces(t):
    """Orbit complex with whole-macroblock vertices U_I and singleton-orbit vertices x_i."""
    vertices = [('U', mask, mask) for mask in range(1, 1 << t)] + [('x', i, 1 << i) for i in range(t)]
    out = []
    def rec(i, used, selected):
        if i == len(vertices):
            out.append(tuple(selected))
            return
        rec(i + 1, used, selected)
        if not (used & vertices[i][2]):
            selected.append(i)
            rec(i + 1, used | vertices[i][2], selected)
            selected.pop()
    rec(0, 0, [])
    return vertices, out


def rank_mod2(columns):
    pivots = {}
    for x in columns:
        while x:
            p = x.bit_length() - 1
            if p in pivots: x ^= pivots[p]
            else:
                pivots[p] = x
                break
    return len(pivots)


def reduced_mod2_betti(t):
    vertices, faces = complex_faces(t)
    by_dim = {}
    for face in faces:
        d = len(face) - 1
        by_dim.setdefault(d, []).append(face)
    dimmax = max(by_dim)
    bdranks = {}
    for d in range(0, dimmax + 1):
        lower = by_dim[d-1]
        rows = {face: j for j, face in enumerate(lower)}
        if d == 0:
            cols = [1 for _ in by_dim[0]]  # augmented boundary to degree -1
        else:
            cols = [sum(1 << rows[face[:i] + face[i+1:]] for i in range(len(face))) for face in by_dim[d]]
        bdranks[d] = rank_mod2(cols)
    return [len(by_dim[d]) - bdranks[d] - bdranks.get(d + 1, 0) for d in range(dimmax + 1)]


def nonsingleton_partition_counts(m):
    counts = {}
    if m == 0:
        counts[0] = 1
    for face in partitions_of_partial_set(m):
        if face and sum(face) == (1 << m) - 1 and all(x.bit_count() >= 2 for x in face):
            counts[len(face)] = counts.get(len(face), 0) + 1
    return counts


def expected_betti(t):
    counts = [nonsingleton_partition_counts(m) for m in range(t+1)]
    return [sum(comb(t,s) * counts[t-s].get(q-s+1, 0) for s in range(t+1)) for q in range(t)]


def young_orbit_faces(sizes):
    t = len(sizes)
    n = sum(sizes)
    starts = [sum(sizes[:i]) for i in range(t)]
    blocks = [set(range(starts[i], starts[i]+sizes[i])) for i in range(t)]
    generators = []
    for B in blocks:
        B = sorted(B)
        for a,b in zip(B,B[1:]):
            p = list(range(n)); p[a],p[b] = p[b],p[a]; generators.append(tuple(p))
    def macro_orbit_label(single_block):
        support = [i for i,B in enumerate(blocks) if any((single_block >> x)&1 for x in B)]
        if len(support) == 1 and single_block.bit_count() == 1:
            return ('x', support[0])
        if all(sum((single_block >> x)&1 for x in blocks[i]) == sizes[i] for i in support):
            return ('U', sum(1 << i for i in support))
        raise AssertionError('unexpected admissible vertex orbit')
    fixed_orbit_faces = set()
    fixed_raw_count = 0
    for F in partitions_of_partial_set(n):
        if not F or not all(frozenset(apply(g,b) for b in F)==frozenset(F) for g in generators):
            continue
        fixed_raw_count += 1
        labels = frozenset(macro_orbit_label(b) for b in F)
        fixed_orbit_faces.add(labels)
    vertices, model_faces = complex_faces(t)
    model = {frozenset((vertices[i][0],vertices[i][1]) for i in face) for face in model_faces}
    assert fixed_orbit_faces == model - {frozenset()}, (sizes,len(fixed_orbit_faces),len(model)-1)
    return fixed_raw_count, len(fixed_orbit_faces)


def main():
    for t in range(1, 6):
        observed = reduced_mod2_betti(t)
        predicted = expected_betti(t)
        assert observed == predicted, (t, observed, predicted)
        print(f'Orbit complex t={t}: Betti_GF2={observed}, Betti_formula={predicted}')
    for sizes in ((2,2),(2,3),(3,3),(2,2,2),(2,2,2,2)):
        actual, model = young_orbit_faces(sizes)
        assert actual == model
        print(f'Young subgroup sizes={sizes}: invariant_simplices={actual}, model_nonempty_faces={model}')
    print('PARTIAL_PARTITION_YOUNG_FIXED_VERIFIED')

if __name__=='__main__': main()
