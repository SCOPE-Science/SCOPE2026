"""Finite checks of an extremal common-knowledge depth classification.
Standard-library Python, no external packages.
Run: python checker.py
"""
from itertools import product
from math import comb, factorial
from collections import deque


def set_partitions(n):
    """Each partition as tuple of disjoint increasing-label blocks."""
    def visit(next_value, blocks):
        if next_value == n:
            yield tuple(tuple(b) for b in blocks)
            return
        for j in range(len(blocks)):
            blocks[j].append(next_value)
            yield from visit(next_value + 1, blocks)
            blocks[j].pop()
        blocks.append([next_value])
        yield from visit(next_value + 1, blocks)
        blocks.pop()
    yield from visit(0, [])


def make_relation(blocks, n):
    result = [set() for _ in range(n)]
    for block in blocks:
        for u in block:
            result[u].update(block)
    return tuple(frozenset(v) for v in result)


def union_diameter(rels, n):
    neighbours = [set().union(*(r[u] for r in rels)) for u in range(n)]
    components_diameter = 0
    for src in range(n):
        ds = {src:0}; queue = deque([src])
        while queue:
            u=queue.popleft()
            for v in neighbours[u]:
                if v not in ds:
                    ds[v]=ds[u]+1
                    queue.append(v)
        components_diameter=max(components_diameter,max(ds.values()))
    return components_diameter, neighbours


def path_type(rels, n):
    _, g=union_diameter(rels,n)
    adj=[set(x)-{i} for i,x in enumerate(g)]
    if n==2:
        if adj[0]!={1}:return False
        ordered=(0,1)
    else:
        endpoints=[i for i,a in enumerate(adj) if len(a)==1]
        if len(endpoints)!=2 or any(len(a) > 2 for a in adj):return False
        ordered=[min(endpoints)]; prev=-1
        while len(ordered)<n:
            options=adj[ordered[-1]]-{prev}
            if len(options)!=1:return False
            nextpoint=next(iter(options))
            if nextpoint in ordered:return False
            prev=ordered[-1];ordered.append(nextpoint)
        if len(adj[ordered[-1]])!=1:return False
        ordered=tuple(ordered)
    colors=[]
    for a,b in zip(ordered,ordered[1:]):
        cover={j for j,r in enumerate(rels) if b in r[a]}
        if not cover:return False
        colors.append(cover)
    return all(not (colors[i]&colors[i+1]) for i in range(len(colors)-1))


def counted(k,n):
    if n==1:return 1
    if n==2:return 2**k-1
    vec={s:1 for s in range(1,k)}
    for _ in range(n-2):
        vec={s:sum(comb(k-s,t)*vec[t] for t in range(1,k-s+1)) for s in range(1,k)}
    return factorial(n)//2*sum(comb(k,s)*vec[s] for s in range(1,k))


def semantics_check(rels, n):
    # Test the actual finite approximant as a truth-set operation, not only graph diameter.
    adjacency = [set().union(*(r[u] for r in rels)) for u in range(n)]
    distances = []
    for src in range(n):
        d = {src: 0}; pending = deque([src])
        while pending:
            u = pending.popleft()
            for v in adjacency[u]:
                if v not in d:
                    d[v] = d[u] + 1
                    pending.append(v)
        distances.append(d)
    trials = 0
    for bits in range(1 << n):
        proposition = {v for v in range(n) if bits & (1 << v)}
        truth_set = proposition.copy()
        for radius in range(n):
            expected = {u for u in range(n)
                        if all(v in proposition for v, dist in distances[u].items()
                               if dist <= radius)}
            assert truth_set == expected, (n, rels, bits, radius)
            truth_set = proposition & {u for u in range(n)
                                       if all(r[u] <= truth_set for r in rels)}
            trials += 1
        common = {u for u in range(n)
                  if all(v in proposition for v in distances[u])}
        assert truth_set == common
    return trials


def independent_sequence_count(k, m):
    masks = list(range(1, 1 << k))
    def count(previous, length):
        if length == 0:
            return 1
        return sum(count(mask, length - 1) for mask in masks
                   if not previous or not (previous & mask))
    return count(0, m)


def check():
    examined=0; truth_tests=0
    for n,k in [(1,2),(2,2),(3,2),(4,2),(5,2),(2,3),(3,3),(4,3),(2,4),(3,4)]:
        rels=[make_relation(p,n) for p in set_partitions(n)]
        hist={};ext=0
        for tup in product(rels,repeat=k):
            diam,_=union_diameter(tup,n)
            pred=path_type(tup,n) if n>=2 else diam==0
            assert (diam==n-1)==pred, (n,k,diam,pred,tup)
            if n <= 4 and k <= 3:
                truth_tests += semantics_check(tup, n)
            hist[diam]=hist.get(diam,0)+1
            ext += diam==n-1
            examined+=1
        expected=counted(k,n)
        assert ext==expected,(n,k,ext,expected)
        print('n',n,'k',k,'frames',len(rels)**k,'diameter_hist',sorted(hist.items()),'extremals',ext)
    for k in range(2, 5):
        for m in range(1, 7):
            expected = independent_sequence_count(k, m)
            computed = counted(k, m + 1) // (factorial(m + 1) // 2)
            assert expected == computed, (k, m, expected, computed)
    print('OK, exhaustive frames checked:', examined)
    print('OK, finite approximant truth-set steps checked:', truth_tests)
    print('OK, independently enumerated nonempty disjoint-subset words: 18 parameter cases')

if __name__=='__main__':check()
