#!/usr/bin/env python3
"""Exact reproducibility checks for binary majority recurrence on Möbius ladders.
Dependencies: Python 3, sympy, networkx, numpy. No online services required.
No claim of external verification is made.
"""
import sys
import networkx as nx
import numpy as np
import sympy as sy

z=sy.Symbol('z')
def bit(v,t,a):
    return (v>>(t*2+a))&1

def sw(v,bits):
    return sum(((v>>i)&1)<<(i^1) for i in range(bits))

def local(u,v,w,temporal):
    for t in range(temporal):
        other=1-t if temporal==2 else 0
        for a in (0,1):
            if bit(v,t,a)!=int(bit(u,other,a)+bit(w,other,a)+bit(v,other,1-a)>=2):
                return False
    return True

def graph(temporal):
    base=4 if temporal==1 else 16
    G=nx.DiGraph()
    G.add_nodes_from(range(base*base))
    for u in range(base):
        for v in range(base):
            for w in range(base):
                if local(u,v,w,temporal):
                    G.add_edge(base*u+v,base*v+w)
    return G,base

def components(G):
    comps=[tuple(sorted(c)) for c in nx.strongly_connected_components(G) if len(c)>1 or G.has_edge(next(iter(c)),next(iter(c)))]
    return sorted(comps,key=lambda c:(-len(c),c[0]))

def block(G,c):
    return sy.Matrix([[int(G.has_edge(u,v)) for v in c] for u in c])

def twisted_block(G,c,base):
    S=lambda p:base*sw(p//base,2 if base==4 else 4)+sw(p%base,2 if base==4 else 4)
    A=block(G,c)
    idx={u:j for j,u in enumerate(c)}
    P=sy.Matrix([[int(S(u)==v) for v in c] for u in c])
    assert A*P==P*A
    plus=[u for u in c if S(u)>=u]
    minus=[u for u in c if S(u)>u]
    Aplus=sy.Matrix([[A[idx[u],idx[v]]+(A[idx[u],idx[S(v)]] if S(v)!=v else 0) for v in plus] for u in plus])
    Aminus=sy.Matrix([[A[idx[u],idx[v]]-A[idx[u],idx[S(v)]] for v in minus] for u in minus])
    return A,P,Aplus,Aminus

G1,b1=graph(1)
cs1=components(G1)
assert list(map(len,cs1))==[4,1,1]
A1,P1,Ap1,Am1=twisted_block(G1,cs1[0],b1)
assert sy.expand(A1.charpoly(z).as_expr()-(z*z-z-1)*(z*z-z+1))==0
assert P1==sy.eye(4)
S1=lambda p:b1*sw(p//b1,2)+sw(p%b1,2)
assert {S1(u) for u in cs1[1]}==set(cs1[2])

G2,b2=graph(2)
cs2=components(G2)
assert list(map(len,cs2))==[16,8,8,2,1,1]
S2=lambda p:b2*sw(p//b2,4)+sw(p%b2,4)
assert {S2(u) for u in cs2[0]}==set(cs2[0])
assert {S2(u) for u in cs2[1]}==set(cs2[2])
assert {S2(u) for u in cs2[3]}==set(cs2[3])
assert {S2(u) for u in cs2[4]}==set(cs2[5])
assert sum(len(c) for c in cs2)==36
A2,P2,Ap2,Am2=twisted_block(G2,cs2[0],b2)
assert (len(Ap2.tolist()),len(Am2.tolist()))==(10,6)
polyplus=(z-1)*(z+1)*(z*z-3*z+1)*(z*z+z+1)*(z**4-z**3+2*z*z+z+1)
polyminus=(z-1)*(z+1)*(z**4+z**3+2*z*z-z+1)
assert sy.expand(Ap2.charpoly(z).as_expr()-polyplus)==0
assert sy.expand(Am2.charpoly(z).as_expr()-polyminus)==0
Ashort,Pshort,_,_=twisted_block(G2,cs2[3],b2)
assert Pshort==sy.eye(2)
assert sy.expand(Ashort.charpoly(z).as_expr()-(z*z-1))==0
assert all(set(S2(u) for u in cs2[j])==set(cs2[9-j]) for j in (4,5))

def lucas(n):
    if n==0:return 2
    a,b=2,1
    for _ in range(2,n+1):a,b=b,a+b
    return b

def cosine_six(n):
    return (2,1,-1,-2,-1,1)[n%6]

def count_formula(n):
    L=lucas(n)
    Q=L+cosine_six(n)
    if n%2:P=Q*Q
    elif n%6==0:P=L*L+2
    else:P=L*L-1
    return P,Q

def trace_twisted(A,P,n):
    return sy.trace((A**n)*P)

for n in range(1,25):
    P,Q=count_formula(n)
    q_mat=trace_twisted(A1,P1,n)
    p_mat=trace_twisted(A2,P2,n)+trace_twisted(Ashort,Pshort,n)
    assert int(q_mat)==Q,(n,Q,q_mat)
    assert int(p_mat)==P,(n,P,p_mat)
print('Exact transfer graph: fixed SCC sizes 4,1,1; recurrent SCC sizes 16,8,8,2,1,1.')
print('Symmetry swap and characteristic polynomials: all exact identities passed.')
print('Formulas equal twisted matrix traces for n=1,...,24 (symbolic charpoly proof gives all n).')

def majority(x,n):
    length=2*n
    y=np.zeros_like(x)
    for i in range(length):
        v=((x>>((i-1)%length))&1)+((x>>((i+1)%length))&1)+((x>>((i+n)%length))&1)
        y|=(v>=2).astype(np.uint32)<<i
    return y

for n in range(3,12):
    x=np.arange(1<<(2*n),dtype=np.uint32)
    f=majority(x,n)
    f2=majority(f,n)
    got=(int(np.count_nonzero(f2==x)),int(np.count_nonzero(f==x)))
    want=count_formula(n)
    assert got==want,(n,got,want)
    print(f'n={n}: P={got[0]}, Q={got[1]}, primitive 2-cycles={(got[0]-got[1])//2}; all {len(x)} states checked')
print('PASS: exhaustive finite replay and all-size exact characteristic identities.')
