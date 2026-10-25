"""Independent finite verification of the spider conflict-free edge-colouring formula."""
from itertools import combinations_with_replacement
from math import prod
from random import Random


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def theorem_count(lengths):
    k = len(lengths)
    equal = [1 if length == 1 else fib(length - 2) for length in lengths]
    different = [1 if length == 1 else fib(length - 1) for length in lengths]
    singleton = any(length == 1 for length in lengths)
    one_minority = sum(different[j] * prod(equal[i] for i in range(k) if i != j)
                       for j in range(k))
    all_same = 0 if singleton else prod(different)
    return 2 * (one_minority + all_same)


def direct_count(lengths):
    # Build graph without using the theorem's center constraints.
    edges = []
    vertex_count = 1
    for length in lengths:
        previous = 0
        for _ in range(length):
            edges.append((previous, vertex_count))
            previous = vertex_count
            vertex_count += 1
    m = len(edges)
    incident = [0] * vertex_count
    for j, (u,v) in enumerate(edges):
        incident[u] |= 1 << j
        incident[v] |= 1 << j
    masks = [incident[u] | incident[v] for u,v in edges]
    sizes = [mask.bit_count() for mask in masks]
    count = 0
    for coloring in range(1 << m):
        for mask, size in zip(masks, sizes):
            red = (coloring & mask).bit_count()
            if red != 1 and red != size - 1:
                break
        else:
            count += 1
    return count


def run():
    n = 0
    exhaustive_profiles = 0
    for k in range(3,7):
        for lengths in combinations_with_replacement(range(1,9),k):
            if sum(lengths) > 14:
                continue
            predicted = theorem_count(lengths)
            direct = direct_count(lengths)
            if predicted != direct:
                raise AssertionError((lengths,predicted,direct))
            has_short = any(L == 1 for L in lengths)
            has_two_2 = sum(L == 2 for L in lengths) >= 2
            if (predicted == 0) != (has_short and has_two_2):
                raise AssertionError(('classification',lengths,predicted))
            n+=1
            exhaustive_profiles+=1
    rng = Random(104729)
    sampled = set()
    for _ in range(160):
        k = rng.randrange(3,9)
        ls=[rng.randrange(1,8) for _ in range(k)]
        if sum(ls)>17:continue
        ls=tuple(sorted(ls))
        if ls in sampled:continue
        sampled.add(ls)
        predicted=theorem_count(ls)
        direct=direct_count(ls)
        if predicted!=direct:raise AssertionError(('sample',ls,predicted,direct))
        n+=1
    # The critical mixed spider forces three colors by the general tree bound.
    assert theorem_count((1,2,2))==0
    assert theorem_count((2,2,2))==2
    assert theorem_count((1,2,3))==2
    assert theorem_count((1,1,1))==6
    print('VERIFY_OK', 'tested_profiles='+str(n), 'systematic='+str(exhaustive_profiles),
          'sampled='+str(len(sampled)))

if __name__ == '__main__':
    run()
