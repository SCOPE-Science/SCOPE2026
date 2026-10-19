#!/usr/bin/env python3
"""Exact-rational verification of trust-game Shapley/core compatibility."""
from fractions import Fraction as F
from itertools import combinations
from math import factorial

def ind(n, arcs):
    return [sum((j, i) in arcs for j in range(n)) for i in range(n)]

def char_value(n, arcs, weights, mask):
    s = {i for i in range(n) if mask & (1 << i)}
    inner = sum(weights[j] for i, j in arcs if i in s and j in s)
    outer = F(0)
    for j in s:
        incoming = [weights[j] for i in range(n) if (i,j) in arcs and i not in s]
        if incoming:
            outer += min(incoming)
    return inner + outer

def shapley_by_definition(n, arcs, weights):
    v = [char_value(n, arcs, weights, mask) for mask in range(1 << n)]
    f = [F(0) for _ in range(n)]
    nf = factorial(n)
    for i in range(n):
        for mask in range(1 << n):
            if mask & (1 << i):
                continue
            k = mask.bit_count()
            f[i] += F(factorial(k) * factorial(n-k-1), nf) * (v[mask|(1<<i)]-v[mask])
    return f

def predicted_shapley(n, arcs, weights):
    d=ind(n, arcs)
    h=[F(0) if z <= 1 else F(z-1, 2*(z+1)) for z in d]
    c=[d[i] * weights[i] for i in range(n)]
    shifts=[sum((weights[j]*h[j] for j in range(n) if (i,j) in arcs),F(0)) - d[i]*weights[i]*h[i] for i in range(n)]
    return [c[i]+shifts[i] for i in range(n)]

def stationary(n, arcs):
    d=ind(n, arcs)
    assert all(v>0 for v in d)
    m=[[F((i,j) in arcs,d[j])-F(i==j) for j in range(n)] for i in range(n)]
    m[-1]=[F(1)]*n
    rhs=[F(0)]*(n-1)+[F(1)]
    for k in range(n):
        p=next(r for r in range(k,n) if m[r][k])
        m[k],m[p]=m[p],m[k]; rhs[k],rhs[p]=rhs[p],rhs[k]
        fac=m[k][k]
        m[k]=[x/fac for x in m[k]]; rhs[k]/=fac
        for r in range(n):
            if r==k:continue
            fac=m[r][k]
            m[r]=[m[r][j]-fac*m[k][j] for j in range(n)]
            rhs[r]-=fac*rhs[k]
    return rhs

def symmetric_arcs(n, edges):
    return {(u,v) for a,b in edges for u,v in ((a,b),(b,a))}

def connected(n, edges):
    if n <2:return True
    seen={0}
    while True:
        update=seen|{v for u,v in edges if u in seen}|{u for u,v in edges if v in seen}
        if update==seen:return len(seen)==n
        seen=update

def verify():
    total=0
    for n in range(2,6):
        pairs=list(combinations(range(n),2))
        for bits in range(1,1<<len(pairs)):
            edges=[pair for k,pair in enumerate(pairs) if bits & (1<<k)]
            if not connected(n,edges):continue
            arcs=symmetric_arcs(n,edges)
            weights=[F(1)]*n
            actual=shapley_by_definition(n,arcs,weights)
            predicted=predicted_shapley(n,arcs,weights)
            assert actual==predicted,(n,edges,actual,predicted)
            d=ind(n,arcs)
            assert (actual==[F(x) for x in d]) == (len(set(d))==1)
            total+=1
    print('Connected simple graphs with 2..5 labeled vertices checked:',total)
    # A nonregular strongly connected digraph, indegree >= 2, with a calibrated target weight.
    ring=symmetric_arcs(4,[(0,1),(1,2),(2,3),(3,0)])
    arcs=ring|{(0,2)}
    d=ind(4,arcs)
    assert d==[2,2,3,2]
    pi=stationary(4,arcs)
    print('Irregular strong digraph indegrees:',d,'stationary pi:',list(map(str,pi)))
    h=[F(z*(z-1),2*(z+1)) for z in d]
    w=[pi[i]/h[i] for i in range(4)]
    w=[u/max(w) for u in w]
    assert min(w)>0 and max(w)<=1
    assert shapley_by_definition(4,arcs,w)==[d[i]*w[i] for i in range(4)]
    print('Balancing target weights:',list(map(str,w)))
    # A mixed indegree-one/indegree-two strong digraph is obstructed.
    arcs2={(0,1),(1,2),(2,0),(0,2)}
    d2=ind(3,arcs2)
    assert d2==[1,1,2]
    for w2 in [[F(1)]*3,[F(1,3),F(1,2),F(1,7)]]:
        assert shapley_by_definition(3,arcs2,w2)!=[d2[i]*w2[i] for i in range(3)]
    # Pure directed cycle is additive even for heterogeneous target weights.
    arcs3={(0,1),(1,2),(2,3),(3,0)}
    w3=[F(1,2),F(1,3),F(2,3),F(1,5)]
    assert shapley_by_definition(4,arcs3,w3)==w3
    # Verify Dirichlet identity on a path.
    arcs4=symmetric_arcs(3,[(0,1),(1,2)])
    phi=shapley_by_definition(3,arcs4,[F(1)]*3)
    assert phi==[F(7,6),F(5,3),F(7,6)],phi
    h=[F(0),F(1,6),F(0)]
    d=[1,2,1]
    assert sum((h[i]*(phi[i]-d[i]) for i in range(3)),F(0))==-sum(((h[u]-h[v])**2 for u,v in [(0,1),(1,2)]),F(0))
    print('Exact path-three Shapley values:',list(map(str,phi)))
    print('PASS: all exact rational checks')

if __name__=='__main__':verify()
