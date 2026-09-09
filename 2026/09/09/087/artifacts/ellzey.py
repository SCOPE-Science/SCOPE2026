"""Ellzey G-descent / inv statistics and N_lambda sets for C_{n,k}. Vertices 0..n-1."""
import itertools
from collections import defaultdict

def build(n, k):
    arcs = [(i, (i + d) % n) for i in range(n) for d in range(1, k + 1)]
    adj = [[False]*n for _ in range(n)]
    for (u, v) in arcs:
        adj[u][v] = True; adj[v][u] = True
    return arcs, adj

def check_circular_indifference(n, k):
    """Witness intervals [i,i+k] (circular, inclusive) give exactly arcs."""
    arcs, _ = build(n, k)
    eset = set(arcs)
    gen = set()
    for i in range(n):
        interval = {(i + t) % n for t in range(k + 1)}
        for u in range(n):
            for v in range(n):
                if u == v: continue
                # clockwise [u,v] subset of interval?
                d = (v - u) % n
                seg = {(u + t) % n for t in range(d + 1)}
                if seg <= interval:
                    gen.add((u, v))
    # intervals family: all [i,i+k]; edge iff [u,v] contained in some member
    return gen == eset, len(gen), len(eset)

def stats(sigma, arcs, adj):
    n = len(sigma)
    pos = [0]*n
    for i, v in enumerate(sigma): pos[v] = i
    # ranks
    rank = {}
    for i, v in enumerate(sigma):
        best = 0
        for j in range(i):
            u = sigma[j]
            if adj[u][v] and rank[u] > best: best = rank[u]
        rank[v] = best + 1
    des = set()
    for i in range(n - 1):
        a, b = sigma[i], sigma[i+1]
        if rank[a] > rank[b] or (rank[a] == rank[b] and a > b):
            des.add(i)  # 0-based position
    inv = sum(1 for (u, v) in arcs if pos[u] > pos[v])
    return rank, des, inv

def N_membership(sigma, des, adj, lam):
    """lam: list of block sizes. Return True iff sigma in N_lam(G)."""
    n = len(sigma)
    s = 0
    # check interior descents: positions s..s+li-2 must not be in des
    for li in lam:
        for p in range(s, s + li - 1):
            if p in des: return False
        # isolated check within block
        block = sigma[s:s+li]
        seen = set()
        for j, v in enumerate(block):
            if j > 0:
                if not any(adj[u][v] for u in block[:j]):
                    return False
        s += li
    return True

def F_expansion(n, k):
    """Return dict: (frozenset DES, inv) -> count, plus list of (sigma,des,inv)."""
    arcs, adj = build(n, k)
    from collections import Counter
    dist = Counter()
    recs = []
    for sigma in itertools.permutations(range(n)):
        _, des, inv = stats(list(sigma), arcs, adj)
        dist[(tuple(sorted(des)), inv)] += 1
        recs.append((sigma, des, inv))
    return arcs, adj, dist, recs
