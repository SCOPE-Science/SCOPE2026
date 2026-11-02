#!/usr/bin/env python3
"""Exhaustive finite-state certificate and independent small prism check."""
from collections import Counter

def bit(s,k): return (s>>k)&1

def allowed(a,b,c):
    ta,ba = bit(a,0),bit(a,1)
    tb,bb,rb = [bit(b,k) for k in range(3)]
    tc,bc,rc = [bit(c,k) for k in range(3)]
    ra=bit(a,2)
    return ((rb==1 or ta+tb+ba+bb==1) and
            (tb==1 or ta+tc+rb+rc==1) and
            (bb==1 or ba+bc+rb+rc==1))

def graph():
    vertices=set(); arcs=set()
    for a in range(8):
      for b in range(8):
        for c in range(8):
          if allowed(a,b,c):
             v=(a,b);w=(b,c)
             vertices.add(v);vertices.add(w);arcs.add((v,w))
    adj={v:set() for v in vertices}
    for v,w in arcs:adj[v].add(w)
    return vertices, arcs, adj

def strongly_connected(adj):
    # Independent standard-library implementation of Kosaraju's algorithm.
    seen=set();order=[]
    def dfs(v):
        seen.add(v)
        for w in adj[v]:
            if w not in seen: dfs(w)
        order.append(v)
    for v in adj:
        if v not in seen:dfs(v)
    radj={v:set() for v in adj}
    for v,ws in adj.items():
        for w in ws:radj[w].add(v)
    seen.clear();comps=[]
    def rdfs(v,component):
        seen.add(v);component.add(v)
        for w in radj[v]:
            if w not in seen:rdfs(w,component)
    for v in reversed(order):
        if v not in seen:
            s=set();rdfs(v,s);comps.append(s)
    return comps

def prism_edges(n):
    # top vertices 0..n-1, bottom n..2*n-1
    edges=[]
    for i in range(n):
        edges.extend([(i,(i+1)%n),(n+i,n+(i+1)%n),(i,n+i)])
    return edges

def brute(n):
    edges=prism_edges(n);m=len(edges)
    nb=[0]*m
    for j,(a,b) in enumerate(edges):
      for k,(c,d) in enumerate(edges):
        if j!=k and (a==c or a==d or b==c or b==d): nb[j]|=1<<k
    ans=Counter()
    for s in range(1<<m):
       if all((s>>j)&1 or (s&nb[j]).bit_count()==1 for j in range(m)):
           ans[s.bit_count()]+=1
    return ans

def theorem(n): return Counter({3*n:1,n:6}) if n%6==0 else Counter({3*n:1})

def main():
    vs,arcs,adj=graph()
    assert len(vs)==42 and len(arcs)==102, (len(vs),len(arcs))
    scc=strongly_connected(adj)
    recurrent=[s for s in scc if len(s)>1 or any(v in adj[v] for v in s)]
    recurrent={frozenset(s) for s in recurrent}
    six=frozenset({(0,1),(1,5),(5,0),(0,2),(2,6),(6,0)})
    assert recurrent=={frozenset({(7,7)}),six},recurrent
    assert all(len(adj[v].intersection(six))==1 for v in six)
    assert sum(sum(bit(v[0],j) for j in range(3)) for v in six)==6
    for n in range(3,7):
        ans=brute(n)
        assert ans==theorem(n),(n,ans,theorem(n))
    # Finite-state cycle count, independent of brute enumeration.
    for n in range(3,49):
        count=Counter()
        for component in recurrent:
           # Each SCC is a single simple directed cycle.
           length=len(component)
           if n%length==0:
               for state in component:
                   weight=sum(bit(v[0],j) for v in component for j in range(3))
                   count[n*weight//length]+=1
        assert count==theorem(n),(n,count)
    print('VERIFY_OK states=42 arcs=102 cyclic_SCCs=1+6 brute_prisms_n=3..6 exact_all_n_by_cycle_classification')

if __name__=='__main__':main()
