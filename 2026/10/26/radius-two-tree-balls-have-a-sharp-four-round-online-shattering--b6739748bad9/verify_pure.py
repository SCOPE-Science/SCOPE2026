"""Independent, standard-library-only exact census for radius-two tree balls.
Run: python verify_pure.py (with WITNESS.json in the same directory).
All vertex labels are integers, from zero through the tree's order minus one.
"""
from collections import Counter
from functools import lru_cache
from pathlib import Path
import json


def canonical_tree(edges):
    """AHU centre-rooted code, unique for each unlabelled free tree."""
    n = len(edges) + 1
    neighbors = [set() for _ in range(n)]
    for u, v in edges:
        neighbors[u].add(v)
        neighbors[v].add(u)
    present = set(range(n))
    degrees = [len(x) for x in neighbors]
    while len(present) > 2:
        leaves = [v for v in present if degrees[v] <= 1]
        for v in leaves:
            present.remove(v)
        for v in leaves:
            for u in neighbors[v]:
                degrees[u] -= 1

    @lru_cache(None)
    def rooted(v, parent):
        children = sorted(rooted(u, v) for u in neighbors[v] if u != parent)
        return "(" + "".join(children) + ")"

    if len(present) == 1:
        return rooted(next(iter(present)), -1)
    u, v = sorted(present)
    a, b = rooted(u, v), rooted(v, u)
    return min(a + "|" + b, b + "|" + a)


def neighborhood_masks(edges):
    n = len(edges) + 1
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    radius_two = []
    for c in range(n):
        reached = {c} | adj[c]
        for u in adj[c]:
            reached |= adj[u]
        radius_two.append(sum(1 << v for v in reached))
    return radius_two


def exact_ldim(edges):
    n = len(edges) + 1
    concepts = list(dict.fromkeys(neighborhood_masks(edges)))
    query_bits = [sum(1 << i for i, c in enumerate(concepts) if (c >> q) & 1)
                  for q in range(n)]

    @lru_cache(None)
    def dimension(version):
        cap = version.bit_count().bit_length() - 1
        if cap == 0:
            return 0
        # A branch-and-bound shortcut does not alter the exhaustive recurrence.
        for q in query_bits:
            yes, no = version & q, version & ~q
            if yes and no and dimension(yes) >= cap - 1 and dimension(no) >= cap - 1:
                return cap
        return max((1 + min(dimension(version & q), dimension(version & ~q))
                    for q in query_bits if (version & q) and (version & ~q)), default=0)

    return dimension((1 << len(concepts)) - 1)


def check_witness(path):
    witness = json.loads(Path(path).read_text(encoding="utf-8"))
    edges = [tuple(edge) for edge in witness["edges"]]
    assert witness["radius"] == 2 and witness["vertices"] == len(edges) + 1 == 16
    assert len(set(tuple(sorted(e)) for e in edges)) == 15
    concepts = neighborhood_masks(edges)
    leaves = []

    def walk(node, constraints=()):
        if "center" in node:
            center = node["center"]
            assert 0 <= center < 16
            assert all(((concepts[center] >> q) & 1) == b for q, b in constraints)
            assert len(constraints) == 4
            leaves.append(center)
            return
        q = node["query"]
        assert 0 <= q < 16
        walk(node["zero"], constraints + ((q, 0),))
        walk(node["one"], constraints + ((q, 1),))

    walk(witness["tree"])
    assert len(leaves) == len(set(leaves)) == 16
    assert len(set(concepts)) == 16
    assert exact_ldim(edges) == 4
    print("WITNESS_OK depth=4 paths=16 centers=16")
    for case in witness["path_certificates"]:
        N = case["vertices"]
        E = [tuple(e) for e in case["edges"]]
        assert E == [(i, i + 1) for i in range(N - 1)]
        path_balls = neighborhood_masks(E)
        seen = []
        def verify(node, bits=()):
            if "center" in node:
                c = node["center"]
                assert all(((path_balls[c] >> q) & 1) == v for q, v in bits)
                assert len(bits) == case["depth"]
                seen.append(c)
                return
            q = node["query"]
            verify(node["zero"], bits + ((q, 0),))
            verify(node["one"], bits + ((q, 1),))
        verify(case["tree"])
        assert len(seen) == (1 << case["depth"])
        assert len(set(seen)) == len(seen)
        assert exact_ldim(E) == case["depth"]
        print("PATH_CERTIFICATE_OK", N, "depth", case["depth"])



def main():
    # Every tree of order n has a leaf; removing it produces an (n-1)-tree.
    # Attach a new leaf to each vertex of each representative and use the
    # centre-rooted AHU invariant to retain exactly one free-tree class.
    previous = [()]
    expected_totals = [1, 1, 2, 3, 6, 11, 23, 47, 106, 235,
                       551, 1301, 3159, 7741, 19320]  # orders 2,...,16
    for n in range(2, 17):
        unique = {}
        for edges in previous:
            for attach in range(n - 1):
                extended = edges + ((attach, n - 1),)
                key = canonical_tree(extended)
                if key not in unique:
                    unique[key] = extended
        previous = list(unique.values())
        assert len(previous) == expected_totals[n - 2], (n, len(previous))
        print("UNLABELLED_TREES", n, len(previous))
    census = Counter(exact_ldim(edges) for edges in previous)
    assert dict(census) == {0: 1, 1: 7, 2: 227, 3: 18516, 4: 569}, census
    print("LDIM_COUNTS_16", sorted(census.items()))
    check_witness(Path(__file__).with_name("WITNESS.json"))
    print("PURE_CENSUS_PASS")


if __name__ == "__main__":
    main()
