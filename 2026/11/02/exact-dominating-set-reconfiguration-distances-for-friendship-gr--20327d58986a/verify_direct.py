"""Direct exhaustive subset-and-reconfiguration verifier for friendship graphs.

Python 3 standard library only. No theorem conclusion is assumed when
building the graph; independent domination predicates select all vertices.
"""
from collections import Counter, deque
from math import comb


def configuration(r):
    n = 2*r+1
    hub = 2*r
    neighbors = [0] * n
    for j in range(r):
        u, v = 2*j, 2*j+1
        neighbors[u] = (1 << v) | (1 << hub)
        neighbors[v] = (1 << u) | (1 << hub)
        neighbors[hub] |= (1 << u) | (1 << v)
    limit = r+1
    states = [mask for mask in range(1 << n)
              if mask.bit_count() <= limit and all(
                  (mask & (1 << v)) or (mask & neighbors[v])
                  for v in range(n))]
    ids = {mask: i for i,mask in enumerate(states)}
    neighbors_in_reconfiguration = [
        [ids[next_mask] for v in range(n)
         if (next_mask := mask ^ (1 << v)) in ids]
        for mask in states
    ]
    return states, neighbors_in_reconfiguration


def predicted_type(mask,r):
    hub = (mask >> (2*r)) & 1
    if not hub:
        doubled = sum(((mask >> (2*j)) & 3) == 3 for j in range(r))
        assert doubled in (0,1)
        return ('outer', doubled)
    pairs = [(mask >> (2*j)) & 3 for j in range(r)]
    a = sum(t in (1,2) for t in pairs)
    b = sum(t==3 for t in pairs)
    return ('hub', a, b)


def predicted_ecc(typ, r):
    if typ[0]=='outer':
        return 2*r+1
    _,a,b=typ
    if b == 0:
        return r+a+2 if a<r else 2*r+1
    return r+a+2*b


def bfs(adj, source):
    distances = [-1] * len(adj)
    distances[source] = 0
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if distances[v] < 0:
                distances[v] = distances[u] + 1
                queue.append(v)
    assert -1 not in distances
    return distances


def main():
    for r in range(2,9):
        masks, adj = configuration(r)
        population = Counter(predicted_type(mask,r) for mask in masks)
        number = sum(comb(2*r,j) for j in range(r+1)) + 2**r + r*2**(r-1)
        edges = 2*r*sum(comb(2*r-1,j) for j in range(r)) + (r+1)*2**r
        assert len(masks) == number
        assert sum(map(len,adj))//2 == edges
        reps = {}
        for i,m in enumerate(masks):
            reps.setdefault(predicted_type(m,r),i)
        all_sources = range(len(masks)) if r <= 5 else reps.values()
        ecc_by_type = {}
        for source in all_sources:
            distances = bfs(adj,source)
            expected = predicted_ecc(predicted_type(masks[source],r),r)
            actual = max(distances)
            assert actual == expected,(r,source,actual,expected)
            typ = predicted_type(masks[source],r)
            if typ in ecc_by_type: assert ecc_by_type[typ]==actual
            ecc_by_type[typ]=actual
        assert min(ecc_by_type.values())==r+2
        assert max(ecc_by_type.values())==2*r+1
        center_total=sum(n for t,n in population.items() if predicted_ecc(t,r)==r+2)
        outer_total=sum(n for t,n in population.items() if predicted_ecc(t,r)==2*r+1)
        assert center_total==r+1,(r,center_total)
        assert outer_total==(r+2)*2**r,(r,outer_total)
        assert len(ecc_by_type)==len(population)
        print(f'DIRECT_PASS r={r} states={number} edges={edges} '
              f'types={len(population)} radius={r+2} diameter={2*r+1} '
              f'centers={center_total} peripherals={outer_total}',flush=True)
    print('ALL_DIRECT_CHECKS_PASS')


if __name__=='__main__':
    main()
