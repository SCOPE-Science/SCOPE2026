#!/usr/bin/env python3
"""Independent exact enumeration and square-flip checks for hypercube matchings.

Python >=3.9, standard library only. No externally downloaded data.
"""
from itertools import permutations, product
from collections import Counter, deque


def canonical_edge(u, v):
    assert u != v
    return (u, v) if u < v else (v, u)


def vertex_recursion(n):
    N = 1 << n
    result = set()

    def grow(free, edges):
        if not free:
            result.add(frozenset(edges))
            return
        v = min(free)
        for j in range(n):
            w = v ^ (1 << j)
            if w in free:
                grow(free - {v, w}, edges + (canonical_edge(v, w),))

    grow(set(range(N)), ())
    return result


def bipartite_injections(n):
    """Independent enumeration assigning every even-parity vertex to a different odd neighbor."""
    N = 1 << n
    even = [v for v in range(N) if v.bit_count() % 2 == 0]
    odd_set = {v for v in range(N) if v.bit_count() % 2}
    found = set()

    def backtrack(k, used, edges):
        if k == len(even):
            assert used == odd_set
            found.add(frozenset(edges))
            return
        v = even[k]
        for j in range(n):
            w = v ^ (1 << j)
            if w not in used:
                backtrack(k+1, used | {w}, edges + (canonical_edge(v,w),))

    backtrack(0, set(), ())
    return found


def faces(n):
    """Exactly one face for each fixed setting of the n-2 other coordinates."""
    result = []
    for j in range(n):
        for k in range(j+1, n):
            for root in range(1 << n):
                if root & ((1 << j) | (1 << k)):
                    continue
                a = root
                b = root ^ (1 << j)
                c = root ^ (1 << k)
                d = root ^ (1 << j) ^ (1 << k)
                x = frozenset((canonical_edge(a,b), canonical_edge(c,d)))
                y = frozenset((canonical_edge(a,c), canonical_edge(b,d)))
                result.append((x,y))
    assert len(result) == n*(n-1)*(1<<(n-3)) if n >= 3 else len(result)==1
    return result


def face_neighbours(matching, face_list):
    ans = set()
    for A, B in face_list:
        if A <= matching:
            ans.add((matching - A) | B)
        elif B <= matching:
            ans.add((matching - B) | A)
    return ans


def paired_edge_neighbours(matching):
    """Independent move search: inspect all unordered pairs of occupied edges,
    and test all endpoint reconnections without referring to a face list."""
    matching = frozenset(matching)
    edges = sorted(matching)
    ans = set()
    for i in range(len(edges)):
        for j in range(i+1, len(edges)):
            (a,b),(c,d) = edges[i],edges[j]
            for newpair in ((canonical_edge(a,c),canonical_edge(b,d)),
                            (canonical_edge(a,d),canonical_edge(b,c))):
                if all((u^v).bit_count()==1 for u,v in newpair):
                    # Two opposite edges in a 4-cycle; for Q_n every C4 is a face.
                    ans.add((matching-{edges[i],edges[j]})|frozenset(newpair))
    return ans


def adjgraph(states, n):
    face_list = faces(n)
    indexed = {m:i for i,m in enumerate(states)}
    graph = [set() for _ in states]
    for i,m in enumerate(states):
        q = face_neighbours(m,face_list)
        t = paired_edge_neighbours(m)
        assert q==t, (n,i)
        for next_m in q:
            assert next_m in indexed
            graph[i].add(indexed[next_m])
    assert all(i in graph[j] for i,vs in enumerate(graph) for j in vs)
    return graph


def components(graph):
    unused=set(range(len(graph)))
    components=[]
    while unused:
        v=min(unused)
        queue=[v]
        unused.remove(v)
        for u in queue:
            for w in sorted(graph[u]):
                if w in unused:
                    unused.remove(w)
                    queue.append(w)
        components.append(sorted(queue))
    return sorted(components,key=lambda c:(-len(c),c[0]))


def eccentricities(graph,comp):
    comp=set(comp)
    out=[]
    for start in comp:
        dist={start:0}
        queue=deque([start])
        while queue:
            u=queue.popleft()
            for v in graph[u]:
                if v not in dist:
                    dist[v]=dist[u]+1
                    queue.append(v)
        assert set(dist)==comp
        out.append(max(dist.values()))
    return Counter(out)


def transform_matching(m,n,perm,translation):
    def xform(v):
        r=translation
        for j in range(n):
            if (v>>j)&1:r ^= (1<<perm[j])
        return r
    return frozenset(canonical_edge(xform(a),xform(b)) for a,b in m)


def prove_quartet(frozen):
    """Search a cross-disjoint quartet, partitioned into two pairs."""
    F=list(sorted(frozen,key=lambda m:tuple(sorted(m))))
    for i in range(len(F)):
        for j in range(i+1,len(F)):
            for k in range(len(F)):
                if k in (i,j):continue
                for l in range(k+1,len(F)):
                    if l in (i,j):continue
                    if all(not (F[a]&F[b]) for a in (i,j) for b in (k,l)):
                        return (i,j,k,l), tuple(F[z] for z in (i,j,k,l))
    raise AssertionError('no cross-disjoint quartet')


def main():
    verified={}
    for n in (2,3,4):
        S=vertex_recursion(n)
        T=bipartite_injections(n)
        assert S==T
        states=sorted(S,key=lambda m:tuple(sorted(m)))
        graph=adjgraph(states,n)
        comps=components(graph)
        degree_hist=dict(sorted(Counter(map(len,graph)).items()))
        edge_count=sum(map(len,graph))//2
        ccs=[(len(c),sum(len(graph[v]) for v in c)//2) for c in comps]
        verified[n]=(states,graph,comps)
        print('Q%d: matchings=%d edges=%d components=%s degrees=%s'%(n,len(states),edge_count,ccs,degree_hist))
        if n<=3:
            assert len(comps)==1
            assert all(graph)
        else:
            assert len(states)==272
            assert edge_count==768
            assert sorted((len(c),sum(len(graph[v]) for v in c)//2) for c in comps)==[(1,0)]*8+[(264,768)]
            assert degree_hist=={0:8,3:32,4:12,5:96,6:48,8:72,12:4}
            ecc=eccentricities(graph,comps[0])
            assert min(ecc)==7 and max(ecc)==8
            print('Q4 giant eccentricities=',dict(sorted(ecc.items())))
            frozen={states[c[0]] for c in comps[1:]}
            assert len(frozen)==8
            seed=next(iter(frozen))
            orbit={transform_matching(seed,4,p,t) for p in permutations(range(4)) for t in range(16)}
            assert orbit==frozen
            print('Q4 frozen symmetry orbit=8, stabilizer=48')
            qids,matching_quartet=prove_quartet(frozen)
            assert all(not (a&b) for a in matching_quartet[:2] for b in matching_quartet[2:])
            print('cross-disjoint frozen quartet indices:',qids)
            for a,m in zip('ABCD',matching_quartet):
                print(a,sorted(m))
            # Check the construction for the first nontrivial higher dimension.
            A,B,C,D=matching_quartet
            for choice in product((0,1),repeat=2):
                # The two slices in Q5 receive one of A,B and one of C,D.
                low=(A,B)[choice[0]]
                high=(C,D)[choice[1]]
                big=frozenset((a+16*s,b+16*s) for s,small in enumerate((low,high)) for a,b in small)
                assert len(big)==16 and not face_neighbours(big,faces(5))
            print('Q5 test: four independently constructed frozen matchings verified')
    print('VERIFY_OK')

if __name__=='__main__':
    main()
