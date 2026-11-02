"""Exact finite checks for the effective secrecy-event counting theorem.

Run with: python checker.py
This finite test checks instances, not the asymptotic/infinite proof.
"""
from itertools import product, combinations


def count_direct(facets, owner):
    """Brute-force the owner-knowledge and external-uncertainty clauses."""
    local = [i for i, facet in enumerate(facets) if owner in facet]
    assert local
    colors = len(facets[0])
    others = set(range(colors)) - {0}
    total = 0
    for mask in range(1 << len(facets)):
        if any(not (mask >> i & 1) for i in local):
            continue
        ok = True
        for i in local:
            for b in others:
                if not any(facets[j][b] == facets[i][b] and not (mask >> j & 1)
                           for j in range(len(facets))):
                    ok = False
                    break
            if not ok:
                break
        total += ok
    return total


def two_agent_formula(facets, owner='v'):
    neighbors = {b for a,b in facets if a == owner}
    touched = sum(sum(c == b for a,c in facets) for b in neighbors)
    product_count = 1
    for b in neighbors:
        degree = sum(c == b for a,c in facets)
        product_count *= (2 ** (degree - 1) - 1)
    return 2 ** (len(facets) - touched) * product_count


def edge_cover_count(edges, b_count, c_count):
    total = 0
    for mask in range(1 << len(edges)):
        selected = [edge for i,edge in enumerate(edges) if mask >> i & 1]
        if all(any(b == x for x,y in selected) for b in range(b_count)) and \
           all(any(c == y for x,y in selected) for c in range(c_count)):
            total += 1
    return total


def check():
    two = 0
    three = 0
    # all simple bipartite graphs on 2-by-3 vertices, skip cases without an owner star
    for left,right in [(2,2), (2,3), (3,2)]:
        candidate_edges = list(product(range(left), range(right)))
        for bits in range(1 << len(candidate_edges)):
            edges = [e for i,e in enumerate(candidate_edges) if bits >> i & 1]
            if not any(a == 0 for a,b in edges):
                continue
            facets = [('v' if a == 0 else f'a{a}', f'b{b}') for a,b in edges]
            assert count_direct(facets, 'v') == two_agent_formula(facets, 'v')
            two += 1
    # every 1x1, 1x2, 2x2, 2x3, and 3x2 bipartite edge set
    for b_count,c_count in [(1,1), (1,2), (2,2), (2,3), (3,2)]:
        candidate_edges = list(product(range(b_count), range(c_count)))
        for bits in range(1 << len(candidate_edges)):
            edges = [e for i,e in enumerate(candidate_edges) if bits >> i & 1]
            if not edges:
                continue  # w must belong to at least one maximal facet
            facets = [('v', f'b{b}', f'c{c}')
                      for b,c in candidate_edges]
            facets += [('w', f'b{b}', f'c{c}') for b,c in edges]
            assert count_direct(facets, 'v') == edge_cover_count(edges, b_count, c_count)
            three += 1
    print(f'ALL_CHECKS_OK two_agent_graphs={two} three_agent_graphs={three}')


if __name__ == '__main__':
    check()
