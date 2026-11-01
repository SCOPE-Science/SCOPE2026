#!/usr/bin/env python3
"""Finite reproducibility checks for permutation-fixed generalized Mycielskian complexes.

Only Python's standard library is used. Finite tests complement the general proof.
"""
from itertools import combinations


def mycielskian(n, ell):
    """Graph levels 0..ell, top clique and apex, with labeled vertices."""
    if n < 2 or ell < 1:
        raise ValueError((n, ell))
    a = lambda j, k: j*n + k
    w = (ell + 1)*n
    e = set()
    for j in range(ell):
        for k in range(n):
            for h in range(n):
                if k != h:
                    e.add(tuple(sorted((a(j, k), a(j+1, h)))))
    for k, h in combinations(range(n), 2):
        e.add(tuple(sorted((a(ell, k), a(ell, h)))))
    for k in range(n):
        e.add(tuple(sorted((w, a(0, k)))))
    return w + 1, e


def cyclic_orbits(n, ell, point_stabilizer):
    """The orbits of a cycle on all labels or on labels 1..n-1."""
    count = (ell+1)*n + 1
    def send(v):
        if v == count - 1:
            return v
        j, k = divmod(v, n)
        if point_stabilizer:
            if k == 0:
                return v
            k = 1 + (k % (n-1))
        else:
            k = (k+1) % n
        return j*n+k
    unseen = set(range(count))
    orbits = []
    while unseen:
        v = min(unseen)
        orb = set()
        x = v
        while x not in orb:
            orb.add(x)
            x = send(x)
        assert x == v
        unseen -= orb
        orbits.append(frozenset(orb))
    return orbits


def orbit_graph(orbits, edges):
    """Induced orbit-conflict graph; vertex labels are orbit indices."""
    useful=[]
    for o in orbits:
        if not any(a in o and b in o for a,b in edges):
            useful.append(o)
    conflicts=set()
    for i,j in combinations(range(len(useful)),2):
        if any((a in useful[i] and b in useful[j]) or
               (a in useful[j] and b in useful[i]) for a,b in edges):
            conflicts.add((i,j))
    return useful,conflicts


def independent_faces(v, e):
    nbd=[0]*v
    for x,y in e:
        nbd[x]|=1<<y
        nbd[y]|=1<<x
    bydim={}
    def go(mask,avail):
        bydim.setdefault(mask.bit_count()-1,[]).append(mask)
        while avail:
            low=avail & -avail
            avail-=low
            u=low.bit_length()-1
            go(mask|low,avail & ~nbd[u])
    go(0,(1<<v)-1)
    return bydim


def reduced_f2_betti(v,e):
    faces=independent_faces(v,e)
    rank={}
    for d in range(1,max(faces)+1):
        lower={mask:i for i,mask in enumerate(faces[d-1])}
        basis={}
        for mask in faces[d]:
            bits=0
            temp=mask
            while temp:
                low=temp & -temp
                temp-=low
                bits^=1<<lower[mask^low]
            while bits:
                top=bits.bit_length()-1
                if top in basis:
                    bits^=basis[top]
                else:
                    basis[top]=bits
                    break
        rank[d]=len(basis)
    out={d:len(fs)-rank.get(d,0)-rank.get(d+1,0)
         for d,fs in faces.items() if d>=0}
    out[0]-=1
    return {d:r for d,r in out.items() if r}, sum(map(len,faces.values()))


def check(n,ell,stab):
    N,E=mycielskian(n,ell)
    orbs=cyclic_orbits(n,ell,stab)
    good,conflicts=orbit_graph(orbs,E)
    # Compare the orbit graph, including canonical vertices and every edge.
    def label(orb):
        if (ell+1)*n in orb:
            return 'w'
        layers={v//n for v in orb}
        assert len(layers)==1
        j=next(iter(layers))
        if not stab:
            assert len(orb)==n
            return ('L',j)
        return ('a',j) if len(orb)==1 else ('B',j)
    actual_vertices={label(x) for x in good}
    actual_edges={frozenset((label(good[a]),label(good[b]))) for a,b in conflicts}
    if not stab:
        expected_vertices={('L',j) for j in range(ell)}|{'w'}
        expected_edges={frozenset((('L',j),('L',j+1))) for j in range(ell-1)}
        expected_edges.add(frozenset(('w',('L',0))))
    else:
        expected_vertices={('a',j) for j in range(ell+1)}|{('B',j) for j in range(ell)}|{'w'}
        expected_edges={frozenset(('w',('a',0))),frozenset(('w',('B',0)))}
        for j in range(ell):
            expected_edges.add(frozenset((('B',j),('a',j+1))))
            if j+1<ell:
                expected_edges.add(frozenset((('a',j),('B',j+1))))
                expected_edges.add(frozenset((('B',j),('B',j+1))))
    assert actual_vertices==expected_vertices, (n,ell,stab,actual_vertices,expected_vertices)
    assert actual_edges==expected_edges, (n,ell,stab,actual_edges^expected_edges)
    faces=independent_faces(len(good),conflicts)
    num_faces=sum(map(len,faces.values()))
    if not stab:
        m=ell+1
        if m%3==0: bet={m//3-1:1}
        elif m%3==1:bet={}
        else:bet={m//3:1}
        assert reduced_f2_betti(len(good),conflicts)[0]==bet,(n,ell)
    else:
        assert reduced_f2_betti(len(good),conflicts)[0]=={},(n,ell)
        idx={label(o):i for i,o in enumerate(good)}
        a=idx[('a',ell-1)]
        b=idx[('a',ell)]
        assert frozenset((('a',ell-1),('a',ell))) not in actual_edges
        neighbors={i:set() for i in range(len(good))}
        for i,j in conflicts:
            neighbors[i].add(j);neighbors[j].add(i)
        # Every independent face is in the star of at least one vertex.
        # The intersection is the star of the independent pair.
        for masks in faces.values():
            for mask in masks:
                in_stara=(not any(mask>>j & 1 for j in neighbors[a]))
                in_starb=(not any(mask>>j & 1 for j in neighbors[b]))
                assert in_stara or in_starb, (n,ell,mask)
    return num_faces


def main():
    tests=0; faces=0
    for n in range(3,8):
        for ell in range(1,10):
            for stab in (False,True):
                faces+=check(n,ell,stab)
                tests+=1
    print(f'VERIFY_OK orbit_graphs={tests} quotient_faces={faces} homology_and_star_cover=passed')

if __name__=='__main__':
    main()
