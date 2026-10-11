#!/usr/bin/env python3
"""Finite sanity checks for a general closed-neighborhood-complex collapse theorem.
The proof of the general theorem is mathematical; these checks do not certify infinity.
Uses only the Python standard library.
"""
from itertools import combinations
from collections import defaultdict
from random import Random


def subsets(items, lo=1, hi=None):
    items = sorted(items)
    if hi is None:
        hi = len(items)
    for k in range(lo, hi + 1):
        for c in combinations(items, k):
            yield frozenset(c)


def base_adj(n, edges):
    adj = [set() for _ in range(n)]
    for a, b in edges:
        assert 0 <= a < b < n
        adj[a].add(b)
        adj[b].add(a)
    assert len(edges) == len(set(edges))
    seen = {0}
    stack = [0]
    while stack:
        v = stack.pop()
        for w in adj[v] - seen:
            seen.add(w)
            stack.append(w)
    assert len(seen) == n
    assert n >= 2 and len(edges) >= 1
    for v in range(n):
        for x, y in combinations(sorted(adj[v]), 2):
            assert y not in adj[x], 'triangle'
            assert not (adj[x] & adj[y] - {v}), 'four-cycle'
    return adj


def prism_adj(adj):
    n = len(adj)
    res = [set() for _ in range(2*n)]
    for v in range(n):
        for i in range(2):
            a = 2*v+i
            res[a].add(2*v + (1-i))
            for w in adj[v]:
                res[a].add(2*w+i)
    for a in range(2*n):
        for b in res[a]:
            assert a in res[b]
    return res


def cech_faces(adj):
    faces = set()
    for v in range(len(adj)):
        faces.update(subsets(adj[v] | {v}))
    return faces


def tetra_boundary(adj):
    expected = set()
    for a in range(len(adj)):
        for b in adj[a]:
            if a < b:
                expected.update(subsets({2*a,2*a+1,2*b,2*b+1}, 1, 3))
    return expected


def verified_collapse(adj, verbose=False):
    n = len(adj)
    P = prism_adj(adj)
    faces = cech_faces(P)
    original = len(faces)
    edges = [(a,b) for a in range(n) for b in sorted(adj[a]) if a < b]
    pairs = []
    for v in range(n):
        for i in range(2):
            center = 2*v+i
            vertical = 2*v+(1-i)
            horizontal = sorted(2*w+i for w in adj[v])
            for h in subsets(horizontal,lo=2):
                for use_vertical in (False,True):
                    low = h | (frozenset({vertical}) if use_vertical else frozenset())
                    upper = low | {center}
                    pairs.append((low, upper))
    assert len(pairs)*2 + len(tetra_boundary(adj)) == original
    assert len(set(low for low,up in pairs)) == len(pairs)
    assert len(set(up for low,up in pairs)) == len(pairs)
    assert not (set(low for low,up in pairs) & set(up for low,up in pairs))
    pairs.sort(key=lambda p:(-len(p[0]), tuple(sorted(p[0]))))
    for j,(low,upper) in enumerate(pairs):
        assert low in faces and upper in faces
        immediate = [low | {w} for w in range(2*n) if w not in low and (low | {w}) in faces]
        assert immediate == [upper], ('not a free face',n,j,low,immediate,upper)
        faces.remove(low)
        faces.remove(upper)
    assert faces == tetra_boundary(adj), ('bad residue', n, len(faces))
    assert all(len(face)<=3 for face in faces)
    m = len(edges)
    assert len(faces) == 8*m + 3*n, (n,m,len(faces))
    if verbose:
        print(f'n={n:2} m={m:2} initial={original:4} collapses={len(pairs):4} residual={len(faces):4}',flush=True)
    return original,len(pairs),faces


def mod2_betti(faces):
    bydim = defaultdict(list)
    for face in faces:
        bydim[len(face)-1].append(tuple(sorted(face)))
    for d in bydim:
        bydim[d].sort()
    ranks = {}
    for d in sorted(bydim):
        if d == 0:continue
        ix={f:j for j,f in enumerate(bydim[d-1])}
        piv={}
        for f in bydim[d]:
            v=0
            for sub in combinations(f,d):v ^= 1 << ix[sub]
            while v:
                b=v.bit_length()-1
                if b not in piv:
                    piv[b]=v
                    break
                v ^= piv[b]
        ranks[d]=len(piv)
    betti={d:len(bydim[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in bydim}
    betti[0]-=1
    return {d:r for d,r in betti.items() if r}


def run_case(n,edges,name):
    a=base_adj(n,edges)
    P=prism_adj(a)
    full=cech_faces(P)
    before,steps,residue=verified_collapse(a,verbose=False)
    beta=mod2_betti(full)
    expected={2:len(edges)}
    if len(edges)-n+1:
        expected[1]=len(edges)-n+1
    assert beta==expected, (name,beta,expected)
    assert mod2_betti(residue)==expected
    print(f'{name:17} n={n:2}, m={len(edges):2}, faces={before:4}, free_pairs={steps:4}, beta={beta}',flush=True)


def graph_from_adj_list(adj):
    return [(v,w) for v in range(len(adj)) for w in adj[v] if v<w]


def random_safe_graph(n,seed):
    rng=Random(seed)
    edges=[]
    adj=[set() for _ in range(n)]
    for v in range(1,n):
        choices=list(range(v))
        rng.shuffle(choices)
        w=choices[0]
        edges.append((w,v));adj[w].add(v);adj[v].add(w)
    possibles=[(v,w) for v in range(n) for w in range(v+1,n) if w not in adj[v]]
    rng.shuffle(possibles)
    for v,w in possibles:
        # add chord only when existing distance at least four
        queue=[v]
        distances={v:0}
        for x in queue:
            for y in adj[x]:
                if y not in distances:
                    distances[y]=distances[x]+1;queue.append(y)
        if distances[w]>=4 and rng.random()<0.25:
            adj[v].add(w);adj[w].add(v);edges.append((v,w))
    return sorted(edges)


def main():
    tests=[]
    tests += [(n,[(i,i+1) for i in range(n-1)],f'path-{n}') for n in range(2,8)]
    tests += [(n,[(i,(i+1)%n) if i<n-1 else (0,n-1) for i in range(n)],f'cycle-{n}') for n in range(5,11)]
    tests += [(n+1,[(0,i) for i in range(1,n+1)],f'star-{n}') for n in range(2,8)]
    # generalized theta, two terminals with 3 internally disjoint paths of length 3
    tests += [(8,[(0,2),(2,3),(3,1),(0,4),(4,5),(5,1),(0,6),(6,7),(7,1)],'theta-3x3')]
    # Petersen graph: outer five-cycle, spokes, inner pentagram
    p=[(i,(i+1)%5) if i<4 else (0,4) for i in range(5)]
    p += [(i,5+i) for i in range(5)]
    p += [(min(5+i,5+(i+2)%5),max(5+i,5+(i+2)%5)) for i in range(5)]
    tests += [(10,p,'Petersen')]
    # Heawood graph, 14 vertices: incidence of Fano plane
    lines=[{0,1,2},{0,3,4},{0,5,6},{1,3,5},{1,4,6},{2,3,6},{2,4,5}]
    h=[(x,7+i) for i,line in enumerate(lines) for x in line]
    tests += [(14,h,'Heawood')]
    for seed in range(20):
        n=7+seed%6
        tests.append((n,random_safe_graph(n,1000+seed),f'sparse-{seed:02}'))
    for n,edges,name in tests:
        edges=sorted({tuple(sorted(edge)) for edge in edges})
        run_case(n,edges,name)
    # The two forbidden short-cycle patterns really change the result.
    for size, observed in [(3,{2:4}),(4,{2:7})]:
        cyc=sorted({tuple(sorted((i,(i+1)%size))) for i in range(size)})
        adj=[set() for _ in range(size)]
        for a,b in cyc:adj[a].add(b);adj[b].add(a)
        beta=mod2_betti(cech_faces(prism_adj(adj)))
        assert beta==observed,('short cycle boundary',size,beta)
        print(f'boundary-C{size:2} homology={beta}',flush=True)
    print('VERIFY_OK:',len(tests),'connected girth>=5 instances, exact free-face collapses and independent mod-2 ranks')

if __name__=='__main__':
    main()
