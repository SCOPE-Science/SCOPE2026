#!/usr/bin/env python3
"""Check top-dimensional multipath chains and Hamiltonian-cycle generators."""
from itertools import permutations
import random


def paths_and_ridges(vertices, arcs):
    arcs = sorted(arcs)
    E = set(arcs)
    # The Hamiltonian paths are exactly the (n-1)-simplices.
    paths = []
    for p in permutations(vertices):
        edges = tuple((p[i], p[i+1]) for i in range(len(p)-1))
        if all(a in E for a in edges):
            paths.append(frozenset(edges))
    assert len(paths) == len(set(paths))
    ridges = {}
    for p in paths:
        for a in p:
            face = p-{a}
            ridges.setdefault(face, []).append(p)
    return paths, ridges


def hamiltonian_cycles(vertices, arcs):
    E=set(arcs)
    root=min(vertices)
    for t in permutations(v for v in vertices if v != root):
        seq=(root,)+t
        c=frozenset((seq[i], seq[(i+1)%len(seq)]) for i in range(len(seq)))
        if all(a in E for a in c):
            yield c


def top_boundary_rank_mod2(paths, ridges):
    I = {p:i for i,p in enumerate(paths)}
    piv={}
    for incident in ridges.values():
        column=0
        for p in incident:column ^= 1<<I[p]
        while column:
            k=column.bit_length()-1
            if k in piv:column ^= piv[k]
            else:piv[k]=column;break
    return len(piv)


def check(n, arcs):
    vertices=tuple(range(n)); arcs=tuple(sorted(arcs))
    paths,ridges=paths_and_ridges(vertices,arcs)
    cycles=list(hamiltonian_cycles(vertices,arcs))
    cycle_paths={c:set(c-{a} for a in c) for c in cycles}
    assert all(len(v)==n for v in cycle_paths.values())
    assert len(set.union(set(),*cycle_paths.values()))==n*len(cycles)
    covered=set.union(set(),*cycle_paths.values())
    assert covered <=set(paths)
    # Each ridge has one or two completions, and two imply a unique directed cycle.
    for ridge,incident in ridges.items():
        assert 1 <=len(incident)<=2
        if len(incident)==2:
            c=incident[0]|incident[1]
            assert len(c)==n and c in cycle_paths
            assert incident[0] in cycle_paths[c] and incident[1] in cycle_paths[c]
        else:
            assert incident[0] not in covered
    # Explicit signed integer cycle, with canonical lexicographic arc orientation.
    for c in cycles:
        basis={}
        c_sorted=sorted(c)
        for i,e in enumerate(c_sorted):
            basis[frozenset(c-{e})] = (-1)**i
        assert len(basis)==n
        for ridge,incident in ridges.items():
            total=0
            for p in incident:
                if p in basis:
                    for i,e in enumerate(sorted(p)):
                        if p-{e}==ridge:
                            total+=basis[p]*(-1)**i
            assert total==0,(n,arcs,ridge,total)
    rank=top_boundary_rank_mod2(paths,ridges)
    assert len(paths)-rank==len(cycles),(n,len(paths),rank,len(cycles))
    return len(paths),len(ridges),len(cycles)


def wheel(m):
    e={(0,i) for i in range(1,m+1)}|{(i,i%m+1) for i in range(1,m+1)}
    return [(a,b) for u,v in e for a,b in ((u,v),(v,u))]


def complete_bipartite(p,q):
    return [(a,b) for a in range(p) for b in range(p,p+q)]+[(b,a) for a in range(p) for b in range(p,p+q)]


def check_wheel_dihedral(m):
    n=m+1
    cycles=set(hamiltonian_cycles(tuple(range(n)),wheel(m)))
    base=next(iter(cycles))
    images=[]
    for reflect in (0,1):
        for shift in range(m):
            def f(v):
                if v==0:return 0
                return ((shift + (-1 if reflect else 1)*(v-1))%m)+1
            img=frozenset((f(a),f(b)) for a,b in base)
            assert img in cycles
            images.append(img)
    assert len(images)==len(set(images))==len(cycles)==2*m


def check_complete_n4_action():
    # For the complete digraph, stabilizers of Hamiltonian directed cycles
    # consist of cyclic rotations, acting by (-1)^(n-1) per one-step rotation.
    n=4
    arcs=[(a,b) for a in range(n) for b in range(n) if a!=b]
    for cycle in hamiltonian_cycles(tuple(range(n)),arcs):
        # Recover successive vertices of this oriented cycle.
        nxt=dict(cycle)
        seq=[0]
        while len(seq)<n:seq.append(nxt[seq[-1]])
        for r in range(n):
            g={seq[i]:seq[(i+r)%n] for i in range(n)}
            perm=[sorted(cycle).index((g[a],g[b])) for a,b in sorted(cycle)]
            inv=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
            assert (-1)**inv == (-1)**((n-1)*r)


def main():
    results=[]
    for n in (3,4):
        arcs=[(i,j) for i in range(n) for j in range(n) if i!=j]
        allgraphs=1<<len(arcs)
        for mask in range(allgraphs):
            a=[edge for k,edge in enumerate(arcs) if mask>>k&1]
            check(n,a)
        results.append(f'EXHAUSTIVE_SIMPLE_DIGRAPHS_n={n} count={allgraphs}: OK')
    random.seed(20261028)
    for n in (5,6):
        for i in range(100):
            p=.2+.65*random.random()
            a=[(u,v) for u in range(n) for v in range(n) if u!=v and random.random()<p]
            check(n,a)
        results.append(f'RANDOM_SIMPLE_DIGRAPHS_n={n} count=100: OK')
    for m in (4,5,6,7):
        n=m+1
        p,r,h=check(n,wheel(m))
        assert h==2*m
        check_wheel_dihedral(m)
        results.append(f'BIDIRECTED_WHEEL_rim={m} pathfacets={p} ridges={r} cycles={h} dihedral_regular=yes: OK')
    p,r,h=check(6,complete_bipartite(3,3))
    assert h==12
    results.append(f'BIDIRECTED_K33 pathfacets={p} cycles={h}: OK')
    check_complete_n4_action()
    results.append('K4_DIRECTED_CYCLE_ROTATION_SIGN_ACTION: OK')
    print('\n'.join(results))
    print('ARBITRARY_DIGRAPH_HAMILTONIAN_TOP_CYCLE_CHECKS_OK')

if __name__=='__main__':main()
