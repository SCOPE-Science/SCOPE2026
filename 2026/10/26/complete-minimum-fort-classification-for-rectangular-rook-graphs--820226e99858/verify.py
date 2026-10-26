#!/usr/bin/env python3
"""Independent exact checks for minimum forts of Cartesian products of cliques.

No optional dependencies; invoke with python3 verify.py.
"""
from itertools import combinations, product
from math import comb


def fort_original(m, n, cells):
    chosen = set(cells)
    for i in range(m):
        for j in range(n):
            if (i, j) not in chosen:
                nearby = sum((r == i or c == j) for r, c in chosen)
                if nearby == 1:
                    return False
    return bool(chosen)


def support_criterion(m, n, cells):
    if not cells:
        return False
    row = [0] * m
    col = [0] * n
    for i,j in cells:
        row[i] += 1
        col[j] += 1
    return (not any(x == 0 for x in col) or all(x != 1 for x in row)) and (not any(x == 0 for x in row) or all(x != 1 for x in col))


def classify_min(p, q):
    assert 1 <= p <= q
    if p == 1:
        k = 1 if q == 1 else 2
        for xs in combinations([(0,j) for j in range(q)], k):
            yield frozenset(xs)
    elif p == 2 and q == 2:
        for perm in ((0,1),(1,0)):
            yield frozenset((i,perm[i]) for i in range(2))
    elif p == 2 and q == 3:
        for rows in product(range(2), repeat=3):
            if set(rows) == {0,1}:
                yield frozenset((rows[j],j) for j in range(3))
    elif p == 2:
        for a in combinations(range(q),2):
            for b in combinations(range(q),2):
                yield frozenset({(0,j) for j in a} | {(1,j) for j in b})
        if q == 4:
            for rows in product(range(2), repeat=4):
                if sorted((rows.count(0),rows.count(1))) == [1,3]:
                    yield frozenset((rows[j],j) for j in range(4))
    elif p == q == 3:
        for perm in __import__('itertools').permutations(range(3)):
            yield frozenset((i,perm[i]) for i in range(3))
    else:
        for rows in combinations(range(p),2):
            for cols in combinations(range(q),2):
                yield frozenset(product(rows, cols))
        if p == 3 and q == 4:
            for rows in product(range(3), repeat=4):
                if set(rows) == {0,1,2}:
                    yield frozenset((rows[j],j) for j in range(4))
        if p == q == 4:
            for perm in __import__('itertools').permutations(range(4)):
                yield frozenset((i,perm[i]) for i in range(4))


def predicted_minimum_size(p,q):
    if p == q == 1: return 1
    if p == 1 or (p,q) == (2,2): return 2
    if (p,q) in {(2,3),(3,3)}: return 3
    return 4


def predicted_number(p,q):
    if p == q == 1: return 1
    if p == 1: return comb(q,2)
    if (p,q) == (2,2): return 2
    if (p,q) in {(2,3),(3,3)}:return 6
    if p == 2:return comb(q,2)**2+(8 if q == 4 else 0)
    return comb(p,2)*comb(q,2)+(36 if (p,q)==(3,4) else 0)+(24 if (p,q)==(4,4) else 0)


def run():
    checked_subsets=0
    for m in range(1,5):
        for n in range(m,9):
            k=predicted_minimum_size(m,n)
            expected=set(classify_min(m,n))
            assert len(expected)==predicted_number(m,n)
            assert all(len(x)==k for x in expected)
            found=set()
            # Direct original-neighborhood test; no support criterion here.
            for h in range(1,k+1):
                for ids in combinations(range(m*n),h):
                    F=frozenset((v//n,v%n) for v in ids)
                    if fort_original(m,n,F):
                        assert h==k, (m,n,h,F)
                        found.add(F)
                    checked_subsets+=1
            assert found==expected,(m,n,len(found),len(expected))
    print('MINIMUM_FORT_CLASSES_OK:', 'pairs=26', 'subsets=', checked_subsets)
    criterion_checked=0
    for m in range(1,5):
        for n in range(m,7):
            if m*n>12:continue
            for mask in range(1<<(m*n)):
                F={(i,j) for i in range(m) for j in range(n) if mask & (1<<(i*n+j))}
                assert fort_original(m,n,F)==support_criterion(m,n,F),(m,n,mask)
                criterion_checked+=1
    print('FULL_SUPPORT_EQUIVALENCE_OK:', 'subsets=', criterion_checked)
    print('EXAMPLES:',[(m,n,predicted_minimum_size(m,n),predicted_number(m,n)) for m,n in [(2,4),(2,6),(3,3),(3,4),(3,6),(4,4),(4,7)]])
    print('VERIFY_OK')
if __name__=='__main__':run()
