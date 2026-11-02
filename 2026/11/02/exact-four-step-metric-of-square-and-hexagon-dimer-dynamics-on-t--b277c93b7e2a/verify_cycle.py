#!/usr/bin/env python3
"""Exhaustive certificate builder/checker for Q4 perfect-matching flips.

Usage: python3 verify_cycle.py --write certificate.json
       python3 verify_cycle.py certificate.json
Only the Python standard library is required.
"""
import argparse
import collections
import json

EXPECTED = {
    'states': 272, 'squares': 24, 'hexagons': 128,
    'edges_4': 768, 'edges_6': 1216,
    'four_components': [1,1,1,1,1,1,1,1,264],
    'six_components': [272], 'six_radius': 4, 'six_diameter': 4,
    'six_eccentricities': {'4': 272},
    'six_distance_pairs': {'1':1984,'2':10784,'3':19568,'4':4520},
    'four_giant_radius': 7, 'four_giant_diameter': 8,
    'four_giant_eccentricities': {'7':252,'8':12},
    'four_frozen_count': 8, 'four_frozen_six_flip_degree': 8,
}

def edges(n):
    return {v: tuple(v^(1<<i) for i in range(n)) for v in range(1<<n)}

def perfect_matchings(n, graph):
    out = []
    def visit(remaining, chosen):
        if not remaining:
            out.append(tuple(sorted(chosen)))
            return
        v = min(remaining)
        for w in graph[v]:
            if w in remaining:
                visit(remaining - {v, w}, chosen + ((min(v,w),max(v,w)),))
    visit(set(graph), ())
    return sorted(out)

def simple_cycles(graph, length):
    found = set()
    def grow(path):
        for nxt in graph[path[-1]]:
            if nxt == path[0] and len(path) == length:
                cycle = frozenset(tuple(sorted((a,b))) for a,b in zip(path,path[1:]+path[:1]))
                assert len(cycle) == length
                found.add(cycle)
            elif len(path)<length and nxt>path[0] and nxt not in path:
                grow(path+[nxt])
    for v in graph: grow([v])
    return sorted(found, key=lambda x: tuple(sorted(x)))

def components(adj):
    visited = set(); blocks=[]
    for v in range(len(adj)):
        if v in visited: continue
        todo = [v]; visited.add(v)
        for q in todo:
            for w in adj[q]:
                if w not in visited:
                    visited.add(w);todo.append(w)
        blocks.append(tuple(todo))
    return sorted(blocks,key=lambda b: (len(b),min(b)))

def distances(adj, start):
    found = {start: 0}; q = collections.deque([start])
    while q:
        v = q.popleft()
        for w in adj[v]:
            if w not in found:
                found[w] = found[v]+1; q.append(w)
    return found

def classify(squares,hexagons,ms):
    id_of = {frozenset(m):k for k,m in enumerate(ms)}
    assert len(id_of)==len(ms)
    adjacency = [[],[]]
    for m in ms:
        sm = frozenset(m)
        row=[]
        for pool in (squares, hexagons):
            vals=set()
            for cyc in pool:
                if len(sm & cyc) == len(cyc)//2:
                    nxt = (sm-cyc) | (cyc-sm)
                    assert len(nxt)==len(m)
                    vals.add(id_of[nxt])
            row.append(sorted(vals))
        adjacency[0].append(row[0]); adjacency[1].append(row[1])
    return adjacency

def build():
    graph = edges(4)
    ms = perfect_matchings(4,graph)
    sq = simple_cycles(graph,4)
    hx = simple_cycles(graph,6)
    ad4,ad6 = classify(sq,hx,ms)
    assert len(ms)==272 and len(sq)==24 and len(hx)==128
    assert all(i in ad4[j] for j,row in enumerate(ad4) for i in row)
    assert all(i in ad6[j] for j,row in enumerate(ad6) for i in row)
    assert all(set(a).isdisjoint(b) for a,b in zip(ad4,ad6))
    ad46=[sorted(set(a)|set(b)) for a,b in zip(ad4,ad6)]
    blocks4 = components(ad4);blocks6=components(ad46)
    eccentric46=[]; pairs=collections.Counter();ecc4_giant=[]
    for v in range(272):
        d=distances(ad46,v)
        eccentric46.append(max(d.values()))
        pairs.update(k for k in d.values() if k>0)
    for v in max(blocks4,key=len):
        eccentric4=distances(ad4,v)
        ecc4_giant.append(max(eccentric4.values()))
    frozen=[i for i,row in enumerate(ad4) if not row]
    stats={
        'states':len(ms),'squares':len(sq),'hexagons':len(hx),
        'edges_4':sum(map(len,ad4))//2,'edges_6':sum(map(len,ad6))//2,
        'four_components':sorted(len(b) for b in blocks4),
        'six_components':sorted(len(b) for b in blocks6),
        'six_radius':min(eccentric46), 'six_diameter':max(eccentric46),
        'six_eccentricities':{str(k):v for k,v in sorted(collections.Counter(eccentric46).items())},
        'six_distance_pairs':{str(k):v//2 for k,v in sorted(pairs.items())},
        'four_giant_radius':min(ecc4_giant), 'four_giant_diameter':max(ecc4_giant),
        'four_giant_eccentricities':{str(k):v for k,v in sorted(collections.Counter(ecc4_giant).items())},
        'four_frozen_count':len(frozen),
        'four_frozen_six_flip_degree':min(map(lambda i:len(ad6[i]),frozen)),
    }
    assert stats==EXPECTED, (stats,EXPECTED)
    assert all(len(ad6[i])==8 for i in frozen)
    assert len(perfect_matchings(2,edges(2)))==2
    assert len(perfect_matchings(3,edges(3)))==9
    for dim in (2,3):
        graph_small=edges(dim)
        sq_small=simple_cycles(graph_small,4)
        states_small=perfect_matchings(dim,graph_small)
        small_ad4,_=classify(sq_small,[],states_small)
        assert len(components(small_ad4))==1
    return {'format':'Q4-matching-flip-adjacency-v1',
        'vertex_labels':'integers 0..15; Hamming-distance-one edges',
        'states':[[list(e) for e in m] for m in ms],
        'neighbors_4':ad4,'neighbors_6_only':ad6,'stats':stats}

def main():
    p=argparse.ArgumentParser()
    p.add_argument('certificate')
    p.add_argument('--write',action='store_true')
    a=p.parse_args()
    obj=build()
    raw=(json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=False)+'\n').encode('utf8')
    if a.write:
        with open(a.certificate,'wb') as f:f.write(raw)
    else:
        with open(a.certificate,'rb') as f:assert f.read()==raw, 'certificate mismatch'
    print('CYCLE_ENUMERATION_PASS states=272 squares=24 hexagons=128 edges4=768 edges6=1216')
    print('SHARP_THRESHOLD_PASS four_components=264+8_singletons six_components=272 radius=diameter=4')
    print('COMPLETE_PAIR_DISTANCE_PASS d1=1984 d2=10784 d3=19568 d4=4520')
if __name__=='__main__':main()
