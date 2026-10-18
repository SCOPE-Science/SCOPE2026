#!/usr/bin/env python3
"""Independent finite checks of signed cubical Lefschetz cancellation for graph flexes."""
from itertools import combinations, permutations
from collections import defaultdict


def sign_perm_on_ordered_set(ordered, p):
    image = [p[x] for x in ordered]
    return (-1) ** sum(image[i] > image[j] for i in range(len(image)) for j in range(i+1,len(image)))


def eval_graph(n, edges):
    edges = tuple(sorted(tuple(sorted(e)) for e in edges))
    edge_to_i = {e:i for i,e in enumerate(edges)}
    edge_set = set(edges)
    automorphisms = [p for p in permutations(range(n)) if {tuple(sorted((p[a],p[b]))) for a,b in edges}==edge_set]
    orientations = list(range(1<<len(edges)))
    sinksets = {}
    for bits in orientations:
        outgoing = [0]*n
        for k,(u,v) in enumerate(edges):
            if (bits>>k)&1: outgoing[u]+=1
            else: outgoing[v]+=1
        sinksets[bits] = frozenset(i for i,x in enumerate(outgoing) if x==0)
    def act(bits,p):
        out=0
        for k,(u,v) in enumerate(edges):
            a,b=(u,v) if ((bits>>k)&1) else (v,u)
            x,y=p[a],p[b]
            new_k=edge_to_i[tuple(sorted((x,y)))]
            if x<y: out|=1<<new_k
        return out
    signed_checked=0
    for p in automorphisms:
        fixed=[o for o in orientations if act(o,p)==o]
        fixed_sinkless=sum(not sinksets[o] for o in fixed)
        signed_trace=0
        cell_count=0
        for o in fixed:
            ss=sorted(sinksets[o])
            for d in range(len(ss)+1):
                for A in combinations(ss,d):
                    if frozenset(p[x] for x in A)==frozenset(A):
                        signed_trace+=(-1)**d *sign_perm_on_ordered_set(A,p)
                        cell_count+=1
        assert signed_trace==fixed_sinkless,(n,edges,p,signed_trace,fixed_sinkless)
        # A second independent computation: orbitwise sink inclusion/exclusion.
        vert_orbits=[]; seen=set()
        for v in range(n):
            if v in seen:continue
            cur=[]; x=v
            while x not in seen:
                cur.append(x);seen.add(x);x=p[x]
            vert_orbits.append(frozenset(cur))
        unoriented_edge_orbits=[]; seen_e=set(); flips_edge=False
        for e in edges:
            if e in seen_e:continue
            orbit=[];a,b=e;pair=e
            while pair not in seen_e:
                seen_e.add(pair);orbit.append(pair)
                a,b=p[a],p[b];pair=tuple(sorted((a,b)))
            # After one full edge orbit, the oriented pair (a,b) may be reversed.
            if (a,b)!=e:flips_edge=True
            unoriented_edge_orbits.append(orbit)
        ie_sum=0
        if not flips_edge:
            for r in range(len(vert_orbits)+1):
                for idx in combinations(range(len(vert_orbits)),r):
                    B=set().union(*(vert_orbits[k] for k in idx)) if idx else set()
                    if any(a in B and b in B for a,b in edges):continue
                    free_orbits=sum(all(a not in B and b not in B for a,b in eo) for eo in unoriented_edge_orbits)
                    ie_sum+=(-1)**r * 2**free_orbits
        assert ie_sum==fixed_sinkless,(n,edges,p,ie_sum,fixed_sinkless)
        signed_checked+=1
    # Euler scalar independently counted as signed sum over all canonical cells.
    euler=sum((-1)**d for o in orientations for d in range(len(sinksets[o])+1) for _ in combinations(sinksets[o],d))
    assert euler==sum(not sinksets[o] for o in orientations)
    # The Reynolds average equals the number of orbit classes of sinkless orientations.
    sinkless=[o for o in orientations if not sinksets[o]]
    visited=set(); orbits=0
    for o in sinkless:
        if o in visited:continue
        visited.update(act(o,p) for p in automorphisms)
        orbits+=1
    assert orbits*len(automorphisms)==sum(sum(act(o,p)==o for o in sinkless) for p in automorphisms)
    return len(automorphisms),len(orientations),signed_checked,orbits


def main():
    graphs=[]
    graphs.append(('single-edge',2,[(0,1)]))
    graphs.append(('three-path',3,[(0,1),(1,2)]))
    graphs.append(('triangle',3,[(0,1),(1,2),(0,2)]))
    graphs.append(('square',4,[(i,(i+1)%4) for i in range(4)]))
    graphs.append(('four-path',4,[(i,i+1) for i in range(3)]))
    graphs.append(('four-clique',4,list(combinations(range(4),2))))
    graphs.append(('star-four',5,[(0,i) for i in range(1,5)]))
    graphs.append(('pentagon',5,[(i,(i+1)%5) for i in range(5)]))
    graphs.append(('triangle-plus-leaf',4,[(0,1),(1,2),(0,2),(2,3)]))
    graphs.append(('disjoint-pair',4,[(0,1),(2,3)]))
    graphs.append(('square-plus-diagonal',4,[(i,(i+1)%4) for i in range(4)]+[(0,2)]))
    for title,n,E in graphs:
        autos,ori,checks,orbits=eval_graph(n,E)
        print(f'{title}: vertices={n} orientations={ori} automorphisms={autos} signed_checks={checks} sinkless_orbits={orbits}')
    print('VERIFY_OK graph_families=11')

if __name__=='__main__':main()
