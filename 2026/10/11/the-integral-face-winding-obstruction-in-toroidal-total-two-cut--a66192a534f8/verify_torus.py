#!/usr/bin/env python3
"""Signed-trace consistency checks for two-cut complexes of toroidal grids."""
from itertools import product
from math import gcd


def vertex_map(m,n,e1,e2,a,b,swap):
    assert not swap or m == n
    return lambda p: ((e1*(p[1] if swap else p[0])+a)%m,
                      (e2*(p[0] if swap else p[1])+b)%n)


def vertex_cycles(m,n,fun):
    unseen=set(product(range(m),range(n)))
    out=[]
    while unseen:
        p=min(unseen); cyc=[]; q=p
        while q in unseen:
            unseen.remove(q);cyc.append(q);q=fun(q)
        assert q==p
        out.append(cyc)
    return out


def graph_edges(m,n):
    vertices=list(product(range(m),range(n)))
    directed=[]
    for i,j in vertices:
        directed.append(((i,j),((i+1)%m,j)))
        directed.append(((i,j),(i,(j+1)%n)))
    d={frozenset(pair):(k,pair) for k,pair in enumerate(directed)}
    assert len(d)==2*m*n
    return vertices,directed,d


def is_clique_subset(T,edge_keys):
    return len(T)<=1 or (len(T)==2 and frozenset(T) in edge_keys)


def signed_lafschetz_on_cut(m,n,fun,edge_keys):
    # A fixed simplex is a union of permutation cycles. Count its signed
    # reduced Euler contribution directly, not via graph-chain characters.
    cycles=vertex_cycles(m,n,fun)
    r=len(cycles)
    v=m*n
    full=(1<<r)-1
    signsum=0
    for mask in range(full+1):
        T=[] # complement of a fixed cut face
        selected=0
        for i,c in enumerate(cycles):
            if mask>>i&1:
                T+=c
                selected+=1
        if not is_clique_subset(T,edge_keys):
            # Faces S comprise omitted orbits, count their sign directly.
            included=r-selected
            signsum += (-1)**(included+1)
    return signsum # character = (-1)^(mn-4) times reduced Lefschetz.


def test(m,n,include_direct_cut):
    vertices,edges,edge_lookup=graph_edges(m,n)
    N=m*n; total=0; direct=0
    for swap in ([False,True] if m==n else [False]):
      for e1,e2,a,b in product((-1,1),(-1,1),range(m),range(n)):
        fun=vertex_map(m,n,e1,e2,a,b,swap)
        vertex_fixed=sum(fun(v)==v for v in vertices)
        edge_trace=0
        for u,v in edges:
          w,z=fun(u),fun(v)
          d=edge_lookup[frozenset((w,z))][1]
          if frozenset((u,v))==frozenset((w,z)):
            edge_trace += 1 if (w,z)==(u,v) else -1
        trace_graph=edge_trace-vertex_fixed+1
        orient=e1*e2*(-1 if swap else 1)
        tr=0 if swap else e1+e2
        fixed_faces=0
        for i,j in vertices:
          k=(e1*(j if swap else i)+a-(e1==-1))%m
          l=(e2*(i if swap else j)+b-(e2==-1))%n
          fixed_faces += (i==k and j==l)
        theory=orient*(fixed_faces-1)+tr
        assert trace_graph==theory,(m,n,swap,e1,e2,a,b,trace_graph,theory)
        c=vertex_cycles(m,n,fun)
        sign=(-1)**(N-len(c))
        if include_direct_cut:
            cut_L=signed_lafschetz_on_cut(m,n,fun,edge_lookup)
            cut_trace=cut_L*((-1)**(N-4))
            assert cut_trace==sign*theory,(m,n,swap,e1,e2,a,b,cut_trace,sign*theory)
            direct+=1
        total+=1
    print('OK',m,n,'group-elements',total,'direct-cut-lefschetz',direct,'betti',m*n+1)
    return total,direct


def invariant_index(m,n):
    # Compute the two edge orbits under all translations, then compute
    # the invariant chain generators' graph boundaries and winding numbers.
    vertices,edges,lookup=graph_edges(m,n)
    seen=set(); orbits=[]
    for edge in edges:
        if edge in seen: continue
        orbit={(((u[0]+a)%m,(u[1]+b)%n),
                 ((v[0]+a)%m,(v[1]+b)%n))
               for a in range(m) for b in range(n) for u,v in [edge]}
        seen |= orbit;orbits.append(orbit)
    assert len(orbits)==2 and len(seen)==len(edges)
    assert all(len(O)==m*n for O in orbits)
    winding=[]
    for O in orbits:
        div={q:0 for q in vertices}
        wx=wy=0
        for u,v in O:
            div[u]-=1;div[v]+=1
            if v[1]==u[1] and u[0]==m-1 and v[0]==0: wx+=1
            if v[0]==u[0] and u[1]==n-1 and v[1]==0: wy+=1
        assert all(x==0 for x in div.values())
        winding.append((wx,wy))
    assert sorted(winding)==sorted([(n,0),(0,m)])
    return n,m

if __name__=='__main__':
    nt=nd=0
    for m,n,direct in [(4,4,True),(4,5,True),(5,5,False),(4,6,False),(5,6,False),(6,6,False)]:
        a,b=test(m,n,direct);nt+=a;nd+=b
        assert invariant_index(m,n)==(n,m)
    print('VERIFY_OK', 'group_character_checks',nt, 'direct_cut_checks',nd)
