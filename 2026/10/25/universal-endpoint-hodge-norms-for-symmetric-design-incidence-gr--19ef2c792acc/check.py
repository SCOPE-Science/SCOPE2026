#!/usr/bin/env python3
"""Exact, standalone rational incidence-graph cut/cycle projection checks.

Only standard-library modules are required. The checks recompute a grounded
Laplacian inverse, rather than using the closed-form voltage solution.
"""
from fractions import Fraction as F


def design_blocks(name):
    if name == "paley11":
        residues = {1, 3, 4, 5, 9}
        v = 11
        return v, [frozenset((a + d) % v for d in residues) for a in range(v)]
    if name == "pg3binary":
        v = 15
        return v, [frozenset(x - 1 for x in range(1, 16)
                             if (a & x).bit_count() % 2 == 0)
                   for a in range(1, 16)]
    raise ValueError(name)


def inverse(a):
    n = len(a)
    b = [[F(a[i][j]) for j in range(n)] + [F(i == j) for j in range(n)]
         for i in range(n)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if b[i][j])
        b[j], b[pivot] = b[pivot], b[j]
        c = b[j][j]
        b[j] = [z / c for z in b[j]]
        for i in range(n):
            if i != j:
                c = b[i][j]
                if c:
                    b[i] = [u - c * z for u, z in zip(b[i], b[j])]
    return [row[n:] for row in b]


def run(v, blocks):
    assert len(blocks) == v and len(set(blocks)) == v
    k = len(blocks[0]); assert all(len(b) == k for b in blocks)
    from itertools import combinations
    vals = {sum({p,q} <= b for b in blocks) for p, q in combinations(range(v), 2)}
    assert len(vals) == 1
    lam = vals.pop()
    assert 2 <= lam <= k-2, (v, k, lam)
    assert all(sum(p in b for b in blocks) == k for p in range(v))
    assert k*(k-1) == lam*(v-1)
    assert all(len(x & y) == lam for x,y in combinations(blocks,2))
    edges = [(p, v+j) for j,b in enumerate(blocks) for p in sorted(b)]
    n = 2*v
    # Node 2v-1 is grounded; the rest form the principal Laplacian minor.
    L = [[0]*(n-1) for _ in range(n-1)]
    for a,b in edges:
        if a < n-1: L[a][a] += 1
        if b < n-1: L[b][b] += 1
        if a < n-1 and b < n-1:
            L[a][b] -= 1
            L[b][a] -= 1
    inv = inverse(L)
    edge_vecs = [tuple((1 if a == z else -1 if b == z else 0)
                       for z in range(n-1)) for a,b in edges]
    qcols = []
    pcols = []
    for a,b in edges:
        # Grounded potentials for a point-to-block unit dipole.
        ph = [inv[i][a]-(inv[i][b] if b < n-1 else 0) for i in range(n-1)]
        ph.append(F(0))
        col = [ph[s]-ph[t] for s,t in edges]
        assert 0 < col[edges.index((a,b))] < 1
        qcols.append(sum(map(abs,col)))
        pcols.append(sum(abs(F(i==edges.index((a,b))) - val)
                         for i,val in enumerate(col)))
    q = F(5*k**3-4*k*k*lam-9*k*k+2*k*lam*lam+7*k*lam+4*k-2*lam*lam-2*lam,
          k*(k*k-k+lam))
    p = F(2*(k-1)*(3*k*k-2*k*lam-4*k+lam*lam+2*lam),
          k*(k*k-k+lam))
    assert all(z == q for z in qcols),(v,k,lam,qcols[:10],q)
    assert all(z == p for z in pcols),(v,k,lam,pcols[:10],p)
    return (v,k,lam,len(edges),str(q),str(p))


def main():
    data=[]
    for name in ("paley11", "pg3binary"):
        v, blocks = design_blocks(name)
        data.append(run(v, blocks))
        compl = [frozenset(set(range(v))-b) for b in blocks]
        data.append(run(v, compl))
    for d in data: print("v=%s k=%s lambda=%s edges=%s Q=%s P=%s" % d)
    print("SYMMETRIC_DESIGN_ENDPOINT_EXACT_OK designs=%d columns=%d" %
          (len(data), sum(z[3] for z in data)))

if __name__ == '__main__': main()
