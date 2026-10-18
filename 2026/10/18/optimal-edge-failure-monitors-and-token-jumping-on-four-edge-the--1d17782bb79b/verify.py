"""Independent finite checks for minimum edge-failure monitoring on equal four-edge-arm theta graphs.

Run: python3 verify.py
Python standard library only.
"""
from collections import deque
from itertools import combinations


def graph(r):
    n = 3*r + 2
    adj = [set() for _ in range(n)]
    for i in range(r):
        chain = (0, 2+3*i, 3+3*i, 4+3*i, 1)
        for a,b in zip(chain, chain[1:]):
            adj[a].add(b); adj[b].add(a)
    edges = sorted((a,b) for a in range(n) for b in adj[a] if a < b)
    return adj, edges


def distances(adj, removed=None):
    result = []
    for start in range(len(adj)):
        dst = [10**6] * len(adj)
        dst[start] = 0
        queue = deque((start,))
        while queue:
            a = queue.popleft()
            for b in adj[a]:
                if removed == (min(a,b), max(a,b)):
                    continue
                if dst[b] == 10**6:
                    dst[b] = dst[a] + 1
                    queue.append(b)
        result.append(dst)
    return result


def monitored_masks(adj, edges):
    n = len(adj)
    original = distances(adj)
    masks = [[0] * n for _ in range(n)]
    for index, edge in enumerate(edges):
        after = distances(adj, edge)
        for a in range(n):
            for b in range(a+1,n):
                if after[a][b] > original[a][b]:
                    masks[a][b] |= 1<<index
    return masks


def is_monitoring(subset, masks, full):
    seen = 0
    for a,b in combinations(subset, 2):
        seen |= masks[a][b]
        if seen == full:
            return True
    return False


def expected_sets(r):
    result = {}
    for subset in range(1, 1<<r):
        sel_u = [0] + [4+3*i if subset>>i & 1 else 3+3*i for i in range(r)]
        sel_v = [1] + [2+3*i if subset>>i & 1 else 3+3*i for i in range(r)]
        result[frozenset(sel_u)] = ('U', subset)
        result[frozenset(sel_v)] = ('V', subset)
    for i in range(r):
        s = [3+3*j for j in range(r) if j != i] + [2+3*i,4+3*i]
        result[frozenset(s)] = ('W',i)
    assert len(result)==2**(r+1)+r-2
    return result


def check(r):
    adj, edges = graph(r)
    masks = monitored_masks(adj,edges)
    full = (1<<len(edges))-1
    expected = expected_sets(r)
    number_examined = 0
    for subset in combinations(range(len(adj)),r):
        number_examined += 1
        assert not is_monitoring(subset,masks,full), (r,'smaller',subset)
    actual = set()
    for subset in combinations(range(len(adj)),r+1):
        number_examined += 1
        if is_monitoring(subset,masks,full):
            actual.add(frozenset(subset))
    assert actual == set(expected), (r, len(actual),len(expected),list(actual.symmetric_difference(expected))[:3])
    nodes = list(expected)
    indices = {key:i for i,key in enumerate(nodes)}
    adj_reconf=[set() for _ in nodes]
    for i,s in enumerate(nodes):
        for j in range(i+1,len(nodes)):
            if len(s ^ nodes[j])==2:
                adj_reconf[i].add(j)
                adj_reconf[j].add(i)
    # Structural check: both punctured cubes and every length-two linking path.
    for i, nbrs in enumerate(adj_reconf):
        t,x=expected[nodes[i]]
        predicted=set()
        if t in ('U','V'):
            for k in range(r):
                y=x^(1<<k)
                if y:
                    predicted.add(indices[next(s for s in nodes if expected[s]==(t,y))])
            if x.bit_count()==1:
                h=x.bit_length()-1
                predicted.add(indices[next(s for s in nodes if expected[s]==('W',h))])
        else:
            for t1 in ('U','V'):
                predicted.add(indices[next(s for s in nodes if expected[s]==(t1,1<<x))])
        assert nbrs==predicted,(r,t,x,nbrs,predicted)
    degree_dist={}
    for nbrs in adj_reconf:
        degree_dist[len(nbrs)] = degree_dist.get(len(nbrs),0)+1
    assert degree_dist=={r:2*((1<<r)-1),2:r}
    edge_count=sum(map(len,adj_reconf))//2
    assert edge_count == r*(1<<r)
    diameter=0
    for start in range(len(nodes)):
        dst=[-1]*len(nodes)
        dst[start]=0
        dq=deque([start])
        while dq:
            a=dq.popleft()
            for b in adj_reconf[a]:
                if dst[b]<0:
                    dst[b]=dst[a]+1
                    dq.append(b)
        assert -1 not in dst
        diameter=max(diameter,max(dst))
    assert diameter==2*r
    return number_examined,len(actual),edge_count,diameter


def main():
    examined=0
    for r in range(3,8):
        tested,nopt,nedge,diam=check(r)
        examined+=tested
        print(f'r={r} candidates={tested} optimum_sets={nopt} reconfiguration_edges={nedge} diameter={diam}')
    print(f'VERIFICATION_OK r=3..7 total_examined={examined}')

if __name__=='__main__':
    main()
