"""Exact checks for the open-neighborhood complex of the ternary three-cube.

Run with Python 3 (standard library only): python3 verify.py
Every mathematical object is reconstructed from coordinate adjacency.
"""
from collections import Counter, defaultdict, deque
from itertools import product

DIM = 3
ALPHABET = range(3)
MATCH_ORDER = (21, 11, 26, 18, 13, 1, 6, 20, 5, 10, 8, 24, 17,
               14, 16, 25, 22, 0, 19, 2, 4, 15, 12, 23, 3, 9, 7)


def vertices():
    return list(product(ALPHABET, repeat=DIM))


def facets_and_faces():
    vs = vertices()
    lookup = {v: i for i, v in enumerate(vs)}
    facets = []
    for v in vs:
        neighbors = set()
        for coord in range(DIM):
            for a in ALPHABET:
                if a != v[coord]:
                    w = v[:coord] + (a,) + v[coord + 1:]
                    neighbors.add(lookup[w])
        assert len(neighbors) == 6
        facets.append(sum(1 << j for j in neighbors))
    faces = set()
    for facet in facets:
        a = facet
        while a:
            faces.add(a)
            a = (a - 1) & facet
    return facets, faces


def stage_matching(faces):
    remain = set(faces)
    matching = []
    for vertex in MATCH_ORDER:
        a = 1 << vertex
        for face in sorted(tuple(remain)):
            upper = face | a
            if face & a == 0 and face in remain and upper in remain:
                matching.append((face, upper))
                remain.remove(face)
                remain.remove(upper)
    return matching, remain


def directed_face_dag(faces, matching):
    # For every codimension-one incidence, reverse its edge iff matched.
    directed = defaultdict(list)
    indegree = {s: 0 for s in faces}
    pairs = set(matching)
    incident = 0
    for upper in faces:
        bits = upper
        while bits:
            a = bits & -bits
            bits -= a
            lower = upper ^ a
            if lower not in faces:
                continue
            if (lower, upper) in pairs:
                src, dest = lower, upper
            else:
                src, dest = upper, lower
            directed[src].append(dest)
            indegree[dest] += 1
            incident += 1
    queue = deque(s for s, k in indegree.items() if k == 0)
    seen = 0
    while queue:
        s = queue.popleft()
        seen += 1
        for d in directed[s]:
            indegree[d] -= 1
            if indegree[d] == 0:
                queue.append(d)
    assert seen == len(faces), (seen, len(faces))
    return incident


def vertices_of(face):
    return tuple(i for i in range(27) if face & (1 << i))


def edge(a, b):
    return (1 << a) | (1 << b)


def tri_edges(face):
    a, b, c = vertices_of(face)
    return edge(a, b), edge(b, c), edge(a, c)


def reduce_word(*factors):
    stack = []
    for factor in factors:
        for letter in factor:
            if stack and stack[-1] == -letter:
                stack.pop()
            else:
                stack.append(letter)
    return tuple(stack)


def inverse(word):
    return tuple(-i for i in reversed(word))


def cyclic_reduce(word):
    a = list(word)
    while len(a) > 1 and a[0] == -a[-1]:
        a = a[1:-1]
    return tuple(a)


def maximal_tree(faces, matching):
    vertex_edge_pairs = [(lo, hi) for lo, hi in matching
                         if lo.bit_count() == 1]
    assert len(vertex_edge_pairs) == 26
    parent = list(range(27))

    def root(k):
        while parent[k] != k:
            k = parent[k]
        return k

    for v, e in vertex_edge_pairs:
        a, b = vertices_of(e)
        ra, rb = root(a), root(b)
        assert ra != rb, 'tree edges must not form a cycle'
        parent[ra] = rb
    assert len({root(i) for i in range(27)}) == 1
    return {hi for _, hi in vertex_edge_pairs}


def group_presentation(faces, matching, tree_edges):
    matched = {}
    for low, high in matching:
        matched[low] = high
        matched[high] = low
    critical_edges = sorted(f for f in faces if f.bit_count() == 2
                            and f not in matched)
    assert len(critical_edges) == 3
    symbols = {e: j + 1 for j, e in enumerate(critical_edges)}
    memo = {}
    active = set()

    def word(e):
        if e in memo:
            return memo[e]
        assert e not in active, 'recursive elimination is not well-founded'
        active.add(e)
        if e in symbols:
            w = (symbols[e],)
        elif e in tree_edges:
            w = ()
        else:
            t = matched[e]
            assert t.bit_count() == 3 and e.bit_count() == 2
            ab, bc, ac = tri_edges(t)
            if e == ab:
                w = reduce_word(word(ac), inverse(word(bc)))
            elif e == bc:
                w = reduce_word(inverse(word(ab)), word(ac))
            else:
                assert e == ac
                w = reduce_word(word(ab), word(bc))
        active.remove(e)
        memo[e] = w
        return w

    edges = sorted(e for e in faces if e.bit_count() == 2)
    assert len(edges) == 243
    assert len(tree_edges) == 26
    assert sum(e not in tree_edges and e not in symbols
               for e in edges) == 214
    assert len({e for e in edges if matched.get(e, 0).bit_count() == 3}) == 214
    for e in edges:
        word(e)
    relators = []
    for f in sorted(faces):
        if f.bit_count() == 3:
            ab, bc, ac = tri_edges(f)
            r = cyclic_reduce(reduce_word(word(ab), word(bc), inverse(word(ac))))
            relators.append(r)
    assert len(relators) == 540
    assert Counter(map(len, relators)) == {0: 485, 4: 30, 6: 21, 8: 4}
    # All relations lie in the commutator subgroup of the free group on 3 generators.
    for r in relators:
        for j in (1, 2, 3):
            assert r.count(j) == r.count(-j)
    # The three explicit relations force pairwise commutation.
    # The last one reduces to [generator 2, generator 1] after using the first two.
    witnesses = ((-3, -1, 3, 1), (-2, -3, 2, 3),
                 (-2, 3, -1, -3, 2, 1))
    for w in witnesses:
        assert w in relators, w
    return critical_edges, relators, witnesses


def rank_mod_two(columns):
    pivot = {}
    for original in columns:
        val = original
        while val:
            k = val.bit_length() - 1
            if k not in pivot:
                pivot[k] = val
                break
            val ^= pivot[k]
    return len(pivot)


def homology_mod_two(faces):
    by_dim = defaultdict(list)
    for f in faces:
        by_dim[f.bit_count() - 1].append(f)
    assert {d: len(c) for d, c in by_dim.items()} == {
        0: 27, 1: 243, 2: 540, 3: 405, 4: 162, 5: 27}
    boundary_rank = {-1: 0, 0: 0}
    for d in range(1, 6):
        low = {s: i for i, s in enumerate(sorted(by_dim[d - 1]))}
        cols = []
        for f in by_dim[d]:
            col = 0
            for v in vertices_of(f):
                col ^= 1 << low[f ^ (1 << v)]
            cols.append(col)
        boundary_rank[d] = rank_mod_two(cols)
    assert [boundary_rank[d] for d in range(1, 6)] == [26, 214, 270, 135, 27]
    betti = {d: len(by_dim[d]) - boundary_rank[d] -
             boundary_rank.get(d + 1, 0) for d in range(6)}
    assert betti == {0: 1, 1: 3, 2: 56, 3: 0, 4: 0, 5: 0}
    return betti


def main():
    facets, faces = facets_and_faces()
    assert len(facets) == 27 and len(set(facets)) == 27
    assert all((facets[i] & facets[j]).bit_count() <= 2
               for i in range(27) for j in range(i + 1, 27))
    assert len(faces) == 1404
    matching, critical = stage_matching(faces)
    assert len(matching) == 672
    assert Counter(f.bit_count() - 1 for f in critical) == {0: 1, 1: 3, 2: 56}
    assert len(critical) + 2 * len(matching) == len(faces)
    edges = maximal_tree(faces, matching)
    incidences = directed_face_dag(faces, matching)
    critical_edges, relators, witnesses = group_presentation(faces, matching, edges)
    assert critical_edges == [10240, 262146, 1050624]
    assert sum((-1) ** (f.bit_count() - 1) for f in faces) == 54
    betti = homology_mod_two(faces)
    print('VERIFY_OK faces=1404 pairs=672 critical=1x0+3x1+56x2'
          f' incidences={incidences} triangle_relators={len(relators)}'
          f' commutator_witnesses={len(witnesses)}'
          ' pi1=Z^3 integral_H2=Z^56 mod2_betti=' + str(betti))


if __name__ == '__main__':
    main()
