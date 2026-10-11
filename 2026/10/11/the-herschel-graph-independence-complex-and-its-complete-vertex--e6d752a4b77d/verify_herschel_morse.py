#!/usr/bin/env python3
"""Standalone exhaustive discrete-Morse verification for Herschel independence complexes."""
from collections import Counter, deque
from itertools import combinations

N = 11
EDGE_SET = {
    (0,5),(0,6),(0,9),(0,10),
    (1,5),(1,6),(1,7),(1,8),
    (2,7),(2,8),(2,9),(2,10),
    (3,5),(3,7),(3,9),
    (4,6),(4,8),(4,10),
}
EDGES = tuple(sorted(tuple(sorted(e)) for e in EDGE_SET))
ALL = (1 << N) - 1
SPECIAL_ORDER = (8,9,1,2,5,3,7,4,0,10,6)


def face_set(allowed):
    return {mask for mask in range(1,1 << N) if mask & ~allowed == 0
            and all(not ((mask & (1<<u)) and (mask & (1<<v))) for u,v in EDGES)}


def greedy_matching(F, order):
    avail = set(F)
    pairs = []
    for v in order:
        bit = 1 << v
        for mask in sorted(avail):
            larger = mask | bit
            if larger != mask and larger in avail:
                avail.remove(mask)
                avail.remove(larger)
                pairs.append((mask,larger))
    return pairs,avail


def certify(F,pairs):
    seen = set()
    up = {}
    for small,large in pairs:
        assert small in F and large in F and small != 0
        assert large.bit_count() == small.bit_count()+1
        assert small & large == small
        assert small not in seen and large not in seen
        seen.add(small);seen.add(large)
        up[small] = large
    directed = {f:[] for f in F}
    indeg = {f:0 for f in F}
    incidences = 0
    for high in F:
        for bit in range(N):
            if high & (1<<bit):
                low = high ^ (1<<bit)
                if low == 0:
                    continue
                assert low in F
                a,b = (low,high) if up.get(low)==high else (high,low)
                directed[a].append(b)
                indeg[b]+=1
                incidences+=1
    queue=deque(sorted(x for x in F if indeg[x]==0))
    count=0
    while queue:
        x=queue.popleft(); count+=1
        for y in directed[x]:
            indeg[y]-=1
            if indeg[y]==0:queue.append(y)
    assert count == len(F), ('cyclic',count,len(F))
    return incidences


def collapse_certificate(F):
    remain = set(F)
    steps=[]
    while len(remain)>1:
        chosen=None
        for lo in sorted(remain,key=lambda m:(-m.bit_count(),m)):
            all_cofaces=[z for z in remain if z != lo and z & lo == lo]
            if len(all_cofaces)==1 and all_cofaces[0].bit_count()==lo.bit_count()+1:
                chosen = (lo,all_cofaces[0]);break
        assert chosen is not None, ('no free face',len(remain))
        remain.difference_update(chosen)
        steps.append(chosen)
    assert len(remain)==1 and next(iter(remain)).bit_count()==1
    return len(steps)


def expected(kind,vertex=None):
    if kind=='all':return {0:1,2:2}
    if kind=='deletion':return {0:1} if vertex in (3,4) else {0:1,2:1}
    if kind=='link':return {0:1,1:2} if vertex in (3,4) else {0:1,1:1}
    raise ValueError(kind)


def execute():
    assert len(EDGES)==18
    degrees=Counter(v for uv in EDGES for v in uv)
    assert sorted(degrees.values())==[3]*8+[4]*3
    assert all(((u<5) != (v<5)) for u,v in EDGES)
    tot_faces=tot_inc=tot_pairs=0
    summary=[]
    for kind,vertex in [('all',None)]+[('deletion',v) for v in range(N)]+[('link',v) for v in range(N)]:
        if kind=='all':allowed=ALL
        elif kind=='deletion':allowed=ALL^(1<<vertex)
        else:
            neighbors={w for a,b in EDGES for w in ([b] if a==vertex else ([a] if b==vertex else []))}
            allowed=ALL^(1<<vertex)
            for w in neighbors:allowed^=1<<w
        F=face_set(allowed)
        order=SPECIAL_ORDER if kind=='deletion' and vertex==2 else tuple(range(N))
        pairs,crit=greedy_matching(F,order)
        incidence=certify(F,pairs)
        hist=dict(Counter(m.bit_count()-1 for m in crit))
        assert hist == expected(kind,vertex),(kind,vertex,hist)
        assert 2*len(pairs)+len(crit)==len(F)
        if kind=='deletion' and vertex in (3,4):
            assert collapse_certificate(F)==48
        if kind=='all':
            assert dict(Counter(m.bit_count()-1 for m in F))=={0:11,1:37,2:45,3:22,4:7,5:1}
            assert len(F)==123 and incidence==338 and len(pairs)==60
        tot_faces+=len(F);tot_inc+=incidence;tot_pairs+=len(pairs)
        summary.append((kind,vertex,len(F),incidence,len(pairs),hist))
    assert len(summary)==23
    print('HERSCHEL_MORSE_OK',len(summary),'faces',tot_faces,'incidences',tot_inc,'pairs',tot_pairs)
    for rec in summary:print(*rec)

if __name__=='__main__':execute()
