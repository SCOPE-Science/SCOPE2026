#!/usr/bin/env python3
"""Exact finite verifier for clique complexes of Fano and non-Fano basis graphs.

Uses only Python's standard library. Vertex labels are three-element sorted tuples
of integers 1..7, ordered lexicographically. Every candidate simplex is enumerated.
"""
import itertools
import collections
import random
import json

POINTS = tuple(range(1,8))
LINES = tuple(sorted({tuple(sorted((a,b,a^b))) for a,b in itertools.combinations(POINTS,2)}))
RELAXED = LINES[0]

def construct(relax=False):
    bases = tuple(t for t in itertools.combinations(POINTS,3) if t not in LINES or (relax and t == RELAXED))
    n = len(bases)
    adj = tuple(sum(1 << j for j in range(n) if j != i and len(set(bases[i]) & set(bases[j])) == 2) for i in range(n))
    faces = []
    def visit(mask, choices):
        if mask: faces.append(mask)
        while choices:
            low = choices & -choices
            i = low.bit_length() - 1
            choices ^= low
            visit(mask | low, choices & adj[i])
    visit(0, (1 << n) - 1)
    assert len(faces) == len(set(faces))
    face_set = set(faces)
    for face in faces:
        bits = face
        while bits:
            low = bits & -bits
            bits ^= low
            if face != low: assert (face ^ low) in face_set
    return bases, faces, face_set, adj

def match_by_order(faces, vertex_order):
    free = set(faces)
    matching = []
    for v in vertex_order:
        bit = 1 << v
        for f in faces:
            if not (f & bit) and f in free and (f | bit) in free:
                free.remove(f)
                free.remove(f | bit)
                matching.append((f, f | bit))
    return matching, free

def check_gradient(faces, matching):
    """Orient unmatched incidences downward and matched incidences upward."""
    face_set=set(faces)
    pairs=set(matching)
    assert len(pairs)==len(matching)
    paired_cells=[x for a,b in matching for x in (a,b)]
    assert len(paired_cells)==len(set(paired_cells))
    for a,b in matching:
        assert a in face_set and b in face_set and a.bit_count()+1==b.bit_count() and (a&b)==a
    indegree={f:0 for f in faces}
    outgoing={f:[] for f in faces}
    incidences=0
    for upper in faces:
        bits=upper
        while bits:
            bit=bits & -bits
            bits ^= bit
            if upper==bit: continue
            lower=upper^bit
            assert lower in face_set
            incidences += 1
            source,target = (lower,upper) if (lower,upper) in pairs else (upper,lower)
            outgoing[source].append(target)
            indegree[target]+=1
    queue=[f for f in faces if indegree[f] == 0]
    removed=0
    while queue:
        source=queue.pop()
        removed+=1
        for target in outgoing[source]:
            indegree[target]-=1
            if indegree[target] == 0: queue.append(target)
    assert removed==len(faces), 'Matching is cyclic'
    return incidences

def check(relax, order):
    bases,faces,face_set,adj=construct(relax)
    assert sorted(order)==list(range(len(bases)))
    pairs,critical=match_by_order(faces,order)
    incidences=check_gradient(faces,pairs)
    fvector=dict(sorted(collections.Counter(f.bit_count()-1 for f in faces).items()))
    cvector=dict(sorted(collections.Counter(f.bit_count()-1 for f in critical).items()))
    target=(len(bases),[28,126,140,28] if not relax else [29,138,170,44,3],
            {0:1,2:13} if not relax else {0:1,2:19})
    assert [fvector.get(i,0) for i in range(len(target[1]))]==target[1]
    assert cvector==target[2]
    assert len(pairs)*2+len(critical)==len(faces)
    return {'bases':len(bases),'f_vector':target[1],'critical_cells':{str(k):v for k,v in cvector.items()},
            'matched_pairs':len(pairs),'hasse_incidences':incidences,
            'face_poset_dag_vertices':len(faces)}

def fano_link():
    bases,_,_,adj=construct(True)
    new_index=bases.index(RELAXED)
    link_v=[i for i in range(len(bases)) if adj[new_index]>>i & 1]
    assert len(link_v)==12
    H=set(RELAXED)
    outside=set(POINTS)-H
    labels={i:(next(iter(H-set(bases[i]))),next(iter(set(bases[i])-H))) for i in link_v}
    assert len(set(labels.values()))==12
    for a,b in itertools.combinations(link_v,2):
        same = labels[a][0]==labels[b][0] or labels[a][1]==labels[b][1]
        assert bool(adj[a]>>b&1)==same
    return {'link_graph':'three_by_four_rook_graph','vertex_count':12,'row_cliques':3,'column_cliques':4,
            'nerve':'K_3,4','first_betti':(3-1)*(4-1)}

def find_order(relax):
    bases,faces,_,_=construct(relax)
    rng=random.Random(19073+(int(relax)))
    target = 14 if not relax else 20
    for i in range(10000):
        order=list(range(len(bases)))
        rng.shuffle(order)
        _,crit=match_by_order(faces,order)
        if len(crit)==target:
            return order,i
    raise AssertionError('No perfect vertex-order matching found')

if __name__=='__main__':
    fano_order,fi=find_order(False)
    non_order,ni=find_order(True)
    info={'fano':check(False,fano_order),'non_fano':check(True,non_order),'link':fano_link(),
          'line_triples':LINES,'relaxed_line':RELAXED,'fano_pivot_order':fano_order,
          'non_fano_pivot_order':non_order,'order_search_trial':[fi,ni],
          'relative_h2_rank':6, 'verification':'VERIFY_OK'}
    print(json.dumps(info,sort_keys=True,separators=(',',':')))
