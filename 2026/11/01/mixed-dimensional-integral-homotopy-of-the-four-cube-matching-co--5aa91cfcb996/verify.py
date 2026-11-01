#!/usr/bin/env python3
"""Exact matching-complex calculation for the 4-dimensional cube.
Requires Python 3 and SymPy. No external data files.
"""
from collections import Counter, deque
from functools import lru_cache
from sympy import SparseMatrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

VERTICES = tuple(range(16))
EDGES = tuple((u, u ^ (1 << k)) for u in VERTICES for k in range(4) if u < (u ^ (1 << k)))
assert len(EDGES) == 32
EDGE_MASK = tuple((1 << u) | (1 << v) for u,v in EDGES)

def all_faces():
    fs = {0}
    def go(i, used, chosen):
        if i == len(EDGES):
            fs.add(chosen)
            return
        go(i+1,used,chosen)
        if used & EDGE_MASK[i] == 0:
            go(i+1,used | EDGE_MASK[i],chosen | (1 << i))
    go(0,0,0)
    return fs

def match(fs, edge_order):
    unmatched = set(fs)
    forward = {}
    for index in edge_order:
        bit = 1 << index
        for face in tuple(unmatched):
            if face & bit == 0 and face | bit in unmatched:
                unmatched.remove(face)
                unmatched.remove(face|bit)
                forward[face] = face|bit
    assert len(unmatched) + 2*len(forward) == len(fs)
    return forward,unmatched

def directed_acyclic(fs, matched):
    indegree = {s:0 for s in fs}
    outgoing = {s:[] for s in fs}
    for upper in fs:
        bits = upper
        while bits:
            bit = bits & -bits
            bits ^= bit
            lower = upper ^ bit
            if lower not in fs: continue
            if matched.get(lower) == upper:
                outgoing[lower].append(upper)
                indegree[upper] += 1
            else:
                outgoing[upper].append(lower)
                indegree[lower] += 1
    queue = deque(s for s in fs if indegree[s] == 0)
    processed = 0
    while queue:
        s = queue.popleft(); processed += 1
        for t in outgoing[s]:
            indegree[t] -= 1
            if indegree[t] == 0:
                queue.append(t)
    return processed == len(fs),processed,sum(map(len,outgoing.values()))

def morse_five_to_four(critical,matched):
    low = sorted(f for f in critical if f.bit_count() == 5)
    high = sorted(f for f in critical if f.bit_count() == 6)
    index = {face:i for i,face in enumerate(low)}
    paired_up = {a:b for a,b in matched.items() if a.bit_count()==5}
    upper_from_three = {b for a,b in matched.items() if a.bit_count()==4}
    @lru_cache(maxsize=None)
    def reduction(face):
        if face in index: return {index[face]:1}
        if face in upper_from_three: return {}
        assert face in paired_up
        big = paired_up[face]
        vs = [j for j in range(32) if big & (1<<j)]
        pivot = next(i for i,j in enumerate(vs) if face & (1<<j) == 0)
        ans = {}
        for i,j in enumerate(vs):
            if i==pivot: continue
            sign = -(-1 if (i+pivot)%2 else 1)
            for row, value in reduction(big^(1<<j)).items():
                ans[row] = ans.get(row,0)+ sign*value
        return {row:value for row,value in ans.items() if value}
    entries = {}
    for col,face in enumerate(high):
        ans = {}
        vs = [j for j in range(32) if face & (1<<j)]
        for i,j in enumerate(vs):
            for row,value in reduction(face^(1<<j)).items():
                ans[row] = ans.get(row,0) + (-1 if i%2 else 1)*value
        for row,value in ans.items():
            if value: entries[(row,col)] = value
    matrix = SparseMatrix(len(low),len(high),entries)
    return low,high,matrix

faces = all_faces()
vec = Counter(f.bit_count() for f in faces)
assert tuple(vec[i] for i in range(9)) == (1,32,400,2496,8256,14208,11648,3712,272)
print('faces_by_cardinality:',[vec[i] for i in range(9)])
print('total_faces_including_empty:',len(faces))
print('reduced_euler:',sum((-1 if i % 2 == 0 else 1)*vec[i] for i in range(9)))

for tag,order in [('forward',range(32)),('reverse',range(31,-1,-1))]:
    matched,critical=match(faces,order)
    # Standard (unaugmented) Forman matching: leave the former pair's vertex critical.
    base_vertex = matched.pop(0)
    critical.add(base_vertex)
    acyclic,processed,arcs=directed_acyclic(faces-{0},matched)
    print(tag,'pairs:',len(matched),'critical_dims:',dict(sorted(Counter(f.bit_count()-1 for f in critical).items())))
    print(tag,'oriented_hasse_edges:',arcs,'acyclic:',acyclic,'processed:',processed)
    assert acyclic and processed==len(faces)-1
    assert all(f.bit_count() in (1,5,6) for f in critical)
    low,high,matrix=morse_five_to_four(critical,matched)
    assert matrix.shape == ((39,168) if tag=='forward' else (12,141))
    diag=smith_normal_form(matrix,domain=ZZ)
    invariants=Counter(abs(int(diag[i,i])) for i in range(min(diag.shape)) if diag[i,i] != 0)
    print(tag,'morse_boundary_shape:',matrix.shape,'nonzero_entries:',len(matrix.todok()),'smith:',dict(invariants))
    assert invariants == ({1:38} if tag=='forward' else {1:11})
    print(tag,'homology_ranks:{4:1,5:130} torsion:none')
print('ALL_CHECKS_PASS')
