"""Independent exhaustive check of maximal-independent-set shattering on graph coronas.

Usage: python3 check_whiskered_shattering.py
Requires only Python 3's standard library. All indices use zero-based conventions.
"""
from itertools import combinations
from math import comb

def base_edges(n, mask):
    return [e for i,e in enumerate(combinations(range(n),2)) if mask>>i&1]

def graph_edges(n, t, edges):
    # Original vertices 0..n-1; private leaves n+t*v+j.
    out = edges[:]
    out.extend((v,n+t*v+j) for v in range(n) for j in range(t))
    return out

def maximal_independent_sets(N, E):
    adj=[0]*N
    for u,v in E:
        adj[u]|=1<<v;adj[v]|=1<<u
    allmask=(1<<N)-1
    ans=[]
    for mask in range(1<<N):
        if any(mask&(1<<u) and mask&(1<<v) for u,v in E):
            continue
        # Maximal: every omitted vertex adjacent to included vertex.
        if all(mask&(1<<v) or mask&adj[v] for v in range(N)):
            ans.append(mask)
    return ans

def independent_subsets(n,E):
    return {a for a in range(1<<n) if not any(a&(1<<u) and a&(1<<v) for u,v in E)}

def supports_from_MIS(N,mis):
    ans=[]
    for support in range(1<<N):
        target=1<<support.bit_count()
        traces={sum(((m>>v)&1)<<j for j,v in enumerate(range(N)) if support>>v&1)
                for m in mis}
        if len(traces)==target:ans.append(support)
    return set(ans)

def predicted_supports(n,t,indep):
    # An index contributes its core vertex or exactly one of t private leaves.
    out=set()
    for indices in indep:
        partial=[0]
        for v in range(n):
            if indices>>v&1:
                partial=[z|(1<<q) for z in partial for q in [v]+[n+t*v+j for j in range(t)]]
        out.update(partial)
    return out

def check(n,t,base_mask):
    E=base_edges(n,base_mask); ind=independent_subsets(n,E)
    mis=maximal_independent_sets(n*(t+1),graph_edges(n,t,E))
    assert len(mis)==len(ind), (n,t,base_mask,'mis count')
    predicted=predicted_supports(n,t,ind)
    direct=supports_from_MIS(n*(t+1),mis)
    assert direct==predicted, (n,t,base_mask, sorted(direct^predicted))
    coefs=[sum(s.bit_count()==k for s in direct) for k in range(n+1)]
    rhs=[sum(a.bit_count()==k for a in ind)*(t+1)**k for k in range(n+1)]
    assert coefs==rhs, (n,t,base_mask,coefs,rhs)
    return len(direct)

def main():
    cases=supports=0
    for n,t in [(0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(0,2),(1,2),(2,2),(3,2),(4,2),(0,3),(1,3),(2,3),(3,3)]:
        for mask in range(1<<comb(n,2)):
            supports+=check(n,t,mask);cases+=1
    print('WHISKERED_MIS_SHATTERING_PASS',cases,supports)
if __name__=='__main__':main()
