"""Exact finite-field verification of cyclic extensions in weighted evolution algebras.
Python 3 standard library; if networkx is installed, independently enumerates graph automorphisms.
"""
from itertools import product
from math import gcd,lcm
from collections import Counter

def order(a,p):
    t=a%p;n=1
    while t!=1:
        t=t*a%p;n+=1
        assert n<p
    return n

def rank(a,p):
    a=[r[:] for r in a];n=len(a);k=0
    for j in range(n):
        i=next((i for i in range(k,n) if a[i][j]%p),None)
        if i is None: continue
        a[k],a[i]=a[i],a[k]
        s=pow(a[k][j],-1,p);a[k]=[x*s%p for x in a[k]]
        for i in range(n):
            if i!=k and a[i][j]:
                t=a[i][j];a[i]=[(x-t*y)%p for x,y in zip(a[i],a[k])]
        k+=1
    return k

def test(m,h,p,xi,r,exhaustive=True):
    M=2**h-1;a=pow(xi,r,p);n=m*h
    assert order(xi,p)==M
    assert (1-(-1)**m*a)%p!=0
    c=[1]*m;c[-1]=a
    ix=lambda i,j:(i%m)*h+j
    B=[[0]*n for _ in range(n)]
    for i in range(m):
        for j in range(h):
            if j==0:
                B[ix(i,0)][ix(i,1)]=1
                B[ix(i,0)][ix(i+1,1)]=c[i]
            else:B[ix(i,j)][ix(i,(j+1)%h)]=1
    assert rank(B,p)==n
    R=[t for t in range(1,p) if pow(t,M,p)==1]
    assert len(R)==M
    inv2=pow(2,-1,M)
    t=[pow(z,inv2,p) for z in c]
    def valid(shift,base):
        perm=[ix(i+shift,j) for i in range(m) for j in range(h)]
        fac=[pow(base[i],2**j,p) for i in range(m) for j in range(h)]
        return all((B[v][u]*fac[u]-fac[v]**2*B[perm[v]][perm[u]])%p==0
                   for v in range(n) for u in range(n))
    assert valid(1,t)
    pr=1
    for s in t:pr=pr*s%p
    assert pr==pow(a,inv2,p)
    # For all roots and every block-rotation, exhaustively count monomial automorphisms.
    if exhaustive:
        good=[]
        for shift in range(m):
            for base in product(R,repeat=m):
                if valid(shift,base):good.append((shift,base))
        assert len(good)==m*M,('count',len(good),m*M)
        # Compare the complete multiset of group-element orders with Smith normal form.
        def ord_monomial(shift,base):
            perm=[ix(i+shift,j) for i in range(m) for j in range(h)]
            fac=[pow(base[i],2**j,p) for i in range(m) for j in range(h)]
            seen=set();ans=1
            for v in range(n):
                if v in seen:continue
                cur=v;prod=1;length=0
                while cur not in seen:
                    seen.add(cur);prod=prod*fac[cur]%p;length+=1;cur=perm[cur]
                ans=lcm(ans,length*order(prod,p))
            return ans
        got=Counter(ord_monomial(s,b) for s,b in good)
        g=gcd(M,m,r);expected=Counter(lcm(g//gcd(g,u), (m*M//g)//gcd(m*M//g,v))
            for u in range(g) for v in range(m*M//g))
        assert got==expected, ('group invariant mismatch',got,expected)
        # Enumerate ALL support-graph automorphisms when networkx is available.
        try:
            import networkx as nx
            from networkx.algorithms.isomorphism import DiGraphMatcher
            G=nx.DiGraph();G.add_nodes_from(range(n))
            G.add_edges_from((v,u) for v in range(n) for u in range(n) if B[v][u])
            assert len(list(DiGraphMatcher(G,G).isomorphisms_iter()))==m
        except ImportError:pass
    g=gcd(M,m,r)
    print('CASE_OK',f'm={m}',f'h={h}',f'F={p}',f'twist={r}',
          f'aut=C_{g}xC_{m*M//g}',f'splits={gcd(m,M)!=0 and r%gcd(m,M)==0}',
          'exhaustive' if exhaustive else 'constructive')

if __name__=='__main__':
    for m,h,p,xi,r in [
        (3,2,7,2,0),(3,2,7,2,1),(4,2,7,2,1),(5,2,7,2,2),
        (3,3,29,16,0),(3,3,29,16,1),(4,3,29,16,1),
        (3,4,31,9,0),(3,4,31,9,1),(3,4,31,9,3),
        (5,4,31,9,5),(5,4,31,9,1),(6,2,7,2,1),
    ]:
        exhaustive=(m,h) not in ((5,4),(6,2))
        test(m,h,p,xi,r,exhaustive=exhaustive)
    print('VERIFY_OK')
