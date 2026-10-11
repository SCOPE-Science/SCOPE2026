"""Finite stress test for the finite equilateral free p-space tree norm.
This is not a proof of the all-n theorem.
"""
import itertools, random, math

def trees(n):
    for code in itertools.product(range(n), repeat=n-2):
        counts=[1]*n
        for v in code: counts[v]+=1
        edges=[]
        for v in code:
            u=next(j for j in range(n) if counts[j]==1)
            edges.append((u,v));counts[u]-=1;counts[v]-=1
        rem=[i for i,c in enumerate(counts) if c==1]
        edges.append(tuple(rem))
        yield edges

def tree_norm_p(mu,p,es):
    n=len(mu);adj=[[] for _ in range(n)]
    for a,b in es:adj[a].append(b);adj[b].append(a)
    parent=[-1]*n;order=[0];parent[0]=0
    for u in order:
        for v in adj[u]:
            if parent[v]<0:parent[v]=u;order.append(v)
    subtotal=list(mu);cost=0
    for u in reversed(order[1:]):
        cost+=abs(subtotal[u])**p
        subtotal[parent[u]]+=subtotal[u]
    return 2*cost**(1/p)

def exact_via_trees(lam,p,ts):
    n=len(lam)
    return max(min(tree_norm_p([lam[i]-(j==i) for i in range(n)],p,t) for t in ts) for j in range(n))

rng=random.Random(5023)
for n in range(4,7):
    ts=list(trees(n)); print('n',n,'trees',len(ts))
    for p in (0.45,0.7,0.83,1.0):
        goal=min(2, 2/n*(n-1)**(1/p))
        choices=[]
        for i in range(n):
            lam=[float(j==i) for j in range(n)]
            choices.append(exact_via_trees(lam,p,ts))
        choices.append(exact_via_trees([1/n]*n,p,ts))
        assert abs(min(choices)-goal)<1e-9,(n,p,min(choices),goal)
        for _ in range(20):
            lam=[rng.expovariate(1) for i in range(n)]
            s=sum(lam);lam=[x/s for x in lam]
            r=exact_via_trees(lam,p,ts)
            assert r+1e-9>=goal,(n,p,r,goal,lam)
        print(f' p={p} target={goal:.12f} tests=20:PASS')
print('FINITE_STRESS_PASS (not exhaustive over centers, not a proof)')
