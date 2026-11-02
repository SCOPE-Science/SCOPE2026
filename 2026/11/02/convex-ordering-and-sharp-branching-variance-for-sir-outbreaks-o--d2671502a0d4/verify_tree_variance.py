"""Exact finite-state check of a rooted-tree SIR outbreak-variance formula.
Uses independent polynomial probability-generating functions, not the pair identity.
"""
from collections import deque
from fractions import Fraction as F
from itertools import product


def adj_from_prufer(seq):
    n=len(seq)+2
    deg=[1]*n
    for x in seq: deg[x]+=1
    edges=[]
    for x in seq:
        leaf=next(i for i in range(n) if deg[i]==1)
        edges.append((leaf,x));deg[leaf]-=1;deg[x]-=1
    u,v=[i for i in range(n) if deg[i]==1]
    edges.append((u,v))
    adj=[[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v);adj[v].append(u)
    return adj


def poly_mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out


def pgf(adj,r,distribution):
    parent={r:None};order=[r]
    for v in order:
        for c in adj[v]:
            if c not in parent:parent[c]=v;order.append(c)
    pg={}
    for v in order[::-1]:
        children=[u for u in adj[v] if u!=parent[v]]
        terms=[]
        for theta,wt in distribution:
            q=[F(1)]
            for u in children:
                h=pg[u]
                term=[(F(1)-theta)+theta*h[0]]+[theta*x for x in h[1:]]
                q=poly_mul(q,term)
            terms.append((q,wt))
        out=[F(0)]*(max(map(lambda t:len(t[0]),terms))+1)
        for q,wt in terms:
            for i,x in enumerate(q): out[i+1]+=wt*x
        pg[v]=out
    return pg[r]


def analytic(adj,r,p):
    n=len(adj);parent={r:None};depth={r:0};order=[r]
    for v in order:
        for u in adj[v]:
            if u not in parent:parent[u]=v;depth[u]=depth[v]+1;order.append(u)
    anc={}
    for v in order:
        path=set();u=v
        while u is not None:path.add(u);u=parent[u]
        anc[v]=path
    def lca_depth(v,w):return max(depth[z] for z in anc[v]&anc[w])
    m=sum(p**depth[v] for v in range(n))
    eb2=sum(p**depth[v] for v in range(n))
    B=F(0)
    for v in range(n):
        for w in range(v+1,n):
            l=lca_depth(v,w)
            eb2+=2*p**(depth[v]+depth[w]-l)
            if v not in anc[w] and w not in anc[v]:
                B+=2*p**(depth[v]+depth[w]-l-2)
    # Separate subtree recursion to cross-check the expression for B.
    h={}
    for v in order[::-1]:
        h[v]=1+p*sum(h[u] for u in adj[v] if u!=parent[v])
    B2=F(0)
    for v in order:
        children=[u for u in adj[v] if u!=parent[v]]
        B2+=2*p**depth[v]*sum(h[children[i]]*h[children[j]] for i in range(len(children)) for j in range(i+1,len(children)))
    assert B==B2,(r,adj,B,B2)
    return m,eb2-m*m,B


def run():
    total=0; nonzero=0
    laws=[[(F(1,5),F(2,3)),(F(4,5),F(1,3))],[(F(0),F(1,2)),(F(1),F(1,2))],[(F(1,2),F(1))]]
    for n in range(2,7):
        for code in product(range(n),repeat=n-2):
            adj=adj_from_prufer(code)
            for root in range(n):
                for law in laws:
                    p=sum(theta*wt for theta,wt in law)
                    q=sum(theta**2*wt for theta,wt in law)
                    m,v0,B=analytic(adj,root,p)
                    poly=pgf(adj,root,law)
                    assert sum(poly)==1
                    m2=sum(i*x for i,x in enumerate(poly))
                    v2=sum(i*i*x for i,x in enumerate(poly))-m2*m2
                    assert (m2,v2)==(m,v0+(q-p*p)*B),(n,code,root,law,m2,v2,m,v0,B)
                    assert 0<=B<=(n-1)*(n-2)
                    if B:nonzero+=1
                    total+=1
        print('n=',n,'cumulative comparisons=',total)
    print('PASS',total, 'exact rooted tree/law comparisons; nonzero branch coefficients:',nonzero)
    star=[[1,2,3,4],[0],[0],[0],[0]]
    p=F(1,2)
    m,v0,B=analytic(star,0,p)
    assert (m,v0,B)==(F(3),F(1),F(12)),(m,v0,B)
    q=F(1,3) # exp recovery beta=gamma, conditional transmissibility uniform [0,1]
    assert v0+(q-p*p)*B==F(2)
    print('Star-5: mean=3, deterministic-period variance=1, exponential-period variance=2; B=12')
if __name__=='__main__': run()
