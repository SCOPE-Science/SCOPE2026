"""Independent exact matching-based census for Hamiltonian 2-switch graphs.

The ribbon G(n, twist) has two rows, vertical rungs and either
untwisted or crossed seams. Every Hamiltonian cycle in a cubic graph
is the complement of a perfect matching; this program uses that fact
but tests connectivity directly, without inserting a formula into the
enumeration.
"""
from collections import Counter, deque


def ribbon(n, twist):
    assert n >= 4
    edges = set()
    def add(a, b):
        edges.add(tuple(sorted((a, b))))
    for i in range(n):
        add(i, n+i)
    for layer in range(2):
        for i in range(n-1):
            add(layer*n+i, layer*n+i+1)
        if not twist:
            add(layer*n+n-1, layer*n)
    if twist:
        add(n-1, n)
        add(2*n-1, 0)
    return tuple(sorted(edges))


def cycles(n, twist):
    E = ribbon(n, twist)
    incident = [[] for _ in range(2*n)]
    for i, (u, v) in enumerate(E):
        incident[u].append((i, v))
        incident[v].append((i, u))
    out = set()
    all_edges = (1 << len(E)) - 1
    def explore(remaining, matched):
        if not remaining:
            chosen = all_edges ^ matched
            adjacency = [[] for _ in range(2*n)]
            for i, (u, v) in enumerate(E):
                if (chosen >> i) & 1:
                    adjacency[u].append(v)
                    adjacency[v].append(u)
            assert all(len(a)==2 for a in adjacency)
            seen={0}; todo=[0]
            while todo:
                for w in adjacency[todo.pop()]:
                    if w not in seen:
                        seen.add(w);todo.append(w)
            if len(seen)==2*n:out.add(chosen)
            return
        v=min(remaining)
        for ei,w in incident[v]:
            if w in remaining:
                explore(remaining-{v,w},matched | (1<<ei))
    explore(frozenset(range(2*n)),0)
    return E,out


def check(n,twist):
    E,H=cycles(n,twist)
    H=list(sorted(H)); adj=[set() for _ in H]
    for i in range(len(H)):
        for j in range(i+1,len(H)):
            # A legal switch deletes exactly two edges and adds two.
            # Because every tested object is a Hamiltonian cycle, this
            # condition itself is sufficient to certify a legal switch.
            if (H[i]^H[j]).bit_count()==4:
                adj[i].add(j);adj[j].add(i)
    degrees=Counter(map(len,adj))
    seen=set();sizes=[]
    for i in range(len(H)):
        if i in seen:continue
        q=[i];seen.add(i)
        for u in q:
            for v in adj[u]:
                if v not in seen:
                    seen.add(v);q.append(v)
        sizes.append(len(q))
    if not twist:
        expected=n+2 if n%2==0 else n
        assert len(H)==expected
        assert degrees==Counter({0:expected})
        assert sizes==[1]*expected
    else:
        expected=n+1 if n%2==0 else n+3
        assert len(H)==expected
        expected_deg=Counter({1:n,n:1})
        if n%2: expected_deg[0]=2
        assert degrees==expected_deg, (n,degrees,expected_deg)
        assert sorted(sizes)==([n+1] if n%2==0 else [1,1,n+1])
    return n, int(twist),len(H),sum(map(len,adj))//2,dict(degrees),sorted(sizes)


if __name__=='__main__':
    for twist in (False,True):
        for n in range(4,19):
            print(check(n,twist))
    print('MATCHING_ENUMERATION_ALL_2_EDGE_SWITCHES_PASS')
