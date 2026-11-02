"""Direct exhaustive power-domination and adjacent-slide reconfiguration tests."""
from collections import Counter, deque
from itertools import combinations


def test(n):
    verts = range(2*n)
    adj = [set() for _ in verts]
    for r in (0, 1):
        for i in range(n):
            v = r*n+i
            adj[v] = {r*n+(i-1)%n, r*n+(i+1)%n, (1-r)*n+i}

    def power_dominates(seeds):
        observed = set(seeds)
        for v in seeds:
            observed.update(adj[v])
        while True:
            extra = set()
            for v in observed:
                outside = adj[v]-observed
                if len(outside)==1:
                    extra.update(outside)
            if not extra-observed:
                return len(observed)==2*n
            observed.update(extra)

    assert all(not power_dominates((v,)) for v in verts)
    pairs = [tuple(z) for z in combinations(verts,2) if power_dominates(z)]
    pos = {pair:i for i,pair in enumerate(pairs)}
    assert len(pos)==11*n
    G=[set() for _ in pairs]
    for ix,(a,b) in enumerate(pairs):
        for old,still in ((a,b),(b,a)):
            for new in adj[old]-{still}:
                candidate=tuple(sorted((new,still)))
                if candidate in pos:
                    G[ix].add(pos[candidate])
    assert all(i in G[j] for i,ns in enumerate(G) for j in ns)
    assert sum(map(len,G))//2==24*n
    assert Counter(map(len,G))=={2:2*n,4:5*n,6:4*n}
    # Connectivity, short cycles, and parity in the actual exchange graph.
    reach={0};queue=deque([0])
    while queue:
        for j in G[queue.popleft()]:
            if j not in reach:
                reach.add(j);queue.append(j)
    assert len(reach)==len(pairs)
    for i,(a,b) in enumerate(pairs):
        di=abs(a%n-b%n)
        dist=min(di,n-di)+(a//n != b//n)
        for j in G[i]:
            c,d=pairs[j];dj=abs(c%n-d%n)
            next_dist=min(dj,n-dj)+(c//n != d//n)
            assert (dist-next_dist)%2
    qsum=0
    for u in G:
        t=list(u)
        for ia in range(len(t)):
            for ib in range(ia+1,len(t)):
                qsum+=len(G[t[ia]] & G[t[ib]])-1
    assert qsum//4==19*n and qsum%4==0
    return len(pairs),sum(map(len,G))//2,qsum//4

if __name__=='__main__':
    for n in range(8,21):
        print('n',n,'(vertices, edges, squares)',test(n))
    print('DIRECT_POWER_DOMINATION_RECONFIGURATION_PASS')
