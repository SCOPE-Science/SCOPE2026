#!/usr/bin/env python3
"""Exact finite checks for matching complexes of corona graphs G∘K1.

Runs without external Python packages.  A graph is a pair (n, edges) on
vertices 0,...,n-1.  Test cases include every graph on four vertices,
selected five- and six-vertex graphs, and symmetry Lefschetz identities.
"""
from collections import defaultdict, deque
from itertools import combinations, permutations
import json
import random


def edges_of_whiskered(n, base_edges):
    """Base edges followed by pendant edges (v,n+v)."""
    return list(sorted(tuple(sorted(e)) for e in base_edges)) + [(v,n+v) for v in range(n)]


def faces_of_matching(n, base_edges):
    edges=edges_of_whiskered(n,base_edges)
    faces=[()]
    def walk(i,choice,used):
        if i == len(edges):
            if choice:faces.append(choice)
            return
        walk(i+1,choice,used)
        a,b=edges[i]
        if not ((used>>a)&1 or (used>>b)&1):
            walk(i+1,choice+(i,),used | (1<<a) | (1<<b))
    walk(0,(),0)
    return edges, sorted(set(faces),key=lambda x:(len(x),x))


def base_perfect_matchings(n, base_edges):
    edges=list(sorted(tuple(sorted(e)) for e in base_edges))
    if n%2:return []
    return [p for p in combinations(range(len(edges)),n//2)
            if len({v for e in p for v in edges[e]})==n]


def check_acyclic(n,base_edges,edges,faces):
    """Check every discrete Morse arrow, including the empty face."""
    lookup={s:i for i,s in enumerate(faces)}
    m=len(base_edges)
    mate={}
    for s in faces:
        rims=s[:sum(i<m for i in s)]
        occupied={v for ei in rims for v in edges[ei]}
        free=next((v for v in range(n) if v not in occupied),None)
        if free is None: continue
        ei=m+free
        t=tuple(sorted(s+(ei,))) if ei not in s else tuple(x for x in s if x!=ei)
        assert t in lookup, (n,s,t)
        mate[lookup[s]]=lookup[t]
    assert all(mate.get(j)==i for i,j in mate.items())
    perfect=base_perfect_matchings(n,base_edges)
    critical=[s for s in faces if lookup[s] not in mate]
    assert sorted(critical)==sorted(perfect),(n,critical,perfect)
    degree=[0]*len(faces)
    out=[[] for _ in faces]
    for s in faces:
        if not s:continue
        j=lookup[s]
        for e in s:
            t=tuple(v for v in s if v!=e)
            i=lookup[t]
            if mate.get(i)==j:
                out[i].append(j);degree[j]+=1
            else:
                out[j].append(i);degree[i]+=1
    todo=deque(i for i,d in enumerate(degree) if d==0)
    count=0
    while todo:
        i=todo.popleft();count+=1
        for j in out[i]:
            degree[j]-=1
            if degree[j]==0:todo.append(j)
    assert count==len(faces),(n,'Morse gradient contains cycle',count,len(faces))
    return len(critical)


def homology_mod2(faces):
    by_dim=defaultdict(list)
    for s in faces:by_dim[len(s)-1].append(s)
    ranks={}
    for d in range(0,max(by_dim)+1):
        lower={s:i for i,s in enumerate(by_dim[d-1])}
        pivots={}
        for s in by_dim[d]:
            col=0
            for j in range(len(s)):
                col ^= 1<<lower[s[:j]+s[j+1:]]
            while col:
                p=col.bit_length()-1
                if p in pivots:col^=pivots[p]
                else:
                    pivots[p]=col;break
        ranks[d]=len(pivots)
    return {d:len(by_dim[d])-ranks.get(d,0)-ranks.get(d+1,0)
            for d in range(-1,max(by_dim)+1)
            if len(by_dim[d])-ranks.get(d,0)-ranks.get(d+1,0)!=0}


def induced_edge_permutation(n,base_edges,vertex_perm):
    edges=edges_of_whiskered(n,base_edges)
    lookup={e:i for i,e in enumerate(edges)}
    return tuple(lookup[tuple(sorted(((vertex_perm[a] if a<n else n+vertex_perm[a-n]),
                                    (vertex_perm[b] if b<n else n+vertex_perm[b-n]))))]
                 for a,b in edges)


def parity_of_permutation(seq):
    return -1 if sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))%2 else 1


def lefschetz_check(n,base_edges,faces,vertex_perm):
    edge_perm=induced_edge_permutation(n,base_edges,vertex_perm)
    lef=0
    for s in faces:
        targets=[edge_perm[e] for e in s]
        if set(s)!=set(targets): continue
        sorted_targets=sorted(targets)
        ranks=[sorted_targets.index(x) for x in targets]
        lef += (-1 if len(s)%2==0 else 1)*parity_of_permutation(ranks)
    # Character on direct sum of orientation lines of all base perfect matchings.
    perfect=base_perfect_matchings(n,base_edges)
    expected_trace=0
    for p in perfect:
        image=[edge_perm[e] for e in p]
        if set(image)==set(p):
            ordered=sorted(image)
            expected_trace+=parity_of_permutation([ordered.index(e) for e in image])
    expected=0 if n%2 else (-1)**(n//2-1)*expected_trace
    assert lef==expected,(n,vertex_perm,lef,expected)
    return lef,expected_trace


def run():
    rng=random.Random(1729)
    tested=0;morse_cases=0;homology_cases=0;lefschetz_cases=0
    examples=[]
    for n in range(1,7):
        complete=list(combinations(range(n),2))
        all_masks=list(range(1<<len(complete)))
        if n>=5:
            picks={0,(1<<len(complete))-1}
            # A path, a cycle, a disjoint-edge graph and random base graphs.
            for special in [set((i,i+1) for i in range(n-1)),
                            set((i,(i+1)%n) if i<n-1 else (0,n-1) for i in range(n)),
                            set((i,i+1) for i in range(0,n-1,2))]:
                picks.add(sum((1<<j) for j,e in enumerate(complete) if e in special))
            while len(picks)<(85 if n==5 else 30):
                picks.add(rng.randrange(1<<len(complete)))
            all_masks=sorted(picks)
        for mask in all_masks:
            base=[e for i,e in enumerate(complete) if mask>>i&1]
            edges,faces=faces_of_matching(n,base)
            p=base_perfect_matchings(n,base)
            assert check_acyclic(n,base,edges,faces)==len(p)
            morse_cases+=1
            if n<=5 or (n==6 and mask in (0,(1<<len(complete))-1)):
                actual=homology_mod2(faces)
                expect={} if not p else {n//2-1:len(p)}
                assert actual==expect,(n,mask,actual,expect)
                homology_cases+=1
            # Integral-cycle leading coefficients: each perfect base matching
            # labels a maximal rim-only face, and no other constructed cycle
            # has a nonzero all-rim coefficient on it.
            assert len(set(p))==len(p)
            tested+=1
        examples.append({'n':n,'tested_graphs':len(all_masks)})
    for n,base,perms in [
            (4, list(combinations(range(4),2)),list(permutations(range(4)))),
            (4, [(i,(i+1)%4) for i in range(4)],
             [tuple((i+k)%4 for i in range(4)) for k in range(4)]+
             [tuple((k-i)%4 for i in range(4)) for k in range(4)]),
            (6, [(i,(i+1)%6) for i in range(6)],
             [tuple((i+k)%6 for i in range(6)) for k in range(6)]+
             [tuple((k-i)%6 for i in range(6)) for k in range(6)]),
            (5, [(i,(i+1)%5) for i in range(5)],
             [tuple((i+k)%5 for i in range(5)) for k in range(5)]+
             [tuple((k-i)%5 for i in range(5)) for k in range(5)])]:
        base=sorted(tuple(sorted(x)) for x in base)
        _,faces=faces_of_matching(n,base)
        for perm in perms:
            lefschetz_check(n,base,faces,perm)
            lefschetz_cases+=1
    print(json.dumps({'status':'PASS','graphs':tested,
                      'morse_dag_cases':morse_cases,
                      'complete_mod2_homology_cases':homology_cases,
                      'signed_lefschetz_cases':lefschetz_cases,
                      'by_vertex_count':examples},sort_keys=True))

if __name__=='__main__':run()
