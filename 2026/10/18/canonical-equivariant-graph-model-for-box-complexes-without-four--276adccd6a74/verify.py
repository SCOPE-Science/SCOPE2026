#!/usr/bin/env python3
"""Reproducible finite tests for a graph Hom-complex equivalence.
The theorem for all C4-free graphs is proved separately; these checks are finite.
"""
from itertools import combinations
from math import comb
from collections import defaultdict


def cycles(n):
    return n, {(i,(i+1)%n) if i<(i+1)%n else ((i+1)%n,i) for i in range(n)}

def complete(n):
    return n, set(combinations(range(n),2))

def petersen():
    a=list(combinations(range(5),2))
    return 10,{(i,j) for i in range(10) for j in range(i+1,10) if not (set(a[i])&set(a[j]))}

def windmill():
    return 5,{(0,1),(0,2),(1,2),(0,3),(0,4),(3,4)}

def heawood():
    return 14,{(i,7+(i-d)%7) for i in range(7) for d in (0,1,3)}

def neighbors(n,edges):
    nb=[set() for _ in range(n)]
    for a,b in edges:nb[a].add(b);nb[b].add(a)
    return nb

def hom_cells(n,edges):
    nb=neighbors(n,edges)
    bydim=defaultdict(set)
    for v in range(n):
        for side in range(2):
            for r in range(1,len(nb[v])+1):
                for S in combinations(sorted(nb[v]),r):
                    A,B=((v,),S) if side==0 else (S,(v,))
                    bydim[r-1].add((A,B))
    return {d:sorted(c) for d,c in bydim.items()}

def gf2rank(columns):
    piv={}
    for x in columns:
        while x:
            p=x.bit_length()-1
            if p not in piv:
                piv[p]=x;break
            x^=piv[p]
    return len(piv)

def cell_homology(n,edges):
    C=hom_cells(n,edges)
    bd={}
    for d in range(1,max(C)+1):
        idx={c:i for i,c in enumerate(C[d-1])}
        cols=[]
        for A,B in C[d]:
            bits=0
            if len(A)>1:
                for v in A:
                    f=(tuple(x for x in A if x!=v),B)
                    bits^=1<<idx[f]
            if len(B)>1:
                for v in B:
                    f=(A,tuple(x for x in B if x!=v))
                    bits^=1<<idx[f]
            cols.append(bits)
        bd[d]=gf2rank(cols)
    betti=[len(C[d])-bd.get(d,0)-bd.get(d+1,0) for d in range(max(C)+1)]
    return C,betti

def sign_of_perm_tuple(t,perm):
    u=list(map(lambda x:perm[x],t))
    return (-1)**sum(u[i]>u[j] for i in range(len(u)) for j in range(i+1,len(u)))

def trace_hom_complex(C,perm,swap=False):
    traces={}
    for d,cells in C.items():
        total=0
        for A,B in cells:
            X=tuple(sorted(perm[x] for x in A));Y=tuple(sorted(perm[y] for y in B))
            if swap:X,Y=Y,X
            if (X,Y)==(A,B):
                total+=sign_of_perm_tuple(A,perm)*sign_of_perm_tuple(B,perm)
        traces[d]=total
    return sum((-1)**d * x for d,x in traces.items())

def connected_components_of_double(n,edges):
    N=2*n; ad=[set() for _ in range(N)]
    for u,v in edges:
        for i,j in ((u,n+v),(v,n+u)):
            ad[i].add(j);ad[j].add(i)
    comp={};subs=[]
    for z in range(N):
        if z in comp:continue
        st=[z];sub=set()
        while st:
            w=st.pop()
            if w in sub:continue
            sub.add(w)
            st.extend(ad[w]-sub)
        for w in sub:comp[w]=len(subs)
        subs.append(sub)
    return comp,subs

def h0trace(comp,subs,n,perm,swap):
    t=0
    for i,s in enumerate(subs):
        q=next(iter(s))
        v,side=q%n,q//n
        transformed=perm[v]+n*(side^int(swap))
        t+=(comp[transformed]==i)
    return t

def formula(n,edges,perm,swap,conn_h0):
    if swap:
        m=sum(perm[u]==v and perm[v]==u for u,v in edges)
        return conn_h0-2*m
    fix={u for u in range(n) if perm[u]==u}
    return conn_h0+2*sum(u in fix and v in fix for u,v in edges)-2*len(fix)

def verify(n,edges,name,perms):
    assert all(len(e)==2 and e[0]!=e[1] for e in edges)
    nb=neighbors(n,edges)
    assert min(map(len,nb))>=2
    assert not any(len(nb[u]&nb[v])>1 for u in range(n) for v in range(u+1,n)), 'C4 present'
    C,b=cell_homology(n,edges)
    comp,subs=connected_components_of_double(n,edges)
    assert b[0]==len(subs) and b[1]==2*len(edges)-2*n+len(subs)
    assert all(x==0 for x in b[2:])
    for perm in perms:
        assert sorted(perm)==list(range(n))
        assert {tuple(sorted((perm[u],perm[v]))) for u,v in edges}==edges
        for swap in (False,True):
            h0=h0trace(comp,subs,n,perm,swap)
            direct_h1=h0-trace_hom_complex(C,perm,swap)
            assert direct_h1==formula(n,edges,perm,swap,h0), (name,swap,direct_h1)
    print(f'{name}: n={n}, edges={len(edges)}, cells={sum(len(v) for v in C.values())}, hom_betti={b}, double_components={len(subs)}, all_characters_verified={2*len(perms)}')

if __name__=='__main__':
    for n in (5,6,7,8):
        v,e=cycles(n)
        verify(v,e,'cycle'+str(n),[[ (i+k)%n for i in range(n)] for k in range(n)]+[[(k-i)%n for i in range(n)] for k in range(n)])
    n,e=complete(3)
    from itertools import permutations
    verify(n,e,'triangle',[list(x) for x in permutations(range(n))])
    n,e=windmill()
    verify(n,e,'two triangles with common apex',[list(range(n)),[0,2,1,4,3],[0,3,4,1,2]])
    n,e=petersen()
    a=list(combinations(range(5),2));m={x:i for i,x in enumerate(a)}
    perms=[]
    for p in permutations(range(5)):
        perms.append([m[tuple(sorted((p[u],p[v])))] for u,v in a])
    verify(n,e,'Petersen',perms)
    n,e=heawood()
    verify(n,e,'Heawood',[list(range(14)),[(i+1)%7 for i in range(7)]+[7+(i+1)%7 for i in range(7)]])
    print('ALL_TESTS_PASSED')
