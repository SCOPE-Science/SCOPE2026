#!/usr/bin/env python3
"""Exact exhaustive census of the minimal unicyclic independence-complex obstruction.
Only standard-library integer arithmetic and exhaustive labeled graphs are used.
"""
from itertools import combinations, permutations
from functools import lru_cache


def bit_graph(n, es):
    nbr = [0] * n
    for a,b in es:
        nbr[a] |= 1<<b
        nbr[b] |= 1<<a
    return tuple(nbr)

def connected(n, es):
    nbr=bit_graph(n,es)
    seen=1
    while True:
        new=seen
        for v in range(n):
            if seen>>v&1: new |= nbr[v]
        if new==seen: return new == (1<<n)-1
        seen=new

def unit_rank(mat):
    # Smith invariants are all units iff every nonzero residual pivot is ±1.
    if not mat: return 0
    a=[row[:] for row in mat]
    r=len(a); c=len(a[0]); rank=0
    while r and c:
        ij=next(((i,j) for i in range(r) for j in range(c) if abs(a[i][j])==1),None)
        if ij is None:
            assert all(not x for row in a for x in row), ('nonunit Smith block',a)
            break
        i,j=ij
        a[0],a[i]=a[i],a[0]
        for row in a:
            row[0],row[j]=row[j],row[0]
        sign=a[0][0]
        for k in range(1,r):
            t=a[k][0]*sign
            for h in range(c): a[k][h]-=t*a[0][h]
        for h in range(1,c):
            t=a[0][h]*sign
            for k in range(r): a[k][h]-=t*a[k][0]
        a=[row[1:] for row in a[1:]]
        r-=1;c-=1;rank+=1
    return rank

@lru_cache(maxsize=None)
def reduced_betti(n,edgemask):
    edges=list(combinations(range(n),2))
    nbr=bit_graph(n,[edges[j] for j in range(len(edges)) if edgemask>>j&1])
    faces=[(0,)] # replaced by actual dim -1 face tuple
    by_dim={-1:[0]}
    for size in range(1,n+1):
        fs=[]
        for verts in combinations(range(n),size):
            s=sum(1<<i for i in verts)
            if all(not (nbr[i]&s) for i in verts): fs.append(s)
        if fs: by_dim[size-1]=fs
    maxd=max(by_dim)
    ranks={-1:0}
    for d in range(maxd+1):
        up=by_dim[d]; low=by_dim[d-1]
        at={m:i for i,m in enumerate(low)}
        matrix=[[0]*len(up) for _ in low]
        for col,face in enumerate(up):
            verts=[i for i in range(n) if face>>i&1]
            for pos,v in enumerate(verts):
                sub=face^(1<<v)
                matrix[at[sub]][col]=(-1)**pos
        ranks[d]=unit_rank(matrix)
    return tuple((d,len(by_dim[d])-ranks[d]-ranks.get(d+1,0)) for d in range(-1,maxd+1) if len(by_dim[d])-ranks[d]-ranks.get(d+1,0))

def encode_residual(n,nbr,rset):
    vs=[v for v in range(n) if rset>>v&1]
    m=len(vs); e=0
    for bit,(i,j) in enumerate(combinations(range(m),2)):
        if nbr[vs[i]]>>vs[j]&1: e|=1<<bit
    return m,e

def violations(n,nbr):
    allmask=(1<<n)-1
    independent=[]; mis_sizes=set()
    for s in range(1,1<<n):
        if any((nbr[v]&s) for v in range(n) if s>>v&1): continue
        independent.append(s)
        dominated=s
        for v in range(n):
            if s>>v&1: dominated|=nbr[v]
        if dominated==allmask:mis_sizes.add(s.bit_count())
    for s in independent:
        q=s.bit_count()
        dominated=s
        for v in range(n):
            if s>>v&1: dominated|=nbr[v]
        remaining=allmask^dominated
        k,code=encode_residual(n,nbr,remaining)
        for j,betti in reduced_betti(k,code):
            p=q+j+1
            if betti and p>=1 and p not in mis_sizes:
                return dict(U=tuple(i for i in range(n) if s>>i&1),p=p,q=q,j=j,betti=betti,mis_sizes=sorted(mis_sizes),R=(k,code))
    return None

def graph_edges(n,mask):
    pool=list(combinations(range(n),2))
    return [pool[i] for i in range(len(pool)) if mask>>i&1]

def template(m):
    edges=[(0,1),(1,2),(2,3),(3,0)] + [(0,4)] + [(v,v+1) for v in range(4,3*m+3)]
    return bit_graph(4+3*m,edges)

def labeled_template_masks():
    n=7
    e=[(0,1),(1,2),(2,3),(3,0),(0,4),(4,5),(5,6)]
    pool=list(combinations(range(n),2)); imap={v:k for k,v in enumerate(pool)}
    ans=set()
    for perm in permutations(range(n)):
        z=0
        for a,b in e:
            z|=1<<imap[tuple(sorted((perm[a],perm[b])))]
        ans.add(z)
    return ans

def main():
    for m in range(1,5):
        n=4+3*m
        nbr=template(m)
        ind=[]
        for s in range(1,1<<n):
            if all(not(nbr[v]&s) for v in range(n) if s>>v&1):
                dom=s
                for v in range(n):
                    if s>>v&1:dom|=nbr[v]
                if dom==(1<<n)-1:ind.append(s.bit_count())
        assert min(ind)==m+2,(m,min(ind))
        U=sum(1<<(3*j+5) for j in range(m))
        dom=U
        for v in range(n):
            if U>>v&1:dom|=nbr[v]
        assert ((1<<n)-1)^dom == 15
        cycle_code=sum(1<<i for i,e in enumerate(combinations(range(4),2)) if e in {(0,1),(1,2),(2,3),(0,3)})
        assert reduced_betti(4,cycle_code)==((0,1),)
    print('FAMILY_CHECK_OK')
    counts={};bad={}
    for n in range(3,8):
        pool=list(combinations(range(n),2));ct=0;bads={}
        for selection in combinations(range(len(pool)),n):
            es=[pool[i] for i in selection]
            if not connected(n,es):continue
            ct+=1
            nbr=bit_graph(n,es)
            hit=violations(n,nbr)
            if hit:
                z=sum(1<<i for i in selection)
                bads[z]=hit
        counts[n]=ct;bad[n]=len(bads)
        print('ORDER',n,'unicyclic_labeled',ct,'failures',len(bads),flush=True)
        if n<7: assert not bads
        else:
            target=labeled_template_masks()
            print('template masks',len(target),'failure symmetric difference',len(set(bads)^target))
            assert len(target)==2520 and set(bads)==target
            example=next(iter(bads.items()))
            print('EXAMPLE',example,flush=True)
    assert reduced_betti(4,sum(1<<i for i,e in enumerate(combinations(range(4),2)) if e in {(0,1),(1,2),(2,3),(0,3)}))==((0,1),)
    print('COUNTS',counts,'FAILURES',bad)
    print('VERIFY_OK')
if __name__=='__main__':main()
