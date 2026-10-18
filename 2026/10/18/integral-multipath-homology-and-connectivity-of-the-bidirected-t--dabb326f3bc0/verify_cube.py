#!/usr/bin/env python3
"""Reproduce the integral homology and connectivity computation for the fully bidirected cube multipath complex.

Python 3 standard library only. No external files or mathematical software required.
"""
from collections import Counter, deque
from functools import lru_cache
from hashlib import sha256
from itertools import product

VERTICES = range(8)
ARCS = tuple((a, b) for a in VERTICES for b in VERTICES if (a ^ b) in (1, 2, 4))
assert len(ARCS) == 24
ARC_INDEX = {e: i for i, e in enumerate(ARCS)}
OUTS = {a: tuple(b for x, b in ARCS if x == a) for a in VERTICES}
ORDER = (1, 5, 16, 10, 14, 15, 12, 0, 4, 2, 22, 11, 19, 18, 8, 21, 3, 17, 13, 7, 20, 23, 6, 9)
EXPECTED_COUNTS = (1, 24, 216, 928, 2016, 2160, 1008, 144)
EXPECTED_CRITICAL = (6, 45, 36, 12)  # dimensions 3,4,5,6


def directed_cycle(out):
    for v in VERTICES:
        u = v
        seen = set()
        while u != -1:
            if u in seen:
                return True
            seen.add(u)
            u = out[u]
    return False


def enumerate_by_choices():
    faces = set()
    for cs in product(range(4), repeat=8):
        out = [-1 if c == 0 else OUTS[v][c-1] for v, c in enumerate(cs)]
        destinations = [b for b in out if b != -1]
        if len(set(destinations)) != len(destinations) or directed_cycle(out):
            continue
        faces.add(sum(1 << ARC_INDEX[(a,b)] for a,b in enumerate(out) if b != -1))
    return faces


def enumerate_by_dfs():
    faces = set()
    out = [-1] * 8
    used_in = [False] * 8
    def walk(v, mask):
        if v == 8:
            faces.add(mask)
            return
        walk(v+1,mask)
        for w in OUTS[v]:
            if used_in[w]:
                continue
            t=w
            while t!=-1 and t!=v:
                t=out[t]
            if t==v:  # the proposed arc closes an oriented cycle
                continue
            out[v]=w
            used_in[w]=True
            walk(v+1,mask|(1<<ARC_INDEX[(v,w)]))
            out[v]=-1
            used_in[w]=False
    walk(0,0)
    return faces


def augmented_boundary(face):
    # Entries (codimension-one face, integer coefficient), with increasing arc-index orientation.
    bits = [j for j in range(24) if face & (1 << j)]
    return tuple((face ^ (1 << j), -1 if t & 1 else 1) for t,j in enumerate(bits))


def matching(faces):
    remaining=set(faces)
    pairs={}
    for j in ORDER:
        bit=1<<j
        lowers=[f for f in remaining if f & bit==0 and (f | bit) in remaining]
        for lower in lowers:
            assert lower in remaining and lower | bit in remaining
            upper=lower|bit
            remaining.remove(lower)
            remaining.remove(upper)
            pairs[lower]=upper
    assert len(set(pairs.values())) == len(pairs)
    assert not set(pairs).intersection(pairs.values())
    assert len(faces) == 2*len(pairs)+len(remaining)
    return pairs, remaining


def check_acyclic(faces, pairs):
    # Each Hasse covering incidence is directed from large to small, except matched arrows reversed.
    indegree={f:0 for f in faces}
    graph={f:[] for f in faces}
    number_incidence=0
    for f in faces:
        for g, _ in augmented_boundary(f):
            number_incidence+=1
            if pairs.get(g)==f:
                graph[g].append(f)
                indegree[f]+=1
            else:
                graph[f].append(g)
                indegree[g]+=1
    q=deque(f for f in faces if indegree[f]==0)
    visited=0
    while q:
        f=q.popleft()
        visited+=1
        for g in graph[f]:
            indegree[g]-=1
            if indegree[g]==0:
                q.append(g)
    assert number_incidence == 29160
    assert visited == len(faces), 'Directed cycle detected in matched Hasse diagram'
    return number_incidence


def check_integral_morse_zero(pairs, critical):
    uppers=set(pairs.values())
    critical=set(critical)
    assert not (set(pairs)&uppers or set(pairs)&critical or uppers&critical)
    @lru_cache(maxsize=None)
    def proj(f):
        if f in critical:
            return {f:1}
        if f in uppers:
            return {}
        up=pairs[f]
        e=dict(augmented_boundary(up))[f]
        assert e in (-1,1)
        acc=Counter()
        for x,c in augmented_boundary(up):
            if x==f:
                continue
            for y,n in proj(x).items():
                acc[y]-=e*c*n
        return {y:n for y,n in acc.items() if n}
    coefficients_checked=0
    for upper in critical:
        total=Counter()
        for lower,sgn in augmented_boundary(upper):
            for cell,coef in proj(lower).items():
                assert cell.bit_count()==lower.bit_count()
                total[cell]+=sgn*coef
                coefficients_checked+=1
        assert not {c:v for c,v in total.items() if v}, ('nonzero Morse differential',upper,total)
    return coefficients_checked


def direct_f2_betti(faces):
    by={d:sorted(f for f in faces if f.bit_count()-1==d) for d in range(-1,7)}
    ranks=[]
    for d in range(0,7):
        lower=by[d-1]
        pivots={}
        ix={f:i for i,f in enumerate(lower)}
        for upper in by[d]:
            column=0
            for f,_ in augmented_boundary(upper):
                column ^= 1<<ix[f]
            while column:
                p=column.bit_length()-1
                if p not in pivots:
                    pivots[p]=column
                    break
                column^=pivots[p]
        ranks.append(len(pivots))
    assert ranks == [1,23,193,735,1275,840,132],ranks
    for d in range(0,7):
        next_rank=ranks[d+1] if d+1<len(ranks) else 0
        actual=len(by[d])-ranks[d]-next_rank
        expected={3:6,4:45,5:36,6:12}.get(d,0)
        assert actual==expected,(d,actual,expected)
    return ranks


def main():
    faces=enumerate_by_choices()
    independent_faces=enumerate_by_dfs()
    assert faces==independent_faces
    counts=tuple(sum(f.bit_count()==k for f in faces) for k in range(8))
    assert counts==EXPECTED_COUNTS,(counts,EXPECTED_COUNTS)
    assert all((f & (f-1)) in faces for f in faces if f) # one vertex deletion, strongest bit
    pairs, critical=matching(faces)
    assert len(pairs)==3199 and len(critical)==99
    critical_counts=tuple(sum(f.bit_count()==k+1 for f in critical) for k in range(3,7))
    assert critical_counts==EXPECTED_CRITICAL,critical_counts
    assert not any(f.bit_count()<=3 for f in critical)
    incidences=check_acyclic(faces,pairs)
    nontrivial_terms=check_integral_morse_zero(pairs,critical)
    ranks=direct_f2_betti(faces)
    digest=sha256(b''.join(f.to_bytes(3,'little') for f in sorted(faces))).hexdigest()
    print('FACES',len(faces),'FVECTOR',counts,'FACE_SHA256',digest)
    print('MATCHED_PAIRS',len(pairs),'HASSE_INCIDENCES',incidences)
    print('CRITICAL_DIM_3_TO_6',critical_counts,'SIGNED_MORSE_DIFFERENTIAL_ZERO',True)
    print('DIRECT_MOD2_BOUNDARY_RANKS_0_TO_6',ranks,'MORSE_REDUCTION_TERMS',nontrivial_terms)
    print('INTEGRAL_REDUCED_BETTI_3_TO_6',critical_counts,'INTEGRAL_TORSION_FREE',True)
    print('HOMOTOPY_2_CONNECTED',True)
    print('VERIFIED_Q3_BIDIRECTED_MULTIPATH_INTEGRAL_HOMOLOGY')


if __name__=='__main__':
    main()
