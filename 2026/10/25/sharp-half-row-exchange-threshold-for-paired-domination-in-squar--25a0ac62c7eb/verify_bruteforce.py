"""Exhaustive independent finite check for paired domination of the 4-by-4 rook graph.
Run: python3 verify_bruteforce.py
Only the Python standard library is required.
"""
from itertools import combinations
from collections import deque, Counter

M = 4
VERTICES = tuple((r,c) for r in range(M) for c in range(M))
ADJ = {x:{y for y in VERTICES if x != y and (x[0] == y[0] or x[1] == y[1])} for x in VERTICES}


def paired(S):
    remaining = frozenset(S)
    if not all((v in S or bool(ADJ[v] & S)) for v in VERTICES):
        return False
    def match_left(T):
        if not T:
            return True
        x = min(T)
        return any(match_left(T - {x,y}) for y in ADJ[x] & T)
    return match_left(remaining)

for k in (0,1,2,3):
    assert not any(paired(frozenset(S)) for S in combinations(VERTICES,k))
SOLUTIONS = [frozenset(S) for S in combinations(VERTICES,4) if paired(frozenset(S))]
assert len(SOLUTIONS) == 80, len(SOLUTIONS)
assert len(set(SOLUTIONS)) == 80
by_orientation = Counter('row' if len({r for r,c in S}) == 4 else 'column' for S in SOLUTIONS)
assert by_orientation == Counter({'row':40,'column':40}), by_orientation


def graph(r):
    edges = {i:set() for i in range(len(SOLUTIONS))}
    for i in range(len(SOLUTIONS)):
        for j in range(i+1,len(SOLUTIONS)):
            if len(SOLUTIONS[i] - SOLUTIONS[j]) <= r:
                edges[i].add(j)
                edges[j].add(i)
    return edges


def graph_stats(A):
    components=[]
    unvisited=set(A)
    while unvisited:
        st={unvisited.pop()}; seen=set(st)
        while st:
            v=st.pop()
            for w in A[v]-seen:
                seen.add(w)
                st.add(w)
                unvisited.discard(w)
        components.append(len(seen))
    return len(components),sorted(components,reverse=True)

G1,G2=graph(1),graph(2)
assert graph_stats(G1) == (80,[1]*80)
assert graph_stats(G2) == (1,[80])
assert set(map(len,G2.values())) == {18}
assert sum(map(len,G2.values()))//2 == 720

layer_patterns=Counter()
for source in G2:
    q=deque([source]); dist={source:0}
    while q:
        v=q.popleft()
        for w in G2[v]:
            if w not in dist:
                dist[w]=dist[v]+1
                q.append(w)
    assert len(dist)==80
    layer_patterns[tuple(Counter(dist.values()).get(j,0) for j in range(max(dist.values())+1))]+=1
assert len(layer_patterns)==1,layer_patterns
assert len(next(iter(layer_patterns)))==4
print('rook graph size 4: minimum paired domination = 4')
print('minimum pairs = 80; row-oriented = 40; column-oriented = 40')
print('batch r=1: 0 edges, 80 isolated vertices')
print('batch r=2: 720 edges, connected, degree 18, diameter 3')
print('uniform distance layers:',next(iter(layer_patterns)), 'on',next(iter(layer_patterns.values())), 'vertices')
print('ALL ASSERTIONS PASSED')
