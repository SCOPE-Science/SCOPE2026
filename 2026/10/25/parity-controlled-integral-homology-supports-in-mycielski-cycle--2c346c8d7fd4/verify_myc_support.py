#!/usr/bin/env python3
"""Independent finite checks of a parity-support theorem for ordinary Mycielski-cycle neighborhood complexes.
All combinatorial and boundary calculations are constructed from the graph definition, without external packages.
Finite checks illustrate but do not replace the all-n proof in RESULT.md.
"""
from itertools import combinations


def rank_gf2(vectors):
    piv = {}
    for v in vectors:
        while v:
            top = v.bit_length()-1
            if top not in piv:
                piv[top]=v
                break
            v ^= piv[top]
    return len(piv)


def make(n):
    V = 2*n+1
    edges=set()
    def edge(a,b): edges.add(tuple(sorted((a,b))))
    for i in range(n):
        edge(i,(i+1)%n)
        edge(n+i,2*n)
        edge(i,n+(i-1)%n)
        edge(i,n+(i+1)%n)
    neigh=[set() for _ in range(V)]
    for a,b in edges:
        neigh[a].add(b)
        neigh[b].add(a)
    faces={k:set() for k in (1,2,3,4)}
    for fac in neigh:
        for k in faces:
            if k<=len(fac):faces[k].update(combinations(sorted(fac),k))
    faces={k:sorted(f) for k,f in faces.items()}
    ix={k:{f:j for j,f in enumerate(faces[k])} for k in faces}
    d={k:[] for k in (2,3,4)}
    for k in d:
        for fac in faces[k]:
            d[k].append(sum(1<<ix[k-1][fac[:i]+fac[i+1:]] for i in range(k)))
    return faces,d,V


def full_homology(faces,d,V,mask):
    indices={k:[i for i,f in enumerate(faces[k]) if all(mask>>x&1 for x in f)] for k in faces}
    boundary_rank={k:rank_gf2([d[k][i] for i in indices[k]]) for k in (2,3,4)}
    return (len(indices[1])-boundary_rank[2]-1,
            len(indices[2])-boundary_rank[2]-boundary_rank[3],
            len(indices[3])-boundary_rank[3]-boundary_rank[4])


def image_H2_dim(faces,d,mask,global_b3):
    # Track each dependence among boundary-2 columns as a cycle in global C_2.
    cols={};subspace={}
    for i,f in enumerate(faces[3]):
        if not all(mask>>x&1 for x in f):continue
        v=d[3][i]; chain=1<<i
        while v:
            p=v.bit_length()-1
            if p not in cols:break
            vv,cc=cols[p];v^=vv;chain^=cc
        if v:
            cols[v.bit_length()-1]=(v,chain)
        else:
            z=chain
            while z and (p:=z.bit_length()-1) in global_b3:
                z^=global_b3[p]
            while z and (p:=z.bit_length()-1) in subspace:
                z^=subspace[p]
            if z:subspace[z.bit_length()-1]=z
    return len(subspace)


def test(n, exhaustive=False):
    faces,d,V=make(n)
    allmask=(1<<V)-1
    def h(mask):return full_homology(faces,d,V,mask)
    expect=(0,0,1) if n%2 else (0,1,2)
    assert h(allmask)==expect,(n,'full',h(allmask),expect)
    for vertex in range(V):
        betti=h(allmask^(1<<vertex))
        if vertex==2*n: expected=(0,0,0)
        elif n%2: expected=(0,0,0)
        else:expected=(0,1,1)
        assert betti==expected,(n,'deletion',vertex,betti,expected)
    base={}
    for i,v in enumerate(d[4]):
        while v:
            j=v.bit_length()-1
            if j not in base:base[j]=v;break
            v^=base[j]
    assert len(base)==len(faces[3])-rank_gf2(d[3])-(1 if n%2 else 2)
    if n%2==0:
        patterns=[]
        for parity in (0,1):
            bits=[2*n]+[i for i in range(n) if i%2==parity]+[n+i for i in range(n) if i%2==parity]
            mask=sum(1<<i for i in bits)
            patterns.append(mask)
            assert h(mask)==(0,0,1),(n,'parity subcomplex',parity,h(mask))
            assert image_H2_dim(faces,d,mask,base)==1
    if exhaustive:
        for mask in range(1,1<<V):
            actual=image_H2_dim(faces,d,mask,base)
            expected=1 if n%2 and mask==allmask else (sum((mask&pattern)==pattern for pattern in patterns) if n%2==0 else 0)
            assert actual==expected,(n,'support mismatch',mask,actual,expected)
    print('n',n,'vertices',V,'full_reduced_betti_1_2',expect[1:],
          'vertex_deletions', 'contractible_homology' if n%2 else 'H1=H2=Z except apex',
          'exhaustive_support_check',exhaustive)


if __name__=='__main__':
    for n in range(5,12):test(n,exhaustive=(n in (5,6)))
    print('VERIFY_OK_MYC_CYCLE_SUPPORT_PARITY')
