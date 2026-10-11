from itertools import combinations
from collections import Counter

V = tuple(range(7))
FACETS = set()
for i in V:
    FACETS.add(tuple(sorted((i, (i+2)%7, (i+3)%7))))
    FACETS.add(tuple(sorted((i, (i+1)%7, (i+3)%7))))
FACETS = set(FACETS)
EDGES = list(combinations(V, 2))
EIDX = {e:i for i,e in enumerate(EDGES)}


def boundary_triangle(t):
    m = 0
    for e in combinations(t, 2):
        m ^= 1 << EIDX[tuple(sorted(e))]
    return m


def basis_insert(basis, v):
    x = v
    while x:
        p = x.bit_length() - 1
        if p in basis:
            x ^= basis[p]
        else:
            basis[p] = x
            return True
    return False


def make_basis(vectors):
    b = {}
    for v in vectors:
        basis_insert(b, v)
    return b


def reduce_mod(v, basis):
    x = v
    for p in sorted(basis, reverse=True):
        if (x >> p) & 1:
            x ^= basis[p]
    return x


def rank(vectors):
    return len(make_basis(vectors))

face_boundaries = [boundary_triangle(t) for t in sorted(FACETS)]
B2 = make_basis(face_boundaries)
assert len(FACETS) == 14
assert len(EDGES) == 21
assert len(B2) == 13
cycle_rank = len(EDGES) - (len(V) - 1)
assert cycle_rank == 15
assert cycle_rank - len(B2) == 2

all_triples = list(combinations(V, 3))
empty = [t for t in all_triples if t not in FACETS]
assert len(empty) == 21
empty_classes = [reduce_mod(boundary_triangle(t), B2) for t in empty]
assert all(empty_classes)
class_counts = Counter(empty_classes)
assert len(class_counts) == 3
assert sorted(class_counts.values()) == [7, 7, 7]
assert rank(class_counts.keys()) == 2

layer_counts = {}
for k in range(8):
    c = Counter()
    for S in combinations(V, k):
        classes = [reduce_mod(boundary_triangle(t), B2) for t in combinations(S, 3)]
        r = rank(classes)
        c[r] += 1
        if k == 4:
            comp = tuple(sorted(set(V) - set(S)))
            assert (r == 2) == (comp in FACETS)
    layer_counts[k] = dict(sorted(c.items()))

expected = {
    0:{0:1},
    1:{0:7},
    2:{0:21},
    3:{0:14,1:21},
    4:{1:21,2:14},
    5:{2:21},
    6:{2:7},
    7:{2:1},
}
assert layer_counts == expected

print('VERIFY_OK H1dim=2 empty_triangles=21 classes=7,7,7 layers=0:0x1;1:0x7;2:0x21;3:0x14,1x21;4:1x21,2x14;5:2x21;6:2x7;7:2x1 complement4=face_iff_rank2 threshold=5')
