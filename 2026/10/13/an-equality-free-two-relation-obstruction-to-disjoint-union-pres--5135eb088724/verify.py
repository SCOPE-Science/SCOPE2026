#!/usr/bin/env python3
"""Finite cross-checks of an equality-free disjoint-union preservation witness.

The arbitrary-model result is proved by a structural induction, not by this
finite enumeration. The checker uses only the standard Python library.
"""
from itertools import product


def holds(domain_size, e, q):
    n = domain_size
    u = [a for a in range(n) if (a, a) in e and (a, a) not in q]
    t = [a for a in range(n) if (a, a) in q]
    nonedge_u = any((a, b) not in e for a in u for b in u)
    complete_t = all((a, b) in e for a in t for b in t)
    return bool(u) and (nonedge_u or complete_t)


def disjoint(x, y):
    n, e, q = x
    m, f, r = y
    return (n + m, e | {(a+n, b+n) for a,b in f},
            q | {(a+n, b+n) for a,b in r})


def finite_structures(n):
    pairs = [(i,j) for i in range(n) for j in range(n)]
    for ebits in range(1 << (n*n)):
        e = frozenset(pairs[k] for k in range(n*n) if ebits >> k & 1)
        for qbits in range(1 << (n*n)):
            q = frozenset(pairs[k] for k in range(n*n) if qbits >> k & 1)
            yield (n, e, q)


def induced_closed(image, small, large):
    n, e0, q0 = small
    m, e1, q1 = large
    if len(image)!=n or len(set(image))!=n: return False
    sub_e = {(i,j) for i in range(n) for j in range(n)
             if (image[i], image[j]) in e1}
    sub_q = {(i,j) for i in range(n) for j in range(n)
             if (image[i], image[j]) in q1}
    if sub_e!=set(e0) or sub_q!=set(q0): return False
    im = set(image)
    for relation in (e1, q1):
        for x,y in relation:
            if (x in im)!=(y in im): return False
    return True


def main():
    structures = [s for n in (1,2) for s in finite_structures(n)]
    models = [s for s in structures if holds(*s)]
    checks=0
    for first,second in product(models,repeat=2):
        assert holds(*disjoint(first,second))
        checks+=1
    a=(2, {(0,0),(1,1)}, {(1,1)})
    b=(3, {(0,0),(1,1),(2,2)}, {(1,1),(2,2)})
    assert holds(*a) and not holds(*b)
    assert induced_closed((0,1),a,b) and induced_closed((0,2),a,b)
    assert {0,1}|{0,2}==set(range(3))
    print('Individual structures (sizes 1 and 2):',len(structures))
    print('Satisfying structures:',len(models))
    print('All ordered satisfying pairs with disjoint union checked:',checks)
    print('Two finite separating structures and their closed embeddings: PASS')
    print('Note: infinite cases and all formulas use the written proof.')

if __name__=='__main__':
    main()
