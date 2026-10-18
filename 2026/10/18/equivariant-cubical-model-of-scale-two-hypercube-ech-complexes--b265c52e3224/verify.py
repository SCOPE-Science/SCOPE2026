#!/usr/bin/env python3
"""Exact finite checks for a cubical model of scale-two hypercube Cech complexes.
No scientific claim relies on numerical extrapolation."""
from itertools import combinations, permutations, product
from math import comb


def cube_neighbors(v,n):
    return (v,)*(1)+tuple(v^(1<<i) for i in range(n))


def cech_faces(n):
    faces=set()
    for v in range(1<<n):
        star=cube_neighbors(v,n)
        for r in range(1,n+2):
            faces.update(combinations(sorted(star),r))
    return faces


def joined_faces(n):
    """Right vertices 0..2**n-1, left center vertices 2**n..2**(n+1)-1."""
    N=1<<n
    faces=set()
    for v in range(N):
        pts=tuple(sorted(cube_neighbors(v,n)))
        for r in range(1,len(pts)+1):
            for ss in combinations(pts,r):
                faces.add(ss)
                faces.add(tuple(sorted(ss+(N+v,))))
        faces.add((N+v,))
    return faces


def residual_faces(n):
    N=1<<n
    faces={(w,) for w in range(N)}|{(N+v,) for v in range(N)}
    for v in range(N):
        st=sorted(cube_neighbors(v,n))
        for w in st:
            faces.add(tuple(sorted((N+v,w))))
        for a,b in combinations(st,2):
            faces.add((a,b))
            faces.add(tuple(sorted((a,b,N+v))))
    return faces


def verify_collapse(n):
    N=1<<n
    faces=joined_faces(n)
    npairs=0
    for r in range(n+1,2,-1):
        candidates=[]
        for v in range(N):
            for ss in combinations(sorted(cube_neighbors(v,n)),r):
                a=ss
                b=tuple(sorted(ss+(N+v,)))
                assert a in faces and b in faces,(n,r,v,ss)
                candidates.append((a,b))
        assert len({a for a,b in candidates})==len(candidates)
        for a,b in candidates:
            # no other codimension-one coface remains
            remain=[f for f in faces if len(f)==len(b) and set(a)<=set(f)]
            assert remain==[b],(n,r,a,remain)
        for a,b in candidates:
            faces.remove(a)
            faces.remove(b)
        npairs+=len(candidates)
    assert faces==residual_faces(n),(n,len(faces),len(residual_faces(n)),len(faces^residual_faces(n)))
    assert npairs==(1<<n)*sum(comb(n+1,r) for r in range(3,n+2))
    return npairs,len(faces)


def perm_apply(v,perm,a):
    return a^sum((1<<perm[i]) for i in range(len(perm)) if v&(1<<i))


def perm_sign(seq):
    return -1 if sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))%2 else 1


def face_lefschetz(n,perm,a,faces):
    s=0
    for f in faces:
        t=tuple(perm_apply(v,perm,a) for v in f)
        if set(t)==set(f):
            s+=(-1)**(len(f)-1)*perm_sign(t)
    return s


def bitpar(x):
    return x.bit_count()%2


def cubical_trace(n,perm,a,k):
    """Signed trace of cellular chains in dimension k of Q_(n+1)."""
    m=n+1
    bigperm=perm+(n,)
    aa=a|(bitpar(a)<<n)
    total=0
    for I in combinations(range(m),k):
        J=tuple(j for j in range(m) if j not in I)
        if set(bigperm[j] for j in I)!=set(I):
            continue
        sign=perm_sign(tuple(bigperm[j] for j in I))*(-1)**sum(bool(aa&(1<<i)) for i in I)
        fixed=0
        for bits in range(1<<len(J)):
            x=sum(((bits>>idx)&1)<<j for idx,j in enumerate(J))
            y=perm_apply(x,bigperm,aa)
            if all(bool(x&(1<<j))==bool(y&(1<<j)) for j in J):
                fixed+=1
        total+=sign*fixed
    return total


def cycle_formula(n,perm,a,k):
    m=n+1; p=perm+(n,); aa=a|(bitpar(a)<<n)
    cycles=[];seen=set()
    for i in range(m):
        if i not in seen:
            C=[];j=i
            while j not in seen:
                seen.add(j);C.append(j);j=p[j]
            cycles.append(C)
    out=0
    for select in product((0,1),repeat=len(cycles)):
        if sum(len(C)*b for C,b in zip(cycles,select))!=k:
            continue
        if any((not b) and sum(bool(aa&(1<<i)) for i in C)%2 for C,b in zip(cycles,select)):
            continue
        expo=sum((len(C)-1)+sum(bool(aa&(1<<i)) for i in C) for C,b in zip(cycles,select) if b)
        out+=(-1)**expo * (2**sum(not b for b in select))
    return out


def cubical_model_check(n):
    """Independently reconstruct every square and the equivariant vertex map."""
    N=1<<n
    Z=residual_faces(n)
    def mapped(p):
        if p<N:
            return p|((1-bitpar(p))<<n)
        v=p-N
        return v|(bitpar(v)<<n)
    square_diagonals={}
    for r,z in combinations(range(N),2):
        shared=[v for v in range(N) if r in cube_neighbors(v,n) and z in cube_neighbors(v,n)]
        if len(shared)==2:
            vertices={mapped(r),mapped(z),mapped(N+shared[0]),mapped(N+shared[1])}
            assert len(vertices)==4 and all((q^t).bit_count()==2 for q,t in combinations(sorted(vertices),2) if (q^t).bit_count()!=1)
            varying=0
            for b in range(n+1):
                if len({(v>>b)&1 for v in vertices})>1:
                    varying|=1<<b
            assert varying.bit_count()==2
            base=min(vertices)
            assert vertices=={base,base^(varying&-varying),base^(varying^(varying&-varying)),base^varying}
            square_diagonals[(r,z)]=frozenset(vertices)
            assert (r,z) in Z
            assert tuple(sorted((r,z,N+shared[0]))) in Z
            assert tuple(sorted((r,z,N+shared[1]))) in Z
        else:
            assert (r,z) not in Z
    all_squares=set(square_diagonals.values())
    expected=set()
    for inds in combinations(range(n+1),2):
        varying=sum(1<<i for i in inds)
        for base in range(1<<(n+1)):
            if base&varying: continue
            expected.add(frozenset((base,base^(1<<inds[0]),base^(1<<inds[1]),base^varying)))
    assert all_squares==expected
    assert len(square_diagonals)==len(expected)==(1<<(n-1))*comb(n+1,2)
    assert len([f for f in Z if len(f)==3])==2*len(expected)
    return len(expected)


def equivariant_map_check(n,perm,a):
    N=1<<n
    bigperm=perm+(n,)
    aa=a|(bitpar(a)<<n)
    for v in range(N):
        old_c=v|(bitpar(v)<<n)
        new_c=perm_apply(perm_apply(v,perm,a),tuple(range(n)),0)
        new_c|=bitpar(new_c)<<n
        assert perm_apply(old_c,bigperm,aa)==new_c
        old_r=v|((1-bitpar(v))<<n)
        new_r=perm_apply(v,perm,a)
        new_r|=(1-bitpar(new_r))<<n
        assert perm_apply(old_r,bigperm,aa)==new_r



def fixed_complex_of_three_cycle(n):
    """Independent orbit-barycenter triangulation of geometric C3 fixed points."""
    assert n>=3
    perm=(1,2,0)+tuple(range(3,n))
    N=1<<n
    seen=set();orbits=[];orbit_id={}
    for v in range(N):
        if v in seen:continue
        O=tuple(sorted({v,perm_apply(v,perm,0),perm_apply(perm_apply(v,perm,0),perm,0)}))
        seen.update(O)
        ix=len(orbits)
        orbits.append(O)
        for x in O:orbit_id[x]=ix
    actual=cech_faces(n)
    fixed_faces=set()
    for face in actual:
        if {perm_apply(v,perm,0) for v in face}==set(face):
            fixed_faces.add(tuple(sorted({orbit_id[v] for v in face})))
    assert all(all(tuple(sorted(set(f)-{v})) in fixed_faces for v in f) for f in fixed_faces if len(f)>1)
    degree={}
    for f in fixed_faces:degree.setdefault(len(f)-1,[]).append(f)
    dims=sorted(degree)
    ranks={}
    for k in dims:
        if k==0:
            ranks[k]=0
            continue
        rows={f:i for i,f in enumerate(degree[k-1])}
        pivots={}
        rank=0
        for face in degree[k]:
            col=0
            for i in range(len(face)):
                sub=tuple(face[:i]+face[i+1:])
                col^=1<<rows[sub]
            while col:
                j=col.bit_length()-1
                if j in pivots:col^=pivots[j]
                else:pivots[j]=col;rank+=1;break
        ranks[k]=rank
    # Unreduced Betti numbers over F2: dim Ck - rank d_k - rank d_(k+1).
    b={k:len(degree[k])-ranks.get(k,0)-ranks.get(k+1,0) for k in dims}
    assert b.get(0)==2
    assert b.get(1,0)==0
    if n<5:
        assert b.get(2,0)==0
    if n==5:
        assert b.get(2,0)==2
    return b,tuple(len(degree[k]) for k in dims)

def main():
    checks=0
    for n in range(1,5):
        npairs,zfaces=verify_collapse(n)
        nsquares=cubical_model_check(n)
        X=cech_faces(n)
        auto=0
        for perm in permutations(range(n)):
            for a in range(1<<n):
                equivariant_map_check(n,perm,a)
                L=face_lefschetz(n,perm,a,X)
                F=[cubical_trace(n,perm,a,k) for k in range(3)]
                assert F==[cycle_formula(n,perm,a,k) for k in range(3)]
                assert L==F[0]-F[1]+F[2],(n,perm,a,L,F)
                auto+=1
                checks+=1
        beta=2**(n-2)*(n*n-3*n+4)-1 if n>=2 else 0
        assert (len(X) and sum((-1)**(len(f)-1) for f in X)-1)==beta
        print(f'n={n} collapse_pairs={npairs} residual_faces={zfaces} squares={nsquares} aut_cases={auto} top_betti={beta}')
    for k in (3,4,5):
        b,fv=fixed_complex_of_three_cycle(k)
        print(f"three_cycle_fixed_n={k} face_vector={fv} betti_F2={b}")
    # independent nontrivial sample in fifth dimension (non-exhaustive)
    n=5
    npairs,zfaces=verify_collapse(n)
    nsquares=cubical_model_check(n)
    X=cech_faces(n)
    chosen=[(tuple(range(n)),a) for a in range(1<<n)]
    chosen += [(tuple(reversed(range(n))),a) for a in range(0,1<<n,3)]
    chosen += [(tuple((i+1)%n for i in range(n)),a) for a in range(0,1<<n,5)]
    for perm,a in chosen:
        equivariant_map_check(n,perm,a)
        L=face_lefschetz(n,perm,a,X)
        F=[cubical_trace(n,perm,a,k) for k in range(3)]
        assert F==[cycle_formula(n,perm,a,k) for k in range(3)]
        assert L==F[0]-F[1]+F[2]
        checks+=1
    print(f'n=5 collapse_pairs={npairs} residual_faces={zfaces} squares={nsquares} sampled_aut_cases={len(chosen)} top_betti=111')
    print(f'VERIFY_OK total_automorphism_cases={checks}')

if __name__=='__main__':
    main()
