#!/usr/bin/env python3
from itertools import combinations

W = {1:0, 2:1, 3:3, 4:6, 5:10, 6:11}
DELTA = [0,1,2,3,2]

def edge_count(adj):
    return sum(len(s) for s in adj)//2

def add_edge(adj,u,v):
    adj[u].add(v); adj[v].add(u)

def clique(n):
    a=[set() for _ in range(n)]
    for u,v in combinations(range(n),2): add_edge(a,u,v)
    return a

def disjoint(graphs):
    n=sum(len(g) for g in graphs); a=[set() for _ in range(n)]; off=0
    for g in graphs:
        for u in range(len(g)):
            for v in g[u]:
                if u<v: add_edge(a,off+u,off+v)
        off+=len(g)
    return a

def join(g,h):
    a=disjoint([g,h]); n=len(g)
    for u in range(n):
        for v in range(n,n+len(h)): add_edge(a,u,v)
    return a

def B6():
    # (K2 union K1) join (K2 union K1)
    side=disjoint([clique(2),clique(1)])
    return join(side,side)

def B8():
    side=disjoint([clique(2),clique(2)])
    return join(side,side)

def max_common(adj):
    m=0
    for u,v in combinations(range(len(adj)),2):
        m=max(m,len(adj[u] & adj[v]))
    return m

def is_k2t_free(adj,t): return max_common(adj) < t

def is_cograph(adj):
    for Q in combinations(range(len(adj)),4):
        deg=[]; e=0
        for u in Q:
            d=sum(v in adj[u] for v in Q if v!=u)
            deg.append(d); e+=d
        if e//2==3 and sorted(deg)==[1,1,2,2]:
            return False
    return True

def graph_from_mask(n,mask):
    a=[set() for _ in range(n)]; bit=0
    for u,v in combinations(range(n),2):
        if (mask>>bit)&1: add_edge(a,u,v)
        bit+=1
    return a

def local_maxima():
    out=[]; examined=0
    for n in range(1,7):
        best=-1
        for mask in range(1 << (n*(n-1)//2)):
            examined+=1
            a=graph_from_mask(n,mask)
            if max((len(s) for s in a),default=0)>4: continue
            if not is_cograph(a): continue
            if not is_k2t_free(a,4): continue
            best=max(best,edge_count(a))
        out.append(best)
    assert out == [0,1,3,6,10,11], out
    return examined

def dp_opt(m):
    dp=[-10**9]*(m+1); sets=[set() for _ in range(m+1)]
    dp[0]=0; sets[0].add((0,0,0,0,0,0))
    for x in range(1,m+1):
        for d in range(1,7):
            if d>x: continue
            val=dp[x-d]+W[d]
            if val>dp[x]: dp[x]=val; sets[x].clear()
            if val==dp[x]:
                for p in sets[x-d]:
                    q=list(p); q[d-1]+=1; sets[x].add(tuple(q))
    return dp[m],sets[m]

def expected_opt_sets(m):
    q,r=divmod(m,5)
    if r==0: return {(0,0,0,0,q,0)}
    if r==1: return {(0,0,0,0,q-1,1)}
    if r==2: return {(0,0,0,0,q-2,2)}
    if r==3:
        s={(0,0,1,0,q,0)}
        if q>=3: s.add((0,0,0,0,q-3,3))
        return s
    return {(0,0,0,1,q,0)}

def extremal(n,alternate=False):
    if n<=6: return clique(n)
    if n==7: return join(clique(1),B6())
    if n==8: return B8()
    m=n-1; q,r=divmod(m,5); blocks=[]
    if r==0: blocks=[clique(5) for _ in range(q)]
    elif r==1: blocks=[clique(5) for _ in range(q-1)]+[B6()]
    elif r==2: blocks=[clique(5) for _ in range(q-2)]+[B6(),B6()]
    elif r==3:
        if alternate and q>=3: blocks=[clique(5) for _ in range(q-3)]+[B6(),B6(),B6()]
        else: blocks=[clique(5) for _ in range(q)]+[clique(3)]
    else: blocks=[clique(5) for _ in range(q)]+[clique(4)]
    return join(clique(1),disjoint(blocks))

def formula(n):
    if n<=6: return n*(n-1)//2
    if n==7: return 17
    if n==8: return 20
    m=n-1; return 3*m-DELTA[m%5]

def main():
    examined=local_maxima()
    for m in range(8,501):
        val,ss=dp_opt(m)
        assert val==2*m-DELTA[m%5], (m,val)
        assert ss==expected_opt_sets(m), (m,ss,expected_opt_sets(m))
    alt=0
    for n in range(1,41):
        g=extremal(n)
        assert len(g)==n and is_cograph(g) and is_k2t_free(g,5)
        assert edge_count(g)==formula(n), (n,edge_count(g),formula(n))
        if n>=19 and (n-1)%5==3:
            h=extremal(n,alternate=True); alt+=1
            assert is_cograph(h) and is_k2t_free(h,5) and edge_count(h)==formula(n)
    print(f"ALL CHECKS PASSED; local_graphs_examined={examined}; knapsack_m=8..500; construction_n=1..40; alternate_residue3_cases={alt}")
if __name__=='__main__': main()
