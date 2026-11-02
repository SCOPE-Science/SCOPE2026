"""Reproduce finite checks for dense-bipartite geodesic-convexity rigidity.

Requires only Python's standard library; all graphs are unweighted and simple.
"""
import itertools
import random
from collections import deque
from functools import lru_cache


def make_graph(p, q, missing):
    if not all(0 <= i < p and 0 <= j < q for i, j in missing):
        raise ValueError('Out-of-range deleted edge')
    adj = [set() for _ in range(p + q)]
    for i in range(p):
        for j in range(q):
            if (i, j) not in missing:
                adj[i].add(p + j)
                adj[p + j].add(i)
    return adj


def distances(adj):
    n = len(adj)
    out = []
    for src in range(n):
        row = [n + 1] * n
        row[src] = 0
        todo = deque([src])
        while todo:
            x = todo.popleft()
            for y in adj[x]:
                if row[y] > row[x] + 1:
                    row[y] = row[x] + 1
                    todo.append(y)
        out.append(row)
    return out


def geodesic_intervals(d):
    n = len(d)
    return {(x, y):sum(1 << z for z in range(n)
        if d[x][z] + d[z][y] == d[x][y])
        for x in range(n) for y in range(x + 1,n)}


def hull(bits, n, intervals):
    while True:
        old = bits
        points = [v for v in range(n) if (bits >> v) & 1]
        for i, x in enumerate(points):
            for y in points[i + 1:]:
                bits |= intervals[x, y]
        if bits == old:
            return bits


def convex_sets(adj):
    n = len(adj)
    intervals = geodesic_intervals(distances(adj))
    return [s for s in range(1 << n) if hull(s, n, intervals) == s]


def expected_sets(adj):
    n = len(adj)
    ans = {0,(1 << n) - 1}
    ans.update(1 << v for v in range(n))
    ans.update((1 << x) | (1 << y) for x in range(n) for y in adj[x])
    return ans


def check_bipartite_degree(p,q,missing,t):
    return (max((sum(i == x for i,j in missing) for x in range(p)),default=0) <= t
        and max((sum(j == y for i,j in missing) for y in range(q)),default=0) <= t)


def pair_hulls_are_universal(adj):
    n=len(adj)
    D=distances(adj)
    if any(D[x][y]>n for x in range(n) for y in range(n)):
        return False
    intervals=geodesic_intervals(D)
    full=(1<<n)-1
    for x in range(n):
        for y in range(x+1,n):
            if y not in adj[x] and hull((1<<x)|(1<<y),n,intervals)!=full:
                return False
    return True


def ldim(concepts,n):
    masks=[sum(1<<j for j,c in enumerate(concepts) if c>>v&1)
           for v in range(n)]
    @lru_cache(None)
    def rec(versions):
        ans=0
        for m in masks:
            yes=versions&m
            no=versions&~m
            if yes and no:
                ans=max(ans,1+min(rec(yes),rec(no)))
        return ans
    return rec((1<<len(concepts))-1)


def extremal_missing(t):
    n=2*t+2
    # A={0,1} on the left, B={0,1} on the right.
    # Every other right vertex misses exactly one of A.
    missing={(0,j) for j in range(2,2+t)}
    missing.update((1,j) for j in range(2+t,n))
    # Every other left vertex misses exactly one of B.
    missing.update((i,0) for i in range(2,2+t))
    missing.update((i,1) for i in range(2+t,n))
    return n,missing


def randomized_complement(p,q,t,random_state):
    rows=[0]*p;cols=[0]*q;missing=set()
    edges=list(itertools.product(range(p),range(q)))
    random_state.shuffle(edges)
    for i,j in edges:
        if rows[i]<t and cols[j]<t and random_state.random()<0.8:
            missing.add((i,j));rows[i]+=1;cols[j]+=1
    return missing


def run():
    # Every bipartite complement of maximum degree one is a partial matching.
    # Up to permutations of its two sides only its number of deleted edges matters.
    for p in (5,6):
        for count in range(p+1):
            missing={(i,i) for i in range(count)}
            adj=make_graph(p,p,missing)
            c=convex_sets(adj)
            assert set(c)==expected_sets(adj),(p,count,len(c))
        print(f'EXACT_COMPLEMENT_DEGREE_ONE_PASS side_order={p} isomorphism_types={p+1}')

    for t in range(1,6):
        n,missing=extremal_missing(t)
        adj=make_graph(n,n,missing)
        assert check_bipartite_degree(n,n,missing,t)
        d=distances(adj);ints=geodesic_intervals(d)
        four=(1<<0)|(1<<1)|(1<<n)|(1<<(n+1))
        assert hull(four,2*n,ints)==four
        assert four not in expected_sets(adj)
        print(f'SHARP_BOUNDARY_PASS defect_degree={t} side_order={n}')

    rand=random.Random(3042026)
    tested=0
    for t,p,q,cases in [(1,5,5,30),(1,5,7,30),(2,7,7,45),
                       (2,7,9,30),(3,9,9,30),(3,9,11,20)]:
        for _ in range(cases):
            missing=randomized_complement(p,q,t,rand)
            assert check_bipartite_degree(p,q,missing,t)
            adj=make_graph(p,q,missing)
            assert pair_hulls_are_universal(adj),(t,p,q,missing)
            tested+=1
        print(f'RIGIDITY_SAMPLED_PASS max_missing_degree={t} side_orders={p},{q} tested={cases}')

    crown=make_graph(5,5,{(i,i) for i in range(5)})
    classes=convex_sets(crown)
    assert len(classes)==32
    assert set(classes)==expected_sets(crown)
    assert ldim(classes,10)==3
    assert all(sum(bool((c>>v)&1) for c in classes)>0 for v in range(10))
    print('CROWN_EXACT_LEARNING_PASS side_order=5 concepts=32 vc=2 littlestone=3')
    print(f'ALL_DENSE_BIPARTITE_RIGIDITY_CHECKS_PASS randomized_graphs={tested}')

if __name__=='__main__':
    run()
