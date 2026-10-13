"""Independent string-based SCC and reachability verifier, Python stdlib only."""
from collections import Counter, deque
from itertools import product

EXPECTED = {
    2: {-1:2, 2:2},
    3: {-1:4, 3:2, 4:2},
    4: {-1:4, 4:2, 5:2, 6:8},
    5: {-1:4, 5:2, 6:10, 7:12, 8:4},
    6: {-1:4, 6:2, 7:16, 8:42},
    7: {-1:4, 7:2, 8:50, 9:64, 10:8},
}

def build(k, failed):
    nodes = [''.join(z) for z in product('01', repeat=k)]
    surviving = [s for s in nodes if s != failed]
    arcs = {s: [s[1:] + bit for bit in '01' if s[1:] + bit != failed] for s in surviving}
    return surviving, arcs

def scc(nodes, arcs):
    rev = {v: [] for v in nodes}
    for u in nodes:
        for v in arcs[u]:
            rev[v].append(u)
    seen = set()
    order = []
    def dfs(x):
        seen.add(x)
        for y in arcs[x]:
            if y not in seen: dfs(y)
        order.append(x)
    for x in nodes:
        if x not in seen: dfs(x)
    seen.clear()
    comps=[]
    def dfsr(x,out):
        seen.add(x); out.add(x)
        for y in rev[x]:
            if y not in seen: dfsr(y,out)
    for x in reversed(order):
        if x not in seen:
            comp=set(); dfsr(x,comp); comps.append(comp)
    return comps

def metric(nodes, arcs):
    top=0
    for s in nodes:
        dist={s:0}
        todo=deque([s])
        while todo:
            u=todo.popleft()
            for v in arcs[u]:
                if v not in dist:
                    dist[v]=dist[u]+1; todo.append(v)
        if len(dist) != len(nodes): return -1
        top=max(top,max(dist.values()))
    return top

for k in range(2,8):
    words = [''.join(z) for z in product('01', repeat=k)]
    badset = {'0'*(k-1)+'1','0'+'1'*(k-1),
              '1'+'0'*(k-1),'1'*(k-1)+'0'}
    tally=Counter()
    for failed in words:
        nodes,arcs=build(k,failed)
        components=scc(nodes,arcs)
        sizes=sorted(len(c) for c in components)
        assert (failed in badset) == (len(components)>1)
        if failed in badset: assert sizes == [1,1,2**k-3]
        else: assert sizes == [2**k-1]
        tally[metric(nodes,arcs)] += 1
    assert dict(tally)==EXPECTED[k],(k,tally)
    print(f'k={k} INDEPENDENT_SCC_AND_DIAMETER_OK {dict(sorted(tally.items()))}')
print('INDEPENDENT_VERIFIED')
