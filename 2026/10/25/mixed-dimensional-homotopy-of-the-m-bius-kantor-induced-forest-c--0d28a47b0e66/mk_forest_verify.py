#!/usr/bin/env python3
"""Exact, self-contained certificate for the induced-forest complex of GP(8,3).

Requires only Python 3.9+ standard library. All faces and incidences are enumerated;
no randomized heuristic, numerical tolerance, external package, or stored certificate
is used. The stated homotopy conclusion also uses the standard cellular form
of discrete Morse theory.
"""
import collections
import functools
import hashlib
import json
from collections import deque

N = 16
EDGES = tuple(sorted({tuple(sorted(edge)) for i in range(8) for edge in
                      ((i,(i+1)%8), (i,8+i), (8+i,8+(i+3)%8))}))
assert len(EDGES) == 24
ADJ = [0] * N
for u,v in EDGES:
    ADJ[u] |= 1<<v
    ADJ[v] |= 1<<u


def forest_independent(mask):
    """Cycle test via disjoint sets and all induced edges."""
    parent = list(range(N))
    def root(v):
        while v != parent[v]:
            v = parent[v]
        return v
    for u,v in EDGES:
        if mask & (1<<u) and mask & (1<<v):
            ru,rv = root(u),root(v)
            if ru == rv:
                return False
            parent[ru] = rv
    return True


def forest_incremental():
    """Different test: attach the least vertex to an already-acyclic graph."""
    face = bytearray(1<<N)
    face[0] = 1
    for mask in range(1,1<<N):
        low_bit = mask & -mask
        v = low_bit.bit_length()-1
        smaller = mask ^ low_bit
        if not face[smaller]:
            continue
        neighbors = ADJ[v] & smaller
        if neighbors.bit_count() < 2:
            face[mask] = 1
            continue
        remainder = smaller
        still_forest = True
        while remainder:
            component = remainder & -remainder
            boundary = component
            while boundary:
                bit = boundary & -boundary
                boundary ^= bit
                w = bit.bit_length()-1
                nxt = ADJ[w] & smaller & ~component
                boundary |= nxt
                component |= nxt
            if (component & neighbors).bit_count() >= 2:
                still_forest = False
                break
            remainder &= ~component
        face[mask] = still_forest
    return face


def boundary(face_mask):
    """(codimension-one face, signed coefficient) in sorted-vertex orientation."""
    position=0
    pending=face_mask
    while pending:
        bit=pending & -pending
        yield face_mask ^ bit, (-1 if position & 1 else 1)
        pending ^= bit
        position += 1


def greedy_toggle(face):
    active = {s for s, present in enumerate(face) if present}
    pair = {}
    pivot_counts=[]
    while True:
        choice=None
        lower_faces=None
        for v in range(N):
            vb=1<<v
            candidates=[s for s in active if not(s&vb) and (s|vb) in active]
            if candidates and (choice is None or len(candidates)>len(lower_faces)):
                choice=v
                lower_faces=candidates
        if choice is None:
            break
        for s in lower_faces:
            upper=s | (1<<choice)
            pair[s]=upper
            active.remove(s)
            active.remove(upper)
        pivot_counts.append((choice,len(lower_faces)))
    return pair, tuple(sorted(active)),pivot_counts


def check_acyclic(face,pair):
    """Verify the entire directed Hasse graph by Kahn's algorithm."""
    adjacent=[[] for _ in range(1<<N)]
    indegree=[0]*(1<<N)
    incidences=0
    for upper,valid in enumerate(face):
        if not valid: continue
        for lower,_ in boundary(upper):
            incidences+=1
            if pair.get(lower)==upper:
                frm,to=lower,upper
            else:
                frm,to=upper,lower
            adjacent[frm].append(to)
            indegree[to]+=1
    queue=deque(s for s,valid in enumerate(face) if valid and indegree[s]==0)
    seen=0
    while queue:
        current=queue.popleft()
        seen+=1
        for nxt in adjacent[current]:
            indegree[nxt]-=1
            if indegree[nxt]==0:
                queue.append(nxt)
    assert seen==sum(face), (seen,sum(face))
    return incidences,seen


def morse_boundary(pair,critical):
    """Exact gradient-path elimination of signed simplicial boundaries."""
    critical_set=set(critical)
    upper_set=set(pair.values())
    @functools.lru_cache(maxsize=None)
    def projection(lower):
        if lower in critical_set:
            return {lower:1}
        if lower in upper_set:
            return {}
        upper=pair[lower]
        pivot=next(c for f,c in boundary(upper) if f==lower)
        tally=collections.defaultdict(int)
        for f,c in boundary(upper):
            if f==lower: continue
            for x,k in projection(f).items():
                tally[x]-=pivot*c*k
        return {x:k for x,k in tally.items() if k}
    cells=collections.defaultdict(list)
    for m in critical:
        cells[m.bit_count()-1].append(m)
    matrices={}
    for dimension in (9,10):
        domain=cells[dimension]
        codomain=cells[dimension-1]
        matrix=[]
        for upper in domain:
            tally=collections.defaultdict(int)
            for lower,c in boundary(upper):
                for x,k in projection(lower).items():
                    tally[x]+=c*k
            assert all(x in codomain for x in tally)
            matrix.append([tally.get(x,0) for x in codomain])
        matrices[dimension]=matrix
    return cells,matrices,projection.cache_info()


def main():
    face=forest_incremental()
    assert all(bool(face[s])==forest_independent(s) for s in range(1<<N))
    vector=collections.Counter(s.bit_count()-1 for s,v in enumerate(face) if v)
    expected=[1,16,120,560,1820,4368,7984,11200,11792,8672,3792,672]
    assert [vector[i] for i in range(-1,11)]==expected
    assert sum((-1)**k*value for k,value in vector.items())==-21
    pair,critical,pivots=greedy_toggle(face)
    assert len(pair)==25483
    assert [(v,c) for v,c in pivots]==[
        (0,23441),(4,1515),(10,221),(14,188),(1,36),(6,31),(13,18),
        (12,15),(11,8),(2,4),(7,3),(3,1),(9,1),(15,1)]
    assert collections.Counter(s.bit_count()-1 for s in critical)=={8:1,9:26,10:4}
    incidences,visited=check_acyclic(face,pair)
    cells,mats,cache=morse_boundary(pair,critical)
    assert len(mats[9])==26 and all(len(row)==1 for row in mats[9])
    assert sum(x!=0 for row in mats[9] for x in row)==7
    assert set(x for row in mats[9] for x in row)=={0,1}
    assert len(mats[10])==4 and all(len(row)==26 for row in mats[10])
    assert all(x==0 for row in mats[10] for x in row)
    result={
        'graph_vertices':N,'graph_edges':len(EDGES),
        'nonempty_faces':sum(face)-1,
        'face_vector_dim_minus1_to10':[vector[i] for i in range(-1,11)],
        'reduced_euler_characteristic':-21,
        'matching_pairs':len(pair),
        'critical_cells_by_dimension':{'8':1,'9':26,'10':4},
        'directed_hasse_incidences':incidences,
        'topologically_sorted_faces':visited,
        'stage_vertex_pair_counts':pivots,
        'morse_boundary_d9_to_d8':[row[0] for row in mats[9]],
        'morse_boundary_d10_to_d9':'zero 26x4 matrix',
        'conclusion_reduced_homology':{'degree9_free_rank':25,'degree10_free_rank':4},
        'face_set_sha256':hashlib.sha256(bytes(face)).hexdigest(),
        'matched_pairs_sha256':hashlib.sha256(json.dumps(sorted(pair.items()),separators=(',',':')).encode()).hexdigest(),
    }
    print(json.dumps(result,sort_keys=True,indent=2))
    print('VERIFY_OK')

if __name__=='__main__':
    main()
