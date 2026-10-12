from itertools import combinations
from collections import Counter, deque
from functools import reduce
from operator import mul

def partitions(n, min_part=2):
    # unordered positive partitions with all parts >= min_part
    if n == 0:
        yield ()
        return
    for x in range(min_part, n+1):
        for rest in partitions(n-x, x):
            yield (x,) + rest

def graph(parts):
    # vertex 0 is the common center; each part is a clique
    groups=[]
    nxt=1
    for k in parts:
        g=list(range(nxt,nxt+k))
        groups.append(g)
        nxt += k
    N=nxt
    adj=[set() for _ in range(N)]
    for v in range(1,N):
        adj[0].add(v); adj[v].add(0)
    for g in groups:
        for a,b in combinations(g,2):
            adj[a].add(b); adj[b].add(a)
    return groups, adj

def all_dist(adj):
    D=[]
    for s in range(len(adj)):
        d=[10**9]*len(adj); d[s]=0
        q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v]==10**9:
                    d[v]=d[u]+1
                    q.append(v)
        D.append(d)
    return D

def rep(D,v,S):
    return tuple(sorted(D[v][s] for s in S))

def actual(D,S):
    S=set(S)
    outs=[v for v in range(len(D)) if v not in S]
    reps=[rep(D,v,S) for v in outs]
    return len(reps)==len(set(reps))

def predicted(groups,S):
    S=set(S)
    omitted_sizes=[]
    for g in groups:
        missing=[v for v in g if v not in S]
        if len(missing)>1:
            return False
        if len(missing)==1:
            omitted_sizes.append(len(g))
    return len(omitted_sizes)==len(set(omitted_sizes))

def poly_expected(parts):
    # (1+z) * product over distinct q of (z^(q*m_q)+m_q*q*z^(q*m_q-1))
    mult=Counter(parts)
    coeff=[1,1]
    for q,m in sorted(mult.items()):
        deg=q*m
        factor=[0]*(deg+1)
        factor[deg]=1
        factor[deg-1]=m*q
        new=[0]*(len(coeff)+len(factor)-1)
        for i,a in enumerate(coeff):
            for j,b in enumerate(factor):
                new[i+j]+=a*b
        coeff=new
    return coeff

types=subsets=bases=0
for peripheral in range(4,11):
    for parts in partitions(peripheral):
        if len(parts)<2:
            continue
        groups,adj=graph(parts)
        D=all_dist(adj)
        N=len(adj)
        cnt=Counter()
        for mask in range(1<<N):
            S=[v for v in range(N) if (mask>>v)&1]
            a=actual(D,S)
            p=predicted(groups,S)
            assert a==p,(parts,S,a,p)
            subsets += 1
            if a: cnt[len(S)] += 1
        expected=poly_expected(parts)
        got=[cnt[k] for k in range(N+1)]
        assert got==expected,(parts,got,expected)
        dim=min(cnt)
        distinct=len(set(parts))
        want=sum(parts)-distinct
        assert dim==want,(parts,dim,want)
        want_bases=1
        for q,m in Counter(parts).items():
            want_bases *= m*q
        assert cnt[dim]==want_bases,(parts,cnt[dim],want_bases)
        bases += cnt[dim]
        types += 1

print("VERIFY_OK")
print("heterogeneous_windmill_types_checked =",types)
print("peripheral_orders = 4..10")
print("vertex_subsets_checked =",subsets)
print("minimum_bases_checked =",bases)
print("all direct outer-multiset tests matched the distinct-omitted-clique-size classification")
print("all cardinality enumerators matched the product formula")
print("all dimensions and minimum-basis counts matched")
