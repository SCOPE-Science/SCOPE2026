"""Independent small-case test via actual simplicial chains and face traces.

This file does not import the recurrence verification implementation.
"""
from itertools import combinations
from collections import defaultdict


def tree(b, h):
    vertices = [()]
    for _ in range(h):
        vertices += [u + (j,) for u in vertices if len(u) == _ for j in range(b)]
    ids = {p: i for i, p in enumerate(vertices)}
    edges = [(ids[p], ids[p[:-1]]) for p in vertices if p]
    return vertices, edges


def faces_by_degree(n, edges):
    masks = [(1 << u) | (1 << v) for u, v in edges]
    out = defaultdict(list)
    for s in range(1 << n):
        if all(s & mask != mask for mask in masks):
            out[s.bit_count() - 1].append(s)
    return out


def rank_f2(boundary_columns):
    piv = {}
    for x in boundary_columns:
        while x:
            k = x.bit_length() - 1
            if k not in piv:
                piv[k] = x
                break
            x ^= piv[k]
    return len(piv)


def reduced_betti(faces):
    dims = sorted(k for k in faces if k >= 0)
    ranks = {}
    for d in dims:
        prev = {face: i for i, face in enumerate(faces[d-1])}
        cols = []
        for face in faces[d]:
            x = face
            col = 0
            while x:
                vbit = x & -x
                col ^= 1 << prev[face ^ vbit]
                x -= vbit
            cols.append(col)
        ranks[d] = rank_f2(cols)
    return {d: len(faces[d]) - ranks[d] - ranks.get(d+1, 0) for d in dims}


def permutation(b, paths, prefix):
    ids = {p: i for i, p in enumerate(paths)}
    depth = len(prefix)
    def swap(p):
        if len(p) > depth and p[:depth] == prefix and p[depth] in (0, 1):
            return p[:depth] + ((1 - p[depth]),) + p[depth+1:]
        return p
    return [ids[swap(p)] for p in paths]


def trace_euler(faces, perm):
    seen = set()
    cycles = []
    for v in range(len(perm)):
        if v in seen:
            continue
        cyc=[]; w=v
        while w not in seen:
            seen.add(w);cyc.append(w);w=perm[w]
        cycles.append(sum(1 << x for x in cyc))
    z = 0
    # Alternating trace of the augmented face complex, including empty face.
    all_faces = set.union(*(set(items) for items in faces.values()))
    for choice in range(1 << len(cycles)):
        mask=0
        for i, c in enumerate(cycles):
            if (choice >> i) & 1: mask |= c
        if mask in all_faces:
            z += (-1) ** choice.bit_count()
    return z


def run():
    tests = [(2,1),(2,2),(2,3),(3,1),(3,2),(4,1)]
    count=0
    for b,h in tests:
        vertices,edges=tree(b,h)
        faces=faces_by_degree(len(vertices),edges)
        betti=reduced_betti(faces)
        P={p for p in vertices if len(p) <= h-1 and (h-1-len(p)) % 3 == 0}
        if h%3==0:
            assert not any(v for v in betti.values()),(b,h,betti)
        else:
            assert betti=={i: 1 if i == len(P)-1 else 0 for i in betti},(b,h,betti,P)
        ident=trace_euler(faces,list(range(len(vertices))))
        assert (ident==0)==(h%3==0)
        for parent in vertices:
            if len(parent)>=h:continue
            perm=permutation(b,vertices,parent)
            actual=trace_euler(faces,perm)
            if h%3==0:
                assert actual==0
            else:
                P_ordered=sorted(P)
                moved=[vertices[perm[vertices.index(x)]] for x in P_ordered]
                inversions=sum(moved[i]>moved[j] for i in range(len(moved)) for j in range(i+1,len(moved)))
                assert actual==ident*(-1 if inversions%2 else 1),(b,h,parent,actual,ident,inversions)
            count+=1
        print('tree',b,h,'vertices',len(vertices),'faces',sum(map(len,faces.values())),'betti',betti,'augmented trace',ident)
    print('independent simplicial chain and action tests:',count,'passed')

if __name__=='__main__':run()
