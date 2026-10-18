#!/usr/bin/env python3
"""Standalone exact lattice-point check of a graph-metric volume response."""
import itertools, math
from fractions import Fraction

CASES = [
    ('singleton',1,[]),
    ('two-antichain',2,[]),
    ('two-chain',2,[(0,1)]),
    ('three-antichain',3,[]),
    ('three-chain',3,[(0,1),(1,2)]),
    ('three-V',3,[(0,2),(1,2)]),
    ('three-L',3,[(0,1)]),
    ('four-diamond',4,[(0,1),(0,2),(1,3),(2,3)]),
    ('four-two-chains',4,[(0,1),(2,3)]),
    ('four-complete-height-two',4,[(0,2),(0,3),(1,2),(1,3)]),
    ('three-relabelled-V',3,[(2,0),(1,0)]),
]

def graph(n, relations):
    reach=[[i==j for j in range(n)] for i in range(n)]
    for a,b in relations:reach[a][b]=True
    for k in range(n):
      for i in range(n):
       for j in range(n):
        if reach[i][k] and reach[k][j]:reach[i][j]=True
    covers=[]
    for i in range(n):
     for j in range(n):
      if i!=j and reach[i][j] and not any(k!=i and k!=j and reach[i][k] and reach[k][j] for k in range(n)):
       covers.append((i,j))
    # Select a linear extension, rather than assume input numbering is topological.
    order=[]
    for _ in range(n):
     next_i=next(i for i in range(n) if i not in order and all(j in order or j==i or not reach[j][i] for j in range(n)))
     order.append(next_i)
    phi=[0]*n
    for k,i in enumerate(order,1):phi[i]=k
    L=n+1; u=n;v=n+1
    edges=[]
    for i in range(n):
      if not any(j!=i and reach[j][i] for j in range(n)): edges.append((u,i,phi[i]))
      if not any(j!=i and reach[i][j] for j in range(n)): edges.append((i,v,L-phi[i]))
    edges += [(i,j,phi[j]-phi[i]) for i,j in covers]
    return reach,edges,phi,L

def height_two_graph(n, relations):
    reach, _, _, _ = graph(n,relations)
    a=[i for i in range(n) if any(reach[i][j] for j in range(n) if j!=i) and not any(reach[j][i] for j in range(n) if j!=i)]
    b=[i for i in range(n) if any(reach[j][i] for j in range(n) if j!=i) and not any(reach[i][j] for j in range(n) if j!=i)]
    assert set(a).isdisjoint(b) and len(a)+len(b)==n
    assert all((i in a and j in b) or (i in b and j in a) or i==j for i in range(n) for j in range(n) if reach[i][j] or reach[j][i])
    phi=[1 if i in a else 2 for i in range(n)]
    u=n;v=n+1
    edges=[(u,i,1) for i in a]+[(i,j,1) for i,j in relations]+[(j,v,1) for j in b]
    return reach,edges,phi,3

def count_extensions(reach):
    n=len(reach)
    dp={0:1}
    for mask in range(1<<n):
      if mask not in dp:continue
      for i in range(n):
        if mask>>i&1: continue
        if all(j==i or not reach[j][i] or mask>>j&1 for j in range(n)):
            dp[mask|(1<<i)] = dp.get(mask|(1<<i),0)+dp[mask]
    return dp[(1<<n)-1]

def top_cap_integer_count(n,edges,phi,L,k):
    if not k:return 0
    ans=0;u=n;v=n+1
    for fv in range((L-1)*k+1,L*k+1):
        allowed=[]
        for i in range(n):
            lo=max(-phi[i]*k, fv-(L-phi[i])*k)
            hi=min(phi[i]*k,fv+(L-phi[i])*k)
            allowed.append(range(lo,hi+1))
        for vals in itertools.product(*allowed):
            f=list(vals)+[0,fv]
            if all(abs(f[i]-f[j])<=w*k for i,j,w in edges):ans+=1
    return ans

def forward_diff(vals):
    a=list(vals)
    while len(a)>1:
        a=[a[i+1]-a[i] for i in range(len(a)-1)]
    return a[0]

def run():
    for name,n,rel in CASES:
      reach,edges,phi,L=graph(n,rel)
      e=count_extensions(reach)
      d=n+1
      N=[2*top_cap_integer_count(n,edges,phi,L,k) for k in range(d+1)]
      c=Fraction(forward_diff(N),math.factorial(d))
      target=Fraction(2*e,math.factorial(d))
      assert c==target, (name,c,target)
      print(f'{name}: n={n} e(P)={e} lead_vol={c} Ehrhart={N} OK')
    for name,n,rel in [
        ('unit-three-V',3,[(0,2),(1,2)]),
        ('unit-four-two-chains',4,[(0,1),(2,3)]),
        ('unit-four-complete-height-two',4,[(0,2),(0,3),(1,2),(1,3)])
    ]:
        reach,edges,phi,L=height_two_graph(n,rel)
        d=n+1;e=count_extensions(reach)
        N=[2*top_cap_integer_count(n,edges,phi,L,k) for k in range(d+1)]
        c=Fraction(forward_diff(N),math.factorial(d))
        assert c==Fraction(2*e,math.factorial(d)),(name,c,e)
        print(f'{name}: unit-edge bipartite diameter-three, e(P)={e}, volume loss={c}, Ehrhart={N} OK')
    print('ALL EXACT TESTS PASS')
if __name__=='__main__':run()
