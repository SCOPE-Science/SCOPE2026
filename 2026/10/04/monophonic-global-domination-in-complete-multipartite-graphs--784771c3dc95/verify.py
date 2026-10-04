from itertools import combinations
from math import comb

def partitions(n, lo=1):
    if n==0:
        yield ()
        return
    for a in range(lo,n+1):
        for rest in partitions(n-a,a):
            yield (a,)+rest

def graph(parts):
    labels=[]
    for i,s in enumerate(parts): labels += [i]*s
    n=len(labels)
    adj=[[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if labels[i]!=labels[j]: adj[i][j]=adj[j][i]=True
    return labels,adj

def intervals(adj):
    n=len(adj); J=[[set() for _ in range(n)] for __ in range(n)]
    for s in range(n):
      for t in range(s+1,n):
        seen=set([s,t])
        # enumerate induced s-t paths incrementally
        def dfs(path):
            u=path[-1]
            if u==t:
                seen.update(path); return
            for w in range(n):
                if w in path: continue
                if not adj[u][w]: continue
                # New endpoint w may only be adjacent to predecessor among earlier path vertices.
                if any(adj[w][path[k]] for k in range(len(path)-1)):
                    continue
                dfs(path+[w])
        dfs([s])
        J[s][t]=J[t][s]=seen
    for i in range(n): J[i][i]={i}
    return J

def is_monophonic(mask,J,n):
    verts=[i for i in range(n) if mask>>i&1]
    if not verts: return False
    hull=set(verts)
    for a,b in combinations(verts,2): hull |= J[a][b]
    return len(hull)==n

def dominates(mask,adj,n):
    for v in range(n):
        if mask>>v&1: continue
        if not any((mask>>u)&1 and adj[v][u] for u in range(n)): return False
    return True

def is_global(mask,adj,n):
    if not dominates(mask,adj,n): return False
    comp=[[False]*n for _ in range(n)]
    for i in range(n):
      for j in range(n):
        if i!=j: comp[i][j]=not adj[i][j]
    return dominates(mask,comp,n)

def predicted(mask,labels,parts):
    r=len(parts)
    m=[0]*r
    for v,p in enumerate(labels):
        if mask>>v&1:m[p]+=1
    if any(x==0 for x in m): return False
    B=[i for i,x in enumerate(m) if x>=2]
    if len(B)>=2:return True
    if len(B)==1:
        i=B[0]; return m[i]==parts[i]
    return all(parts[i]==1 for i in range(r))

def gamma_formula(parts):
    r=len(parts); q=sum(s>=2 for s in parts); N=sum(parts)
    if q<=1:return N
    return r+1 if any(s==2 for s in parts) else r+2

def min_count_formula(parts):
    r=len(parts); q=sum(s>=2 for s in parts)
    if q<=1:return 1
    if any(s==2 for s in parts):
        return sum(prod(parts[j] for j in range(r) if j!=i) for i,s in enumerate(parts) if s==2)
    ans=0
    # two parts contribute exactly two each
    idx=[i for i,s in enumerate(parts) if s>=2]
    for ii in range(len(idx)):
      for jj in range(ii+1,len(idx)):
        i,j=idx[ii],idx[jj]
        ans += comb(parts[i],2)*comb(parts[j],2)*prod(parts[h] for h in range(r) if h not in (i,j))
    # one full 3-part, all others one
    ans += sum(prod(parts[j] for j in range(r) if j!=i) for i,s in enumerate(parts) if s==3)
    return ans

def prod(xs):
    z=1
    for x in xs:z*=x
    return z

types=subsets=0
for n in range(2,10):
  for parts in partitions(n):
    if len(parts)<2: continue
    labels,adj=graph(parts); J=intervals(adj)
    good=[]
    for mask in range(1<<n):
      subsets+=1
      actual=is_monophonic(mask,J,n) and is_global(mask,adj,n)
      pred=predicted(mask,labels,parts)
      assert actual==pred,(parts,mask,actual,pred)
      if actual: good.append(mask)
    mn=min(m.bit_count() for m in good)
    cnt=sum(m.bit_count()==mn for m in good)
    assert mn==gamma_formula(parts),(parts,mn,gamma_formula(parts))
    assert cnt==min_count_formula(parts),(parts,cnt,min_count_formula(parts))
    types+=1
print('VERIFY_OK')
print('multipartite_types_checked =',types)
print('vertex_subsets_checked =',subsets)
print('orders = 2..9')
