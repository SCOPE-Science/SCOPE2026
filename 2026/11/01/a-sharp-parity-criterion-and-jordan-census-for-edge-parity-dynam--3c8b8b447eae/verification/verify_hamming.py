#!/usr/bin/env python3
"""Independent finite-field rank checks for XOR neighbor dynamics on line graphs of Hamming products."""
from itertools import product
from math import prod

def rows_rank(rows):
    pivots={}
    for x in rows:
        while x:
            k=x.bit_length()-1
            if k in pivots: x^=pivots[k]
            else: pivots[k]=x;break
    return len(pivots)

def mulvec(rows,v):
    return sum(1<<i for i,row in enumerate(rows) if (row&v).bit_count()%2)

def get_edges(sizes):
    coords=list(product(*(range(v) for v in sizes)))
    idx={v:i for i,v in enumerate(coords)}
    edges=[]
    for i,c in enumerate(coords):
      for j in range(len(sizes)):
       for a in range(c[j]+1,sizes[j]):
         v=list(c);v[j]=a
         edges.append((i,idx[tuple(v)]))
    return edges

def odd_fixed_witness(sizes):
    assert any(s%2 for s in sizes)
    j=next(i for i,s in enumerate(sizes) if s%2)
    coords=list(product(*(range(v) for v in sizes)))
    # For one odd alphabet, the two selected slices carry the ones value.
    color=[int(c[j] in (0,1)) for c in coords]
    edges=get_edges(sizes)
    edge_vector=sum((color[u]^color[v])<<i for i,(u,v) in enumerate(edges))
    assert edge_vector!=0
    incident=[0]*prod(sizes)
    for i,(u,v) in enumerate(edges): incident[u]|=1<<i;incident[v]|=1<<i
    adj=[incident[u]^incident[v] for u,v in edges]
    assert mulvec(adj,edge_vector)==edge_vector,(sizes,'not fixed')
    return f'odd factor {sizes}: nonzero fixed edge pattern weight={edge_vector.bit_count()}'

def calc(sizes):
    edges=get_edges(sizes); e=len(edges)
    incident=[0]*prod(sizes)
    for i,(u,v) in enumerate(edges): incident[u]|=1<<i;incident[v]|=1<<i
    adj=[(incident[u]^incident[v]) for i,(u,v) in enumerate(edges)]
    # incidence parity: both end masks contain edge, thus XOR has zero diagonal
    r1=rows_rank(adj)
    adj2=[mulvec(adj,adj[j]) for j in range(e)]
    r2=rows_rank(adj2)
    adj3=[mulvec(adj,adj2[j]) for j in range(e)]
    r3=rows_rank(adj3)
    n=prod(sizes); D=sum(s-1 for s in sizes); H=prod(s-2 for s in sizes)
    expected=(n-2,(n-H)//2-2,0) if len(sizes)>=2 else (n-2,0,0)
    res=(r1,r2,r3)
    assert res==expected,(sizes,res,expected)
    b3=r2;b2=r1-2*r2;b1=e-2*r1+r2
    assert b1>=0 and b2>=0 and b3>=0 and b1+2*b2+3*b3==e
    return f'{sizes}: V={n}, E={e}, ranks={res}, Jordan1/2/3={(b1,b2,b3)}'

if __name__=='__main__':
    tests=[(2,2),(2,4),(2,6),(4,4),(4,6),(6,6),(2,2,2),(2,2,4),(2,4,4),(2,2,2,2),(2,2,2,4),(4,4,4),(2,2,2,2,2),(2,2,2,2,2,2)]
    for ss in tests: print(calc(ss))
    for ss in [(3,2),(3,3),(3,4),(3,5,2),(2,2,3),(5,5),(2,2,2,3)]: print(odd_fixed_witness(ss))
    print('PASS: rank formulas and nilpotency for all test cases.')
