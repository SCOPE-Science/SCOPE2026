#!/usr/bin/env python3
"""Reproducible low-degree checks for the Gamma-cubical graph vanishing result.
Python 3 standard library only. Checks integer prism relations and finite mod-2 chain ranks.
"""
from itertools import product,combinations

def nondeg(t,k):
    return all(any(t[u]!=t[u | (1<<i)] for u in range(1<<k) if not u&(1<<i)) for i in range(k))

def face(t,k,i,s):
    return tuple(t[(u & ((1<<i)-1))|((u>>i)<<(i+1))|(s<<i)] for u in range(1<<(k-1)))

def normadd(d,t,a):
    if not a or not nondeg(t,len(t).bit_length()-1):return
    d[t]=d.get(t,0)+a
    if not d[t]: del d[t]

def boundary(t,k):
    out={}
    for i in range(k):
        normadd(out,face(t,k,i,1),(-1)**i)
        normadd(out,face(t,k,i,0),-(-1)**i)
    return out

def prism(t,k,base):
    return tuple(list(t)+[base]*(1<<k))

def chain_prism(d,k,base):
    out={}
    for t,a in d.items():normadd(out,prism(t,k,base),a)
    return out

def chainsub(x,y):
    z=dict(x)
    for t,a in y.items(): z[t]=z.get(t,0)-a
    return {t:a for t,a in z.items() if a}

def valid_graph(t,k,edge_set):
    if k==1:return t[0]==t[1] or frozenset(t) in edge_set
    return all(len({t[u]}|{t[u^(1<<i)] for i in range(k)})<=2 and
        (len({t[u]}|{t[u^(1<<i)] for i in range(k)})<2 or
         frozenset({t[u]}|{t[u^(1<<i)] for i in range(k)}) in edge_set)
         for u in range(1<<k))

def rank_mod2(columns):
    piv={}
    for col in columns:
        while col:
            i=col.bit_length()-1
            if i in piv:col^=piv[i]
            else:piv[i]=col;break
    return len(piv)

def finite_graph_h2(n,edges):
    edge_set={frozenset(e) for e in edges}
    c1=[t for t in product(range(n),repeat=2) if nondeg(t,1) and valid_graph(t,1,edge_set)]
    i1={t:i for i,t in enumerate(c1)}
    c2=[t for t in product(range(n),repeat=4) if nondeg(t,2) and valid_graph(t,2,edge_set)]
    i2={t:i for i,t in enumerate(c2)}
    for t in c2:
        assert len(set(t))==2 and frozenset(t) in edge_set
        # A cube supported on a single edge has a valid 3D prism filling.
        assert valid_graph(prism(t,2,min(t)),3,edge_set)
    def col(t,k,index):
        bits=0
        for f,a in boundary(t,k).items():
            if f in index and a%2: bits^=1<<index[f]
        return bits
    r2=rank_mod2(col(t,2,i1) for t in c2)
    r3=rank_mod2(col(t,3,i2) for t in product(range(n),repeat=8)
                 if nondeg(t,3) and valid_graph(t,3,edge_set))
    assert len(c2)-r2-r3==0,(n,edges,len(c2),r2,r3)
    return len(c2)

def main():
    # Verify an integer chain-homotopy identity, not merely mod-2 ranks:
    # d(P_2 sigma) - P_1(d sigma) = -sigma for each 2-edge cube.
    squares=0
    for t in product((0,1),repeat=4):
        if not nondeg(t,2):continue
        d3=boundary(prism(t,2,0),3)
        lhs=chainsub(d3,chain_prism(boundary(t,2),1,0))
        assert lhs=={t:-1},(t,lhs)
        squares+=1
    graphs=0;squares_checked=0
    for n in range(1,5):
        opts=list(combinations(range(n),2))
        for bits in range(1<<len(opts)):
            edges=[e for i,e in enumerate(opts) if bits>>i&1]
            squares_checked+=finite_graph_h2(n,edges)
            graphs+=1
    # A few five-vertex shapes to expand the finite audit.
    n=5
    examples=[list(combinations(range(5),2)),[(i,(i+1)%5) for i in range(5)],
              [(i,i+1) for i in range(4)],[(0,i) for i in range(1,5)],
              [(0,1),(1,2),(2,0),(2,3),(3,4)],[]]
    for e in examples:
        squares_checked+=finite_graph_h2(n,e);graphs+=1
    print('PASS integer cubical prism identity on',squares,'two-color normalized square generators')
    print('PASS mod-2 degree-two homology zero on',graphs,'graphs, all simple graphs up to 4 vertices')
    print('PASS all',squares_checked,'eligible degree-two cube generators localized to unique graph edges')
    print('LIMIT: finite mod-2 calculations supplement, not replace, the integral universal proof')
if __name__=='__main__':main()
