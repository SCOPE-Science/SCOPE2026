"""Exact finite-rank certificate for scale-two Rips complexes of adjacent-swap permutation graphs.
Run: python3 verify_rips.py
Only the Python standard library is used. Every arithmetic operation is exact over F_2.
"""
import itertools
from collections import Counter

EXPECTED = {
    1: ((1,), ()),
    2: ((2, 1), (1,)),
    3: ((6, 12, 8), (5, 7)),
    4: ((24, 96, 112, 30), (23, 73, 30)),
    5: ((120, 780, 1320, 690, 120), (119, 661, 570, 120)),
    6: ((720, 6840, 15360, 12060, 4320, 720), (719, 6121, 8370, 3600, 720)),
}

MAXIMAL_CLIQUE_SIZE_COUNTS = {
    1:{1:1}, 2:{2:1}, 3:{3:8},
    4:{3:16,4:30}, 5:{3:120,4:90,5:120},
    6:{3:960,4:1260,6:720},
}

def permutations_and_square_graph(n):
    perms = list(itertools.permutations(range(n)))
    index = {p: i for i, p in enumerate(perms)}
    graph = [set() for _ in perms]
    for i, p in enumerate(perms):
        for j in range(n - 1):
            q = list(p)
            q[j], q[j + 1] = q[j + 1], q[j]
            k = index[tuple(q)]
            graph[i].add(k)
            graph[k].add(i)
    graph2 = [set(v) for v in graph]
    for i, neigh in enumerate(graph):
        graph2[i].update(j for k in neigh for j in graph[k])
        graph2[i].discard(i)
    for i in range(len(graph2)):
        assert all(i in graph2[j] for j in graph2[i])
    return perms, graph2

def maximal_cliques(adjacency):
    # Bron-Kerbosch with pivoting. Neighbors are represented as vertex sets.
    out = []
    def visit(r, p, x):
        if not p and not x:
            out.append(tuple(sorted(r)))
            return
        u = max(p | x, key=lambda v: len(p & adjacency[v])) if p or x else None
        for v in sorted(p - adjacency[u] if u is not None else p):
            visit(r + (v,), p & adjacency[v], x & adjacency[v])
            p.remove(v)
            x.add(v)
    visit((), set(range(len(adjacency))), set())
    return out

def faces_from_maximal_cliques(cliques):
    by_dim = {}
    for clique in cliques:
        for size in range(1, len(clique) + 1):
            by_dim.setdefault(size - 1, set()).update(itertools.combinations(clique, size))
    return [sorted(by_dim[k]) for k in sorted(by_dim)]

def exact_boundary_rank(domain, target):
    """Rank of simplicial boundary over F_2, with deterministic pivot vectors."""
    index = {face: i for i, face in enumerate(target)}
    pivots = {}
    for simplex in domain:
        x = 0
        for i in range(len(simplex)):
            face = simplex[:i] + simplex[i + 1:]
            x ^= (1 << index[face])
        while x:
            j = x.bit_length() - 1
            if j in pivots:
                x ^= pivots[j]
            else:
                pivots[j] = x
                break
    return len(pivots)

def run(n):
    perm, adjacency = permutations_and_square_graph(n)
    cliques = maximal_cliques(adjacency)
    assert len(cliques) == len(set(cliques))
    assert dict(Counter(map(len,cliques))) == MAXIMAL_CLIQUE_SIZE_COUNTS[n]
    assert all(not (set(c) < set(d)) for i, c in enumerate(cliques) for d in cliques[i+1:]) if n<=3 else True
    faces = faces_from_maximal_cliques(cliques)
    counts = tuple(map(len, faces))
    ranks = tuple(exact_boundary_rank(faces[k], faces[k-1]) for k in range(1,len(faces)))
    beta = tuple(counts[k] - (ranks[k-1] if k else 1) - (ranks[k] if k<len(ranks) else 0) for k in range(len(counts)))
    expected = EXPECTED[n]
    assert counts == expected[0], (n, counts, expected[0])
    assert ranks == expected[1], (n, ranks, expected[1])
    if n <= 5: assert (beta[3] if len(beta)>3 else 0) == 0
    if n == 6: assert beta == (0, 0, 869, 90, 0, 0)
    print('n',n,'maximal_cliques',len(cliques),'f',counts,'boundary_ranks',ranks,'reduced_betti',beta,flush=True)

if __name__ == '__main__':
    for n in range(1,7):run(n)
    print('EXACT_GF2_VERIFY_OK')
