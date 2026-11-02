#!/usr/bin/env python3
"""Exact modular checks for minimum coordinate actuation on rook graphs.

No external packages. The analytic all-size proof is in RESULT.md; tests are finite
regression checks, not a substitute for that proof.
"""
from itertools import combinations
from collections import Counter
from math import comb
P = 1000003


def rank(A):
    if not A:
        return 0
    A = [[int(z) % P for z in row] for row in A]
    rows, cols = len(A), len(A[0])
    assert all(len(row) == cols for row in A)
    r = 0
    for c in range(cols):
        t = next((i for i in range(r, rows) if A[i][c]), None)
        if t is None:
            continue
        A[r], A[t] = A[t], A[r]
        inv = pow(A[r][c], -1, P)
        A[r][c:] = [v * inv % P for v in A[r][c:]]
        for i in range(r + 1, rows):
            if A[i][c]:
                mul = A[i][c]
                A[i][c:] = [(a - mul * b) % P for a, b in zip(A[i][c:], A[r][c:])]
        r += 1
        if r == rows:
            break
    return r


def components(m, n, E):
    parent = list(range(m + n))
    def get(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for i, j in E:
        a, b = get(i), get(m + j)
        if a != b:
            parent[a] = b
    groups = {}
    for i in range(m + n):
        groups.setdefault(get(i), []).append(i)
    return list(groups.values())


def connected(m, n, E):
    return len(components(m, n, E)) == 1


def predicted(m, n, U):
    q = (m - 1) * (n - 1)
    if len(U) != q:
        raise ValueError('Only minimum-size placements are classified')
    T = {(i, j) for i in range(m) for j in range(n)} - set(U)
    if not connected(m, n, T):
        return False
    if m != n:
        return True
    C = components(m, n, U)
    if len(C) >= 3:
        return False
    if len(C) == 1:
        return True
    a = sum(x < m for x in C[0]); b = sum(x >= m for x in C[0])
    return a != b


def modal_controllable(m, n, U):
    def injective(eigenspace_basis):
        if not eigenspace_basis:
            return True
        return rank([[v[i*n+j] for v in eigenspace_basis] for i,j in U]) == len(eigenspace_basis)
    basis_hi=[]
    for i in range(m-1):
        for j in range(n-1):
            basis_hi.append([(int(a==i)-int(a==m-1))*(int(b==j)-int(b==n-1)) for a in range(m) for b in range(n)])
    if not injective(basis_hi):
        return False
    basis_m = [[int(a==i)-int(a==m-1) for a in range(m) for b in range(n)] for i in range(m-1)]
    basis_n = [[int(b==j)-int(b==n-1) for a in range(m) for b in range(n)] for j in range(n-1)]
    return injective(basis_m + basis_n) if m==n else injective(basis_m) and injective(basis_n)


def kalman_controllable(m, n, U):
    N=m*n; L=[[0]*N for _ in range(N)]
    for i in range(m):
        for j in range(n):
            a=i*n+j
            for k in range(N):
                if a!=k and (i==k//n or j==k%n):
                    L[a][k]=-1
            L[a][a]=m+n-2
    B=[[int(t == i*n+j) for i,j in U] for t in range(N)]
    block=[row[:] for row in B]
    current=B
    for s in range(1,N):
        current=[[sum(L[i][k]*current[k][j] for k in range(N)) % P for j in range(len(U))] for i in range(N)]
        for i in range(N):
            block[i].extend(current[i])
    return rank(block)==N


def zero_forcing(m, n, U):
    black=set(U)
    allvertices=set((i,j) for i in range(m) for j in range(n))
    while True:
        forced=set()
        for i,j in black:
            whites=[(a,b) for a,b in allvertices-black if (i==a or j==b)]
            if len(whites)==1:
                forced.add(whites[0])
        if not forced:
            return black==allvertices
        black.update(forced)


def run():
    total=0
    for m,n in [(3,3),(3,4),(4,4),(3,5)]:
        edges=[(i,j) for i in range(m) for j in range(n)]
        q=(m-1)*(n-1)
        count_tree=count_good=0
        bad=Counter()
        for U0 in combinations(edges,q):
            U=set(U0)
            T=set(edges)-U
            is_tree=connected(m,n,T)
            count_tree+=is_tree
            good=predicted(m,n,U)
            assert good==modal_controllable(m,n,U), (m,n,U)
            if m==3 and n==3:
                assert good==kalman_controllable(m,n,U),(m,n,U)
            if good:count_good+=1
            elif is_tree:
                cs=components(m,n,U)
                bad[tuple(sorted((sum(x<m for x in C),sum(x>=m for x in C)) for C in cs))]+=1
            total+=1
        assert count_tree==m**(n-1)*n**(m-1)
        target=(m**(n-1)*n**(m-1) if m!=n else n**(2*n-2)-n*n*((n-1)**2+1))
        assert count_good==target,(m,n,count_good,target)
        if m==n:
            assert sum(bad.values())==n*n*((n-1)**2+1)
            assert sorted(bad.values())==sorted([n*n,n*n*(n-1)**2])
        print('modal enumeration:',m,n,'subsets',comb(m*n,q),'trees',count_tree,'controllable',count_good,'bad-tree types',dict(bad))
    # Deterministic pseudo-samples of direct Kalman matrices for larger dimensions
    for m,n in [(3,4),(4,4)]:
        edges=[(i,j) for i in range(m) for j in range(n)]
        q=(m-1)*(n-1)
        sample=list(combinations(edges,q))
        ix=sorted(set([0,1,2,len(sample)//2,len(sample)-1]+list(range(0,len(sample),max(1,len(sample)//19)))))
        for j in ix:
            U=set(sample[j])
            assert predicted(m,n,U)==kalman_controllable(m,n,U),(m,n,j)
            total+=1
        print('direct Kalman modular checks:',m,n,len(ix))
    for m,n in [(3,3),(3,4)]:
        edges=[(i,j) for i in range(m) for j in range(n)]
        q=(m-1)*(n-1)
        assert not any(zero_forcing(m,n,set(U)) for U in combinations(edges,q))
        assert any(zero_forcing(m,n,set(U)) for U in combinations(edges,q+1))
        print('zero-forcing gap checked:',m,n,'Z=',q+1)
    print('PASS: exact modular modal and Kalman checks, full indicated finite searches; cases=',total)

if __name__ == '__main__':
    run()
