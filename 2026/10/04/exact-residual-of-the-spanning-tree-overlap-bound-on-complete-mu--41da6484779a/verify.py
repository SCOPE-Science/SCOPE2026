from itertools import combinations
from math import comb as _comb

def comb(n,k):
    return _comb(n,k) if n>=0 and 0<=k<=n else 0

MAX_ORDER=11

def parts(n, minv=1):
    if n==0:
        yield ()
        return
    for a in range(minv,n+1):
        for rest in parts(n-a,a):
            yield (a,)+rest

def build(ps):
    part=[]
    for i,s in enumerate(ps): part += [i]*s
    n=len(part)
    adj=[set() for _ in range(n)]
    for u in range(n):
        for v in range(u+1,n):
            if part[u]!=part[v]:
                adj[u].add(v); adj[v].add(u)
    return part,adj

def dominates(S, adj):
    S=set(S)
    return all(v in S or (adj[v]&S) for v in range(len(adj)))

def max_tree_weight(weights,n):
    # Kruskal maximum spanning tree on complete graph.
    parent=list(range(n)); rank=[0]*n
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def union(a,b):
        a=find(a); b=find(b)
        if a==b:return False
        if rank[a]<rank[b]:a,b=b,a
        parent[b]=a
        if rank[a]==rank[b]:rank[a]+=1
        return True
    total=0; used=0
    for w,u,v in sorted(weights, reverse=True):
        if union(u,v):
            total+=w; used+=1
            if used==n-1: break
    assert used==n-1
    return total

types=0; parameter_cases=0; subsets=0
for N in range(2,MAX_ORDER+1):
  for ps in parts(N):
    if len(ps)<2: continue
    types+=1
    part,adj=build(ps)
    closed=[{v}|adj[v] for v in range(N)]
    for k in range(1,N+1):
      parameter_cases+=1
      den=comb(N,k)
      # Direct sigma numerator
      sigma_num=sum(comb(N-len(closed[v]),k) for v in range(N))
      sigma_formula=sum(s*comb(s-1,k) for s in ps)
      assert sigma_num==sigma_formula,(ps,k,'sigma',sigma_num,sigma_formula)
      # Direct tau numerator by maximum spanning tree
      weights=[]
      for u in range(N):
        for v in range(u+1,N):
          c=N-len(closed[u]|closed[v])
          weights.append((comb(c,k),u,v))
      tau_num=max_tree_weight(weights,N)
      tau_formula=sum((s-1)*comb(s-2,k) for s in ps)
      assert tau_num==tau_formula,(ps,k,'tau',tau_num,tau_formula)
      # Direct domination count
      dk=0
      for S in combinations(range(N),k):
        subsets+=1
        dk+=dominates(S,adj)
      nondom=den-dk
      nondom_formula=sum(comb(s,k) for s in ps if s>k)
      assert nondom==nondom_formula,(ps,k,'nondom',nondom,nondom_formula)
      # Exact residual numerator
      residual_num=(dk-den)+sigma_num-tau_num
      residual_formula=sum((s-k-1)*comb(s-1,k-1) for s in ps if s>=k+2)
      assert residual_num==residual_formula,(ps,k,'resid',residual_num,residual_formula)
      exact = residual_num==0
      criterion=max(ps)<=k+1
      assert exact==criterion,(ps,k,'criterion',exact,criterion,residual_num)
print(f'ALL CHECKS PASSED; multipartite_types={types}; parameter_cases={parameter_cases}; subsets={subsets}; max_order={MAX_ORDER}')
