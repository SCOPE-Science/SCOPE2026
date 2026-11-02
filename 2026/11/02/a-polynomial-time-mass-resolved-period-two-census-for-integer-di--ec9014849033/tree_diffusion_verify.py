#!/usr/bin/env python3
"""Independent finite checks of a tree diffusion orbit-count recurrence."""
from itertools import product
from collections import defaultdict

def count_dp(n, edges):
    if n < 1 or len(edges) != n - 1:
        raise ValueError('Expected a nonempty tree.')
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b); adj[b].append(a)
    parent = [-2] * n
    parent[0] = -1
    order = [0]
    for v in order:
        for w in adj[v]:
            if w == parent[v]: continue
            if parent[w] != -2: raise ValueError('Not a tree.')
            parent[w] = v
            order.append(w)
    if len(order) != n: raise ValueError('Disconnected.')
    F = [None] * n
    for v in reversed(order):
        children = [w for w in adj[v] if w != parent[v]]
        deg = len(adj[v])
        Fv = {(s,q):0 for s in (-1,0,1) for q in range(-deg,deg+1)}
        for q in range(-deg,deg+1):
            accum = {0: 1}
            for w in children:
                contrib = {}
                for t in (-1,0,1):
                    val = 0
                    for qw in range(-len(adj[w]),len(adj[w])+1):
                        ct = F[w][-t,qw]
                        if t == 0:
                            wt = int(q == qw)
                        else:
                            wt = max(0,t*(q-qw)-1)
                        val += ct * wt
                    contrib[t] = val
                nxt = defaultdict(int)
                for total, ways in accum.items():
                    for t, val in contrib.items():
                        nxt[total+t] += ways * val
                accum = nxt
            for s in (-1,0,1):
                Fv[s,q] = accum.get(q-s,0)
        F[v] = Fv
    classes = sum(F[0][0,q] for q in range(-len(adj[0]),len(adj[0])+1))
    assert classes%2==1
    return classes,(classes-1)//2

def count_brute(n, edges):
    assert len(edges) == n-1
    val = 0
    for s in product((-1,0,1), repeat=len(edges)):
        q = [0]*n
        for (u,v),t in zip(edges,s):
            q[u] += t; q[v] -= t
        ways = 1
        for (u,v),t in zip(edges,s):
            d=q[u]-q[v]
            if t == 0:
                if d: ways=0;break
            else:
                ways *= max(0,t*d-1)
        val += ways
    return val,(val-1)//2

def direct_periodic(n,edges,grid):
    adj=[[] for _ in range(n)]
    for u,v in edges:adj[u].append(v);adj[v].append(u)
    count=0
    for z in product(range(-grid,grid+1),repeat=n-1):
        x=(0,)+z
        def F(y):
            return tuple(y[u]+sum((y[w]>y[u])-(y[w]<y[u]) for w in adj[u]) for u in range(n))
        y=F(x)
        if F(y)==x: count += 1
    return count

# Seven small labelled trees, including nonisomorphic degree-multiset twins.
shapes=[
 [(0,1),(1,2),(2,3),(3,4),(4,5)],
 [(0,1),(0,2),(0,3),(0,4),(0,5)],
 [(0,1),(0,2),(0,3),(3,4),(4,5)],
 [(0,1),(0,2),(0,3),(1,4),(1,5)],
 [(0,1),(0,2),(0,3),(3,4),(3,5)],
 [(0,1),(0,2),(2,3),(3,4),(3,5)],
 [(0,3),(0,5),(1,0),(1,2),(3,4)]
]
if __name__ == '__main__':
    tested=0
    for n in range(2,7):
        # Every labelled tree via Prüfer sequences, including multiplicities.
        for seq in product(range(n),repeat=n-2):
            degrees=[1]*n
            for u in seq:degrees[u]+=1
            edges=[]
            for u in seq:
                v=next(v for v in range(n) if degrees[v]==1)
                edges.append((u,v));degrees[u]-=1;degrees[v]-=1
            leaves=[v for v in range(n) if degrees[v]==1]
            edges.append(tuple(leaves))
            actual=count_dp(n,edges)
            expected=count_brute(n,edges)
            assert actual==expected,(n,edges,actual,expected)
            tested+=1
    print('DP_BRUTE_ALL_LABELLED_TREES_OK',tested)
    for j,edges in enumerate(shapes):
        dp=count_dp(6,edges)
        brute=count_brute(6,edges)
        direct=direct_periodic(6,edges,7)
        assert dp==brute and direct==dp[0],(j,dp,brute,direct)
        degree=sorted(sum(u in e for e in edges) for u in range(6))
        print('SIX_NODE_SHAPE',j,'degree',degree,'edges',edges,'periodic_classes',dp[0],'primitive_orbits',dp[1])
    for n in (10,20,40,80):
        path=[(u,u+1) for u in range(n-1)]
        star=[(0,u) for u in range(1,n)]
        print('PATH',n,count_dp(n,path))
        print('STAR',n,count_dp(n,star))
    print('TREE_DIFFUSION_DP_VERIFIED')

def count_mass_dp(n, edges):
    """Return counts of states of period <= 2 at each chip-sum residue mod n."""
    if n == 1: return [1]
    adj=[[] for _ in range(n)]
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    parent=[-2]*n; parent[0]=-1; order=[0]
    for v in order:
        for w in adj[v]:
            if w != parent[v]:
                if parent[w] != -2:raise ValueError('Not a tree')
                parent[w]=v;order.append(w)
    if len(order)!=n:raise ValueError('Disconnected')
    sz=[1]*n
    for v in reversed(order[1:]):sz[parent[v]] += sz[v]
    F=[None]*n
    zero=(0,)*n; identity=(1,)+(0,)*(n-1)
    def mul(a,b):
        c=[0]*n
        for i,ai in enumerate(a):
            if not ai:continue
            for j,bj in enumerate(b):
                if bj:c[(i+j)%n]+=ai*bj
        return tuple(c)
    for v in reversed(order):
        ch=[w for w in adj[v] if w != parent[v]]
        d=len(adj[v]); Fv={}
        for q in range(-d,d+1):
            acc={0:identity}
            for w in ch:
                cn={t:[0]*n for t in (-1,0,1)}
                for t in (-1,0,1):
                    for qw in range(-len(adj[w]),len(adj[w])+1):
                        src=F[w][-t,qw]
                        if t==0:
                            if q!=qw: continue
                            weights=identity
                        else:
                            L=max(0,t*(q-qw)-1)
                            weights=[0]*n
                            for k in range(1,L+1):weights[(-sz[w]*t*k)%n]+=1
                        prod=mul(src,weights)
                        for i,z in enumerate(prod):cn[t][i]+=z
                nxt={}
                for idx,prefix in acc.items():
                    for t in (-1,0,1):
                        prod=mul(prefix,cn[t])
                        key=idx+t
                        old=nxt.get(key,zero)
                        nxt[key]=tuple(a+b for a,b in zip(old,prod))
                acc=nxt
            for s in (-1,0,1):Fv[s,q]=acc.get(q-s,zero)
        F[v]=Fv
    out=[0]*n
    for q in range(-len(adj[0]),len(adj[0])+1):
        for i,x in enumerate(F[0][0,q]):out[i]+=x
    return out

def count_mass_brute(n,edges):
    adj=[[] for _ in range(n)]
    for u,v in edges:adj[u].append(v);adj[v].append(u)
    parent=[-2]*n;parent[0]=-1;order=[0]
    for v in order:
        for w in adj[v]:
            if w != parent[v]:parent[w]=v;order.append(w)
    sz=[1]*n
    for v in reversed(order[1:]):sz[parent[v]]+=sz[v]
    ord_edges=[(parent[w],w) for w in order[1:]]
    counts=[0]*n
    for s in product((-1,0,1),repeat=n-1):
        q=[0]*n
        for (u,v),t in zip(ord_edges,s):q[u]+=t;q[v]-=t
        allowed=[]
        for (u,v),t in zip(ord_edges,s):
            delta=q[u]-q[v]
            if t==0:
                allowed.append((0,) if delta==0 else ())
            else:
                allowed.append(tuple(t*k for k in range(1,max(0,t*delta-1)+1)))
        for gaps in product(*allowed):
            residue=(-sum(sz[v]*d for (u,v),d in zip(ord_edges,gaps)))%n
            counts[residue]+=1
    return counts

if __name__=='__main__':
    for n in range(1,7):
        if n==1:
            es=[[]]
        else:
            es=[]
            for seq in product(range(n),repeat=n-2):
                degree=[1]*n
                for x in seq:degree[x]+=1
                e=[]
                for x in seq:
                    y=next(v for v in range(n) if degree[v]==1)
                    e.append((x,y));degree[y]-=1;degree[x]-=1
                ends=[x for x in range(n) if degree[x]==1]
                e.append(tuple(ends));es.append(e)
        for e in es:
            d=count_mass_dp(n,e)
            b=count_mass_brute(n,e)
            assert d==b and sum(d)==count_dp(n,e)[0],(n,e,d,b)
        print('MASS_DP_BRUTE_LABELED_TREES_OK',n,len(es))
    for label,e in (('A',[(0,4),(1,0),(1,2),(1,3),(4,5)]),
                     ('B',[(0,3),(0,5),(1,0),(1,2),(3,4)])):
        c=count_mass_dp(6,e)
        assert sum(c)==count_dp(6,e)[0]
        print('DEGREE_TWIN',label,'mass_fixed_state_counts',c,'primitive_orbits_per_mass_residue',[(x-int(i==0))//2 for i,x in enumerate(c)])
    print('TREE_MASS_DP_VERIFIED')
