#!/usr/bin/env python3
"""Self-contained finite checks for the Paley-17 flag-complex result.

Run with Python 3.10+, standard library only. An optional certificate file
is passed as the first argument and is checked against independently
reconstructed faces. Nothing is downloaded.
"""
import itertools
import json
import sys
from collections import Counter

P = 17
Q = {i * i % P for i in range(1, P)}
VERTICES = [(i,) for i in range(P)]
EDGES = [e for e in itertools.combinations(range(P), 2) if (e[1] - e[0]) % P in Q]
TRIANGLES = [t for t in itertools.combinations(range(P), 3)
             if all((b-a)%P in Q for a,b in itertools.combinations(t,2))]
TETRAHEDRA = [t for t in itertools.combinations(range(P), 4)
              if all((b-a)%P in Q for a,b in itertools.combinations(t,2))]
FACES = set(VERTICES + EDGES + TRIANGLES + TETRAHEDRA)
MIDPOINT = {(u,v): tuple(sorted((u,v,((u+v)*9)%P))) for (u,v) in EDGES}
assert len(set(MIDPOINT.values()))==len(TRIANGLES) and set(MIDPOINT.values())==set(TRIANGLES)
assert len(Q)==8 and (len(EDGES),len(TRIANGLES),len(TETRAHEDRA)) == (68,68,0)
assert len(FACES)==153

def canonical(face):return tuple(sorted(face))

def construct_certificate():
    # Deterministic BFS spanning tree with labeled tie break.
    seen={0}; parent={}
    frontier=[0]
    for u in frontier:
        for v in range(P):
            if v not in seen and canonical((u,v)) in EDGES:
                seen.add(v);parent[v]=u;frontier.append(v)
    assert len(seen)==P
    tree={canonical((v,p)) for v,p in parent.items()}
    resolved=set(tree)
    selected=[]
    while len(resolved)<len(EDGES):
        for triangle in TRIANGLES:
            unresolved=[e for e in itertools.combinations(triangle,2) if e not in resolved]
            if len(unresolved)==1:
                e=unresolved[0]
                selected.append({'edge':list(e),'triangle':list(triangle)})
                resolved.add(e)
                break
        else:
            raise AssertionError('no singleton-edge triangle to continue')
    assert len(selected)==52
    return {'prime':P,'quadratic_residues':sorted(Q),'root':0,
            'tree_parent':[[v,parent[v]] for v in sorted(parent)],
            'edge_triangle_pairs':selected}

def cycle_check(cert):
    # Directed Hasse diagram: matched arrows go low->high;
    # unmatched arrows go high->low.
    tree_pairs={(canonical((v,)),canonical((v,p))) for v,p in cert['tree_parent']}
    tri_pairs={(canonical(row['edge']),canonical(row['triangle']))
               for row in cert['edge_triangle_pairs']}
    pairs=tree_pairs|tri_pairs
    assert len(tree_pairs)==16 and len(tri_pairs)==52 and len(pairs)==68
    matched_cells=[]
    for a,b in pairs:
        assert a in FACES and b in FACES and len(b)==len(a)+1
        assert set(a).issubset(b)
        matched_cells += [a,b]
    assert len(matched_cells)==len(set(matched_cells))
    assert all((v,) in FACES for v in range(P))
    successors={f:[] for f in FACES}
    indeg={f:0 for f in FACES}
    covers=0
    for high in FACES:
        if len(high)==1:continue
        for low in itertools.combinations(high,len(high)-1):
            if (low,high) in pairs:
                u,v=low,high
            else:
                u,v=high,low
            successors[u].append(v)
            indeg[v]+=1
            covers+=1
    work=[v for v in FACES if indeg[v]==0]
    traversed=0
    while work:
        x=work.pop();traversed+=1
        for y in successors[x]:
            indeg[y]-=1
            if indeg[y]==0:work.append(y)
    assert traversed==len(FACES),'not acyclic'
    critical=FACES-set(matched_cells)
    assert len(critical)==17 and (0,) in critical
    assert Counter(map(len,critical))=={1:1,3:16}
    return critical,covers

def parity(values):
    return -1 if sum(x>y for i,x in enumerate(values) for y in values[i+1:])%2 else 1

def trace(a,b):
    moved=lambda x:(a*x+b)%P
    euler=0
    contributions=Counter()
    for simplex in FACES:
        image=tuple(moved(x) for x in simplex)
        if set(image)==set(simplex):
            signed=(-1)**(len(simplex)-1)*parity(image)
            euler+=signed
            contributions[(len(simplex),signed)]+=1
    return euler-1,contributions

def verify():
    cert=construct_certificate()
    for a in Q:
        for b in range(P):
            for edge, triangle in MIDPOINT.items():
                im_e=canonical(((a*x+b)%P for x in edge))
                im_t=canonical(((a*x+b)%P for x in triangle))
                assert MIDPOINT[im_e]==im_t
    if len(sys.argv)>1:
        actual=json.load(open(sys.argv[1],encoding='utf8'))
        assert cert==actual,'certificate does not match independent deterministic construction'
    critical,covers=cycle_check(cert)
    assert covers == 68*2 +68*3, covers
    aorders={}
    for a in sorted(Q):
        order=next(n for n in range(1,9) if pow(a,n,P)==1)
        aorders[a]=order
        for b in range(P):
            expected = 16 if (a,b)==(1,0) else (-1 if a==1 else 0)
            observed,_=trace(a,b)
            assert observed==expected,(a,b,observed,expected)
    assert sorted(aorders.values())==[1,2,4,4,8,8,8,8]
    assert trace(16,0)[1] == {(1,1):1,(2,1):4,(3,-1):4}
    # Translation subgroup has character 16 at identity and -1 elsewhere.
    assert sum(trace(1,b)[0] for b in range(P))==0
    for d in [1,2,4,8]:
        assert (16//d)==16/d
    for d in [1,2,4,8]:
        # Complement subgroup fixed dimension, and all conjugates.
        H=sorted(a for a in Q if pow(a,d,P)==1)
        assert len(H)==d
        assert sum(trace(a,0)[0] for a in H)==16
        assert sum(trace(a,0)[0] for a in H)//d == 16//d
    print('residues:',','.join(map(str,sorted(Q))))
    print('faces (dimensions 0,1,2,3):',len(VERTICES),len(EDGES),len(TRIANGLES),len(TETRAHEDRA))
    print('affine-equivariant midpoint bijection: 68 edges to 68 triangles verified')
    print('Morse matching: 16 vertex-edge pairs, 52 edge-triangle pairs')
    print('Hasse cover relations:',covers,'acyclic: yes')
    print('critical cells: one vertex, sixteen triangles')
    print('affine elements checked:',len(Q)*P)
    print('character: 16 on identity, -1 on 16 nonidentity translations, 0 on 119 other elements')
    print('order-two multiplier fixed-simplex signed count:',dict(trace(16,0)[1]))
    print('subgroup invariants: translation-containing 0; translation-free order 1,2,4,8 have ranks 16,8,4,2')
    print('PASS')
    return cert

if __name__=='__main__':verify()
