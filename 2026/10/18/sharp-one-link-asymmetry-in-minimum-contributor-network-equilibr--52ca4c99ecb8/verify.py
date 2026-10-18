"""Exact finite cross-check of independent domination under one-edge addition.
All computations use Python's standard library and integers only.
Run: python3 verify_bestshot_new.py
"""
from itertools import combinations


def independent_domination(n, edge_mask, pairs):
    closed = [1 << i for i in range(n)]
    for p, (u, v) in enumerate(pairs):
        if (edge_mask >> p) & 1:
            closed[u] |= 1 << v
            closed[v] |= 1 << u
    universe = (1 << n) - 1
    for size in range(1, n + 1):
        for nodes in combinations(range(n), size):
            selected = sum(1 << v for v in nodes)
            if any(closed[v] & selected != (1 << v) for v in nodes):
                continue
            union = 0
            for v in nodes:
                union |= closed[v]
            if union == universe:
                return size
    raise AssertionError('independent dominating set absent')


def connected(n, edge_mask, pairs):
    seen = 1
    while True:
        nxt = seen
        for p, (u, v) in enumerate(pairs):
            if (edge_mask >> p) & 1:
                if (seen >> u) & 1:
                    nxt |= 1 << v
                if (seen >> v) & 1:
                    nxt |= 1 << u
        if nxt == seen:
            return seen == ((1 << n) - 1)
        seen = nxt


def check_all(n):
    pairs = list(combinations(range(n), 2))
    full = (1 << len(pairs)) - 1
    hist = {}
    comparisons = 0
    for e in range(full + 1):
        if not connected(n, e, pairs):
            continue
        k = independent_domination(n, e, pairs)
        for bit in range(len(pairs)):
            if (e >> bit) & 1:
                continue
            h = independent_domination(n, e | (1 << bit), pairs)
            delta = h-k
            hist[delta] = hist.get(delta, 0)+1
            comparisons += 1
            assert -1 <= delta <= max(0, (n - 4) // 2), (n,e,bit,k,h)
    return comparisons, hist


def family(a, b):
    # vertices u=0,p=1,q=2,v=3; leaves of u, then leaves of v
    n = a+b+4
    pairs = list(combinations(range(n), 2))
    edges = {(0,1), (1,2), (2,3)}
    edges.update((0,i) for i in range(4,4+a))
    edges.update((3,i) for i in range(4+a,n))
    old = sum(1 << j for j,p in enumerate(pairs) if p in edges)
    new = old | (1 << pairs.index((0,3)))
    return independent_domination(n,old,pairs), independent_domination(n,new,pairs)


def improvement(n):
    # u=0, w=1, v=2; n-3 other leaves at u
    pairs = list(combinations(range(n),2))
    edges = {(0,1), (1,2)}
    edges.update((0,i) for i in range(3,n))
    g = sum(1 << i for i,p in enumerate(pairs) if p in edges)
    h = g | (1 << pairs.index((0,2)))
    return independent_domination(n,g,pairs), independent_domination(n,h,pairs)


def run():
    for n in range(3,7):
        comp,dist=check_all(n)
        print('n=',n,'comparisons=',comp,'delta_counts=',dict(sorted(dist.items())))
        assert max(dist) == max(0,(n-4)//2)
        if n>=4: assert min(dist)==-1
    for n in range(4,15):
        assert improvement(n)==(2,1)
    for n in range(6,15):
        a=(n-4)//2
        b=n-4-a
        assert family(a,b)==(2,a+2), (n,a,b,family(a,b))
    print('Constructions verified for orders 4..14. All assertions passed.')

if __name__ == '__main__':
    run()
