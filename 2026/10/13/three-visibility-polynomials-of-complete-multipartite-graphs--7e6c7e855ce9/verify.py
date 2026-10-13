from itertools import combinations
from collections import deque, Counter

def partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for x in range(lo, n+1):
        for rest in partitions(n-x, x):
            yield (x,) + rest

def graph_from_parts(parts):
    labels=[]
    for i,s in enumerate(parts):
        labels += [i]*s
    N=len(labels)
    adj=[set() for _ in range(N)]
    for u in range(N):
        for v in range(u+1,N):
            if labels[u]!=labels[v]:
                adj[u].add(v); adj[v].add(u)
    return labels, adj

def dist_avoiding(adj, a, b, blocked):
    if a==b: return 0
    blocked=set(blocked)-{a,b}
    q=deque([a])
    d={a:0}
    while q:
        u=q.popleft()
        for v in adj[u]:
            if v in blocked or v in d: continue
            d[v]=d[u]+1
            if v==b: return d[v]
            q.append(v)
    return None

def all_dist(adj):
    N=len(adj)
    D=[[None]*N for _ in range(N)]
    for s in range(N):
        q=deque([s]); D[s][s]=0
        while q:
            u=q.popleft()
            for v in adj[u]:
                if D[s][v] is None:
                    D[s][v]=D[s][u]+1
                    q.append(v)
    return D

def visible(adj,D,X,u,v):
    return dist_avoiding(adj,u,v,X)==D[u][v]

def actual_variant(adj,D,X,kind):
    N=len(adj); X=set(X); Y=set(range(N))-X
    if kind=="mutual":
        pairs=combinations(sorted(X),2)
    elif kind=="outer":
        pairs=list(combinations(sorted(X),2))+[(u,v) for u in X for v in Y]
    elif kind=="dual":
        pairs=list(combinations(sorted(X),2))+list(combinations(sorted(Y),2))
    else:
        raise ValueError
    return all(visible(adj,D,X,u,v) for u,v in pairs)

def predicted(labels,X,kind):
    N=len(labels); X=set(X); Y=set(range(N))-X
    part_ids=sorted(set(labels))
    parts={i:{v for v,l in enumerate(labels) if l==i} for i in part_ids}
    if all(len(parts[i])==1 for i in part_ids):
        return True
    if not Y:
        return False
    touched={labels[v] for v in Y}
    if len(touched)>=2:
        return True
    i=next(iter(touched))
    ni=len(parts[i]); yi=len(Y); xi=ni-yi
    if kind=="mutual":
        return xi<=1
    if kind=="outer":
        return yi==ni
    if kind=="dual":
        return yi==1 and ni<=2
    raise ValueError

def expected_counts(parts,kind):
    N=sum(parts)
    q=sum(s>=2 for s in parts)
    c=[0]*(N+1)
    for k in range(N+1):
        c[k]=__import__("math").comb(N,k)
    if q==0:
        return c
    c[N]-=1
    if kind=="mutual":
        for s in parts:
            if s>=3:
                for j in range(1,s-1):
                    c[N-j]-=__import__("math").comb(s,j)
    elif kind=="outer":
        for s in parts:
            if s>=2:
                for j in range(1,s):
                    c[N-j]-=__import__("math").comb(s,j)
    elif kind=="dual":
        for s in parts:
            if s==2:
                c[N-2]-=1
            elif s>=3:
                for j in range(1,s+1):
                    c[N-j]-=__import__("math").comb(s,j)
    return c

types=0
subset_trials=0
variant_trials=0
for N in range(2,10):
    for parts in partitions(N):
        if len(parts)<2: continue
        labels,adj=graph_from_parts(parts)
        D=all_dist(adj)
        types+=1
        actual={k:Counter() for k in ("mutual","outer","dual")}
        for mask in range(1<<N):
            X={v for v in range(N) if (mask>>v)&1}
            subset_trials+=1
            for kind in actual:
                variant_trials+=1
                a=actual_variant(adj,D,X,kind)
                p=predicted(labels,X,kind)
                assert a==p,(parts,kind,X,a,p)
                if a: actual[kind][len(X)]+=1
        for kind in actual:
            got=[actual[kind][k] for k in range(N+1)]
            exp=expected_counts(parts,kind)
            assert got==exp,(parts,kind,got,exp)

print("VERIFY_OK")
print("complete_multipartite_types_checked =",types)
print("orders = 2..9")
print("vertex_subsets_checked =",subset_trials)
print("variant_set_tests =",variant_trials)
print("all mutual/outer/dual classifications matched direct geodesic visibility")
print("all three cardinality enumerators matched the closed formulas")
