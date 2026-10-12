from itertools import combinations
from collections import Counter
from math import prod


def partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for x in range(lo, n+1):
        for rest in partitions(n-x, x):
            yield (x,) + rest


def build(parts):
    labels=[]
    for i,s in enumerate(parts): labels.extend([i]*s)
    N=len(labels)
    adj=[set() for _ in range(N)]
    for u in range(N):
        for v in range(u+1,N):
            if labels[u] != labels[v]:
                adj[u].add(v); adj[v].add(u)
    return labels,adj


def maximal_geodesics(labels,adj):
    N=len(labels)
    paths=[]
    edges=set()
    for u in range(N):
        for v in adj[u]:
            if u<v: edges.add((u,v))
    used_edges=set()
    # Every length-two shortest path is maximal because diameter <= 2.
    for u,v in combinations(range(N),2):
        if v in adj[u]:
            continue
        for w in sorted(adj[u] & adj[v]):
            paths.append((u,w,v))
            used_edges.add(tuple(sorted((u,w))))
            used_edges.add(tuple(sorted((w,v))))
    # An edge is a maximal geodesic exactly when it is not contained in a length-two geodesic.
    for e in sorted(edges-used_edges):
        paths.append(e)
    return paths


def direct_transversal(paths,S):
    S=set(S)
    return all(any(v in S for v in P) for P in paths)


def predicted(labels,S):
    S=set(S); N=len(labels); T=set(range(N))-S
    parts={}
    for v,i in enumerate(labels): parts.setdefault(i,set()).add(v)
    non=[i for i,vs in parts.items() if len(vs)>=2]
    singles=[next(iter(vs)) for i,vs in parts.items() if len(vs)==1]
    # large complement inside one non-singleton part
    if any(T <= parts[i] for i in non):
        return True
    # sparse complement: <=1 in each non-singleton part, <=1 singleton total
    if sum(v in T for v in singles)>1:
        return False
    return all(len(T & parts[i])<=1 for i in non)


def expected_complement_counts(parts):
    N=sum(parts)
    non=[n for n in parts if n>=2]
    s=sum(n==1 for n in parts)
    c=[0]*(N+1)
    # sparse family
    poly=[1,s] if s else [1]
    for n in non:
        f=[1,n]
        new=[0]*(len(poly)+1)
        for i,a in enumerate(poly):
            for j,b in enumerate(f): new[i+j]+=a*b
        poly=new
    for k,a in enumerate(poly): c[k]+=a
    # large one-part subsets (size >=2)
    from math import comb
    for n in non:
        for k in range(2,n+1): c[k]+=comb(n,k)
    return c


types=0; subset_trials=0; path_count=0; basis_trials=0
for N in range(2,11):
    for parts in partitions(N):
        if len(parts)<2: continue
        labels,adj=build(parts); paths=maximal_geodesics(labels,adj)
        types+=1; path_count+=len(paths)
        cnt=Counter(); actual_bases=[]
        for mask in range(1<<N):
            subset_trials+=1
            S={v for v in range(N) if (mask>>v)&1}
            a=direct_transversal(paths,S); p=predicted(labels,S)
            assert a==p,(parts,S,a,p,paths)
            if a: cnt[len(S)]+=1
        comp=expected_complement_counts(parts)
        expected=[comp[N-k] for k in range(N+1)]
        got=[cnt[k] for k in range(N+1)]
        assert got==expected,(parts,got,expected)
        gt=min(cnt)
        I=[n for n in parts if n>=2]
        q=len(I); s=sum(n==1 for n in parts); M=max(I,default=0); c=q+(1 if s else 0); L=max(M,c)
        assert gt==N-L,(parts,gt,N-L)
        a=sum(1 for n in I if n==M) if M else 0
        b=(s if s else 1)*prod(I)
        eb = a if M>c else b if c>M else a+b
        assert cnt[gt]==eb,(parts,cnt[gt],eb,M,c)
        basis_trials += cnt[gt]

print('VERIFY_OK')
print('complete_multipartite_types_checked =',types)
print('orders = 2..10')
print('vertex_subsets_checked =',subset_trials)
print('maximal_geodesic_instances_across_types =',path_count)
print('minimum_bases_checked =',basis_trials)
print('all direct maximal-geodesic hitting tests matched the complement classification')
print('all cardinality enumerators matched the closed complement polynomial')
print('all geodesic-transversal numbers and basis counts matched the formulas')
