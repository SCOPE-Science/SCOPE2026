"""Exact integer and mod-two tests of exchange eigenspaces of star two-point spaces.

Runs under standard Python 3. No external dependencies; enumerates graph spanning-tree
cycle bases and verifies the mod-two extension and character identities.
"""
from collections import deque
from itertools import permutations
from math import comb


def gf2_rank(vectors):
    pivots = {}
    for v in vectors:
        x = v
        while x:
            highest = x.bit_length() - 1
            if highest in pivots:
                x ^= pivots[highest]
            else:
                pivots[highest] = x
                break
    return len(pivots)


def graph_cycle_basis(n):
    edges = [(i, j) for i in range(n) for j in range(n) if i != j]
    vertices = [('u', i) for i in range(n)] + [('v', j) for j in range(n)]
    adjacent = {v: [] for v in vertices}
    for idx, (i, j) in enumerate(edges):
        a, b = ('u', i), ('v', j)
        adjacent[a].append((b, idx, 1))
        adjacent[b].append((a, idx, -1))
    base = vertices[0]
    q = deque([base]); parent = {base: None}; used = set()
    while q:
        a = q.popleft()
        for b, idx, orient in adjacent[a]:
            if b not in parent:
                parent[b] = (a, idx, orient)
                used.add(idx)
                q.append(b)
    assert len(parent) == len(vertices)
    assert len(used) == len(vertices) - 1

    def path_to_root(v):
        out = []
        while parent[v] is not None:
            a, idx, orient = parent[v]
            out.append((v, a, idx, -orient))
            v = a
        return out

    cycles = []
    for idx, (i, j) in enumerate(edges):
        if idx in used:
            continue
        vec = [0] * len(edges)
        vec[idx] = 1
        # Path from V_j to U_i in spanning tree, using common ancestor.
        va, vb = ('v', j), ('u', i)
        pp = path_to_root(va)
        qq = path_to_root(vb)
        keys = {va: 0}
        w = va
        for t, (v, a, eid, sign) in enumerate(pp):
            w = a; keys[w] = t+1
        w = vb; toward_b = []
        while w not in keys:
            a, eid, sign = parent[w]
            toward_b.append((eid, sign))
            w = a
        ancestor = w
        steps = keys[ancestor]
        for v, a, eid, sign in pp[:steps]:
            vec[eid] += sign
        for eid, sign in reversed(toward_b):
            vec[eid] += sign
        assert all(sum(vec[eid] for eid, (a, b) in enumerate(edges) if a == h) == 0 for h in range(n)), (n,idx,vec,edges,pp,qq)
        assert all(sum(vec[eid] for eid, (a, b) in enumerate(edges) if b == h) == 0 for h in range(n))
        cycles.append(vec)
    return edges, cycles


def cycle_type(p):
    unseen = set(range(len(p))); sizes = []
    while unseen:
        i = unseen.pop(); count = 1; j = p[i]
        while j != i:
            unseen.remove(j); count += 1; j = p[j]
        sizes.append(count)
    return tuple(sorted(sizes))


def check(n):
    edges, basis = graph_cycle_basis(n)
    eidx = {edge: i for i, edge in enumerate(edges)}
    m = n*(n-1)
    rank = m - 2*n + 1
    assert len(basis) == rank == n*n - 3*n + 1
    unordered = [(i, j) for i in range(n) for j in range(i+1,n)]
    mapped = []
    for vec in basis:
        p = 0
        for a, (i,j) in enumerate(unordered):
            if (vec[eidx[(i,j)]] + vec[eidx[(j,i)]]) & 1:
                p |= (1 << a)
        assert p.bit_count() % 2 == 0
        assert all(sum(((p >> a)&1) for a,(u,v) in enumerate(unordered) if u==i or v==i)%2==0 for i in range(n))
        mapped.append(p)
    # Every even Eulerian parity vector is a sum of four-cycles of K_n.
    four_cycles = []
    if n >= 4:
        by_edge = {pair: bit for bit, pair in enumerate(unordered)}
        for i in range(n):
            for j in range(i+1, n):
                for a in range(n):
                    for b in range(a+1, n):
                        if len({i, j, a, b}) != 4:
                            continue
                        bitset = 0
                        for u,v in ((i,a),(i,b),(j,a),(j,b)):
                            bitset ^= 1 << by_edge[tuple(sorted((u,v)))]
                        four_cycles.append(bitset)
    assert gf2_rank(four_cycles) == n*(n-3)//2
    assert gf2_rank(mapped+four_cycles) == gf2_rank(mapped)
    extension_dim = gf2_rank(mapped)
    assert extension_dim == n*(n-3)//2
    assert rank == (n-1)*(n-2)//2 + n*(n-3)//2
    assert rank - extension_dim == (n-1)*(n-2)//2

    # Integral transpose-orientation action stabilizes the exact integer cycle lattice.
    for vec in basis:
        tau = [-vec[eidx[(j,i)]] for i,j in edges]
        assert all(sum(tau[eid] for eid, (a,b) in enumerate(edges) if a==i)==0 for i in range(n))
        assert all(sum(tau[eid] for eid, (a,b) in enumerate(edges) if b==i)==0 for i in range(n))
        assert [-tau[eidx[(j,i)]] for i,j in edges] == vec
    # Tests one representative of each conjugacy class, up to n=8.
    reps={}
    for perm in permutations(range(n)):
        cls=cycle_type(perm)
        if cls not in reps:reps[cls]=perm
    for cls, perm in reps.items():
        f=cls.count(1); t=cls.count(2)
        tr_oriented_edges=sum(perm[i]==i and perm[j]==j for i,j in edges)
        tr_vertices=2*f
        sigma_trace=tr_oriented_edges-tr_vertices+1
        assert sigma_trace==f*f-3*f+1
        tr_swapped_edges = -sum(perm[j]==i and perm[i]==j for i,j in edges)
        swap_trace=tr_swapped_edges+1
        assert swap_trace == 1-2*t
        # Characters of Lambda^2 Std and the pair-permutation kernel.
        plus = ((f-1)*(f-1)-(f+2*t-1))//2
        minus = comb(f,2) + t - f
        assert plus + minus == sigma_trace
        assert plus - minus == swap_trace
    print(f'n={n} | H1 rank={rank} | mod-2 gluing dim={extension_dim} | index=2^{extension_dim} | conjugacy types={len(reps)} PASS')


if __name__=='__main__':
    for number in range(3, 9):
        check(number)
    print('All exact checks passed.')
