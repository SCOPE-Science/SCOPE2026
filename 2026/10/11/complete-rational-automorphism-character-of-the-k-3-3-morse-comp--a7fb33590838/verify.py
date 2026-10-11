#!/usr/bin/env python3
"""Exact verification of the ordinary Morse-complex rational homology character of K(3,3)."""
from collections import Counter
from itertools import combinations, permutations, product

NODES=tuple(range(6))
EDGES=tuple((i,j) for i in range(3) for j in range(3,6))
ARC=tuple((u,v) for u in NODES for v in NODES if (min(u,v),max(u,v)) in EDGES)
ARC_INDEX={a:i for i,a in enumerate(ARC)}


def is_field(pairs):
    tails=[u for u,v in pairs]
    if len(tails)!=len(set(tails)):return False
    if len({(min(u,v),max(u,v)) for u,v in pairs})!=len(pairs):return False
    nxt=dict(pairs)
    for start in nxt:
        seen=set();x=start
        while x in nxt:
            if x in seen:return False
            seen.add(x);x=nxt[x]
    return True


def face_from_arcs(arcs):
    return tuple(sorted(ARC_INDEX[a] for a in arcs))


def census_by_vertex():
    allowed=[(None,)+tuple(v for v in NODES if (min(u,v),max(u,v)) in EDGES) for u in NODES]
    faces=set()
    for opt in product(*allowed):
        arcs=[(u,v) for u,v in enumerate(opt) if v is not None]
        if arcs and is_field(arcs):faces.add(face_from_arcs(arcs))
    return faces


def census_by_edge():
    faces=set()
    for opt in product((0,1,2), repeat=9):
        arcs=[]
        for (a,b),o in zip(EDGES,opt):
            if o==1:arcs.append((a,b))
            elif o==2:arcs.append((b,a))
        if arcs and is_field(arcs):faces.add(face_from_arcs(arcs))
    return faces


def rank_mod2(columns):
    piv={}
    for bits in columns:
        while bits:
            hi=bits.bit_length()-1
            if hi in piv:bits^=piv[hi]
            else:piv[hi]=bits;break
    return len(piv)


def parity(perm):
    return -1 if sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))%2 else 1


def s3char(p):
    return (1,parity(p),sum(p[i]==i for i in range(3))-1)


def permclass(p):
    if all(p[i]==i for i in range(3)):return '1^3'
    return '2,1' if parity(p)<0 else '3'


def group_actions():
    for a in permutations(range(3)):
        for b in permutations(range(3)):
            for t in (0,1):
                p=tuple(a[i]+(3 if t else 0) for i in range(3))+tuple(b[i]+(0 if t else 3) for i in range(3))
                yield (a,b,t,p)


def calculate():
    by_vertex=census_by_vertex()
    by_edge=census_by_edge()
    assert by_vertex==by_edge
    faces=by_vertex
    assert len(faces)==1791
    by={k:sorted(f for f in faces if len(f)==k) for k in range(1,6)}
    assert tuple(len(by[k]) for k in range(1,6))==(18,126,432,729,486)
    assert all(f[:j]+f[j+1:] in faces for f in faces for j in range(len(f)) if len(f)>1)
    ranks=[1]
    for k in range(2,6):
        lower={f:j for j,f in enumerate(by[k-1])}
        cols=[]
        for f in by[k]:
            col=0
            for j in range(k):col^=1<<lower[f[:j]+f[j+1:]]
            cols.append(col)
        ranks.append(rank_mod2(cols))
    assert ranks==[1,17,109,323,406],ranks
    # Each rank over Q is bounded below by its mod-2 rank and above by
    # the dimension of the kernel of the preceding boundary. The listed
    # ranks saturate every one of those upper bounds.
    f=[1]+[len(by[k]) for k in range(1,6)]
    assert all(ranks[k]==f[k]-ranks[k-1] for k in range(1,5))
    assert f[5]-ranks[4]==80
    assert sum((-1)**(k-1)*len(by[k]) for k in range(1,6))==81

    character=[]
    irrep={k:[] for k in ('tt+','tt-','ss+','ss-','uu+','uu-','ts','tu','su')}
    class_value={}
    actions=list(group_actions())
    assert len(actions)==72
    for a,b,t,p in actions:
        perm_arc=[ARC_INDEX[(p[u],p[v])] for u,v in ARC]
        sum_direct=0
        sum_by_orbits=0
        for face in faces:
            seq=[perm_arc[j] for j in face]
            if set(seq)!=set(face):continue
            assert tuple(sorted(seq)) in faces
            k=len(face)
            # Signed oriented simplex trace with orientation induced by ARC ordering.
            sum_direct+=(-1)**(k-1)*parity(seq)
            # Independent parity check: sign of a permutation with c cycles
            # on k letters is (-1)^(k-c).
            visited=set(); cycles=0
            for j in face:
                if j in visited:continue
                cycles+=1;x=j
                while x not in visited:
                    visited.add(x);x=perm_arc[x]
            assert len(visited)==k
            sum_by_orbits+=(-1)**(cycles-1)
        assert sum_direct==sum_by_orbits
        v=sum_direct-1
        character.append(v)
        if t==0:key=tuple(sorted((permclass(a),permclass(b))))
        else:key=('swap',permclass(tuple(b[a[i]] for i in range(3))))
        if key in class_value:assert class_value[key]==v
        else:class_value[key]=v
        ca=s3char(a);cb=s3char(b)
        if not t:
            for j,k in enumerate(('tt','ss','uu')):
                irrep[k+'+'].append(ca[j]*cb[j])
                irrep[k+'-'].append(ca[j]*cb[j])
            for (i,j),k in zip(((0,1),(0,2),(1,2)),('ts','tu','su')):
                irrep[k].append(ca[i]*cb[j]+ca[j]*cb[i])
        else:
            q=tuple(b[a[i]] for i in range(3));cq=s3char(q)
            for j,k in enumerate(('tt','ss','uu')):
                irrep[k+'+'].append(cq[j]);irrep[k+'-'].append(-cq[j])
            for k in ('ts','tu','su'):irrep[k].append(0)
    assert class_value=={
       ('1^3','1^3'):80, ('1^3','2,1'):0, ('1^3','3'):2,
       ('2,1','2,1'):0, ('2,1','3'):0, ('3','3'):5,
       ('swap','1^3'):-4, ('swap','2,1'):0, ('swap','3'):-1},class_value
    # Prove the nine candidates are a full orthonormal character basis.
    labels=list(irrep)
    assert all(sum(x*y for x,y in zip(irrep[k],irrep[h]))==(72 if k==h else 0)
               for k in labels for h in labels)
    dim={k:irrep[k][0] for k in labels}
    assert sum(d*d for d in dim.values())==72
    numer={k:sum(x*y for x,y in zip(character,irrep[k])) for k in labels}
    assert all(z%72==0 for z in numer.values())
    mult={k:z//72 for k,z in numer.items()}
    assert mult=={'tt+':1,'tt-':2,'ss+':1,'ss-':2,'uu+':4,'uu-':5,'ts':3,'tu':4,'su':4},mult
    assert sum(mult[k]*dim[k] for k in labels)==80
    assert sum(character)==72 # one-dimensional full fixed subspace
    assert character[1]==-4 # pure bipartition interchange
    print('FACETS',tuple(len(by[k]) for k in range(1,6)))
    print('AUGMENTED_MOD2_RANKS',tuple(ranks))
    print('AUTOMORPHISMS',len(actions))
    print('CHARACTER_CLASSES',dict(sorted(class_value.items(),key=lambda x:str(x[0]))))
    print('IRREDUCIBLE_MULTIPLICITIES',mult)
    print('GLOBAL_INVARIANTS',sum(character)//72)
    print('SWAP_EIGEN_DIMENSIONS',(80-4)//2,(80+4)//2)
    print('VERIFY_OK')

if __name__=='__main__':calculate()
