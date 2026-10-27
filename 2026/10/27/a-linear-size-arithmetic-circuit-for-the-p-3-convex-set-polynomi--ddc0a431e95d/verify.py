#!/usr/bin/env python3
"""Finite brute-force tests of the clique-block recurrence for P3 convex sets."""
from itertools import combinations
from random import Random
from collections import Counter


def add(p,q):
    r=[0]*max(len(p),len(q))
    for i,x in enumerate(p):r[i]+=x
    for i,x in enumerate(q):r[i]+=x
    return r

def mul(p,q):
    r=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j]+=a*b
    return r

def block_polynomial(blocks,n):
    # Blocks are edge-cliques of size >=2 of a block graph; incidence is a forest.
    incidence=[[] for _ in range(n)]
    for k,B in enumerate(blocks):
        for v in B:incidence[v].append(k)
    def vert(v,parent):
        omit0,omit1,sel=[1],[0],[0,1]
        for b in incidence[v]:
            if b==parent:continue
            c0,c1,cs=block(b,v)
            omit1=add(mul(omit1,c0),mul(omit0,c1))
            omit0=mul(omit0,c0)
            sel=mul(sel,cs)
        return omit0,omit1,sel
    def block(b,parent):
        omit0,omit1=[1],[0]
        zero_or_one=[1]
        selected_none=[1]
        selected_all=[1]
        for u in blocks[b]:
            if u==parent:continue
            a0,a1,ac=vert(u,b)
            omit1=add(mul(omit1,a0),mul(omit0,ac))
            omit0=mul(omit0,a0)
            zero_or_one=mul(zero_or_one,add(a0,a1))
            selected_none=mul(selected_none,a0)
            selected_all=mul(selected_all,ac)
        return zero_or_one,omit1,add(selected_none,selected_all)
    # Handle forests (for tests generated graphs all connected).
    seen=set()
    ans=[1]
    for v in range(n):
        if v in seen:continue
        queue=[v];seen.add(v)
        for x in queue:
            for b in incidence[x]:
                for y in blocks[b]:
                    if y not in seen:seen.add(y);queue.append(y)
        x,y,z=vert(v,None)
        ans=mul(ans,add(add(x,y),z))
    return ans

def brute(blocks,n):
    adj=[0]*n
    for block in blocks:
        for u,v in combinations(block,2):
            adj[u]|=1<<v;adj[v]|=1<<u
    counts=[0]*(n+1)
    for mask in range(1<<n):
        if all(mask&(1<<v) or (adj[v]&mask).bit_count()<2 for v in range(n)):
            counts[mask.bit_count()]+=1
    return counts

def construct(attachments):
    # Start at vertex zero; attach every clique along one existing vertex.
    n=1;blocks=[]
    for root,num_new in attachments:
        assert 0<=root<n and num_new>=1
        B=[root]+list(range(n,n+num_new))
        n+=num_new
        blocks.append(B)
    return blocks,n

def check(attachments):
    B,n=construct(attachments)
    got=block_polynomial(B,n)
    want=brute(B,n)
    assert got==want,(attachments,B,got,want)
    return n

def main():
    cases=0;size_hist=Counter()
    for n in range(1,10):
        # Non-isomorphic shape not needed: many attachment histories, all checked exactly.
        if n==1:
            cases+=1;size_hist[check([])]+=1
        for seed in range(84):
            rng=Random(n*1000+seed)
            attachment=[];current=1
            while current<n:
                root=rng.randrange(current)
                count=rng.randint(1,min(4,n-current))
                attachment.append((root,count));current+=count
            size_hist[check(attachment)]+=1;cases+=1
    for seed in range(180):
        rng=Random(200000+seed)
        n=rng.randint(10,16)
        attachment=[];current=1
        while current<n:
            root=rng.randrange(current)
            count=rng.randint(1,min(7,n-current))
            attachment.append((root,count));current+=count
        size_hist[check(attachment)]+=1;cases+=1
    # Infinite-class closed form, checked as a separate independent polynomial identity.
    bouquets=0
    for sizes in ((3,3),(3,4,6),(2,2,5),(2,3,3,3),(5,5,6,7)):
        attachments=[(0,m-1) for m in sizes]
        B,n=construct(attachments)
        rhs=[1,1+sum(m-1 for m in sizes)]
        prod=[1]
        for m in sizes:
            p=[1]+[0]*(m-2)+[1]
            prod=mul(prod,p)
        closed=add([1,sum(m-1 for m in sizes)],mul([0,1],prod))
        got=block_polynomial(B,n)
        assert got==closed,(sizes,got,closed)
        if n<=16:assert got==brute(B,n)
        bouquets+=1
    # All labelled simple graphs up to six vertices, with block decomposition
    # performed from scratch (no external Python dependencies).
    def blocks_of_graph(n, edges):
        nbr=[[] for _ in range(n)]
        for u,v in edges:
            nbr[u].append(v);nbr[v].append(u)
        disc=[-1]*n;low=[0]*n;stack=[];clock=[0];blocks=[]
        def dfs(u,parent):
            disc[u]=low[u]=clock[0];clock[0]+=1
            for v in nbr[u]:
                if disc[v]==-1:
                    stack.append((u,v));dfs(v,u);low[u]=min(low[u],low[v])
                    if low[v]>=disc[u]:
                        block=set()
                        while True:
                            e=stack.pop();block.update(e)
                            if e==(u,v):break
                        blocks.append(sorted(block))
                elif v!=parent and disc[v]<disc[u]:
                    stack.append((u,v));low[u]=min(low[u],disc[v])
        for u in range(n):
            if disc[u]==-1:dfs(u,-1)
        for B in blocks:
            Bset=set(B)
            if sum(u in Bset and v in Bset for u,v in edges)!=len(B)*(len(B)-1)//2:
                return None
        return blocks
    all_count=0;graph_counts={}
    for n in range(1,7):
        edges=list(combinations(range(n),2));good=0
        for mask in range(1<<len(edges)):
            E=[e for i,e in enumerate(edges) if (mask>>i)&1]
            B=blocks_of_graph(n,E)
            if B is None:continue
            lhs=block_polynomial(B,n);rhs=brute(B,n)
            assert lhs==rhs,(n,E,B,lhs,rhs)
            good+=1
        graph_counts[n]=good;all_count+=good
    print(f'VERIFY_OK {cases} constructed block graphs, {all_count} labelled block graphs through six vertices, {bouquets} clique bouquets')
    print('labelled size histogram:',graph_counts)
    print('sizes:',dict(sorted(size_hist.items())))
    print('test closed form B(3,4,6):', block_polynomial(construct([(0,2),(0,3),(0,5)])[0],11))

if __name__=='__main__': main()
