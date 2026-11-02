#!/usr/bin/env python3
"""Standalone finite tests of an Ising line-graph microcanonical formula.

No external packages are needed.  Input graphs are simple biregular bipartite graphs.
"""
from functools import lru_cache
from collections import Counter
import math


def make_graph(m,n,edges):
    edges=tuple(sorted(tuple(x) for x in edges))
    assert len(edges)==len(set(edges))
    assert all(0<=u<m and 0<=v<n for u,v in edges)
    du=Counter(u for u,v in edges); dv=Counter(v for u,v in edges)
    assert len(du)==m and len(dv)==n
    assert len(set(du.values()))==len(set(dv.values()))==1
    r=du[0];s=dv[0]
    assert len(edges)==m*r==n*s
    return m,n,r,s,edges


def formula(graph,K,Ju,Jv):
    m,n,r,s,edges=graph
    q,t=divmod(K,m)
    z,w=divmod(K,n)
    return (Ju*((m-t)*(2*q-r)**2+t*(2*q-r+2)**2-m*r)
        +Jv*((n-w)*(2*z-s)**2+w*(2*z-s+2)**2-n*s))/2


def enumerate_ising(graph,Ju,Jv):
    m,n,r,s,edges=graph
    e=len(edges)
    adj=[]
    for i,(u,v) in enumerate(edges):
        for j,(uu,vv) in enumerate(edges[i+1:],i+1):
            if u==uu: adj.append((i,j,Ju))
            elif v==vv: adj.append((i,j,Jv))
    best=[float('inf')]*(e+1)
    counts=[0]*(e+1)
    for mask in range(1<<e):
        K=mask.bit_count()
        spins=[1 if mask>>i & 1 else -1 for i in range(e)]
        E=sum(w*spins[i]*spins[j] for i,j,w in adj)
        if E<best[K]-1e-8:best[K]=E;counts[K]=1
        elif abs(E-best[K])<1e-8:counts[K]+=1
    for K in range(e+1):
        assert abs(best[K]-formula(graph,K,Ju,Jv))<1e-8,(graph,K,best[K],formula(graph,K,Ju,Jv))
    return best,counts


def matchings(graph):
    m,n,r,s,edges=graph
    E=len(edges);ans=0
    for mask in range(1<<E):
        U=set();V=set();valid=True
        for i,(u,v) in enumerate(edges):
            if mask>>i&1:
                if u in U or v in V:valid=False;break
                U.add(u);V.add(v)
        ans+=valid
    return ans


def matchings_by_subset_dp(graph):
    """Independent subset dynamic program for the matching count."""
    m,n,r,s,edges=graph
    nb=[[v for u,v in edges if u==i] for i in range(m)]
    @lru_cache(None)
    def dp(i,mask):
        if i==m:return 1
        return dp(i+1,mask)+sum(dp(i+1,mask|(1<<v)) for v in nb[i] if not (mask>>v&1))
    return dp(0,0)


def graph_examples():
    # Connected eight-cycle, with 4 vertices on each side.
    c8=[(i,i) for i in range(4)]+[(i,(i+1)%4) for i in range(4)]
    # Two disjoint four-cycles, with the same order and degrees.
    twoc4=[(i,j) for block in ((0,1),(2,3)) for i in block for j in block]
    k23=[(u,v) for u in range(2) for v in range(3)]
    k34=[(u,v) for u in range(3) for v in range(4)]
    # 3-cube: U and V contain the even- and odd-parity binary vectors.
    U=[x for x in range(8) if x.bit_count()%2==0]
    V=[x for x in range(8) if x.bit_count()%2==1]
    cube=[(i,j) for i,u in enumerate(U) for j,v in enumerate(V) if (u^v).bit_count()==1]
    return [('C8',make_graph(4,4,c8)),('2C4',make_graph(4,4,twoc4)),
        ('K23',make_graph(2,3,k23)),('K34',make_graph(3,4,k34)),
        ('Cube',make_graph(4,4,cube))]


def main():
    pairs=[(1,1),(2,3),(3,2),(1.25,0.75)]
    tests=0; sectors=0
    for name,g in graph_examples():
        m,n,r,s,edges=g
        for Ju,Jv in pairs:
            en,counts=enumerate_ising(g,Ju,Jv)
            assert counts[0]==counts[-1]==1
            thresholds=[Ju*(2*(K//m)-r+1)+Jv*(2*(K//n)-s+1) for K in range(len(edges))]
            assert all(a<=b+1e-10 for a,b in zip(thresholds,thresholds[1:]))
            brk={0,len(edges)}|{K for K in range(1,len(edges)) if K%m==0 or K%n==0}
            assert len(brk)==r+s-math.gcd(r,s)+1
            # All half-step fields must have unique ground states at breakpoint sectors.
            for h in [(a+b)/2 for a,b in zip(sorted(set(thresholds)),sorted(set(thresholds))[1:])]:
                vals=[E-h*(2*K-len(edges)) for K,E in enumerate(en)]
                km=[i for i,v in enumerate(vals) if abs(v-min(vals))<1e-8]
                assert len(km)==1 and km[0] in brk
            # At h_sat, exactly every matching of the underlying graph minimizes.
            h=Ju*(r-1)+Jv*(s-1)
            vals=[E-h*(2*K-len(edges)) for K,E in enumerate(en)]
            count=sum(counts[i] for i,v in enumerate(vals) if abs(v-min(vals))<1e-8)
            assert count==matchings(g)==matchings_by_subset_dp(g),(name,count,matchings(g))
            tests+=1;sectors+=len(en)
        print(name,'m,n,r,s,edges=',m,n,r,s,len(edges),
              'saturation_matching_count=',matchings(g),
              'plateaux=',r+s-math.gcd(r,s)+1)
    # Two connected 3-regular bipartite graphs on 12 vertices.
    # Their entire field staircases coincide but saturation degeneracies differ.
    a=make_graph(6,6,[(i,(i+s)%6) for i in range(6) for s in (0,1,2)])
    b=make_graph(6,6,[(i,(i+s)%6) for i in range(6) for s in (0,1,3)])
    assert matchings(a)==matchings_by_subset_dp(a)==1104
    assert matchings(b)==matchings_by_subset_dp(b)==1092
    for graph in [a,b]:
        Ju=Jv=1
        H=[Ju*(2*(k//6)-3+1)+Jv*(2*(k//6)-3+1) for k in range(18)]
        assert sorted(set(H))==[-4,0,4]
    print('connected 3-regular bipartite witnesses: saturation counts 1104 versus 1092; identical thresholds -4,0,4')
    g1,g2=graph_examples()[0][1],graph_examples()[1][1]
    assert matchings(g1)==47 and matchings(g2)==49
    print('PASS',tests,'full Ising enumerations,',sectors,'fixed-spin sectors;',
         'all analytic energies, breakpoints, and critical matching counts agree.')

if __name__=='__main__': main()
