#!/usr/bin/env python3
"""Exact finite checks for cyclic-block averaging and local rigidity.
This is supplementary verification, not an exhaustive proof for all cycle lengths.
"""
from fractions import Fraction as F
from itertools import product

def partitions(items):
    if not items:
        yield ()
        return
    first, *rest = items
    for p in partitions(rest):
        yield (frozenset((first,)),) + p
        for j in range(len(p)):
            q = list(p)
            q[j] = q[j] | frozenset((first,))
            yield tuple(q)

def cyclic_blocks(p, n):
    for block in p:
        if len(block) == n:
            continue
        changes = sum(((i in block) != ((i+1) % n in block)) for i in range(n))
        if changes != 2:
            return False
    return True

def variation(x, weights):
    n = len(x)
    return sum(weights[i] * abs(x[i] - x[(i+1) % n]) for i in range(n))

def averaged(v, p, a):
    out = [None]*len(v)
    for B in p:
        q = sum((a[i]*v[i] for i in B), F(0)) / sum((a[i] for i in B), F(0))
        for i in B:
            out[i] = q
    return out

def main():
    tested = 0
    partition_counts = {}
    for n in range(4, 8):
        blocks = [p for p in partitions(list(range(n))) if cyclic_blocks(p,n)]
        partition_counts[n] = len(blocks)
        for mass_seed in range(3):
            a = [F(1 + ((j*j + 3*j + 2*mass_seed) % 7)) for j in range(n)]
            w = [F(1)]*n
            for p in blocks:
                for bits in range(1, (1<<n)-1):
                    v = [F((bits>>j)&1) for j in range(n)]
                    assert variation(averaged(v,p,a),w) <= variation(v,w)
                    tested += 1
    # Every positive nonconstant edge vector has an edge where a positive
    # weighted average of its two neighbors strictly exceeds its own weight.
    rigidity_tests = 0
    for n in range(4,8):
        for a_seed in range(3):
            a = [F(1+((j*3 + a_seed*2)%7)) for j in range(n)]
            for off in range(n):
                w = [F(1 + ((j-off)%n == 0)*3 + ((j-off)%n == 2)) for j in range(n)]
                deficits = []
                for i in range(n):
                    avg = (a[(i+1)%n]*w[(i-1)%n] + a[i]*w[(i+1)%n])/(a[i]+a[(i+1)%n])
                    deficits.append(avg - w[i])
                assert max(deficits) > 0
                rigidity_tests += 1
    # Fully specified four-vertex diamond local-Jacobian witness.
    v = list(map(F, [1,0,0,1]))
    w = list(map(F,[1,1,1,2]))
    p = (frozenset((0,1)), frozenset((2,)), frozenset((3,)))
    av = averaged(v,p,[F(1)]*4)
    assert variation(v,w)==2 and variation(av,w)==F(5,2)
    assert variation(av,w)/variation(v,w) == F(5,4)
    print('PASS cyclic_blocks', partition_counts, 'exact_cut_tests', tested)
    print('PASS nonuniform_rigidity',rigidity_tests, 'diamond_local_ratio',F(5,4))
if __name__=='__main__': main()
