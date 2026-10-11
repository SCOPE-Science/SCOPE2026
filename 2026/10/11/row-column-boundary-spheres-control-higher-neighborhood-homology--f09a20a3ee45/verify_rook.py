#!/usr/bin/env python3
"""Recompute the high-degree homology structure of open-neighborhood complexes of rook graphs."""
from itertools import combinations
from collections import defaultdict


def faces_of_neighborhood_complex(m,n):
    v=tuple((i,j) for i in range(m) for j in range(n))
    neighborhoods={(i,j): frozenset((a,b) for a,b in v if (a==i or b==j) and (a,b)!=(i,j)) for i,j in v}
    faces={frozenset()}
    for N in neighborhoods.values():
        s=sorted(N)
        for k in range(1,len(s)+1):
            faces.update(frozenset(t) for t in combinations(s,k))
    return v,neighborhoods,faces


def in_core(face,m,n):
    return len(face)<=2 or len({i for i,j in face})<=1 or len({j for i,j in face})<=1


def check_decomposition(m,n):
    v,N,faces=faces_of_neighborhood_complex(m,n)
    core={f for f in faces if in_core(f,m,n)}
    assert len([f for f in core if len(f)==2])==len(v)*(len(v)-1)//2
    assert not any(len(f)==n and len({i for i,j in f})==1 for f in faces)
    assert not any(len(f)==m and len({j for i,j in f})==1 for f in faces)
    outside=[f for f in faces if f not in core]
    for f in outside:
        centers=[c for c,S in N.items() if f<=S]
        assert len(centers)==1,(m,n,f,centers)
    for (i,j),S in N.items():
        a={(i,t) for t in range(n) if t!=j}
        b={(t,j) for t in range(m) if t!=i}
        assert a.isdisjoint(b) and S==a|b
        # The intersection of this simplex with the core consists precisely
        # of two full simplices and all edges joining them.
        for k in range(1,len(S)+1):
            for u in combinations(sorted(S),k):
                f=frozenset(u)
                expect=f<=a or f<=b or len(f)<=2
                assert (f in core)==expect,(m,n,(i,j),f)
    return v,N,faces,core,len(outside)


def gf2_rank(cols):
    pivots={}
    for col in cols:
        while col:
            i=col.bit_length()-1
            if i not in pivots:
                pivots[i]=col
                break
            col^=pivots[i]
    return len(pivots)


def mod2_betti(faces):
    bydim=defaultdict(list)
    for f in faces:
        if f:bydim[len(f)-1].append(tuple(sorted(f)))
    ranks={}
    for k in range(1,max(bydim)+1):
        rows={f:i for i,f in enumerate(sorted(bydim[k-1]))}
        cols=[]
        for face in bydim[k]:
            mask=0
            for sub in combinations(face,k):mask^=1<<rows[sub]
            cols.append(mask)
        ranks[k]=gf2_rank(cols)
    return {k:len(v)-ranks.get(k,0)-ranks.get(k+1,0) for k,v in bydim.items()}


def oriented_boundary(elements):
    elements=sorted(elements)
    out={}
    for k in range(len(elements)):
        f=tuple(elements[:k]+elements[k+1:])
        out[f]=(-1)**k
    return out


def act(chain,permutation):
    out={}
    for face,c in chain.items():
        image=[permutation(p) for p in face]
        inv=sum(image[i]>image[j] for i in range(len(image)) for j in range(i+1,len(image)))
        face2=tuple(sorted(image))
        out[face2]=out.get(face2,0)+((-1)**inv)*c
    return {f:c for f,c in out.items() if c}


def signed_action_test(m,n):
    rows=[oriented_boundary([(i,j) for j in range(n)]) for i in range(m)]
    cols=[oriented_boundary([(i,j) for i in range(m)]) for j in range(n)]
    for a in range(m-1):
        def perm(v,a=a):
            i,j=v
            return (a+1 if i==a else a if i==a+1 else i,j)
        assert all(act(rows[i],perm)==rows[a+1 if i==a else a if i==a+1 else i] for i in range(m))
        assert all(act(cols[j],perm)=={f:-c for f,c in cols[j].items()} for j in range(n))
    for a in range(n-1):
        def perm(v,a=a):
            i,j=v
            return (i,a+1 if j==a else a if j==a+1 else j)
        assert all(act(rows[i],perm)=={f:-c for f,c in rows[i].items()} for i in range(m))
        assert all(act(cols[j],perm)==cols[a+1 if j==a else a if j==a+1 else j] for j in range(n))


def main():
    samples=[(3,3),(3,4),(3,5),(3,6),(4,4),(4,5),(5,5),(5,6)]
    for m,n in samples:
        v,N,K,K0,outside=check_decomposition(m,n)
        signed_action_test(m,n)
        relative_chi=sum((-1)**(len(f)-1) for f in K-K0 if f)
        assert relative_chi==m*n*((m-1)*(n-1)-1)
        betti=mod2_betti(K)
        core_betti=mod2_betti(K0)
        predicted={k:(m if k==n-2 else 0)+(n if k==m-2 else 0) for k in range(3,max(m,n)-1)}
        assert all(betti.get(k,0)==expected==core_betti.get(k,0) for k,expected in predicted.items()),(m,n,betti,core_betti,predicted)
        print(f'{m}x{n}: full_faces={len(K)} core_faces={len(K0)} outside={outside} relative_euler={relative_chi} high_reduced_betti={{{", ".join(f"{k}: {v}" for k,v in predicted.items())}}}; all_checks_ok')
    print('VERIFY_OK: exact_face_decomposition, unique_mixed_centers, complete_core_edges, relative_links, relative_euler, mod2_high_homology, signed_Sm_by_Sn_action')

if __name__=='__main__':main()
