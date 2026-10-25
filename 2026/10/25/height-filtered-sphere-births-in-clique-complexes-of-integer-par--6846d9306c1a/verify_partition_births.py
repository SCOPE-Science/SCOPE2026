#!/usr/bin/env python3
"""Finite checks of partition-graph upper links and positive Betti-rank series.

Standard-library only. These checks corroborate, but do not prove, the
all-n topological theorem. Run: python3 verify_partition_births.py
"""
from functools import lru_cache

@lru_cache(None)
def partitions(n, cap=None):
    if cap is None: cap=n
    if n==0: return ((),)
    return tuple((s,)+tail for s in range(min(n,cap),0,-1)
                 for tail in partitions(n-s,s))

def height(p): return sum((i+1)*v for i,v in enumerate(p))

def neighbors(p):
    ans=set()
    for i in range(len(p)):
        for j in range(len(p)+1):
            if i==j: continue
            q=list(p); q[i]-=1
            if j==len(p): q.append(1)
            else: q[j]+=1
            q=tuple(sorted((v for v in q if v), reverse=True))
            if q!=p: ans.add(q)
    return ans

def transfer(p,a,b):
    q=list(p); q.remove(a); q.append(a-1)
    if b: q.remove(b); q.append(b+1)
    else: q.append(1)
    return tuple(sorted((v for v in q if v),reverse=True))

def edges_upper(p):
    S=set(p)
    return {(a,b) for a in S for b in S|{0} if a>=b+2}

def rank_by_support(p):
    S=set(p); M=max(p)
    return sum(1 for a in S for b in S if b+2<=a<M)

def count_cliques_euler(V,adj):
    V=sorted(V); chi=0; nfaces=0
    def visit(candidates,sign):
        nonlocal chi,nfaces
        for i,v in enumerate(candidates):
            chi+=sign; nfaces+=1
            tail=[w for w in candidates[i+1:] if w in adj[v]]
            visit(tail,-sign)
    visit(V,1)
    return chi,nfaces

def series(N):
    ans=[0]*(N+1)
    for M in range(4,N+1):
        # Restricted partition numbers from the Euler product.
        p=[0]*(N-M+1);p[0]=1
        for size in range(1,M+1):
            for j in range(size,len(p)):p[j]+=p[j-size]
        for a in range(3,M):
            for b in range(1,a-1):
                k=M+a+b
                for n in range(k,N+1): ans[n]+=p[n-k]
    return ans

def main():
    q=series(60)
    # Table 1 (n=1..25) in arXiv:2603.14370v1, public 2026-03-15.
    published=[0,0,0,0,0,0,0,1,2,5,10,19,32,55,87,137,207,310,
               451,652,921,1293,1787,2453,3324]
    assert q[1:26]==published
    vertices_checked=0
    for n in range(1,23):
        V=partitions(n)
        adj={p:neighbors(p) for p in V}
        local_sum=0
        for v in V:
            B=edges_upper(v)
            up={u for u in adj[v] if height(u)>height(v)}
            edge_to_neighbor={e:transfer(v,*e) for e in B}
            assert len(set(edge_to_neighbor.values()))==len(B)
            assert up==set(edge_to_neighbor.values())
            for e in B:
                for f in B:
                    if e==f:continue
                    lhs=edge_to_neighbor[f] in adj[edge_to_neighbor[e]]
                    rhs=(e[0]==f[0] or e[1]==f[1])
                    assert lhs==rhs,(n,v,e,f)
            left={a for a,b in B};right={b for a,b in B}
            cycle_rank=len(B)-len(left)-len(right)+(1 if B else 0)
            assert cycle_rank==rank_by_support(v)
            local_sum+=cycle_rank
            vertices_checked+=1
        chi,nfaces=count_cliques_euler(V,adj)
        assert local_sum==q[n]==chi-1,(n,local_sum,q[n],chi)
        print(n,len(V),nfaces,local_sum)
    print('PASS: 25 published ranks; 22 exact clique Euler comparisons; '
          f'{vertices_checked} local upper-link models; 60 q-series coefficients.')

if __name__=='__main__':main()
