"""Exact enumeration of isolate/component-size covariance in G(n,p)."""
from fractions import Fraction
from itertools import combinations
import math
from collections import deque

checks=0
for n in range(3,7):
    edges=list(combinations(range(n),2)); M=len(edges)
    for pr in (Fraction(1,5),Fraction(2,5),Fraction(3,5)):
        weights=[pr**e*(1-pr)**(M-e) for e in range(M+1)]
        c0=Fraction(0); c=[Fraction(0)]*(n+1); cross=[Fraction(0)]*(n+1)
        # distinguish graph shape inside components: number of tree components (size k)
        tree=[Fraction(0)]*(n+1); cross_tree=[Fraction(0)]*(n+1)
        for mask in range(1<<M):
            adj=[[] for _ in range(n)]; E=mask.bit_count(); w=weights[E]
            for e,(u,v) in enumerate(edges):
                if mask>>e&1:adj[u].append(v);adj[v].append(u)
            isolates=sum(not x for x in adj)
            visited=set(); sizes=[]; t_sizes=[]
            for u in range(n):
                if u in visited:continue
                seen={u}; que=[u]
                for v in que:
                    for z in adj[v]:
                        if z not in seen:seen.add(z);que.append(z)
                visited.update(seen); k=len(seen)
                sizes.append(k)
                if sum(len(adj[v]) for v in seen)==2*(k-1):t_sizes.append(k)
            c0+=w*isolates
            for k in range(2,n):
                ncomp=sizes.count(k); ntree=t_sizes.count(k)
                c[k]+=w*ncomp;cross[k]+=w*isolates*ncomp
                tree[k]+=w*ntree;cross_tree[k]+=w*isolates*ntree
        assert c0==n*(1-pr)**(n-1)
        for k in range(2,n):
            factor=(n-k)/(n*(1-pr)**k)-1
            lhs=cross[k]-c0*c[k]
            rhs=c0*c[k]*factor
            assert lhs==rhs,(n,k,pr,'all',lhs,rhs)
            checks+=1
            lhs=cross_tree[k]-c0*tree[k];rhs=c0*tree[k]*factor
            assert lhs==rhs,(n,k,pr,'tree',lhs,rhs)
            checks+=1
        print('n',n,'p',str(pr),'passed')
print('CHECKS',checks)
