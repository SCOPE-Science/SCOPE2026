#!/usr/bin/env python3
from itertools import combinations, product


def has_clique(n, edges, k, subset_mask=None):
    if k <= 1:
        if subset_mask is None:
            return n >= 1
        return subset_mask != 0
    vertices = range(n) if subset_mask is None else [v for v in range(n) if (subset_mask >> v) & 1]
    if len(vertices) < k:
        return False
    E = edges
    for C in combinations(vertices, k):
        ok = True
        for i in range(k):
            for j in range(i + 1, k):
                a, b = C[i], C[j]
                if a > b:
                    a, b = b, a
                if (a, b) not in E:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            return True
    return False


def allowed_neighbor_masks(n, edges, r):
    # S is an admissible neighborhood for one new vertex in a K_r-free graph
    # iff A[S] has no K_{r-1}.
    out = []
    for mask in range(1 << n):
        if not has_clique(n, edges, r - 1, mask):
            out.append(mask)
    return out


def extension_is_kr_free(n, edges, r, mask):
    new_edges = set(edges)
    x = n
    for v in range(n):
        if (mask >> v) & 1:
            new_edges.add((v, x))
    return not has_clique(n + 1, new_edges, r)


def clique_free_subset_polynomial(n, edges, q):
    coeff = [0] * (n + 1)
    for mask in range(1 << n):
        if not has_clique(n, edges, q, mask):
            coeff[mask.bit_count()] += 1
    return coeff


def all_graphs(n):
    pairs = list(combinations(range(n), 2))
    for bits in range(1 << len(pairs)):
        E = {pairs[i] for i in range(len(pairs)) if (bits >> i) & 1}
        yield E


def bipartite_graphs(a, b):
    pairs = [(i, a + j) for i in range(a) for j in range(b)]
    for bits in range(1 << len(pairs)):
        E = {pairs[i] for i in range(len(pairs)) if (bits >> i) & 1}
        yield E


def join_with_clique(n, edges, c):
    # vertices 0..n-1 are the old graph, n..n+c-1 form K_c and join to all old vertices
    E = set(edges)
    clique = list(range(n, n + c))
    for u, v in combinations(clique, 2):
        E.add((u, v))
    for u in range(n):
        for v in clique:
            E.add((u, v))
    return n + c, E


def independent_set_count(n, edges):
    total = 0
    for mask in range(1 << n):
        if not has_clique(n, edges, 2, mask):
            total += 1
    return total


def verify_one_point_criterion():
    # Exhaustively check every K_r-free graph through n=5 for r=3,4,5.
    checked = 0
    for r in (3, 4, 5):
        for n in range(0, 6):
            for E in all_graphs(n):
                if has_clique(n, E, r):
                    continue
                allowed = set(allowed_neighbor_masks(n, E, r))
                direct = {mask for mask in range(1 << n) if extension_is_kr_free(n, E, r, mask)}
                assert allowed == direct, (r, n, E, allowed ^ direct)
                coeff = clique_free_subset_polynomial(n, E, r - 1)
                by_masks = [0] * (n + 1)
                for mask in allowed:
                    by_masks[mask.bit_count()] += 1
                assert coeff == by_masks
                checked += 1
    return checked


def verify_triangle_free_independence_polynomial():
    # For r=3, coefficients are exactly the independence polynomial coefficients.
    examples = {}
    for n in range(0, 7):
        for E in all_graphs(n):
            if has_clique(n, E, 3):
                continue
            coeff = clique_free_subset_polynomial(n, E, 2)
            assert sum(coeff) == independent_set_count(n, E)
    # C5: I(y)=1+5y+5y^2, total complete 1-types = 5+11=16.
    E_c5 = {(0,1),(1,2),(2,3),(3,4),(0,4)}
    coeff = clique_free_subset_polynomial(5, E_c5, 2)
    assert coeff == [1,5,5,0,0,0]
    assert 5 + sum(coeff) == 16
    examples['C5'] = (coeff, 16)
    # K_{2,3}: I(y)=1+5y+4y^2+y^3, also total = 16.
    E_k23 = {(i,j) for i in (0,1) for j in (2,3,4)}
    coeff = clique_free_subset_polynomial(5, E_k23, 2)
    assert coeff == [1,5,4,1,0,0]
    assert 5 + sum(coeff) == 16
    examples['K23'] = (coeff, 16)
    return examples


def verify_hardness_identity():
    # For every fixed r>=3 and bipartite B, with A=B join K_{r-3},
    # C_{r-1}(A;1)=(2^{r-3}-1)2^{|B|}+i(B).
    checked = 0
    for r in range(3, 8):
        c = r - 3
        for a in range(0, 4):
            for b in range(0, 4):
                n = a + b
                for E in bipartite_graphs(a, b):
                    N, Aedges = join_with_clique(n, E, c)
                    assert not has_clique(N, Aedges, r)
                    lhs = sum(clique_free_subset_polynomial(N, Aedges, r - 1))
                    rhs = ((1 << c) - 1) * (1 << n) + independent_set_count(n, E)
                    assert lhs == rhs, (r, a, b, E, lhs, rhs)
                    # Hence #IS(B) is exactly recovered from total type count:
                    total_types = N + lhs
                    recovered = total_types - N - ((1 << c) - 1) * (1 << n)
                    assert recovered == independent_set_count(n, E)
                    checked += 1
    return checked


def main():
    c1 = verify_one_point_criterion()
    ex = verify_triangle_free_independence_polynomial()
    c2 = verify_hardness_identity()
    print(f"one_point_instances={c1}")
    print(f"hardness_instances={c2}")
    print(f"examples={ex}")
    print("VERIFY_OK")


if __name__ == '__main__':
    main()
