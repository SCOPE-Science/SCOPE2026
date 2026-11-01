#!/usr/bin/env python3
"""Exhaustive finite checks for higher independence complexes of three-hub trees.

Vertex order: 0=u, 1=v, 2=w, then a leaves at u and c leaves at w.
No library dependencies. All mod-two calculations are independent of the proof.
"""
from math import comb


def binom(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def valid_faces(n, edges, r):
    """List all faces, including empty face, by number of vertices."""
    out = {}
    for mask in range(1 << n):
        parent = {i: i for i in range(n) if (mask >> i) & 1}
        def root(i):
            while parent[i] != i:
                i = parent[i]
            return i
        for x, y in edges:
            if x in parent and y in parent:
                parent[root(x)] = root(y)
        sizes = {}
        for i in parent:
            z = root(i)
            sizes[z] = sizes.get(z, 0) + 1
        if all(v <= r for v in sizes.values()):
            out.setdefault(mask.bit_count(), []).append(mask)
    return out


def rank_mod2(columns):
    pivots = {}
    for column in columns:
        while column:
            bit = column.bit_length() - 1
            if bit in pivots:
                column ^= pivots[bit]
            else:
                pivots[bit] = column
                break
    return len(pivots)


def reduced_betti(faces):
    """Boundary ranks on augmented mod-two simplicial chains."""
    max_size = max(faces)
    ranks = {1: 1 if faces.get(1) else 0}
    for sz in range(2, max_size + 1):
        idx = {m: j for j, m in enumerate(faces[sz-1])}
        cols = []
        for mask in faces[sz]:
            x = mask
            column = 0
            while x:
                low = x & -x
                x -= low
                column ^= 1 << idx[mask ^ low]
            cols.append(column)
        ranks[sz] = rank_mod2(cols)
    ans = {}
    for sz in range(1, max_size + 1):
        k = len(faces[sz]) - ranks.get(sz, 0) - ranks.get(sz + 1, 0)
        if k:
            ans[sz-1] = k
    return ans


def tree_edges(a, c):
    return [(0,1),(1,2)] + [(0,i) for i in range(3,3+a)] + [(2,i) for i in range(3+a,3+a+c)]


def expected_betti(a,c,r):
    output = {}
    def add(d,k):
        if k:
            output[d] = output.get(d,0) + k
    add(2*r-1,binom(a-1,r-1)*binom(c-1,r-1))
    add(r-1,binom(a+c-1,r-3))
    return output


def run():
    cases = 0
    all_faces = 0
    mixed = []
    for a in range(1,5):
        for c in range(1,5):
            n = a+c+3
            edges = tree_edges(a,c)
            for r in range(1,n+1):
                faces = valid_faces(n,edges,r)
                got = reduced_betti(faces)
                expected = expected_betti(a,c,r)
                assert got == expected, (a,c,r,got,expected)
                # Independent verification of the deletion-link face identity.
                # With middle hub 1 deleted, every face lies in two separate stars.
                del_masks = [m for layer in faces.values() for m in layer if not (m&2)]
                with_middle = [m for layer in faces.values() for m in layer if m&2]
                assert len(del_masks)+len(with_middle)==sum(map(len,faces.values()))
                assert all((m & ~2) in del_masks for m in with_middle)
                cases+=1
                all_faces+=sum(map(len,faces.values()))
                if len(got)>=2:
                    mixed.append((a,c,r,got))
    print('VERIFY_OK',cases,'parameters',all_faces,'face instances',len(mixed),'mixed-degree instances')
    print('Examples:',[x for x in mixed if x[:2] in [(3,3),(4,4)]][:5])

if __name__=='__main__':
    run()
