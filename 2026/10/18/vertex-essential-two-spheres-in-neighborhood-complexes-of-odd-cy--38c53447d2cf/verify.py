"""Finite checks accompanying the odd-cycle Mycielskian neighborhood theorem.
The general statement is proved symbolically in RESULT.md; sample computation
is a reproducibility check and is not offered as an infinite proof.
Uses only Python's standard library.
"""
from itertools import combinations
from collections import Counter


def subfaces(facet):
    a = sorted(facet)
    for k in range(1, len(a) + 1):
        yield from combinations(a, k)


def rank_f2(columns):
    pivots = {}
    for col in columns:
        while col:
            j = col.bit_length() - 1
            if j in pivots:
                col ^= pivots[j]
            else:
                pivots[j] = col
                break
    return len(pivots)


def betti_mod2(faces, vertices):
    vertset = set(vertices)
    groups = {}
    for f in faces:
        if set(f) <= vertset:
            groups.setdefault(len(f) - 1, []).append(f)
    assert 0 in groups
    maximum = max(groups)
    rank = {}
    for d in range(1, maximum + 1):
        lookup = {face: i for i, face in enumerate(groups[d - 1])}
        columns = []
        for f in groups.get(d, []):
            columns.append(sum(1 << lookup[f[:j] + f[j + 1:]]
                               for j in range(len(f))))
        rank[d] = rank_f2(columns)
    return tuple(len(groups.get(d, [])) - rank.get(d, 0)
                 - rank.get(d + 1, 0) - int(d == 0)
                 for d in range(maximum + 1))


def nerve(facets):
    out = set()
    for k in range(1, len(facets) + 1):
        for indices in combinations(range(len(facets)), k):
            intersection = set(facets[indices[0]])
            for i in indices[1:]:
                intersection.intersection_update(facets[i])
            if intersection:
                out.add(indices)
    return out


def check(n):
    assert n >= 5 and n % 2 == 1
    root = 2*n
    x = list(range(n))
    y = list(range(n, 2*n))
    F = [{(i-1)%n,(i+1)%n,n+(i-1)%n,n+(i+1)%n}
         for i in range(n)]
    Y = set(y)
    T = [{(i-1)%n,(i+1)%n,root} for i in range(n)]
    allfacets = F + [Y] + T
    faces = set(face for facet in allfacets for face in subfaces(facet))
    full_b = betti_mod2(faces, range(2*n+1))
    assert full_b[:3] == (0,0,1)
    assert not any(full_b[d] for d in range(3,len(full_b)))
    for deleted in (0,n,root):
        bs = betti_mod2(faces, set(range(2*n+1))-{deleted})
        assert all(v == 0 for v in bs), (n,deleted,bs)
    original_nerve = nerve(F+[Y]);removed_y_nerve = nerve(
        [facet-{n} for facet in F]+[Y-{n}])
    assert Counter(map(len, original_nerve)) == {1:n+1,2:2*n,3:n}
    assert Counter(map(len, removed_y_nerve)) == {1:n+1,2:2*n,3:n-1}
    step_two_edges = {tuple(sorted(((i-1)%n,(i+1)%n))) for i in range(n)}
    assert len(step_two_edges) == n
    deg = Counter(k for edge in step_two_edges for k in edge)
    assert set(deg) == set(x) and set(deg.values()) == {2}
    # The triangle omitted from the second nerve is exactly the triangle
    # with vertices (F_{-1}, F_{+1}, Y).
    tri0 = {f for f in original_nerve if len(f)==3}
    tri1 = {f for f in removed_y_nerve if len(f)==3}
    assert tri0-tri1 == {tuple(sorted(((n-1),1,n)))}
    return [len([f for f in faces if len(f)==d]) for d in range(1,n+2)]


if __name__ == '__main__':
    for n in (5,7,9,11):
        f = check(n)
        print('CHECK_OK',n,'VERTICES',2*n+1,'F_VECTOR',','.join(map(str,f)))
    print('VERIFY_OK ODD_CYCLE_NERVE_AND_HOMOLOGY_SAMPLES')
