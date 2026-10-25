#!/usr/bin/env python3
"""Exact finite verification of transposition-fixed Johnson clique complexes."""
from itertools import combinations
from math import comb


def subsets(n, k):
    return [sum(1 << z for z in C) for C in combinations(range(n), k)]


def swap_bits(x):
    a, b = (x & 1) != 0, (x & 2) != 0
    return x ^ 3 if a != b else x


def neighbor(x, y):
    return (x ^ y).bit_count() == 2


def orbits(n, k):
    seen = set()
    out = []
    for x in subsets(n, k):
        if x in seen:
            continue
        y = swap_bits(x)
        seen.add(x); seen.add(y)
        if x == y or neighbor(x, y):
            out.append(tuple(sorted(set((x, y)))))
    return out


def fixed_faces(n, k):
    obs = orbits(n, k)
    count = len(obs)
    adjacency = [0] * count
    for i in range(count):
        for j in range(i + 1, count):
            if all(neighbor(x, y) for x in obs[i] for y in obs[j]):
                adjacency[i] |= 1 << j
                adjacency[j] |= 1 << i
    faces = {}
    def grow(prefix, mask):
        while mask:
            b = mask & -mask
            mask -= b
            j = b.bit_length()-1
            f = prefix | b
            faces.setdefault(f.bit_count() - 1, []).append(f)
            grow(f, mask & adjacency[j] & ~((1 << (j + 1)) - 1))
    grow(0, (1 << count)-1)
    return obs, faces


def rank_mod2(columns):
    pivots = {}
    for x in columns:
        while x:
            p = x.bit_length()-1
            if p in pivots:
                x ^= pivots[p]
            else:
                pivots[p] = x
                break
    return len(pivots)


def betti(faces):
    maxdim = max(faces)
    sizes = [len(faces.get(i, [])) for i in range(maxdim+1)]
    ranks = []
    for d in range(1, maxdim + 1):
        idx = {face:z for z, face in enumerate(faces[d-1])}
        cols = []
        for face in faces[d]:
            col = 0
            x = face
            while x:
                b = x & -x
                x -= b
                col ^= 1 << idx[face ^ b]
            cols.append(col)
        ranks.append(rank_mod2(cols))
    hom = []
    for d,s in enumerate(sizes):
        lo = ranks[d-1] if d > 0 else 0
        hi = ranks[d] if d < maxdim else 0
        hom.append(s-lo-hi)
    hom[0] -= 1
    return sizes,hom


def beta(m,j):
    if j in (0,1,m-1,m):
        return 0
    assert 2<=j<=m-2
    v=comb(m,j)
    e=v*j*(m-j)//2
    return (v-e-1
        +comb(m,j-1)*(comb(m-j+1,2)-(m-j+1)+1)
        +comb(m,j+1)*(comb(j+1,2)-(j+1)+1))


def main():
    for n,k in [(6,3),(7,3),(7,4),(8,3),(8,4),(9,3),(9,4),(10,4),(10,5),(11,5)]:
        obs,F=fixed_faces(n,k)
        f,h=betti(F)
        m=n-2
        exp1=comb(m,k-1)-1
        exp2=beta(m,k)+beta(m,k-2)
        assert h==[0,exp1,exp2]+[0]*max(0,len(h)-3),(n,k,h,(exp1,exp2))
        assert f[0]==comb(m,k)+comb(m,k-2)+comb(m,k-1)
        print(f'(n,k)=({n},{k}): orbit_vertices={len(obs)}, faces={sum(f)}, f={f}, reduced_betti_mod2={h}, prediction=(0,{exp1},{exp2})')
    print('JOHNSON_TRANSPOSITION_FIXED_HOMOLOGY_VERIFIED')

if __name__ == '__main__': main()
