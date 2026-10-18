#!/usr/bin/env python3
"""Independent brute-force checks for minimum dominating sets of a subdivided leaf-corona.
Usage: python3 verify.py
Requires only Python 3 standard library. All graphs are labelled, simple, undirected.
"""
from itertools import combinations
from collections import deque
from math import comb


def graph_B(n, edges):
    # original 0..n-1, leaves n..2n-1, subdivision vertices 2n..
    N = 2*n + len(edges)
    nbr = [0]*N
    def add(u,v):
        nbr[u] |= 1<<v
        nbr[v] |= 1<<u
    for v in range(n):
        add(v, n+v)
    for j,(u,v) in enumerate(edges):
        add(u,2*n+j)
        add(v,2*n+j)
    return nbr


def is_independent(n, edges, mask):
    return all(not ((mask>>u)&1 and (mask>>v)&1) for u,v in edges)


def brute_minimum(n, edges):
    nbr=graph_B(n,edges)
    N=len(nbr)
    allbits=(1<<N)-1
    gamma=N+1
    mins=set()
    count=0
    for mask in range(1<<N):
        count+=1
        # Dominates all vertices: union of closed neighborhoods of selected vertices.
        cover=mask
        j=mask
        while j:
            last=j&-j
            cover|=nbr[last.bit_length()-1]
            j^=last
        if cover != allbits:
            continue
        weight=mask.bit_count()
        if weight<gamma:
            gamma=weight
            mins={mask}
        elif weight==gamma:
            mins.add(mask)
    return gamma,mins,count


def predicted(n,edges):
    return {(sum((1<<(v+n)) if ((I>>v)&1) else (1<<v) for v in range(n)),I.bit_count())
            for I in range(1<<n) if is_independent(n,edges,I)}


def cube_counts_from_faces(n,edges):
    # Form the actual independent-set reconfiguration graph, then enumerate
    # vertex collections forming coordinate faces and check every induced edge.
    ind={s for s in range(1<<n) if is_independent(n,edges,s)}
    adj={s:{t for t in ind if (s^t).bit_count()==1} for s in ind}
    out=[0]*(n+1)
    for k in range(n+1):
        seen=set()
        for fixed in range(1<<n):
            for coords in combinations([v for v in range(n) if not (fixed>>v)&1],k):
                verts={fixed|sum(1<<v for v in selection)
                       for length in range(k+1) for selection in combinations(coords,length)}
                if not verts.issubset(ind):
                    continue
                if all((u in adj[v]) == ((u^v).bit_count()==1)
                       for u in verts for v in verts if u!=v):
                    seen.add(frozenset(verts))
        out[k]=len(seen)
    return out


def distances_match(n, edges):
    ind={s for s in range(1<<n) if is_independent(n,edges,s)}
    adj={s:[t for t in ind if (s^t).bit_count()==1] for s in ind}
    for origin in ind:
        dist={origin:0}
        q=deque([origin])
        while q:
            v=q.popleft()
            for w in adj[v]:
                if w not in dist:
                    dist[w]=dist[v]+1
                    q.append(w)
        if len(dist)!=len(ind) or any(dist[t]!=(origin^t).bit_count() for t in ind):
            return False
    return True


def check(n, edges):
    gamma, mins, count = brute_minimum(n,edges)
    expected=predicted(n,edges)
    predicted_D={d for d,_ in expected}
    assert gamma==n and mins==predicted_D, (n,edges,gamma,mins^predicted_D)
    # Compute actual slide and jump adjacency directly from derived minimum sets,
    # rather than inferring adjacency merely from the source independent sets.
    nbr=graph_B(n,edges)
    labels={d:sum(1<<v for v in range(n) if (d>>(n+v))&1) for d in mins}
    for a,b in combinations(sorted(mins),2):
        dropped=a & ~b
        inserted=b & ~a
        jump=(dropped.bit_count()==1 and inserted.bit_count()==1)
        slide=jump and bool(nbr[dropped.bit_length()-1] & inserted)
        source_flip=((labels[a]^labels[b]).bit_count()==1)
        assert jump==source_flip and slide==source_flip,(n,edges,a,b,jump,slide,source_flip)
    coeff=[sum(1 for _,k in expected if k==i) for i in range(n+1)]
    # Count cubes by their induced vertex graph rather than reusing the formula.
    cubes=cube_counts_from_faces(n,edges)
    expected_cubes=[sum(c*comb(j,k) for j,c in enumerate(coeff) if j>=k)
                    for k in range(n+1)]
    assert cubes==expected_cubes,(n,edges,cubes,expected_cubes)
    assert distances_match(n,edges)
    return count,len(mins),coeff,cubes


def main():
    checks=0
    graph_count=0
    maximum_N=0
    for n in range(1,5):
        possible=list(combinations(range(n),2))
        for e_mask in range(1<<len(possible)):
            E=[e for i,e in enumerate(possible) if (e_mask>>i)&1]
            count, sets, _, _=check(n,E)
            checks+=count
            graph_count+=1
            maximum_N=max(maximum_N,2*n+len(E))
    # Explicit nontrivial five-vertex samples, including dense and sparse cases.
    n=5
    tests={
        "empty":[],
        "complete":list(combinations(range(n),2)),
        "path": [(0,1),(1,2),(2,3),(3,4)],
        "cycle": [(0,1),(1,2),(2,3),(3,4),(4,0)],
        "star": [(0,i) for i in range(1,5)],
        "complete_bipartite": [(i,j) for i in (0,1) for j in (2,3,4)],
    }
    for tag,E in tests.items():
        count,sets,coeff,cubes=check(n,E)
        checks+=count
        graph_count+=1
        maximum_N=max(maximum_N,2*n+len(E))
        print(f"five-vertex sample {tag}: gamma=5, minima={sets}, coeff={coeff}, cubes={cubes}")
    print(f"PASS: exhaustive checks of {checks} selected subsets across {graph_count} source graphs; maximum derived graph order {maximum_N}.")
    print("PASS: each minimum dominating set bijects to a source independent set; slide and jump edges agree; Hamming shortest distances agree; cube polynomial coefficients agree.")

if __name__ == '__main__':
    main()
