#!/usr/bin/env python3
"""Exact finite checks for local toric divisor groups of complete-graph spanning-tree polytopes.

Uses only Python's standard library. Each calculation is over integers or F_1000003.
The all-n proof is mathematical, not finite verification.
"""
from itertools import combinations, product


def edges(n):
    return list(combinations(range(n), 2))


def is_tree(n, subset):
    adj = [[] for _ in range(n)]
    for u,v in subset:
        adj[u].append(v); adj[v].append(u)
    seen={0}; pending=[0]
    while pending:
        for w in adj[pending.pop()]:
            if w not in seen:
                seen.add(w); pending.append(w)
    return len(seen)==n


def connected(n, tree, vertices):
    allowed=set(vertices)
    a=next(iter(allowed)); seen={a}; pending=[a]
    adj={i:[] for i in allowed}
    for u,v in tree:
        if u in allowed and v in allowed:
            adj[u].append(v);adj[v].append(u)
    while pending:
        for w in adj[pending.pop()]:
            if w not in seen:
                seen.add(w);pending.append(w)
    return len(seen)==len(allowed)


def rank_mod(rows,p=1000003):
    if not rows:return 0
    a=[[(v%p) for v in row] for row in rows]
    m=len(a);q=len(a[0]);r=0
    for j in range(q):
        s=next((i for i in range(r,m) if a[i][j]),None)
        if s is None:continue
        a[r],a[s]=a[s],a[r]
        inv=pow(a[r][j],-1,p)
        a[r]=[(v*inv)%p for v in a[r]]
        for i in range(r+1,m):
            if a[i][j]:
                f=a[i][j]
                a[i]=[(v-f*w)%p for v,w in zip(a[i],a[r])]
        r+=1
        if r==m:break
    return r


def main():
    for n in (4,5,6):
        E=edges(n);m=len(E)
        trees=[frozenset(t) for t in combinations(E,n-1) if is_tree(n,t)]
        assert len(trees)==n**(n-2)
        subsets=[frozenset(S) for k in range(2,n) for S in combinations(range(n),k)]
        rlist=[]
        for T in trees:
            c=sum(connected(n,T,S) for S in subsets)
            # All exactly-tight matroid-facet inequalities at vertex T.
            tight_non_tree=sum(e not in T for e in E)
            tight_flats=sum(sum(u in S and v in S for u,v in T)==len(S)-1 for S in subsets)
            assert c==tight_flats
            rk=tight_non_tree+tight_flats-(m-1)
            assert rk==c-n+2
            assert rk>0
            rlist.append(rk)
        star=2**(n-1)-n
        path=(n-1)*(n-2)//2
        assert min(rlist)==path and max(rlist)==star
        if n<=5:
            vectors=[[int(e in T) for e in E] for T in trees]
            dim=rank_mod([[a-b for a,b in zip(v,vectors[0])] for v in vectors[1:]])
            assert dim==m-1
            count=0
            # Exact facet dimension checks modulo a prime: rank=m-2.
            for j,e in enumerate(E):
                face=[v for v in vectors if v[j]==0]
                assert rank_mod([[a-b for a,b in zip(v,face[0])] for v in face[1:]])==m-2
                count+=1
            for S in subsets:
                idx=[i for i,(u,v) in enumerate(E) if u in S and v in S]
                face=[v for v in vectors if sum(v[i] for i in idx)==len(S)-1]
                assert rank_mod([[a-b for a,b in zip(v,face[0])] for v in face[1:]])==m-2
                count+=1
            assert count==m+len(subsets)
            print(f'n={n}: {len(trees)} spanning trees; {count} candidate facets are codimension one; local ranks {path}..{star}')
        else:
            print(f'n={n}: {len(trees)} spanning trees; all local formula counts verified; local ranks {path}..{star}')
    print('PASS: exact finite checks (general result requires proof).')


if __name__=='__main__':main()
