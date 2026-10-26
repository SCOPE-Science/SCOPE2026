"""Exact reproducibility test for one-node protection and surviving-pair reliability.

Run: python3 verify.py > certificate.json
Requires only the Python 3 standard library.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
import json


def prufer_tree(code, n):
    """Inverse Prufer bijection on labeled trees with vertices 0,...,n-1."""
    degree = [1] * n
    for v in code:
        degree[v] += 1
    edges = []
    for v in code:
        leaf = next(i for i in range(n) if degree[i] == 1)
        a, b = sorted((leaf, v))
        edges.append((a, b))
        degree[leaf] -= 1
        degree[v] -= 1
    a, b = [i for i in range(n) if degree[i] == 1]
    edges.append(tuple(sorted((a, b))))
    return tuple(sorted(edges))


def adjacency(edges, n):
    a = [0] * n
    for i, j in edges:
        a[i] |= 1 << j
        a[j] |= 1 << i
    return a


def independent_subset_counts(adj, allowed):
    """Count independent subsets in G[allowed] by their cardinality."""
    n = len(adj)
    c = [0] * n
    sub = allowed
    while True:
        rem = sub
        independent = True
        while rem:
            lsb = rem & -rem
            v = lsb.bit_length() - 1
            rem ^= lsb
            if adj[v] & rem:
                independent = False
                break
        if independent:
            c[sub.bit_count()] += 1
        if sub == 0:
            break
        sub = (sub - 1) & allowed
    return tuple(c)


def protection_polynomials(adj):
    n = len(adj)
    full = (1 << n) - 1
    return tuple(independent_subset_counts(adj, full & ~(adj[v] | (1 << v))) for v in range(n))


def coefficientwise_optima(polys):
    return [i for i, a in enumerate(polys)
            if all(all(ai <= bi for ai, bi in zip(a, b)) for b in polys)]


def is_subdivided_three_star(adj):
    """Exactly one degree-three center, each arm is two edges."""
    if len(adj) != 7:
        return False
    c = [v for v, a in enumerate(adj) if a.bit_count() == 3]
    if len(c) != 1:
        return False
    center = c[0]
    arms = [v for v in range(7) if adj[center] & (1 << v)]
    if len(arms) != 3 or any(adj[v].bit_count() != 2 for v in arms):
        return False
    leaves = [v for v in range(7) if adj[v].bit_count() == 1]
    return len(leaves) == 3 and all(any(adj[v] & (1 << l) for l in leaves) for v in arms)


def exact_success(adj, protected, p):
    """Independently enumerate all unprotected vertex survival states."""
    n = len(adj)
    other = [v for v in range(n) if v != protected]
    total = Fraction(0)
    for bits in range(1 << len(other)):
        alive = 1 << protected
        successes = 0
        for j, v in enumerate(other):
            if bits & (1 << j):
                alive |= 1 << v
                successes += 1
        if any(adj[v] & alive for v in range(n) if alive & (1 << v)):
            total += p**successes * (1 - p)**(n - 1 - successes)
    return total


def main():
    stats = []
    exceptional_edges = None
    exception_count = 0
    seen_structures = Counter()
    for n in range(2, 8):
        total = 0
        dominated = 0
        exceptions = 0
        for code in product(range(n), repeat=n - 2):
            edges = prufer_tree(code, n)
            adj = adjacency(edges, n)
            polynomials = protection_polynomials(adj)
            optima = coefficientwise_optima(polynomials)
            total += 1
            if optima:
                dominated += 1
            else:
                exceptions += 1
                if n != 7 or not is_subdivided_three_star(adj):
                    raise AssertionError('Unexpected non-dominance configuration')
                center = next(v for v in range(n) if adj[v].bit_count() == 3)
                arms = [v for v in range(n) if adj[center] & (1 << v)]
                leaves = [v for v in range(n) if adj[v].bit_count() == 1]
                assert polynomials[center][:4] == (1, 3, 3, 1)
                assert all(polynomials[v][:4] == (1, 4, 4, 0) for v in arms)
                assert all(polynomials[v][:4] == (1, 5, 6, 1) for v in leaves)
                exceptional_edges = edges
                exception_count += 1
        assert total == n ** (n-2)
        assert (exceptions == 840 if n == 7 else exceptions == 0)
        stats.append({'n': n, 'all_labeled_trees': total,
                      'coefficientwise_dominated': dominated,
                      'exceptional': exceptions})
    assert exception_count == 840
    # Complete construction of the unique unlabeled exception.
    edges = ((0,1),(0,3),(0,5),(1,2),(3,4),(5,6))
    adj = adjacency(edges, 7)
    center, arm = 0, 1
    for pp in (Fraction(1,4), Fraction(1,2), Fraction(3,4), Fraction(9,10)):
        pc = exact_success(adj, center, pp)
        pa = exact_success(adj, arm, pp)
        assert pc == 1 - (1 - pp)**3
        assert pa == 1 - (1 - pp)**4 * (1 + pp)**2
        assert pc - pa == pp * (1 - pp)**3 * (1 - pp - pp**2)
        for v in range(7):
            assert max(exact_success(adj, w, pp) for w in range(7)) >= exact_success(adj, v, pp)
        assert max(exact_success(adj, w, pp) for w in range(7)) == max(pc, pa)
    certificate = {
        'method':'Full Prufer-sequence enumeration of every labeled tree on n=2,...,7; exact independent-set coefficient comparisons',
        'enumeration': stats,
        'unique_seven_vertex_exception_up_to_isomorphism': 'subdivided 3-star, three arms of length two',
        'exception_labeled_count': exception_count,
        'exception_automorphism_order': 6,
        'example_edges': [list(e) for e in edges],
        'center_independence_coefficients_low_degree_first':[1,3,3,1],
        'each_arm_neighbor_independence_coefficients_low_degree_first':[1,4,4],
        'each_leaf_independence_coefficients_low_degree_first':[1,5,6,1],
        'difference_success_center_minus_arm':'p*(1-p)^3*(1-p-p^2)',
        'switch_threshold':'(sqrt(5)-1)/2',
        'separate_direct_survival_enumeration_probabilities':['1/4','1/2','3/4','9/10'],
        'logic':'All nonexceptional trees have a single coefficientwise-minimal independent-set polynomial. Every exception is the subdivided three-star. The two undominated polynomials there cross once at positive activity (1+sqrt(5))/2, corresponding to the displayed survival threshold.'
    }
    print(json.dumps(certificate, ensure_ascii=False, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
