from itertools import combinations, product

def gf2_rank(rows, ncols):
    rows=list(rows); r=0
    for c in range(ncols):
        p=next((i for i in range(r,len(rows)) if (rows[i]>>c)&1),None)
        if p is None: continue
        rows[r],rows[p]=rows[p],rows[r]
        for i in range(len(rows)):
            if i!=r and ((rows[i]>>c)&1): rows[i]^=rows[r]
        r+=1
    return r

def comps(n,E):
    p=list(range(n))
    def f(x):
        while p[x]!=x:
            p[x]=p[p[x]]; x=p[x]
        return x
    for i,j in E:
        a,b=f(i),f(j)
        if a!=b:p[b]=a
    return len({f(i) for i in range(n)})

checks=0
for n in range(2,8):
    edges=list(combinations(range(n),2))
    # incidence rank formula on all subsets for n<=5, deterministic sample thereafter
    masks=range(1<<len(edges)) if n<=5 else [0,1,(1<<len(edges))-1] + [((1<<len(edges))-1)//(k+1) for k in range(1,20)]
    for mask in masks:
        E=[e for q,e in enumerate(edges) if (mask>>q)&1]
        rows=[(1<<i)|(1<<j) for i,j in E]
        rank=gf2_rank(rows,n)
        assert rank==n-comps(n,E)
        assert (rank==len(E)) == (len(E)==n-comps(n,E))
        checks+=2
    # affine two-graph law using a deterministic graphing g and all t
    g={(i,j):((i*17+j*31+n)%2) for i,j in edges}
    ys=[]
    for t in product([0,1], repeat=n):
        y=tuple(g[i,j]^t[i]^t[j] for i,j in edges)
        # every quadruple parity condition relative to parameter triple parity
        for i,j,k in combinations(range(n),3):
            rij=g[min(i,j),max(i,j)]^g[min(i,k),max(i,k)]^g[min(j,k),max(j,k)]
            yij=y[edges.index((min(i,j),max(i,j)))]
            yik=y[edges.index((min(i,k),max(i,k)))]
            yjk=y[edges.index((min(j,k),max(j,k)))]
            assert yij^yik^yjk^rij==0
            checks+=1
        ys.append(y)
    assert len(set(ys))==2**(n-1); checks+=1
    # each y has exactly two t preimages (global complement)
    from collections import Counter
    C=Counter(ys)
    assert set(C.values())=={2}; checks+=1
print(f'VERIFY_OK {checks} exact assertions')
