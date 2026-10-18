#!/usr/bin/env python3
"""Exact independent finite checks of homogeneous-survival unrooted PD.

Uses only the Python standard library; no numerical threshold solver is trusted.
Analytical uniqueness and universal size bound are proved in RESULT.md.
"""
from fractions import Fraction as Q
from math import comb


def split_sizes(vertices, edges, leaves):
    adj = {v: set() for v in vertices}
    for u, v, w in edges:
        adj[u].add(v); adj[v].add(u)
    assert all(len(adj[v]) == 1 for v in leaves)
    result = []
    for u, v, w in edges:
        reached, frontier = {u}, [u]
        while frontier:
            x = frontier.pop()
            for y in adj[x]:
                if {x, y} == {u, v}:
                    continue
                if y not in reached:
                    reached.add(y); frontier.append(y)
        a = len(reached.intersection(leaves))
        assert 1 <= a < len(leaves)
        result.append((a, len(leaves) - a, Q(w), reached))
    return result


def direct_poly_in_q(vertices, edges, leaves):
    # Enumerate each possible survivor subset and compute PD by deleting
    # edges which have no surviving leaf on one side.
    spl = split_sizes(vertices, edges, leaves)
    n = len(leaves)
    coefficients = [Q(0) for _ in range(n + 1)]
    for mask in range(1 << n):
        survivors = {leaves[i] for i in range(n) if (mask >> i) & 1}
        k = len(survivors)
        pd = sum((w for a, b, w, part in spl
                  if survivors.intersection(part)
                  and survivors.difference(part)), Q(0))
        # (1-q)^k * q^(n-k)
        for j in range(k + 1):
            coefficients[n - k + j] += pd * (-1 if j % 2 else 1) * comb(k, j)
    return coefficients


def edge_poly_in_q(vertices, edges, leaves):
    n = len(leaves)
    coefficients = [Q(0) for _ in range(n + 1)]
    for a, b, w, part in split_sizes(vertices, edges, leaves):
        coefficients[0] += w
        coefficients[a] -= w
        coefficients[b] -= w
        coefficients[n] += w
    return coefficients


def second(poly, q):
    return sum((k*(k-1)*c*q**(k-2) for k,c in enumerate(poly) if k >= 2), Q(0))


def evaluate(poly, q):
    return sum((c*q**k for k,c in enumerate(poly)), Q(0))


def check(tree):
    vertices, edges, leaves = tree
    p1=direct_poly_in_q(vertices, edges, leaves)
    p2=edge_poly_in_q(vertices, edges, leaves)
    assert p1 == p2, (p1, p2)
    n = len(leaves)
    for qq in [Q(1,100), Q(1,10), Q(1,4), Q(1,2), Q(3,4), Q(9,10), Q(99,100)]:
        for a,b,w,side in split_sizes(vertices, edges, leaves):
            assert Q(1)-qq**a-qq**b+qq**n == (1-qq**a)*(1-qq**b)
    assert second(p2,Q(1)) == sum((2*a*b*w for a,b,w,_ in split_sizes(vertices,edges,leaves)),Q(0))
    q0 = Q(n-2,n)
    assert second(p2,q0) <= 0, (n,second(p2,q0))
    for mean, delta, expected_sign in [(Q(1,10),Q(1,100),1), (Q(9,10),Q(1,100),-1)]:
        gap=(evaluate(p2,1-mean-delta)+evaluate(p2,1-mean+delta))/2-evaluate(p2,1-mean)
        assert gap*expected_sign>0, (mean,gap)
    return p2


def main():
    trees=[]
    for n in range(3,9):
        c=n
        edges=[(i,c,(i%3)+1) for i in range(n)]
        trees.append((list(range(n+1)),edges,list(range(n))))
    trees.append((list(range(6)),[(0,4,1),(1,4,1),(4,5,2),(5,2,1),(5,3,1)],list(range(4))))
    trees.append((list(range(8)),[(0,5,1),(1,5,2),(5,6,3),(2,6,1),(6,7,2),(3,7,1),(4,7,3)],list(range(5))))
    for j,t in enumerate(trees):
        p=check(t)
        print('tree',j,'leaves',len(t[2]),'coefficients_in_q',str(p))
    unitquart=(list(range(6)),[(0,4,1),(1,4,1),(4,5,2),(5,2,1),(5,3,1)],list(range(4)))
    pq=check(unitquart)
    assert pq == [Q(6),Q(-4),Q(-4),Q(-4),Q(6)]
    assert second(pq,Q(1,2)) == Q(-2)
    assert second(pq,Q(3,5)) == Q(88,25)
    print('PASS: 8 star/branching trees, exact survival-subset enumeration, coefficient identity, curvature endpoints, size bound, and Jensen witnesses')

if __name__=='__main__':
    main()
