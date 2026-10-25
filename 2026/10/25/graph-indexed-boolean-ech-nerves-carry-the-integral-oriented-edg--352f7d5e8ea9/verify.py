#!/usr/bin/env python3
"""Independent finite tests for graph-indexed radius-one intrinsic Cech nerves.
Scientific definitions are included directly below. Python 3 standard library only.
"""
from itertools import combinations, permutations
from random import Random


def vertices(n, edges):
    return [0] + [1 << i for i in range(n)] + [((1 << i) | (1 << j)) for i,j in sorted(edges)]


def faces_of_ball(vset, witness):
    ball = [v for v in vset if (v ^ witness).bit_count() <= 1]
    return set(frozenset(c) for k in range(1, len(ball)+1) for c in combinations(ball,k))


def nerve_and_cone(n, edges):
    vs = vertices(n, edges)
    all_faces, base_faces = set(), set()
    for w in vs:
        new = faces_of_ball(vs, w)
        all_faces.update(new)
        if w == 0 or w.bit_count() == 1:
            base_faces.update(new)
    return all_faces, base_faces


def gf2_rank(columns):
    pivots = {}
    for x in columns:
        while x:
            p = x.bit_length()-1
            if p in pivots:
                x ^= pivots[p]
            else:
                pivots[p]=x
                break
    return len(pivots)


def bettis_mod2(faces):
    by_degree = {}
    for f in faces:
        by_degree.setdefault(len(f)-1, []).append(tuple(sorted(f)))
    ranks={}
    for d in sorted(by_degree):
        if d == 0: ranks[d]=0;continue
        rows={f:i for i,f in enumerate(by_degree[d-1])}
        columns=[]
        for f in by_degree[d]:
            mask=0
            for face in combinations(f,len(f)-1):mask ^= 1<<rows[face]
            columns.append(mask)
        ranks[d]=gf2_rank(columns)
    betti={d:len(by_degree[d])-ranks[d]-ranks.get(d+1,0) for d in by_degree}
    betti[0] -= 1
    return {d:b for d,b in betti.items() if b}


def permute_mask(mask, p):
    out=0
    for i,j in enumerate(p):
        if mask>>i&1:out|=1<<j
    return out


def signed_trace(faces,p):
    trace=0
    for f in faces:
        new=[permute_mask(v,p) for v in sorted(f)]
        if set(new)!=f:continue
        inversions=sum(new[i]>new[j] for i in range(len(new)) for j in range(i+1,len(new)))
        trace+=(-1)**(len(f)-1+inversions)
    return trace


def module_trace(edges,p):
    out=0
    for i,j in edges:
        if {p[i],p[j]} == {i,j}:
            out += 1 if (p[i],p[j])==(i,j) else -1
    return out


def run():
    rng=Random(260932786)
    cases=0; face_checks=0; homology_checks=0; action_checks=0
    for n in range(1,7):
        pairs=list(combinations(range(n),2))
        if n<=4: graphs=[tuple(e for k,e in enumerate(pairs) if mask>>k&1) for mask in range(1<<len(pairs))]
        else:
            graphs=[tuple(pairs),(),tuple((i,i+1) for i in range(n-1))]
            graphs += [tuple(e for e in pairs if rng.getrandbits(1)) for _ in range(20)]
        for E in graphs:
            cases+=1
            F,B=nerve_and_cone(n,E)
            assert all(frozenset(f|{0}) in B for f in B),('not cone',n,E)
            expected={frozenset(((1<<i),(1<<j),(1<<i)|(1<<j))) for i,j in E}
            assert F-B == expected,('relative faces mismatch',n,E, F-B,expected)
            face_checks+=1
            if n<=5 or (n==6 and len(E)<=8):
                assert bettis_mod2(F)==({2:len(E)} if E else {}),(n,E,bettis_mod2(F))
                homology_checks+=1
            if n<=4:
                for p in permutations(range(n)):
                    transformed={tuple(sorted((p[i],p[j]))) for i,j in E}
                    if transformed!=set(E):continue
                    action_checks+=1
                    assert signed_trace(F,p)==1+module_trace(E,p),(n,E,p,signed_trace(F,p),module_trace(E,p))
    print('PASS: graph instances',cases)
    print('PASS: cone and exact relative faces',face_checks)
    print('PASS: independent exact mod-2 reduced homology',homology_checks)
    print('PASS: signed simplicial Lefschetz vs oriented-edge character',action_checks)
if __name__=='__main__':run()
