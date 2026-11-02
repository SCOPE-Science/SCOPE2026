#!/usr/bin/env python3
"""Exact, standard-library verification of the Fermat-quartic 48-line graph critical group.
The graph is derived independently by determinants over Z[zeta_8]."""
from collections import Counter, deque
from itertools import permutations
from math import prod

PAIRS = (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))
VERTICES = [(p, a, b) for p in range(3) for a in range(4) for b in range(4)]
N = len(VERTICES)
PERMS = [(perm, -1 if sum(perm[i] > perm[j] for i in range(4) for j in range(i + 1, 4)) % 2 else 1)
         for perm in permutations(range(4))]


def line_rows(label):
    p, a, b = label
    (i, j), (k, ell) = PAIRS[p]
    # A row dictionary index -> (integer coefficient sign, power of primitive zeta_8).
    return [{i: (1, 0), j: (-1, 2*a+1)},
            {k: (1, 0), ell: (-1, 2*b+1)}]


def det4(rowmaps):
    # Exact determinant in Z[zeta_8], using zeta_8^4 = -1.
    ans = [0] * 4
    for perm, parity in PERMS:
        coeff, exp = parity, 0
        for i, j in enumerate(perm):
            term = rowmaps[i].get(j)
            if term is None:
                coeff = 0
                break
            coeff *= term[0]
            exp += term[1]
        if coeff:
            exp %= 8
            if exp >= 4:
                coeff = -coeff
                exp -= 4
            ans[exp] += coeff
    return tuple(ans)


def formula_intersect(u, v):
    p, a, b = u
    q, c, d = v
    if p == q:
        return a == c or b == d
    if (p, q) == (0, 1):
        return (a + d - c - b) % 4 == 0
    if (p, q) == (0, 2):
        return (a + b + d + 1 - c) % 4 == 0
    if (p, q) == (1, 2):
        return (a + b - c - d) % 4 == 0
    raise ValueError((p, q))


def build_graph():
    assert N == 48 and len(set(VERTICES)) == 48
    a = [[0]*N for _ in range(N)]
    rows = [line_rows(v) for v in VERTICES]
    same = cross = 0
    for i in range(N):
        for j in range(i + 1, N):
            exact = det4(rows[i] + rows[j]) == (0, 0, 0, 0)
            predicted = formula_intersect(VERTICES[i], VERTICES[j])
            assert exact == predicted, (VERTICES[i], VERTICES[j])
            a[i][j] = a[j][i] = int(exact)
            if exact:
                if VERTICES[i][0] == VERTICES[j][0]:
                    same += 1
                else:
                    cross += 1
    assert same == 144 and cross == 192
    assert all(sum(row) == 14 for row in a)
    visited = {0}
    queue = deque([0])
    while queue:
        i = queue.popleft()
        for j, edge in enumerate(a[i]):
            if edge and j not in visited:
                visited.add(j); queue.append(j)
    assert len(visited) == N
    print('EXACT_CYCLOTOMIC_INTERSECTIONS_OK: 48 lines, 144 same-family edges, 192 cross-family edges; 14-regular connected')
    return a


def multiply(a, b):
    n = len(a)
    z = [[0]*n for _ in range(n)]
    for i in range(n):
        row = z[i]
        for k, ak in enumerate(a[i]):
            if ak:
                bk = b[k]
                for j in range(n):
                    row[j] += ak*bk[j]
    return z


def diagonal_trace(a):
    return sum(a[i][i] for i in range(len(a)))


def spectrum(a):
    n=len(a)
    eye=[[int(i==j) for j in range(n)] for i in range(n)]
    current=eye
    traces=[n]
    for power in range(1,5):
        current=multiply(current,a)
        traces.append(diagonal_trace(current))
    roots=[14,2,-2,-6,-10]
    multiplicities=[1,28,12,6,1]
    assert all(traces[k] == sum(m*(r**k) for m,r in zip(multiplicities,roots)) for k in range(5))
    # Annihilating polynomial confirms every eigenvalue belongs to the above set.
    poly=eye
    for root in roots:
        t=[[a[i][j]-int(i==j)*root for j in range(n)] for i in range(n)]
        poly=multiply(poly,t)
    assert all(all(x==0 for x in row) for row in poly)
    # A is symmetric, hence diagonalizable; Vandermonde uniqueness gives the multiplicities.
    print('EXACT_SPECTRUM_OK: 14^1, 2^28, (-2)^12, (-6)^6, (-10)^1')
    return roots,multiplicities


def padic_valuations(mat,p,K):
    """Local unimodular diagonalization modulo p^K, with K > v_p(det)."""
    n=len(mat)
    mod=p**K
    a=[[value%mod for value in row] for row in mat]
    i=0
    offset=0
    exponents=[]
    while i<n:
        unit=None
        for j in range(i,n):
            for k in range(i,n):
                if a[j][k]%p:
                    unit=(j,k)
                    break
            if unit is not None:break
        if unit is None:
            assert offset < K
            for j in range(i,n):
                for k in range(i,n):
                    assert a[j][k]%p==0
                    a[j][k]//=p
            mod//=p
            offset+=1
            continue
        j,k=unit
        a[i],a[j]=a[j],a[i]
        for row in a:
            row[i],row[k]=row[k],row[i]
        inv=pow(a[i][i],-1,mod)
        for j in range(i+1,n):
            factor=a[j][i]*inv%mod
            if factor:
                for k in range(i+1,n):
                    a[j][k]=(a[j][k]-factor*a[i][k])%mod
            a[j][i]=0
        exponents.append(offset)
        i+=1
    return exponents


def critical_group(a,roots,multiplicities):
    n=len(a)
    lap=[[14*int(i==j)-a[i][j] for j in range(n)] for i in range(n)]
    reduced=[row[:-1] for row in lap[:-1]]
    # Matrix-tree theorem; 14 eigenvalue of A supplies the lone zero Laplacian eigenvalue.
    tree_count=prod((14-r)**m for r,m in zip(roots[1:],multiplicities[1:]))//n
    assert tree_count == 2**115 * 3**28 * 5**6
    dic={}
    for p, exponent in ((2,115),(3,28),(5,6)):
        vals=padic_valuations(reduced,p,exponent+1)
        assert len(vals)==n-1 and sum(vals)==exponent
        dic[p]=sorted(vals)
        print('LOCAL_SMITH_CERTIFICATE_OK',p,sorted(Counter(vals).items()))
    invariants=[prod(p**dic[p][i] for p in (2,3,5)) for i in range(n-1)]
    assert all(invariants[i+1]%invariants[i]==0 for i in range(n-2))
    expected=Counter({1:18,4:2,12:10,24:5,192:6,960:2,1920:3,5760:1})
    assert Counter(invariants)==expected
    assert prod(invariants)==tree_count
    print('INVARIANT_FACTORS_OK',sorted(Counter(invariants).items()))
    print('CRITICAL_GROUP_ORDER=2^115*3^28*5^6; EXPONENT=5760')
    print('VERIFY_OK')


def main():
    a=build_graph()
    roots, multiplicities=spectrum(a)
    critical_group(a,roots,multiplicities)

if __name__ == '__main__':
    main()
