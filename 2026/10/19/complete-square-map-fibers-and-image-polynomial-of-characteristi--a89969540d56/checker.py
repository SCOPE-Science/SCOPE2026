#!/usr/bin/env python3
"""Independent finite-field and graph checks for graphical-group square fibers."""
from itertools import product, combinations
from collections import Counter

class GF:
    def __init__(self, q):
        self.q=q
        self.poly={2:0b11,4:0b111,8:0b1011}[q]
        self.k=q.bit_length()-1
    def mul(self, a,b):
        r=0
        for _ in range(self.k*2):
            if b&1: r^=a
            b >>= 1
            a <<= 1
            if a & self.q: a ^= self.poly
            if b==0: break
        return r
    def div(self,a,b):
        assert b
        return self.mul(a,next(t for t in range(1,self.q) if self.mul(b,t)==1))

def independent_poly_eval_on_vertices(vertices,edges,q):
    vertices=tuple(sorted(vertices))
    return sum((q-1)**len(S) for r in range(len(vertices)+1) for S in combinations(vertices,r) if all(i not in S or j not in S for i,j in edges))

def independent_poly_eval(n,edges,q):
    return independent_poly_eval_on_vertices(range(n),edges,q)

def predicted_fiber(n,edges,target,F):
    q=F.q
    positive=[e for e,y in zip(edges,target) if y]
    W=set(v for i,j in positive for v in (i,j))
    if any(i in W and j in W and not y for (i,j),y in zip(edges,target)):
        return 0
    excluded=set(W)
    for i,j in edges:
        if i in W or j in W: excluded.update((i,j))
    R=set(range(n))-excluded
    nfree=independent_poly_eval_on_vertices(R,[(i,j) for i,j in edges if i in R and j in R],q)
    adj={v:[] for v in W}
    for (i,j),y in zip(edges,target):
        if y: adj[i].append((j,y));adj[j].append((i,y))
    seen=set(); factors=1
    for root in sorted(W):
        if root in seen:continue
        stack=[root]; seen.add(root); vertices=[]
        while stack:
            u=stack.pop();vertices.append(u)
            for v,y in adj[u]:
                if v not in seen:seen.add(v);stack.append(v)
        good=0
        for start in range(1,q):
            vals={root:start};pending=[root]
            while pending:
                u=pending.pop()
                for v,y in adj[u]:
                    if v not in vals:
                        vals[v]=F.div(y,vals[u]);pending.append(v)
            if all(F.mul(vals[u],vals[v])==y for u in vertices for v,y in adj[u]):
                good+=1
        factors*=good
    return factors*nfree

def predicted_distinct_squares(n,edges,q):
    result=0
    for mask in range(1<<n):
        W={v for v in range(n) if mask>>v&1}
        adj={v:set() for v in W}
        for u,v in edges:
            if u in W and v in W:
                adj[u].add(v);adj[v].add(u)
        if any(not adj[u] for u in W): continue
        seen=set(); b=0
        for root in W:
            if root in seen:continue
            depth={root:0};stack=[root];seen.add(root); bipartite=True
            while stack:
                u=stack.pop()
                for v in adj[u]:
                    if v not in depth:
                        depth[v]=1-depth[u];seen.add(v);stack.append(v)
                    elif depth[v]==depth[u]: bipartite=False
            if bipartite:b+=1
        result+=(q-1)**(len(W)-b)
    return result

def run_case(q,n,edges):
    F=GF(q)
    observed=Counter()
    for x in product(range(q),repeat=n):
        result=tuple(F.mul(x[i],x[j]) for i,j in edges)
        observed[result]+=1
    for target in product(range(q),repeat=len(edges)):
        expected=predicted_fiber(n,edges,target,F)
        assert observed[target]==expected,(q,n,edges,target,observed[target],expected)
    assert sum(observed.values())==q**n
    assert observed[(0,)*len(edges)]==independent_poly_eval(n,edges,q)
    assert len(observed)==predicted_distinct_squares(n,edges,q), (q,n,edges,len(observed),predicted_distinct_squares(n,edges,q))
    if n<=4 and len(edges)<=4 and q<=4:
        # Independent check of the actual group square using its multiplication law.
        for x in product(range(q), repeat=n):
            for z in product(range(q),repeat=len(edges)):
                product_v=tuple(a^a for a in x)
                product_z=tuple(z[t]^z[t]^F.mul(x[i],x[j]) for t,(i,j) in enumerate(edges))
                assert product_v==(0,)*n
                assert product_z==tuple(F.mul(x[i],x[j]) for i,j in edges)
    print('PASS',q,n,len(edges),'square targets',q**len(edges),'inputs',q**n,
          'zero-target',observed[(0,)*len(edges)],'nonzero-targets',len(observed)-1)

if __name__=='__main__':
    graphs={
        'empty3':(3,()),'edge2':(2,((0,1),)),
        'P3':(3,((0,1),(1,2))),
        'triangle':(3,((0,1),(1,2),(0,2))),
        'P4':(4,((0,1),(1,2),(2,3))),
        'C4':(4,((0,1),(1,2),(2,3),(0,3))),
        'K4':(4,tuple(combinations(range(4),2))),
        'two_components':(5,((0,1),(1,2),(0,2),(3,4))),
        'C5':(5,((0,1),(1,2),(2,3),(3,4),(4,0))),
    }
    tests=[(q,name) for q in (2,4,8) for name in graphs if (q,name) not in ((8,'K4'),(8,'C5'),(8,'two_components'))]
    for q,name in tests:
        n,edges=graphs[name]
        run_case(q,n,edges)
    print('ALL_EXACT_SQUARE_FIBER_CHECKS_PASSED',len(tests))
