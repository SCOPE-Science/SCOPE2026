"""Exact rational sample checks for finite subset-Euclidean norms.

These tests illustrate, but do not replace, the structural proof.
"""
from fractions import Fraction as Q
from itertools import combinations, product, permutations

def norm_sq(v, facets):
    return max(sum(v[i] * v[i] for i in F) for F in facets)

def all_facet_families(n):
    subsets = tuple(tuple(i for i in range(n) if s >> i & 1)
                    for s in range(1, 1 << n))
    m = len(subsets)
    for r in range(1, m + 1):
        for ids in combinations(range(m), r):
            facets = tuple(subsets[j] for j in ids)
            cover = set().union(*(set(F) for F in facets))
            if len(cover) != n:
                continue
            if any(set(F) < set(G) for F, G in combinations(facets, 2)):
                continue
            yield facets

def twins(facets, n):
    groups = {}
    for i in range(n):
        k = tuple(j for j, F in enumerate(facets) if i in F)
        groups.setdefault(k, []).append(i)
    return tuple(tuple(v) for v in groups.values())

def rotated(v, i, j):
    y = list(v)
    y[i] = Q(3,5)*v[i] - Q(4,5)*v[j]
    y[j] = Q(4,5)*v[i] + Q(3,5)*v[j]
    return y

def check():
    count = 0
    pairs = 0
    evaluated = 0
    permuted_facet_checks = 0
    # Exhaust every antichain of maximal subsets on 1..4 coordinates.
    for n in range(1, 5):
        vectors = tuple(product((-1, 0, 1), repeat=n))
        for facets in all_facet_families(n):
            count += 1
            blocks = twins(facets, n)
            # Every twin pair admits an exact 3-4-5 Euclidean rotation.
            for B in blocks:
                for i, j in combinations(B, 2):
                    pairs += 1
                    for x in vectors:
                        v = [Q(t) for t in x]
                        assert norm_sq(v,facets) == norm_sq(rotated(v,i,j),facets), (facets,i,j,x)
                        evaluated += 1
            # Coordinate permutations preserve the norm iff they preserve facets.
            for perm in permutations(range(n)):
                permuted = tuple(frozenset(perm[i] for i in F) for F in facets)
                automorphism = set(permuted) == {frozenset(F) for F in facets}
                # Check the complete nonnegative 0/1/2 grid, avoiding a purely
                # empirical claim about arbitrary vectors.
                test_equal = all(
                    norm_sq(v, facets) == norm_sq(tuple(v[perm.index(i)] for i in range(n)), facets)
                    for v in product((0,1,2), repeat=n)
                )
                assert test_equal == automorphism, (n,facets,perm,test_equal,automorphism)
                permuted_facet_checks += 1
    print('facet_families:',count)
    print('twin_pairs:',pairs)
    print('exact_equality_checks:',evaluated)
    print('coordinate_permutation_checks:',permuted_facet_checks)
    assert count > 100 and pairs > 10 and evaluated > 1000

if __name__ == '__main__':
    check()
