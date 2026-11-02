#!/usr/bin/env python3
"""Independent perfect-matching and all-pairs symmetric-difference verifier.

Usage: python3 verify_bipartite.py certificate.json
No imported project modules; only Python standard library.
"""
import collections
import json
import sys

def make_states():
    even=sorted(v for v in range(16) if v.bit_count()%2==0)
    odd=sorted(v for v in range(16) if v.bit_count()%2==1)
    options=[[v for v in odd if (v^u).bit_count()==1] for u in even]
    output=[]
    def step(k,chosen,used):
        if k==len(even):
            state=tuple(sorted((min(a,b),max(a,b)) for a,b in zip(even,chosen)))
            output.append(state)
            return
        for v in options[k]:
            if v not in used:step(k+1, chosen+[v],used|{v})
    step(0,[],set())
    return sorted(output)

def one_cycle(edges):
    # The difference of two 1-factors is 2-regular; ensure it is ONE cycle.
    graph=collections.defaultdict(set)
    for a,b in edges:
        graph[a].add(b); graph[b].add(a)
    if any(len(xs)!=2 for xs in graph.values()):return False
    visited=set(); todo=[next(iter(graph))]
    while todo:
        v=todo.pop()
        if v in visited:continue
        visited.add(v); todo.extend(graph[v]-visited)
    return len(visited)==len(graph)==len(edges)

def classify(states):
    edge_sets=[frozenset(s) for s in states]
    four=[set() for _ in states]
    six=[set() for _ in states]
    for i in range(len(states)):
        for j in range(i+1,len(states)):
            diff=edge_sets[i]^edge_sets[j]
            if len(diff) in (4,6) and one_cycle(diff):
                if len(diff)==4: four[i].add(j);four[j].add(i)
                else:six[i].add(j);six[j].add(i)
    return [list(map(sorted,x)) for x in (four,six)]

def components(ad):
    visited=set();out=[]
    for i in range(len(ad)):
        if i in visited:continue
        todo=[i];visited.add(i)
        for v in todo:
            for w in ad[v]:
                if w not in visited:visited.add(w);todo.append(w)
        out.append(len(todo))
    return sorted(out)

def bfs(ad,source):
    queue=collections.deque([source]);dst={source:0}
    while queue:
        v=queue.popleft()
        for w in ad[v]:
            if w not in dst:dst[w]=dst[v]+1;queue.append(w)
    return dst

def main(path):
    with open(path,encoding='utf8') as f:obj=json.load(f)
    states=make_states()
    assert len(states)==272
    assert obj['states']==[[list(e) for e in s] for s in states]
    a4,a6=classify(states)
    assert a4==obj['neighbors_4'] and a6==obj['neighbors_6_only']
    assert sum(map(len,a4))==1536 and sum(map(len,a6))==2432
    assert components(a4)==[1]*8+[264]
    a46=[sorted(set(x)|set(y)) for x,y in zip(a4,a6)]
    assert components(a46)==[272]
    e=[]; pair_counts=collections.Counter()
    for i in range(272):
        dis=bfs(a46,i)
        assert len(dis)==272
        e.append(max(dis.values()))
        for j in range(i+1,272):pair_counts[dis[j]]+=1
    assert set(e)=={4} and len(e)==272
    assert dict(sorted(pair_counts.items()))=={1:1984,2:10784,3:19568,4:4520}
    frozen=[i for i in range(272) if len(a4[i])==0]
    assert len(frozen)==8 and all(len(a6[i])==8 for i in frozen)
    print('BIPARTITE_ALL_PAIRS_PASS states=272 four_components=264+8_singletons')
    print('INDEPENDENT_SIX_CYCLE_GEOMETRY_PASS radius=4 diameter=4 edges=1984')
    print('INDEPENDENT_DISTANCE_PROFILE_PASS 1984 10784 19568 4520')
if __name__=='__main__':
    assert len(sys.argv)==2
    main(sys.argv[1])
