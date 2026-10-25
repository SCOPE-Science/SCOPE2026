"""Finite independent checks for strong-geodetic subsets of complete prisms."""
from collections import Counter, deque
from itertools import combinations
from math import comb

def graph(n):
    adj=[set() for _ in range(2*n)]
    for layer in (0,1):
        for i,j in combinations(range(n),2):
            u,v=layer*n+i,layer*n+j
            adj[u].add(v);adj[v].add(u)
    for i in range(n):
        adj[i].add(n+i);adj[n+i].add(i)
    return adj

def pred_direct(n,mask,adj,dist):
    S=[v for v in range(2*n) if (mask>>v)&1]
    U=[v for v in range(2*n) if not (mask>>v)&1]
    if not U:return True
    resources={}
    for i in range(len(S)):
        for j in range(i+1,len(S)):
            u,v=S[i],S[j];d=dist[u][v]
            if d<=1:continue
            mids=[w for w in U if dist[u][w]+dist[w][v]==d]
            if mids:resources[(u,v)]=mids
    # A pair may supply at most one path; a path has at most one interior vertex.
    # We match every unselected vertex to a different endpoint pair.
    opts={w:[] for w in U}
    for pair,mids in resources.items():
        for w in mids:opts[w].append(pair)
    if any(not opts[w] for w in U):return False
    assigned={}
    def augment(w,seen):
        for pair in opts[w]:
            if pair in seen:continue
            seen.add(pair)
            if pair not in assigned or augment(assigned[pair],seen):
                assigned[pair]=w
                return True
        return False
    for w in sorted(U,key=lambda x:len(opts[x])):
        if not augment(w,set()):return False
    return True

def pred_formula(n,mask):
    a=sum(bool(mask>>i&1) for i in range(n))
    b=sum(bool(mask>>(n+i)&1) for i in range(n))
    full=sum(bool(mask>>i&1) and bool(mask>>(n+i)&1) for i in range(n))
    occupied=sum(bool(mask>>i&1) or bool(mask>>(n+i)&1) for i in range(n))
    return occupied==n and (full>=1 or (a>=2 and b>=2))

def predicted_poly(n):
    out=Counter()
    for d in range(1,n+1):
        for s in range(n-d+1):
            out[n+d]+=comb(n,d)*comb(n-d,s) # every state with d double columns, others single
    if n>=4:out[n]+=2**n-2*n-2
    return +out

def predicted_facets(n):
    if n<=3:return {n+1:n*2**(n-1)}
    return {n:2**n-2*n-2,n+1:2*n}

def check_n(n):
    adj=graph(n)
    dist=[]
    for root in range(2*n):
        dr=[10000]*(2*n);dr[root]=0;q=deque([root])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if dr[v]>dr[u]+1:dr[v]=dr[u]+1;q.append(v)
        dist.append(dr)
    valid={mask for mask in range(1<<(2*n)) if pred_direct(n,mask,adj,dist)}
    for mask in range(1<<(2*n)):
        assert ((mask in valid)==pred_formula(n,mask)), ('classification',n,mask)
    poly=Counter(mask.bit_count() for mask in valid)
    assert poly==predicted_poly(n),(n,poly,predicted_poly(n))
    minimal={mask for mask in valid if not any(mask ^(1<<i) in valid for i in range(2*n) if (mask>>i)&1)}
    facets=Counter(mask.bit_count() for mask in minimal)
    assert facets==predicted_facets(n),(n,facets,predicted_facets(n))
    assert len(valid)==3**n - (2*n+2 if n>=4 else 2**n)
    print('DIRECT_OK',n,'subsets',1<<(2*n),'valid',len(valid),'facets',dict(sorted(facets.items())))
    if n>=4:
        base=[mask for mask in valid if mask.bit_count()==n]
        E={x:set() for x in base}
        for i,u in enumerate(base):
            for v in base[i+1:]:
                if (u^v).bit_count()==2:
                    E[u].add(v);E[v].add(u)
        if n==4:
            assert all(not E[x] for x in base)
            print('RECONFIG_ISOLATED_OK n=4',len(base))
        else:
            for src in base:
                d={src:0};q=deque([src])
                while q:
                    x=q.popleft()
                    for y in E[x]:
                        if y not in d:d[y]=d[x]+1;q.append(y)
                assert len(d)==len(base)
                assert all(d[y]==(src^y).bit_count()//2 for y in base)
            dia=max((x^y).bit_count()//2 for x in base for y in base)
            assert dia==n
            print('RECONFIG_ISOMETRIC_OK',n,'vertices',len(base),'diameter',dia)

if __name__=='__main__':
    for n in range(2,8):check_n(n)
    print('ALL_CHECKS_PASS')
