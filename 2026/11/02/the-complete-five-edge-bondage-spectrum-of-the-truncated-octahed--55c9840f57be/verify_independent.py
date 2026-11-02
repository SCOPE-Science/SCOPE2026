"""Independent exact certificate for five-edge bondage witnesses of the S4 permutohedron."""
from itertools import permutations, combinations
from collections import Counter

def main():
    verts = list(permutations(range(4)))
    idx = {p: i for i, p in enumerate(verts)}
    adj = [set() for _ in verts]
    for i, p in enumerate(verts):
        for k in range(3):
            q = list(p)
            q[k], q[k+1] = q[k+1], q[k]
            j = idx[tuple(q)]
            adj[i].add(j)
    edges = [(i,j) for i in range(24) for j in sorted(adj[i]) if i < j]
    edge_number = {e: i for i,e in enumerate(edges)}
    assert len(edges) == 36 and all(len(a) == 3 for a in adj)
    # Independent 24-vertex LCF description of the truncated-octahedral graph.
    lcf_to_perm = [0,1,7,6,8,14,15,9,11,10,20,21,23,17,16,22,19,18,4,5,3,13,12,2]
    assert sorted(lcf_to_perm) == list(range(24))
    lcf_edges = set()
    shifts = (3,-7,7,-3)
    for i in range(24):
        for j in ((i+1) % 24, (i+shifts[i % 4]) % 24):
            x,y = lcf_to_perm[i], lcf_to_perm[j]
            lcf_edges.add((min(x,y),max(x,y)))
    assert lcf_edges == set(edges)
    closed = [(1 << i) | sum(1 << u for u in adj[i]) for i in range(24)]
    full = (1 << 24)-1
    def dominating(d):
        cover = 0
        for i in d:
            cover |= closed[i]
        return cover == full
    # Monotonicity: if any k<=7 dominates, some seven-set dominates.
    assert not any(dominating(d) for d in combinations(range(24), 7))
    opt = [d for d in combinations(range(24),8) if dominating(d)]
    assert len(opt) == 1767
    killers = {}
    for i, D in enumerate(opt):
        Dset = set(D)
        for v in range(24):
            if v in Dset:
                continue
            qs = tuple(sorted(edge_number[(min(v,u),max(v,u))] for u in adj[v] if u in Dset))
            assert 1 <= len(qs) <= 3
            killers[qs] = killers.get(qs,0) | (1 << i)
    fullopt = (1 << len(opt)) -1
    winners = []
    for F in combinations(range(36),5):
        killed = 0
        for k in (1,2,3):
            for qs in combinations(F,k):
                killed |= killers.get(qs,0)
        if killed == fullopt:
            winners.append(F)
    assert len(winners) == 276
    winners_set = set(winners)
    automorphisms = []
    for a in permutations(range(4)):
        for reverse in (False,True):
            permutation=[]
            for v,p in enumerate(verts):
                q=p[::-1] if reverse else p
                permutation.append(idx[tuple(a[x] for x in q)])
            edge_perm=[]
            for x,y in edges:
                xx,yy = permutation[x],permutation[y]
                edge_perm.append(edge_number[(min(xx,yy),max(xx,yy))])
            assert len(set(edge_perm)) == 36
            automorphisms.append(tuple(edge_perm))
    assert len(set(automorphisms)) == 48
    unvisited=set(winners)
    sizes=[]
    representatives=[]
    while unvisited:
        F=min(unvisited)
        orb={tuple(sorted(g[e] for e in F)) for g in automorphisms}
        assert orb <= winners_set
        sizes.append(len(orb))
        representatives.append((min(orb),len(orb)))
        unvisited-=orb
    assert sorted(sizes) == [12,24,24,24,48,48,48,48]
    # Independently check one witness on the edge-deleted graph by direct search.
    exemplar = winners[0]
    def dominates_after_delete(D, F):
        cut = {edges[e] for e in F}
        cover = set(D)
        for v in D:
            for w in adj[v]:
                if (min(v,w),max(v,w)) not in cut:
                    cover.add(w)
        return len(cover)==24
    assert not any(dominates_after_delete(D,exemplar) for D in opt)
    print('VERIFY_OK vertices=24 edges=36 LCF_isomorphic=true minimum_dominating_sets=1767 deletion_5_cases=376992 bondage_five_sets=276 automorphisms=48 orbits=8 orbit_sizes='+str(sorted(sizes)))
    print('REPRESENTATIVES '+repr(sorted(representatives)))
if __name__=='__main__':
    main()
