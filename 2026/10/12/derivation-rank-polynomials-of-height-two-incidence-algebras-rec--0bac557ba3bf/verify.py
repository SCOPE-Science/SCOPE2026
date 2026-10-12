#!/usr/bin/env python3
"""Direct finite checks for derivation rank enumerators of height-two incidence algebras.

Run: python3 verify.py
Python standard library only.
"""
from itertools import product
from collections import Counter
from math import comb


def rank_mod(matrix, q):
    a = [list(row) for row in matrix]
    nr = len(a)
    if nr == 0:
        return 0
    nc = len(a[0]); r = 0
    assert q in (2,3,5)
    for c in range(nc):
        pivot = next((i for i in range(r,nr) if a[i][c] % q),None)
        if pivot is None: continue
        a[r],a[pivot] = a[pivot],a[r]
        inv=pow(a[r][c] % q, -1, q)
        a[r]=[(v*inv)%q for v in a[r]]
        for i in range(nr):
            if i!=r and a[i][c]:
                h=a[i][c];a[i]=[(v-h*w)%q for v,w in zip(a[i],a[r])]
        r+=1
        if r==nr: break
    return r


def components(n,edges):
    par=list(range(n))
    def root(i):
        while par[i]!=i:i=par[i]
        return i
    for u,v in edges:
        ru,rv=root(u),root(v)
        par[ru]=rv
    return len({root(i) for i in range(n)})


def direct_matrix(n,edges,b,l,q):
    m=len(edges);d=n+m
    M=[[0]*d for _ in range(d)]
    for h,(s,t) in enumerate(edges):
        M[n+h][s]=(-b[h])%q
        M[n+h][t]=b[h]%q
        M[n+h][n+h]=l[h]%q
    return M


def expected_rank(n,edges,b,l):
    L=[j for j,v in enumerate(l) if v]
    U=[edges[j] for j in range(len(edges)) if b[j] and not l[j]]
    return len(L)+n-components(n,U)


def model_enumerator(n,edges,q):
    m=len(edges); freq=Counter()
    for z in product(range(q),repeat=2*m):
        b,l=z[:m],z[m:]
        rr=rank_mod(direct_matrix(n,edges,b,l,q),q)
        assert rr==expected_rank(n,edges,b,l)
        freq[rr]+=1
    return freq


def graph_formula(n,edges,q):
    m=len(edges)
    result=Counter()
    for labels in product(range(3),repeat=m):
        # state 0: beta=lambda=0; 1: lambda!=0, beta arbitrary; 2: lambda=0, beta!=0
        L=[i for i,t in enumerate(labels) if t==1]
        U=[edges[i] for i,t in enumerate(labels) if t==2]
        rank=len(L)+n-components(n,U)
        result[rank]+=(q*(q-1))**len(L)*(q-1)**len(U)
    return result


def cycle_formula(m,q):
    out=Counter({j:comb(m,j)*(q*q-1)**j for j in range(m+1)})
    out[m-1]+=(q-1)**m
    out[m]-=(q-1)**m
    return out


def multiplication(n,edges):
    m=len(edges);d=n+m
    p=[[None]*d for _ in range(d)]
    for i in range(n):p[i][i]=i
    for j,(s,t) in enumerate(edges):
        p[s][n+j]=n+j
        p[n+j][t]=n+j
    return p


def derivation_space_dimension(n,edges,q):
    mult=multiplication(n,edges)
    d=len(mult);N=d*d
    eq=[]
    for i in range(d):
        for j in range(d):
            for k in range(d):
                row=[0]*N
                h=mult[i][j]
                if h is not None:row[h*d+k]+=1
                for t in range(d):
                    if mult[t][j]==k:row[i*d+t]-=1
                    if mult[i][t]==k:row[j*d+t]-=1
                if any(row):eq.append(row)
    return N-rank_mod(eq,q)


def check():
    cycle4=[(0,2),(1,2),(1,3),(0,3)]
    cycle6=[(0,3),(1,3),(1,4),(2,4),(2,5),(0,5)]
    path5=[(0,3),(1,3),(1,4),(2,4)]
    lollipop=cycle4+[(1,4)]
    k23=[(i,j) for i in range(2) for j in range(2,5)]
    for n,E,q in [(4,cycle4,2),(4,cycle4,3),(6,cycle6,2),
                    (5,path5,2),(5,path5,3),(5,lollipop,2),(5,k23,2)]:
        freq=model_enumerator(n,E,q)
        expected=graph_formula(n,E,q)
        assert freq==expected,(n,E,q,freq,expected)
        if E in (cycle4,cycle6):assert freq==cycle_formula(len(E),q)
        assert sum(freq.values())==q**(2*len(E))
        print('CHECK',q,n,len(E),sorted(freq.items()))
    for q in (2,3):
        dim=derivation_space_dimension(4,cycle4,q)
        assert dim==8
        print('DERIVATION_SPACE',q,dim)
    print('VERIFY_OK')
if __name__=='__main__':check()

def shortest_cycles(n,edges):
    # Returns (girth, number of distinct shortest cycles), or (None,0).
    from itertools import combinations
    m=len(edges)
    for g in range(3,m+1):
        count=0
        for J in combinations(range(m),g):
            e=[edges[j] for j in J]
            deg=[0]*n
            for a,b in e:deg[a]+=1;deg[b]+=1
            if any(d not in (0,2) for d in deg):continue
            active={v for v in range(n) if deg[v]==2}
            if len(active)==g and n-components(n,e)==len(active)-1: count+=1
        if count:return g,count
    return None,0

def check_girth():
    graphs=[(4,[(0,2),(1,2),(1,3),(0,3)]),
            (6,[(0,3),(1,3),(1,4),(2,4),(2,5),(0,5)]),
            (5,[(i,j) for i in range(2) for j in range(2,5)]),
            (6,[(i,j) for i in range(3) for j in range(3,6)]),
            (5,[(0,2),(1,2),(1,3),(0,3),(1,4)]),
            (5,[(0,3),(1,3),(1,4),(2,4)])]
    for n,E in graphs:
        m=len(E)
        g,c=shortest_cycles(n,E)
        f=graph_formula(n,E,2)
        baseline=Counter({j:comb(m,j)*3**j for j in range(m+1)})
        ds=[j for j in range(m+1) if f[j]!=baseline[j]]
        if g is None: assert not ds
        else:
            assert ds[0]==g-1 and f[g-1]-baseline[g-1]==c
        print('GIRTH',n,m,g,c,'first_difference',ds[0] if ds else None)
if __name__=='__main__':check_girth()
