#!/usr/bin/env python3
"""Standalone direct check of independent-coalition partitions of leaf coronas.

The combinatorial formula and the exhaustive partition predicate are implemented
separately. No external libraries are required.
"""
from itertools import combinations
from collections import Counter


def components_and_bipartite(n, edges):
    nbr = [[] for _ in range(n)]
    for i, j in edges:
        nbr[i].append(j)
        nbr[j].append(i)
    color = {}
    components = 0
    for i in range(n):
        if i in color:
            continue
        components += 1
        color[i] = 0
        stack = [i]
        while stack:
            u = stack.pop()
            for v in nbr[u]:
                if v in color:
                    if color[v] == color[u]:
                        return components, False
                else:
                    color[v] = 1 - color[u]
                    stack.append(v)
    return components, True


def predicted(n, edges):
    if n == 1:
        return Counter({2: 1})
    c, ok = components_and_bipartite(n, edges)
    if not ok:
        return Counter()
    raw = (1 << (c-1)) * ((1 << (n-1)) - 1)**2
    collisions = ((1 << (c-1)) - 1) * (1 << (c-2)) if c >= 2 else 0
    return Counter({4: raw - collisions})


def brute(n, edges):
    N = 2*n
    full = (1 << N) - 1
    adj = [0]*N
    for i, j in edges:
        adj[i] |= 1 << j
        adj[j] |= 1 << i
    for i in range(n):
        adj[i] |= 1 << (i+n)
        adj[i+n] |= 1 << i
    indep = [False]*(1<<N)
    ids = [False]*(1<<N)
    allowed = []
    for s in range(1,1<<N):
        if all(not (adj[i] & s) for i in range(N) if s>>i & 1):
            indep[s] = True
            ids[s] = all((s>>i&1) or (adj[i]&s) for i in range(N))
            if not ids[s] or (s.bit_count()==1):
                allowed.append(s)
    coal = {}
    for a in allowed:
        coal[a] = {b for b in allowed if not (a&b) and ids[a|b] and not ids[a] and not ids[b]}
    choices = [[] for _ in range(N)]
    for s in allowed:
        for i in range(N):
            if s>>i & 1:
                choices[i].append(s)
    counts = Counter()
    def rec(used, blocks):
        if used == full:
            if all((ids[b] and b.bit_count()==1) or any(c in coal[b] for c in blocks) for b in blocks):
                counts[len(blocks)] += 1
            return
        first = (full ^ used)&-(full ^ used)
        k = first.bit_length()-1
        for b in choices[k]:
            if not (b&used):
                blocks.append(b)
                rec(used|b, blocks)
                blocks.pop()
    rec(0,[])
    return counts


def test(n,edges):
    actual=brute(n,edges)
    want=predicted(n,edges)
    if actual != want:
        raise AssertionError((n,edges,actual,want))
    return actual


def main():
    cases = 0
    for n in range(1,5):
        all_edges = list(combinations(range(n), 2))
        for mask in range(1<<len(all_edges)):
            edges = [e for i,e in enumerate(all_edges) if mask>>i&1]
            test(n,edges)
            cases += 1
    print('ALL LABELED GRAPHS n=1..4: %d exact partition censuses agree' % cases)
    samples = [
        ('five-cycle',5,[(i,(i+1)%5) for i in range(5)]),
        ('five-path',5,[(i,i+1) for i in range(4)]),
        ('five-clique',5,list(combinations(range(5),2))),
        ('edge-plus-3-isolates',5,[(0,1)]),
        ('two-edges-plus-isolate',5,[(0,1),(2,3)]),
        ('five-edgeless',5,[]),
        ('triangle-plus-two-isolates',5,[(0,1),(1,2),(0,2)]),
    ]
    for name,n,es in samples:
        print(name,dict(test(n,es)))
        cases += 1
    print('PASS: %d graphs checked by independent exhaustive enumeration' % cases)

if __name__=='__main__':
    main()
