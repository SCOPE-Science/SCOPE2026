"""Exact integral and symmetry checks for low-degree graph magnitude chains.
Publicly reproducible computations use no network and no external scientific data.
"""
import itertools
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
from collections import Counter

def plane_fano():
    V=list(range(14)); adj={v:set() for v in V}
    for p in range(1,8):
        for l in range(1,8):
            if (p&l).bit_count()%2==0:
                adj[p-1].add(6+l);adj[6+l].add(p-1)
    dist={}
    for x in V:
        ds={x:0};queue=[x]
        for y in queue:
            for z in adj[y]:
                if z not in ds:ds[z]=ds[y]+1;queue.append(z)
        assert len(ds)==14
        dist[x]=ds
    assert all(len(adj[i])==3 for i in V)
    return V,adj,dist

def endpoint_complex(V,dist,a,z):
    groups={};index={}
    for k in (2,3,4):
        chains=[]
        def rec(seq,length):
            if len(seq)==k+1:
                if length==4 and seq[-1]==z:chains.append(tuple(seq))
                return
            for v in V:
                if v==seq[-1]:continue
                s=length+dist[seq[-1]][v]
                if s<=4 and s+(k-len(seq))<=4: rec(seq+[v],s)
        rec([a],0)
        groups[k]=chains; index[k]={p:i for i,p in enumerate(chains)}
    D={}
    for k in (3,4):
        A=sp.zeros(len(groups[k-1]),len(groups[k]))
        for j,p in enumerate(groups[k]):
            for i in range(1,k):
                if dist[p[i-1]][p[i]]+dist[p[i]][p[i+1]]==dist[p[i-1]][p[i+1]]:
                    A[index[k-1][p[:i]+p[i+1:]],j]+=(-1)**i
        D[k]=A
    assert D[3]*D[4]==sp.zeros(len(groups[2]),len(groups[4]))
    return groups,index,D

def snf_ones(A):
    S=smith_normal_form(A,domain=ZZ)
    d=[abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]]
    return len(d),Counter(d)

def test_equal():
    V,adj,dist=plane_fano();a=0
    groups,idx,D=endpoint_complex(V,dist,a,a)
    print('equal C sizes',*(len(groups[k]) for k in (2,3,4)), flush=True)
    r3,d3=snf_ones(D[3]);r4,d4=snf_ones(D[4]);print('ranks',r3,r4,'SNF3',d3,'SNF4',d4,flush=True)
    assert r3+r4==len(groups[3]) and set(d4)=={1} and set(d3)=={1}
    print('EQUAL_ENDPOINT_INTEGRAL_H3_VANISHES',flush=True)

def sixcycle_class(V,adj,dist,a,z,R):
    assert a!=z and dist[a][z]==2 and dist[a][R]==dist[z][R]==2
    B=next(iter(adj[a]&adj[z]))
    A=next(iter(adj[a]&adj[R]))
    C=next(iter(adj[R]&adj[z]))
    assert len({A,B,C})==3
    return {(a,A,C,z):1,(a,A,a,z):-1,(a,B,C,z):-1}

def test_distinct():
    V,adj,dist=plane_fano()
    a,z=0,next(z for z in V if dist[0][z]==2)
    gs,idx,D=endpoint_complex(V,dist,a,z)
    outside=[R for R in V if 0<=R<7 and R!=a and R!=z and next(iter(adj[a]&adj[z])) not in adj[R]]
    assert len(outside)==4
    Z=sp.zeros(len(gs[3]),len(outside))
    for j,R in enumerate(outside):
        for p,v in sixcycle_class(V,adj,dist,a,z,R).items():Z[idx[3][p],j]=v
    assert D[3]*Z==sp.zeros(len(gs[2]),len(outside))
    r3,d3=snf_ones(D[3]);r4,d4=snf_ones(D[4]);rz,dz=snf_ones(D[4].row_join(Z))
    print('distinct C sizes',*(len(gs[k]) for k in (2,3,4)),'ranks',r3,r4,rz,'SNF',d3,d4,dz,flush=True)
    assert r3+r4+4==len(gs[3]) and rz==r4+4 and set(d4)=={1} and set(dz)=={1}
    print('FOUR_HEXAGON_CLASSES_INTEGRAL_BASIS',flush=True)

if __name__=='__main__':
    test_equal();test_distinct()

def test_full_group_and_naturality():
    V,adj,dist=plane_fano()
    from itertools import permutations
    def point_map(bits,p):
        v=[(p>>j)&1 for j in range(3)]
        out=0
        for i in range(3):
            if sum(((bits>>(3*i+j))&1)*v[j] for j in range(3))%2:out|=(1<<i)
        return out
    automorphisms=[]
    ordered_noncollinear=[(p,q,r) for p,q,r in itertools.permutations(range(1,8),3) if p^q^r!=0]
    assert len(ordered_noncollinear)==168
    for bits in range(512):
        pp={p:point_map(bits,p) for p in range(1,8)}
        if len(set(pp.values()))!=7:continue
        ll={}
        for l in range(1,8):
            image={pp[p] for p in range(1,8) if (p&l).bit_count()%2==0}
            choices=[t for t in range(1,8) if {p for p in range(1,8) if (p&t).bit_count()%2==0}==image]
            assert len(choices)==1
            ll[l]=choices[0]
        perm={p-1:pp[p]-1 for p in range(1,8)}
        perm.update({6+l:6+ll[l] for l in range(1,8)})
        assert all({perm[b] for b in adj[a]}==adj[perm[a]] for a in V)
        automorphisms.append((pp,ll,perm))
    assert len(automorphisms)==168
    assert {tuple(pp[p] for p in (1,2,4)) for pp,_,_ in automorphisms}==set(ordered_noncollinear)
    for pp,ll,perm in automorphisms:
        a,z,R=(0,1,3)
        lhs={tuple(perm[t] for t in simplex):coeff for simplex,coeff in sixcycle_class(V,adj,dist,a,z,R).items()}
        rhs=sixcycle_class(V,adj,dist,perm[a],perm[z],perm[R])
        assert lhs==rhs
    # Fano polarity exchanges point and line labels with the same nonzero vector.
    dual={p-1:6+p for p in range(1,8)}
    dual.update({6+p:p-1 for p in range(1,8)})
    assert all({dual[b] for b in adj[a]}==adj[dual[a]] for a in V)
    a,z,R=(0,1,3)
    lhs={tuple(dual[t] for t in simplex):c for simplex,c in sixcycle_class(V,adj,dist,a,z,R).items()}
    assert lhs==sixcycle_class(V,adj,dist,dual[a],dual[z],dual[R])
    print('FANO_336_FULL_AUTOMORPHISMS_REGULAR_ON_HEXAGON_BASIS_VERIFIED', flush=True)

if __name__=='__main__':
    test_full_group_and_naturality()
