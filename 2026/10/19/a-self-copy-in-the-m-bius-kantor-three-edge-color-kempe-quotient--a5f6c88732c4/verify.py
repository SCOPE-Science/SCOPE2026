#!/usr/bin/env python3
"""Reproduce the exact three-edge-coloring Kempe-state classification of GP(8,3).

Run: python3 verify.py. Requires only Python's standard library.
All enumerations are exhaustive, not statistical tests.
"""
from collections import Counter, deque
from itertools import combinations, permutations

N = 16
EDGES = sorted({tuple(sorted(pair)) for i in range(8) for pair in
                ((i, (i+1)%8), (i, 8+i), (8+i, 8+(i+3)%8))})
assert len(EDGES) == 24 and all(0 <= u < v < N for u,v in EDGES)
INC = [[] for _ in range(N)]
for ei,(u,v) in enumerate(EDGES):
    INC[u].append((v,ei)); INC[v].append((u,ei))
assert all(len(row)==3 for row in INC)
FULL = (1 << len(EDGES)) - 1

def perfect_matchings():
    """Exact independent perfect matching recursion (first unmatched vertex)."""
    out = []
    def extend(free, chosen):
        if not free:
            out.append(chosen); return
        v = (free & -free).bit_length()-1
        for w,e in INC[v]:
            if free & (1 << w):
                extend(free ^ (1 << v) ^ (1 << w), chosen | (1 << e))
    extend((1 << N)-1, 0)
    assert len(out)==len(set(out))
    return sorted(out)

def factor_from_matching_recursion():
    pm = perfect_matchings(); P=set(pm)
    fac={tuple(sorted((a,b,FULL^(a|b)))) for a,b in combinations(pm,2)
         if (a&b)==0 and FULL^(a|b) in P}
    assert len(pm)==33
    return sorted(fac)

def factor_from_edge_coloring_backtracking():
    """Independent enumeration: directly assign each of 24 edges one of 3 colors.
    Colors at vertex 0 are fixed in increasing edge order; global S3
    normalization makes one representative of each 1-factorization.
    """
    used=[0]*N; assignment=[-1]*len(EDGES)
    for color, (_,edge) in enumerate(sorted(INC[0],key=lambda t:t[1])):
        u,v=EDGES[edge];assignment[edge]=color
        used[u] |= 1<<color;used[v] |= 1<<color
    result=set()
    def rec(remaining):
        if not remaining:
            masks=[0,0,0]
            for j,color in enumerate(assignment):masks[color]|=1<<j
            result.add(tuple(sorted(masks)))
            return
        chosen=None; opts=();best=4
        for e in remaining:
            u,v=EDGES[e]; a=tuple(c for c in range(3)
                              if not ((used[u]|used[v]) & (1<<c)))
            if len(a)<best:
                chosen=e;opts=a;best=len(a)
                if not best: return
                if best==1:break
        u,v=EDGES[chosen]
        for c in opts:
            bit=1<<c;used[u]|=bit;used[v]|=bit;assignment[chosen]=c
            rec(tuple(e for e in remaining if e!=chosen))
            used[u]^=bit;used[v]^=bit;assignment[chosen]=-1
    rec(tuple(e for e,c in enumerate(assignment) if c<0))
    return sorted(result)

def cycle_masks(a,b):
    """Connected two-colored cycle masks in union of two disjoint matchings."""
    z=a|b; unseen={i for i in range(len(EDGES)) if z>>i & 1}
    cycles=[]
    while unseen:
        ei=min(unseen); stack=[EDGES[ei][0]];seen={stack[0]};cyc=0
        while stack:
            u=stack.pop()
            for v,j in INC[u]:
                if (z>>j)&1:
                    cyc|=1<<j
                    if v not in seen:seen.add(v);stack.append(v)
        curr={j for j in range(len(EDGES)) if cyc>>j&1}
        assert curr <= unseen
        unseen-=curr
        assert len(curr)==len(seen) and all(sum(bool(cyc>>j&1) for _,j in INC[u])==2
                                        for u in seen)
        cycles.append(cyc)
    return cycles

def quotient_adjacency_by_cycles(F):
    index={f:i for i,f in enumerate(F)}
    adj=[set() for _ in F]
    for i,f in enumerate(F):
        for a,b in ((0,1),(0,2),(1,2)):
            for mask in cycle_masks(f[a],f[b]):
                nxt=list(f);nxt[a]^=mask;nxt[b]^=mask
                j=index[tuple(sorted(nxt))]
                if i!=j: adj[i].add(j)
    assert all(i in adj[j] for j,li in enumerate(adj) for i in li)
    return adj

def one_cycle_symmetric_difference(a,b):
    z=a^b
    if not z:return False
    active={j for j in range(len(EDGES)) if z>>j&1}
    # Every component of this symmetric difference is an even cycle.
    # Test whether it consists of exactly one connected component.
    vertex=EDGES[min(active)][0];visited={vertex};stack=[vertex]
    while stack:
        u=stack.pop()
        for v,j in INC[u]:
            if j in active and v not in visited:
                visited.add(v);stack.append(v)
    return all(EDGES[j][0] in visited for j in active)

def quotient_adjacency_by_pairwise_matching_test(F):
    """Independent adjacency reconstruction using pairwise factor comparison."""
    adj=[set() for _ in F]
    for i,j in combinations(range(len(F)),2):
        common=set(F[i]) & set(F[j])
        if len(common)!=1:continue
        s=next(iter(common))
        if any(one_cycle_symmetric_difference(a,b)
               for a in F[i] if a!=s for b in F[j] if b!=s):
            adj[i].add(j);adj[j].add(i)
    return adj

def components(adj):
    unseen=set(range(len(adj)));comps=[]
    while unseen:
        seed=min(unseen);unseen.remove(seed);seen={seed};q=deque([seed])
        while q:
            for v in adj[q.popleft()]:
                if v not in seen:
                    seen.add(v);q.append(v);unseen.remove(v)
        comps.append(seen)
    return sorted(comps,key=lambda s:(len(s),min(s)))

def graph_edges_from_mapping(adj, nodes, labels):
    return {tuple(sorted((labels[i],labels[j]))) for i in nodes
            for j in adj[i] if i<j}

def labelled_kempe_graph(F):
    colorings=sorted(set(p for f in F for p in permutations(f)))
    assert len(colorings)==120
    idx={f:i for i,f in enumerate(colorings)}
    adj=[set() for _ in colorings]
    for i,f in enumerate(colorings):
        for a,b in ((0,1),(0,2),(1,2)):
            for mask in cycle_masks(f[a],f[b]):
                nxt=list(f);nxt[a]^=mask;nxt[b]^=mask
                j=idx[tuple(nxt)]
                assert i!=j;adj[i].add(j)
    assert all(i in adj[j] for j,li in enumerate(adj) for i in li)
    return colorings,adj

def radius_diameter(adj,comp):
    radius=10**9;diameter=0;hist=Counter()
    for source in comp:
        D={source:0};q=deque([source])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if v not in D:D[v]=D[u]+1;q.append(v)
        assert set(D)==comp
        radius=min(radius,max(D.values()));diameter=max(diameter,max(D.values()))
        hist.update(D.values())
    return radius,diameter,dict(sorted(hist.items()))

def main():
    a=factor_from_matching_recursion()
    b=factor_from_edge_coloring_backtracking()
    assert a==b,('two enumerators disagree',len(a),len(b))
    assert len(a)==20
    Q=quotient_adjacency_by_cycles(a)
    Q2=quotient_adjacency_by_pairwise_matching_test(a)
    assert Q==Q2
    qc=components(Q)
    assert sorted(map(len,qc))==[4,16]
    assert sum(map(len,Q))//2==27
    small,big=qc
    assert small=={0,1,4,11} and Q[1]=={0,4,11}
    assert all(Q[v]=={1} for v in (0,4,11))
    assert all(len(Q[i])==3 for i in big)
    # Explicit graph isomorphism: F sorted as tuples of binary edge masks.
    # Verify *every* edge and nonedge against the original GP(8,3).
    isomap={2:0,3:8,5:7,6:15,7:3,8:11,9:2,10:1,
            12:9,13:12,14:13,15:5,16:6,17:14,18:10,19:4}
    assert set(isomap)==big and set(isomap.values())==set(range(16))
    base_edges=set(EDGES)
    image_edges=graph_edges_from_mapping(Q,big,isomap)
    assert image_edges==base_edges
    for i,j in combinations(sorted(big),2):
        mapped=tuple(sorted((isomap[i],isomap[j])))
        assert (j in Q[i]) == (mapped in base_edges)
    C,K=labelled_kempe_graph(a)
    cc=components(K)
    assert sorted(map(len,cc))==[24,96]
    assert sum(map(len,K))//2==342
    for comp in cc:
        n=len(comp);subedges=sum(len(K[i]) for i in comp)//2
        radius,diameter,hist=radius_diameter(K,comp)
        if n==24:
            assert subedges==54 and (radius,diameter)==(3,3)
            assert Counter(len(K[i]) for i in comp)==Counter({4:18,6:6})
        else:
            assert subedges==288 and (radius,diameter)==(4,4)
            assert set(len(K[i]) for i in comp)=={6}
        print('labelled component:',n,'edges',subedges,'radius',radius,
              'diameter',diameter,'degrees',sorted(Counter(len(K[i]) for i in comp).items()),
              'ordered distance histogram',hist)
    assert {len({tuple(sorted(C[i])) for i in co}) for co in cc}=={4,16}
    print('perfect_matchings',len(perfect_matchings()))
    print('unlabelled_factorizations',len(a),'labelled_edge_colorings',len(C))
    print('quotient_edges',sum(map(len,Q))//2,'components',sorted(map(len,qc)))
    print('quotient_isomorphism K1,3 disjoint GP(8,3): VERIFIED')
    print('independent matching and direct edge-color enumerators: AGREE')
    print('independent quotient constructions: AGREE')
    print('ALL CHECKS PASS')

if __name__=='__main__':main()
