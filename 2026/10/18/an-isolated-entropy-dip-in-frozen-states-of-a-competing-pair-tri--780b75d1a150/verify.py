#!/usr/bin/env python3
"""Independent finite-volume checks for a pair/triplet Ising ring."""
import itertools
from fractions import Fraction
import sympy as sp
from math import isclose
import networkx as nx

S=list(itertools.product((-1,1),repeat=4)); IX={t:i for i,t in enumerate(S)}

def transfer(r):
    T=sp.zeros(16)
    for t in S:
        a,b,c,d=t
        for e in (-1,1):
            force=c*((b+d)-r*(a*b+b*d+d*e))
            if force>0: T[IX[t],IX[(b,c,d,e)]]=1
    return T

def energy(s,r):
    n=len(s)
    return -sum(s[i]*s[(i+1)%n] for i in range(n)) + r*sum(s[i]*s[(i+1)%n]*s[(i+2)%n] for i in range(n))

def check_full(n,r):
    count=0
    for bits in itertools.product((-1,1),repeat=n):
        base=energy(bits,r)
        ok=True
        for i in range(n):
            b=list(bits);b[i]*=-1
            if energy(b,r)<=base: ok=False;break
        if ok:count+=1
    return count

rvals=[Fraction(0),Fraction(1,2),Fraction(2,3),Fraction(1),Fraction(2),Fraction(3)]
count=0
for r in rvals:
    rr=sp.Rational(r.numerator,r.denominator)
    T=transfer(rr)
    if r==0: polys='lambda**14*(lambda - 1)**2'
    elif r<sp.Rational(2,3): polys='lambda**10*(lambda - 1)*(lambda**2 - lambda + 1)*(lambda**3 - lambda - 1)'
    elif r==sp.Rational(2,3): polys='lambda**11*(lambda**2 - lambda + 1)*(lambda**3 - lambda - 1)'
    elif r<2: polys='lambda**6*(lambda**10 - lambda**9 - lambda**7 - lambda**5 + lambda**4 + lambda + 1)'
    elif r==2: polys='lambda**6*(lambda - 1)*(lambda**9 - lambda**6 - lambda**5 - lambda**3 - lambda**2 - lambda - 1)'
    else: polys='lambda**4*(lambda**3 - lambda**2 - 1)*(lambda**9 - lambda**3 - 1)'
    x=sp.Symbol('lambda')
    assert sp.expand(T.charpoly().as_expr()-sp.sympify(polys.replace('lambda', 'x'), locals={'x':x}))==0,(r,T.charpoly().as_expr())
    G=nx.DiGraph()
    G.add_nodes_from(range(16))
    G.add_edges_from((i,j) for i in range(16) for j in range(16) if T[i,j])
    comps=[c for c in nx.strongly_connected_components(G) if len(c)>1 or any(G.has_edge(i,i) for i in c)]
    sizes=sorted((len(c) for c in comps),reverse=True)
    want={Fraction(0):[1,1],Fraction(1,2):[6,1],Fraction(2,3):[6],Fraction(1):[11],Fraction(2):[10],Fraction(3):[12]}[r]
    assert sizes==want,(r,sizes,want)
    main=max(comps,key=len)
    assert any(G.has_edge(i,i) for i in main) # ensures aperiodic component
    assert nx.is_strongly_connected(G.subgraph(main))
    print('characteristic polynomial and primitive recurrent component PASS:',r)

    M=sp.eye(16)
    for n in range(1,12):
        M=M*T
        if n>=5:
            expect=check_full(n,r)
            assert int(sp.trace(M))==expect,(n,r,int(sp.trace(M)),expect)
            count+=1
    print('counts PASS:',r)
print('ALL PASS:',count,'direct finite ring counts and six exact characteristic polynomials')
