#!/usr/bin/env python3
"""Exact supplementary checks for Moran-Geary network ranking classification.
Only Python's standard library is required. Graphs are unweighted, simple, connected.
"""
from fractions import Fraction
from itertools import combinations


def indices(n, edges, values):
    assert len(values) == n and len(set(values)) > 1
    m = len(edges)
    mean = Fraction(sum(values), n)
    z = [Fraction(a) - mean for a in values]
    norm = sum(t*t for t in z)
    prod = 2*sum(z[u]*z[v] for u,v in edges)
    energy = sum((z[u]-z[v])**2 for u,v in edges)
    return Fraction(n, 2*m)*prod/norm, Fraction(n-1, 2*m)*energy/norm


def connected(n, edges):
    adj = [set() for _ in range(n)]
    for u,v in edges:
        adj[u].add(v); adj[v].add(u)
    reached={0}; pending=[0]
    while pending:
        u=pending.pop()
        for v in adj[u]-reached:
            reached.add(v);pending.append(v)
    return len(reached)==n


def graph_types(n, edges):
    ds=[0]*n
    for u,v in edges: ds[u]+=1;ds[v]+=1
    regular=len(set(ds))==1
    star=sorted(ds)==[1]*(n-1)+[n-1]
    return ds,regular or star


def affine_via_independent_quadratic_form(n, edges, ds):
    """Check D|_{1perp} in span(I|_{1perp},A|_{1perp})."""
    links={tuple(sorted(e)) for e in edges}
    def a(u,v): return int(tuple(sorted((u,v))) in links) if u!=v else 0
    entries=[]
    for i in range(n-1):
        for j in range(i,n-1):
            gram=int(i==j)+1
            adj=a(i,j)-a(i,n-1)-a(j,n-1)
            degree=(ds[i] if i==j else 0)+ds[n-1]
            entries.append((Fraction(gram),Fraction(adj),Fraction(degree)))
    pair=None
    for t in range(len(entries)):
        for u in range(t+1,len(entries)):
            p,q,_=entries[t];r,s,_=entries[u]
            det=p*s-q*r
            if det:
                pair=(t,u,det);break
        if pair:break
    if pair is None:
        return all(h*entries[0][2]==entries[0][0]*d for h,_,d in entries)
    t,u,det=pair
    p,q,w=entries[t];r,s,v=entries[u]
    alpha=(w*s-q*v)/det
    beta=(p*v-w*r)/det
    return all(d==alpha*h+beta*a for h,a,d in entries)


def main():
    path=((0,1),(1,2),(2,3))
    x=(1,1,4,2); y=(1,2,1,4)
    assert sum(x)==sum(y)==8
    assert sum(t*t for t in x)==sum(t*t for t in y)==22
    assert indices(4,path,x)==(Fraction(-2,9),Fraction(13,12))
    assert indices(4,path,y)==(Fraction(-4,9),Fraction(11,12))
    assert indices(4,path,x)[0]>indices(4,path,y)[0]
    assert indices(4,path,x)[1]>indices(4,path,y)[1]

    counts=[]
    for n in range(2,7):
        pairs=list(combinations(range(n),2))
        total=matched=0
        for mask in range(1,1<<len(pairs)):
            edges=tuple(pairs[k] for k in range(len(pairs)) if mask>>k&1)
            if not connected(n,edges):continue
            total+=1
            ds,predicted=graph_types(n,edges)
            measured=affine_via_independent_quadratic_form(n,edges,ds)
            assert measured==predicted,(n,edges,ds,measured,predicted)
            matched+=int(measured)
        counts.append((n,total,matched))

    for n in range(3,10):
        star=tuple((0,i) for i in range(1,n))
        vec=tuple((3*i*i+2*i+1)%19+1 for i in range(n))
        I,C=indices(n,star,vec)
        assert C==Fraction(1,2)-Fraction(n-1,2)*I
        cycle=tuple((i,(i+1)%n) for i in range(n))
        I,C=indices(n,cycle,vec)
        assert C==Fraction(n-1,n)*(1-I)
    print('VERIFY_OK', 'witness_P4=2', 'equal_mean_variance=1',
          'connected_graph_census='+repr(counts),'star_cycle_identities=14')

if __name__=='__main__':main()
