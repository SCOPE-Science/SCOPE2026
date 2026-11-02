"""Standalone independent finite checker of clique-corona fort and zero forcing transformations.
This file performs direct adjacency-based tests and polynomial comparisons for small graphs.
"""
from itertools import combinations
from collections import Counter
from math import comb


def simple_graph(n, edge_bits):
    edges=list(combinations(range(n),2))
    a=[0]*n
    for j,(u,v) in enumerate(edges):
        if (edge_bits>>j)&1:
            a[u] |=1<<v
            a[v] |=1<<u
    return a


def clique_corona(a, sizes):
    n=len(a)
    a=list(a)+[0]*sum(sizes)
    off=n
    for v,r in enumerate(sizes):
        verts=[v]+list(range(off,off+r))
        for i,u in enumerate(verts):
            for w in verts[i+1:]:
                a[u] |= 1<<w
                a[w] |= 1<<u
        off+=r
    return a


def is_fort(mask, adj):
    if not mask:
        return False
    for v,av in enumerate(adj):
        if not ((mask>>v)&1) and (av&mask).bit_count()==1:
            return False
    return True


def is_zf(mask,adj):
    all_= (1<<len(adj))-1
    while True:
        if mask==all_:
            return True
        added=0
        for i,neigh in enumerate(adj):
            if (mask>>i)&1:
                avail=neigh &~mask
                if avail and avail&(avail-1)==0:
                    added |=avail
        if added==0:
            return False
        mask |=added


def direct(a):
    n=len(a)
    z=Counter()
    forts=[]
    for s in range(1<<n):
        if is_zf(s,a):
            z[s.bit_count()]+=1
        if is_fort(s,a):
            forts.append(s)
    min_f=[]
    for s in sorted(forts,key=lambda s:s.bit_count()):
        if not any((f&s)==f for f in min_f):
            min_f.append(s)
    f=Counter(s.bit_count() for s in min_f)
    return z,f,min_f


def predict_uniform_z(z,n,r):
    # (r*z^(r-1))^n Z_G(z*(z+r+1)/r)
    poly=Counter()
    for t,coeff in z.items():
        for j in range(t+1):
            degree=n*(r-1)+t+j
            poly[degree]+=coeff*comb(t,j)*pow(r,n-t)*pow(r+1,t-j)
    return poly


def predict_fort(f,n,r):
    out=Counter({2:n*comb(r,2)})
    for t,c in f.items():
        out[2*t]+=c*pow(r,t)
    return out


def predict_mixed_z(z_graph_n, base_zsets, sizes):
    # sum over base ZF T of prod local factors
    # factor for v in T: z^r(z+r+1); else: r z^(r-1)
    n=len(sizes)
    poly=Counter()
    for T in base_zsets:
        p=Counter({0:1})
        for v,r in enumerate(sizes):
            local=Counter({r-1:r}) if not ((T>>v)&1) else Counter({r:r+1,r+1:1})
            p=multiply(p,local)
        poly.update(p)
    return poly


def multiply(a,b):
    result=Counter()
    for i,c in a.items():
        for j,d in b.items():
            result[i+j]+=c*d
    return result


def check():
    tested=0
    tested_masks=0
    for n in (1,2,3,4):
        for ebits in range(1<<comb(n,2)):
            base=simple_graph(n,ebits)
            bz,bf,_=direct(base)
            for r in ([2,3] if n<=3 else [2]):
                H=clique_corona(base,[r]*n)
                hz,hf,_=direct(H)
                assert hz==predict_uniform_z(bz,n,r), ('zero forcing uniform',n,ebits,r,hz,predict_uniform_z(bz,n,r))
                assert hf==predict_fort(bf,n,r), ('minimal forts',n,ebits,r,hf,predict_fort(bf,n,r))
                tested+=1; tested_masks+=1<<len(H)
            if n<=3:
                # heterogeneous cliques, independent direct test
                sizes=tuple(2+(v%2) for v in range(n))
                H=clique_corona(base,sizes)
                hz,hf,_=direct(H)
                valid_T=[T for T in range(1<<n) if is_zf(T,base)]
                assert hz==predict_mixed_z(bz,valid_T,sizes), ('zero forcing mixed',n,ebits,sizes)
                expected_f=Counter({2:sum(comb(r,2) for r in sizes)})
                for A in range(1<<n):
                    if is_fort(A,base) and all(not is_fort(B,base) for B in range(1<<n) if B!=A and B&A==B):
                        ways=1
                        for v,r in enumerate(sizes):
                            if (A>>v)&1: ways*=r
                        expected_f[2*A.bit_count()]+=ways
                assert hf==expected_f, ('minimal forts mixed',n,ebits,sizes,hf,expected_f)
                tested+=1; tested_masks+=1<<len(H)
    # independent larger-base spot checks
    n=5
    for ebits in (0,1,3,15,127,512,1023):
        base=simple_graph(n,ebits)
        bz,bf,_=direct(base)
        H=clique_corona(base,[2]*n)
        hz,hf,_=direct(H)
        assert hz==predict_uniform_z(bz,n,2)
        assert hf==predict_fort(bf,n,2)
        tested+=1;tested_masks+=1<<len(H)
    print(f'VERIFY_OK: {tested} graph-corona instances, {tested_masks} direct vertex subsets; uniform and mixed clique sizes; all zero-forcing coefficients and all minimal-fort coefficients')

if __name__=='__main__':
    check()
