#!/usr/bin/env python3
"""Exact enumeration and six-colour exclusion for the Tutte--Coxeter graph.

Python standard library only. Execute: python3 verify_exact.py
Vertex labels: 0..14 are lexicographically ordered edges of K6;
15..29 are perfect matchings of K6 in the canonical recursive order.
The ordered edge list of the incidence graph is grouped by edge of K6.
"""
from collections import Counter
import json
from pathlib import Path
from itertools import combinations

COLORS = (0,6,1,3,6,4,0,1,4,6,2,0,5,2,0,2,3,4,0,5,4,2,5,3,1,6,5,2,4,6,5,3,1,4,6,3,2,0,6,4,0,1,5,1,6)

def perfect_matchings(vertices):
    if not vertices:
        yield ()
        return
    a = vertices[0]
    for b in vertices[1:]:
        rest = tuple(x for x in vertices if x != a and x != b)
        for tail in perfect_matchings(rest):
            yield ((a,b),)+tail

def graph():
    duads = list(combinations(range(6),2))
    synthemes = list(perfect_matchings(tuple(range(6))))
    assert len(duads)==15 and len(synthemes)==15
    edges = [(i,15+j) for i,e in enumerate(duads) for j,s in enumerate(synthemes) if e in s]
    assert len(edges)==45
    adj = [set() for _ in range(30)]
    for u,v in edges:
        adj[u].add(v); adj[v].add(u)
    compatible = [0]*45
    for i,(a,b) in enumerate(edges):
        for j,(c,d) in enumerate(edges):
            if i!=j and not ({a,b}&{c,d}) and not any(v in adj[u] for u in (a,b) for v in (c,d)):
                compatible[i] |= 1<<j
    return edges,compatible

def enumerate_all(compatible):
    counts=Counter(); last={7:[],8:[],9:[]}
    def visit(current,possible,size):
        while possible:
            bit=possible & -possible; possible-=bit
            i=bit.bit_length()-1
            new=current|bit
            next_size=size+1
            counts[next_size]+=1
            if next_size in last:
                last[next_size].append(new)
            visit(new,possible & compatible[i],next_size)
    visit(0,(1<<45)-1,0)
    return counts,last

def can_partition_into_four_sevens(remaining,candidates):
    seven_by_edge = [[] for _ in range(45)]
    for s in candidates:
        for i in range(45):
            if s>>i&1:seven_by_edge[i].append(s)
    def search(rest,depth):
        if depth==0:return rest==0
        if rest.bit_count()!=7*depth:return False
        pivot=None; options=None
        mask=rest
        while mask:
            bit=mask&-mask;mask-=bit
            i=bit.bit_length()-1
            legal=[s for s in seven_by_edge[i] if s & rest == s]
            if not legal:return False
            if options is None or len(legal)<len(options):pivot=i;options=legal
        return any(search(rest^s,depth-1) for s in options)
    return search(remaining,4)

def verify():
    edges,compatible=graph()
    counts,last=enumerate_all(compatible)
    expected={1:45,2:720,3:5160,4:16920,5:22680,6:8520,7:720,8:90,9:10}
    assert dict(counts)==expected, (dict(counts),expected)
    maxima=sorted(last[9]); assert len(maxima)==10
    certificate=json.loads(Path(__file__).with_name('CERTIFICATE.json').read_text(encoding='utf8'))
    assert certificate['ordered_edges']==[list(e) for e in edges]
    assert certificate['strong_seven_colors']==list(COLORS)
    assert certificate['induced_matching_count_by_size']=={str(k):counts[k]for k in sorted(counts)}
    assert certificate['maximum_induced_matchings_as_edge_indices']==[
        [i for i in range(45) if m>>i&1] for m in maxima]
    assert Counter(sum(m>>i&1 for m in maxima) for i in range(45))==Counter({2:45})
    assert all((m&n).bit_count()==1 for j,m in enumerate(maxima) for n in maxima[:j])
    assert len(set(COLORS))==7 and len(COLORS)==45
    assert all(COLORS[i]!=COLORS[j] for i in range(45) for j in range(i) if not (compatible[i]>>j&1))
    assert all(any((s & m)==s for m in maxima) for s in last[8])
    # A six-class partition of the 45 edges must have sizes (9,8,7,7,7,7):
    # distinct maximum nine-sets intersect in exactly one edge, each edge lies
    # in exactly two maxima, so at most two disjoint eights (and at most one
    # alongside a nine). If there is no nine, 2*8+4*7<45. With one nine,
    # 9+8+4*7=45 is the sole remaining possibility. Each eight is the
    # other nine-set with its common edge deleted. Exhaust all 90 pairs.
    trials=0;num_candidate_sevens=Counter();full=(1<<45)-1
    for a in maxima:
        for b in maxima:
            if a==b:continue
            common=a&b
            assert common.bit_count()==1
            eight=b^common
            rest=full ^ (a|eight)
            assert rest.bit_count()==28
            cand=[s for s in last[7] if (s & rest)==s]
            num_candidate_sevens[len(cand)]+=1
            assert not can_partition_into_four_sevens(rest,cand)
            trials+=1
    assert trials==90
    print('GRAPH vertices=30 edges=45 degree=3')
    print('INDUCED_MATCHINGS_BY_SIZE',','.join('%d:%d'%(k,counts[k]) for k in sorted(counts)))
    print('MAXIMUM_SIZE 9 COUNT 10 EACH_EDGE_IN_TWO EACH_PAIR_INTERSECTION_ONE')
    print('STRONG_7_COLORING VERIFIED',','.join(map(str,COLORS)))
    print('SIX_COLOR_EXCLUSION 90 ordered_nine_eight_cases candidates='+str(dict(num_candidate_sevens))+' all_unsatisfiable')
    print('RESULT strong_chromatic_index=7')
if __name__=='__main__': verify()
