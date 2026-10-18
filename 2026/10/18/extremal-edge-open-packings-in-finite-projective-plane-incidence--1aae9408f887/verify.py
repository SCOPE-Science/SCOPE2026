"""Finite checks for maximal edge-open packings of projective-plane incidence graphs.

Run: python verify.py
Requires Python 3.9+ and networkx for the independent exhaustive q=2,3 census.
Proof for arbitrary projective planes is given in RESULT.md, not in this script.
"""
from itertools import product
import networkx as nx


def pg2_prime(q):
    """Construct PG(2,q) for prime q by normalized nonzero vectors."""
    vectors = set()
    for a in product(range(q), repeat=3):
        if a == (0, 0, 0):
            continue
        pivot = next(x for x in a if x)
        inverse = pow(pivot, -1, q)
        vectors.add(tuple((x * inverse) % q for x in a))
    vectors = sorted(vectors)
    incidences = {(i, j) for i, p in enumerate(vectors) for j, line in enumerate(vectors)
                  if sum(x * y for x, y in zip(p, line)) % q == 0}
    return vectors, incidences


def valid_packing(selection, incidence):
    if not selection <= incidence:
        return False
    selected = sorted(selection)
    for i, (p, l) in enumerate(selected):
        for r, s in selected[i+1:]:
            if p != r and l != s and ((p, s) in incidence or (r, l) in incidence):
                return False
    return True


def canonical_packings(v, incidence):
    for line in range(v):
        yield frozenset((p, ell) for p, ell in incidence if p in {x for x in range(v) if (x, line) in incidence} and ell != line)
    for point in range(v):
        yield frozenset((p, ell) for p, ell in incidence if ell in {x for x in range(v) if (point, x) in incidence} and p != point)


def certify(q):
    vertices, incidence = pg2_prime(q)
    v = len(vertices)
    assert v == q*q + q + 1
    assert len(incidence) == v * (q+1)
    for p in range(v):
        assert sum(a == p for a, b in incidence) == q + 1
        assert sum(b == p for a, b in incidence) == q + 1
    for p in range(v):
        for t in range(p+1, v):
            assert sum((p, l) in incidence and (t, l) in incidence for l in range(v)) == 1
            assert sum((r, p) in incidence and (r, t) in incidence for r in range(v)) == 1
    constructions = set(canonical_packings(v, incidence))
    assert len(constructions) == 2*v
    assert all(len(S) == q*(q+1) and valid_packing(S, incidence) for S in constructions)
    print(f'PG(2,{q}): v={v}, incidences={len(incidence)}, explicit_optimal={len(constructions)}, edge_count={q*(q+1)}')
    if q > 3:
        return
    edges = sorted(incidence)
    compatibility = nx.Graph()
    compatibility.add_nodes_from(range(len(edges)))
    for i, (p, l) in enumerate(edges):
        for j, (r, s) in enumerate(edges[i+1:], i+1):
            if not (p != r and l != s and ((p, s) in incidence or (r, l) in incidence)):
                compatibility.add_edge(i, j)
    maximal = list(nx.find_cliques(compatibility))
    max_size = max(map(len, maximal))
    maximum_sets = {frozenset(edges[i] for i in ids) for ids in maximal if len(ids) == max_size}
    assert max_size == q*(q+1)
    assert maximum_sets == constructions
    assert len(maximum_sets) == 2*v
    print(f' exhaustive: maximal_sets={len(maximal)}, maximum_size={max_size}, maximum_sets={len(maximum_sets)}, exact_match=True')


if __name__ == '__main__':
    for q in (2, 3, 5, 7):
        certify(q)
    print('VERIFY_OK')
