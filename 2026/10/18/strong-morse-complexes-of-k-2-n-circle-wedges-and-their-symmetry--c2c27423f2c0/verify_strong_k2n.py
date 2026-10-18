"""Reproducible finite tests for the strong Morse complex of K_{2,n}.
Run with Python 3.10 or newer. No external packages are required.
"""
import itertools
from collections import Counter


def setup(n):
    vertices=range(n+2)
    A,B=0,1
    leaves=range(2,n+2)
    edges=[(c,j) for c in (A,B) for j in leaves]
    arcs=[(u,v) for u,v in edges]+[(v,u) for u,v in edges]
    arc_id={a:i for i,a in enumerate(arcs)}
    adjacent=[set() for _ in vertices]
    for u,v in edges:
        adjacent[u].add(v);adjacent[v].add(u)
    return arcs,arc_id,adjacent


def all_faces(n):
    arcs,arc_id,adjacent=setup(n)
    faces={0}
    for order in itertools.permutations(range(n+2)):
        seen=set()
        generator=0
        for v in order:
            earlier=seen.intersection(adjacent[v])
            if len(earlier)==1:
                u=next(iter(earlier))
                generator|=1<<arc_id[(v,u)]
            seen.add(v)
        sub=generator
        while sub:
            faces.add(sub)
            sub=(sub-1)&generator
    return faces,arcs


def predicted_faces(n,arcs):
    arc_id={a:i for i,a in enumerate(arcs)}
    U=[arc_id[(j,0)] for j in range(2,n+2)]
    V=[arc_id[(j,1)] for j in range(2,n+2)]
    P=[arc_id[(0,j)] for j in range(2,n+2)]
    Q=[arc_id[(1,j)] for j in range(2,n+2)]
    facets=[U,V]
    for j in range(n):
        facets.extend([[P[j]]+[U[k] for k in range(n) if k!=j],
                       [Q[j]]+[V[k] for k in range(n) if k!=j],
                       [U[j],Q[j]],[P[j],V[j]],[P[j],Q[j]]])
    faces={0}
    for facet in facets:
        mask=sum(1<<j for j in facet)
        sub=mask
        while sub:
            faces.add(sub)
            sub=(sub-1)&mask
    return faces


def mod2_betti(faces):
    groups={d:[] for d in range(max(f.bit_count() for f in faces))}
    for face in faces:
        if face:groups[face.bit_count()-1].append(face)
    ranks={}
    for d in sorted(groups,reverse=True):
        if d==0:continue
        indices={f:i for i,f in enumerate(groups[d-1])}
        pivots={}
        for f in groups[d]:
            bd=0;s=f
            while s:
                b=s&-s;s-=b
                bd^=1<<indices[f^b]
            while bd:
                pivot=bd.bit_length()-1
                if pivot in pivots:bd^=pivots[pivot]
                else:pivots[pivot]=bd;break
        ranks[d]=len(pivots)
    return {d:len(groups[d])-ranks.get(d,0)-ranks.get(d+1,0)-(d==0) for d in groups}


def induced_lefschetz(faces,arcs,leaf_permutation,swap):
    n=len(leaf_permutation)
    vertex_perm={0:1 if swap else 0,1:0 if swap else 1}
    vertex_perm.update({j+2:leaf_permutation[j]+2 for j in range(n)})
    arc_ids={a:i for i,a in enumerate(arcs)}
    p=[arc_ids[(vertex_perm[u],vertex_perm[v])] for u,v in arcs]
    total=0
    for face in faces:
        if not face:continue
        ids=[i for i in range(len(arcs)) if face>>i&1]
        images=[p[i] for i in ids]
        if sorted(images)!=ids:continue
        parity=sum(images[i]>images[j] for i in range(len(images)) for j in range(i+1,len(images)))%2
        total+=(-1)**(len(ids)-1+parity)
    return total


def run():
    for n in range(2,8):
        actual,arcs=all_faces(n)
        expected=predicted_faces(n,arcs)
        assert actual==expected,(n,'facet equality',list(actual^expected)[:10])
        betti=mod2_betti(actual)
        assert betti[0]==0 and betti[1]==3*n-1 and all(betti[d]==0 for d in betti if d>=2),(n,betti)
        counts=dict(sorted(Counter(f.bit_count()-1 for f in actual if f).items()))
        print('n',n,'faces',len(actual)-1,'f_vector',counts,'reduced_mod2_betti',betti,'facet_identification','PASS')
        if n<=5:
            count=0
            for sigma in itertools.permutations(range(n)):
                fixed=sum(sigma[i]==i for i in range(n))
                for swap in (False,True):
                    L=induced_lefschetz(actual,arcs,sigma,swap)
                    expected_trace=(1-fixed if swap else 3*fixed-1)
                    assert L==1-expected_trace,(n,sigma,swap,L,expected_trace)
                    count+=1
            print('n',n,'automorphism_Lefschetz_checks',count,'PASS')
    print('ALL_CHECKS_PASS')

if __name__=='__main__':run()
