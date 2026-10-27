#!/usr/bin/env python3
"""Exact-rational checks for one-antagonistic-bridge FJ equilibrium identities.

Run: python3 verify.py
Only Python standard library is required. Finite checks are not an infinite proof.
"""
from fractions import Fraction as F
from random import Random


def solve(M, y):
    n = len(M)
    a = [[F(z) for z in row] + [F(y[i])] for i, row in enumerate(M)]
    for j in range(n):
        k = next((r for r in range(j, n) if a[r][j]), None)
        assert k is not None
        a[j], a[k] = a[k], a[j]
        v = a[j][j]
        a[j] = [x / v for x in a[j]]
        for i in range(n):
            if i == j:
                continue
            v = a[i][j]
            if v:
                a[i] = [a[i][k] - v * a[j][k] for k in range(n + 1)]
    return [a[i][-1] for i in range(n)]


def base_matrix(K, edges):
    n = len(K)
    M = [[F(0) for j in range(n)] for i in range(n)]
    for i, k in enumerate(K):
        M[i][i] += k
    for i, j, w in edges:
        M[i][i] += w
        M[j][j] += w
        M[i][j] -= w
        M[j][i] -= w
    return M


def model(K, edges, a, b, t):
    M = base_matrix(K, edges)
    M[a][a] += t
    M[b][b] += t
    M[a][b] += t
    M[b][a] += t
    return solve(M, K)


def bridge_formula(K, edges, na, a, b, t):
    n = len(K)
    L = base_matrix(K[:na], [(i,j,w) for i,j,w in edges if i < na])
    R = base_matrix(K[na:], [(i-na,j-na,w) for i,j,w in edges if i >= na])
    Ga = solve(L, [F(int(i == a)) for i in range(na)])
    Gb = solve(R, [F(int(i == b-na)) for i in range(n-na)])
    A = 1 / Ga[a]
    B = 1 / Gb[b-na]
    hL = [z / Ga[a] for z in Ga]
    hR = [z / Gb[b-na] for z in Gb]
    den = A*B + t*(A+B)
    predicted = [1-2*t*B*h/den for h in hL] + [1-2*t*A*h/den for h in hR]
    flip_side = 'left' if A < B else 'right' if B < A else 'none'
    for side, hs, other, self_ in [('left', hL, B, A), ('right', hR, A, B)]:
        for h in hs:
            c = 2*other*h-(A+B)
            w0 = A*B/c if c > 0 else None
            value = (A*B-t*c)/den
            assert value in predicted
            if w0 is None:
                assert value > 0
            else:
                assert side == flip_side
                assert (value < 0) == (t > w0)
                assert (value == 0) == (t == w0)
    return predicted, A, B, hL, hR


def run():
    checks = 0
    rng = Random(1729)
    values = [F(1,10), F(1,4), F(1,2), F(1), F(2), F(4)]
    weights = [F(1,3), F(1,2), F(1), F(2), F(3)]
    tvals = [F(1,5), F(1,2), F(1), F(3,2), F(2), F(3), F(8)]
    for sample in range(650):
        na = 1 + rng.randrange(4)
        nb = 1 + rng.randrange(4)
        n = na + nb
        K = [rng.choice(values) for _ in range(n)]
        a = rng.randrange(na)
        b = na + rng.randrange(nb)
        edges=[]
        for off, size in [(0,na),(na,nb)]:
            for j in range(1, size):
                edges.append((off+j-1,off+j,rng.choice(weights)))
            for i in range(size):
                for j in range(i+2,size):
                    if rng.randrange(2):
                        edges.append((off+i,off+j,rng.choice(weights)))
        for t in tvals:
            observed=model(K,edges,a,b,t)
            predicted,A,B,hL,hR=bridge_formula(K,edges,na,a,b,t)
            assert observed == predicted, (sample,t,observed,predicted)
            assert all(F(0) < h <= 1 for h in hL + hR)
            assert hL[a] == 1 and hR[b-na] == 1
            assert not (any(v < 0 for v in observed[:na]) and any(v < 0 for v in observed[na:]))
            for i in range(n):
                if observed[i] < 0:
                    assert (i < na and A < B) or (i >= na and B < A)
            # Every negative-opinion set is connected to its bridge root.
            adj = [[] for _ in range(n)]
            for i,j,_ in edges:
                adj[i].append(j)
                adj[j].append(i)
            roots = [a,b]
            for root,allowed in [(a,range(na)),(b,range(na,n))]:
                negatives={i for i in allowed if observed[i] < 0}
                if negatives:
                    assert root in negatives
                    seen={root}
                    queue=[root]
                    for v in queue:
                        for u in adj[v]:
                            if u in negatives and u not in seen:
                                seen.add(u);queue.append(u)
                    assert negatives==seen
            checks += 1
    # Exact three-agent illustration: left components c--a, antagonistic a--b.
    K=[F(1,10), F(1), F(4)]
    edges=[(0,1,F(1))]
    for t, want in [(F(1),[F(3,13),F(2,13),F(10,13)]),
                    (F(3,2),[F(1,11),F(0),F(8,11)]),
                    (F(2),[F(0),F(-1,10),F(7,10)]),
                    (F(3),[F(-1,9),F(-2,9),F(2,3)])]:
        x=model(K,edges,1,2,t)
        pred,*_=bridge_formula(K,edges,2,1,2,t)
        assert x==pred==want
        # Note node 0 flips after node 1.
        checks += 1
    # Even uniform anchoring can yield reversal through unequal topology.
    uniformK=[F(1),F(1),F(1)]
    positive_edge=[(1,2,F(1))]
    for t,want in [(F(3),[F(0),F(1,3),F(2,3)]),
                   (F(4),[F(-1,23),F(7,23),F(15,23)])]:
        x=model(uniformK,positive_edge,0,1,t)
        pred,*_=bridge_formula(uniformK,positive_edge,1,0,1,t)
        assert x==pred==want
        checks+=1
    print('EXACT_BRIDGE_VERIFICATION_OK',checks,'random/illustrative cases')

if __name__=='__main__':
    run()
