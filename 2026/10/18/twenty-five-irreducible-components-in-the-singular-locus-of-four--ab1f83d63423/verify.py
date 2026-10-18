#!/usr/bin/env python3
"""Finite exact checks for the four-column orthogonality singular-stratum theorem.

Requires Python 3 standard library only. This is a finite consistency test, not
an exhaustive proof over complex points or over arbitrary ambient dimensions.
"""
from fractions import Fraction
from itertools import combinations, product


def rank(a):
    if not a:
        return 0
    a = [[Fraction(v) for v in row] for row in a]
    m, n = len(a), len(a[0])
    piv = 0
    for col in range(n):
        k = next((j for j in range(piv, m) if a[j][col]), None)
        if k is None:
            continue
        a[piv], a[k] = a[k], a[piv]
        p = a[piv][col]
        a[piv] = [v / p for v in a[piv]]
        for row in range(m):
            if row != piv and a[row][col]:
                f = a[row][col]
                a[row] = [x - f*y for x, y in zip(a[row], a[piv])]
        piv += 1
        if piv == m:
            break
    return piv


def hmatrix(m):
    h = [[0] * m for _ in range(m)]
    for i, j in [(0, 2), (1, 3)]:
        h[i][j] = h[j][i] = 1
    for i in range(4, m):
        h[i][i] = 1
    return h


def dot(a, b, h):
    return sum(a[i] * h[i][j] * b[j] for i in range(len(a)) for j in range(len(b)))


def jacobian(v, h):
    m = len(v[0])
    rows = []
    for i, j in combinations(range(4), 2):
        row = [0] * (4*m)
        for t in range(m):
            row[i*m+t] = sum(h[t][s]*v[j][s] for s in range(m))
            row[j*m+t] = sum(h[t][s]*v[i][s] for s in range(m))
        rows.append(row)
    return rows


def vectors(m):
    e = [[int(i == k) for i in range(m)] for k in range(5)]
    add = lambda a,b:[x+y for x,y in zip(a,b)]
    neg = lambda a:[-x for x in a]
    mul = lambda c,a:[c*x for x in a]
    return e, add, neg, mul


def all_witnesses(m):
    e, add, neg, mul = vectors(m)
    zero = [0]*m
    result = []
    # Six two-zero-index loci.
    for i, j in combinations(range(4), 2):
        v = [zero[:] for _ in range(4)]
        k, l = [x for x in range(4) if x not in (i,j)]
        v[k], v[l] = add(e[0],e[2]), add(e[1],e[3])
        result.append(('A',v))
    # Four isotropic two-plane loci.
    for i in range(4):
        v = [zero[:] for _ in range(4)]
        for k, val in zip([x for x in range(4) if x != i], [e[0],e[1],add(e[0],e[1])]):
            v[k] = val
        result.append(('T',v))
    # Twelve loci with one zero and one distinguished anisotropic vector.
    for i in range(4):
        for j in range(4):
            if i == j: continue
            v = [zero[:] for _ in range(4)]
            v[j] = e[4]
            k, l = [x for x in range(4) if x not in (i,j)]
            v[k], v[l] = e[0], mul(2,e[0])
            result.append(('R',v))
    # Three partitions into two collinear isotropic pairs.
    for pair in [(0,1),(0,2),(0,3)]:
        v = [zero[:] for _ in range(4)]
        rest = [x for x in range(4) if x not in pair]
        v[pair[0]], v[pair[1]] = e[0], mul(2,e[0])
        v[rest[0]], v[rest[1]] = e[1], mul(3,e[1])
        result.append(('P',v))
    assert len(result) == 25
    return result


def rank_mod(a, p):
    a = [[v % p for v in row] for row in a]
    z = 0
    for j in range(len(a[0])):
        k = next((i for i in range(z, len(a)) if a[i][j]), None)
        if k is None: continue
        a[z],a[k] = a[k],a[z]
        inv = pow(a[z][j], -1, p)
        for l in range(j, len(a[0])):
            a[z][l] = a[z][l] * inv % p
        for i in range(z+1, len(a)):
            c = a[i][j]
            for l in range(j, len(a[0])):
                a[i][l] = (a[i][l]-c*a[z][l]) % p
        z += 1
        if z == len(a): break
    return z


def bipartite_support(c):
    for types in product((0,1,2), repeat=4):
        if 1 not in types or 2 not in types: continue
        if all(c[i][j] == 0 or {types[i], types[j]} == {1,2}
               for i in range(4) for j in range(i+1,4)):
            return True
    return False


def main():
    tested = 0
    for m in (5,6,7,8):
        h = hmatrix(m)
        for name,v in all_witnesses(m):
            assert all(dot(v[i], v[j],h)==0 for i,j in combinations(range(4),2)),(m,name)
            assert rank(jacobian(v,h)) == 5,(m,name)
            assert rank([[v[i][t] for i in range(4)] for t in range(m)]) == 2
            tested += 1
        e, add, neg, mul = vectors(m)
        a=add(e[0],e[2]);b=add(e[1],e[3]);c=e[4];d=add(e[0],neg(e[2]))
        for v in ([a,b,c,[0]*m],[a,b,c,d]):
            assert all(dot(v[i],v[j],h)==0 for i,j in combinations(range(4),2))
            assert rank(jacobian(v,h)) == 6
            tested += 1
    # All 4-by-4 hollow symmetric matrices over F_3 of rank two have
    # bipartite cross-support, as required by the characteristic-zero lemma.
    cnt = 0
    for vals in product(range(3),repeat=6):
        c = [[0]*4 for _ in range(4)]
        for (i,j),v in zip(combinations(range(4),2), vals):
            c[i][j]=c[j][i]=v
        if rank_mod(c,3)==2:
            assert bipartite_support(c), vals
            cnt += 1
    assert cnt > 0
    print(f'VERIFY_OK witness_cases={tested} hollow_rank_two_mod3={cnt}')

if __name__ == '__main__':
    main()
