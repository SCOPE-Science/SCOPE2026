#!/usr/bin/env python3
"""Exact, dependency-free verification of parity-window cyclic covers.

The checker enumerates all simple cycles of the relevant binary de Bruijn
arc graph up to the explicit feasible augmentation budget. A subset dynamic
program then certifies the cheapest connected hypergraph of simple cycles.
All counts, decisions and certificates use integer arithmetic.
"""
import json
from pathlib import Path

EXPECTED = {2:(4,2,3),3:(7,3,5),4:(16,8,19),5:(24,8,41),6:(46,14,697),7:(82,18,10377)}
ODD_ONLY = {2:2,3:3,4:8,5:10,6:14,7:21}

def required_cycles(n):
    states = 1 << (n-1)
    unseen = set(range(states))
    result = []
    while unseen:
        start = min(unseen)
        v = start
        tour = []
        while v in unseen:
            unseen.remove(v)
            tour.append(v)
            v = ((2*v) % states) | (v.bit_count() & 1)
        assert v == start
        result.append(tuple(tour))
    return result

def simple_cycle_footprints(n, maximum_length):
    """Return min length and witness for each footprint; exhaustive and canonical."""
    vertices = 1 << (n-1)
    components = required_cycles(n)
    idx = {v:i for i,cycle in enumerate(components) for v in cycle}
    best = {}
    witness = {}
    counts = {}
    for start in range(vertices):
        used = {start}
        def explore(v, path, cover):
            for bit in (0,1):
                w = ((v * 2) % vertices) | bit
                if w == start:
                    length = len(path)
                    counts[length] = counts.get(length,0) + 1
                    if length < best.get(cover, 10**9):
                        best[cover] = length
                        witness[cover] = tuple(path)
                elif w > start and w not in used and len(path) < maximum_length:
                    used.add(w)
                    explore(w, path+[w], cover | (1 << idx[w]))
                    used.remove(w)
        explore(start,[start],1 << idx[start])
    return components,best,witness,counts

def hypergraph_optimum(n, budget):
    components, best, witness, counts = simple_cycle_footprints(n,budget)
    full = (1 << len(components)) - 1
    costs = sorted((length, mask) for mask,length in best.items() if mask.bit_count()>1)
    inf = 10**9
    dp = [inf]*(full+1)
    prev = {}
    dp[1] = 0
    for mask in range(1, full+1,2):
        if dp[mask] >= inf: continue
        for length, arc_mask in costs:
            if mask & arc_mask:
                extended = mask | arc_mask
                if extended != mask and dp[extended] > dp[mask] + length:
                    dp[extended] = dp[mask] + length
                    prev[extended] = (mask, arc_mask)
    chosen = []
    mask = full
    if dp[mask]<inf:
        while mask != 1:
            predecessor,arc_mask = prev[mask]
            chosen.append(witness[arc_mask])
            mask = predecessor
    chosen.reverse()
    return dp[full],chosen,components,best,counts

def euler_word(n, paths):
    """One copy of every required even edge, plus chosen augmenting cycles."""
    V = 1 << (n-1)
    graph = [[] for _ in range(V)]
    for u in range(V):
        b = u.bit_count() & 1
        graph[u].append((2*u%V | b,b))
    for path in paths:
        for a,b in zip(path,path[1:]+path[:1]):
            bit = b & 1
            assert ((2*a)%V | bit) == b
            graph[a].append((b,bit))
    for arcs in graph:arcs.sort(reverse=True)
    total = sum(map(len, graph))
    start = 0
    stack = [(start,None)]
    result = []
    while stack:
        u,_ = stack[-1]
        if graph[u]:
            v,bit = graph[u].pop()
            stack.append((v,bit))
        else:
            _,bit = stack.pop()
            if bit is not None: result.append(str(bit))
    result.reverse()
    assert len(result)==total
    return ''.join(result)

def verify_cover(n, word):
    assert all(c in '01' for c in word)
    L=len(word)
    factors={int(''.join(word[(i+j)%L] for j in range(n)),2) for i in range(L)}
    expected={x for x in range(1<<n) if x.bit_count()%2==0}
    assert expected.issubset(factors),(n,expected-factors)

def odd_only_cost(n):
    """Exact optimum if *all* supplementary windows must have odd parity."""
    V=1<<(n-1)
    even=required_cycles(n)
    component_of={v:i for i,c in enumerate(even) for v in c}
    unseen=set(range(V));odd=[]
    while unseen:
        s=min(unseen);v=s;c=[]
        while v in unseen:
            unseen.remove(v);c.append(v)
            v=(2*v%V)|((v.bit_count()&1)^1)
        assert v==s
        odd.append(c)
    groups=[(sum(1<<i for i in {component_of[v] for v in c}),len(c)) for c in odd]
    min_cost=10**9
    for mask in range(1<<len(odd)):
        cost=sum(groups[j][1] for j in range(len(odd)) if mask>>j&1)
        if cost>=min_cost:continue
        parent=list(range(len(even)))
        def root(i):
            while parent[i]!=i: i=parent[i]
            return i
        for j in range(len(odd)):
            if mask>>j&1:
                h=groups[j][0]
                ids=[i for i in range(len(even)) if h>>i&1]
                for k in ids[1:]:parent[root(k)]=root(ids[0])
        if len({root(i) for i in range(len(even))})==1:
            min_cost=cost
    assert min_cost<10**9
    return min_cost

def main():
    data=json.loads(Path(__file__).with_name('witnesses.json').read_text('utf-8'))
    results=[]
    for n,(optimal,budget,expected_count) in EXPECTED.items():
        cost, chosen, required,best,counts=hypergraph_optimum(n,budget)
        assert cost == budget == optimal-(1<<(n-1)),(n,cost)
        assert sum(counts.values())==expected_count,(n,sum(counts.values()))
        assert len(required)==data[str(n)]['even_cycle_count']
        candidate=euler_word(n,chosen)
        assert candidate==data[str(n)]['word'],(n,candidate)
        assert len(candidate)==optimal
        verify_cover(n,candidate)
        assert odd_only_cost(n)==ODD_ONLY[n]
        results.append((n,optimal,cost,len(required),len(best),expected_count))
    assert results==[(2,4,2,2,3,3),(3,7,3,2,3,5),(4,16,8,4,11,19),(5,24,8,4,12,41),(6,46,14,8,90,697),(7,82,18,10,529,10377)]
    for row in results:print('n=%s L=%s extra=%s components=%s footprints=%s enumerated_cycles=%s'%row)
    print('VERIFY_OK')

if __name__ == '__main__':main()
