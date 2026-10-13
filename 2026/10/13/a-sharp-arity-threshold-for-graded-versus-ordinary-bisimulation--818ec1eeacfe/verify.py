#!/usr/bin/env python3
"""Independent finite checks for counting versus ordinary modal bisimulation.

Run with Python 3 standard library: python3 verify.py
The asymptotic lower and upper bounds are established by mathematical proof,
not by the finite enumerations in this file.
"""
from itertools import product, combinations_with_replacement
from math import comb, factorial, log


def complete_tree(arity, height):
    children = [[]]
    levels = [[0]]
    for _ in range(height):
        new = []
        for parent in levels[-1]:
            for _ in range(arity):
                child = len(children)
                children.append([])
                children[parent].append(child)
                new.append(child)
        levels.append(new)
    return children, levels


def modal_partitions(children, coloring):
    """Canonical bottom-up codes: successor support vs. successor multiset."""
    ranks = []
    for multiplicities in (False, True):
        ids, codes, next_id = [None]*len(children), {}, 0
        for v in range(len(children)-1, -1, -1):
            image = [ids[w] for w in children[v]]
            neighborhood = tuple(sorted(image)) if multiplicities else frozenset(image)
            signature = (coloring[v], neighborhood)
            if signature not in codes:
                codes[signature] = next_id
                next_id += 1
            ids[v] = codes[signature]
        ranks.append(ids)
    return tuple(ranks)


def check_refinement(plain, graded):
    g_to_p = {}
    for a, b in zip(plain, graded):
        if b in g_to_p:
            assert g_to_p[b] == a
        else:
            g_to_p[b] = a


def count_types(ids):
    return len(set(ids))


def check_fixed_point(children, coloring, multiplicities):
    """Separate iterative partition-refinement implementation."""
    n = len(children)
    block = list(coloring)
    for _ in range(n+1):
        signatures = []
        for v in range(n):
            child_blocks = [block[w] for w in children[v]]
            support = tuple(sorted(child_blocks)) if multiplicities else tuple(sorted(set(child_blocks)))
            signatures.append((block[v], support))
        sorted_types = {key:i for i,key in enumerate(sorted(set(signatures)))}
        updated = [sorted_types[key] for key in signatures]
        if len(set(updated)) == len(set(block)):
            # New partition refines the old, so equal block count is stability.
            return updated
        block = updated
    raise AssertionError('refinement did not converge')


def same_partition(x, y):
    to_y, to_x = {}, {}
    for a,b in zip(x,y):
        if a in to_y: assert to_y[a] == b
        else: to_y[a] = b
        if b in to_x: assert to_x[b] == a
        else: to_x[b] = a


def type_count_g(arity, height):
    g = arity - 1
    for _ in range(1, height):
        g = comb(g + arity - 1, arity)
    return g


def types_at_height(arity, height, count):
    """Construct distinct legal types without materializing the huge full census."""
    if height == 1:
        assert count <= arity-1
        return list(range(1, count+1))
    t = 1
    while comb(t+arity-1, arity) < count:
        t += 1
    old = types_at_height(arity, height-1, t)
    output = []
    for tup in combinations_with_replacement(old, arity):
        output.append(tup)
        if len(output) == count:
            return output
    raise AssertionError('unranking exhausted')


def construct_witness(arity, height):
    children, levels = complete_tree(arity, height)
    k = next(k for k in range(1, height+1)
             if type_count_g(arity, k) >= arity**(height-k))
    targets = levels[height-k]
    descriptions = types_at_height(arity, k, len(targets))
    coloring = [0]*len(children)
    def place(v, depth, desc):
        if depth == 1:
            for i,child in enumerate(children[v]):
                coloring[child] = int(i < desc)
        else:
            for child,sub in zip(children[v],desc):
                place(child, depth-1, sub)
    for v, desc in zip(targets, descriptions):
        place(v,k,desc)
    plain, graded = modal_partitions(children,coloring)
    check_refinement(plain,graded)
    assert count_types(plain) == height + 2
    assert len(set(graded[v] for v in targets)) == len(targets)
    return len(children), k, len(targets), count_types(plain), count_types(graded)


def main():
    cases = tables = fixed = 0
    for arity, heights in ((2,range(0,4)),(3,range(0,3))):
        for h in heights:
            edges, levels = complete_tree(arity,h)
            n = len(edges)
            sep, min_ordinary = 0, n+1
            for val in product((0,1),repeat=n):
                ordinary, graded = modal_partitions(edges,val)
                check_refinement(ordinary,graded)
                po, pg = count_types(ordinary), count_types(graded)
                if arity == 2: assert po == pg
                if pg > po:
                    sep += 1
                    min_ordinary = min(min_ordinary,po)
                if tables % 127 == 0:
                    for mult, bottom in ((False,ordinary),(True,graded)):
                        top = check_fixed_point(edges,val,mult)
                        same_partition(bottom,top)
                        fixed += 1
                tables += 1
            if arity == 3 and h == 2:
                assert sep > 0 and min_ordinary == h+2
            print('EXHAUSTIVE',arity,h,n,2**n,'split_colorings',sep,'min_ordinary_split',min_ordinary if sep else '- ')
            cases += 1
    witnesses = 0
    for arity, heights in ((3,range(3,10)),(4,range(3,7)),(5,range(3,6))):
        for h in heights:
            n,k,target,p,g = construct_witness(arity,h)
            print('WITNESS',arity,h,'worlds',n,'window',k,'distinct_at_window',target,'plain',p,'graded',g)
            witnesses += 1
    for arity in range(3,12):
        g1 = arity-1
        g2 = comb(g1 + arity-1, arity)
        assert g2 >= arity+1
        assert (g2**(arity-1)) > factorial(arity)
    print('VERIFY_OK exhaustive_colorings',tables,'parameter_cases',cases,
          'independent_partition_comparisons',fixed,'structured_witnesses',witnesses,
          'growth_threshold_checks',9)


if __name__ == '__main__':
    main()
