#!/usr/bin/env python3
"""Independent finite checks for closed unit-ball online dimension on trees.
Requires only Python standard library. Run: python3 verify.py
"""
from collections import defaultdict
from functools import lru_cache
from itertools import product,combinations
from heapq import heapify,heappop,heappush

def tree_from_prufer(n,word):
    if n==1:return [set()]
    degree=[1]*n
    for w in word:degree[w]+=1
    leaves=[i for i,d in enumerate(degree) if d==1]
    heapify(leaves)
    adj=[set() for _ in range(n)]
    for p in word:
        leaf=heappop(leaves)
        adj[leaf].add(p);adj[p].add(leaf)
        degree[leaf]-=1;degree[p]-=1
        if degree[p]==1:heappush(leaves,p)
    a,b=leaves
    adj[a].add(b);adj[b].add(a)
    return adj

def canonical(adj):
    n=len(adj)
    if n==1:return '()'
    degree=[len(x) for x in adj]
    live=n
    leaves=[i for i,d in enumerate(degree) if d<=1]
    while live>2:
        live-=len(leaves)
        new=[]
        for x in leaves:
            degree[x]=0
            for y in adj[x]:
                if degree[y]>0:
                    degree[y]-=1
                    if degree[y]==1:new.append(y)
        leaves=new
    def encode(x,p):
        return '('+''.join(sorted(encode(y,x) for y in adj[x] if y!=p))+')'
    if len(leaves)==1:return encode(leaves[0],-1)
    x,y=leaves
    return '('+''.join(sorted((encode(x,y),encode(y,x))))+')'

def exact_dimension(adj):
    n=len(adj)
    masks=[]
    for v in range(n):
        masks.append(sum(1<<w for w in range(n) if w==v or w in adj[v]))
    distinct=sorted(set(masks))
    # Masks index hypotheses; query outcome computed from its center.
    pos=[]
    for x in range(n):
        pos.append(sum(1<<i for i,m in enumerate(distinct) if m&(1<<x)))
    @lru_cache(None)
    def value(H):
        best=0
        for p in pos:
            a=H&p;b=H&~p
            if a and b:
                best=max(best,1+min(value(a),value(b)))
        return best
    return value((1<<len(distinct))-1)

def structural_dimension(adj):
    n=len(adj)
    if n<=2:return 0
    if n==3:return 1
    for x in range(n):
        if len(adj[x])<3:continue
        barred=set(range(n))-(set(adj[x])|{x})
        m=len(barred)
        if m<4:continue
        for y in range(n):
            q=len(barred&(set(adj[y])|{y}))
            if 2<=q<=m-2:return 3
    return 2

def vc_dimension(adj):
    n=len(adj)
    sets=[set(a)|{i} for i,a in enumerate(adj)]
    best=0
    for r in range(1,4):
        for sample in combinations(range(n),r):
            pattern={tuple(int(x in N) for x in sample) for N in sets}
            if len(pattern)==(1<<r):best=max(best,r)
    return best

def check_witness():
    edges=[(0,1),(0,2),(0,3),(1,4),(1,5),(2,6),(2,7)]
    adj=[set() for _ in range(8)]
    for a,b in edges:adj[a].add(b);adj[b].add(a)
    # Root query 0; second query 1; third queries depend on the first two bits.
    last={(1,1):2,(1,0):2,(0,1):4,(0,0):6}
    paths=[]
    for a,b,c in product((0,1),repeat=3):
        query=(0,1,last[(a,b)])
        witnesses=[v for v in range(8) if all(int(x==v or x in adj[v])==z for x,z in zip(query,(a,b,c)))]
        assert witnesses,(a,b,c)
        paths.append({'labels':''.join(map(str,(a,b,c))), 'queries':list(query), 'witness_centers':witnesses})
    assert structural_dimension(adj)==3==exact_dimension(adj)
    return paths

def main():
    summary={}
    examples={}
    for n in range(1,9):
        seen={}
        count=0
        if n==1:iterable=[()]
        elif n==2:iterable=[()]
        else:iterable=product(range(n),repeat=n-2)
        for word in iterable:
            count+=1
            adj=tree_from_prufer(n,word)
            key=canonical(adj)
            if key not in seen:seen[key]=adj
        histogram=defaultdict(int)
        for key,adj in seen.items():
            predicted=structural_dimension(adj)
            exact=exact_dimension(adj)
            assert predicted==exact,(n,key,predicted,exact)
            assert vc_dimension(adj)<=2,(n,key)
            histogram[exact]+=1
        summary[n]={'labelled_trees_checked':count,'unlabelled_trees_checked':len(seen),'dimension_histogram':dict(sorted(histogram.items()))}
        print('n=%d labelled=%d unlabelled=%d dimensions=%s'%(n,count,len(seen),dict(sorted(histogram.items()))))
    assert summary[8]['unlabelled_trees_checked']==23
    assert summary[8]['dimension_histogram']=={2:11,3:12}
    assert all(3 not in summary[n]['dimension_histogram'] for n in range(1,8))
    paths=check_witness()
    print('depth_three_example_paths=%d'%len(paths))
    for p in paths:print('path',p)
    print('ALL_CHECKS_PASS')
if __name__=='__main__':main()
