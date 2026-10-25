"""Independent cycle-enumeration certificate for a generalized quadrangle incidence graph.

Run: python verify_cycles.py
Only the Python standard library is required.
"""
from itertools import combinations
from collections import Counter, deque
from hashlib import sha256


def build_graph():
    pairs = list(combinations(range(6), 2))
    # Enumerate the synthemes as 3-subsets of the 15 edges, not via recursion.
    synthemes = []
    for triple in combinations(range(15), 3):
        ends = [x for t in triple for x in pairs[t]]
        if len(set(ends)) == 6:
            synthemes.append(triple)
    assert len(synthemes) == 15
    edges = {(u, 15+i) for i, triple in enumerate(synthemes) for u in triple}
    assert len(edges) == 45
    nbr = [set() for _ in range(30)]
    for a, b in edges:
        nbr[a].add(b)
        nbr[b].add(a)
    assert all(len(x) == 3 for x in nbr)
    return edges, nbr


def all_cycles(nbr, size):
    out = set()
    def walk(start, path):
        u = path[-1]
        if len(path) == size:
            if start in nbr[u] and path[1] < path[-1]:
                out.add(tuple(path))
            return
        for v in sorted(nbr[u]):
            if v > start and v not in path:
                walk(start, path + [v])
    for root in range(30):
        walk(root, [root])
    return sorted(out)


def all_matchings(nbr):
    full = (1 << 30) - 1
    results = set()
    def recurse(used, taken):
        if used == full:
            results.add(frozenset(taken))
            return
        v = next(i for i in range(30) if not ((used >> i) & 1))
        for w in sorted(nbr[v]):
            if not ((used >> w) & 1):
                recurse(used | (1 << v) | (1 << w),
                        taken + [(min(v, w), max(v, w))])
    recurse(0, [])
    return results


def canon(m):
    val = [None] * 15
    for a,b in m:
        assert a < 15 <= b
        val[b-15] = a
    assert all(v is not None for v in val)
    return tuple(val)


def components_of_edges(edges):
    adj = [[] for _ in range(30)]
    for a,b in edges:
        adj[a].append(b)
        adj[b].append(a)
    seen = set()
    sizes = []
    for v in range(30):
        if v not in seen:
            todo = [v]
            seen.add(v)
            for u in todo:
                for w in adj[u]:
                    if w not in seen:
                        seen.add(w)
                        todo.append(w)
            sizes.append(len(todo))
    return tuple(sorted(sizes))


def bfs(s, adj):
    dist = [-1] * len(adj)
    dist[s] = 0
    queue = deque([s])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)
    return dist


def main():
    E, nbr = build_graph()
    assert len(all_cycles(nbr, 4)) == 0
    assert len(all_cycles(nbr, 6)) == 0
    cycles = all_cycles(nbr, 8)
    M = all_matchings(nbr)
    ms = sorted(M, key=canon)
    index = {m:i for i,m in enumerate(ms)}
    assert len(ms) == 288
    adj = [set() for _ in ms]
    n_switches = 0
    for cycle in cycles:
        c_edges = [tuple(sorted((cycle[k], cycle[(k+1)%8]))) for k in range(8)]
        left = frozenset(c_edges[::2]);right=frozenset(c_edges[1::2])
        for i,matching in enumerate(ms):
            if left <= matching:
                new = (matching - left) | right
            elif right <= matching:
                new = (matching - right) | left
            else:
                continue
            j = index[new]
            adj[i].add(j)
            n_switches += 1
    assert n_switches == 2880
    assert all(len(nbrs)==10 for nbrs in adj)
    assert all(i in adj[j] for j,neigh in enumerate(adj) for i in neigh)
    shape = [components_of_edges(E - m) for m in ms]
    assert Counter(shape)=={(10,20):144,(30,):144}
    profiles=Counter()
    anti=Counter()
    hamiltonian_pairs=0
    distance_six_pairs=0
    for i,m in enumerate(ms):
        d=bfs(i,adj)
        assert all(v>=0 for v in d)
        profiles[(shape[i],tuple(Counter(d)[k] for k in range(max(d)+1)))] +=1
        for j in range(i+1,len(ms)):
            is_ham = (components_of_edges(m ^ ms[j])==(30,))
            is_six = (d[j]==6)
            assert is_ham==is_six
            hamiltonian_pairs += int(is_ham)
            distance_six_pairs += int(is_six)
    assert hamiltonian_pairs==distance_six_pairs==144
    assert profiles=={
        ((10,20),(1,10,45,97,96,37,2)):144,
        ((30,),(1,10,42,97,101,37)):144}
    outpairs=sorted((i,j) for i in range(len(ms)) for j in adj[i] if i<j)
    assert len(outpairs)==1440
    payload=('\n'.join(f'{i},{j}' for i,j in outpairs)+'\n').encode()
    print('girth_at_least_8=True')
    print(f'eight_cycles={len(cycles)}')
    print('perfect_matchings=288')
    print('two_factor_types=10+20:144,30:144')
    print('eight_cycle_flip_edges=1440 degrees=10 connected_components=1')
    print('10+20_profile=1,10,45,97,96,37,2 count=144')
    print('30_profile=1,10,42,97,101,37 count=144')
    print('radius=5 diameter=6')
    print('distance_6_pairs=144 all_and_only_hamiltonian_symmetric_difference')
    print('adjacency_sha256='+sha256(payload).hexdigest())
    print('VERIFY_OK')


if __name__=='__main__':
    main()
