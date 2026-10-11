"""Exact checks for the Euclidean geometry of a bipartite-cycle root polytope.

Run: python3 verify.py
Only Python's standard library is needed for the exact tests.
Optional hull check: python3 verify.py --hull (requires NumPy/SciPy).
The finite checks are corroboration and do not prove the all-parameter theorem.
"""
from fractions import Fraction as Q
from math import floor
from sys import argv


def rank(a):
    a = [[Q(x) for x in row] for row in a]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    pivots = 0
    for c in range(n):
        i = next((i for i in range(pivots, m) if a[i][c]), None)
        if i is None:
            continue
        a[pivots], a[i] = a[i], a[pivots]
        a[pivots] = [x / a[pivots][c] for x in a[pivots]]
        for j in range(m):
            if j != pivots and a[j][c]:
                t = a[j][c]
                a[j] = [x - t * y for x, y in zip(a[j], a[pivots])]
        pivots += 1
        if pivots == m:
            break
    return pivots


def solve(a, b):
    n = len(a[0])
    aug = [[Q(x) for x in row] + [Q(v)] for row, v in zip(a, b)]
    pivots = []
    r = 0
    for col in range(n):
        z = next((h for h in range(r, len(aug)) if aug[h][col]), None)
        if z is None:
            continue
        aug[r], aug[z] = aug[z], aug[r]
        pivot = aug[r][col]
        aug[r] = [z / pivot for z in aug[r]]
        for h in range(len(aug)):
            if h != r and aug[h][col]:
                t = aug[h][col]
                aug[h] = [x - t * y for x, y in zip(aug[h], aug[r])]
        pivots.append(col)
        r += 1
    assert r == n and all(any(row[:n]) or row[-1] == 0 for row in aug)
    sol = [Q(0)] * n
    for h, col in enumerate(pivots):
        sol[col] = aug[h][-1]
    return sol


def normal_formula(k, i, j):
    d = (j-i) % k
    x = [(-d + k * (1 <= ((h-i) % k) <= d)) for h in range(k)]
    y = [x[h]-1+k*(h == i) for h in range(k)]
    return [Q(z) for z in x+y]


def normal_independent(k, i, j):
    a=[]; b=[]
    for h in range(k):
        if h != i:
            row = [0]*(2*k);row[h] = 1;row[k+h] = -1
            a.append(row);b.append(1)
        if h != j:
            row = [0]*(2*k);row[(h+1)%k] = 1;row[k+h] = -1
            a.append(row);b.append(1)
    a.append([1]*k + [0]*k);b.append(0)
    a.append([0]*k + [1]*k);b.append(0)
    return solve(a,b)


def test(k, independent=False):
    profiles={}
    contacts=[]
    maxsq = k*(k-1+2*((k-1)**2//4))
    for i in range(k):
        for j in range(k):
            n = normal_formula(k,i,j)
            if independent:
                assert n == normal_independent(k,i,j)
            assert sum(n[:k])==0 and sum(n[k:])==0
            for h in range(k):
                assert n[h]-n[k+h] == (1-k if h==i else 1)
                assert n[(h+1)%k]-n[k+h] == (1-k if h==j else 1)
            sq = sum(z*z for z in n)
            d=(j-i)%k
            assert sq == k*(k-1+2*d*(k-1-d))
            profiles[sq]=profiles.get(sq,0)+1
            if sq==maxsq:
                contacts.append(n)
    assert sum(profiles.values())==k*k
    assert max(profiles)==maxsq
    assert len(contacts)==(k if k%2 else 2*k)
    assert maxsq == (k*(k*k - (1 if k%2 else 2)))//2
    assert rank(contacts) == (k-1 if k%2 else 2*k-2)
    print(f'k={k}: {k*k} candidate facets, {len(profiles)} shells, '
          f'{len(contacts)} closest facets, contact rank {rank(contacts)}; '
          f'1/r^2={maxsq}')


def hull(k):
    import numpy as np
    from scipy.spatial import ConvexHull
    center = np.r_[np.ones(k)/k, -np.ones(k)/k]
    roots=[]
    for i in range(k):
        a=np.zeros(2*k);a[i]=1;a[k+i]=-1;roots.append(a-center)
    for i in range(k):
        a=np.zeros(2*k);a[(i+1)%k]=1;a[k+i]=-1;roots.append(a-center)
    mat=np.array(roots)
    _,s,vh=np.linalg.svd(mat,full_matrices=False)
    d=np.count_nonzero(s>1e-8)
    assert d==2*k-2
    h=ConvexHull(mat @ vh[:d].T)
    planes=set()
    for equation in h.equations:
        assert abs(np.linalg.norm(equation[:-1])-1)<1e-8
        planes.add(tuple(np.round(equation,8)))
    assert len(planes)==k*k
    distances=sorted(-eq[-1] for eq in planes)
    expected=sorted((float(sum(z*z for z in normal_formula(k,i,j))))**-.5
                    for i in range(k) for j in range(k))
    assert np.allclose(distances,expected,atol=1e-7)
    print(f'hull k={k}: independent convex-hull facets and distances agree')


if __name__ == '__main__':
    for k in range(2,15):
        test(k,independent=(k<=7))
    if '--hull' in argv:
        for k in range(2,7):
            hull(k)
    print('EXACT_CHECKS_PASS')
