#!/usr/bin/env python3
"""Exact, self-contained finite check of tree connected-partition truncations.

Only Python's standard library is used. Rooted trees are enumerated as multisets
of child rooted trees; unrooted trees are deduplicated by their centre encodings.
Every spanning forest is checked by independent union-find and DFS procedures.
"""
from collections import Counter, defaultdict

ROOTED = {1: ('()',)}

def rooted_codes(n):
    if n in ROOTED: return ROOTED[n]
    coins = [(s, c) for s in range(1, n) for c in rooted_codes(s)]
    sols=[]
    def recurse(start, left, codes):
        if left==0:
            sols.append('(' + ''.join(sorted(codes)) + ')')
            return
        for j in range(start,len(coins)):
            s, code=coins[j]
            if s > left: continue
            recurse(j,left-s,codes+[code])
    recurse(0,n-1,[])
    assert len(sols)==len(set(sols))
    ROOTED[n]=tuple(sorted(sols))
    return ROOTED[n]

def parse_tree(code):
    adj=[]; stack=[]
    for x in code:
        if x=='(':
            i=len(adj);adj.append([])
            if stack:
                j=stack[-1];adj[i].append(j);adj[j].append(i)
            stack.append(i)
        elif x==')':
            stack.pop()
        else: raise ValueError(x)
    assert not stack
    return adj

def centre_code(adj):
    n=len(adj)
    if n==1: return '()'
    deg=[len(x) for x in adj]
    leaves=[i for i in range(n) if deg[i]<=1]
    remaining=n
    while remaining>2:
        remaining-=len(leaves)
        fresh=[]
        for i in leaves:
            deg[i]=0
            for j in adj[i]:
                if deg[j]>0:
                    deg[j]-=1
                    if deg[j]==1: fresh.append(j)
        leaves=fresh
    centres=sorted(leaves)
    if len(centres)!=remaining: raise AssertionError(('centres',n,centres,remaining))
    def enc(u,p):
        return '('+''.join(sorted(enc(v,u) for v in adj[u] if v!=p))+')'
    if len(centres)==1:
        return enc(centres[0],-1)
    a,b=centres
    x,y=sorted((enc(a,b),enc(b,a)))
    return '<'+x+'|'+y+'>'

def edges_of(adj):
    return tuple((i,j) for i,nbrs in enumerate(adj) for j in nbrs if j>i)

def hist_union_find(adj):
    n=len(adj);edges=edges_of(adj);h=[Counter() for _ in range(n)]
    for mask in range(1<<(n-1)):
        par=list(range(n));sizes=[1]*n
        def get(x):
            while par[x]!=x:
                x=par[x]
            return x
        for k,(u,v) in enumerate(edges):
            if mask>>k&1:
                a,b=get(u),get(v)
                if a!=b:
                    par[b]=a;sizes[a]+=sizes[b]
        partition=tuple(sorted((sizes[j] for j in range(n) if par[j]==j),reverse=True))
        h[mask.bit_count()][partition]+=1
    return h

def hist_dfs(adj):
    n=len(adj);edges=edges_of(adj);h=[Counter() for _ in range(n)]
    for mask in range(1<<(n-1)):
        chosen=[[] for _ in range(n)]
        for k,(a,b) in enumerate(edges):
            if mask>>k&1:
                chosen[a].append(b);chosen[b].append(a)
        seen=set();sizes=[]
        for i in range(n):
            if i in seen:continue
            stack=[i];seen.add(i);size=0
            while stack:
                u=stack.pop();size+=1
                for v in chosen[u]:
                    if v not in seen:
                        seen.add(v);stack.append(v)
            sizes.append(size)
        h[mask.bit_count()][tuple(sorted(sizes,reverse=True))]+=1
    return h

def graph_diameter(adj):
    from collections import deque
    dmax=0
    for a in range(len(adj)):
        ds={a:0};todo=deque([a])
        while todo:
            u=todo.popleft()
            for v in adj[u]:
                if v not in ds:
                    ds[v]=ds[u]+1;todo.append(v)
        dmax=max(dmax,max(ds.values()))
    return dmax

def main():
    expected_rooted=[None,1,1,2,4,9,20,48,115,286,719]
    expected_unrooted=[None,1,1,1,2,3,6,11,23,47,106]
    print('METHOD rooted-multiset enumeration; unrooted centre canonicalization; two exact spanning-forest algorithms')
    for n in range(1,11):
        roots=rooted_codes(n)
        assert len(roots)==expected_rooted[n]
        by_centre={}
        for r in roots:
            tree=parse_tree(r)
            can=centre_code(tree)
            by_centre.setdefault(can,tree)
        assert len(by_centre)==expected_unrooted[n], (n,len(by_centre))
        if n<4:continue
        codes=sorted(by_centre)
        hists=[]
        for code in codes:
            tree=by_centre[code]
            a=hist_union_find(tree)
            b=hist_dfs(tree)
            assert a==b,(n,code,'two counters disagree')
            assert sum(map(sum,(c.values() for c in a)))==2**(n-1)
            hists.append(tuple(tuple(sorted(lev.items())) for lev in a))
        counts=[]; groups_at_bound={}
        for t in range(n-1):
            groups=defaultdict(list)
            for idx,h in enumerate(hists):groups[h[:t+1]].append(idx)
            coll=[v for v in groups.values() if len(v)>1]
            pairs=sum(len(c)*(len(c)-1)//2 for c in coll)
            counts.append(pairs)
            if t==n//2:groups_at_bound={tuple(x) for x in coll}
        tau=next(t for t,x in enumerate(counts) if x==0)
        print(f'n={n} rooted={len(roots)} unrooted={len(codes)} bound={n//2} tau={tau} collision_pairs_by_rank={counts}')
        assert tau>=n//2
        if n<10:assert tau==n//2
        if n==10:
            assert tau==6 and counts[5]==1 and counts[6]==0
            assert len(groups_at_bound)==1
            i,j=next(iter(groups_at_bound))
            for label,k in (('TREE_A',i),('TREE_B',j)):
                tree=by_centre[codes[k]]
                print(label+' edges='+str(edges_of(tree))+' diameter='+str(graph_diameter(tree))+' centre_code='+codes[k])
            before=dict(hists[i][6]);after=dict(hists[j][6])
            diffs=[(part,before.get(part,0),after.get(part,0)) for part in sorted(set(before)|set(after)) if before.get(part,0)!=after.get(part,0)]
            print('RANK6_DIFFERENCES',diffs)
            assert (4,2,2,2) in [x[0] for x in diffs]
    print('VERIFICATION_OK first_strict_order=10 tau10=6 unique_rank5_collision_pair=1')
if __name__=='__main__':main()
