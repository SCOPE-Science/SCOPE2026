"""Independent finite enumeration of mutually annihilating partial idempotents."""
from itertools import product
from collections import Counter
from math import comb, factorial


def maps(n):
    out=[]
    for entries in product(range(-1,n),repeat=n):
        if any(v!=-1 and entries[v]!=v for v in entries):
            continue
        domain=sum(1<<i for i,v in enumerate(entries) if v!=-1)
        image=0
        for v in entries:
            if v!=-1:image|=1<<v
        out.append((entries,domain,image,image.bit_count(),domain.bit_count()))
    return out


def formula(n,r,s):
    if r<0 or s<0 or r+s>n:return 0
    return factorial(n)//(factorial(r)*factorial(s)*factorial(n-r-s))*((r+1)*(s+1))**(n-r-s)


def conditional(n,r,d,s):
    if s>n-d:return 0
    return comb(n-d,s)*(s+1)**(n-r-s)


def count_idempotents(n,r,d):
    if r==0: return int(d==0)
    if d<r:return 0
    return comb(n,r)*comb(n-r,d-r)*r**(d-r)

for n in range(1,7):
    f=maps(n)
    profiles=Counter((r,d) for _,_,_,r,d in f)
    assert sum(profiles.values())==len(f)
    for r in range(n+1):
        for d in range(n+1):
            assert profiles[(r,d)]==count_idempotents(n,r,d), (n,r,d,profiles[(r,d)])
    counts=Counter()
    conditional_counts=Counter()
    if n<=5:
        # Completely independent verification of the zero-product equations.
        for e,de,ie,r,d in f:
            for g,dg,ig,s,ds in f:
                if all(g[y]==-1 for y in e if y!=-1) and all(e[y]==-1 for y in g if y!=-1):
                    counts[r,s]+=1
                    conditional_counts[r,d,s]+=1
    else:
        # Higher degree replay with bitsets of the actual image and domain.
        for e,de,ie,r,d in f:
            for g,dg,ig,s,ds in f:
                if (ie&dg)==0 and (ig&de)==0:
                    counts[r,s]+=1
                    conditional_counts[r,d,s]+=1
    for r in range(n+1):
        for s in range(n+1):
            assert counts[r,s]==formula(n,r,s), (n,r,s,counts[r,s],formula(n,r,s))
            for d in range(n+1):
                expected=count_idempotents(n,r,d)*conditional(n,r,d,s) if r>0 else (formula(n,0,s) if d==0 else 0)
                assert conditional_counts[r,d,s]==expected,(n,r,d,s,conditional_counts[r,d,s],expected)
    print(f'n={n} idempotents={len(f)} ordered_zero_pairs={sum(counts.values())} nonzero_graph_edges={sum(v for (r,s),v in counts.items() if r and s)//2}')

for n in range(1,20):
    # Independent aggregation of incidence by domain size, avoiding power expansions.
    for r in range(1,n+1):
        for s in range(n-r+1):
            lhs=sum(count_idempotents(n,r,d)*conditional(n,r,d,s) for d in range(r,n-s+1))
            assert lhs==formula(n,r,s),(n,r,s,lhs)
print('VERIFY_OK_ORTHOGONAL_PARTIAL_IDEMPOTENT_RANK_DEGREES')

# Independent graph metric and degree tests at small orders.
from collections import deque
for n in range(2,5):
    fs=maps(n)
    vertices=[i for i,(f,d,im,r,z) in enumerate(fs) if r>0]
    adj={i:set() for i in vertices}
    for a,i in enumerate(vertices):
        f,d,im,r,z=fs[i]
        for j in vertices[a+1:]:
            g,dg,img,s,zg=fs[j]
            if all(g[y]==-1 for y in f if y!=-1) and all(f[y]==-1 for y in g if y!=-1):
                adj[i].add(j);adj[j].add(i)
    nonis=[i for i in vertices if adj[i]]
    isolated=[i for i in vertices if not adj[i]]
    assert len(isolated)==sum(comb(n,r)*r**(n-r) for r in range(1,n+1))
    for i in vertices:
        f,d,im,r,z=fs[i]
        deg=sum(comb(n-z,s)*(s+1)**(n-r-s) for s in range(1,n-z+1))
        assert len(adj[i])==deg, (n,r,z,len(adj[i]),deg)
    maxdist=0
    for i in nonis:
        dist={i:0};q=deque([i])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if v not in dist:dist[v]=dist[u]+1;q.append(v)
        assert len(dist)==len(nonis)
        maxdist=max(maxdist,max(dist.values()))
    assert maxdist==(1 if n==2 else 3), (n,maxdist)
    print('GRAPH_OK',n,'connected_nonisolated',len(nonis),'isolates',len(isolated),'diameter',maxdist)
print('VERIFY_OK_ORTHOGONAL_IDEMPOTENT_GRAPH_METRIC')
