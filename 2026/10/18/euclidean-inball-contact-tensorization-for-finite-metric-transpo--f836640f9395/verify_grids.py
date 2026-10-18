"""Exact finite checks for grid transportation-ball inradius and contact facets.

Run with Python 3 standard library only: python verify_grids.py.
The theorem for arbitrary grid dimensions is proved separately; this is
finite corroboration, not a proof of the infinite-family assertion.
"""
from fractions import Fraction
from itertools import product
from collections import deque


def rank_over_q(matrix):
    if not matrix:
        return 0
    a = [[Fraction(v) for v in row] for row in matrix]
    n, m = len(a), len(a[0])
    row = 0
    for col in range(m):
        pivot = next((r for r in range(row, n) if a[r][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        pivot_val = a[row][col]
        a[row] = [v / pivot_val for v in a[row]]
        for r in range(n):
            if r != row and a[r][col]:
                factor = a[r][col]
                a[r] = [x-factor*y for x, y in zip(a[r], a[row])]
        row += 1
        if row == n:
            break
    return row


def inspect_grid(sizes):
    vs = list(product(*(range(k) for k in sizes)))
    index = {v:i for i,v in enumerate(vs)}
    n = len(vs)
    edges=[]
    for v in vs:
        for i,k in enumerate(sizes):
            if v[i]+1 < k:
                w=list(v);w[i]+=1
                edges.append((index[v],index[tuple(w)]))
    adj=[[] for _ in vs]
    for u,v in edges:
        adj[u].append(v);adj[v].append(u)
    parents=[None]*n
    parents[0]=0
    q=deque([0])
    order=[]
    while q:
        u=q.popleft()
        for v in adj[u]:
            if parents[v] is None:
                parents[v]=u
                order.append(v)
                q.append(v)
    assert len(order)==n-1
    target = Fraction(n*n,12) * sum(k*k-1 for k in sizes)
    assert target.denominator==1
    best=-1
    maximizers=[]
    total=0
    for mask in range(1<<(n-1)):
        f=[0]*n
        for j,v in enumerate(order):
            f[v]=f[parents[v]] + (1 if mask>>j&1 else -1)
        if any(abs(f[u]-f[v])!=1 for u,v in edges):
            continue
        total+=1
        sq=n*sum(x*x for x in f)-sum(f)**2
        if sq>best:
            best=sq;maximizers=[]
        if sq==best:
            maximizers.append(f)
    assert best==target,(sizes,best,target)
    assert len(maximizers)==2**len(sizes),(sizes,len(maximizers))
    normals=[[n*x-sum(f) for x in f] for f in maximizers]
    assert rank_over_q(normals)==len(sizes)
    expected={tuple(sum(signs[i]*v[i] for i in range(len(sizes))) for v in vs) for signs in product((-1,1),repeat=len(sizes))}
    assert {tuple(f) for f in maximizers} == expected
    print('sizes',sizes,'vertices',n,'facets',total,'max_scaled_norm_squared',best,
          'contacts',len(maximizers),'normal_rank',rank_over_q(normals),
          'incenter_affine_dimension',n-1-len(sizes))


def main():
    for sizes in ((2,2),(2,3),(3,3),(2,2,2),(2,2,3),(2,3,3),(2,2,2,2)):
        inspect_grid(sizes)
    print('ALL EXACT FINITE CHECKS PASSED')


if __name__ == '__main__':
    main()
