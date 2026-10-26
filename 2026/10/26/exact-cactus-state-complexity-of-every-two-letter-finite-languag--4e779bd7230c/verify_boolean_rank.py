"""Exact finite tests for the two-letter-language cactus automata theorem.
Run with Python 3.9+ standard library: python verify_boolean_rank.py.
The theorem's general lower bound is a proof, not a finite computation.
"""
from collections import Counter, deque
from itertools import combinations, product
from math import comb


def rectangles(q, target):
    out = {}
    for a in range(1, 1 << q):
        for b in range(1, 1 << q):
            cells = sum(1 << (i*q+j) for i in range(q) for j in range(q)
                        if (a >> i) & 1 and (b >> j) & 1)
            if cells & ~target == 0:
                out[cells] = (a, b)
    return list(out.items())


def minimum_rectangle_cover(q, target):
    options = rectangles(q, target)
    # Shortest path on bitmasks; BFS also produces an explicit optimum cover.
    queue = deque([0])
    predecessor = {0: None}
    while queue:
        mask = queue.popleft()
        if mask == target:
            result = []
            while mask:
                prev, option = predecessor[mask]
                result.append(option)
                mask = prev
            result.reverse()
            return result
        for cells, ab in options:
            next_mask = mask | cells
            if next_mask not in predecessor:
                predecessor[next_mask] = (mask, ab)
                queue.append(next_mask)
    raise AssertionError('No rectangle cover')


def make_cactus_nfa(q, rectangles_):
    t = len(rectangles_)
    nf = (t + 1)//2
    n = 1 + t + nf
    transitions = {}
    for index, (a, b) in enumerate(rectangles_):
        mid = 1 + index
        final = 1 + t + index // 2
        for symbol in range(q):
            if (a >> symbol) & 1:
                transitions.setdefault((0, symbol), set()).add(mid)
            if (b >> symbol) & 1:
                transitions.setdefault((mid, symbol), set()).add(final)
    return (n, transitions, set(range(1+t,n)))


def accept(nfa, w):
    n, transitions, finals = nfa
    states = {0}
    for a in w:
        states = {v for u in states for v in transitions.get((u,a), ())}
    return bool(states & finals)


def simple_cycles(n, graph):
    cycles = set()
    def visit(start, path):
        current = path[-1]
        for nxt in graph[current]:
            if nxt == start and len(path) >= 3:
                cycle_edges = frozenset(frozenset((path[i],path[(i+1)%len(path)])) for i in range(len(path)))
                cycles.add(cycle_edges)
            elif nxt > start and nxt not in path:
                visit(start,path+[nxt])
    for v in range(n):
        visit(v,[v])
    return list(cycles)


def cactus_and_bipartite(nfa):
    n, transitions, finals = nfa
    graph = [set() for _ in range(n)]
    for (u,a), vs in transitions.items():
        for v in vs:
            graph[u].add(v)
            graph[v].add(u)
    color = {}
    for s in range(n):
        if s not in color:
            color[s]=0
            queue=deque([s])
            while queue:
                u=queue.popleft()
                for v in graph[u]:
                    if v in color:
                        assert color[v] != color[u], 'Not bipartite'
                    else:
                        color[v]=1-color[u]
                        queue.append(v)
    cycles=simple_cycles(n,graph)
    for i,c in enumerate(cycles):
        verts={v for edge in c for v in edge}
        for d in cycles[:i]:
            assert len(verts & {v for edge in d for v in edge}) <= 1, 'Not cactus'


def run():
    for q in (2,3):
        frequencies=Counter()
        for relation in range(1, 1 << (q*q)):
            cover=minimum_rectangle_cover(q,relation)
            t=len(cover)
            nf=make_cactus_nfa(q,cover)
            assert nf[0] == 1+t+(t+1)//2
            cactus_and_bipartite(nf)
            for size in range(5):
                for word in product(range(q),repeat=size):
                    expected=size==2 and bool(relation & (1 << (word[0]*q+word[1])))
                    assert accept(nf,word)==expected,(q,relation,word)
            frequencies[t]+=1
        print('alphabet',q,'number of nonempty relations',sum(frequencies.values()),
              'Boolean-cover-rank frequencies',sorted(frequencies.items()))
    for q in range(2,15):
        relation=sum(1 << (i*q+j) for i in range(q) for j in range(q) if i != j)
        # For q>=4 use the explicit Sperner antichain rectangle construction.
        t=next(t for t in range(1,20) if comb(t,t//2)>=q)
        antichain=list(combinations(range(t),t//2))[:q]
        cover=[]
        for r in range(t):
            a=sum(1 << i for i,s in enumerate(antichain) if r in s)
            b=sum(1 << j for j,s in enumerate(antichain) if r not in s)
            if a and b: cover.append((a,b))
        union=0
        for a,b in cover:
            union |=sum(1 << (i*q+j) for i in range(q) for j in range(q)
                       if (a>>i)&1 and (b>>j)&1)
        assert union==relation and len(cover)==t,(q,t)
        nf=make_cactus_nfa(q,cover)
        cactus_and_bipartite(nf)
        assert all(accept(nf,(i,j))==(i!=j) for i in range(q) for j in range(q))
        print('not-equal',q,'Boolean rank',t,'cactus states',nf[0])
    print('VERIFY_OK')


if __name__=='__main__':
    run()
