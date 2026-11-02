"""Brute-force finite checks for implication-fixpoint and material-implication counts.

The checked objects are finite rooted forests presented in parent-before-child
order. This enumerates representatives of every rooted-forest isomorphism type
within the stated size cutoff, not every labeled forest.
"""
from itertools import product
from math import prod


def ideals_and_downsets(parents):
    n = len(parents)
    ancestor = []
    for v in range(n):
        ancestors = 1 << v
        p = parents[v]
        while p >= 0:
            ancestors |= 1 << p
            p = parents[p]
        ancestor.append(ancestors)
    ideals = [x for x in range(1 << n)
              if all(not (x & (1 << i)) or x & ancestor[i] == ancestor[i]
                     for i in range(n))]
    return ideals, ancestor


def implication(a, b, ancestor):
    return sum(1 << i for i, down in enumerate(ancestor)
               if down & a & ~b == 0)


def brute_statistics(parents):
    ideals, ancestor = ideals_and_downsets(parents)
    n = len(parents)
    total = (1 << n) - 1
    N = len(ideals)
    fixpoint_count = 0
    material_failure_count = 0
    for a in ideals:
        neg = implication(a, 0, ancestor)
        for b in ideals:
            arrow = implication(a, b, ancestor)
            fixpoint_count += (arrow == b)
            material_failure_count += (arrow != (neg | b))
    return N, fixpoint_count, material_failure_count


def expected_fixpoint_count(parents):
    # Recurrence: s(empty)=1, s(disjoint union)=product of s(components),
    # and s(root plus a forest Q)=|J(Q)|+1+s(Q).
    children = [[] for _ in parents]
    roots = []
    for i, p in enumerate(parents):
        if p < 0:
            roots.append(i)
        else:
            children[p].append(i)

    def component(v):
        descendant_children = [component(c) for c in children[v]]
        m = prod(size for size, _ in descendant_children)
        s = prod(score for _, score in descendant_children)
        return m + 1, m + 1 + s

    components = [component(r) for r in roots]
    return prod(size for size, _ in components), prod(score for _, score in components)


def main():
    total_cases = 0
    connected_cases = 0
    for n in range(1, 8):
        cases = 0
        for parents in product(*(range(-1, i) for i in range(n))):
            cases += 1
            total_cases += 1
            N, s, f = brute_statistics(parents)
            expected_N, expected_s = expected_fixpoint_count(parents)
            assert (N, s) == (expected_N, expected_s), (parents, N, s, expected_N, expected_s)
            assert 2 * s <= N * (N + 1), ('upper bound', parents, N, s)
            is_chain = sum(p == -1 for p in parents) == 1 and all(
                sum(q == i for q in parents) <= 1 for i in range(n))
            assert (2 * s == N * (N + 1)) == is_chain, ('equality', parents)
            is_connected = sum(p == -1 for p in parents) == 1
            if is_connected and n > 1:
                connected_cases += 1
                assert 2*f >= (N-1)*(N-2), ('connected bound', parents, N, f)
                assert (2*f == (N-1)*(N-2)) == is_chain, ('connected equality', parents)
            # In a rooted forest, the material-implication identity holds
            # identically precisely when every component is a singleton.
            non_boolean = any(p >= 0 for p in parents)
            if non_boolean:
                assert 9*f >= N*N, ('one-ninth gap', parents, N, f)
                # Equality: exactly one nontrivial component, with two points.
                root_of = []
                for j in range(n):
                    r = j
                    while parents[r] >= 0:
                        r = parents[r]
                    root_of.append(r)
                component_sizes = sorted(root_of.count(r) for r in set(root_of))
                # More robust classification: one component size 2,
                # all remaining components size 1.
                special = component_sizes.count(2) == 1 and all(k in (1,2) for k in component_sizes)
                assert (9*f == N*N) == special, ('gap equality', parents, N, f)
            else:
                assert f == 0, ('Boolean case', parents, N, f)
        print(f'FORESTS_OK points={n} increasing_representations={cases}',flush=True)
    print(f'ALL_FOREST_COUNTS_PASS checked={total_cases} connected_nontrivial={connected_cases}')
    for n in range(2, 9):
        parents = (-1,) + (0,)*(n-1)
        N, _, F = brute_statistics(parents)
        assert N == 1 + 2**(n-1)
        assert F == 4**(n-1) - 3**(n-1)
    print('ROOTED_STAR_FORMULA_PASS leaves=1..7')
    for n in range(2, 13):
        parents = (-1,) + tuple(i-1 for i in range(1,n))
        N, s, F = brute_statistics(parents)
        assert N == n + 1 and F == n*(n-1)//2
        assert s == N*(N+1)//2
    print('CHAIN_SHARPNESS_PASS vertices=2..12')
    print('ALL_MATERIAL_GODEL_GAP_CHECKS_PASS')

if __name__ == '__main__':
    main()
