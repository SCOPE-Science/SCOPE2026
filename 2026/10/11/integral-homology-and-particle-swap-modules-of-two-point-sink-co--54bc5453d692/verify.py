#!/usr/bin/env python3
"""Exact finite checks of two-particle sink-configuration chain models and symmetry characters."""
from itertools import permutations, product
from math import comb

PRIMES = (2, 3, 5, 7)


def mod_rank(columns, row_count, prime):
    """Rank of a sparse integer column matrix over a prime field."""
    pivots = {}
    for entries in columns:
        v = {i: x % prime for i, x in entries.items() if x % prime}
        while v:
            i = min(v)
            if i not in pivots:
                c = pow(v[i], -1, prime)
                pivots[i] = {j: (c * a) % prime for j, a in v.items() if (c * a) % prime}
                break
            c = v[i]
            for j, a in pivots[i].items():
                t = (v.get(j, 0) - c * a) % prime
                if t: v[j] = t
                else: v.pop(j, None)
    return len(pivots)


def cellular_model(m, n):
    V = m+n
    edges = [(i, m+j) for i in range(m) for j in range(n)]
    E = len(edges)
    c0 = [(u, v) for u in range(V) for v in range(V)]
    c1 = [('e', e, v) for e in range(E) for v in range(V)] + [('v', u, e) for u in range(V) for e in range(E)]
    c2 = [(e, f) for e in range(E) for f in range(E) if e != f]
    idx0 = {v:i for i,v in enumerate(c0)}
    idx1 = {v:i for i,v in enumerate(c1)}
    d1 = []
    for kind, a, b in c1:
        if kind == 'e':
            u, v = edges[a]
            d1.append({idx0[(v,b)]:1,idx0[(u,b)]:-1})
        else:
            u,v = edges[b]
            d1.append({idx0[(a,v)]:1,idx0[(a,u)]:-1})
    d2 = []
    for e,f in c2:
        a,b = edges[e]
        c,d = edges[f]
        d2.append({idx1[('v',b,f)]:1,idx1[('v',a,f)]:-1,
                   idx1[('e',e,d)]:-1,idx1[('e',e,c)]:1})
    for col in d2:
        z = {}
        for i,coeff in col.items():
            for j,a in d1[i].items():z[j] = z.get(j,0) + coeff*a
        assert all(not v for v in z.values()), 'd1*d2 not zero'
    return (V,E,c0,c1,c2,d1,d2)


def graph_cycles(m,n):
    E=[(i,j) for i in range(m) for j in range(n)]
    # Rectangles on row 0/row i, col 0/col j form an integral cycle basis.
    cycles=[]
    for i in range(1,m):
        for j in range(1,n):
            cycles.append([1 if (a,b) in ((0,0),(i,j)) else
                           -1 if (a,b) in ((0,j),(i,0)) else 0 for a,b in E])
    return cycles


def expected_r(m,n):
    if m==n==2: return 1
    if min(m,n)==2:return max(m,n)
    return m*n


def sym2_char(w, w2):return (w*w+w2)//2

def alt2_char(w, w2):return (w*w-w2)//2


def perm2(p):return tuple(p[i] for i in p)


def character_components(m,n,p,q):
    pm=sum(p[i]==i for i in range(m)); pn=sum(q[j]==j for j in range(n))
    pm2=sum(p[p[i]]==i for i in range(m)); pn2=sum(q[q[j]]==j for j in range(n))
    wm=pm-1;wn=pn-1;wm2=pm2-1;wn2=pn2-1
    u=wm*wn
    if m==n==2:
        signm=wm;signn=wn
        return (u, 2*u+signm+signn,0,0)
    if m==2 or n==2:
        if m==2:
            sign=wm; w=wn; w2=wn2; perm=pn
        else:
            sign=wn; w=wm; w2=wm2; perm=pm
        return (u,u+sign*perm,alt2_char(w,w2),sym2_char(w,w2)-perm)
    sm=sym2_char(wm,wm2);sn=sym2_char(wn,wn2)
    am=alt2_char(wm,wm2);an=alt2_char(wn,wn2)
    A_m=sm-pm;A_n=sn-pn
    hplus=am*sn+sm*an
    hminus=A_m*pn+pm*A_n+A_m*A_n+am*an
    return (u,u,hplus,hminus)


def trace_cells(m,n,p,q,swap):
    V=m+n
    g=tuple(p)+tuple(m+q[j] for j in range(n))
    edges=[(i,m+j) for i in range(m) for j in range(n)]
    E=len(edges)
    edge_idx={v:i for i,v in enumerate(edges)}
    ge=[edge_idx[(g[a],g[b])] for a,b in edges]
    if not swap:
        fixV=sum(g[i]==i for i in range(V))
        fixE=sum(ge[i]==i for i in range(E))
        return fixV*fixV,2*fixV*fixE,fixE*(fixE-1)
    fixV2=sum(g[g[i]]==i for i in range(V))
    fixE2=sum(ge[ge[i]]==i for i in range(E))
    fixE=sum(ge[i]==i for i in range(E))
    return fixV2,0,-(fixE2-fixE)


def verify_rep(m,n):
    total=0
    for p,q in product(permutations(range(m)),permutations(range(n))):
        h1p,h1m,h2p,h2m=character_components(m,n,p,q)
        for swap in (False,True):
            t0,t1,t2=trace_cells(m,n,p,q,swap)
            h1=(h1p-h1m) if swap else (h1p+h1m)
            h2=(h2p-h2m) if swap else (h2p+h2m)
            assert t0-t1+t2 == 1-h1+h2,(m,n,p,q,swap,t0,t1,t2,h1,h2)
            total+=1
    return total


def verify_case(m,n):
    V,E,c0,c1,c2,d1,d2=cellular_model(m,n)
    b=(m-1)*(n-1)
    r=expected_r(m,n)
    want=(1,2*b+E-r,b*b-r)
    assert all(x>=0 for x in want)
    found=[]
    for prime in PRIMES:
        rank1=mod_rank(d1,len(c0),prime)
        rank2=mod_rank(d2,len(c1),prime)
        got=(len(c0)-rank1,len(c1)-rank1-rank2,len(c2)-rank2)
        assert got==want,(m,n,prime,got,want)
        found.append((prime,rank1,rank2))
    cycles=graph_cycles(m,n)
    products=[]
    for a in cycles:
        for b_ in cycles:
            products.append({i:a[i]*b_[i] for i in range(E) if a[i]*b_[i]})
    ranks={p:mod_rank(products,E,p) for p in PRIMES}
    assert set(ranks.values())=={r},(m,n,ranks,r)
    assert character_components(m,n,tuple(range(m)),tuple(range(n))) == (
        b,b+E-r,comb(b,2),b*(b+1)//2-r)
    cases=verify_rep(m,n)
    print('K_%d,%d'% (m,n),'cells',(len(c0),len(c1),len(c2)),
          'Betti',want,'r',r,'boundary_ranks',found,'symmetry_cases',cases)


if __name__=='__main__':
    for m,n in ((2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(4,4)):
        verify_case(m,n)
    print('VERIFY_OK')
