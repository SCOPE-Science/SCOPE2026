"""Independent exhaustive certificate: all DAGs on up to six points.
Topological edge-subset generation, globally synchronized directed color refinement,
and exact backtracking isomorphism constrained by refinement colors. Python 3 stdlib only.
"""
from collections import defaultdict


def dag(n, mask):
    adj = [0]*n
    k = 0
    for i in range(n):
        for j in range(i+1, n):
            if mask & (1 << k): adj[i] |= 1 << j
            k += 1
    return adj


def isomorphic(a, b, ca, cb):
    n = len(a)
    candidates = [tuple(j for j in range(n) if cb[j] == ca[i]) for i in range(n)]
    order = sorted(range(n), key=lambda i: len(candidates[i]))
    pairing = [-1]*n
    used = [False]*n
    def visit(t):
        if t == n: return True
        v = order[t]
        for w in candidates[v]:
            if used[w]: continue
            if any(bool(a[v] & (1 << x)) != bool(b[w] & (1 << pairing[x])) or
                   bool(a[x] & (1 << v)) != bool(b[pairing[x]] & (1 << w))
                   for x in order[:t]):continue
            pairing[v] = w; used[w] = True
            if visit(t+1): return True
            used[w] = False; pairing[v] = -1
        return False
    return visit(0)


def verify(n):
    N = 1 << (n*(n-1)//2)
    G = [dag(n, i) for i in range(N)]
    # Every DAG has a topological order; its relabeled adjacency appears in G.
    inn = [[tuple(i for i in range(n) if g[i] & (1 << v)) for v in range(n)] for g in G]
    out = [[tuple(j for j in range(n) if g[v] & (1 << j)) for v in range(n)] for g in G]
    color = [[0]*n for _ in G]
    for step in range(n+1):
        keys = [(color[i][v],tuple(sorted(color[i][u] for u in inn[i][v])),
                 tuple(sorted(color[i][u] for u in out[i][v])))
                for i in range(N) for v in range(n)]
        dictionary = {key:k for k,key in enumerate(sorted(set(keys)))}
        nxt = [[dictionary[keys[i*n+v]] for v in range(n)] for i in range(N)]
        if nxt == color:break
        color = nxt
    assert nxt == color, 'refinement not stabilized within n+1 rounds'
    print('stable_rounds',step)
    buckets = defaultdict(list)
    for i,row in enumerate(color):buckets[tuple(sorted(row))].append(i)
    class_count = 0; collisions = []
    for cases in buckets.values():
        representatives = []
        for i in cases:
            if not any(isomorphic(G[i],G[j],color[i],color[j]) for j in representatives):
                representatives.append(i)
        class_count += len(representatives)
        if len(representatives)>1:collisions.append(representatives)
    print(f'n={n} topological={N} isomorphism_types={class_count} C2_classes={len(buckets)} colliding_class_sizes={list(map(len,collisions))}')
    for cases in collisions:
        for i in cases:
            print(' witness',i,[(v,w) for v in range(n) for w in range(n) if G[i][v] & (1<<w)])
    return class_count,len(buckets),list(map(len,collisions))

if __name__ == '__main__':
    expected = ((1,1,()),(2,2,()),(6,6,()),(31,31,()),(302,302,()),(5984,5983,(2,)))
    for n,e in enumerate(expected,1):
        got = verify(n)
        assert got[0:2] == e[0:2] and tuple(got[2]) == e[2],(n,got,e)
    print('VERIFIED')
