#!/usr/bin/env python3
"""Independent finite consistency checks for coordinate-block fixed Rips complexes.
Run: python3 check_fixed_double_swap.py
Only finite cases are checked; the infinite-family proof is in RESULT.md.
"""
from itertools import combinations


def trans(x):
    return (x & ~15) | ((x & 1) << 1) | ((x & 2) >> 1) | ((x & 4) << 1) | ((x & 8) >> 1)


def orbitset(n, mode):
    total = 1 << n
    if mode == 'cyclic':
        generators = [trans]
    else:
        def s1(x): return (x & ~3) | ((x & 1) << 1) | ((x & 2) >> 1)
        def s2(x): return (x & ~12) | ((x & 4) << 1) | ((x & 8) >> 1)
        generators = [s1, s2]
    seen = set()
    result = []
    for x in range(total):
        if x in seen: continue
        o = {x}
        stack = [x]
        while stack:
            u = stack.pop()
            for g in generators:
                v = g(u)
                if v not in o: o.add(v); stack.append(v)
        seen.update(o)
        o = tuple(sorted(o))
        if max((a ^ b).bit_count() for a in o for b in o) <= 2:
            result.append(o)
    return sorted(result)


def complex_faces(orbits):
    N = len(orbits)
    adjacent = [set() for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            if all((a ^ b).bit_count() <= 2 for a in orbits[i] for b in orbits[j]):
                adjacent[i].add(j)
                adjacent[j].add(i)
    faces = set()
    def extend(f, candidates):
        if f: faces.add(tuple(f))
        for index, v in enumerate(candidates):
            extend(f + [v], [u for u in candidates[index+1:] if u in adjacent[v]])
    extend([], list(range(N)))
    return faces


def betti_one_mod_two(faces):
    vertices = {f for f in faces if len(f) == 1}
    edges = sorted(f for f in faces if len(f) == 2)
    tris = sorted(f for f in faces if len(f) == 3)
    parent = {v[0]:v[0] for v in vertices}
    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for a,b in edges:
        pa,pb = root(a),root(b)
        parent[pa] = pb
    components = len({root(v[0]) for v in vertices})
    rank_d1 = len(vertices)-components
    eindex = {e:i for i,e in enumerate(edges)}
    basis = {}
    for a,b,c in tris:
        v = (1 << eindex[a,b]) ^ (1 << eindex[a,c]) ^ (1 << eindex[b,c])
        while v:
            high = v.bit_length()-1
            if high not in basis: basis[high]=v; break
            v ^= basis[high]
    return len(edges) - rank_d1 - len(basis), components


def collapse_4(faces):
    faces = set(faces)
    triangle_pairs = []
    while True:
        match = None
        triangles = {f for f in faces if len(f) == 3}
        for edge in sorted(f for f in faces if len(f) == 2):
            co = [t for t in triangles if set(edge).issubset(t)]
            if len(co) == 1:
                match = (edge, co[0]); break
        if not match: break
        faces.remove(match[0]); faces.remove(match[1]); triangle_pairs.append(match)
    assert not any(len(f)==3 for f in faces)
    vertex_pairs=[]
    while True:
        deg = {v[0]: 0 for v in faces if len(v)==1}
        for u,v in (e for e in faces if len(e)==2):
            deg[u]+=1;deg[v]+=1
        leaves=sorted(u for u,d in deg.items() if d==1)
        if not leaves: break
        u=leaves[0];e=next(e for e in faces if len(e)==2 and u in e)
        faces.remove((u,));faces.remove(e);vertex_pairs.append((u,e))
    assert len(triangle_pairs) == 8
    assert len(vertex_pairs) == 3
    assert len([f for f in faces if len(f)==2]) == 5
    assert len([f for f in faces if len(f)==1]) == 5
    assert betti_one_mod_two(faces) == (1,1)
    print('n=4 elementary collapse: 8 triangle-edge pairs, 3 edge-vertex pairs, final 5-cycle')


def main():
    for n in range(4,9):
        a=orbitset(n,'cyclic')
        b=orbitset(n,'klein')
        assert a==b, ('orbit discrepancy',n)
        assert len(a)==8*(1<<(n-4))
        faces=complex_faces(a)
        b1,components=betti_one_mod_two(faces)
        assert (components,b1)==(1,1),(n,components,b1)
        print('n=%d: %d orbit vertices, %d nonempty simplices, H_1(F_2) rank %d' % (n,len(a),len(faces),b1))
        if n==4:collapse_4(faces)
    print('Finite consistency checks passed; no infinite or integral conclusion is inferred from enumeration.')

if __name__=='__main__':main()
