#!/usr/bin/env python3
"""Self-contained exact verification of an involution-class separation in graph groups."""
from collections import Counter
from itertools import product
from math import comb

A_EDGES = ((0,1),(0,3),(0,4),(1,3),(1,4),(1,6),(2,4),(2,5))
B_EDGES = ((0,1),(0,2),(0,4),(0,5),(1,2),(2,3),(4,5),(5,6))


def masks(n, edges):
    adj=[0]*n
    for u,v in edges:
        assert 0 <= u < v < n
        adj[u]|=1<<v; adj[v]|=1<<u
    return adj


def count_components(s, adj):
    rem=s; c=0
    while rem:
        c+=1
        front=rem & -rem; rem-=front
        while front:
            bit=front & -front; front-=bit
            i=bit.bit_length()-1
            new=adj[i]&rem
            front|=new; rem-=new
    return c


def histograms(n,edges):
    adj=masks(n,edges)
    full=Counter(); invol=Counter(); independent_size=Counter()
    for s in range(1<<n):
        N=0
        for v in range(n):
            if s>>v&1: N|=adj[v]
        closed=s|N
        rank=closed.bit_count()-count_components(s,adj)
        full[(s.bit_count(),rank)]+=1
        if all(not(adj[v]&s) for v in range(n) if s>>v&1):
            inrank=(N&~s).bit_count()
            invol[(s.bit_count(),inrank)]+=1
            independent_size[s.bit_count()]+=1
    return full,invol,independent_size


def polyn(hist,edgecount):
    P=Counter()
    for (s,r),mult in hist.items():
        for j in range(s+1):
            P[(edgecount-r+j,r)]+=mult*comb(s,j)*(-1)**(s-j)
    return {k:v for k,v in P.items() if v}


def factor_polynomial():
    # q^3(q-1)^2 Y^2(Y-q)^3
    P=Counter()
    for i in range(3):
        for j in range(4):
            P[(3+i+3-j,2+j)]+=comb(2,i)*(-1)**(2-i)*comb(3,j)*(-1)**(3-j)
    return {k:v for k,v in P.items() if v}


def evalpoly(poly,q):
    D=Counter()
    for (i,r),v in poly.items(): D[r]+=v*q**i
    return {r:v for r,v in D.items() if v}


def mul(a,b,q):
    if q==2:return a&b
    if q==4:
        x=0
        while b:
            if b&1:x^=a
            b>>=1
            a<<=1
            if a&4:a^=7
        return x
    raise ValueError('finite field size')


def group_product(x,y,n,edges,q):
    a,c=x; b,d=y
    return (tuple(u^v for u,v in zip(a,b)),
            tuple(c[i]^d[i]^mul(a[u],b[v],q) for i,(u,v) in enumerate(edges)))


def literal_involution_spectrum(n,edges,q):
    e=len(edges)
    z=(0,)*e
    ret=Counter(); num_elements=0
    all_vertices=list(product(range(q),repeat=n))
    for a in all_vertices:
        x=(a,z)
        if group_product(x,x,n,edges,q)[0] != (0,)*n:raise AssertionError('square vector')
        if group_product(x,x,n,edges,q)[1] != z: continue
        num_elements+=q**e
        commuting=0
        for b in all_vertices:
            y=(b,z)
            if group_product(x,y,n,edges,q)==group_product(y,x,n,edges,q):
                commuting+=1
        assert q**n % commuting==0
        orbit=q**n//commuting
        assert q**e % orbit==0
        ret[orbit]+=q**e//orbit
    return dict(ret),num_elements


def expected_from_poly(poly,q):
    return {q**i:num for i,num in evalpoly(poly,q).items()}


def main():
    fa,ia,na=histograms(7,A_EDGES)
    fb,ib,nb=histograms(7,B_EDGES)
    assert sum(fa.values())==sum(fb.values())==128
    assert fa==fb, 'complete class-support histograms differ'
    assert na==nb, 'independence polynomial differs'
    assert ia!=ib, 'involution support histograms should differ'
    assert polyn(fa,8)==polyn(fb,8)
    pa=polyn(ia,8);pb=polyn(ib,8)
    P=Counter(pa);P.subtract(pb)
    assert {k:v for k,v in P.items() if v}==factor_polynomial(), 'factor identity'
    for q in (2,):
        for edges,formula in ((A_EDGES,pa),(B_EDGES,pb)):
            direct,nelt=literal_involution_spectrum(7,edges,q)
            assert direct==expected_from_poly(formula,q),(edges,direct,expected_from_poly(formula,q))
            assert sum(c*s for s,c in direct.items())==nelt
            print('seven vertices q=',q,'class distribution',sorted(direct.items()),'involutions+identity',nelt)
    for n,edges in ((3,((0,1),(1,2))),(4,((0,1),(1,2),(2,3))),
                    (4,((0,1),(0,2),(0,3))), (4,((0,1),(0,2),(1,2)))):
        _,ind,_=histograms(n,edges)
        for q in (2,4):
            direct,nelt=literal_involution_spectrum(n,edges,q)
            assert direct==expected_from_poly(polyn(ind,len(edges)),q)
            print('small graph',n,edges,'q',q,'PASS')
    for m in range(1,17):
        edges=tuple((i,i+1) for i in range(m-1))
        _,ind,_=histograms(m,edges)
        mx=max(r for (s,r) in ind)
        assert mx==2*m//3
        a,rem=divmod(m,3)
        q=4
        predicted=(q**(a-1)*(q-1)**a if rem==0 else
                   q**a*((a+1)*(q-1)**a+comb(a+2,2)*(q-1)**(a+1)) if rem==1 else
                   q**a*(a+2)*(q-1)**(a+1))
        if m==1: predicted=2 # q^0 + (q-1), q=4 total q, so fix below
        if m==1: predicted=q
        actual=evalpoly(polyn(ind,m-1),q)[mx]
        assert actual==predicted,(m,predicted,actual)
    print('VERIFY_OK_GRAPHICAL_INVOLUTION_CLASS_TWINS')

if __name__=='__main__':main()
