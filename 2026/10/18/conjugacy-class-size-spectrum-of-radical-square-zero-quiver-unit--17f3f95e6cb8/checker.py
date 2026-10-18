#!/usr/bin/env python3
"""Independent finite-field unit-group and graph-subset checks."""
from itertools import product, combinations
from collections import Counter
from math import prod


def add(a,b,q): return a^b if q==4 else (a+b)%q

def mul(a,b,q):
    if q!=4:return a*b%q
    c=0
    for i in range(2):
        for j in range(2):
            if a>>i&1 and b>>j&1:c ^= (1<<(i+j))
    if c&8:raise AssertionError('unexpected')
    if c&4:c^=7 # x^2 = x+1
    return c

def group_items(n,edges,loops,q):
    arrows=list(edges)+[(v,v) for v in loops]
    units=[(t,x) for t in product(range(1,q),repeat=n)
           for x in product(range(q),repeat=len(arrows))]
    return units,arrows

def group_product(g,h,arrows,q):
    t,x=g; s,y=h
    ts=tuple(mul(a,b,q) for a,b in zip(t,s))
    z=tuple(add(mul(t[u],y[e],q),mul(x[e],s[v],q),q)
            for e,(u,v) in enumerate(arrows))
    return ts,z

def count_components(n,edges):
    parent=list(range(n))
    def find(a):
        while parent[a]!=a:a=parent[a]
        return a
    for a,b in edges:
        ra,rb=find(a),find(b)
        parent[ra]=rb
    return len({find(i) for i in range(n)})

def predicted(n,edges,loops,q):
    # Collapse parallel/opposite arrows into undirected edge multiplicities.
    es=Counter(tuple(sorted(e)) for e in edges if e[0]!=e[1]);
    E=sorted(es); m=sum(es.values()); h=len(loops)
    subsets=lambda xs:(tuple(xs[i] for i in range(len(xs)) if mask>>i&1)
                        for mask in range(1<<len(xs)))
    class_num=0
    for F in subsets(E):
        c=count_components(n,F)
        beta=len(F)-n+c
        term=q**h*(q-1)**(c+beta)*prod(sum(q**es[e]-1 for _ in range(1))//(q-1) for e in F)
        class_num+=term
    # Exact class-size polynomial via labelled vertex colors and support F.
    # This is independent of the ambient unit-group multiplication.
    dist=Counter()
    for t in product(range(1,q),repeat=n):
        B={e for e in E if t[e[0]]==t[e[1]]}
        outside=sum(es[e] for e in E if e not in B)
        for F in subsets(sorted(B)):
            c=count_components(n,F)
            beta=len(F)-n+c
            num=q**h*(q-1)**beta*prod((q**es[e]-1)//(q-1) for e in F)
            size=q**outside*(q-1)**(n-c)
            dist[size]+=num
    return class_num,dist

def direct(n,edges,loops,q):
    items,arrows=group_items(n,edges,loops,q)
    N=len(items)
    by_size=Counter()
    for g in items:
        # Full multiplication, not centralizer-formula shortcuts.
        cen=sum(group_product(g,h,arrows,q)==group_product(h,g,arrows,q) for h in items)
        assert N%cen==0
        by_size[N//cen]+=1
    assert all(count % size==0 for size,count in by_size.items())
    return sum(count//s for s,count in by_size.items()),Counter({s:count//s for s,count in by_size.items()})

def go():
    cases=[
      ('isolated',3,[],[],3),
      ('single_arrow',2,[(0,1)],[],5),
      ('two_opposites',2,[(0,1),(1,0)],[],3),
      ('two_parallel',2,[(0,1),(0,1)],[],3),
      ('loop_and_arrow',2,[(0,1)],[0],3),
      ('path3',3,[(0,1),(1,2)],[],3),
      ('fork3',3,[(0,1),(0,2)],[],3),
      ('triangle3',3,[(0,1),(1,2),(2,0)],[],3),
      ('cycle4_binary',4,[(0,1),(1,2),(2,3),(3,0)],[],2),
      ('double_disconnected',3,[(0,1),(0,1)],[2],2),
      ('single_GF4',2,[(0,1)],[],4),
    ]
    for name,n,edges,loops,q in cases:
        expected_e,expected_d=predicted(n,edges,loops,q)
        actual_e,actual_d=direct(n,edges,loops,q)
        assert expected_e==actual_e,(name,'k',expected_e,actual_e)
        assert expected_d==actual_d,(name,'distribution',expected_d,actual_d)
        print(name,'q=',q,'classes=',actual_e,'spectrum=',dict(sorted(actual_d.items())))
    # Independent graph-subset calculation of a bridge-detection witness.
    g1=[(0,1),(0,2),(0,3),(0,4),(1,3),(1,5),(2,3),(2,5)]
    g2=[(0,4),(0,5),(1,3),(1,4),(2,3),(2,4),(3,4),(4,5)]
    k1,d1=predicted(6,g1,[],3); k2,d2=predicted(6,g2,[],3)
    assert k1==k2==2340 and d1[3]==2 and d2[3]==0
    assert sum(s*n for s,n in d1.items())==sum(s*n for s,n in d2.items())==2**6*3**8
    # In a connected underlying graph with no loops, singleton
    # bridge edges give precisely (q-1)(q-2) size-q classes.
    for graph,ds in ((g1,d1),(g2,d2)):
        assert count_components(6,graph)==1
        bridges=sum(count_components(6,graph[:i]+graph[i+1:])>1
                    for i in range(len(graph)))
        assert ds[3]==2*bridges
    print('BRIDGE_SPECTRUM_WITNESS_PASSED',k1,d1[3],d2[3])
    print('ALL_QUOTIENT_UNIT_CLASS_TESTS_PASSED',len(cases))
if __name__=='__main__':go()
