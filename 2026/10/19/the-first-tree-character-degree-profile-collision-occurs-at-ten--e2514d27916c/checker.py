"""Exact dependency-free census of unlabeled trees and matching-support character polynomials.
Run: python3 checker.py. All arithmetic uses integers; no external tables are loaded.
"""
from collections import Counter, defaultdict


def canonical(n, edges):
    adj = [set() for _ in range(n)]
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    degree = [len(row) for row in adj]
    remaining = set(range(n))
    while len(remaining)>2:
        leaves = [v for v in remaining if degree[v]<=1]
        for v in leaves: remaining.remove(v)
        for v in leaves:
            for u in adj[v]: degree[u]-=1
    def rooted(v, parent):
        return '(' + ''.join(sorted(rooted(u,v) for u in adj[v] if u!=parent)) + ')'
    centers=sorted(remaining)
    if len(centers)==1: return rooted(centers[0],-1)
    a,b=centers
    return '('+''.join(sorted([rooted(a,b),rooted(b,a)]))+')'


def unlabeled_trees(n):
    reps = {canonical(1,[]):()}
    for k in range(2,n+1):
        dest = {}
        for edges in reps.values():
            for v in range(k-1):
                nxt = edges+((v,k-1),)
                key=canonical(k,nxt)
                if key not in dest:dest[key]=nxt
        reps=dest
        yield k,reps


def matching_number(n, edges):
    # Exhaustive independent bitmask matching recursion, not a leaf-greedy approximation.
    E=tuple(edges); memo={}
    def rec(i,occupied):
        key=(i,occupied)
        if key in memo:return memo[key]
        if i==len(E):return 0
        a,b=E[i]
        z=rec(i+1,occupied)
        if not ((occupied>>a|occupied>>b)&1):
            z=max(z,1+rec(i+1,occupied|(1<<a)|(1<<b)))
        memo[key]=z
        return z
    return rec(0,0)


def polynomial(n,edges):
    out=Counter(); E=tuple(edges)
    for bits in range(1<<len(E)):
        sub=[e for i,e in enumerate(E) if bits>>i&1]
        out[(len(sub),matching_number(n,sub))]+=1
    return tuple(sorted(out.items()))


def rooted_poly(n,edges):
    # Independent rooted-tree maximum-matching-state recurrence.
    adj=[[] for _ in range(n)]
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    def mul(A,B):
        C=Counter()
        for i,a in A.items():
            for j,b in B.items(): C[(i[0]+j[0],i[1]+j[1])]+=a*b
        return C
    def add(A,B,scale=1):
        C=Counter(A)
        for k,v in B.items():C[k]+=scale*v
        return +C
    def step(v,parent):
        # States delta=0/1; exponent pair (# nonzero edges, maximum matching size).
        # An active edge to child of delta0 lets root gain one matching edge.
        zero=Counter({(0,0):1}); total=Counter({(0,0):1})
        for w in adj[v]:
            if w==parent:continue
            f0,f1=step(w,v)
            child_total=add(f0,f1)
            allowed=add(f0,add(f1,{(k[0]+1,k[1]):val for k,val in f1.items()}))
            choices=add(child_total,{(k[0]+1,k[1]):val for k,val in child_total.items()})
            zero=mul(zero,allowed)
            total=mul(total,choices)
        one=Counter()
        for (k,m),val in (total-zero).items():
            if val:one[(k,m+1)]+=val
        return zero,one
    a,b=step(0,-1)
    return tuple(sorted((a+b).items()))


def diameter(n,edges):
    adj=[[] for _ in range(n)]
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    best=0
    for v in range(n):
        dist={v:0}; queue=[v]
        for u in queue:
            for w in adj[u]:
                if w not in dist:dist[w]=dist[u]+1;queue.append(w)
        best=max(best,max(dist.values()))
    return best


def main():
    known={2:1,3:1,4:2,5:3,6:6,7:11,8:23,9:47,10:106}
    first=None
    for n,reps in unlabeled_trees(10):
        assert len(reps)==known[n], (n,len(reps))
        seen={}; duplicates=[]
        for key,E in reps.items():
            poly=polynomial(n,E)
            if poly in seen: duplicates.append((seen[poly],(key,E),poly))
            else:seen[poly]=(key,E)
        print('n',n,'unlabeled',len(reps),'profiles',len(seen),'collisions',len(duplicates))
        if duplicates:
            assert first is None
            first=(n,duplicates)
            break
    n,duplicates=first
    assert n==10 and len(duplicates)==1
    ((code1,E1),(code2,E2),coeffs)=duplicates[0]
    assert code1!=code2
    assert (diameter(n,E1),diameter(n,E2))==(6,7)
    assert polynomial(n,E1)==polynomial(n,E2)==rooted_poly(n,E1)==rooted_poly(n,E2)
    assert len(coeffs)==19
    assert sum(v for _,v in coeffs)==2**(n-1)
    print('WITNESS_A',repr(E1));print('WITNESS_B',repr(E2))
    print('COEFFICIENTS',repr(coeffs))
    print('ALL_EXACT_CHECKS_PASSED')

if __name__=='__main__': main()
