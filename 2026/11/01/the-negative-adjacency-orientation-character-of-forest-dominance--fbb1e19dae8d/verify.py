"""Independent finite checks of forest dominance orientation characters.

Usage: python forest_dominance_verify.py
Assumptions: Python 3, networkx, numpy. This verifies finite examples, not the
all-forest theorem, which is established by the accompanying mathematical proof.
"""
import networkx as nx
import numpy as np
from collections import deque


def parity_sort(seq):
    return -1 if sum(x > y for i, x in enumerate(seq) for y in seq[i + 1:]) % 2 else 1


def minimum_covers(n, edges, m):
    return [mask for mask in range(1 << n)
            if mask.bit_count() == m and all(mask & ((1 << a) | (1 << b)) for a, b in edges)]


def matching_coefficient(mask, matching):
    selected = []
    sign = 1
    for a, b in matching:
        if mask & (1 << a):
            selected.append(a)
        else:
            assert mask & (1 << b)
            selected.append(b)
            sign = -sign
    return sign * parity_sort(selected)


def permutation_sign_on_cover(mask, p):
    selected = [i for i in range(len(p)) if mask & (1 << i)]
    return parity_sort([p[i] for i in selected])


def lefschetz_character(n, neighborhoods, p, m):
    seen, orbits = set(), []
    for v in range(n):
        if v in seen:
            continue
        u, orbit_mask = v, 0
        while u not in seen:
            seen.add(u)
            orbit_mask |= (1 << u)
            u = p[u]
        orbits.append(orbit_mask)
    alternating_sum = 0
    for u in range(1 << len(orbits)):
        subset = 0
        for j, orb in enumerate(orbits):
            if (u >> j) & 1:
                subset |= orb
        if not any((subset & N) == N for N in neighborhoods):
            alternating_sum += (-1) ** u.bit_count()
    # Reduced Lefschetz number is minus the alternating sum over invariant faces,
    # including the empty face. The only reduced group is in degree m-1.
    return (-1) ** m * alternating_sum


def connected_flip_graph(covers):
    if not covers:
        return True
    remaining = set(covers)
    todo = deque([covers[0]])
    remaining.remove(covers[0])
    while todo:
        c = todo.popleft()
        for d in list(remaining):
            if (c ^ d).bit_count() == 2:
                remaining.remove(d)
                todo.append(d)
    return not remaining


def check_case(G, p):
    n = len(G)
    assert sorted(G.nodes()) == list(range(n))
    edges = [tuple(sorted(e)) for e in G.edges()]
    m = len(nx.max_weight_matching(G, maxcardinality=True))
    if m == 0:
        return
    M = [tuple(sorted(e)) for e in sorted(nx.max_weight_matching(G, maxcardinality=True))]
    assert len(M) == m
    covers = minimum_covers(n, edges, m)
    assert len(covers) > 0
    assert connected_flip_graph(covers)
    nbh = [sum(1 << w for w in {v, *G.neighbors(v)}) for v in range(n)]
    M = sorted(M)
    c = covers[0]
    gc = sum(1 << p[i] for i in range(n) if c & (1 << i))
    cf, gf = matching_coefficient(c, M), matching_coefficient(gc, M)
    comb = permutation_sign_on_cover(c, p) * cf * gf
    direct = lefschetz_character(n, nbh, p, m)
    assert comb == direct, (n, edges, p, comb, direct)
    A = nx.to_numpy_array(G, nodelist=list(range(n)), dtype=float)
    eigenvalues, eigenvectors = np.linalg.eigh(A)
    neg = eigenvectors[:, eigenvalues < -1e-7]
    assert neg.shape[1] == m
    P = np.eye(n)[p, :]
    spectral = int(round(np.linalg.det(neg.T @ P @ neg)))
    assert spectral == direct, (n, edges, p, spectral, direct)
    # All minimum covers must compute the same global character.
    for c in covers:
        gc = sum(1 << p[i] for i in range(n) if c & (1 << i))
        val = (permutation_sign_on_cover(c, p)
               * matching_coefficient(c, M)
               * matching_coefficient(gc, M))
        assert val == comb


def main():
    num_graphs = num_actions = 0
    for n in range(2, 10):
        for T in nx.nonisomorphic_trees(n):
            T = nx.convert_node_labels_to_integers(T, ordering='sorted')
            automorphisms = nx.algorithms.isomorphism.GraphMatcher(T, T).isomorphisms_iter()
            count = 0
            for g in automorphisms:
                check_case(T, [g[i] for i in range(n)])
                num_actions += 1
                count += 1
                if count >= 5:
                    break
            num_graphs += 1
    # Example where a naive Hamming-distance sign formula fails: two disjoint edges,
    # endpoints interleaved in vertex order, with simultaneous endpoint flips.
    F = nx.Graph()
    F.add_nodes_from(range(4))
    F.add_edges_from([(0, 2), (1, 3)])
    check_case(F, [2, 3, 0, 1])
    num_graphs += 1
    num_actions += 1
    # Isolated vertices do not alter the nonzero homology character.
    F.add_node(4)
    check_case(F, [2, 3, 0, 1, 4])
    num_graphs += 1
    num_actions += 1
    print('checked_forests=', num_graphs)
    print('checked_automorphism_actions=', num_actions)
    print('checks: vertex covers, reconfiguration, integral facet characters,')
    print('        simplicial Lefschetz numbers, negative spectral determinants')
    print('ALL_CHECKS_PASS')


if __name__ == '__main__':
    main()
