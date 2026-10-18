#!/usr/bin/env python3
"""Exact finite-graph bond-percolation check; Python standard library only.

Run: python3 verify.py
Every one of 2^9 edge states is traversed for each of the six roots
in both 3-regular graphs.  Integer polynomials are ascending in p.
"""
from itertools import combinations
from math import comb
from fractions import Fraction

N = 6
K = tuple((u, v) for u in range(3) for v in range(3, 6))
P = ((0, 1), (1, 2), (0, 2), (3, 4), (4, 5), (3, 5),
     (0, 3), (1, 4), (2, 5))
assert len(K) == len(P) == 9


def add(a, b):
    return [((a[i] if i < len(a) else 0) +
             (b[i] if i < len(b) else 0)) for i in range(max(len(a), len(b)))]


def multiply(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def scale(a, c):
    return [c*x for x in a]


def power(a, k):
    c = [1]
    for _ in range(k):
        c = multiply(c, a)
    return c


def equal(a, b):
    n = max(len(a), len(b))
    return all((a[i] if i < len(a) else 0) ==
               (b[i] if i < len(b) else 0) for i in range(n))


def component_size_bfs(edges, mask, root):
    adj = [set() for _ in range(N)]
    for j, (u, v) in enumerate(edges):
        if (mask >> j) & 1:
            adj[u].add(v)
            adj[v].add(u)
    seen = {root}
    queue = [root]
    for u in queue:
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                queue.append(v)
    return len(seen)


def component_size_union_find(edges, mask, root):
    par = list(range(N))
    def find(x):
        while par[x] != x:
            x = par[x]
        return x
    for j, (u, v) in enumerate(edges):
        if (mask >> j) & 1:
            a, b = find(u), find(v)
            par[a] = b
    return sum(find(i) == find(root) for i in range(N))


def distribution(edges):
    m = len(edges)
    counts = {(k, s): 0 for k in range(m+1) for s in range(1, N+1)}
    rooted = [{(k, s): 0 for k in range(m+1) for s in range(1, N+1)} for _ in range(N)]
    for mask in range(1 << m):
        k = mask.bit_count()
        for root in range(N):
            size = component_size_bfs(edges, mask, root)
            assert size == component_size_union_find(edges, mask, root)
            rooted[root][k, size] += 1
            counts[k, size] += 1
    assert all(rooted[r] == rooted[0] for r in range(1, N))
    total = 0
    for k in range(m+1):
        assert sum(counts[k, s] for s in range(1, N+1)) == N*comb(m, k)
        total += sum(counts[k, s] for s in range(1, N+1))
    assert total == N*(1 << m)
    # Graphs are vertex-transitive, so the uniform-root mean equals a fixed-root mean.
    polynomials = {}
    for s in range(1, N+1):
        polynomials[s] = [0]
        for k in range(m+1):
            count = counts[k, s]
            assert count % N == 0  # orbit-averaged polynomial coefficient is integral
            polynomials[s] = add(polynomials[s],
                                 scale(multiply(power([0, 1], k),
                                                power([1, -1], m-k)), count//N))
    assert equal([sum(polynomials[s][j] if j<len(polynomials[s]) else 0
                      for s in range(1,N+1)) for j in range(m+1)], [1])
    return polynomials


def tail(distribution, k):
    out = [0]
    for i in range(k, N+1):
        out = add(out, distribution[i])
    return out


def moment(distribution, power_):
    out = [0]
    for s in range(1, N+1):
        out = add(out, scale(distribution[s], s**power_))
    return out


def value(pol, p):
    return sum(c*p**i for i,c in enumerate(pol))


def all_cubic_six():
    edges = tuple(combinations(range(6), 2))
    seen_by_triangles = {0:0, 2:0}
    for mask in range(1<<15):
        if mask.bit_count()!=9:
            continue
        deg = [0]*6
        subset = []
        for j,(u,v) in enumerate(edges):
            if (mask>>j)&1:
                deg[u]+=1; deg[v]+=1; subset.append((u,v))
        if deg != [3]*6:
            continue
        tris = sum(all(tuple(sorted(e)) in set(subset) for e in ((a,b),(a,c),(b,c)))
                   for a,b,c in combinations(range(6),3))
        assert tris in (0,2)
        seen_by_triangles[tris]+=1
    assert all(v>0 for v in seen_by_triangles.values())
    return seen_by_triangles


def main():
    k_dist, p_dist = distribution(K), distribution(P)
    q = [20,-4,-34,-161,-26,248,596,-832,168,-823,1717,-1123,245]
    base = multiply(power([0,1], 3), power([1,-1], 3))
    for cutoff in range(2,7):
        delta = add(tail(k_dist,cutoff),scale(tail(p_dist,cutoff),-1))
        if cutoff < 4:
            assert equal(delta, [0])
        else:
            assert equal(delta,multiply(multiply(power([0,1],cutoff-4),base),
                                        [cutoff, -(cutoff-1)]))
    mK, mP = moment(k_dist,1), moment(p_dist,1)
    sK, sP = moment(k_dist,2), moment(p_dist,2)
    dmean = add(mK,scale(mP,-1))
    dvar = add(add(sK,scale(sP,-1)),
               add(scale(multiply(mK,mK),-1),multiply(mP,mP)))
    assert equal(dmean,multiply(base,[4,2,2,-5]))
    assert equal(dvar,multiply(base,q))
    # Convert Q(p) to (1+t)^12 Q(t/(1+t)); exactly one sign change.
    co = [sum(q[k]*comb(12-k,i-k) for k in range(i+1)) for i in range(13)]
    expected = [20,236,1242,3679,6235,4684,-2428,-8366,-7038,-3191,-870,-135,-9]
    assert co == expected
    assert all(x>0 for x in co[:6]) and all(x<0 for x in co[6:])
    assert value(q,Fraction(479,1000))>0
    assert value(q,Fraction(480,1000))<0
    assert value(q,Fraction(0))==20 and value(q,Fraction(1))==-9
    assert value(dmean,Fraction(1,2))==Fraction(39,512)
    assert value(dvar,Fraction(1,2))==-Fraction(5941,262144)
    assert value(mK,Fraction(1,2))==Fraction(2229,512)
    assert value(mP,Fraction(1,2))==Fraction(1095,256)
    assert value(add(sK,scale(multiply(mK,mK),-1)), Fraction(1,2))==Fraction(847367,262144)
    assert value(add(sP,scale(multiply(mP,mP),-1)), Fraction(1,2))==Fraction(213327,65536)
    cubic = all_cubic_six()
    print('PASS: 6144 rooted-edge-state traversals, 2 independent component algorithms')
    print('PASS: six cluster-size tails and two exact moment identities')
    print('PASS: unique variance threshold by one Descartes sign change')
    print('PASS: six-vertex cubic class triangle signatures',cubic)
    print('PASS: exact rational anchor values')

if __name__=='__main__':
    main()
