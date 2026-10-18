#!/usr/bin/env python3
"""Independent BFS-based validation of a subdivision-clique monitoring enumerator."""
from collections import deque,Counter
from itertools import combinations
from math import comb,factorial

def graph(n):
    edgelist=list(combinations(range(n),2))
    N=n+len(edgelist)
    adj=[set() for _ in range(N)]
    E=[]
    for j,(a,b) in enumerate(edgelist):
        v=n+j
        for u in (a,b):
            adj[u].add(v);adj[v].add(u);E.append((u,v))
    return N,adj,E,edgelist

def bfs(adj,root,drop=-1,E=None):
    dist=[1000000]*len(adj);dist[root]=0;q=deque([root]);
    while q:
        a=q.popleft()
        for b in adj[a]:
            if drop>=0 and ((a,b)==E[drop] or (b,a)==E[drop]):continue
            if dist[b]>dist[a]+1:
                dist[b]=dist[a]+1;q.append(b)
    return dist

def all_monitors(n):
    N,adj,E,pairs=graph(n)
    D=[bfs(adj,i) for i in range(N)]
    M=[0]*N
    for e in range(len(E)):
        for x in range(N):
            de=bfs(adj,x,e,E)
            if any(u!=v for u,v in zip(D[x],de)):
                M[x]|=1<<e
    return M,(1<<len(E))-1,pairs

def condition(n,mask,pairs):
    U={i for i in range(n) if mask>>i&1}
    F={pair for e,pair in enumerate(pairs) if mask>>(n+e)&1}
    bad={i for i in range(n) if i not in U and all(i not in pair for pair in F)}
    return not bad or (len(bad)==1 and len(U)==n-1)

def formula(n):
    e=comb(n,2)
    # polynomial (1+z)^e * (n*z^(n-1)+z^n), plus u<=n-2 with IE
    p=Counter()
    for u in (n-1,n):
        for f in range(e+1):p[u+f]+=comb(n,u)*comb(e,f)
    for u in range(n-1):
        w=n-u
        for j in range(w+1):
            r=comb(n-j,2)
            mul=comb(n,u)*(-1)**j*comb(w,j)
            for f in range(r+1):p[u+f]+=mul*comb(r,f)
    return p

def predicted_minimal(n):
    # Independent labeled-set partition recurrence: construct a chosen set of original
    # probes (isolated blocks), then partition the remaining labels into star blocks.
    from functools import lru_cache
    from collections import Counter
    def rec(vertices):
        if not vertices:return Counter({0:1})
        v=vertices[0];out=Counter()
        # Chosen original vertex: a singleton probe.
        for cost,num in rec(vertices[1:]).items():out[cost+1]+=num
        # Star component on block containing smallest remaining label.
        for k in range(2,len(vertices)+1):
            for rest in combinations(vertices[1:],k-1):
                chosen=set(rest)|(set([v]));remaining=tuple(x for x in vertices if x not in chosen)
                centers=1 if k==2 else k
                for cost,num in rec(remaining).items():out[cost+k-1]+=centers*num
        return out
    # cache rec properly via wrapper for n up to 6 (avoid repeated subcalls)
    rec=lru_cache(None)(rec)
    p=rec(tuple(range(n)));p[n]-=1;p[n-1]+=n
    return p

def target_formula(n):
    r=n//2
    if n==3:return 9
    if n%2==0:return factorial(n)//(2**r*factorial(r))
    return (n*comb(n-1,2)*factorial(n-3)//(2**(r-1)*factorial(r-1))
            +n*factorial(n-1)//(2**r*factorial(r)))

def main():
    total=0
    for n in range(3,7):
        M,full,pairs=all_monitors(n)
        N=len(M);maxmask=1<<N
        # recurrence stores union bit mask for any candidate using low-bit removal
        cov=[0]*maxmask
        actual=Counter();minimal=Counter();verified=0
        for mask in range(1,maxmask):
            b=mask&-mask;i=b.bit_length()-1
            cov[mask]=cov[mask^b]|M[i]
            ok=(cov[mask]==full)
            pred=condition(n,mask,pairs)
            assert ok==pred,(n,mask,ok,pred)
            if ok:
                actual[mask.bit_count()]+=1;verified+=1
                if all(cov[mask^(1<<i)]!=full for i in range(N) if mask>>i&1):
                    minimal[mask.bit_count()]+=1
        expected=formula(n)
        assert all(actual[k]==expected[k] for k in range(N+1)),(n,actual,expected)
        pred_min=predicted_minimal(n)
        assert all(minimal[k]==pred_min[k] for k in range(N+1)),(n,minimal,pred_min)
        assert min(minimal)==(n+1)//2 and max(minimal)==n-1,(n,minimal)
        assert sorted(minimal)==list(range((n+1)//2,n)),(n,minimal)
        first=min(actual)
        assert first==(n+1)//2 and actual[first]==target_formula(n),(n,first,actual[first],target_formula(n))
        total+=maxmask
        print('n',n,'subsets',maxmask,'DEM_sets',verified,'min',first,'min_count',actual[first],'coefficients',[actual[k] for k in range(N+1)],'minimal_coefficients',dict(sorted(minimal.items())))
    print('VERIFICATION_OK exhaustive_subsets',total,'range=3..6')

if __name__=='__main__':main()
