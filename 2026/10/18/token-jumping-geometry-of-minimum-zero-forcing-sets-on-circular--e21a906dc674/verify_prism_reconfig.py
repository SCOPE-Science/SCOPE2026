"""Independent finite verification of zero-forcing reconfiguration on circular ladders.
Run: python3 verify_prism_reconfig.py (Python 3.9+; standard library only).
"""
from itertools import combinations
from collections import Counter, defaultdict, deque


def edges(n):
    adj = [set() for _ in range(2*n)]
    for i in range(n):
        for layer in (0, 1):
            a = layer*n+i
            for b in (layer*n+(i-1)%n, layer*n+(i+1)%n, (1-layer)*n+i):
                adj[a].add(b)
    return tuple(tuple(sorted(x)) for x in adj)


def forceable(adj, S):
    blue = set(S)
    while len(blue) != len(adj):
        new = {next(iter(w)) for v in blue if len(w := (set(adj[v])-blue)) == 1}
        if not new:
            return False
        blue.update(new)
    return True


def orbit(n, vertices):
    result=set()
    for reversal in (-1, 1):
        for offset in range(n):
            for swap in (0, 1):
                result.add(frozenset(((v//n)^swap)*n + (reversal*(v%n)+offset)%n
                                     for v in vertices))
    return result


def selected_sets(n):
    u=lambda i:i%n
    v=lambda i:n+i%n
    representatives = {
        'Q': (u(0),u(1),v(0),v(1)),
        'R': (u(0),u(1),u(2),u(3)),
        'T': (u(0),u(1),v(0),v(-1)),
        'E': (u(0),u(1),u(2),v(0)),
        'J': (u(0),u(1),u(3),v(1)),
    }
    groups = {name:orbit(n, rep) for name,rep in representatives.items()}
    assert sum(map(len,groups.values())) == len(set().union(*groups.values()))
    return groups


def reconfiguration_graph(S):
    V=sorted(S, key=lambda a:tuple(sorted(a)))
    ids={s:i for i,s in enumerate(V)}
    buckets=defaultdict(set)
    for i,s in enumerate(V):
        for triple in combinations(sorted(s),3):
            buckets[triple].add(i)
    adj=[set() for _ in V]
    for block in buckets.values():
        for i in block:
            adj[i].update(block-{i})
    return V, adj


def connected(adj):
    seen={0};queue=deque([0])
    while queue:
        for y in adj[queue.popleft()]:
            if y not in seen:
                seen.add(y); queue.append(y)
    return len(seen)==len(adj)


def run():
    total_checked=0
    expected={'Q':1,'R':2,'T':2,'E':4,'J':4}
    expected_deg={'Q':12,'R':8,'T':8,'E':8,'J':5}
    quota={'Q':{'Q':0,'R':0,'T':4,'E':4,'J':4},
           'R':{'Q':0,'R':2,'T':0,'E':4,'J':2},
           'T':{'Q':2,'R':0,'T':0,'E':4,'J':2},
           'E':{'Q':1,'R':2,'T':2,'E':1,'J':2},
           'J':{'Q':1,'R':1,'T':1,'E':2,'J':0}}
    for n in range(6,16):
        adj=edges(n)
        groups=selected_sets(n)
        catalog=set().union(*groups.values())
        assert {name:len(sets) for name,sets in groups.items()} == {k:v*n for k,v in expected.items()}
        for sub in combinations(range(2*n),4):
            total_checked+=1
            assert forceable(adj,sub)==(frozenset(sub) in catalog),(n,sub)
        for sub in combinations(range(2*n),3):
            assert not forceable(adj,sub)
        V,g=reconfiguration_graph(catalog)
        assert len(V)==13*n and connected(g)
        assert sum(map(len,g))//2 == 48*n
        type_of={s:name for name,ss in groups.items() for s in ss}
        for s,near in zip(V,g):
            kind=type_of[s]
            assert len(near)==expected_deg[kind]
            actual=Counter(type_of[V[j]] for j in near)
            assert {k:actual[k] for k in groups}==quota[kind],(n,kind,actual)
    # Large-width reconfiguration check, without an all-subset search.
    for n in (24,40,80):
        groups=selected_sets(n)
        V,g=reconfiguration_graph(set().union(*groups.values()))
        assert len(V)==13*n and connected(g)
        assert sum(map(len,g))//2 ==48*n
    print(f'RECONFIGURATION_VERIFIED n=6..15 raw_four_subsets_checked={total_checked} all_groups=5')
    print('FINITE_EXTENSIONS n=24,40,80 connected_and_edge_formula=true')
    print('QUOTIENT_ADJACENCIES Q:[0,0,4,4,4] R:[0,2,0,4,2] T:[2,0,0,4,2] E:[1,2,2,1,2] J:[1,1,1,2,0]')

if __name__=='__main__':
    run()
