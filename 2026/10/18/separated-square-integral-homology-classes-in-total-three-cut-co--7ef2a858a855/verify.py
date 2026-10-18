#!/usr/bin/env python3
"""Reproduce finite checks for separated-square classes in robust clique complexes.
No external packages are required. The all-parameter result is proved in RESULT.md.
"""
import itertools
from collections import defaultdict


def adjacent(m, n, u, v):
    a, i = divmod(u, n)
    b, j = divmod(v, n)
    return (i == j and a != b) or (a == b and abs(i-j) == 1)


def allowed(m, n, vertices):
    for a,b,c in itertools.combinations(vertices, 3):
        if not (adjacent(m,n,a,b) or adjacent(m,n,a,c) or adjacent(m,n,b,c)):
            return False
    return True


def edge_chain(u,v):
    return {(min(u,v),max(u,v)): (1 if u<v else -1)}


def square_chain(m,n,i,a):
    vertices=[i, a*n+i, a*n+i+1, i+1]
    z=defaultdict(int)
    for k in range(4):
        for e,c in edge_chain(vertices[k],vertices[(k+1)%4]).items():z[e]+=c
    return {s:c for s,c in z.items() if c}


def parity(seq):
    return -1 if sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))%2 else 1


def product(m,n,i,j,a,b):
    x=square_chain(m,n,i,a)
    y=square_chain(m,n,j,b)
    out=defaultdict(int)
    for e,ce in x.items():
        for f,cf in y.items():
            assert len(set(e+f))==4
            t=e+f
            assert allowed(m,n,t)
            out[tuple(sorted(t))]+=ce*cf*parity(t)
    return {s:c for s,c in out.items() if c}


def boundary(chain):
    out=defaultdict(int)
    for s,c in chain.items():
        for k in range(len(s)):
            t=s[:k]+s[k+1:]
            out[t]+=c*(-1)**k
    return {s:c for s,c in out.items() if c}


def facet(m,n,i,j,a,b):
    return tuple(sorted([a*n+i,a*n+i+1,b*n+j,b*n+j+1]))


def check_case(m,n):
    labels=[(i,j,a,b) for i in range(n-1) for j in range(i+2,n-1)
            for a in range(1,m) for b in range(1,m)]
    expect=(m-1)**2*(n-2)*(n-3)//2
    assert len(labels)==expect
    cofaces=[]
    chains=[]
    for (i,j,a,b) in labels:
        f=facet(m,n,i,j,a,b)
        assert allowed(m,n,f)
        bad=[w for w in range(m*n) if w not in f and allowed(m,n,f+(w,))]
        assert bad==[],(m,n,i,j,a,b,bad)
        z=product(m,n,i,j,a,b)
        assert len(z)==16,(m,n,i,j,a,b,len(z))
        assert not boundary(z),(m,n,i,j,a,b)
        assert abs(z.get(f,0))==1
        chains.append(z)
        cofaces.append(f)
    for t, z in enumerate(chains):
        for s, f in enumerate(cofaces):
            coefficient=z.get(f,0)
            assert coefficient==(z.get(cofaces[t],0) if s==t else 0),(m,n,t,s,coefficient)
    print(f'm={m}, n={n}: {len(labels)} independent integral cycle/cochain pairs; all facets maximal; signed boundaries zero; evaluation diagonal unimodular',flush=True)


def full_mod2_rank(m,n):
    import functools
    N=m*n
    forb=[]
    for u,v,w in itertools.combinations(range(N),3):
        if not (adjacent(m,n,u,v) or adjacent(m,n,u,w) or adjacent(m,n,v,w)):
            forb.append((1<<u)|(1<<v)|(1<<w))
    faces={}
    for mask in range(1<<N):
        if any(mask&t==t for t in forb): continue
        faces.setdefault(mask.bit_count(), []).append(mask)
    def rank_boundary(k):
        rows={x:i for i,x in enumerate(faces[k])}
        piv={}
        for x in faces.get(k+1,[]):
            col=0
            for i in range(N):
                if x & (1<<i):col^=1<<rows[x^(1<<i)]
            while col:
                j=col.bit_length()-1
                if j in piv:col^=piv[j]
                else:piv[j]=col;break
        return len(piv)
    r3=rank_boundary(3)
    r4=rank_boundary(4)
    betti3=len(faces[4])-r3-r4
    print(f'  Full GF(2) H_3 for m={m},n={n}: rank={betti3}; total {sum(map(len,faces.values()))} augmented faces',flush=True)
    assert betti3>=((m-1)**2*(n-2)*(n-3)//2)


def main():
    for m,n in [(3,4),(3,5),(3,6),(4,4),(4,5),(5,4),(5,6)]:
        check_case(m,n)
    for m,n in [(3,4),(3,5),(3,6),(4,4),(4,5),(5,4)]:
        full_mod2_rank(m,n)
    print('All finite checks passed. The general proof is in RESULT.md.')

if __name__=='__main__':main()
