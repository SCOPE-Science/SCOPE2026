"""Exact rational spot checks for the isotropic-point apartment theorem.

The mathematical proof applies in all ranks; these finite checks test the
sharp configurations and both forms of obstruction independently.
"""
from fractions import Fraction
from itertools import combinations


def rank(rows):
    if not rows:
        return 0
    a = [[Fraction(v) for v in row] for row in rows]
    piv = 0
    n = len(a[0])
    for j in range(n):
        k = next((i for i in range(piv, len(a)) if a[i][j]), None)
        if k is None:
            continue
        a[piv], a[k] = a[k], a[piv]
        c = a[piv][j]
        a[piv] = [v/c for v in a[piv]]
        for i in range(len(a)):
            if i != piv and a[i][j]:
                d = a[i][j]
                a[i] = [a[i][t] - d*a[piv][t] for t in range(n)]
        piv += 1
        if piv == len(a):
            break
    return piv


def pairing(x, y):
    m = len(x)//2
    return sum(x[i]*y[m+i]+x[m+i]*y[i] for i in range(m))


def e(m, i, dual=False):
    out = [0]*(2*m)
    out[i+m*int(dual)] = 1
    return out


def apartment_test(vectors):
    if not vectors:
        return True
    assert all(pairing(x, x) == 0 for x in vectors)
    assert len(set(tuple(x) for x in vectors)) == len(vectors)
    deg = [0]*len(vectors)
    for i,j in combinations(range(len(vectors)),2):
        if pairing(vectors[i],vectors[j]):
            deg[i] += 1
            deg[j] += 1
    singles = [vectors[i] for i in range(len(vectors)) if deg[i] == 0]
    return max(deg,default=0)<=1 and rank(singles)==len(singles)


def sharp_witness(m, d):
    base = [e(m,i) for i in range(d)]
    return base + [[sum(x[k] for x in base) for k in range(2*m)]]


def check():
    for m in range(4,13):
        for d in range(2,m+1):
            vectors = sharp_witness(m,d)
            assert not apartment_test(vectors)
            for subset in combinations(vectors,d):
                assert apartment_test(subset)
            assert rank(vectors)==d
            assert all(pairing(x,y)==0 for x,y in combinations(vectors,2))
        good = [e(m,0),e(m,0,True)]+[e(m,i) for i in range(1,m)]
        assert apartment_test(good)
        bad = [e(m,0),e(m,0,True),
               [e(m,0,True)[k]+e(m,1,True)[k] for k in range(2*m)]]
        assert not apartment_test(bad)
        assert all(apartment_test(list(s)) for s in combinations(bad,2))
    print('EXACT_TESTS_OK: ranks 4..12, every projective obstruction dimension 2..rank')


if __name__ == '__main__':
    check()
