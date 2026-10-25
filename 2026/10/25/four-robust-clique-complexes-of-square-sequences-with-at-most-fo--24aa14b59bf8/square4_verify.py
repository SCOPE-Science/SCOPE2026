"""Exhaustive finite square-sequence four-robust clique-complex verifier.

Run: python square4_verify.py
Requires Python >=3.10, networkx.
"""
from itertools import combinations
from collections import Counter
import networkx as nx


def unique_iso(graphs):
    # Isomorphism, not a graph hash, determines equality.
    representatives = []
    for candidate in graphs:
        if not any(nx.is_isomorphic(candidate, prior) for prior in representatives):
            representatives.append(candidate)
    return representatives


def extend(graph):
    new_vertex = max(graph.nodes) + 1
    for a, b in sorted((min(a,b), max(a,b)) for a,b in graph.edges):
        h=graph.copy()
        h.add_edges_from(((b,new_vertex),(new_vertex,new_vertex+1),(new_vertex+1,a)))
        yield h
    for b in sorted(graph):
        for a, c in combinations(sorted(graph.neighbors(b)), 2):
            h=graph.copy()
            h.add_edges_from(((a,new_vertex),(new_vertex,c)))
            yield h


def complex_faces(graph):
    # A nonface is exactly a subset containing an independent four-set.
    nodes = sorted(graph)
    assert nodes == list(range(len(nodes)))
    N=len(nodes)
    forb=[]
    for q in combinations(nodes, 4):
        if all(not graph.has_edge(a,b) for a,b in combinations(q,2)):
            forb.append(sum(1<<v for v in q))
    faces={m for m in range(1,1<<N) if not any(m&f==f for f in forb)}
    return faces,forb


def morse(graph):
    F,nonfaces=complex_faces(graph)
    current=set(F)
    matched=set()
    for vertex in range(len(graph)):
        bit=1<<vertex
        for low in sorted(tuple(current)):
            if low&bit:continue
            high=low|bit
            if low in current and high in current:
                current.remove(low);current.remove(high)
                matched.add((low,high))
    # Directed Hasse graph: matched covers ascend, unmatched covers descend.
    indeg={f:0 for f in F}
    outgoing={f:[] for f in F}
    for high in F:
        for v in range(len(graph)):
            bit=1<<v
            if not high&bit:continue
            low=high^bit
            if low==0 or low not in F:continue
            source,target=(low,high) if (low,high) in matched else (high,low)
            outgoing[source].append(target)
            indeg[target]+=1
    queue=[f for f in F if indeg[f]==0]
    visited=0
    while queue:
        f=queue.pop()
        visited+=1
        for g in outgoing[f]:
            indeg[g]-=1
            if indeg[g]==0:queue.append(g)
    assert visited==len(F), 'non-acyclic Morse matching'
    critical=Counter(f.bit_count()-1 for f in current)
    assert critical.get(0)==1
    assert set(critical).issubset({0,5}),critical
    assert len(F)==2*len(matched)+len(current)
    return len(F),len(nonfaces),len(matched),len(outgoing),critical


def main():
    levels=[[nx.cycle_graph(4)]]
    signature={}
    for level in range(1,5):
        if level>1:
            levels.append(unique_iso(h for g in levels[-1] for h in extend(g)))
        graphs=levels[-1]
        classifications=Counter()
        summary=[]
        for g in graphs:
            f,nf,m,e,c=morse(g)
            rank=c.get(5,0)
            classifications[(g.number_of_nodes(),rank)]+=1
            # canonical graph6 representative is not needed for the proof of isomorphism.
            summary.append((len(g),rank,f,nf,m))
        signature[level]=dict(sorted(classifications.items()))
        print('squares=',level, 'isomorphism_classes=',len(graphs),
              'classification=',sorted((v,r,c) for (v,r),c in classifications.items()),flush=True)
    assert [len(x) for x in levels]==[1,2,7,29]
    assert signature[1]=={(4,0):1}
    assert signature[2]=={(5,0):1,(6,0):1}
    assert signature[3]=={(6,0):2,(7,0):2,(8,1):3}
    assert signature[4]=={(7,0):3,(8,0):4,(8,1):4,(9,2):7,(9,3):2,(9,4):1,(10,4):8}
    print('PASS all 39 isomorphism classes: exhaustive enumeration, face criteria, acyclic matching, critical dimensions')

if __name__=='__main__':main()
