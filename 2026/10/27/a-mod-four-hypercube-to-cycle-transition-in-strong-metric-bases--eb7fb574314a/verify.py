"""Independent finite checks of strong metric bases of squared cycles.

Uses graph-based breadth-first search and the geodesic definition, not the
closed-form cyclic distance identity, to verify strong resolution.
"""
from collections import Counter, deque
from itertools import combinations, product
from math import comb


def expected_complement_sets(n):
    if n % 4 == 2:
        h = n // 2
        return {(sum(1 << (i + h * b) for i, b in enumerate(bits)))
                for bits in product((0, 1), repeat=h)}
    if n % 4 == 0:
        q = n // 4
        return {sum(1 << ((t + j) % n) for j in range(2*q-1))
                for t in range(n)}
    if n % 4 == 1:
        q = (n - 1) // 4
        return {sum(1 << ((2*q * (t + 2*j)) % n) for j in range(2*q-1))
                for t in range(n)}
    q = (n - 3) // 4
    return {sum(1 << (((2*q+1)*(t+2*j)) % n) for j in range(2*q+1))
            for t in range(n)}


def distances(n):
    adj = [[(v + d) % n for d in (-2,-1,1,2)] for v in range(n)]
    distances = []
    for src in range(n):
        d = [-1]*n
        d[src] = 0
        Q = deque([src])
        while Q:
            v = Q.popleft()
            for w in adj[v]:
                if d[w] == -1:
                    d[w] = d[v] + 1
                    Q.append(w)
        assert all(z >= 0 for z in d)
        distances.append(d)
    return adj, distances


def calculate(n):
    adj, dist = distances(n)
    mmd_edges = set()
    geodesic_resolver_masks = []
    for a in range(n):
        for b in range(a+1,n):
            if all(dist[z][b] <= dist[a][b] for z in adj[a]) and all(
                    dist[z][a] <= dist[a][b] for z in adj[b]):
                mmd_edges.add((a,b))
            d = dist[a][b]
            mask = sum(1<<w for w in range(n) if
                dist[a][w] == d+dist[b][w] or dist[b][w] == d+dist[a][w])
            assert mask
            geodesic_resolver_masks.append(mask)
    if n%4 in (0,1):
        expect_steps = [n//2-1,n//2] if n%4==0 else [(n-1)//2-1,(n-1)//2]
    else:
        expect_steps = [n//2]
    expect_edges = {tuple(sorted((i,(i+s)%n))) for i in range(n)
                    for s in expect_steps}
    assert mmd_edges == expect_edges,(n,'MMD',mmd_edges ^ expect_edges)

    complements = expected_complement_sets(n)
    assert all(not ((x>>a)&1 and (x>>b)&1) for x in complements for a,b in mmd_edges)
    k = n - next(iter(complements)).bit_count()
    if n%4==0: assert k==n//2+1
    elif n%4==1: assert k==(n+3)//2
    elif n%4==2: assert k==n//2
    else: assert k==(n+1)//2

    geodesic_bases=set()
    for selected in combinations(range(n),k):
        mask=sum(1<<v for v in selected)
        if all(mask & x for x in geodesic_resolver_masks):
            geodesic_bases.add(mask)
    expected_bases = {((1<<n)-1)^x for x in complements}
    assert geodesic_bases == expected_bases,(n,'bases',len(geodesic_bases),len(expected_bases))
    if n<=15:
        for smaller_size in range(k):
            assert not any(all(sum(1<<v for v in selected)&x for x in geodesic_resolver_masks)
                           for selected in combinations(range(n),smaller_size))

    base_set=geodesic_bases
    degree=Counter(); edge_count=0;neighbors={}
    for x in base_set:
        near=set()
        for a in range(n):
            if x>>a&1:
                for b in range(n):
                    if not (x>>b&1):
                        y = x ^ (1<<a) ^ (1<<b)
                        if y in base_set: near.add(y)
        neighbors[x]=near;degree[len(near)]+=1;edge_count+=len(near)
    edge_count//=2
    if n%4==2:
        h=n//2
        assert len(base_set)==2**h and degree==Counter({h:2**h})
        assert edge_count==h*2**(h-1)
    else:
        assert len(base_set)==n and degree==Counter({2:n})
        assert edge_count==n
    seen=set(); components=[]
    for x in base_set:
        if x not in seen:
            todo=[x];seen.add(x);part=[]
            while todo:
                y=todo.pop();part.append(y)
                for z in neighbors[y]:
                    if z not in seen:seen.add(z);todo.append(z)
            components.append(part)
    assert len(components)==1
    diameter=0
    for src in base_set:
        todo=deque([src]); distx={src:0}
        while todo:
            x=todo.popleft()
            for y in neighbors[x]:
                if y not in distx:
                    distx[y]=distx[x]+1;todo.append(y)
        diameter=max(diameter,max(distx.values()))
    expected_diam = n//2 if n%4!=2 else n//2
    assert diameter==expected_diam
    print(f'n={n} sdim={k} bases={len(base_set)} edges={edge_count} '
          f'diameter={diameter} graph={"hypercube" if n%4==2 else "cycle"} OK')

if __name__ == '__main__':
    for n in range(6,21): calculate(n)
    print('ALL_VERIFY_OK')
