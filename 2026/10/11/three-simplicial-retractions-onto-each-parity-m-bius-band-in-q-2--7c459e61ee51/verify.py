from itertools import combinations


def complex_data(p):
    assert p >= 5 and p % 2 == 1
    n = 2 * p
    m = (p - 1) // 2
    facets = set()
    for i in range(n):
        facets.add(frozenset((i, (i + 1) % n, (i + 2) % n)))
        facets.add(frozenset((i, (i + 2) % n, (i + p + 1) % n)))
    return n, m, facets


def induced_parity(p, parity):
    n, m, facets = complex_data(p)
    verts = {v for v in range(n) if v % 2 == parity}
    subfacets = {f for f in facets if f <= verts}
    edges = set()
    edge_degree = {}
    for f in subfacets:
        for e in combinations(sorted(f), 2):
            e = frozenset(e)
            edges.add(e)
            edge_degree[e] = edge_degree.get(e, 0) + 1
    boundary = {e for e, d in edge_degree.items() if d == 1}
    return verts, subfacets, edges, boundary


def is_simplex(face, facets):
    face = frozenset(face)
    return any(face <= f for f in facets)


def brute_retractions(p, parity=0):
    n, m, facets = complex_data(p)
    target, _, _, _ = induced_parity(p, parity)
    a = [-1] * n
    for v in target:
        a[v] = v
    moving = [v for v in range(n) if v not in target]
    incident = [[] for _ in range(n)]
    for f in facets:
        for v in f:
            incident[v].append(f)

    count = 0
    maps = []
    def ok(v, val):
        for f in incident[v]:
            image = []
            for u in f:
                x = val if u == v else a[u]
                if x != -1:
                    image.append(x)
            if not is_simplex(image, facets):
                return False
        return True

    def rec(k=0):
        nonlocal count
        if k == len(moving):
            count += 1
            maps.append(tuple(a))
            return
        v = moving[k]
        for val in sorted(target):
            if ok(v, val):
                a[v] = val
                rec(k + 1)
                a[v] = -1
    rec()
    return count, maps


def formula_maps(p, parity=0):
    n = 2 * p
    out = []
    for mode in (-1, 1, p):
        a = list(range(n))
        for v in range(n):
            if v % 2 != parity:
                a[v] = (v + mode) % n
        out.append(tuple(a))
    return out


def check_formula_map(p, f):
    n, m, facets = complex_data(p)
    return all(is_simplex({f[v] for v in face}, facets) for face in facets)


def main():
    checked = []
    for p in (5, 7, 9, 11, 13, 15):
        n, m, facets = complex_data(p)
        assert len(facets) == 4 * p
        for parity in (0, 1):
            verts, subfacets, edges, boundary = induced_parity(p, parity)
            assert len(verts) == p
            assert len(subfacets) == p
            assert len(edges) == 2 * p
            assert len(boundary) == p
            assert len(verts) - len(edges) + len(subfacets) == 0
            # Boundary edges form one p-cycle: every boundary vertex has degree two.
            bddeg = {v: 0 for v in verts}
            for e in boundary:
                for v in e:
                    bddeg[v] += 1
            assert set(bddeg.values()) == {2}
            for f in formula_maps(p, parity):
                assert all(f[v] == v for v in verts)
                assert check_formula_map(p, f)
        checked.append(p)

    # Exhaustive retraction search on four family members.
    for p in (5, 7, 9, 11):
        for parity in (0, 1):
            count, maps = brute_retractions(p, parity)
            assert count == 3
            assert set(maps) == set(formula_maps(p, parity))

    # Symbolic local transition table for states 0,1,2.
    # At k=0, x_0 is 0,1,m+1 and x_1 is 1,2,m+2.
    for p in (5, 7, 9, 11, 13, 15, 17, 19):
        m = (p - 1) // 2
        target_facets = {frozenset((a % p, (a + 1) % p, (a + m + 1) % p)) for a in range(p)}
        opts0 = [0, 1, m + 1]
        opts1 = [1, 2, m + 2]
        transitions = set()
        for s, x in enumerate(opts0):
            for t, y in enumerate(opts1):
                if is_simplex({x % p, 1, y % p}, target_facets):
                    transitions.add((s, t))
        assert transitions == {(0,0),(1,0),(1,1),(1,2),(2,0),(2,2)}

    print("VERIFY_OK parity_bands=Mobius retractions_per_band=3 brute_p=5,7,9,11 symbolic_p_through=19")


if __name__ == "__main__":
    main()
