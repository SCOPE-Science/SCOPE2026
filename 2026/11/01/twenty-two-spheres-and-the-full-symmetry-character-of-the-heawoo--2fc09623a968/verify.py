#!/usr/bin/env python3
"""Standalone exact finite certificate for a flag-complex homotopy and its symmetries."""
import collections
import itertools
import json
import os


def dot(p, q):
    return (p & q).bit_count() % 2


def apply_columns(cols, x):
    return (cols[0] if x & 1 else 0) ^ (cols[1] if x & 2 else 0) ^ (cols[2] if x & 4 else 0)


def matrices():
    for a, b, c in itertools.product(range(1, 8), repeat=3):
        if a != b and c not in (a, b, a ^ b):
            yield (a, b, c)


FLAGS = [(p, q) for p in range(1, 8) for q in range(1, 8) if dot(p, q) == 0]
N = len(FLAGS)
assert N == 21


def compatible(x, y):
    p, q = x
    r, s = y
    # Endpoint-disjoint edges without either possible cross-incidence.
    return p != r and q != s and dot(p, s) == 1 and dot(r, q) == 1


def direct_faces():
    faces = {()}
    for k in range(1, 5):
        for f in itertools.combinations(range(N), k):
            if all(compatible(FLAGS[i], FLAGS[j]) for i, j in itertools.combinations(f, 2)):
                faces.add(f)
    assert not any(len(f) == 4 for f in faces)
    return faces


def recursive_faces():
    masks = [0] * N
    for i in range(N):
        for j in range(i + 1, N):
            p, q = FLAGS[i]
            r, s = FLAGS[j]
            # Second test: induced bipartite endpoints have exactly two incidences.
            if len({p, r}) == 2 and len({q, s}) == 2 and sum(dot(a, b) == 0 for a in (p, r) for b in (q, s)) == 2:
                masks[i] |= 1 << j
                masks[j] |= 1 << i
    found = {()}
    def extend(seq, possible):
        while possible:
            bit = possible & -possible
            possible ^= bit
            i = bit.bit_length() - 1
            item = seq + (i,)
            found.add(item)
            extend(item, possible & masks[i])
    extend((), (1 << N) - 1)
    return found


def rank_mod_p(matrix, p):
    mat = [[x % p for x in row] for row in matrix]
    if not mat:
        return 0
    rows = len(mat)
    cols = len(mat[0])
    rank = 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if mat[r][col]), None)
        if pivot is None:
            continue
        mat[rank], mat[pivot] = mat[pivot], mat[rank]
        inv = pow(mat[rank][col], -1, p)
        for j in range(col, cols):
            mat[rank][j] = mat[rank][j] * inv % p
        for r in range(rank + 1, rows):
            factor = mat[r][col]
            if factor:
                for j in range(col, cols):
                    mat[r][j] = (mat[r][j] - factor * mat[rank][j]) % p
        rank += 1
        if rank == rows:
            break
    return rank


def verify_cell_certificate(faces, certificate):
    edges = set(f for f in faces if len(f) == 2)
    triangles = set(f for f in faces if len(f) == 3)
    tree = [tuple(x) for x in certificate['tree_edges']]
    cancellations = [tuple(x) for x in certificate['elimination_triangles']]
    assert len(tree) == 20 and len(set(tree)) == 20 and set(tree) <= edges
    assert len(cancellations) == 64 and len(set(cancellations)) == 64 and set(cancellations) <= triangles
    parent = list(range(N))
    def root(a):
        while parent[a] != a:
            a = parent[a]
        return a
    for u, v in tree:
        a, b = root(u), root(v)
        assert a != b
        parent[a] = b
    assert len({root(i) for i in range(N)}) == 1
    known = set(tree)
    for face in cancellations:
        three = set(itertools.combinations(face, 2))
        assert len(three & known) == 2
        new = three - known
        assert len(new) == 1
        known |= new
    assert known == edges
    leftover = triangles - set(cancellations)
    assert len(leftover) == 20
    assert [list(x) for x in sorted(leftover)] == certificate['remaining_triangles']
    return len(tree), len(cancellations), len(leftover)


def parity(perm):
    return -1 if sum(perm[i] > perm[j] for i in range(len(perm)) for j in range(i + 1, len(perm))) % 2 else 1


def verify_symmetry(faces):
    fplus = sorted(face for face in faces if face)
    idx = {f: i for i, f in enumerate(FLAGS)}
    matrices_list = list(matrices())
    assert len(matrices_list) == 168
    perms = []
    for cols in matrices_list:
        inverse_transpose = {
            q: next(s for s in range(1, 8) if all(dot(apply_columns(cols, p), s) == dot(p, q) for p in (1, 2, 4)))
            for q in range(1, 8)
        }
        for interchange in (False, True):
            mapping = [idx[(apply_columns(cols, q if interchange else p),
                            inverse_transpose[p if interchange else q])]
                       for p, q in FLAGS]
            assert len(set(mapping)) == N
            perms.append((tuple(mapping), interchange))
    assert len(set(x[0] for x in perms)) == 336
    face_set = set(fplus)
    chars = collections.Counter()
    by_type = collections.Counter()
    for mapping, interchange in perms:
        for face in fplus:
            assert tuple(sorted(mapping[v] for v in face)) in face_set
        reduced_lefschetz = -1
        for face in fplus:
            image = [mapping[v] for v in face]
            if sorted(image) != list(face):
                continue
            signed = parity([list(face).index(y) for y in image])
            reduced_lefschetz += (-1 if len(face) % 2 == 0 else 1) * signed
        chars[reduced_lefschetz] += 1
        by_type[(interchange, reduced_lefschetz)] += 1
    assert chars == collections.Counter({-4: 21, -1: 48, 0: 210, 2: 56, 20: 1}), chars
    assert sum(k * v for k, v in chars.items()) == 0
    assert sum(k * k * v for k, v in chars.items()) == 1008
    return chars, by_type


def verify():
    all_faces = direct_faces()
    assert all_faces == recursive_faces(), 'The two face tests disagree'
    count = collections.Counter(len(f) for f in all_faces)
    assert count == {0: 1, 1: 21, 2: 84, 3: 84}, count
    with open(os.path.join(os.path.dirname(__file__), 'cell_certificate.json'), encoding='utf-8') as fh:
        cert = json.load(fh)
    tree_count, eliminated, remaining = verify_cell_certificate(all_faces, cert)
    vertices = sorted(f for f in all_faces if len(f) == 1)
    edges = sorted(f for f in all_faces if len(f) == 2)
    triangles = sorted(f for f in all_faces if len(f) == 3)
    vi = {f: i for i, f in enumerate(vertices)}
    ei = {f: i for i, f in enumerate(edges)}
    b1 = [[0] * len(edges) for _ in vertices]
    b2 = [[0] * len(triangles) for _ in edges]
    for j, (u, v) in enumerate(edges):
        b1[vi[(u,)]][j] = -1
        b1[vi[(v,)]][j] = 1
    for j, (u, v, w) in enumerate(triangles):
        b2[ei[(v, w)]][j] = 1
        b2[ei[(u, w)]][j] = -1
        b2[ei[(u, v)]][j] = 1
    assert all(sum(b1[r][k] * b2[k][j] for k in range(len(edges))) == 0
               for r in range(len(vertices)) for j in range(len(triangles)))
    for p in (2, 3, 5):
        assert (rank_mod_p(b1, p), rank_mod_p(b2, p)) == (20, 64)
    chars, split_chars = verify_symmetry(all_faces)
    print('face_counts_by_size=1,21,84,84')
    print('CW_cancellations=tree:%d,one_cell_two_cell:%d,remaining_two_cells:%d' % (tree_count, eliminated, remaining))
    print('boundary_ranks_mod_2_3_5=20,64')
    print('homotopy=wedge_of_20_two_spheres')
    print('automorphisms=336')
    print('character_distribution=' + json.dumps(dict(sorted(chars.items())), sort_keys=True))
    print('bipartition_character_distribution=' + json.dumps({str(k): v for k, v in sorted(split_chars.items())}, sort_keys=True))
    print('invariant_homology_dimension=0')
    print('VERIFY_OK')

if __name__ == '__main__':
    verify()
