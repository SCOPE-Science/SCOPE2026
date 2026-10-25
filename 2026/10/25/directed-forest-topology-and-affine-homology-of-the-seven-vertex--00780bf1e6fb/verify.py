#!/usr/bin/env python3
"""Reproduce the finite directed-forest and equivariant homology certificates."""
from collections import Counter, deque, defaultdict
from itertools import product

MOD = 7
STEPS = (1, 2, 4)
EDGES = tuple(sorted((u, (u + d) % MOD) for u in range(MOD) for d in STEPS))
EID = {e: i for i, e in enumerate(EDGES)}
HEAD = [tuple(i for i, (_, v) in enumerate(EDGES) if v == h) for h in range(MOD)]


def acyclic_parents(parent):
    # An indegree-at-most-one functional forest has no directed cycle iff
    # every reverse (parent) orbit terminates at a root.
    for u in range(MOD):
        seen = 0
        v = u
        while parent[v] != -1:
            if seen & (1 << v):
                return False
            seen |= 1 << v
            v = parent[v]
    return True


def all_faces():
    faces = set()
    for selection in product(*[(-1,) + bucket for bucket in HEAD]):
        parent = [-1] * MOD
        face = 0
        for h, edge_index in enumerate(selection):
            if edge_index != -1:
                face |= 1 << edge_index
                parent[h] = EDGES[edge_index][0]
        if acyclic_parents(parent):
            faces.add(face)
    return faces


def morse_matching(faces):
    alive = set(faces)
    pairs = {}
    # Deterministic elementary matchings in each coordinate. Every step
    # pairs only faces still present in the residual face poset.
    for i in range(len(EDGES)):
        bit = 1 << i
        for lower in sorted(alive, key=lambda mask: (mask.bit_count(), mask)):
            upper = lower | bit
            if lower in alive and not lower & bit and upper in alive:
                pairs[lower] = upper
                alive.remove(lower)
                alive.remove(upper)
    # Empty face does not belong to the ordinary simplicial Hasse diagram.
    assert 0 in pairs
    critical = alive | {pairs[0]}
    del pairs[0]
    indegree = {f: 0 for f in faces if f}
    out = defaultdict(list)
    incidences = 0
    for upper in faces:
        if not upper:
            continue
        for i in range(len(EDGES)):
            if not upper & (1 << i):
                continue
            lower = upper ^ (1 << i)
            if lower == 0:
                continue
            # Invert arrow precisely for matched face-coface incidences.
            src, dst = (lower, upper) if pairs.get(lower) == upper else (upper, lower)
            out[src].append(dst)
            indegree[dst] += 1
            incidences += 1
    queue = deque(f for f in indegree if indegree[f] == 0)
    processed = 0
    while queue:
        f = queue.popleft()
        processed += 1
        for g in out[f]:
            indegree[g] -= 1
            if indegree[g] == 0:
                queue.append(g)
    assert processed == len(faces) - 1, 'Acyclicity failed'
    return pairs, critical, incidences, processed


def equivariant_character(faces, multiplier, shift):
    assert multiplier in (1, 2, 4) and 0 <= shift < MOD
    perm = [EID[((multiplier * u + shift) % MOD,
                   (multiplier * v + shift) % MOD)] for u, v in EDGES]
    fixed_count = 0
    face_lefschetz = 0
    by_size = Counter()
    for face in faces:
        if not face:
            continue
        ids = [i for i in range(len(EDGES)) if face & (1 << i)]
        images = [perm[i] for i in ids]
        if sum(1 << i for i in images) != face:
            continue
        inversions = sum(x > y for p, x in enumerate(images) for y in images[p+1:])
        signed_action = -1 if inversions % 2 else 1
        face_lefschetz += ((-1) ** (len(ids) - 1)) * signed_action
        fixed_count += 1
        by_size[len(ids)] += 1
    # Reduced Lefschetz number = face_lefschetz - 1.
    # All reduced homology is degree five, hence character = 1 - face_lefschetz.
    return 1 - face_lefschetz, fixed_count, by_size



def root_tree_cofactor():
    # Directed matrix-tree theorem: delete one row and column of the
    # incoming-arc Laplacian to count spanning out-arborescences at that root.
    from fractions import Fraction
    lap = [[0] * MOD for _ in range(MOD)]
    for tail, head in EDGES:
        lap[head][head] += 1
        lap[head][tail] -= 1
    mat = [[Fraction(lap[i][j]) for j in range(1, MOD)]
           for i in range(1, MOD)]
    det = Fraction(1)
    for col in range(MOD - 1):
        row = next(k for k in range(col, MOD - 1) if mat[k][col])
        if row != col:
            mat[col], mat[row] = mat[row], mat[col]
            det = -det
        pivot = mat[col][col]
        det *= pivot
        for r in range(col+1, MOD-1):
            factor = mat[r][col] / pivot
            for c in range(col, MOD-1):
                mat[r][c] -= factor * mat[col][c]
    assert det.denominator == 1
    return int(det)

def main():
    assert len(EDGES) == 21
    faces = all_faces()
    assert len(faces) == 10648
    f_vector = Counter(f.bit_count() - 1 for f in faces if f)
    assert [f_vector[i] for i in range(6)] == [21, 189, 931, 2646, 4116, 2744]
    assert sum((-1)**i * f_vector[i] for i in range(6)) == -511
    assert root_tree_cofactor() == 392
    assert f_vector[5] == 7 * root_tree_cofactor()
    pairs, critical, incidences, visited = morse_matching(faces)
    assert len(pairs) == 5067
    assert Counter(f.bit_count()-1 for f in critical) == {0:1, 5:512}
    assert incidences == 50799 and visited == 10647
    expected_counts = {(1, 0): 512, (1, 1): 1, (2, 0): -1}
    for multiplier in (1,2,4):
        for shift in range(MOD):
            value, fixed, by_size = equivariant_character(faces, multiplier, shift)
            expected = 512 if (multiplier, shift)==(1,0) else (1 if multiplier==1 else -1)
            assert value == expected, (multiplier,shift,value,expected)
            if multiplier==1 and shift:
                assert fixed == 0
            if multiplier != 1:
                assert fixed == 6 and by_size == {3:4, 6:2}
    # All rational irreducibles of the affine group (order 21) have
    # dimensions 1, 2 and 6, with class characters
    #                 identity  nontrivial C7  order3
    # trivial:           1           1           1
    # cyclotomic C3:     2           2          -1
    # C7-induced:        6          -1           0
    # Solve: 24*(1,1,1)+25*(2,2,-1)+73*(6,-1,0).
    assert 24 + 25*2 + 73*6 == 512
    assert 24 + 25*2 - 73 == 1
    assert 24 - 25 == -1
    print('f_vector=21,189,931,2646,4116,2744; total_nonempty=10647')
    print('matrix_tree_cofactor=392; spanning_out_trees=2744')
    print('morse_pairs=5067; critical=one_0_cell,512_5_cells')
    print('nonempty_hasse_incidences=50799; topological_sort=10647')
    print('affine_group_order=21; character=(512,1,-1); irreps=(24,25,73)')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
