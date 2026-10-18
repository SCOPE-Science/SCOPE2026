"""Exact, standard-library face and lattice checks for ASM(3)'s normal fan.

Run with: python3 VERIFY_COMPUTATION.py
All arithmetic is integer or rational. This verifies the finite face census and
lattice-cone certificates; the accompanying proof supplies their geometry.
"""
from fractions import Fraction
from itertools import combinations
from functools import reduce
from math import gcd

VERTICES = {
    "012": (1, 0, 0, 1),
    "021": (1, 0, 0, 0),
    "102": (0, 1, 1, 0),
    "120": (0, 1, 0, 0),
    "201": (0, 0, 1, 0),
    "210": (0, 0, 0, 1),
    "X":   (0, 1, 1, -1),
}


def determinant(a):
    n = len(a)
    if n == 0:
        return 1
    if n == 1:
        return a[0][0]
    return sum((-1)**j * a[0][j] * determinant(
        [r[:j]+r[j+1:] for r in a[1:]]) for j in range(n))


def rank(a):
    if not a:
        return 0
    b = [list(map(Fraction, row)) for row in a]
    r = 0
    for j in range(len(b[0])):
        i = next((i for i in range(r, len(b)) if b[i][j]), None)
        if i is None:
            continue
        b[r], b[i] = b[i], b[r]
        c = b[r][j]
        b[r] = [t/c for t in b[r]]
        for i in range(len(b)):
            if i != r and b[i][j]:
                c = b[i][j]
                b[i] = [x-c*y for x, y in zip(b[i], b[r])]
        r += 1
        if r == len(b):
            break
    return r


def primitive(v):
    d = reduce(gcd, (abs(x) for x in v), 0)
    assert d != 0
    return tuple(x//d for x in v)


def maximal_minor_gcd(rows):
    r = len(rows)
    if r == 0:
        return 1
    assert r <= 4
    return reduce(gcd, (
        abs(determinant([[row[j] for j in cols] for row in rows]))
        for cols in combinations(range(4), r)
    ), 0)


def facet_candidates():
    """Exhaust 4-vertex independent supports and orient primitive normals."""
    items = list(VERTICES.items())
    out = {}
    for four in combinations(items, 4):
        p = four[0][1]
        a = [[q-pq for q, pq in zip(v, p)] for _, v in four[1:]]
        if rank(a) != 3:
            continue
        normal = primitive([(-1)**j * determinant(
            [row[:j]+row[j+1:] for row in a]) for j in range(4)])
        vals = {name: sum(n*v for n, v in zip(normal, xy))
                for name, xy in items}
        val = vals[four[0][0]]
        if max(vals.values()) == val:
            pass
        elif min(vals.values()) == val:
            normal = tuple(-v for v in normal)
            vals = {name: -z for name, z in vals.items()}
            val = -val
        else:
            continue
        support = frozenset(name for name, z in vals.items() if z == val)
        out[support] = (normal, val)
    return out


def face_data(facets):
    """All faces are intersections of containing facets (including full P)."""
    supports = list(facets)
    sets = {frozenset(VERTICES)}
    for mask in range(1, 1 << len(supports)):
        verts = frozenset(VERTICES)
        for i, support in enumerate(supports):
            if (mask >> i) & 1:
                verts &= support
        if verts:
            sets.add(verts)
    out = {}
    for f in sets:
        p = VERTICES[sorted(f)[0]]
        dim = rank([[x-y for x, y in zip(VERTICES[name], p)]
                    for name in f if name != sorted(f)[0]])
        rays = [facets[support][0] for support in supports if f <= support]
        c = 4-dim
        assert rank(rays) == c
        smooth = len(rays) == c and maximal_minor_gcd(rays) == 1
        out[f] = (dim, rays, smooth)
    return out


def square_relation(rays):
    assert len(rays) == 4 and rank(rays) == 3
    cols = next(cols for cols in combinations(range(4), 3)
                if rank([[v[j] for j in cols] for v in rays]) == 3)
    m = [[v[j] for j in cols] for v in rays]
    r = primitive([(-1)**i * determinant(
        [row for j, row in enumerate(m) if j != i]) for i in range(4)])
    assert all(sum(r[i]*rays[i][j] for i in range(4)) == 0
               for j in range(4))
    assert sorted(r) == [-1, -1, 1, 1], r
    assert all(maximal_minor_gcd([rays[i] for i in inds]) == 1
               for inds in combinations(range(4), 3))
    return r


def main():
    # Explicit integral equivalence with the four-cycle stable-set polytope.
    x = VERTICES["X"]
    columns = [tuple(a-b for a, b in zip(VERTICES[key], x))
               for key in ("021", "102", "120", "201")]
    basis = [list(row) for row in zip(*columns)]
    assert abs(determinant(basis)) == 1
    def matvec(coeff):
        return tuple(x[i] + sum(columns[j][i]*coeff[j] for j in range(4))
                     for i in range(4))
    stable_vectors = [(0, 0, 0, 0)]
    stable_vectors += [tuple(int(i == j) for i in range(4)) for j in range(4)]
    stable_vectors += [(1, 1, 0, 0), (0, 0, 1, 1)]
    assert {matvec(v) for v in stable_vectors} == set(VERTICES.values())

    facets = facet_candidates()
    assert len(facets) == 8, len(facets)
    faces = face_data(facets)
    counts = {d: sum(dim == d for dim, rays, ok in faces.values())
              for d in range(5)}
    assert counts == {0: 7, 1: 17, 2: 18, 3: 8, 4: 1}, counts
    singular = {f: data for f, data in faces.items() if not data[2]}
    sing_counts = {d: sum(data[0] == d for data in singular.values())
                   for d in range(5)}
    assert sing_counts == {0: 6, 1: 5, 2: 0, 3: 0, 4: 0}, sing_counts
    maximal_singular = {f: data for f, data in singular.items()
                        if not any(f < f2 for f2 in singular)}
    expected = {frozenset(x) for x in
                (("012", "021"), ("012", "102"), ("012", "210"),
                 ("210", "120"), ("210", "201"))}
    assert set(maximal_singular) == expected
    assert {f for f, (d, _, ok) in singular.items() if d == 0} == {
        frozenset((x,)) for x in VERTICES if x != "X"}
    for f, (dim, rays, _) in maximal_singular.items():
        assert dim == 1
        square_relation(rays)
    print("VERIFY_OK")
    print("facets", len(facets))
    print("face_counts", counts)
    print("singular_face_counts", sing_counts)
    print("maximal_singular_edges",
          sorted("-".join(sorted(f)) for f in maximal_singular))
    print("all_five_transverse_cones: unit-square cones")


if __name__ == "__main__":
    main()
