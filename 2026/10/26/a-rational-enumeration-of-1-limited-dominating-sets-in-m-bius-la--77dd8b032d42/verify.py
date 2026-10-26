#!/usr/bin/env python3
"""Exact arithmetic checks for 1-limited domination on Möbius ladders.

Requires Python 3 only. Polynomial dictionaries use (t-degree, z-degree) keys.
The determinant routine is a direct Leibniz expansion via subset dynamic
programming, independent of symbolic-algebra libraries.
"""
from collections import defaultdict
from itertools import combinations


def plus(a, b):
    d = dict(a)
    for k, v in b.items():
        d[k] = d.get(k, 0) + v
        if not d[k]:
            del d[k]
    return d


def times(a, b):
    d = defaultdict(int)
    for (i, j), x in a.items():
        for (k, h), y in b.items():
            d[(i + k, j + h)] += x * y
    return {k: v for k, v in d.items() if v}


def scaled(a, k):
    return {ij: k*v for ij, v in a.items() if k*v}


def determinant(coeff):
    """Compute det(I-tA) as a bivariate polynomial exactly."""
    d = len(coeff)
    matrix = []
    for i in range(d):
        row = []
        for j in range(d):
            a = {(0, 0): 1} if i == j else {}
            for zdegree, v in coeff[i][j].items():
                a = plus(a, {(1, zdegree): -v})
            row.append(a)
        matrix.append(row)
    dp = {0: {(0, 0): 1}}
    for i in range(d):
        nxt = {}
        for mask, pol in dp.items():
            for j in range(d):
                if mask & (1 << j):
                    continue
                if not matrix[i][j]:
                    continue
                inversions = (mask >> (j+1)).bit_count()
                term = times(pol, matrix[i][j])
                if inversions % 2:
                    term = scaled(term, -1)
                new_mask = mask | (1 << j)
                nxt[new_mask] = plus(nxt.get(new_mask, {}), term)
        dp = nxt
    return dp[(1 << d)-1]


def matrix_from_edges(size, edges):
    a = [[{} for _ in range(size)] for _ in range(size)]
    for i, j, c, power in edges:
        a[i][j][power] = c
    return a

# Seven-state symmetric and three-state antisymmetric cyclic cores of the
# twisted column-pair transfer. Zero-eigenvalue transient states are omitted.
P = matrix_from_edges(7, [
    (0,0,1,0),(0,1,2,0),(0,2,1,0),
    (1,3,1,1),(1,4,1,1),
    (2,5,1,2),(2,6,1,2),
    (3,0,1,0),(3,1,1,0),
    (4,3,1,1),(4,4,1,1),
    (5,0,1,0),
    (6,5,1,2),
])
N = matrix_from_edges(3, [
    (0,1,1,1),(0,2,1,1),
    (1,0,-1,0),
    (2,1,1,1),(2,2,1,1),
])

def expected_determinants():
    # D_plus=(1-tz)(1-Q) where each item is (t power,z power,coefficient).
    Q = {(1,0):1, (2,1):1, (3,1):1, (3,2):2,
         (4,2):1, (4,3):1, (4,4):1, (5,4):1}
    base = plus({(0,0):1}, scaled(Q,-1))
    dp = times({(0,0):1,(1,1):-1}, base)
    dn = {(0,0):1,(1,1):-1,(2,1):1}
    return dp,dn


def det_trace(det, maximum):
    """Newton's identities yield trace(A^n) from det(I-tA)."""
    d = defaultdict(dict)
    for (tdeg,zdeg),c in det.items():
        if tdeg:
            d[tdeg][zdeg] = c
    ret = [{}]
    for n in range(1,maximum+1):
        v = {a: -n*c for a,c in d.get(n,{}).items()}
        for j in range(1,n):
            if j in d:
                for za,ca in d[j].items():
                    for zb,cb in ret[n-j].items():
                        k=za+zb
                        v[k]=v.get(k,0)-ca*cb
        ret.append({k:vl for k,vl in v.items() if vl})
    return ret


def full_transfer_trace(n):
    def colbit(c, r): return (c >> r) & 1
    def swap(c): return (c & 1)*2 + (c >> 1)
    pairs = [(p,c) for p in range(4) for c in range(4)]
    transitions = [[] for _ in range(16)]
    for i,(p,c) in enumerate(pairs):
        for q in range(4):
            if all(colbit(p,r)+colbit(q,r)+colbit(c,1-r)
                   <= 1+colbit(c,r) for r in range(2)):
                j=pairs.index((c,q))
                transitions[i].append((j,c.bit_count()))
    total=defaultdict(int)
    for s,(p,c) in enumerate(pairs):
        target=pairs.index((swap(p),swap(c)))
        dp={(s,0):1}
        for _ in range(n):
            nxt=defaultdict(int)
            for (state,w),count in dp.items():
                for j,inc in transitions[state]:
                    nxt[(j,w+inc)]+=count
            dp=nxt
        for (j,w),count in dp.items():
            if j==target:
                total[w]+=count
    return dict(total)


def brute(n):
    size=2*n
    adj=[]
    for v in range(size):
        adj.append(((v-1)%size,(v+1)%size,(v+n)%size))
    counts=defaultdict(int)
    # Count all size strata, without transfer-matrix assumptions.
    for k in range(size+1):
        for S in combinations(range(size),k):
            white=set(S)
            if all((sum(v in white for v in adj[u])<=1
                    if u not in white
                    else any(v not in white for v in adj[u]))
                   for u in range(size)):
                counts[k]+=1
    return dict(counts)


def main():
    dp=determinant(P); dn=determinant(N)
    xp,xn=expected_determinants()
    assert dp==xp,(dp,xp)
    assert dn==xn,(dn,xn)
    print('DETERMINANT_IDENTITIES_OK',len(dp),len(dn))
    p=det_trace(dp,50);m=det_trace(dn,50)
    for n in range(3,51):
        z={a:p[n].get(a,0)-m[n].get(a,0)
           for a in (p[n].keys()|m[n].keys())}
        z={a:b for a,b in z.items() if b}
        assert z==full_transfer_trace(n),(n,z,full_transfer_trace(n))
        mx=max(z)
        optimum=n if n%4==0 else n+1
        number=(4 if n%4==0 else (2*n if n%2==0 else 3*n))
        assert mx==2*n-optimum and z[mx]==number,(n,mx,z[mx])
        if n<=10:
            assert z==brute(n),(n,z,brute(n))
    print('TRACE_AND_OPTIMUM_IDENTITIES_OK n=3..50')
    print('INDEPENDENT_BRUTE_ENUMERATION_OK n=3..10')
    for n in range(3,11):
        Pn=full_transfer_trace(n)
        print('n=%d profile=%s'%(n,sorted(Pn.items())))
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
